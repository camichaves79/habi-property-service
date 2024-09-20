from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import db

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/properties'):
            self.handle_properties_request()
        else:
            self.send_response(404)
            self.end_headers()

    def handle_properties_request(self):
        filters = self.parse_query_string()
        properties = db.get_properties(filters)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(properties).encode('utf-8'))

    def do_POST(self):
        if self.path.startswith('/like'):
            self.handle_like_request()
        else:
            self.send_response(404)
            self.end_headers()

    def handle_like_request(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))
        property_id = self.path.split('/')[-1]
        user_id = data.get('user_id')
        result = db.like_property(property_id, user_id)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(result).encode('utf-8'))

    def parse_query_string(self):
        query_string = self.path.split('?')[-1]
        filters = {}
        for param in query_string.split('&'):
            key, value = param.split('=')
            filters[key] = value
        return filters

def run(server_class=HTTPServer, handler_class=RequestHandler, port=5000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
