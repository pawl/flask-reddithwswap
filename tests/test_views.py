import unittest
from unittest.mock import patch

from heckingoodboys import app


class TestViews(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    @patch('heckingoodboys.views.get_media')
    def test_index(self, mock_get_media):
        mock_get_media.return_value = []
        rv = self.client.get('/')
        self.assertEqual(rv.status_code, 200)
