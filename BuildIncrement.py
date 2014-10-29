import string
from random import randint

def IncreaseDefine(define, lines):
    for idx, item in enumerate(lines):
        if define in item:
            tmp_str =  item.split()
            tmp_str[2] = str(int(tmp_str[2])+1)+"\n"
            item = ' '.join(tmp_str)
            line[idx] = item
            return int(tmp_str[2])

def ResetDefine(define, lines):
    for idx, item in enumerate(lines):
        if define in item:
            tmp_str =  item.split()
            tmp_str[2] = "0\n"
            item = ' '.join(tmp_str)
            line[idx] = item

fo = open("src\\config.h", "r+")
print "Name of the file: ", fo.name
line = fo.readlines()

rand = randint(1,5)
for a in range(0, rand):
    IncreaseDefine('#define VERSION_REVISION', line)
if IncreaseDefine('#define VERSION_BUILD', line)%100 == 0:
    if IncreaseDefine('#define VERSION_MINOR', line) == 10:
        ResetDefine('#define VERSION_MINOR', line)
        IncreaseDefine('#define VERSION_MAJOR', line)


fo.seek(0)
for idx, item in enumerate(line):
    fo.write(item)
fo.truncate()
fo.close()
