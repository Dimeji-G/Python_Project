import http.server
import socketserver
import socket
import os

PORT = 8219  # Choose a port number

class FileHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        #if self.path == '/home/dimeji/Documents/Python_Script':
            # Serve a directory listing if a specific file is not requested
            #self.path = 'index.html'  # Default file to serve
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

def main():
    with socketserver.TCPServer(("0.0.0.0", PORT), FileHandler) as httpd:
        print("Serving at http://{}:{}/".format(socket.gethostbyname(socket.gethostname()), PORT))
        httpd.serve_forever()

if __name__ == "__main__":
    main()
