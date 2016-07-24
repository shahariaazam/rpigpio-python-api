import falcon

import json


class GPIO(object):

    def on_get(self, req, resp, pin, in_out, value):
        print pin, in_out, value
        resp.body = json.dumps({'message': 'Hello world!'})
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200