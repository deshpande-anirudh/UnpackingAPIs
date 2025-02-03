import asyncio
import websockets

async def echo(websocket):
    async for message in websocket:
        await websocket.send(f"Server echo: {message}")

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        print("Server started on ws://localhost:8765")
        await asyncio.Future()  # Run forever


asyncio.run(main())
