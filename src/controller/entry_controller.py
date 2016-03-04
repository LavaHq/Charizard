import tornado.web


class EntryHandler(tornado.web.RequestHandler):
    """A controller that Creates, Updates and Fetches Entries"""
    def get(self):
        self.write("Hello, GET")

    def post(self):
        self.write("Hello, POST")
