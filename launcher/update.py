"""
更新。
"""

from pathlib import Path
import git

UPDATE_URL = "https://github.com/StarPixel-Team/PCL-Client"
"""
更新提取地址。
"""


class Update:
    """
    更新对象。
    """

    def __init__(self) -> None:
        self.repo = git.Repo(Path.cwd())

    def update(self):
        """
        更新。
        """
        origin = self.repo.create_remote("origin", UPDATE_URL)
        origin.fetch()
        origin.pull("generated")
