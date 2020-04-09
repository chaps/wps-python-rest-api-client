import requests
from .enums import EndpointsEnums


class ProductsEndpoints:

    def get_products(self, products=[], *args, **kwargs):
        uri = self.build_uri(
            EndpointsEnums.PRODUCTS.value
        )
        if products:
            uri = "/".join(
                EndpointsEnums.PRODUCTS.value, products
            )
        return requests.get(
            uri,   
            headers=self.get_headers()
        )

    def get_product(self, product_id, *args, **kwargs):
        return requests.get(
            "{}/{}".format(
                self.build_uri(EndpointsEnums.PRODUCTS.value),
                product_id
            ),
            headers=self.get_headers()
        )

    def get_product_attributekeys(self, product_id):
        return requests.get(
            self.build_uri(
                "{}/{}/{}".format(
                    EndpointsEnums.PRODUCTS.value,
                    product_id,
                    EndpointsEnums.ATTRIBUTEKEYS.value,
                ),
                headers=self.get_headers()
            )
        )
    
    def get_product_attributevalues(self, product_id):
        return requests.get(
            self.build_uri(
                "{}/{}/{}".format(
                    EndpointsEnums.PRODUCTS.value,
                    product_id,
                    EndpointsEnums.ATTRIBUTEVALUES.value,
                ),
                headers=self.get_headers()
            )
        )
    
    def get_product_blocks(self, product_id):
        return requests.get(
            self.build_uri(
                "{}/{}/{}".format(
                    EndpointsEnums.PRODUCTS.value,
                    product_id,
                    EndpointsEnums.BLOCKS.value,
                ),
                headers=self.get_headers()
            )
        )

        pass
    
    def get_product_features(self, product_id):
        return requests.get(
            self.build_uri(
                "{}/{}/{}".format(
                    EndpointsEnums.PRODUCTS.value,
                    product_id,
                    EndpointsEnums.FEATURES.value,
                ),
                headers=self.get_headers()
            )
        )


    def get_product_images(self, product_id):
        return requests.get(
            self.build_uri(
                "{}/{}/{}".format(
                    EndpointsEnums.PRODUCTS.value,
                    product_id,
                    EndpointsEnums.IMAGES.value,
                ),
                headers=self.get_headers()
            )
        )


    def get_product_items(self, product_id):
        return requests.get(
            self.build_uri(
                "{}/{}/{}".format(
                    EndpointsEnums.PRODUCTS.value,
                    product_id,
                    EndpointsEnums.ITEMS.value,
                ),
            headers=self.get_headers()
            )
        )
    
    def get_product_resources(self, product_id):
        return requests.get(
            self.build_uri(
                "{}/{}/{}".format(
                    EndpointsEnums.PRODUCTS.value,
                    product_id,
                    EndpointsEnums.RESOURCES.value,
                ),
            headers=self.get_headers()
            )
        )

    def get_product_tags(self, product_id):
        return requests.get(
            self.build_uri(
                "{}/{}/{}".format(
                    EndpointsEnums.PRODUCTS.value,
                    product_id,
                    EndpointsEnums.TAGS.value,
                ),
            headers=self.get_headers()
            )
        )

    def get_product_taxonomyterms(self, product_id):
        return requests.get(
            self.build_uri(
                "{}/{}/{}".format(
                    EndpointsEnums.PRODUCTS.value,
                    product_id,
                    EndpointsEnums.TAXONOMYTERMS.value,
                ),
            headers=self.get_headers()
            )
        )