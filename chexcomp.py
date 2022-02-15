import os
import sys




def wb(byte):
    try:
        f = open("test.chexc", "ab")
        f.write(byte)
        f.close()
    except:
        print("something went wrong during the writing process")
        sys.exit(1)
def ewerr(err, errcode, line):
    print("CHex compile error on line " + line + ":" + err)
    sys.exit(errcode)
    


f = open("test.chex", "r")
lines = f.readlines()
f.close()
linenum = 0
os.system("touch test.chexc")
wb(b'hi')
for line in lines:
    linenum += 1
    split = line.split()
    if line == "" or line.startswith(";"):
        pass
    elif line.startswith("pr "):
        if not len(split) == 2:
            ewerr("Wrong args", 5, linenum)
        try:
            hext = b'\x01' + bytes([int(split[1])])
        except:
            ewerr("Can't convert decimal to hex", 4, linenum)
        wb(hext)
    elif line.startswith("jmp "):
        if not len(split) == 2:
            ewerr("Wrong args", 5, linenum)
        try:
            hext = b'\x02' + bytes([int(split[1])])
        except:
            ewerr("Can't convert decimal to hex", 4, linenum)
        wb(hext)
    elif line.startswith("str "):
        if not len(split) == 3:
            ewerr("Wrong args", 5, linenum)
        try:
            hext = b'\x03' + bytes([int(split[1])]) + bytes([int(split[2])])
        except:
            ewerr("Can't convert decimal to hex", 4, linenum)
        wb(hext)
    else:
        ewerr("Unkown command", 10, linenum)
            
        
