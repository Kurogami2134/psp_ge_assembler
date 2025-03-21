from re import sub
from psp_ge_asm.ge_asm import ge_asm, NotAlignedException


def AssemblerException(line_number, msg) -> None:
    print(f'Error at line {line_number+1}: {msg}')
    exit()


def to_num(string) -> int:
    if isinstance(string, str):
        if 'X' in string:
            return int(string, 16)
        elif '.' in string:
            res = float(string, )
            if res % 1:
                return res
            else:
                return int(res)
        else:
            return int(string)
    return int(string)


class Parser:
    def __init__(self) -> None:
        self.symbols = {'FALSE': 0, 'TRUE': 1}
        self.lines = []

    def fromList(self, list: list[str]) -> None:
        for line_number, line in enumerate(list):
            line = sub("\t", " ", sub(";.*", "", line.replace("\n", "")))
            while "  " in line:
                line = sub("  ", " ", line)
            line = sub(", ", ",", line)

            if line == "":
                continue

            if "#include" in line:
                with open(line.split(" ")[1], "r") as file:
                    self.read(file)
                continue

            line = line.upper()

            if "=" in line:
                line = line.replace(" ", "").replace(":", "=").split("=")
                if line[0] not in self.symbols.keys():
                    self.symbols[line[0]] = to_num(line[1])
                    continue
                else:
                    AssemblerException(line_number, f'{line[0]} is already defined.')
            
            self.lines.append((line_number, line))

    def read(self, fd) -> None:
        self.fromList(fd.readlines())


class Assembler:
    def __init__(self) -> None:
        self.parser = Parser()
    
    def read(self, fd) -> None:
        self.parser.read(fd)
    
    def fromList(self, list: str) -> None:
        self.parser.fromList(list)
    
    def assemble(self) -> bytes:
        bin = b''
        for line_number, line in self.parser.lines:
                op_code = line.split(" ")[0]
                if len(line.split(" ")) > 1:
                    args = [to_num(self.parser.symbols[x]) if x in self.parser.symbols.keys() else to_num(x) for x in line.split(" ")[1].split(",")]
                else:
                    args = []
                try:
                    bin += ge_asm(op_code, args)
                except (OverflowError, NotAlignedException, NotImplementedError) as error:
                    print(f'{type(error).__name__}: {error}, line {line_number+1}\n{line}')
                    exit()
        
        return bin
