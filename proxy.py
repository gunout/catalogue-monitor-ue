from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs, unquote
import urllib.request
import json

class ProxyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == '/proxy':
            params = parse_qs(parsed.query)
            target_url = unquote(params.get('url', [''])[0])
            if not target_url:
                self.send_error(400, 'Missing url parameter')
                return
            try:
                req = urllib.request.Request(target_url, headers={'User-Agent': 'CatalogueMonitor/1.0'})
                with urllib.request.urlopen(req, timeout=30) as response:
                    data = response.read()
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(data)
            except Exception as e:
                self.send_error(502, f'Proxy error: {str(e)}')
        else:
            self.send_error(404, 'Not found')

    def log_message(self, format, *args):
        pass  # silence les logs

if __name__ == '__main__':
    print('Proxy running on http://localhost:8974')
    HTTPServer(('localhost', 8002), ProxyHandler).serve_forever()