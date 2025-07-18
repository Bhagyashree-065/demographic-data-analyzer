import pandas as pd
import unittest
from demographic_data_analyzer import calculate_demographic_data
class TestDemographicDataAnalyzer(unittest.TestCase):
    def test_output_structure(self):
        result = calculate_demographic_data(print_data=False)
        
        # Check that result is a dictionary
        self.assertIsInstance(result, dict)

        # Check that all expected keys are present
        expected_keys = [
            'race_count',
            'average_age_men',
            'percentage_bachelors',
            'higher_education_rich',
            'lower_education_rich',
            'min_work_hours',
            'rich_percentage',
            'highest_earning_country',
            'highest_earning_country_percentage',
            'top_IN_occupation'
        ]
        for key in expected_keys:
            self.assertIn(key, result)

        # Check types of some key values
        self.assertIsInstance(result['race_count'], pd.Series)
        self.assertIsInstance(result['average_age_men'], float)
        self.assertIsInstance(result['highest_earning_country'], str)

if __name__ == '__main__':
   unittest.main()