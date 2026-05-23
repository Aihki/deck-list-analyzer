def display_deck(deck):
    """Display the parsed deck in a readable format."""
    print("\n" + "="*80)
    print("decklist:")
    print("="*80)
    
    mid = len(deck) // 2
    left = deck[:mid]
    right = deck[mid:]
    
    total_cards = 0
    for (count1, name1), (count2, name2) in zip(left, right):
        line1 = f"{count1:2d}x {name1}"
        line2 = f"{count2:2d}x {name2}"
        print(f"{line1:<40}{line2}")
        total_cards += count1 + count2
        
    if len(left) != len(right):
        count,name = right[-1]
        print(f"{count:2d}x {name}")
        total_cards += count
    
    print("="*80)
    print(f"Total cards in deck: {total_cards}")
    print("="*80)
    