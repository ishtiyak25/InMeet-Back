from django.test import Client, TestCase

guest_client = Client()


class StaticURLTests(TestCase):
    def setUp(self):
        self.guest_client = Client()

    def test_homepage(self):
        response = self.guest_client.get("/")
        assert response.status_code == 200
