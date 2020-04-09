"""Main module."""
import requests

from .enums import EndpointsEnums
from .products_endpoints import ProductsEndpoints
from .items_endpoints import ItemsEndpoints


class WPSRestAPI(ProductsEndpoints, ItemsEndpoints):


    def __init__(self, token, host="http://api.wps-inc.com/"):
        self.token = token
        self.host = host


    def get_headers(self):
        """ Returns a dict of the min.
        required headers to perform an intended 
        request to WPS Rest API
        """
        return {
            "Authorization": f"Bearer {self.token}"
        }
    
    def build_uri(self, endpoint):
        """ Builds the URI 
        to be used under a request.
        """
        if self.host.endswith("/") and endpoint.startswith("/"):
            return "{}{}".format(self.host, endpoint[1:])
        if (not self.host.endswith("/")) and (not endpoint.startswith("/")):
            return "{}/{}".format(self.host, endpoint)
        return "{}{}".format(self.host, endpoint)
