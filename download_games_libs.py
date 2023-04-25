import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import requests
import os
from os import path
import signal
import sys

# LIBS CONFIG
download_options = [
    ['3DO', 'https://archive.org/download/Panasonic-3DO-Redump.org-2019-05-14'],
    ['Atari Jaguar', 'https://archive.org/download/AtariJaguarReuploadByGhostware'],
    ['Neo Geo (AES)', 'https://archive.org/download/NeoGeoRomCollectionByGhostware'],
    ['Neo Geo (CD)', 'https://archive.org/download/redump.ngcd.revival'],
    ['Sega Master System', 'https://archive.org/download/SegaMasterSystemCollectionByGhostware'],
    ['Sega Genesis', 'https://archive.org/download/SegaGenesisMegaDriveRomCollectionByGhostware'],
    ['Sega CD', 'https://archive.org/download/SegaCDCollection'],
    ['Sega 32X', 'https://archive.org/download/Sega-32x-Romset-us'],
    ['Sega Saturn', 'https://archive.org/download/redump.ss'], #'https://archive.org/download/SegaSaturnRomCollectionByGhostware'],
    ['Sega DreamCast', 'https://archive.org/download/DreamcastCollectionByGhostwareMulti-region'],
    ['TurboGrafx16', 'https://archive.org/download/NECPCEngineTurboGrafx16Complete'],
    ['TurboGrafx16 CD', 'https://archive.org/download/TurboGrafxCDCollection'],
    ['Sony PlayStation (USA)', 'https://archive.org/download/rr-sony-playstation-u/usa/'],
    ['Sony PlayStation 2 (Part 1)', 'https://archive.org/download/RedumpSonyPS2NTSCU'],
    ['Sony PlayStation 2 (Part 2)', 'https://archive.org/download/RedumpSonyPS2NTSCUPart2'],
    ['Sony PlayStation 3 (#-C)','https://archive.org/download/PS3_ALVRO_PART_1'],
    ['Sony PlayStation 3 (C-D)','https://archive.org/download/PS3_ALVRO_PART_2'],
    ['Sony PlayStation 3 (D-G)','https://archive.org/download/PS3_ALVRO_PART_3'],
    ['Sony PlayStation 3 (G-J)','https://archive.org/download/PS3_ALVRO_PART_4'],
    ['Sony PlayStation 3 (J-M)','https://archive.org/download/PS3_ALVRO_PART__5'],
    ['Sony PlayStation 3 (M-N)','https://archive.org/download/PS3_ALVRO_PART_6'],
    ['Sony PlayStation 3 (N-R)','https://archive.org/download/PS3_ALVRO_PART_7'],
    ['Sony PlayStation 3 (R-S)','https://archive.org/download/PS3_ALVRO_PART_8'],
    ['Sony PlayStation 3 (S-T)','https://archive.org/download/PS3_ALVRO_PART_9'],
    ['Sony PlayStation 3 (T)','https://archive.org/download/PS3_ALVRO_PART_10'],
    ['Sony PlayStation 3 (T-Z)','https://archive.org/download/PS3_ALVRO_PART_11'],
    ['Sony PlayStation Portable (US)','https://archive.org/download/rr-sony-playstation-portable/usa/'],
    ['Sony PlayStation Portable (JP)','https://archive.org/download/rr-sony-playstation-portable/japan/'],
    ['Sony PlayStation Portable (EU)','https://archive.org/download/rr-sony-playstation-portable/europe/'],
    ['Nintendo Entertainment System (NES)', 'https://archive.org/download/NintendoMultiRomCollectionByGhostware'],
    ['Super Nintendo (SNES)', 'https://archive.org/download/SuperNintendoMultiRegionSetByGhostware'],
    ['Super Nintendo (SNES) MSU-1', 'https://archive.org/download/SNES-MSU1-Arquivista'],
    ['Nintendo 64 (US/JP/EU)', 'https://archive.org/download/Nintendo64V2RomCollectionByGhostware'],
    ['Nintendo GameCube (US)', 'https://archive.org/download/gamecubeusaredump'],
    ['X68000', 'https://archive.org/download/SharpX68000RomCollectionByGhostware'],
    ['Translated Roms (Multiple Systems)', 'https://archive.org/download/En-ROMs/En-ROMs/'],
    ['Translated Roms (Xbox)', 'https://archive.org/download/En-ROMs/En-ROMs/Microsoft%20-%20XBOX%20%5BT-En%5D%20Collection/'],
    ['Translated Roms (Xbox 360)', 'https://archive.org/download/En-ROMs/En-ROMs/Microsoft%20-%20XBOX%20360%20%5BT-En%5D%20Collection/'],
    ['Translated Roms (NEC - PC Engine)', 'https://archive.org/download/En-ROMs/En-ROMs/NEC%20-%20PC%20Engine%20CD%20%5BT-En%5D%20Collection/'],
    ['Translated Roms (Nintendo GameCube)', 'https://archive.org/download/En-ROMs/En-ROMs/Nintendo%20-%20GameCube%20%5BT-En%5D%20Collection/'],
    ['Translated Roms (Nintendo Wii)', 'https://archive.org/download/En-ROMs/En-ROMs/Nintendo%20-%20Wii%20%5BT-En%5D%20Collection/'],
    ['Translated Roms (Sega MegaCD)', 'https://archive.org/download/En-ROMs/En-ROMs/Sega%20-%20Mega%20CD%20%5BT-En%5D%20Collection/'],
    ['Translated Roms (Sega Saturn)', 'https://archive.org/download/En-ROMs/En-ROMs/Sega%20-%20Saturn%20%5BT-En%5D%20Collection/'],
    ['Translated Roms (Sega DreamCast)', 'https://archive.org/download/En-ROMs/En-ROMs/Sega%20-%20Dreamcast%20%5BT-En%5D%20Collection/'],
    ['Translated Roms (Sony PlayStation)', 'https://archive.org/download/En-ROMs/En-ROMs/Sony%20-%20PlayStation%20%5BT-En%5D%20Collection/'],
    ['Translated Roms (Sony PlayStation 2)', 'https://archive.org/download/En-ROMs/En-ROMs/Sony%20-%20PlayStation%202%20%5BT-En%5D%20Collection/'],
    ['Translated Roms (Sony PlayStation 3)', 'https://archive.org/download/En-ROMs/En-ROMs/Sony%20-%20PlayStation%203%20%5BT-En%5D%20Collection/'],
    ['Translated Roms (Sony PlayStation Portable)', 'https://archive.org/download/En-ROMs/En-ROMs/Sony%20-%20PlayStation%20Portable%20%5BT-En%5D%20Collection/'],
    ['Magazines - Nintendo Power Issues', 'https://archive.org/download/Nintendo_Power_Issue001-Issue127']
]


