#!/usr/bin/env python3

import sys
from firefox_remote import *

def main():
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Usage: DISPLAY=:1 ./move_mouse_to.py <x> <y>")
        sys.exit(1)
    
    # Get the command line arguments
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    
    # Example usage of the arguments
    print(f"Moving mouse to coordinates: ({x}, {y})")


    move_mouse_to(x,y)

if __name__ == "__main__":
    main()