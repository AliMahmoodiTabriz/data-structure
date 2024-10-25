from typing import List
import re

def removeSubfolders(folder: List[str]) -> List[str]:
    folder.sort()
    result = []
    for f in folder:
        if not result or not f.startswith(result[-1] + '/'):
            result.append(f)
    return result

print(removeSubfolders(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]))
print(removeSubfolders(["/a", "/a/b/c", "/a/b/d"]))
print(removeSubfolders(["/a/b/c","/a/b/ca","/a/b/d"]))
print(removeSubfolders(["/abc/de","/abc/dee","/abc/def","/abc/def/gh","/abc/def/ghi","/abc/def/ghij","/abc/def/ghijk","/abc/dez"]))
