from source.connector.external_api_connector import ExternalApiConnector


class ShippingOptions:

    @staticmethod
    def get_shipping_option():
        data = ExternalApiConnector().get_data_from_connector() 
        result = sorted(data, 
                        key=lambda x: (x.get('cost'), x.get('estimated_days')),
                        reverse=False)
        return result 