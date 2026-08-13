#!/usr/bin/env python
import subprocess
from pathlib import Path


def main():
    root = Path(__file__).resolve().parent
    sources = [
        (root / "ifmac.py", Path("/usr/bin/ifmac")),
        (root / "app" / "ifmac.png", Path("/usr/share/icons/ifmac.png")),
        (root / "ifmac.desktop", Path("/usr/share/applications/ifmac.desktop")),
    ]
    try:
        print("preparing files...")
        for source, destination in sources:
            subprocess.run(["sudo", "cp", str(source), str(destination)], check=True)
    except subprocess.CalledProcessError as error:
        print(f"installation failed; sudo permissions are required: {error}")
        return 1
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
