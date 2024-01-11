from django.test import SimpleTestCase

# Create your tests here.

class SimpleTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        # l8, refers to home path with an empty string, that is why
        # it represents ('/'), but if you add a name
        # to that path in the pages\urls.py, make sure to add a name
        # as well inside the ('/'), otherwise you'll get error 404 != 200

    def test_about_page_status_code(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)

        # l9, refers to the about path in in the pages/urls.py
        # do not remove slash, just add the name of the link
        # to avoid error 404 != 200

# SimpleTestCase is a test for system that do not have database, this is faster and lightweight
# TestCase is for system that has database
# thus we use SimpleTestCase since our program does not have database :)