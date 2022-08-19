import asyncio
import json
import logging
import websockets


logging.basicConfig(level=logging.INFO)


async def consumer_handler(websocket: websockets.WebSocketClientProtocol) -> None:
    async for message in websocket:
        log_message(message)
async def consume(connstring: str) -> None:
    entityId = "ENTITY_ID"
    obj = {
        "tsSubCmds": [
            {
                "entityType": "DEVICE",
                "entityId": entityId,
                "scope": "LATEST_TELEMETRY",
                "cmdId": 10
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
    logging.info(f"message: {message}")


async def produce(message: str, connstring: str) -> None:
    async with websockets.connect(connstring) as ws:
        await ws.send(message)
        await ws.recv()

if __name__ == '__main__':
    token = "TOKEN"
    connstring = f"ws://localhost:9090/api/ws/plugins/telemetry?token="+token

    loop = asyncio.get_event_loop()

    # loop.run_until_complete(produce(json.dumps(obj), connstring))
    loop.run_until_complete(consume(
        connstring
        ))

    # loop.run_forever()