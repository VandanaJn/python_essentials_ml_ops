import os
from os.path import abspath, join, getsize

sizes = {}
for top_dir, directories, files in os.walk("."):
    for _file in files:
        full_path = abspath(join(top_dir, _file))
        size = getsize(full_path)
        sizes[full_path] = size
sorted_results = sorted(sizes.keys(), key=lambda k: sizes[k], reverse=False)
for path in sorted_results[:10]:
    print("Path: {0}, size: {1}".format(path, sizes[path]))
