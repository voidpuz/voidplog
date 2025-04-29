from django.test import TestCase
from django.urls import reverse

from posts.models import Post


class PostsTests(TestCase):
    def test_post_list(self):
        response = self.client.get(reverse("post_list"))
        print(">>>", response)
        self.assertEqual(response.status_code, 200)

    def test_post_detail(self):
        response = self.client.get("127.0.0.1:8000/posts/1/")
        print(response)
        self.assertEqual(response.status_code, 200)