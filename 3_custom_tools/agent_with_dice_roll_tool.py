from strands import Agent, tool

@tool
def roll_dice(faces: int = 6) -> int:
    """Roll a dice with a given number of faces.

    Args:
        faces: The number of faces on the dice. Defaults to 6.

    Returns:
        int: A random integer between 1 and the number of faces.
    """

    import random

    if faces < 1:
        raise ValueError("Dice must have at least 1 face")

    return random.randint(1, faces)


print(roll_dice.tool_spec)  # what Strands tells the model about your tool

dice_master = Agent(
    system_prompt="""You are Lady Luck, the mystical keeper of dice and fortune in D&D adventures.
    You speak with theatrical flair and always announce dice rolls with appropriate drama.
    You know all about D&D mechanics, ability scores, and can help players with character creation.
    When rolling ability scores, remember the traditional method: roll 4d6, drop the lowest die.""",
    tools=[roll_dice]
)

dice_master("Help me create a new D&D character! Roll the strength, wisdom, charisma and intelligence abilities scores using 4d6 drop lowest method.")