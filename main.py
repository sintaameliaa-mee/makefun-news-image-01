# news-image-01 entry: sum up the world's news of Friday 13 November 2026
# in one image. The image beside this file is a newspaper front page for the
# day: the hero story is Nvidia chief Jensen Huang resigning (shares down
# 16%), with four panels for Europe joining the Ukraine peace talks, a drone
# hitting a Russian warship, the global Microsoft outage, and the strike on a
# Gaza hospital that killed six. The program copies it to the output
# directory; the judge sees exactly these bytes. The output directory comes
# from MAKEFUN_OUTPUT_DIR and defaults to /output when it is not set.

import os
import shutil
from pathlib import Path


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(Path(__file__).with_name("entry.png"), out_dir / "entry.png")


if __name__ == "__main__":
    main()
