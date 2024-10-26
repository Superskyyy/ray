# from socketify import App

# app = App()
# app.get("/", lambda res, req: res.end("Hello World socketify from Python!"))
# app.listen(8000, lambda config: print("Listening on port http://localhost:%d now\n" % config.port))
# app.run()

import time
import asyncio
from aiohttp import ClientSession
from socketify import ASGI
from fastapi import FastAPI

# Step 1: Define a simple FastAPI app to use as the ASGI app
fastapi_app = FastAPI()
from fastapi.responses import PlainTextResponse

@fastapi_app.get("/", response_class=PlainTextResponse)
async def root():
    return "ok"

# Step 2: Define the function that mimics the original run_http_server setup
def run_http_server():
    from socketify import ASGI


    app = ASGI(fastapi_app)
    # Step 3: Start listening on the specified host and port
    app.listen(8080)

    # Step 4: Run the app in an asyncio loop, equivalent to uvicorn's server loop
    app.run(block=False)
    time.sleep(999)
run_http_server()
# Step 4: Define the aiohttp client test to check server connectivity
# async def test_server_connectivity():
#     # Start the server in a background task
#     server_task = asyncio.create_task(run_http_server())
#     #await asyncio.sleep(1)  # Wait briefly to allow the server to start

#     # Send a request to the server using aiohttp
#     for i in range(99):
#         async with ClientSession() as session:
#             async with session.get("http://localhost:8080") as response:
#                 print(f"Status: {response.status}")
#                 text = await response.json()
#                 print(f"Response: {text}")

#     # Stop the server after the test
#     server_task.cancel()
#     try:
#         await server_task
#     except asyncio.CancelledError:
#         pass

# # Run the test
# asyncio.run(test_server_connectivity())
