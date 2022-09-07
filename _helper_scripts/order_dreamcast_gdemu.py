import os, sys, shutil

def rename_dirs(is_sort_run=False):

    folder_name = 2
    basedir = os.path.dirname(os.path.abspath(__file__)) #'.'
    games = sorted(os.listdir(basedir))

    for fn in games:
      if not os.path.isdir(os.path.join(basedir, fn)):
        continue # Not a directory
      else:
        '''
            Image layout:

            Every image must be put in a separate folder
            Folder names must consist of:
            2 digits for 01 to 99
            3 digits up to 999
            4 digits up to 9999
            All file names must be in DOS 8.3 format
            The main image file must be called “disc” with appropriate extension
        '''
        if not is_sort_run:
            new_folder_name = f'{folder_name:02}' # GDEMU convention
            print('Renaming folder %s to: %s' % (fn, new_folder_name))
            os.rename(fn, new_folder_name)
        else:
            os.rename(fn, '%s_' % fn)
        folder_name += 1


#rename_dirs(True) # run this if you just want to re-order folders for a sort run
rename_dirs(False)
