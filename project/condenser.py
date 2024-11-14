import os


def assimilate(source, dest):
    for filename in os.listdir(source):
        f = os.path.join(source, filename)

        #we want it to not read compiled files
        if f[len(f)-1]!='c':
            # checking if it is a file or a directory
            if os.path.isdir(f):
                assimilate(f, dest)
            if os.path.isfile(f):
                openF = open(f, "r")
                data = openF.readlines()
                dest.writelines(data)
                openF.close()


directory = "scripts"
output = "project/singleScript.rpy"

destFile = open(output, "w+")

assimilate(directory, destFile)