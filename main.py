startup = ```
--------------------
HACK YOUR WII
--------------------
This tool assumes you have Letterbomb downloaded and extracted from please.hackmii.com.
It should be in a folder called LetterBomb when you are finished
```
check_letterbomb = ```
--------------------
CHECK FOR REQUIRED
FILES
--------------------
Press 1 to start
Press 2 to exit
```
get_osc = ```
--------------------
OPEN SHOP CHANNEL
--------------------
The Open Shop Channel allows you to download Homebrew from your Wii.
Press 1 to download it (recommended)
Press 2 to cancel
```
get_priiloader = ```
--------------------
PRIILOADER
--------------------
Priiloader provides brick protection for your console.
Press 1 to download it (recommended)
Press 2 to cancel (NOT RECOMMENDED)
```
sd_letter = 
```
--------------------
SD CARD
--------------------
Insert your SD card and type it's drive letter.
Example: D:/
```
def download(osc,prii,sd):
    print('Will download to:',sd)
    if os.path.exists('LetterBomb'):
      print('Found Letterbomb!')
      print('Copying to SD card...')
      os.path.copy('LetterBomb/private',sd + 'private')
      print('Complete!')
      os.mkdir(sd + 'apps')
      if prii = '1':
        print('Downloading Priiloader\nPlease wait...')
        wget.download('https://wii.guide/assets/files/Priiloader_v0_8_2.zip', sd + 'priiloader.zip')
        print('Downloaded Priiloader! Extracting\nPlease wait...')
        with ZipFile(sd + 'priiloader.zip', 'r') as zpObj:
          zipObj,extractall(sd)
        print('SUCCESS!')
      if osc == '1':
        print('Downloading Open Shop Channel\nPlease wait...')
        wget.download('https://wii.guide/assets/files/homebrew_browser_v0.3.9e.zip',sd + 'homebrew_browser.zip')
        print("Downloaded! Extracting\nPlease wait...')
        with ZipFile(sd + 'homebrew_browser.zip', 'r') as zipObj:
         # Extract all the contents of zip file into apps folder
         zipObj.extractall(sd + 'apps')
        print('SUCCESS!')
      print('Your download was complete!')
      print('''
      --------------------
      INSTALLING HOMEBREW
      CHANNEL
      --------------------
      This will install the Homebrew Channel on your Wii!
      Step 1: Eject your SD card and put it into your Wii
      Step 2: Go to the mail icon
      Step 3: Go a day back and look for the red letter
      Step 3a: If you see it, open it and procced to step 4
      Step 3b: If you don't see it, go a day forward, and open it if you see it, and procced to step 4
      Step 3c: If you still don't see it, go another day forward, and it should be there, if it's not, you did it wrong. Restart this guide.
      Step 4: When it warns you about paying for this software, wait around 30-60 seconds until you see "Press [1] to continue"
      Step 5: Press 1 on your Wii Remote
      Step 6: Use your Wii Remote to select Install The Homebrew Channel, and hit A
      Step 7: Press Yes
      Step 8: Press Continue
      Step 9: Use your Wii Remote to select BootMii, and hit A
      Step 10: Select Install BootMii as IOS 
      Step 11: Select Yes
      Step 12: Select Continue
      Step 13: Select Exit
      Step 14: Select Exit again
      Step 15: You are now in the Homebrew Channel, hit the HOME button
      Step 16: Hit the "Launch BootMii button" 
      Step 16a: If you have a GameCube controller, use it to select the gear and then select the SD card with the Green Arrow
      Step 16b: If you don't have a GameCube controller, use the POWER button to navigate right to the gear and press Reset, then use the POWER button to navigate right to the SD card with the green arrow and press Reset
      Step 17: Wait until the you see the option to exit by pressing any button
      Step 18: Navigate Right using either POWER or Right on your GameCube controller's D-Pad to the Back Arrow
      Step 19: Navigate Right to the Wii Logo and press Select (Reset/A)
      Step 20: Connect your Wii Remote and launch the Homebrew Channel
      Step 21: Launch Priiloader
      Step 22: Hit A 
      Step 23: Hit A again when it tells you SUCCESS
      Step 24: Now you can launch Open Shop Channel (Might be called Homebrew Browser)
      Step 25: You have Homebrewed your Wii! If you need help, follow wii.guide for more info!
      
      
              
        
        
    else:
      print('Letterbomb was not found, the program will now exit')
      exit()
print(startup)
import os.path
import wget
from zipfile import ZipFile
#wget.download(url, 'filepath')
print(check_letterbomb)
answer = input()
if answer == "1":
  print(get_osc)
  osc = input()
  print(get_priiloader)
  prii = input()
  print(sd_letter)
  sd = input()
  config = "--------------------\nCONFIGURATION\n--------------------\nOPEN SHOP CHANNEL: " + osc + "\n" + "PRIILOADER: " + prii + "\nSD Card" + sd
  print(config)
  print("Is this correct? (y/n)")
  confirm = input()
  if confirm == "y":
    print("Now downloading!")
    download(osc,prii,sd)
  else:
    print('The program will now exit, rerun to change configuration')
else:
  print('Ok! Bye!')
  exit()
  
  
