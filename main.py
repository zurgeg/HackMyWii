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
print(startup)
import os
import wget
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
  
  
