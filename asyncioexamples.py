# Python3.7.3
# Asyncio examples with newest features with version 3.7.3

import asyncio
import time


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
