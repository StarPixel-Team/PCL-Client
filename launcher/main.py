"""
程序入口点：启动器。
"""

from pathlib import Path
import shutil
from update import Update


def main():
    """
    主函数。
    """
    upd = Update()
    shutil.copy2(Path("PCL/PCL.exe").absolute(), Path("PCL.exe").absolute())

    upd.has_update()


if __name__ == "__main__":
    main()
