import unittest
from ggachi import fly

class GgachiTestCase(unittest.TestCase):
    def test_fly_to_google(self):
        result = fly(
            {
                "api_endpoint": "https://www.google.com/"
                , "method": "GET"
                , "expected_response_status_code": 200
            }
        )

        self.assertEqual(result['status'], 'ok')

if __name__ == '__main__':
    unittest.main()