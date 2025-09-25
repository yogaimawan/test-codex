import io
import unittest
from contextlib import redirect_stdout

import hello


class HelloWorldTestCase(unittest.TestCase):
    def test_hello_world_prints_expected_greeting(self) -> None:
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            hello.hello_world("Budi")
        self.assertEqual(buffer.getvalue().strip(), "Hello, Budi dari Codex!")


if __name__ == "__main__":
    unittest.main()
