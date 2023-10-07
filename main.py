from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def get_visitor_ip():
    ip_address = request.remote_addr
    return f'The visitor IP address is: {ip_address}'

if __name__ == '__main__':
    app.run()
