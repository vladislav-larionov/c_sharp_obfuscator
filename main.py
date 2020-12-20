import os
import sys
from pathlib import Path

from c_sharp_obfuscator import CSharpObfuscator

# Как запустить:
# main.py D:\Projects\C#\to_obfus\qsort\qsort\Program.cs


def main():
    if not sys.argv[1]:
        print('invalid arg')
        return 1
    code_path = Path(sys.argv[1])
    with open(code_path, 'r') as file:
        code = file.read()
    obfuscated_code = CSharpObfuscator(code).obfuscate()
    if not os.path.exists('result'):
        os.mkdir('result')
    with open(f'result/{code_path.name}', 'w') as file:
        file.write(obfuscated_code)


if __name__ == '__main__':
    main()
