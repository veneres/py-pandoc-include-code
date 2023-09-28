import unittest
from panflute import run_filter
from py_pandoc_include_code import action
import io


class TestSum(unittest.TestCase):

    def test_snippet_filet(self):
        test_file = open("resources/test.json", "r")
        output_res = io.StringIO()

        run_filter(action, input_stream=test_file, output_stream=output_res)

        res_lines = output_res.getvalue()
        output_res.close()
        test_file.close()

        with open("resources/expected_res.json", "r") as f:
            oracle = "".join(f.readlines())

        self.assertEqual(res_lines, oracle)

if __name__ == '__main__':
    unittest.main()