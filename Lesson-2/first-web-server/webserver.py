from __future__ import print_function
try:
    from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer   #Python 2
except ImportError:
    from http.server import BaseHTTPRequestHandler, HTTPServer      #Python 3


class WebServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path.endswith("/hello"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = b""
            message += b"<html><body>Hello!</body></html>"
            self.wfile.write(message)
            print(message)
            return
        else:
            self.send_error(404, 'File Not Found: %s' % self.path)


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        print("Web Server running on port %s" % port)
        server.serve_forever()
    except KeyboardInterrupt:
        print(" ^C entered, stopping web server....")
        server.socket.close()

if __name__ == '__main__':
    main()
