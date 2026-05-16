import os
import re
from collections import Counter

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

def display_deck(deck):
    """Display the parsed deck in a readable format."""
    print("\n" + "="*80)
    print("decklist:")
    print("="*80)
    
    mid = len(deck) // 2
    left = deck[:mid]
    right = deck[:mid]
    
    total_cards = 0
    for (count1, name1), (count2, name2) in zip(left, right):
        line1 = f"{count1:2d}x {name1}"
        line2 = f"{count2:2d}x {name2}"
        print(f"{line1:<40}{line2}")
        total_cards += count1 + count2
        
    if len(left) != len(right):
        count,name = right[-1]
        print(f"{count2:2d}x {name}")
        total_cards += count
    
    print("="*80)
    print(f"Total cards in deck: {total_cards}")
    print("="*80)
    
    
    
def main():
    print("Add deck list file:")
    filename = input().strip()
    
    try:
        with open(filename, 'r') as file:
            deck_text = file.read()  
        deck = parse_decklist(deck_text)
        display_deck(deck)
        if os.path.exists(filename):
            os.remove(filename)
            print(f"file {filename} was removed")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found ")
    except Exception as e:
        print(f"Error reading file: {e}")

if __name__ == "__main__":
    main()
