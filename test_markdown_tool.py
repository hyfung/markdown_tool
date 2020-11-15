import unittest
import markdown_tool

class TestMarkdownTool(unittest.TestCase):

    def test_leftpad(self):
        """
        """

        self.assertEqual(markdown_tool.leftpad("abc", 5), "  abc")
        self.assertEqual(markdown_tool.leftpad("111", 5, '0'), "00111")
        self.assertEqual(markdown_tool.leftpad("hellworld", 5), "hellworld")

    def test_rightpad(self):
        """
        """
        self.assertEqual(markdown_tool.rightpad("abc", 5), "abc  ")
        self.assertEqual(markdown_tool.rightpad("hellworld", 5), "hellworld")

    def test_get_max_len(self):
        """
        """
        my_list = ["abc", "helloworld", "12345"]
        self.assertEqual(markdown_tool.get_max_len(my_list), 10)

    def test_find_all_titles(self):
        """
        """
        # self.assertEqual()

if __name__ == '__main__':
    unittest.main()
