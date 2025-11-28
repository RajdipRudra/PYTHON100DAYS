

import time, sys

def type_out(text, delay=0.08):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

lyrics = [
    "Lock me up and throw away the key",
    "He knows how to get the best out of me",
    "I'm no force for the world to see",
    "Trade my whole life just to be",
    "Top of the world but I'm still not free",
    "It's such a secret that I keep",
    "Until it's gone, I can never find peace",
    "Brace my whole life just to be"
]

for line in lyrics:
    type_out("\n"+line)

print("\n")