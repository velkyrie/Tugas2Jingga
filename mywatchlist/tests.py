from django.test import TestCase, Client

# Create your tests here.
class TestMywatchlist(TestCase):
    def test_html(self):
        response = Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code,200)
    
    def test_json(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code,200)

    def test_xml(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)
