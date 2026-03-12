from unittest import TestCase
from printer import PrinterError, Printer


class TestPrinter(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.printer = Printer(2.0, 300)

    def test_print(self):
        printer = Printer(10, 100)
        self.assertEqual(printer.print(10), "Printed 10 pages in 1 seconds")
        with self.assertRaises(PrinterError):
            printer.print(101)

    def test_print_within_capacity(self):
        # printer = Printer(2.0, 300)
        msg = self.printer.print(25)
        self.assertEqual(f"Printed 25 pages in 12.50 seconds", msg)
        # with self.assertRaises(PrinterError):
        # printer.print(101)

    def test_print_outside_capacity(self):
        with self.assertRaises(PrinterError):
            self.printer.print(301)

    def test_print_exact_capacity(self):
        self.printer.print(self.printer._capacity)
        # with self.assertRaises(PrinterError):
        #     self.printer.print(301)

    def test_printer_speed(self):
        pages = 10
        expected_result = "Printed 10 pages in 5 seconds"
        result = self.printer.print(pages)
        self.assertEqual(result, expected_result)

    def test_speed_in_two_decimals(self):
        fast_printer = Printer(3.0, 300)
        pages = 11
        expected_result = "Printed 11 pages in 3.67 seconds"
        result = self.printer.print(pages)
        self.assertEqual(result, expected_result)

        result = fast_printer.print(pages)
        self.assertEqual(result, expected_result)

    def test_multiple_print_runs(self):
        self.printer.print(25)
        self.printer.print(50)
        self.printer.print(100)
        self.printer.print(225)

    def test_multiple_print_runs_endsup_error(self):
        self.printer.print(25)
        self.printer.print(50)
        self.printer.print(100)
        self.printer.print(225)

        with self.assertRaises(PrinterError):
            self.printer.print(1)
