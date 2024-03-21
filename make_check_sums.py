#!/usr/bin/env python
import hashlib
from pathlib import Path


def file_md5_checksum(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        hash_md5.update(f.read())
    return hash_md5.hexdigest()


def main(suffix, dry_run=False):
    files = Path().cwd().rglob(f'*.{suffix}')
    for f in files:
        md5 = Path(f"{f}.md5")
        if not md5.exists():
            if dry_run:
                print(f"Create checksum for {f}")
                continue

            with open(md5, "w") as out:
                out.write(file_md5_checksum(f))


if __name__ == '__main__':
    main("imma")
    main("csv")
    main("psv")
    main("immt")
    main("nc")
