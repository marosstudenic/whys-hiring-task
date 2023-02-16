import json

from rest_framework.test import APITestCase

from jsonToElasticParser.models import Model


class ModelNameIdTestCase(APITestCase):

    def setUp(self):
        Model.objects.create(name="TestModel", content={"test": "test", "id": 1})
        Model.objects.create(name="TestModel", content={"test": "test2", "id:": 2})
        Model.objects.create(name="TestModel", content={"test": "test3", "id:": 2})

    def test_retrieve_models_by_api(self):
        """Test whether we got same content as we saved"""
        response = self.client.get('/detail/TestModel/1')
        self.assertTrue(len(response.data) == 1)
        self.assertTrue(response.data[0]['name']=='TestModel')
        self.assertTrue(json.dumps(response.data[0]['content'])=='{"id": 1, "test": "test"}')

    def test_filter_no_records(self):
        response = self.client.get('/detail/TestModel/1?test=test2')
        self.assertTrue(len(response.data) == 0)

    def test_filter_one_record(self):
        response = self.client.get('/detail/TestModel/2?test=test2')
        self.assertTrue(len(response.data) == 0)
