# Simulate sending temperature sensor data to Kafka topic
from kafka import KafkaProducer
import json, random, time

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

while True:
    temp_data = {
        'machine_id': 'RW-01',
        'temperature': round(random.uniform(45, 105), 2),
        'timestamp': time.time()
    }
    producer.send('temperature_topic', value=temp_data)
    time.sleep(5)
