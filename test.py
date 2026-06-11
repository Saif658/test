import random

adjectives = ["Crazy", "Silent", "Broken", "Dark", "Neon", "Lost", "Cold", "Wild"]
nouns = ["Coder", "Dev", "Builder", "Hacker", "Ghost", "Wolf", "Mind", "Soul"]
numbers = ["", "404", "99", "777", "01", "X"]

def gen():
    return f"{random.choice(adjectives)}{random.choice(nouns)}{random.choice(numbers)}"

for _ in range(10):
    print(gen())