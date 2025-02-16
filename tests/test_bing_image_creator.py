import unittest
from bing_image_creator import BingImageCreator

class TestBingImageCreator(unittest.TestCase):
    def test_initialization(self):
        creator = BingImageCreator(cookies=["test_cookie"])
        self.assertEqual(creator.cookies, ["test_cookie"])

    def test_empty_cookies(self):
        with self.assertRaises(ValueError):
            creator = BingImageCreator()

if __name__ == '__main__':
    unittest.main()