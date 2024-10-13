import base64
import json


class CommonActions:

    @staticmethod
    def parse_json(json_data):
        if isinstance(json_data, bytes):
            json_data = str(json_data, "utf8")
        try:
            return json.loads(json_data)
        except json.JSONDecodeError:
            return json.loads(json_data.replace("'", '"'))

    @staticmethod
    def find_list_in_nested_list(list_original, nested_list):
        for list_item in nested_list:
            if list_item == list_original:
                return True
        return False

    @staticmethod
    def is_list_contains_sublist(list_items, sublist_items):
        return [element for element in list_items if element in sublist_items] == [
            element for element in sublist_items if element in list_items
        ]

    @staticmethod
    def is_string_contains_list_items(text_string, list_items):
        return any(ext in text_string for ext in list_items)

    @staticmethod
    def convert_string_to_dict(string):
        return json.loads(string)


