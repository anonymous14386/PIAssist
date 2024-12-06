# PIAssist
PI 5 AI assistant

I bought a pi5 recently and I'd like to make an ai assistant with it

I'll put a parts list here and any code in the repo

OS: Raspberry Pi OS


----------
Low power warning
  sudo rpi-eeprom-config -e

  Change the POWER_OFF_ON_HALT=0 to =1
  add "PSU_MAX_CURRENT=5000" to the bottom
  
  reboot

-----------
Wallpaper cred: https://www.reddit.com/r/StableDiffusion/comments/11lhrme/some_trippy_wallpapers_generated_with_leonardoai/#lightbox

----------

Changelog:

#Get some llamas
curl -fsSL https://ollama.com/install.sh | sh
