import asyncio
import time
# pip install awaits
from awaits.awaitable import awaitable


def sync_task():
    time.sleep(1)
    print(1)
    return 1


@awaitable
def two():
    time.sleep(1)
    print(2)


async def main():
    tasks = [
        asyncio.get_event_loop().run_in_executor(None, sync_task),
        asyncio.get_event_loop().run_in_executor(None, sync_task),
        asyncio.get_event_loop().run_in_executor(None, sync_task),
        asyncio.get_event_loop().run_in_executor(None, sync_task),
        asyncio.get_event_loop().run_in_executor(None, sync_task),

        two(),
        two(),
        two(),
        two(),
        two(),
    ]
    await asyncio.gather(*tasks)
    # await two()


if __name__ == '__main__':
    asyncio.run(main())
