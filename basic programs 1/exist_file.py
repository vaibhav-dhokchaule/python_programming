# Check if file exists, then delete it:

import os
if os.path.exists("textfile.txt"):
  os.remove("textfile.txt")
else:
  print("The file does not exist")