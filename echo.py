from flask import Flask, request
app = Flask(__name__)

print('Starting a flask application')

counter = 0

@app.route('/')
def hello_world():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ips = (s.getsockname())
    s.close()

    global counter

    counter += 1

    print('I received a request')
    return 'Hello MEST\n'