def start_download(folder_name, url):
    http = httplib2.Http()
    status, response = http.request(url)

    try:
        os.mkdir(folder_name)
    except OSError as e:
        pass

    for link in BeautifulSoup(response, parse_only=SoupStrainer('a'), features="html.parser"):
        if link.has_attr('href'):
            if not 'Contents' in str(link):
                for file_format in ['.zip', '.7z', '.rar', '.j64', '.iso', '.pdf', '.cbr']:
                    if file_format in str(link).lower():
                        file_name = '%s/%s' % (folder_name, link.text)
                        file_url = '%s/%s' % (url, link['href'])

                        # check if file already exists
                        if path.isfile(file_name):
                            print('Download skipped. File already exists in target directory: %s' % file_name)
                            continue
                        else:
                            # Start Download
                            print('Downloading %s from: %s' % (file_name, file_url))

                            try:
                                r = requests.get(file_url)
                                with open(file_name, 'wb') as f:
                                    f.write(r.content)
                            except:
                                print('>>>> ERROR: Failed to download: %s' % file_url)
    else:
        exit()


def signal_handler(sig, frame):
    print('\n\nEXITING SCRIPT! Byeeeeeeeeeeeeeeeeeeee\n')
    sys.exit(0)


if __name__ == "__main__":

    signal.signal(signal.SIGINT, signal_handler)

    print("\nWELCOME TO THE JANKY INTERNET ARCHIVE GAME DOWNLOAD SCRIPT :P!\n")
    max_input = len(download_options)
    for idx, val in enumerate(download_options):
        print('[%s] %s' % (idx, val[0]))

    lib_selection = input("\nWhich library do you want to download: ")

    if not int(lib_selection) >= max_input:
        is_start_download = input("\nYou entered '%s' for '%s'. Are you sure you want to start the download (Y/N): " % (lib_selection, download_options[int(lib_selection)][0]))
        if is_start_download.strip().upper() == 'Y':

            lib_name = download_options[int(lib_selection)][0]
            lib_url = download_options[int(lib_selection)][1]

            print("\nWOOHOO!!!! Starting download for '%s' library:\n" % lib_name)
            start_download(lib_name, lib_url)
        else:
            exit()
    else:
        print('\nPlease select a valid library, dummy!')
