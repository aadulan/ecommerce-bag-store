from path import py_path
import os
import subprocess


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    subprocess.run([py_path, 'manage.py', 'runserver'])


if __name__ == "__main__":
    main()
