import unittest
from app import RequestHandler
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import db

class TestApp(unittest.TestCase):
    def setUp(self):
        self.handler = RequestHandler

    def test_get_properties(self):
        # Simula una solicitud GET a la ruta /properties
        pass

    def test_like_property(self):
        # Simula una solicitud POST a la ruta /like
        pass

if __name__ == '__main__':
    unittest.main()
