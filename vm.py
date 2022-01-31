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

# magic number check
if hexcode[0] == "0x68" and hexcode[1] == "0x69":
    pass
else:
    print("Not a CHex bianary file.")
# set offset to 2 because of magic number
offset = 2
# init mem
memory = {}
while True:
    try:
        hex = hexcode[offset]
    except:
        sys.exit()
    # blank hex
    if hex == "0x0":
        offset += 1
    # print ascii from memory
    elif hex == "0x1":
        # print(memory[int(hexcode[offset + 1][2:], 16)][2:])
        hexval = memory[int(hexcode[offset + 1][2:], 16)][2:]
        if not len(hexval) == 2:
            hexval = "0" + hexval
        print(str(codecs.decode(hexval, "hex"), "utf-8"), end="")
        offset += 2
    # same as asm jmp
    elif hex == "0x2":
        offset = int(hexcode[offset + 1], 16)
    # store value in mem
    elif hex == "0x3":
        memory[int(hexcode[offset + 1], 16)] = hexcode[offset + 2]
        offset += 3
    # jump to hex stored in memory
    elif hex == "0x4":
        offset = int(memory[int(hexcode[offset + 1]], 16), 16)
    else:
        print("Unknown hex at offset: " + str(offset))
        sys.exit()
