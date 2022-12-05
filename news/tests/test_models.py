from django.test import TestCase

from news.models import Topic, Newspaper


def sample_topic(name):
    return Topic.objects.create(name=name)


class ModelTests(TestCase):
    def test_topic_str(self):
        name = "Test"
        topic = sample_topic(name)

        self.assertEqual(str(topic), name)

    def test_newspaper_str(self):
        newspaper_name = "Test"
        newspaper = Newspaper.objects.create(
            title=newspaper_name,
            content="",
            topic=sample_topic("Topic_name")
        )

        self.assertEqual(str(newspaper), newspaper_name)
