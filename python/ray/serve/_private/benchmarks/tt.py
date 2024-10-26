import asyncio
from aiohttp import ClientSession


async def test_server_connectivity():

    async with ClientSession() as session:
        async with session.get("http://localhost:8080/") as response:
            print(f"Status: {response.status}")
            # Read response text manually and attempt to decode as JSON
            text = await response.text()
            print(text)
            if text == "ok":
                print('haha')
            else:
                print(f'nono - text == {text}')
            assert text == "ok"
            try:
                json_data = await response.json(content_type=None)  # Skip content type check
                print(f"Response JSON: {json_data}")
            except ValueError:
                print("Response is not valid JSON")
                print(f"Response Text: {text}")



asyncio.run(test_server_connectivity())
