from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from .models import Article, Publisher, User


class ArticleAPITests(TestCase):
    def setUp(self):
        # Publisher + journalist
        self.publisher = Publisher.objects.create(name="Daily Post")

        self.journalist = User.objects.create_user(
            username="journalist_test",
            password="pass12345!",
            role=User.Role.JOURNALIST,
            email="journalist@test.com",
        )

        # API client user (reader)
        self.reader = User.objects.create_user(
            username="reader_test",
            password="pass12345!",
            role=User.Role.READER,
            email="reader@test.com",
        )

        # Reader subscriptions
        self.reader.subscribed_publishers.add(self.publisher)
        self.reader.subscribed_journalists.add(self.journalist)

        # Articles (approved + unapproved)
        self.approved_pub_article = Article.objects.create(
            title="Approved Publisher Article",
            content="Approved content",
            publisher=self.publisher,
            journalist=self.journalist,
            approved=True,
        )

        self.unapproved_pub_article = Article.objects.create(
            title="Unapproved Publisher Article",
            content="Draft content",
            publisher=self.publisher,
            journalist=self.journalist,
            approved=False,
        )

        self.approved_journalist_article = Article.objects.create(
            title="Approved Journalist Article",
            content="Approved independent content",
            journalist=self.journalist,
            approved=True,
        )

        self.client = APIClient()
        self.client.login(username="reader_test", password="pass12345!")

    def test_publisher_articles_returns_only_approved(self):
        url = reverse("publisher-articles", kwargs={"publisher_id": self.publisher.id})
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        titles = [item["title"] for item in res.json()]

        self.assertIn("Approved Publisher Article", titles)
        self.assertNotIn("Unapproved Publisher Article", titles)

    def test_journalist_articles_returns_only_approved(self):
        url = reverse("journalist-articles", kwargs={"journalist_id": self.journalist.id})
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        titles = [item["title"] for item in res.json()]

        self.assertIn("Approved Journalist Article", titles)

    def test_requires_authentication(self):
        anon = APIClient()
        url = reverse("publisher-articles", kwargs={"publisher_id": self.publisher.id})
        res = anon.get(url)

        # Session/Basic auth should block anonymous access
        self.assertIn(res.status_code, (401, 403))
