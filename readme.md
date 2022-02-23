kafka-console-producer.sh --broker-list 127.0.0.1:9092 --topic test1
kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --topic test1 --from-beginning