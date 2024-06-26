"""
更新。
"""

from pathlib import Path
import requests
import git

UPDATE_URL = "https://github.com/StarPixel-Team/PCL-Client"
"""
更新提取地址。
"""
VERSION = 0
"""
当前版本号。
"""


class Update:
    """
    更新对象。
    """

    failed: bool = False
    """是否失败。"""

    def __init__(self) -> None:
        self.repo = git.Repo(Path(__file__).parent)
        if len(self.repo.remotes) == 0:
            self.origin = self.repo.create_remote("origin", UPDATE_URL)
        else:
            self.origin = self.repo.remotes.origin
        self.release_ver = 0
        self.release_hash = ""
        try:
            self.origin.fetch()
        except:
            self.failed = True

    def has_update(self, timeout_seconds: int = 3):
        """
        是否有更新。
        """
        if self.failed:
            return False
        try:
            result = (
                requests.get(
                    f"{UPDATE_URL}/raw/master/release.txt", timeout=timeout_seconds
                )
                .content.decode("utf-8")
                .split("|")
            )
        except:
            self.failed = True
            return False
        self.release_ver = int(result[0])
        self.release_hash = result[1]
        return self.release_ver > VERSION

    def update(self):
        """
        更新。
        """
        if self.failed:
            return False
        if not self.release_hash:
            return False
        self.origin.pull(self.release_hash, 30)
        self.repo.git.reset(f"{self.release_hash} --hard")
        return True
