import asyncio
from aiohttp import ClientSession


async def test_server_connectivity():

    async with ClientSession() as session:
        try:
            async with session.get("http://localhost:8000/") as response:
                print(f"Status: {response.status}")
                # Read response text manually and attempt to decode as JSON
                text = await response.text()
                try:
                    json_data = await response.json(content_type=None)  # Skip content type check
                    print(f"Response JSON: {json_data}")
                except ValueError:
                    print("Response is not valid JSON")
                    print(f"Response Text: {text}")
        except Exception as e:
            print(f"Failed to connect: {e}")


asyncio.run(test_server_connectivity())
