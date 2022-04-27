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


class TestClass:
    def test_get(self):
        response = requests.get("http://localhost:8000/api/v1/get")
        print(response)
        assert response.status_code==200
    def test_post(self):
        data_post = requests.post("http://localhost:8000/api/v1/post", data=json.dumps(test_data))
        assert data_post.status_code==200
