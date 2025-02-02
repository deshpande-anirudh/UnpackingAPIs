from flask import Flask, Response, render_template
from confluent_kafka import Consumer, KafkaException

app = Flask(__name__)

# Global Kafka Consumer setup
def create_consumer():
    consumer = Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'score-consumer-group',
        'auto.offset.reset': 'earliest',
    })
    consumer.subscribe(['live_scores'])
    return consumer

kafka_consumer = create_consumer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stream')
def stream():
    def generate():
        try:
            while True:
                msg = kafka_consumer.poll(1.0)  # Poll Kafka for new messages
                if msg is None:
                    continue
                if msg.error():
                    print(f"Kafka error: {msg.error()}")
                    continue

                score_update = msg.value().decode('utf-8')
                print(f"Received score update: {score_update}")
                yield f"data: {score_update}\n\n"
        except GeneratorExit:
            print("Client disconnected.")
        except Exception as e:
            print(f"Unexpected error: {e}")
        finally:
            kafka_consumer.close()

    return Response(generate(), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
