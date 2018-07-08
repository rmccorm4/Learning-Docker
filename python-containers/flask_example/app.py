import os
import socket

from flask import Flask

app = Flask(__name__)

'''
from redis import Redis, RedisError
# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)
'''

@app.route("/")
def hello():
    '''
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"
    '''
    html = "<h3>Hello {name}!</h3>" \
           "<b>Container ID:</b> {hostname}<br/>" \
           "<img src={image} alt={image}>"

    #return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)
    return html.format(name="Docker", hostname=socket.gethostname(), image='/static/head.jpg')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
