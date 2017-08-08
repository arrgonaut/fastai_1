import sys
import glob
import random
import os
from os import listdir
import distutils.dir_util
from os.path import *
from shutil import copyfile, rmtree

# path to train
base_dir = abspath (sys.argv[1])
samp_dir = join (base_dir, "sample")
samp_train_dir = join (samp_dir, "train")
samp_valid_dir = join (samp_dir, "valid")
copy_num       = int (sys.argv[2])

# make the results dir
result_dir = join (base_dir, "results")
distutils.dir_util.mkpath (result_dir)
result_samp_dir = join (samp_dir, "results")
distutils.dir_util.mkpath (result_samp_dir)

def copy_files (sdir, ddir, msg):
    #rmtree (ddir)
    distutils.dir_util.mkpath (ddir)
    
    file_list = [f for f in listdir(sdir) if isfile(join(sdir, f))]
    random.shuffle (file_list)
    
    for i in range (copy_num):
        src = join (sdir, file_list[i])
        dst = join (ddir, file_list[i])
        copyfile (src, dst)
        print "[%s.%4d] Copy %s to %s" % (msg, i, src, dst)

for kind in ["train", "valid", "test"]:
    print "Doing kind = %s" % (kind)
    kind_base_dir = join (base_dir, kind)
    kind_samp_dir = join (samp_dir, kind)

    if (kind == "test"):
        for sub in ["unknown"]:
            print "Doing sub category = %s" % (sub)
    
            sub_base_dir = kind_base_dir
            sub_samp_dir = join (kind_samp_dir, sub)
            copy_files (sub_base_dir, sub_samp_dir, sub)

    else:
        for sub in listdir (kind_base_dir):
            print "Doing sub category = %s" % (sub)
    
            sub_base_dir = join (kind_base_dir, sub)
            sub_samp_dir = join (kind_samp_dir, sub)
            copy_files (sub_base_dir, sub_samp_dir, sub)
