import tornado.ioloop
import tornado.web
import handlers.MainHandler as mh
import handlers.TimeHandler as th


def make_app():
    return tornado.web.Application([
        (r"/", mh.MainHandler),
        (r"/time", th.TimeHandler),
    ])


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
