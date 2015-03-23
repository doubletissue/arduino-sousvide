import datetime
import urllib2
import webapp2

from google.appengine.api import mail

import models
import utils

class GetCommand(webapp2.RequestHandler):

    def _GetCommand(self):
        cooker_id = self.request.get("id")
        temp = float(self.request.get("temp"))

        cooker = utils.GetCooker(cooker_id)
        cooker.current_temp = temp
        cooker.put()

        utils.AddHistoryPoint(cooker)

        return cooker.current_output

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write("%f\n" % self._GetCommand())

    def post(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write("%f\n" % self._GetCommand())

app = webapp2.WSGIApplication([
    ('/ping', GetCommand),
])
