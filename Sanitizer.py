import os


def reversefile(in_name, out_name):
    with open(in_name, "rt") as in_f, open(out_name, "wt") as out_f:
        for line in in_f:
            line = line.strip()
            reversed_line = ''.join(reversed(line))
            out_f.write(reversed_line + "\n")


def replacer(replace1, replace2, file1, file2, n=''): 
    replacements = {replace1: replace2}
    with open(file1) as infile, open(file2, 'w') as outfile:
        for line in infile:
            for src, target in replacements.items():
                line = line.replace(src, target, n) #number of . to change
                outfile.write(line)


def cleaninput(file):
    file = open(file, "w")
    file.close()

replacer('[.]', '.', 'C:/Users/-/inputfile.txt',  # read file and clean [.]
         'C:/Users/-/inputfileclean.txt',-1)
reversefile("inputfileclean.txt", "backward.txt")
replacer('.', '].[', 'C:/Users/-/backward.txt',  # read backward file and replace . with [.]
         'C:/Users/-/inputfile.txt',1)
reversefile("inputfile.txt", "outputfile.txt")
cleaninput('inputfile.txt')  # clean input
os.remove("backward.txt")  # delete file used
os.remove('inputfileclean.txt')  # delete file used
print("All Sanitized")
input('Press Enter to exit...')
