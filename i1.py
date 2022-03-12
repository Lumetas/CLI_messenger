from flask import *
from logging.config import *
import sys


def mss(x):
    f = open('msg.txt', 'w',)
    f.write(x)
    f.close()


host = sys.argv[1]
port = sys.argv[2]
f = open('Key.txt', 'r')
Key = f.read()
Key = "/" + Key + "/"
print('http://' + host + ':' + port + Key)


app = Flask(__name__)

log = logging.getLogger('werkzeug') 
log.setLevel(logging.ERROR)



@app.route(Key)
def starte():
    return ''
    
@app.route(Key + "<msg>")
def say(msg):
    print(msg)
    return 'sended'
        
        


if __name__ == '__main__':
    app.run(host=host, port=port)

