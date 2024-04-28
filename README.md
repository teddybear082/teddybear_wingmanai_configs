# teddybear_wingmanai_configs
 Hosts config files for wingmen created by teddybear082


Steps to use:

1. Download this repository and unzip somewhere on your computer.

2. Put the Borderlands and No Man's Sky folders (or whichever you choose) into your Wingmanai User Directory.  This is typically **%AppData%/Roaming/ShipBit/WingmanAI/[release number]/configs**:

![image](https://github.com/teddybear082/teddybear_wingmanai_configs/assets/87204721/918d2f9a-3215-415c-804f-9103892b0213)

3. Go to the releases section of the github repo here:  https://github.com/teddybear082/teddybear_wingmanai_configs/releases/tag/voice_files and download the voice_files zip.

4. Unzip the voice files zip into your xvasynth directory (at the base/root folder, where your xvasynth.exe folder is).  This should put the new voice folders in your resources/app/models directory automatically.  To check that it unzipped correctly, go to xvasynth/resources/app/models and see if you now have an "other" and "borderlands" directory.

![image](https://github.com/teddybear082/teddybear_wingmanai_configs/assets/87204721/881a2e5b-9089-4034-8213-a8c7a2aa72b5)


5. In the Borderlands and No Man's Sky folders in your wingman ai configs, you will find files named **Marcus.yaml** and **Suit.yaml**, respectively. Open each with a code editor like Visual Script Code or Notepad++.  At the very bottom you will see this line:
```
xvasynth_path: D:\DExtraSteamGames\steamapps\common\xVASynth  
```
Change that to the path to your xvasynth game folder instead in both files.

6. These wingmen are configure to use whispercpp in voice activation mode. If you do not want to use this, then find the part in each wingman config that looks like this:

```
features:
  conversation_provider: wingman_pro
  debug_mode: false
  stt_provider: whispercpp
  summarize_provider: wingman_pro
  tts_provider: xvasynth
```  

And change stt_provider to wingman_pro instead of whispercpp.

7. Now run wingman AI and, if there were no installation errors in the insall, you should now be able to use these additional wingmen.

8. Note that you can make further adjustments to the Wingmen, and possibly make the config changes above, with the WingmanAI user interface, and without manually editing the .yaml files.
