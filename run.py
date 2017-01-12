import os
from eve import Eve

port = 80
host = '0.0.0.0'
app = Eve()

if __name__ == '__main__':
    app.run(host=host, port=port)
