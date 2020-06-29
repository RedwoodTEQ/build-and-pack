import sys
import os
from lib import vsproj


def main():
    os.system(f'release-gsv.bat {vsproj.get_project_version()}')


if __name__ == '__main__':
    sys.exit(main())
