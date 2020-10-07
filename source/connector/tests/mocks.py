
class MockResponse:
    def __init__(self, *args, **kwargs):
        self.json_data = kwargs.get('json_data')
        self.status_code = kwargs.get('status_code')
    
    def json(self):
        return self.json_data