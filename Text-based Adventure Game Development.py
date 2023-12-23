# game based on the story:- Realm of Eldoria (Quest for the Crown of Destiny)
# Define the game's story and choices
story = {
    "start": {
        "text": "In the realm of Eldoria, you are a young hero chosen for a grand quest. Your mission is to recover the lost Crown of Destiny and restore peace to the land. Your journey begins in the bustling city of Eldorium. What's your first move?",
        "choices": {
            "explore city": "city_gate",
            "visit the mage's guild": "mage_guild",
        },
    },
    "city_gate": {
        "text": "You decide to explore the city. At the city gate, you encounter a mysterious traveler who offers to sell you a map to the Crown's possible location. Will you buy the map or continue your journey without it?",
        "choices": {
            "buy the map": "treasure_map",
            "continue without the map": "city_market",
        },
    },
    "mage_guild": {
        "text": "You visit the mage's guild and seek guidance. The mage offers to enchant your weapon to help you on your quest. Do you accept the enchantment or leave the guild without it?",
        "choices": {
            "accept enchantment": "enchanted_weapon",
            "continue without enchantment": "city_market",
        },
    },
    "treasure_map": {
        "text": "You buy the map and learn that the Crown might be hidden in the cursed Forest of Shadows. Your adventure leads you to the dark forest. As you enter, you must decide between two paths. Which way will you go?",
        "choices": {
            "follow the moonlit path": "moonlit_path",
            "enter the cave of whispers": "cave_of_whispers",
        },
    },
    "enchanted_weapon": {
        "text": "With an enchanted weapon, you feel more confident in your abilities. You leave the mage's guild and head towards the Forest of Shadows to find the Crown. As you enter the forest, you face a choice.",
        "choices": {
            "follow the moonlit path": "moonlit_path",
            "enter the cave of whispers": "cave_of_whispers",
        },
    },
    "city_market": {
        "text": "You visit the city's bustling market, where you can purchase supplies or listen to rumors. What's your next move?",
        "choices": {
            "buy supplies": "buy_supplies",
            "listen to rumors": "city_rumors",
        },
    },
    "moonlit_path": {
        "text": "You follow the moonlit path and soon encounter a pack of wolves. You must decide whether to fight or try to evade them.",
        "choices": {
            "fight the wolves": "wolf_fight",
            "evade the wolves": "wolf_evasion",
        },
    },
    "cave_of_whispers": {
        "text": "You enter the eerie Cave of Whispers. Inside, you find strange, glowing mushrooms. Do you eat one of the mushrooms or continue through the cave?",
        "choices": {
            "eat a mushroom": "mushroom_effect",
            "continue through the cave": "cave_exit",
        },
    },
    "buy_supplies": {
        "text": "You purchase supplies to prepare for your journey. Now equipped, you can make your way to the Forest of Shadows. Which path will you choose in the forest?",
        "choices": {
            "follow the moonlit path": "moonlit_path",
            "enter the cave of whispers": "cave_of_whispers",
        },
    },
    "city_rumors": {
        "text": "You hear rumors of a hermit in the Forest of Shadows who possesses knowledge about the Crown's location. Will you seek out the hermit or explore the forest on your own?",
        "choices": {
            "find the hermit": "forest_hermit",
            "explore alone": "moonlit_path",
        },
    },
    "wolf_fight": {
        "text": "You choose to fight the wolves. After a fierce battle, you emerge victorious. Your journey continues deeper into the forest.",
        "choices": {
            "proceed into the forest": "crown_location",
        },
    },
    "wolf_evasion": {
        "text": "You skillfully evade the wolves and continue through the forest. Your path leads you to a mysterious cave entrance. Will you enter the cave?",
        "choices": {
            "enter the cave": "cave_of_mysteries",
            "continue through the forest": "crown_location",
        },
    },
    "mushroom_effect": {
        "text": "You eat a glowing mushroom and feel a surge of energy. The effects are temporary, but you proceed through the cave with newfound vigor. The cave leads you to a hidden part of the forest.",
        "choices": {
            "continue exploring": "hidden_glade",
        },
    },
    "cave_exit": {
        "text": "You decide not to eat the mushrooms and continue through the cave, which leads to an exit in the forest. You are one step closer to your destination.",
        "choices": {
            "proceed into the forest": "crown_location",
        },
    },
    "forest_hermit": {
        "text": "You decide to find the hermit in the Forest of Shadows. The hermit provides you with a riddle that hints at the Crown's location. You continue your quest.",
        "choices": {
            "proceed into the forest": "crown_location",
        },
    },
    "cave_of_mysteries": {
        "text": "You enter the cave of mysteries, which is filled with ancient artifacts. While exploring, you discover a valuable relic that could aid you on your quest.",
        "choices": {
            "take the relic": "relic_aid",
            "exit the cave": "crown_location",
        },
    },
    "hidden_glade": {
        "text": "You arrive at a hidden glade where you find a mysterious well. You can choose to drink from the well or leave it alone.",
        "choices": {
            "drink from the well": "well_effect",
            "leave it alone": "crown_location",
        },
    },
    "relic_aid": {
        "text": "You take the valuable relic with you, and it enhances your abilities. You continue your quest with newfound strength and determination.",
        "choices": {
            "proceed into the forest": "crown_location",
        },
    },
    "well_effect": {
        "text": "You drink from the well and feel a magical surge of power. The well's magic enhances your abilities, making you better equipped to continue your quest.",
        "choices": {
            "proceed into the forest": "crown_location",
        },
    },
    "crown_location": {
        "text": "You follow the hints, riddles, and your own intuition and discover the hidden location of the Crown of Destiny. You've succeeded in your quest and saved the realm of Eldoria!",
        "end": True,
    },
}

# Functions to handle user interaction and game logic
def display_choices(choices):
    print("Available choices:")
    for choice in choices:
        print(f"- {choice}")

def play_game():
    current_scene = "start"

    while True:
        scene = story[current_scene]
        print(scene["text"])

        if "choices" in scene:
            display_choices(scene["choices"])
            choice = input("Choose your path: ").lower()

            if choice in scene["choices"]:
                current_scene = scene["choices"][choice]
            else:
                print("Invalid choice. Try again.")
        elif "end" in scene:
            print("Congratulations! You've completed your epic quest.")
            break

if __name__ == "__main__":
    print("Welcome to the Text Adventure Game!")
    play_game()
