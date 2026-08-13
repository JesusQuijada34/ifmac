import ast
from pathlib import Path

for name in ("ifmac.py", "install.py", "updater.py"):
    ast.parse(Path(name).read_text(encoding="utf-8"), filename=name)

source = Path("ifmac.py").read_text(encoding="utf-8")
installer = Path("install.py").read_text(encoding="utf-8")
updater = Path("updater.py").read_text(encoding="utf-8")
assert "import secrets" in source
assert "regex.fullmatch" in source
assert "shell=True" not in source
assert "subprocess.run(['sudo', 'ip', 'link', 'set', profile" in source
assert "shell=True" not in source + installer + updater
assert "safe_extract_zip" in updater
assert "MAX_UPDATE_BYTES" in updater
assert "check=True" in installer
print("IFMAC_STATIC_SECURITY_CHECK_OK")
