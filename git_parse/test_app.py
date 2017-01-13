import unittest

from git_parse import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.a = app.App("")

    def test_initialise(self):
        self.assertIsNotNone(self.a)

    def test_dataisset(self):
        self.assertEqual(self.a.data, "")

    def test_grok(self):
        self.assertIsNone(self.a.grok())
