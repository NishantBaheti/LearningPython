import asyncio
import random

def print_random():
    print(random.randint(1, 10))

async def main():
    print('start')

    await asyncio.sleep(1)

    i = 0
    while i< 5:
        print_random()

        i += 1

    await asyncio.sleep(1)
    print('end')

if __name__== "__main__":
    asyncio.run(main())
