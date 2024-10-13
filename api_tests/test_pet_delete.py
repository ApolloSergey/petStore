import copy

from entities_stubs.pet import PET_BODY
from enums.urls import URL
from utils.base_pet_api_test import BasePetApiTest
from utils.helpers.fake_data_provider import fake
from utils.helpers.verify import Verify


class TestDeletePet(BasePetApiTest):
    """
    Verify deletion of  entity on delete endpoint
    """

    def test_pet_delete_positive(self):
        api_url = self.api_data.pet_url
        pet_body = copy.deepcopy(PET_BODY)
        pet_body["id"] = int(fake.number_n_digits())
        pet_body["name"] = fake.words_combination()

        response = self.api_data.api_request(
            api_url=api_url,
            request_type="post",
            endpoint=URL.pet.value,
            body=pet_body
        )
        Verify.equals(response.status_code, 200, "Wrong status status code")
        response = self.api_data.api_request(
            api_url=api_url,
            request_type="delete",
            entity_id=pet_body["id"],
            endpoint=URL.pet.value,
        )
        Verify.equals(response.status_code, 200, "Wrong status status code")
        response = self.api_data.api_request(
            api_url=api_url,
            request_type="get",
            entity_id=pet_body["id"],
            endpoint=URL.pet.value,
        )
        Verify.equals(response.status_code, 404, "Wrong status status code")