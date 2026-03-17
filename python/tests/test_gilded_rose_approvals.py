import io
import sys
import unittest
from pathlib import Path

# Add parent directory to path so we can import texttest_fixture.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from texttest_fixture import main


class GildedRoseApprovalTest(unittest.TestCase):
    def test_gilded_rose_approvals(self):
        approved_path = (
            Path(__file__).resolve().parent
            / "approved_files"
            / "test_gilded_rose_approvals.test_gilded_rose_approvals.approved.txt"
        )

        original_stdout = sys.stdout
        original_argv = sys.argv

        try:
            fake_stdout = io.StringIO()
            sys.stdout = fake_stdout
            sys.argv = ["texttest_fixture.py", "30"]
            main()
            actual_output = fake_stdout.getvalue()
        finally:
            sys.stdout = original_stdout
            sys.argv = original_argv

        expected_output = approved_path.read_text(encoding="utf-8")
        self.assertMultiLineEqual(expected_output, actual_output)


if __name__ == "__main__":
    unittest.main()
