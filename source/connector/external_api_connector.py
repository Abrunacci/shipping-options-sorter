import requests

from config.environment import configurations

class ExternalApiConnector:
    """External API connector class representation."""


    def __init__(self, *args, **kwargs):
        """class initialization."""
        self.url = configurations.get('EXTERNAL_API_URL')

    def execute_call(self, endpoint:str, method:str):
        """Execute call.
        This functions execute the request call to obtain the
        data from external api.
        
        Arguments:
            endpoint : str
                A string.
            method : str
                The method
        Returns:
            response : dict
                The response from requests
        """
        
        methods = {
            'get': requests.get
        }
        headers = None
        params = None
        response = None
        if method in methods.keys():
            response = methods.get(method)(endpoint)
        else:
            raise Exception
        return response.json()

    def get_data_from_connector(self):
        """..."""
        data = self.execute_call(endpoint=self.url, method='get')
        return data