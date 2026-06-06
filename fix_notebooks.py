import json
import glob
import sys
import os

folder = sys.argv[1] if len(sys.argv) > 1 else "."

for path in glob.glob(os.path.join(folder, "**", "*.ipynb"), recursive=True):
    with open(path) as f:
        nb = json.load(f)

    if "widgets" in nb.get("metadata", {}):
        del nb["metadata"]["widgets"]

        with open(path, "w") as f:
            json.dump(nb, f, indent=2)