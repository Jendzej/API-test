import json
from urllib import response
import requests

test_data = {
    "first_name":"Test",
    "last_name":"Test",
    "middle_name":"Test",
    "gender":"male",
    "roles":["admin"]
}
update_data = {
    "first_name":"Update",
    "last_name":"Test",
    "middle_name":"Test",
    "gender":"male",
    "roles":["admin"]
}

user_id = []
class TestClass:

    def test_getting_user_data(self):
        response = requests.get("http://localhost:8000/api/v1/users")
        user_id.append(response.json()[-1]["py_id"])
        assert response.status_code==200


    def test_getting_one_user_data(self):
        response = requests.get(f"http://localhost:8000/api/v1/users/1/{user_id[0]}")
        assert response.status_code==200


    def test_inserting_user_data(self):
        data_post = requests.post("http://localhost:8000/api/v1/users", data=json.dumps(test_data))
        response = requests.get("http://localhost:8000/api/v1/users")
        user_id.append(response.json()[-1]["py_id"])
        assert data_post.status_code==200
    
    
    def test_updating_user_data(self):
        data_put = requests.put(f"http://localhost:8000/api/v1/users/1/{user_id[-1]}", data=json.dumps(test_data))
        assert data_put.status_code==200
    
    
    def test_deleting_user_data(self):
        data_delete = requests.delete(f"http://localhost:8000/api/v1/users/1/{user_id[-1]}")
        assert data_delete.status_code==200
