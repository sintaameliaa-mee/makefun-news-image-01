"""Entry for the world-news image bounty: places the finished front page
into the output folder so it can be collected for judging."""

import os
import shutil
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, out_dir / "entry.png")


if __name__ == "__main__":
    main()
