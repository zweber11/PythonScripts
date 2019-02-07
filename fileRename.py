import os
for dir, subdirs, files in os.walk("."):
  for f in files:
    f_new = f + 'png'
    os.rename(os.path.join(root, f), os.path.join(root), f_new))
