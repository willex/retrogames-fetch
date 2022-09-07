# fetch-retrogames

This is a simple (& still janky :P) python script I wrote to streamline platform collection downloads for a MISTER <> RetroNas/Synology/QNAP setups. It is also really useful for Everdrives, ODEs or any other flash carts though.

Some links might've expired since the last time I updated the script - if you run into any issues just file a bug and I'll have a look at it.

## Main features:
- Comprehensive curated list of popular systems
- Simple lightweight python script that can be used easily
- Easy download without the need of torrent or endless clicks

> !!! THIS IS NOT INTENDED TO FACILITATE PIRACY AND YOU SHOULD ONLY USE THIS FOR PLATFORMS & GAMES THAT YOU PHYSICALLY OWN !!!

## Installation:

```
pip3 install -r requirements.txt
```

Usage:
usage is fairly straight forward. Put the script into the directory you want to download to and run it via:

```
python3 download_games_libs.py
```

You'll be presented with a list of supported platforms and prompted to enter
```
WELCOME TO THE JANKY INTERNET ARCHIVE GAME DOWNLOAD SCRIPT :P!

[0] 3DO
[1] Atari Jaguar
[2] Neo Geo (AES)
[3] Sega Master System
[4] Sega Genesis
[5] Sega CD
[6] Sega 32X
[7] Sega Saturn
[8] Sega DreamCast
[9] TurboGrafx16
[10] TurboGrafx16 CD
[11] Sony PlayStation (1-G)
[12] Sony PlayStation (H-P)
[13] Sony PlayStation (Q-Z)
[14] Sony PlayStation 2 (Part 1)
[15] Sony PlayStation 2 (Part 2)
[16] Sony PlayStation 3 (#-C)
[17] Sony PlayStation 3 (C-D)
[18] Sony PlayStation 3 (D-G)
[19] Sony PlayStation 3 (G-J)
[20] Sony PlayStation 3 (J-M)
[21] Sony PlayStation 3 (M-N)
[22] Sony PlayStation 3 (N-R)
[23] Sony PlayStation 3 (R-S)
[24] Sony PlayStation 3 (S-T)
[25] Sony PlayStation 3 (T)
[26] Sony PlayStation 3 (T-Z)
[27] Sony PlayStation Portable (US)
[28] Sony PlayStation Portable (JP)
[29] Sony PlayStation Portable (EU)
[30] Nintendo Entertainment System (NES)
[31] Super Nintendo (SNES)
[32] Super Nintendo (SNES) MSU-1
[33] Nintendo 64 (US/JP/EU)
[34] Nintendo GameCube (US)
[35] X68000
[36] Translated Roms (Multiple Systems)
[37] Translated Roms (Xbox)
[38] Translated Roms (Xbox 360)
[39] Translated Roms (NEC - PC Engine)
[40] Translated Roms (Nintendo GameCube)
[41] Translated Roms (Nintendo Wii)
[42] Translated Roms (Sega MegaCD)
[43] Translated Roms (Sega Saturn)
[44] Translated Roms (Sega DreamCast)
[45] Translated Roms (Sony PlayStation)
[46] Translated Roms (Sony PlayStation 2)
[47] Translated Roms (Sony PlayStation 3)
[48] Translated Roms (Sony PlayStation Portable)

Which library do you want to download: 6

You entered '6' for 'Sega 32X'. Are you sure you want to start the download (Y/N): Y

WOOHOO!!!! Starting download for 'Sega 32X' library:

Downloading Sega 32X/After Burner Complete _ After Burner (Japan, USA).7z from: https://archive.org/download/Sega-32x-Romset-us/After%20Burner%20Complete%20_%20After%20Burner%20%28Japan%2C%20USA%29.7z
```
Simply enter the number hit `Y` and off you go.

> *NOTE*: If you stop the script and resume it will skip existing games in the folder already.


## TODO / added soon:
- better retry logic if connection is interrupted
- parallel downloads
- integration into Synology (maybe create a DSM package)
