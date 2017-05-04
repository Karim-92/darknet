import os

with open("data/input.names", "w") as a:
    for path, subdirs, files in os.walk(r'testing'):
       for filename in files:
         f = os.path.join(path, filename)
         a.write(str(f) + os.linesep)
