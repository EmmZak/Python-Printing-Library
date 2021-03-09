"""
Printing stuff to console
"""

class Printer:

    OTHER = '\033[90m'
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    END = '\033[0m'

    def __init__(self):
        pass

    def print_dict(self, struct):
        print('{')
        for k, v in struct.items():
            print(f'  {self.PURPLE}{k}{self.END} : {self.GREEN}{v}{self.END}')
        print('}')
    
    def print_list(self, struct):
        print(f'{self.GREEN}[{self.END}', end="")
        for e in struct:
            print(f' {e}', end="")
            #print(f' {self.GREEN}{e}{self.END}', end="")
        print(f'{self.GREEN} ]{self.END}')

    # determines object's type and call corresponding function
    def print_object(self, obj):
        if isinstance(obj, dict):
            print()
            self.print_dict(obj)
        elif isinstance(obj, list):
            #print()
            self.print_list(obj)
        else:
            print(obj, sep="", end="")
    
    def info(self, *args):
        print(f'{self.BLUE}[INFO]{self.END} ', end="")
        for arg in args:
            self.print_object(arg)
        print()

    def success(self, *args):
        print(f'{self.GREEN}[SUCCESS]{self.END} ', end="")
        for arg in args:
            self.print_object(arg)
        print()

    def warning(self, *args):
        print(f'{self.YELLOW}[WARNING]{self.END} ', end="")
        for arg in args:
            self.print_object(arg)
        print()

    def error(self, *args):
        print(f'{self.RED}[ERROR]{self.END} ', end="")
        for arg in args:
            self.print_object(arg)
        print()
#p = Printer()
#p.info('ok')