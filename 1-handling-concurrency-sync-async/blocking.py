import time
from datetime import datetime


def prepare_coffee(customer_id):
    time.sleep(1)
    print(f"{customer_id} Your coffee is prepared, and heading to the counter")
    time.sleep(0.2)


def order_coffee(customer_id):
    time.sleep(0.5)
    print(f"{customer_id} Your coffee is ordered. Preparing...")
    prepare_coffee(customer_id)
    print(f"{customer_id} Please pick up your coffee from the counter")


start = datetime.now()
for i in range(5):
    order_coffee(i+1)
print(f"Processing time {(datetime.now() - start).total_seconds()} seconds")

"""
Output: 

1 Your coffee is ordered. Preparing...
1 Your coffee is prepared, and heading to the counter
1 Please pick up your coffee from the counter
2 Your coffee is ordered. Preparing...
2 Your coffee is prepared, and heading to the counter
2 Please pick up your coffee from the counter
3 Your coffee is ordered. Preparing...
3 Your coffee is prepared, and heading to the counter
3 Please pick up your coffee from the counter
4 Your coffee is ordered. Preparing...
4 Your coffee is prepared, and heading to the counter
4 Please pick up your coffee from the counter
5 Your coffee is ordered. Preparing...
5 Your coffee is prepared, and heading to the counter
5 Please pick up your coffee from the counter

Processing time 8.551196 seconds
"""


