import asyncio
import datetime as dt


async def wait_for(sec):
    await asyncio.sleep(sec)
    print("waited for :",sec,"seconds, Now",dt.datetime.now())

async def main():
    task_first = asyncio.create_task(wait_for(5))
    task_second = asyncio.create_task(wait_for(1))
    task_third = asyncio.create_task(wait_for(10))
    
    await task_first
    await task_second
    await task_third


if __name__ == "__main__":
    print("running tasks")
    asyncio.run(main())
