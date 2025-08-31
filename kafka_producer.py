from kafka import KafkaProducer
import json, time, random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    temp_reading = {
        'machine_id': 'RW-45',
        'timestamp': time.time(),
        'temperature': round(random.uniform(60, 100), 2)
    }
    producer.send('temperature_topic', value=temp_reading)
    time.sleep(2)  # simulate interval
