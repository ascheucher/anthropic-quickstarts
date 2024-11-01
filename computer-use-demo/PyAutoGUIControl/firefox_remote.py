import os
from PIL import Image, ImageDraw
import pyautogui
from time import sleep

def screenshot_wih_cross(path: str, id: str):
  x,y = pyautogui.position()
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
  path = os.path.join(path, f"id-{x}-{y}.png")
  combined.save(path)

def move_mouse_and_click(x,y):
  pyautogui.click(x,y)

def open_bash_terminal():
  pyautogui.click(750, 738, duration=0.5)
  
def focus_terminal():
  pyautogui.click(200, 738, duration=0.5)
  
def type_and_execute_in_terminal(command):
  pyautogui.write(command)
  
  pyautogui.keyDown('enter')
  sleep(0.2)
  pyautogui.keyUp('enter')

def press_button(char):
  pyautogui.keyDown(char)
  sleep(0.2)
  pyautogui.keyUp(char)

def enter_url(url):
  # activate the browser URL bar
  pyautogui.click(512, 101, duration=5)
  
  # copy in the URL
  pyautogui.write(url)
  press_button('enter')  

def open_firefox(url):
  print(f"opening firefox and opening {url}")
  # open firefox
  pyautogui.click(805, 738, duration=0.25)  
  if(url):
    enter_url(url)

def focus_firefox():
  pyautogui.click(600, 738, duration=0.25)  

def open_new_tab_or_select_second_tab_n_load_url(url):
  print(f"open a firefox tab with: {url}")
  # click the + (new tab) button
  pyautogui.click(289, 58, duration=0.25)
  enter_url(url)
  
def accept_make_dot_com_cookies():
  pyautogui.click(727, 386, duration=.25)

def press_login_button():  
  pyautogui.click(792, 163, duration=.25)
  
def enter_credentials_and_press_login(email, pwd):
  pyautogui.click(293, 341)
  pyautogui.write(email)
  pyautogui.click( 293, 423)
  pyautogui.write(pwd)
  pyautogui.click(293, 496)

def press_don_safe_credentials():
  pyautogui.click(469, 359)

def switch_from_inspector_to_console():
  pyautogui.click(170, 471) # TODO fix xy
  
def click_in_console():
  pyautogui.click(30, 675) # TODO fix xy

def move_mouse_to(x,y):
  pyautogui.moveTo(x,y)
  
def open_message():
  pyautogui.write('jQuery("span:contains(\'Message\')").parent().click()')
  press_button('enter')
  
def copy_text_to_clipboard():
  pyautogui.write('copy(jQuery("span:contains(\'Text\')").parent().next().text())')
