from django.test import TestCase, Client


class TestHome(TestCase):
    def test_open_homepage_should_be_success(self): # expected success
        c = Client()
        response = c.get("http://127.0.0.1:8000/")
        assert response.status_code == 200

    def test_post_homepage_should_return_405(self): # expected fail
        c = Client()
        response = c.post("http://127.0.0.1:8000/")
        assert response.status_code == 405


class TestRestCreate(TestCase):
    def test_should_allow_only_get(self):
        c = Client()
        response = c.post("http://127.0.0.1:8000/") # expected fail
        assert response.status_code == 405
        response = c.put("http://127.0.0.1:8000/") # expected fail
        assert response.status_code == 405
        response = c.delete("http://127.0.0.1:8000/") # expected fail
        assert response.status_code == 405
        response = c.patch("http://127.0.0.1:8000/") # expected fail
        assert response.status_code == 405


class TestRestaurantCreate(TestCase):
    def test_create_restaurant_should_be_success(self): # expected success
        c = Client()
        response = c.post("http://127.0.0.1:8000/for_test/",
                          data={
                              "name": "asd"
                            })
        assert response.status_code == 201


class TestCreateUser(TestCase):
    def test_create_user_should_be_success(self):
        c = Client()
        response = c.post("http://127.0.0.1:8000/auth/registration/",
                          data={
                              "email": "asdqwerty2387y2836@gmail.com",
                              "password": "asd12asd234",
                              "confirm_password": "asd12asd234",
                            })
        assert response.status_code == 200



