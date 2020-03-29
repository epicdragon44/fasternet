import ctypes, sys
import runpy


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if __name__ == '__main__':
    if is_admin():
        runpy.run_path('./main.py', run_name='__main__')
        runpy.run_path('./gui.py', run_name='setDone')
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(" ".join(sys.argv)), None, 1)
