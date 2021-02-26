from pathlib import Path
import re

from pyhpc import __version__


def test_version():
    toml = (Path(__file__).parents[1] / "pyproject.toml").read_text()
    version = re.search(r'version = "([\d\.]+)"', toml).groups(1)[0]
    assert version == __version__
