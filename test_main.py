import unittest
import os
from main import makesave

class TestMain(unittest.TestCase):

    def setUp(self):
        # Set up the test environment
        os.makedirs("Saves/existing_save", exist_ok=True)

    def tearDown(self):
        # Clean up test directories
        if os.path.exists("Saves/test_save"):
            os.rmdir("Saves/test_save")
        if os.path.exists("Saves/existing_save"):
            os.rmdir("Saves/existing_save")

    def test_makesave_success(self):
        save_name = "test_save"
        result = makesave(save_name)
        self.assertEqual(result, "Success")

    def test_makesave_failure(self):
        save_name = "existing_save"
        result = makesave(save_name)
        self.assertEqual(result, "Save Creation Failed")

if __name__ == '__main__':
    unittest.main()
