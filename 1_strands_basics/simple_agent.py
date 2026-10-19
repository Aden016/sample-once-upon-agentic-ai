from strands import Agent
import logging

logging.basicConfig(level=logging.DEBUG)

agent = Agent(system_prompt="You are a game master for a Dungeon & Dragon game")

response = agent("Hi, I am an adventurer ready for adventure!")
print(response)