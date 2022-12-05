from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.test import TestCase
from django.urls import reverse

from news.models import Topic, Newspaper


HOME_PAGE_URL = reverse("news:index")
TOPIC_PAGE_URL = reverse("news:topic-list")
REDACTOR_LIST_URL = reverse("news:redactor-list")
NEWSPAPER_LIST_URL = reverse("news:newspaper-list")


def setup_for_tests():
    topic1 = Topic.objects.create(name="Test1")
    topic2 = Topic.objects.create(name="Test2")

    redactor1 = get_user_model().objects.create_user(
        username="Test_user1", password="test1234"
    )
    redactor2 = get_user_model().objects.create_user(
        username="Test_user2", password="test1234"
    )

    newspaper1 = Newspaper.objects.create(
        title="Test1", content="empty", topic=topic1
    )
    newspaper2 = Newspaper.objects.create(
        title="Test2", content="empty", topic=topic2
    )

    newspaper1.publishers.add(redactor1)
    newspaper1.save()
    newspaper2.publishers.add(redactor2)
    newspaper2.save()


class PublicTests(TestCase):
    def setUp(self) -> None:
        setup_for_tests()

    def test_unauthorized_user_can_see_all_list_page(self):
        for page in [
            HOME_PAGE_URL,
            TOPIC_PAGE_URL,
            REDACTOR_LIST_URL,
            NEWSPAPER_LIST_URL,
        ]:
            response = self.client.get(page)

            self.assertEqual(response.status_code, 200)

    def test_unauthorized_cant_create_or_retrieve_objects(self):
        for pages in [
            reverse("news:topic-create"),
            reverse("news:newspaper-create"),
            reverse("news:topic-detail", args=[1]),
            reverse("news:redactor-detail", args=[1]),
            reverse("news:newspaper-detail", args=[1]),
        ]:
            response = self.client.get(pages)

            self.assertNotEqual(response.status_code, 200)


class TopicTests(TestCase):
    def setUp(self) -> None:
        setup_for_tests()
        self.user = get_user_model().objects.create_user(
            username="Test_user", password="test12345"
        )
        self.client.force_login(self.user)

    def test_topic_update(self):
        topic = Topic.objects.create(name="TestName1")

        self.client.post(
            reverse("news:topic-update", args=[topic.id]),
            data={"name": "TestName2"},
        )

        topic.refresh_from_db()

        self.assertEqual(topic.name, "TestName2")

    def test_topic_search_filter(self):
        response = self.client.get(TOPIC_PAGE_URL + "?title=Test1")

        self.assertEqual(
            list(response.context["topic_list"]),
            list(Topic.objects.filter(name__icontains="Test1")),
        )

    def test_topic_create(self):
        self.client.post(reverse("news:topic-create"), {"name": "test_name23"})

        self.assertEqual(Topic.objects.count(), 3)
        self.assertEqual(Topic.objects.filter(name="test_name23").count(), 1)


class NewspaperTests(TestCase):
    def setUp(self) -> None:
        setup_for_tests()
        self.user = get_user_model().objects.create_user(
            username="Test_user", password="test12345"
        )
        self.client.force_login(self.user)

    def test_newspapers_list(self):
        response = self.client.get(NEWSPAPER_LIST_URL)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["newspaper_list"]),
            list(Newspaper.objects.all()),
        )

    def test_newspaper_detail_page(self):
        response = self.client.get(reverse("news:newspaper-detail", args=[1]))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context_data["newspaper"], Newspaper.objects.get(id=1)
        )

    def test_newspaper_search_filter(self):
        response = self.client.get(NEWSPAPER_LIST_URL + "?title=Test1")

        self.assertEqual(
            list(response.context["newspaper_list"]),
            list(Newspaper.objects.filter(title__icontains="Test1")),
        )


class RedactorTests(TestCase):
    def setUp(self) -> None:
        setup_for_tests()
        self.user = get_user_model().objects.create_user(
            username="Test_user", password="test12345"
        )
        self.client.force_login(self.user)

    def test_redactor_list(self):
        response = self.client.get(REDACTOR_LIST_URL)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["redactor_list"]),
            list(get_user_model().objects.all()),
        )

    def test_redactor_detail_page(self):
        response = self.client.get(
            reverse("news:redactor-detail", args=[self.user.id])
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context_data["redactor"],
            get_user_model().objects.get(id=self.user.id),
        )

    def test_redactor_create(self):
        payload = {
            "username": "Test_user123",
            "password1": "testpassword",
            "password2": "testpassword",
            "first_name": "Test_name",
            "last_name": "Test_surname",
        }

        self.client.post(reverse("news:redactor-create"), payload)
        user = get_object_or_404(get_user_model(), username="Test_user123")

        self.assertEqual(payload["first_name"], user.first_name)
        self.assertEqual(payload["last_name"], user.last_name)

    def test_redactor_search_filter(self):
        response = self.client.get(REDACTOR_LIST_URL + "?username=user1")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context_data["redactor_list"]),
            list(get_user_model().objects.filter(username__icontains="user1")),
        )
