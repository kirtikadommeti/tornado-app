import tornado
import datetime


class TimeHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Date is " + str(datetime.datetime.now().time()))