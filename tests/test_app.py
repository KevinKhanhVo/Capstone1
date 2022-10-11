import app
from unittest import TestCase
from flask import session

class APITestCase(TestCase):
    """Test that we receive correct APIs"""

    def test_pokemon_type(self):
        """ Test the pokemon type API. """

        # Test that we are able to get the fire's element weaknesses.
    def test_return_pokemon_weaknesses(self):
        self.assertEqual(app.return_pokemon_weaknesses('fire'), ['ground', 'rock', 'water'])


class ShowPageTestCase(TestCase):
    """ Test loading the home page. """

    def test_show_home_page(self):
        with app.app.test_client() as client:
            resp = client.get('/pokemon')
            
            self.assertEqual(resp.status_code, 200)

    def test_pokemon_list_page(self):
        with app.app.test_client() as client:
            resp = client.get('/pokemon/list')
            
            self.assertEqual(resp.status_code, 200)

class RedirectPokemonTestCase(TestCase):
    """ Test the / route to redirect. """

    def test_redirect(self):
        with app.app.test_client() as client:
            resp = client.get('/')

            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, "http://localhost/pokemon")

class SignUpGetTestCase(TestCase):
    """ Test /users/signup route GET Method. """

    def test_signup_get_method(self):
        with app.app.test_client() as client:
            resp = client.get('/users/signup')

            self.assertEqual(resp.status_code, 200)


class SignUpPostTestCase(TestCase):
    """ Test /users/signup route POST Method. """

    def test_signup_post_method(self):
        with app.app.test_client() as client:

            resp = client.post('/users/signup', data = {
                'trainer_name' : 'Rice',
                'username': 'trainer1',
                'password': 'trainer1',
                'img_url': 'rice.png'
            })

            self.assertEqual(resp.status_code, 200)

class LoginGetTestCase(TestCase):
    """ Test /users/login GET method. """

    def test_login_get_method(self):
        with app.app.test_client() as client:
            resp = client.get('/users/login')

            self.assertEqual(resp.status_code, 200)

class LoginPostTestCase(TestCase):
    """ Test /users/login GET method. """

    def test_login_post_method(self):
        with app.app.test_client() as client:
            resp = client.post('/users/login', data = {
                'username': 'trainer1',
                'password': 'trainer1'
            })

            self.assertEqual(resp.status_code, 200)

class LogoutTestCase(TestCase):
    """ Test /users/logout GET method. """

    def test_logout_route(self):
        with app.app.test_client() as client:
            resp = client.get('/users/logout')

            self.assertEqual(resp.status_code, 302)

class DeletePokemonTestCase(TestCase):
    """ Test /pokemon/delete route. """

    def test_delete_pokemon(self):
        with app.app.test_client() as client:
            resp = client.get('/pokemon/delete/1')

            self.assertEqual(resp.status_code, 302)

# class TestSessionTestCase(TestCase):
#     """ Test the trainer object saved in session. """

#     def test_session(self):
#         with app.app.test_client() as client:
#             with client.session_transaction() as sess:
#                 sess['count'] = 0

#             resp = client.get('/users/login')
#             self.assertEqual(resp.status_code, 302)
#             self.assertEqual(session['count', 1])