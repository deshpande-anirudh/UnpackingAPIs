---

# Concurrency vs Parallelism

## Overview

This repository contains a simulation of a coffee shop where multiple customers place orders and have their coffee prepared. The simulation demonstrates the difference between **concurrency** and **parallelism** using **asyncio** and **multiprocessing** in Python. The order-taking process is handled sequentially, but the coffee preparation for each customer is done in parallel across separate processes, using multiple CPU cores.

## Code Description

The simulation consists of the following key components:
- **`order_coffee()`**: Simulates a customer placing an order.
- **`prepare_coffee_in_process()`**: Simulates the process of preparing coffee, which is handled in parallel using **multiprocessing**.
- **`main()`**: Starts multiple coffee preparation processes for different customers and tracks the processing time.

In this simulation:
- **Order Taking** is sequential.
- **Coffee Preparation** is parallel, with each customer’s coffee being prepared in a separate process.

---

## Concepts: Concurrency vs Parallelism

### **Concurrency**:
- Concurrency refers to the concept of **managing multiple tasks at the same time**. However, these tasks might not run at exactly the same time. Instead, the system switches between tasks rapidly, creating the illusion that they are running simultaneously.
- **Concurrency** is useful when dealing with **I/O-bound tasks**, where the program has to wait for external resources (e.g., disk reads, network requests). During the waiting period, other tasks can be executed.
- In the coffee shop simulation, **order-taking** could be concurrent because the system might be waiting for input or some other resource (e.g., waiting for a customer to provide payment), and in the meantime, other tasks could run.

### **Parallelism**:
- Parallelism, on the other hand, involves **actually running tasks simultaneously** on separate processors or cores. This is useful for **CPU-bound tasks**, where the program needs to perform intensive computations that can be split across multiple processors.
- In the coffee shop simulation, **coffee preparation** is parallel because each customer's coffee is prepared in a separate process, using multiple CPU cores to handle these tasks at the same time.

---

## When to Use Concurrency vs Parallelism

- **Use Concurrency**:
  - When tasks are I/O-bound (e.g., network requests, file reads/writes, waiting for user input).
  - When you need to manage many tasks at the same time, but those tasks don't require a lot of CPU power.
  - Example: In web servers or chat applications, concurrency helps handle multiple users without waiting for one user’s request to finish before starting the next one.

- **Use Parallelism**:
  - When tasks are CPU-bound (e.g., heavy computations, data processing).
  - When you need to divide the work into independent pieces that can be executed on separate CPU cores to speed up the overall process.
  - Example: In image processing, data analysis, or simulations where multiple computations can be done at the same time, parallelism will significantly improve performance.

---

## How **`asyncio`** Works Behind the Scenes

**`asyncio`** is a library in Python that provides support for asynchronous programming. It allows tasks to run concurrently by using a **single thread**. The key features of `asyncio` are:

- **Event Loop**: The event loop is the core of `asyncio`. It manages the execution of asynchronous tasks. Instead of waiting for one task to finish before moving to the next, `asyncio` switches between tasks, making progress on multiple tasks without blocking.
- **Coroutines**: Functions defined with `async def` are called coroutines. They can be paused and resumed with the `await` keyword, allowing other coroutines to run while one is waiting.
- **Non-blocking**: When `await` is called in a coroutine (e.g., `await asyncio.sleep()`), it doesn't block the event loop. Instead, it yields control, allowing the event loop to run other tasks.

In our coffee shop simulation:
- **Concurrency** (with `asyncio`) is used for order-taking. The program can start multiple customer orders without waiting for the previous order to finish, but the coffee preparation (done by separate processes) runs in parallel.

---

## How **`multiprocessing`** Works Behind the Scenes

**`multiprocessing`** is a module in Python that allows for parallel execution by creating multiple **processes**, each running on a separate CPU core. Key features:

- **Separate Processes**: Each process has its own memory space and runs independently from other processes. This bypasses the **Global Interpreter Lock (GIL)** in Python, allowing true parallelism on multi-core systems.
- **Processes vs Threads**: While threads share memory, processes have their own memory space, making them ideal for CPU-bound tasks where computations need to be divided among multiple processors.
- **`multiprocessing.Process`**: This class is used to create a new process. We start the process using `.start()` and wait for it to finish using `.join()`.

In our coffee shop simulation:
- **Parallelism** (with `multiprocessing`) is used for preparing coffee. Each coffee preparation runs in a separate process, allowing the program to prepare multiple coffees at the same time using different CPU cores.

---

## How to Run the Code

### Prerequisites:
- Python 3.x installed.
- No additional libraries are required (the code uses standard Python libraries: `asyncio`, `multiprocessing`, `time`, and `datetime`).

### Steps:
1. Clone or download the repository.
2. Open a terminal and navigate to the directory containing the `coffee_shop.py` file.
3. Run the code using the command:
   ```
   python coffee_shop.py
   ```

### Expected Output:
```
Welcome to the coffee shop
Hi 1, please place your order
Hi 2, please place your order
Hi 3, please place your order
Hi 4, please place your order
Hi 5, please place your order
Hi 1, your coffee is prepared and heading to the counter
Hi 2, your coffee is prepared and heading to the counter
Hi 3, your coffee is prepared and heading to the counter
Hi 4, your coffee is prepared and heading to the counter
Hi 5, your coffee is prepared and heading to the counter
Hi 1, your coffee is placed at the counter, please collect
Hi 2, your coffee is placed at the counter, please collect
Hi 3, your coffee is placed at the counter, please collect
Hi 4, your coffee is placed at the counter, please collect
Hi 5, your coffee is placed at the counter, please collect
Processing time: 2.536 seconds
```

---

## Conclusion

This coffee shop simulation demonstrates the power of **concurrency** and **parallelism**. We use **`asyncio`** for managing concurrent tasks (like placing orders) and **`multiprocessing`** for running parallel tasks (like preparing coffee). Understanding the difference between concurrency and parallelism, and knowing when to use each, can greatly improve the performance and scalability of your Python applications.

---