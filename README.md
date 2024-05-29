# teddybear_wingmanai_configs
 Hosts config files for wingmen created by teddybear082


Steps to use:

1. Download this repository and unzip somewhere on your computer.

2. Put the Borderlands, No Man's Sky and Windows folders (or whichever you choose) into your Wingmanai User Directory.  This is typically **%AppData%/Roaming/ShipBit/WingmanAI/[release number]/configs**:

![image](https://github.com/teddybear082/teddybear_wingmanai_configs/assets/87204721/fa3a0ddf-c950-4cc2-a6af-d85374e63d03)


Then put the typing_assistant skill folder and web_search folder into your Wingmanai User Directory.  This is typically **%AppData%/Roaming/ShipBit/WingmanAI/[release number]/skills**:

![image](https://github.com/teddybear082/teddybear_wingmanai_configs/assets/87204721/40ab4f0f-5234-45d9-8f10-392832f750fe)


3. Go to the releases section of the github repo here:  https://github.com/teddybear082/teddybear_wingmanai_configs/releases/tag/voice_files and download the voice_files zip.

4. Unzip the voice files zip into your xvasynth directory (at the base/root folder, where your xvasynth.exe folder is).  This should put the new voice folders in your resources/app/models directory automatically.  To check that it unzipped correctly, go to xvasynth/resources/app/models and see if you now have an "other" and "borderlands" directory.

![image](https://github.com/teddybear082/teddybear_wingmanai_configs/assets/87204721/881a2e5b-9089-4034-8213-a8c7a2aa72b5)


5. In the Borderlands and No Man's Sky folders in your wingman ai configs, you will find files named **Marcus.yaml** and **Suit.yaml**, respectively. Open each with a code editor like Visual Script Code or Notepad++.  At the very bottom you will see this line:
```
xvasynth_path: D:\DExtraSteamGames\steamapps\common\xVASynth  
```
Change that to the path to your xvasynth game folder instead in both files.

6. These wingmen are configured to use whispercpp in voice activation mode. If you do not want to use this, then find the part in each wingman config that looks like this:

```
features:
  conversation_provider: wingman_pro
  debug_mode: false
  stt_provider: whispercpp
  summarize_provider: wingman_pro
  tts_provider: xvasynth
```  

And change stt_provider to wingman_pro instead of whispercpp.

7. Now run wingman AI and, if there were no installation errors in the install, you should now be able to use these additional wingmen.  If you load a wingman, like the Clippy wingman or try to use a skill, like the web_search skill in another wingman, and WingmanAI indicates there are errors due to missing modules, then download this release of additional files here: https://github.com/teddybear082/teddybear_wingmanai_configs/releases/download/_internal_wingman_ai_folder_additions/add_to_wingman_internal_folder.zip and unzip the files contained in there into your _internal folder that is in the wingmanai install directory (same location as WingmanAI.exe and WingmanAiCore.exe).  That adds the additional built-in python libraries for Python 3.11.7 that are not bundled with WingmanAI because they are not used by the core WingmanAI functions.

8. Note that you can make further adjustments to the Wingmen, and possibly make the config changes above, with the WingmanAI user interface, and without manually editing the .yaml files.
