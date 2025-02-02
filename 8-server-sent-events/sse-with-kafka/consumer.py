from confluent_kafka import Consumer, KafkaException

def create_consumer():
    # Kafka Consumer configuration
    consumer = Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'score-consumer-group',
        'auto.offset.reset': 'earliest',  # Read from the earliest messages if no offsets are present
    })

    # Subscribe to the topic
    topic = 'live_scores'
    consumer.subscribe([topic])

    print(f"Consumer subscribed to topic: {topic}")

    try:
        while True:
            msg = consumer.poll(1.0)  # Poll Kafka for new messages
            if msg is None:
                continue
            if msg.error():
                raise KafkaException(msg.error())

            # Print the received message
            score_update = msg.value().decode('utf-8')
            print(f"Received score update: {score_update}")

    except KeyboardInterrupt:
        print("Consumer stopped manually")
    finally:
        consumer.close()
        print("Consumer closed")


if __name__ == "__main__":
    create_consumer()
