import os
import shutil

path = '.'

for filename in os.listdir(path):
    # do your stuff
    dir_name = os.path.splitext(filename)[0]
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    dest = '%s/%s' % (path, dir_name)
    shutil.move(filename, dest)


