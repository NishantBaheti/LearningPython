import asyncio
import datetime
import random

async def say_after(sec):
    await asyncio.sleep(sec)
    print("Waited for :",sec," seconds, ",datetime.datetime.utcnow())


async def main(n_tasks):
    
    task_list = []
    for _ in range(n_tasks):
        task_list.append(say_after(random.randint(1,50)))

    l = await asyncio.gather(*task_list)
    print(l)


if __name__ == '__main__':
    print("starting at",datetime.datetime.utcnow())
    asyncio.run(main(10))
    print("ending at", datetime.datetime.utcnow())
