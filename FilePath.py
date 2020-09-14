import re
import random

def check_path(filename):
    try:
        #integer is index where the last slash is found
        index = filename.rindex('/')
    except ValueError:
        index = -1
    
    return index

def get_dir(filename):
    if len(filename) > 0 and filename[-1] == '/':
        return filename

    index = check_path(filename)

    dirName = ''
    if index >= 0:
        dirName = filename[0: index + 1]
    else:
        dirName = ''

    return dirName

# access_log
def getFilenamePart(sFilename):
    try:
        int(sFilename.rindex('/'))
    except:
        return sFilename

    pos = sFilename.rindex('/')
    base_name = sFilename[pos + 1:]
    return base_name


#.png
def getEndOfFile(sFilename):
    try:
        occurrences = [m.start() for m in re.finditer('\.', sFilename)]
        return sFilename[occurrences[-1] + 1:]
    except:
        pass

    return ''


assert(get_dir("log/cups/access_log") == "log/cups/")
assert(get_dir("log/cups/") == "log/cups/")
assert(get_dir("cups/access_log") == "cups/")
assert(get_dir("access_log") == "")
assert(getFilenamePart("log/cups/access_log") == "access_log")
assert(getFilenamePart("log/cups/") == "")
assert(getFilenamePart("cups/access_log") == "access_log")
assert(getFilenamePart("access_log") == "access_log")
assert(getEndOfFile("log/cups/access_log") == "")
assert(getEndOfFile("base/FileHelper.cpp") == "cpp")
assert(getEndOfFile("base/FileHelper.cpp.bak") == "bak")