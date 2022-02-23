from pykafka import KafkaClient
import json
from datetime import datetime
import uuid
import time

# READ COORDINATES FROM GEOJSON
input_file = open('./data/bus2.json', encoding="utf8")
json_array = json.load(input_file)
coordinates = json_array['features'][0]['geometry']['coordinates']
print(coordinates)

# GENERATE UUID
def generate_uuid():
    return uuid.uuid4()


# KAFKA PRODUCER
client = KafkaClient(hosts="localhost:9092")
topic = client.topics['geodata_final']
producer = topic.get_sync_producer()

# CONSTRUCT MESSAGE
data = {}
data['busline'] = '00002'


def generate_checkpoint(coordinates):
    i = 0
    while i < len(coordinates):
        data['key'] = data['busline'] + '_' + str(generate_uuid())
        data['timestamp'] = str(datetime.utcnow())
        data['latitude'] = coordinates[i][1]
        data['longitude'] = coordinates[i][0]
        message = json.dumps(data)
        print(message)
        producer.produce(message.encode('utf8'))
        time.sleep(1)

        #if bus reaches last coordinate, start from beginning
        if i == len(coordinates)-1:
            i = 0
        else:
            i += 1


generate_checkpoint(coordinates)
