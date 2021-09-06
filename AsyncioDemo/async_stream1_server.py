import asyncio
import datetime
import json
import random

INTERVAL = 2


async def get_data(sleep_sec):
    await asyncio.sleep(sleep_sec)
    return {
        'timestamp' : str(datetime.datetime.now()),
        'value' : random.randint(1,100)
    }


async def handle_connection(reader,writer):
    data = await reader.read(100)
    message = data.decode().strip()
    addr = writer.get_extra_info('peername')

    if message == "please":
        print("Starting the connection with", addr)
        writer.write(b'Connected successfully.')

        while True:
            try:
                payload = await get_data(INTERVAL)
                writer.write(bytes(json.dumps(payload), 'utf-8'))
                await writer.drain()

                del payload

            except Exception as e:
                print(e)
                break

    print("Closing the connection with", addr)
    writer.write(b'Connection failed.')
    writer.close()


async def main():
    server = await asyncio.start_server(handle_connection, '0.0.0.0', 8888)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    asyncio.run(main())
