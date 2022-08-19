import asyncio
import json
import logging
import websockets


logging.basicConfig(level=logging.INFO)


async def consumer_handler(websocket: websockets.WebSocketClientProtocol) -> None:
    async for message in websocket:
        log_message(message)
async def consume(connstring: str) -> None:
    obj = {
        "tsSubCmds": [
            {
                "entityType": "DEVICE",
                "entityId": "c6fd7090-1edc-11ed-9523-2b90da0aac54",
                "scope": "LATEST_TELEMETRY",
                "cmdId": 1
            }
        ],
        "historyCmds": [],
        "attrSubCmds": []
    }

    async with websockets.connect(connstring) as websocket:
        await websocket.send(json.dumps(obj))
        await websocket.recv()
        await consumer_handler(websocket)

def log_message(message: str) -> None:
    print()
    logging.info(f"message: {message}")
    print()


def main():
    # await consume("ws://localhost:9090/api/ws/plugins/telemetry?token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJoaXRlc2hAaW5mb3N5cy5jb20iLCJ1c2VySWQiOiI5ZTQ1MTdjMC0xZWRjLTExZWQtOTUyMy0yYjkwZGEwYWFjNTQiLCJzY29wZXMiOlsiVEVOQU5UX0FETUlOIl0sImlzcyI6InRoaW5nc2JvYXJkLmlvIiwiaWF0IjoxNjYwODIwMjY5LCJleHAiOjE2NjA4MjkyNjksImZpcnN0TmFtZSI6IkhpdGVzaCIsImxhc3ROYW1lIjoiSmFpbiIsImVuYWJsZWQiOnRydWUsImlzUHVibGljIjpmYWxzZSwidGVuYW50SWQiOiI4OTQ5ZDhiMC0xZWRjLTExZWQtOTUyMy0yYjkwZGEwYWFjNTQiLCJjdXN0b21lcklkIjoiMTM4MTQwMDAtMWRkMi0xMWIyLTgwODAtODA4MDgwODA4MDgwIn0.COoVvxd2M5Gnk2kkOKr6qTrAGXxQHCHjiMDXEku0gzCcSgH8k7PA_1GVXi5xaoI8ilCgQlfsyoz6293wQWn8EQ")
    pass
if __name__ == '__main__':
    connstring = f"ws://localhost:9090/api/ws/plugins/telemetry?token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJoaXRlc2hAaW5mb3N5cy5jb20iLCJ1c2VySWQiOiI5ZTQ1MTdjMC0xZWRjLTExZWQtOTUyMy0yYjkwZGEwYWFjNTQiLCJzY29wZXMiOlsiVEVOQU5UX0FETUlOIl0sImlzcyI6InRoaW5nc2JvYXJkLmlvIiwiaWF0IjoxNjYwODIwMjY5LCJleHAiOjE2NjA4MjkyNjksImZpcnN0TmFtZSI6IkhpdGVzaCIsImxhc3ROYW1lIjoiSmFpbiIsImVuYWJsZWQiOnRydWUsImlzUHVibGljIjpmYWxzZSwidGVuYW50SWQiOiI4OTQ5ZDhiMC0xZWRjLTExZWQtOTUyMy0yYjkwZGEwYWFjNTQiLCJjdXN0b21lcklkIjoiMTM4MTQwMDAtMWRkMi0xMWIyLTgwODAtODA4MDgwODA4MDgwIn0.COoVvxd2M5Gnk2kkOKr6qTrAGXxQHCHjiMDXEku0gzCcSgH8k7PA_1GVXi5xaoI8ilCgQlfsyoz6293wQWn8EQ"
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(produce(json.dumps(obj), connstring))
    loop.run_until_complete(consume(
        connstring
        ))

    # loop.run_forever()