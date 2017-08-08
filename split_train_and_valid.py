import sys
import glob
import random
import os
from os import listdir
import distutils.dir_util
from os.path import *

# path to train
orig_train_dir = abspath (sys.argv[1])

# make cat and dog dirs
# and move all the files accordingly
for sub in ["dog", "cat"]:
    print "Making = %s" % (sub)
    sub_dir = join (orig_train_dir, sub+"s")
    distutils.dir_util.mkpath (sub_dir)
    file_list = [ f for f in listdir (orig_train_dir) if (isfile (join (orig_train_dir, f)) and sub in f) ]

    for f in file_list:
        src = join (orig_train_dir, f)
        dst = join (sub_dir, f)
        os.rename (src, dst)
        print "Moved %s to %s" % (src, dst)

# Now split some of train to valid
orig_valid_dir = join (dirname (orig_train_dir), "valid")
move_num       = int (sys.argv[2])

for sub in listdir (orig_train_dir):
    print "Doing sub category = %s" % (sub)
    
    sub_train_dir = join (orig_train_dir, sub)
    
    if (isdir (sub_train_dir)):
        sub_valid_dir = join (orig_valid_dir, sub)
        distutils.dir_util.mkpath (sub_valid_dir)

        file_list = [f for f in listdir(sub_train_dir) if isfile(join(sub_train_dir, f))]
        random.shuffle (file_list)
        
        for i in range (move_num):
            src = "%s/%s" % (sub_train_dir, file_list[i])
            dst = "%s/%s" % (sub_valid_dir, file_list[i])
            os.rename (src, dst)
            print "[%4d] Moved %s to %s" % (i, src, dst)

