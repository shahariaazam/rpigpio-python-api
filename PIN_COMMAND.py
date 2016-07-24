import falcon

import json
from gpiozero import LED, Button


class GPIO(object):
    def on_get(self, req, resp, pin, in_out, value):
        led = LED(int(pin))
        if (in_out == 'write' and value == 'true'):
            # print "write-true"
            led.on()
        if in_out == 'write' and value == 'false':
            # print "write-false"
            led.off()

        resp.body = json.dumps({'pin': pin, 'in_out': in_out, 'value': value})
        resp.content_type = 'application/json'
        resp.status = falcon.HTTP_200
