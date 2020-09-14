
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

    return dirName

def get_filename(filename):

    index = check_path(filename)
    file_name = ''
    if index >= 0:
        file_name = filename[index + 1:]
        return file_name
    else:
        return filename



def get_file_ext(filename):
    try:
        return filename[filename.rindex('.')+1:]
    except:
        return ''


assert(get_dir("log/cups/access_log") == "log/cups/")
assert(get_dir("log/cups/") == "log/cups/")
assert(get_dir("cups/access_log") == "cups/")
assert(get_dir("access_log") == "")
assert(get_filename("log/cups/access_log") == "access_log")
assert(get_filename("log/cups/") == "")
assert(get_filename("cups/access_log") == "access_log")
assert(get_filename("access_log") == "access_log")
assert(get_file_ext("log/cups/access_log") == "")
assert(get_file_ext("base/FileHelper.cpp") == "cpp")
assert(get_file_ext("base/FileHelper.cpp.bak") == "bak")