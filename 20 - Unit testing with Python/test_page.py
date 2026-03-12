from unittest import TestCase
from unittest.mock import patch
from page import PageReq


class TestPageReq(TestCase):
    def setUp(self):
        self.page = PageReq("https://www.google.com")

    def test_make_req(self):
        with patch("requests.get") as mocked_get:
            self.page.get()
            mocked_get.assert_called()

    def test_content_returned(self):
        fake_response = "Hello"

        class FakeRes:
            def __init__(self):
                self.content = fake_response

        with patch("requests.get", return_value=FakeRes()) as mocked_get:
            self.assertEqual(self.page.get(), fake_response)
