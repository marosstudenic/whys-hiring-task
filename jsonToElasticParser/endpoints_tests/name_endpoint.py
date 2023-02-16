import json
from jsonToElasticParser.models import Model
from rest_framework.test import APITestCase


class ModelNameTestCase(APITestCase):
    def setUp(self):
        Model.objects.create(name="TestModels", content={"test": "test"})
        Model.objects.create(name="TestModels", content={"test": "test2"})

    def test_retrieve_models_by_api(self):
        """general api test"""
        response = self.client.get('/detail/TestModels')
        self.assertTrue(len(response.data) == 2)
        self.assertTrue(response.data[0]['name']=='TestModels')
        self.assertTrue(json.dumps(response.data[0]['content'])=='{"test": "test"}')
        self.assertTrue(json.dumps(response.data[1]['content'])=='{"test": "test2"}')

    def test_filter_models_api(self):
        response = self.client.get('/detail/TestModels?test=test2')
        self.assertTrue(len(response.data) == 1)
        self.assertTrue(response.data[0]['name'] == 'TestModels')
        self.assertTrue(json.dumps(response.data[0]['content']) == '{"test": "test2"}')
