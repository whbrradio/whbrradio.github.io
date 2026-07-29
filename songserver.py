from http.server import HTTPServer, BaseHTTPRequestHandler

FILE = r"C:\Users\braed\OneDrive\Desktop\whbr website\nowplaying.txt"


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path.startswith("/nowplaying.txt"):

            try:

                with open(FILE,"r",encoding="utf-8") as f:
                    song=f.read()

                self.send_response(200)

                self.send_header(
                    "Access-Control-Allow-Origin",
                    "*"
                )

                self.send_header(
                    "Content-type",
                    "text/plain"
                )

                self.end_headers()

                self.wfile.write(
                    song.encode()
                )

            except Exception as e:

                self.send_response(500)
                self.end_headers()

        else:

            self.send_response(404)
            self.end_headers()


server = HTTPServer(
    ("0.0.0.0",8080),
    Handler
)

print(
"WHBR Song Server running on port 8080"
)

server.serve_forever()