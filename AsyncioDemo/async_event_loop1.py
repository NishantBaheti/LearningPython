import asyncio
import datetime

INTERVAL = 5

async def get_data(sleep_sec):
    await asyncio.sleep(sleep_sec)
    print(datetime.datetime.now())

async def main():
    while True:
        await get_data(INTERVAL)


if __name__ == '__main__':
    asyncio.run(main())
