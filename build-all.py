import sys
import os
from lib import vsproj

solution_root = r"e:\rp\outdoor-asset-tracking\github\GeoSensePluse-Server"
gsv_csproj = f"{solution_root}\\GeoSensePlus.Server\\GeoSensePlus.Server.csproj"
gs_csproj = f"{solution_root}\\GeoSensePlus.Cli\\GeoSensePlus.Cli.csproj"


def build_gs():
    # ver = vsproj.get_csproj_version(gs_csproj)
    # print(f"Building gs {ver} ...")
    vsproj.get_updated_csproj_version(gs_csproj)


def build_gsv():
    ver = vsproj.get_csproj_version(gsv_csproj)
    print(f"Building gsv {ver} ...")


def invalid_subcommand():
    print("Please specify a subcommand from the following options:")
    for k, _ in subcommands.items():
        print(k)


subcommands = {
    "gs": build_gs,
    "gsv": build_gsv,
}


def main():
    # os.system(f'release-gsv.bat {vsproj.get_csproj_version()}')

    if len(sys.argv) > 1:
        subcommands.get(sys.argv[1], invalid_subcommand)()
    else:
        print("no subcommand specified")


if __name__ == '__main__':
    sys.exit(main())
