---
title: "How to Check if a File Exists in Python"
author: Lane Wagner
date: "2021-12-08"
categories: 
  - "python"
images:
  - /img/800/file.webp
---

When working with files in Python, you'll often need to check if a file exists before you do anything else with it, such as reading from or writing to it. Luckily, the Python standard library makes this a piece of cake.

## Use pathlib.Path.exists(path) to check for files and directories

```py
from pathlib import Path

path_exists = Path.exists("home/dir/file.txt")

if path_exists:
    print("found it!")
else:
    print("not found :(")
```

Notice that `path_exists` will be `True` whether this is a file or a directory, it's only checking if the _path_ exists.

Note: On older versions of Python you may not have access to the [pathlib module](https://docs.python.org/3/library/pathlib.html). If that's the case, you can use `os.path.exists()`.

```py
from os.path import exists

path_exists = exists("home/dir/file.txt")

if path_exists:
    print("found it!")
else:
    print("not found :(")
```

## Use pathlib.Path(path).is\_file() to check for only files

```py
from pathlib import Path

file_exists = Path.is_file("home/dir/file.txt")

if file_exists:
    print("found it!")
else:
    print("not found :(")
```

## Use pathlib.Path(path).is\_dir() to check for only directories

```py
from pathlib import Path

dir_exists = Path.is_dir("home/dir")

if dir_exists:
    print("found it!")
else:
    print("not found :(")
```

{{< cta1 >}}

## Use pathlib.Path(path).is\_symlink() to check for only symlinks

A [symlink](https://en.wikipedia.org/wiki/Symbolic_link) is a path that points to, or aliases another path in a filesystem.

```py
from pathlib import Path

symlink_exists = Path.is_dir("home/dir/some_symlink")

if symlink_exists:
    print("found it!")
else:
    print("not found :(")
```
