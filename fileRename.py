import os
import shutil

olddir = "E:/School/2015-2016/English 2H/Raw/"
newdir = "E:/School/2015-2016/English 2H/Mullen/"

print ("Preparing to rename files")

for filename in os.listdir(olddir):
    print (filename)
    if filename.endswith(".docx"):
        shutil.copyfile(olddir + filename, newdir + filename)
        os.rename(newdir + filename, newdir + "HARRIS_" + filename)


