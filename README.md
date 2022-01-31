# CHex
A bytecode vm written in python.
# hex command meaning
> note: the first two hex values of a CHex program are the magic number  
# 0x01 (offset in memory in hex)
Print the ascii hex character stored in memory at the offset given.
# 0x02 (program offset to jump to)
Equivelent of jump command in asm.
# 0x03 (offset in memory to store value at) (hex value to store(can be ascii hex))
Store a value in memory at the given offset.
# 0x04 (offset in memory to get program offset from)
Jump to a program offset stored in memory.
# Machine code can be written in a hex editor that is compatible with this.
If you would like to see some code I have already written lease check the example binary.
# What it simulates
1. It inits the memory.
2. It inits the only register the cpu has. (offset)
3. It loads the first two bytes of the program file and checks if they say "hi" in ascii.
4. It sets offset to 0x02
5. It gets the command at the location of offset and runs it.
6. It sets offset to the next command
7. Goes back to step 5 and repeats ntil the program ends.
