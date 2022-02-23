from pykafka import KafkaClient
import json

'''
client = KafkaClient(hosts="localhost:9092")

topic = client.topics['test1']

producer = topic.get_sync_producer()

producer.produce('test from py'.encode('ascii'))
'''