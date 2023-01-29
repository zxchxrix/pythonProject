from pathlib import Path

path = Path()
# print(path.exists())
for files in path.glob('*'):
    print(files)
