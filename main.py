import runpy
import sys

if __name__ == '__main__':
    sys.argv = ['', '-x']
    runpy.run_path('./namebench.py', run_name='__main__')