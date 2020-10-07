from unittest.mock import patch

from source.connector.external_api_connector import ExternalApiConnector
from .mocks import MockResponse


class TestExternalApiConnector:
    """External-API connector tests class representation."""
    
    def setup(self, *args, **kwargs):
        """class setup."""
        self.connector = ExternalApiConnector()

    def teardown(self, *args, **kwargs):
        """class teardown."""
        pass

    @patch('source.connector.external_api_connector.requests')
    def test_get_data_from_connector_response(self, mocked_requests):
        """Test get_data_from_connector response.
        This function tests that the connector response to the
        'get_data_from_connector' matches the expected criteria.

        Expected criteria:

            {'shipping_options': [
                {
                    "name": "name",
                    "type": "type",
                    "cost": 6,
                    "estimated_days": 3
                }
            ]}

        """
        expect = {
            'shipping_options': [
                {
                    "name": "name",
                    "type": "type",
                    "cost": 6,
                    "estimated_days": 3
                }
            ]
        }
        mocked_requests.get.return_value = MockResponse(json_data=expect, 
                                                        tatus_code=200)
        response = self.connector.get_data_from_connector()
        assert expect == response

        