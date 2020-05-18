import sys
import os


def main():
    os.system('build-image.bat')
    os.system('pack-cli.bat')


if __name__ == '__main__':
    sys.exit(main())
