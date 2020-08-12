import unittest

from track_gps.exception_logger import catch_any_exception_and_log_it


@catch_any_exception_and_log_it
def raise_file_exists_error():
    raise FileExistsError("Some smart message")


@catch_any_exception_and_log_it
def divide_first_by_second(first, second, third=None):
    return first / second


class TestZeroDivisionError(unittest.TestCase):
    def test_save_usage(self):
        self.assertEqual(1, divide_first_by_second(1, 1))

    def test_no_kwargs(self):
        with self.assertLogs() as cm:
            divide_first_by_second(1, 0)
        self.assertEqual(cm.output, ["ERROR:track_gps.exception_logger:Caught ZeroDivisionError while trying "
                                     "'divide_first_by_second(1, 0)'. Message: division by zero."])

    def test_with_kwargs(self):
        with self.assertLogs() as cm:
            divide_first_by_second(1, 0, third=2)
        self.assertEqual(cm.output, ["ERROR:track_gps.exception_logger:Caught ZeroDivisionError while trying "
                                     "'divide_first_by_second(1, 0, third=2)'. Message: division by zero."])


class TestErrorWithMessage(unittest.TestCase):
    def test_message_from_file_exists_error(self):
        with self.assertLogs() as cm:
            raise_file_exists_error()
        self.assertEqual(cm.output, ["ERROR:track_gps.exception_logger:Caught FileExistsError while trying "
                                     "'raise_file_exists_error()'. Message: Some smart message."])
