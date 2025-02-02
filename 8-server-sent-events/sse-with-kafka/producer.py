from confluent_kafka import Producer
import random
import time

# Define Kafka configurations
conf = {
    'bootstrap.servers': 'localhost:9092',  # Kafka broker address
    'client.id': 'score-producer'
}

# Create Kafka producer instance
producer = Producer(conf)

# List of sports events (simulated)
teams = ['Team A', 'Team B']
events = ['Goal Scored', 'Penalty', 'Timeout']


# Function to create a random score update
def generate_score_update():
    team = random.choice(teams)
    event = random.choice(events)
    score = random.randint(0, 10)
    update = f'{team}: {event} - Score: {score}'
    return update


# Send score updates to Kafka
def send_score_updates():
    while True:
        score_update = generate_score_update()
        producer.produce('live_scores', key='score', value=score_update)  # 'live_scores' is the topic
        print(f"Produced: {score_update}")

        time.sleep(2)  # Simulate a delay between updates


# Start sending score updates
send_score_updates()
