# ------------------------------------------------------------------------------- #
# Title: Test Processing Classes Module
# # Description: A collection of tests for the processing classes module
# ChangeLog: (Who, When, What)
# JWidner,24aug2024,Created Script
# ------------------------------------------------------------------------------- #

import unittest
import tempfile
import json
from data_classes import Employee
from processing_classes import FileProcessor


class TestFileProcessor(unittest.TestCase):

    def setUp(self):
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name
        self.employee_data = []

    def tearDown(self):
        # Clean up and delete the temporary file
        self.temp_file.close()

    def test_read_data_from_file(self):
        # Create some sample data and write it to the temporary file
        sample_data: list = [
            {"FirstName": "John", "LastName": "Doe", "ReviewDate": "2024-08-17", "ReviewRating": 3},
            {"FirstName": "Alice", "LastName": "Smith", "ReviewDate": "2024-09-25", "ReviewRating": 4},
        ]
        with open(self.temp_file_name, "w") as file:
            json.dump(sample_data, file)

        # Call the read_data_from_file method and check if it returns the expected data
        employees: list = FileProcessor.read_employee_data_from_file(self.temp_file_name, self.employee_data, Employee)

        # Assert that the employee_data list contains the expected employee objects
        self.assertEqual(len(employees), len(sample_data))
        self.assertEqual(employees[0].first_name, sample_data[0]["FirstName"])
        self.assertEqual(employees[1].review_rating, sample_data[1]["ReviewRating"])


if __name__ == "__main__":
    unittest.main()
