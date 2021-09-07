'''
server.py

server program.
'''
import asyncio
import datetime
import json
import random
import sys

INTERVAL = 2 #seconds
HOST = '0.0.0.0'
PORT = 8888
_SECRET_KEY = "prettyplease"

async def get_data(sleep_sec: int)->dict:
    """Dummy function to get data.

    Args:
        sleep_sec (int): sleep seconds.

    Returns:
        dict: data.
    """
    await asyncio.sleep(sleep_sec)
    return {
        'timestamp' : datetime.datetime.now(),
        'value' : random.randint(1, 100)
    }


async def handle_connection(reader: asyncio.StreamReader, writer: asyncio.StreamWriter)->None:
    """Handle connection function.

    Args:
        reader (asyncio.StreamReader): stream reader variable.
        writer (asyncio.StreamWriter): stream writer variable.
    """
    # get secret key
    data = await reader.read(100)
    secret_key = data.decode().strip()
    addr = writer.get_extra_info('peername')

    if secret_key == _SECRET_KEY:
        print("Starting the connection with", addr)
        writer.write('Connected successfully'.encode())

        while True:
            try:
                payload = await get_data(INTERVAL)
                writer.write(f"{json.dumps(payload)}".encode())
                await writer.drain()

                del payload
            except ConnectionError as conn_err:
                print(conn_err)
                break
            except Exception as ex:
                print(ex)
                break

    print("Closing the connection with", addr)
    writer.write(b'Connection failed.')
    writer.close()


async def start(host: str, port: int)->None:
    """Start server function.

    Args:
        host (str): host.
        port (int): port.
    """
    server = await asyncio.start_server(handle_connection, host, port)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    print(sys.argv)
    asyncio.run(start(HOST, PORT))
