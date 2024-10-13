import ast
import json
import requests
from utils.helpers.config_provider import settings_config
from utils.helpers.singleton import singleton


@singleton
class ApiDataProvider:

    def __init__(self):
        self.pet_url = settings_config["base_url"]

    def api_request(
        self,
        api_url,
        request_type="",
        endpoint="",
        body=None,
        entity_id=None,
        parameters="",
    ):
        response = ""
        if request_type == "post":
            response = requests.post(api_url + endpoint, json=body)
        if request_type == "get":
            if entity_id is None:
                response = requests.get(api_url + endpoint + parameters)
            else:
                test = api_url + endpoint + "/" + str(entity_id)
                response = requests.get(api_url + endpoint + "/" + str(entity_id))
        if request_type == "put":
            response = requests.put(api_url + endpoint, json=body)
        if request_type == "delete":
            response = requests.delete(api_url + endpoint + "/" + str(entity_id))
        return response

    def compare_request_and_response_content(self, request, response):
        list_results = []
        response_dict = ast.literal_eval(str(response))
        for key in request:
            if key in response:
                request_value = request[key]
                response_value = response_dict[key]
                list_results.append(request_value == response_value)
        return all(list_results)

    def compare_request_and_response_items(self, request, response):
        response_json = json.loads(response)
        if self.compare_request_and_response_content(request, response_json):
            return True
        return False


    def check_items_order_in_response(self, response, field_name, ascending=True):
        response_json = json.loads(response)
        dict_items = response_json["data"]
        list_original = []
        for item in dict_items:
            list_original.append(item[field_name])
        list_ordered = list_original[:]
        if ascending:
            list_ordered.sort(reverse=False)
        else:
            list_ordered.sort(reverse=True)
        return list_ordered == list_original

    def get_field_value(self, response, field_name):
        response_json = json.loads(response)
        return response_json[field_name]

    @staticmethod
    def verify_error_response_content(expected_error_message, response):
        return expected_error_message in response

    @staticmethod
    def get_entity_id_from_response(response):
        response_dict = ast.literal_eval(response)
        return response_dict["id"]

    @staticmethod
    def verify_error_response(response, status_code, error_message, error_type):
        result = [
            error_message in response.text,
            error_type in response.text,
            status_code == response.status_code,
        ]
        return all(result)
