import argparse
import os
from pathlib import Path

from c_sharp_obfuscator import CSharpObfuscator

# Как запустить:
# main.py --nargs D:\Projects\Python\c_sharp_obfuscator\resources\Irotosfen.cs D:\Projects\Python\c_sharp_obfuscator\resources\list.cs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--nargs', nargs='+')
    for code_path in parser.parse_args().nargs:
        code_path = Path(code_path)
        with open(code_path, 'r', encoding="utf-8") as file:
            code = file.read()
        obfuscated_code = CSharpObfuscator(code).obfuscate()
        if not os.path.exists('result'):
            os.mkdir('result')
        with open(f'result/{code_path.name}', 'w', encoding="utf-8") as file:
            file.write(obfuscated_code)


if __name__ == '__main__':
    main()
