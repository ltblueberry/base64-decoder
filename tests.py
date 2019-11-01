import unittest
import os
import imghdr
from base64decoder import main as script
from base64decoder import messages


class ScriptTest(unittest.TestCase):

    def test_input_empty(self):
        exit_message = script(None, "test_input_empty.none")
        self.assertEqual(exit_message, messages.NONE_INPUT)

    def test_input_not_found(self):
        inputFile = "nofile.txt"
        exit_message = script(inputFile, "test_input_not_found.none")
        self.assertEqual(exit_message, messages.FILE_NOT_FOUND.format(
            os.path.abspath(inputFile)))

    def test_output_empty(self):
        exit_message = script("text.b64", None)
        self.assertEqual(exit_message, messages.NONE_OUTPUT)

    def test_decode_text(self):
        outputFile = "result.txt"
        exit_message = script("text.b64", outputFile)
        if exit_message != messages.DONE:
            self.assertTrue(False)
            return
        if os.path.exists(outputFile) == False:
            self.assertTrue(False)
            return

        readFile = open(outputFile, "r")
        content = readFile.read()
        if content != "Hello World!":
            self.assertTrue(False)

    def test_decode_image(self):
        outputFile = "result.png"
        exit_message = script("image.b64", outputFile)
        if exit_message != messages.DONE:
            self.assertTrue(False)
            return
        if os.path.exists(outputFile) == False:
            self.assertTrue(False)
            return

        self.assertTrue(imghdr.what(outputFile), "png")


if __name__ == '__main__':
    unittest.main()
