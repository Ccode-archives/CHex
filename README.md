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
# Machine code can be written in a hex editor that is compatible with this.
