import requests
import json

from utils import extract_data_by_property_name
from utils import assert_array_by_value
from test_data import UserData
from test_data import CreatedUser
from test_data import DeletedUser
from test_data import RegisterUser
import unittest

url_list_users = "https://reqres.in/api/users?page=2"
url_user_not_found = "https://reqres.in/api/users/23"
url_create = "https://reqres.in/api/users"
url_update = "https://reqres.in/api/users/2"
url_delete = "https://reqres.in/api/users/2"
url_register = "https://reqres.in/api/register"


class TestReqresAPI(unittest.TestCase):
    def test_list_users(self):
        response = requests.get(url_list_users)
        assert response.status_code == 200
        data = (json.loads(response.text)).get('data')

        emails = extract_data_by_property_name(data, 'email')
        first_names = extract_data_by_property_name(data, 'first_name')
        last_names = extract_data_by_property_name(data, 'last_name')
        avatars = extract_data_by_property_name(data, 'avatar')

        assert_array_by_value(emails, UserData.emails)
        assert_array_by_value(first_names, UserData.first_names)
        assert_array_by_value(last_names, UserData.last_names)
        assert_array_by_value(avatars, UserData.avatars)

    def test_user_not_found(self):
        response = requests.get(url_user_not_found)
        assert response.status_code == 404

    def test_create_user(self):
        test_response = (requests.get(url_create)).json()
        assert 'name', 'job' in test_response != CreatedUser.user_name_job

        file = open('./create_a_user.json', 'r')
        user = json.loads(file.read())
        response = requests.post(url_create, user)
        assert response.status_code == 201
        assert 'name', 'job' in response.json() == CreatedUser.user_name_job
        file.close()

    def test_update_user(self):
        file = open('./create_a_user.json', 'r')
        request_json = json.loads(file.read())
        response = requests.put(url_update, request_json)
        assert response.status_code == 200
        assert 'name', 'job' in response.json() == CreatedUser.user_name_job
        file.close()

    def test_delete_user(self):
        response = requests.get(url_delete)
        data = (json.loads(response.text)).get('data')
        assert data == DeletedUser.deleted_user_data
        response_to_delete = requests.delete(url_delete)
        assert response_to_delete.status_code == 204
        assert response_to_delete != DeletedUser.deleted_user_data

    def test_register_successful_user(self):
        file = open('./register_successful_user.json', 'r')
        user = json.loads(file.read())
        response = requests.post(url_register, user)
        assert response.status_code == 200
        assert response.json() == RegisterUser.register_successful_data
        file.close()

    def test_register_unsuccessful_user(self):
        file = open('./register_unsuccessful_user.json', 'r')
        user = json.loads(file.read())
        response = requests.post(url_register, user)
        assert response.status_code == 400
        assert response.json() == RegisterUser.register_unsuccessful_data
        file.close()


