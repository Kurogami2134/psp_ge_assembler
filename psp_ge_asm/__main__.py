from psp_ge_asm import Assembler
from sys import argv
from genericpath import exists


if __name__ == "__main__":
    if len(argv) != 3:
        print("Usage: python3 -m psp_ge_asm <assembly-file> <output-file>")
        exit()

    if not exists(argv[1]):
        print("File not found")
        exit()
    
    asm = Assembler()

    with open(argv[1], "r") as file:
        asm.read(file)
    
    with open(argv[2], "wb") as out:
        out.write(asm.assemble())
