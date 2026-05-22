import re

def parse_decklist(deck_list):
    deck = []
    for line in deck_list.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        match = re.match(r"(\d+) (.+)", line)
        if match:
            count = int(match.group(1))
            name = match.group(2)
            deck.append((count, name))
    return deck