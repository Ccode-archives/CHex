import os
import sys
import codecs
try:
    file = open(sys.argv[1], "rb")
except:
    print("File does not exist or is not given.")
    sys.exit()
bytecode = file.read()
file.close()
bytecode = list(bytecode)
hexcode = []
for dec in bytecode:
    hexcode += [hex(dec)]
# print(hexcode)

if hexcode[0] == "0x68" and hexcode[1] == "0x69":
    pass
else:
    print("Not a CHex bianary file.")
# set nummbers
offset = 2
memory = {}
while True:
    try:
        hex = hexcode[offset]
    except:
        sys.exit()
    # blank hex
    if hex == "0x0":
        offset += 1
    # test
    elif hex == "0x1":
        # print(memory[int(hexcode[offset + 1][2:], 16)][2:])
        hexval = memory[int(hexcode[offset + 1][2:], 16)][2:]
        if not len(hexval) == 2:
            hexval = "0" + hexval
        print(str(codecs.decode(hexval, "hex"), "utf-8"), end="")
        offset += 2
    elif hex == "0x2":
        offset = int(hexcode[offset + 1], 16)
    elif hex == "0x3":
        memory[int(hexcode[offset + 1], 16)] = hexcode[offset + 2]
        offset += 3
    else:
        print("Unknown command at offset: " + str(offset))
        sys.exit()