import os


dirs = [
    os.path.join("data", "raw"),
    os.path.join("data","processed"),
    os.path.join("data","modified"),
    "features",
    "pymdmentity",
    "notebooks",
    "saved_models",
    "Results",
    "tests"
]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        pass


files = [
    "dvc.yaml",
    "params.yaml",
  "README.md",
    os.path.join("src","__init__.py")
]

for file_ in files:
    with open(file_, "w") as f:
        pass
