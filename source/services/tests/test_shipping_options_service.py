from unittest.mock import patch

from source.services.shipping_options import ExternalApiConnector
from source.services.shipping_options import ShippingOptions


class TestShippingOptionsService:

    def setup(self, *args, **kwargs):
        self.service = None

    def teardown(self, *args, **kwargs):
        pass

    @patch.object(ExternalApiConnector, 'execute_call')
    def test_get_shipping_opt_res_with_equals_costs_and_days(self, 
                                                             mocked_call):
        expect = [
            {"name":"Option 1","type":"Delivery","cost":10,"estimated_days":3},
            {"name":"Option 2","type":"Custom","cost":10,"estimated_days":3},
            {"name":"Option 3","type":"Pickup","cost":10,"estimated_days":3}    
        ]

        mocked_call.return_value = [
            {"name":"Option 1","type":"Delivery","cost":10,"estimated_days":3},
            {"name":"Option 2","type":"Custom","cost":10,"estimated_days":3},
            {"name":"Option 3","type":"Pickup","cost":10,"estimated_days":3}
        ]
        result = ShippingOptions.get_shipping_option()
        assert result == expect

    @patch.object(ExternalApiConnector, 'execute_call')
    def test_get_shipping_opt_res_with_equal_costs_and_diff_days(self, 
                                                                 mocked_call):
        expect =[
            {"name":"Option 2","type":"Custom","cost":10,"estimated_days":2},
            {"name":"Option 3","type":"Pickup","cost":10,"estimated_days":3},
            {"name":"Option 1","type":"Delivery","cost":10,"estimated_days":5}
        ]

        mocked_call.return_value = [
            {"name":"Option 2","type":"Custom","cost":10,"estimated_days":2},
            {"name":"Option 3","type":"Pickup","cost":10,"estimated_days":3},
            {"name":"Option 1","type":"Delivery","cost":10,"estimated_days":5}
        ]
        result = ShippingOptions.get_shipping_option()
        assert result == expect

    @patch.object(ExternalApiConnector, 'execute_call')
    def test_get_shipping_opt_res_with_diff_costs_and_equal_days(self,
                                                                 mocked_call):
        expect =[
            {"name":"Option 2","type":"Custom","cost":5,"estimated_days":3},
            {"name":"Option 1","type":"Delivery","cost":6,"estimated_days":3},
            {"name":"Option 3","type":"Pickup","cost":10,"estimated_days":3}
        ]

        mocked_call.return_value = [
            {"name":"Option 2","type":"Custom","cost":5,"estimated_days":3},
            {"name":"Option 1","type":"Delivery","cost":6,"estimated_days":3},
            {"name":"Option 3","type":"Pickup","cost":10,"estimated_days":3}
        ]
        result = ShippingOptions.get_shipping_option()
        assert result == expect


    @patch.object(ExternalApiConnector, 'execute_call')
    def test_get_shipping_opt_res_with_diff_costs_and_days(self, mocked_call):
        expect = [
            {"name":"Option 2","type":"Custom","cost":5,"estimated_days":3},
            {"name":"Option 3","type":"Pickup","cost":7,"estimated_days":2},
            {"name":"Option 1","type":"Delivery","cost":10,"estimated_days":5}
        ]

        mocked_call.return_value = [
            {"name":"Option 1","type":"Delivery","cost":10,"estimated_days":5},
            {"name":"Option 2","type":"Custom","cost":5,"estimated_days":3},
            {"name":"Option 3","type":"Pickup","cost":7,"estimated_days":2}
        ]
        result = ShippingOptions.get_shipping_option()
        assert result == expect

    @patch.object(ExternalApiConnector, 'execute_call')
    def test_get_shipping_opt_res_with_no_data(self, mocked_call):
        expect = []

        mocked_call.return_value = []
        result = ShippingOptions.get_shipping_option()
        assert result == expect