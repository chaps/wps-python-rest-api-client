


class ItemsEndpoints:

    def get_items(self, items=[], *args, **kwargs):
        uri = self.build_uri(
            EndpointsEnums.ITEMS
        )
        if items:
            uri = "/".join(EndpointsEnums.ITEMS, items, )
        return requests.get(
            uri,   
            headers=self.get_headers()
        ).json()


    def get_item(self, item_id, *args, **kwargs):
        return requests.get(
            "{}/{}".format(
                self.build_uri(EndpointsEnums.ITEMS),
                item_id
            ),
            headers=self.get_headers()
        ).json()


    def get_item_attributevalues(self, item_id):
        return requests.get(
            self.build_uri(
                "{}/{}/{}".format(
                    EndpointsEnums.ITEMS,
                    item_id,
                    EndpointsEnums.ATTRIBUTEVALUES,
                ),
                headers=self.get_headers()
            )
        ).json()
    
    def get_item_country(self, item_id):
        return requests.get(
            self.build_uri(
                "{}/{}/{}".format(
                    EndpointsEnums.ITEMS,
                    item_id,
                    EndpointsEnums.COUNTRY,
                ),
                headers=self.get_headers()
            )
        ).json()


    def get_item_images(self, item_id):
        return requests.get(
            self.build_uri(
                "{}/{}/{}".format(
                    EndpointsEnums.ITEMS,
                    item_id,
                    EndpointsEnums.IMAGES,
                ),
                headers=self.get_headers()
            )
        ).json()


    def get_item_product(self, item_id):
        return requests.get(
            self.build_uri(
                "{}/{}/{}".format(
                    EndpointsEnums.ITEMS,
                    item_id,
                    EndpointsEnums.PRODUCT,
                ),
            headers=self.get_headers()
            )
        ).json()
    
    def get_item_quantities(self, item_id):
        return requests.get(
            self.build_uri(
                "{}/{}/{}".format(
                    EndpointsEnums.ITEMS,
                    item_id,
                    EndpointsEnums.QUANTITIES,
                ),
            headers=self.get_headers()
            )
        ).json()

    def get_item_tags(self, item_id):
        return requests.get(
            self.build_uri(
                "{}/{}/{}".format(
                    EndpointsEnums.ITEMS,
                    item_id,
                    EndpointsEnums.TAGS,
                ),
            headers=self.get_headers()
            )
        ).json()

    def get_item_taxonomyterms(self, item_id):
        return requests.get(
            self.build_uri(
                "{}/{}/{}".format(
                    EndpointsEnums.ITEMS,
                    item_id,
                    EndpointsEnums.TAXONOMYTERMS,
                ),
            headers=self.get_headers()
            )
        ).json()