# things.py

# Let's get this party started!
import falcon

import gpio

# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
pin = gpio.GPIO()

# things will handle all requests to the '/things' URL path
app.add_route('/gpio/{pin}/{in_out}/{value}', pin)