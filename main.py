import httpx
import time
import json
import random

client = httpx.Client()
config = json.load(open("config.json"))

def change_name(name):
    client.patch(f"https://discord.com/api/guilds/{config['serverId']}", headers={"Authorization": config['token']}, json={"name": name})
    print(f"Changed name to {name}")

def main():
    while True:
        for name in config["names"]:
            change_name(name)
            time.sleep(5)

if __name__ == "__main__":
    main()