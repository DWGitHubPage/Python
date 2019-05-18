# Python3.7.3
# Asyncio examples with newest features with version 3.7.3

import asyncio
import time


async def coroutine_1():
    print('coroutine_1 is active on the event loop')

    print('coroutine_1 yielding control. Going to be blocked for 4 seconds')
    await asyncio.sleep(4)

    print('coroutine_1 resumed. coroutine_1 exiting')

async def coroutine_2():
    print('coroutine_2 is active on the event loop')

    print('coroutine_2 yielding control. Going to be blocked for 5 seconds')
    await asyncio.sleep(5)

    print('coroutine_2 resumed. coroutine_2 exiting')

# this is the event loop
loop = asyncio.get_event_loop()

# schedule both the coroutines to run on the event loop
loop.run_until_complete(asyncio.gather(coroutine_1(), coroutine_2()))

print('\n')


# Second example.

async def main():
    print("Asyncio ...")
    await asyncio.sleep(2)
    print("...a library to write concurrent code using the async/await syntax.")
    await asyncio.sleep(4)
    print('\n')
    print("...It is used as a foundation for multiple Python asynchronous "
          "frameworks that  provide high-performance network and web-servers, "
          "database connection libraries, distributed task queues, etc.")
    await asyncio.sleep(10)
    print('\n')
    print("...Asyncio is often a perfect fit for IO-bound and high-level"
          "structured network code.")
    print('\n')
    await asyncio.sleep(2)

asyncio.run(main())


# Third example.

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"Second Asyncio starting at {time.strftime('%X')}")
    print('\n')
    await say_after(3, "Asyncio...")
    await say_after(2, "...a library to write concurrent code using the async/await syntax.")
    print('\n')
    await say_after(3, "...It is used as a foundation for multiple Python asynchronous "
          "frameworks that  provide high-performance network and web-servers, "
          "database connection libraries, distributed task queues, etc.")
    print('\n')
    await say_after(10, "...Asyncio is often a perfect fit for IO-bound and high-level"
          "structured network code.")
    print('\n')
    print(f"Finished at {time.strftime('%X')}")

asyncio.run(main())
          
print('\n')
          
# Fourth example.

async def fake_network_request(request):
    print('making network call for request:  ' + request)
    # simulate network delay
    await asyncio.sleep(1)

    return 'got network response for request: ' + request

async def web_server_handler():
    # Schedule both the network calls in a non-blocking way.

    # Ensure_future creates a task from the coroutine object, & schedules it on the event loop
    task1 = asyncio.ensure_future(fake_network_request('one'))

    # Another way to do the scheduling
    task2 = asyncio.get_event_loop().create_task(fake_network_request('two'))

    # Simulate a no-op blocking task. This gives a chance to the network requests scheduled above to be executed.
    await asyncio.sleep(0.5)

    print('doing useful work while network calls are in progress...')

    # Wait for the network calls to complete. Time to step off the event loop using await. 
    await asyncio.wait([task1, task2])

    print(task1.result())
    print(task2.result())

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.ensure_future(web_server_handler()))

print('\n')

# Fifth example.

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")


# Now an example that is Synchronous.
""" This is 2.13 seconds longer than the previous example with
the first three run throughs although .2 seconds shorter with
the fourth run."""

def count():
    print("One")
    time.sleep(1)
    print("Two")

def main():
    for _ in range(3):
        count()

if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
