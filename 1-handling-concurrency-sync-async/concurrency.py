import asyncio
from datetime import datetime


async def prepare_coffee(customer_id):
    await asyncio.sleep(1)
    print("Your coffee is prepared, and heading to the counter!")
    await asyncio.sleep(0.5)


async def order_coffee(customer_id):
    print("Welcome! Please order your coffee. ")
    await asyncio.sleep(0.5)
    preparation_task = await prepare_coffee(customer_id)
    print("Your coffee is prepared! Please head to the counter")
    return preparation_task


async def main():
    start = datetime.now()
    await asyncio.gather(
        *[order_coffee(i+1) for i in range(5)]
    )
    print(f"The processing time: {(datetime.now() - start).total_seconds()} seconds")


asyncio.run(main())
