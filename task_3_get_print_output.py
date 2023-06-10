"""
Write a function that will receive a string and write it to stderr
if line starts with "error" and to the stdout otherwise.


>>> my_precious_logger("error: file not found")
# stderr
'error: file not found'


>>> my_precious_logger("OK")
# stdout
'OK'

Definition of done:
 - function is created
 - function is properly formatted
 - function has positive tests

You will learn:
 - how to write to stderr
 - how to test output to the stderr and stdout


"""
import io
import sys
import unittest


class TestMyPreciousLogger(unittest.TestCase):
    def test_stdout(self):
        # Redirect stdout to a buffer
        stdout_buffer = io.StringIO()
        sys.stdout = stdout_buffer
        # Call the function with a string that does not start with "error"
        my_precious_logger("OK")
        # Get the output from the buffer
        output = stdout_buffer.getvalue().strip()
        # Reset stdout
        sys.stdout = sys.__stdout__
        # Check if the output is correct
        self.assertEqual(output, "OK")

    def test_stderr(self):
        # Redirect stderr to a buffer
        stderr_buffer = io.StringIO()
        sys.stderr = stderr_buffer
        # Call the function with a string that starts with "error"
        my_precious_logger("error: file not found")
        # Get the output from the buffer
        output = stderr_buffer.getvalue().strip()
        # Reset stderr
        sys.stderr = sys.__stderr__
        # Check if the output is correct
        self.assertEqual(output, "error: file not found")


if __name__ == '__main__':
    unittest.main()
