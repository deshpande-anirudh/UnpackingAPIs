import time
import multiprocessing
from datetime import datetime


def prepare_coffee_in_process(customer_id):
    time.sleep(1)
    print(f"Hi {customer_id}, your coffee is prepared and heading to the counter")
    time.sleep(0.5)
    print(f"Hi {customer_id}, your coffee is placed at the counter, please collect")


def order_coffee(customer_id):
    print(f"Hi {customer_id}, please place your order")
    time.sleep(0.5)
    process = multiprocessing.Process(target=prepare_coffee_in_process, args=(customer_id,))
    process.start()
    return process


def main():
    print("Welcome to the coffee shop")

    start = datetime.now()

    processes = []

    for i in range(5):
        process = order_coffee(i+1)
        processes.append(process)

    for process in processes:
        process.join()

    print(f"Processing time: {(datetime.now() - start).total_seconds()} seconds")


if __name__ == "__main__":
    main()

