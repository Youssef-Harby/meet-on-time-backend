import imp
from flask import Flask, render_template, Response
from matplotlib.pyplot import get, text
from pykafka import KafkaClient

def get_kafka_client():
    return KafkaClient(hosts='localhost:9092')

app = Flask(__name__)


@app.route('/')
def index():
    return(render_template('index.html'))

@app.route('/map')
def map():
    return(render_template('pages/map.html'))

#CONSUMER API
@app.route('/topic/<topicname>')
def get_messages(topicname):
    client = get_kafka_client()
    def events():
        for i in client.topics[topicname].get_simple_consumer():
            yield 'data:{0}\n\n'.format(i.value.decode())
    return Response(events(), mimetype="text/event-stream")

if __name__ == '__main__':
    app.run(debug=True, port=5001)