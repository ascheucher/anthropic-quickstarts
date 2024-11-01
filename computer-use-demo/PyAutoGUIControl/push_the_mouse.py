#!/usr/bin/env python3

import pyperclip
from email import message
import os
import re
import json
from platform import node
from time import sleep
from dotenv import load_dotenv
from firefox_remote import *
  

def load_history_paths():
  with open('history_page_paths.json', 'r') as file:
      return json.load(file)

def clear_terminal():
    os.system('clear')
    
def print_wait():
  clear_terminal()
  print("WAIT")

def print_done():
  clear_terminal()
  print("DONE")
  
def clean_input(input: str) -> str:
  unwanted = "The operation was completed."
  str = input.strip()
  if(str.startswith(unwanted)):
    return str[len(unwanted):]
  return str
  
def get_history_id_from(url):
  pattern = r"(?<=/logs/)[^?]+"
  match = re.search(pattern, url)
  if match:
      extracted_part = match.group(0)
      return extracted_part
  else:
    raise RuntimeError("malformed URL")
  
def click_telegram_status():
  pyautogui.click(98, 460)

OUTPUTDIR = "done"

def write_outfile(id: str, url: str, telegram_text: str):
  os.makedirs(OUTPUTDIR, exist_ok=True)
  file_path = os.path.join(OUTPUTDIR, f"{id}.json")    
  data = {
    "id": id,
    "url": url,
    "telegram_text": telegram_text
  }
  with open(file_path, 'w') as outfile:
    json.dump(data, outfile, indent=2)
  
  print(f"Data written to {file_path}")


def main():
  # Load environment variables from .env file
  load_dotenv()

  make_email = os.getenv('MAKE_EMAIL')
  make_pwd = os.getenv('MAKE_PWD')

  display_num = os.getenv('DISPLAY_NUM')
  display_height = os.getenv('HEIGHT')
  display_width = os.getenv('WIDTH')

  print(f"Display Number: {display_num}")
  print(f"Height: {display_height}")
  print(f"Width: {display_width}")
  
  os.makedirs(OUTPUTDIR, exist_ok=True)

  wh = pyautogui.size()
  print(f"{wh}")
  sleep(2)
  print_wait()
  
  open_firefox("make.com")
  accept_make_dot_com_cookies()
  press_login_button()
  sleep(2)
  enter_credentials_and_press_login(make_email, make_pwd)
  sleep(2)
  press_don_safe_credentials()
  sleep(1)
  paths = load_history_paths()
  
  focus_terminal()
  for idx, path in enumerate(paths):
    url = f"https://eu2.make.com{path}"
    try:
      id = get_history_id_from(url)
      focus_firefox()
      open_new_tab_or_select_second_tab_n_load_url(url)
      sleep(5)
      click_telegram_status()
      screenshot_wih_cross(OUTPUTDIR, id)
      sleep(1) # TODO increase to 120 to have time to paste in the prompt and also let claude do it's thing
      press_button('f12')
      click_in_console()
      sleep(2)
      switch_from_inspector_to_console()
      click_in_console() # TODO 1. fix the coordinates
      open_message()
      copy_text_to_clipboard()
      press_button('f12')
      focus_terminal()
      telegram_text = pyperclip.paste()
      print(f"Telegram text: {telegram_text}")
      cleaned_telegram_text = clean_input(telegram_text)
      write_outfile(id, url, cleaned_telegram_text)
      print_done()
    
    except RuntimeError as e:
      print(f"failure in url: {url}")
      
    if(idx > 0):
      print("we are finished")
      exit(0)

main()