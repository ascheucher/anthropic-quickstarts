#!/usr/bin/env python3

from PIL import Image, ImageDraw
import pyautogui
from firefox_remote import *

def main():
    pyautogui.moveTo(465, 469, duration=.25)
    #pyautogui.moveTo(85, 469, duration=.25)
    x = 98
    y = 460
    pyautogui.moveTo(x, y, duration=.25)
    
    im = pyautogui.screenshot()
    overlay = Image.new('RGBA', im.size, (255,255,255,0))
    draw = ImageDraw.Draw(overlay)
    # Define the coordinates for the red cross
    cross_center = (x, y)
    cross_size = 20  # Half-length of each arm of the cross
    # Draw the horizontal line of the cross
    draw.line((cross_center[0] - cross_size, cross_center[1], 
            cross_center[0] + cross_size, cross_center[1]), fill='red', width=1)
    # Draw the vertical line of the cross
    draw.line((cross_center[0], cross_center[1] - cross_size, 
           cross_center[0], cross_center[1] + cross_size), fill='red', width=1)
    
    combined = Image.alpha_composite(im.convert('RGBA'), overlay)    
    # Save the resulting image
    combined.save(f"Screenshot_{x}-{y}.png")
    
if __name__ == "__main__":
    main()