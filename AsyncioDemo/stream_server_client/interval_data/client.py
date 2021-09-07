'''
client.py

client program.
'''

import asyncio
import json


HOST = '0.0.0.0'
PORT = 8888
_SECRET_KEY = "prettyplease"
MSG_SIZE = 1024 * 2

async def start(host: str, port: int)-> None:
    """Start client.

    Args:
        host (str): host.
        port (int): port.
    """

    reader, writer = await asyncio.open_connection(
        host=host,
        port=port
    )

    print("Asking for connection")
    writer.write(_SECRET_KEY.encode())
    await writer.drain()

    data = await reader.read(n=MSG_SIZE)
    print(data.decode())

    while True:

        try:

            payload_bytes = await reader.read(n=MSG_SIZE)
            payload = json.loads(payload_bytes.decode())
            print(payload)
        except Exception as ex:
            print(ex)
            break

    print('Close the connection')
    writer.close()
    await writer.wait_closed()

if __name__ == '__main__':
    asyncio.run(start(host=HOST, port=PORT))
