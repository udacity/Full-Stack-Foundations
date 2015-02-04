from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()



class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        restaurants = session.query(Restaurant).all()
        try:
            if self.path.endswith("/restaurants"):
                output = ""
                self.send_response(200)
                self.send_header('Content-type',	'text/html')
                self.end_headers()
                
                output += "<html><body>"
                for restaurant in restaurants:
                    output += restaurant.name
                    output += "</br></br></br>"
                output += "</body></html>"
                self.wfile.write(output)

                
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)
     

   

def main():
    try:
        server = HTTPServer(('', 80), MyHandler)
        print 'Web server running...open localhost:8080/restaurants in your browser'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()
