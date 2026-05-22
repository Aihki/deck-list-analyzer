import os
from deck_parse import parse_decklist
from display import display_deck


    
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
