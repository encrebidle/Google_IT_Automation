'''The new_directory function creates a new directory inside the current working directory, 
then creates a new empty file inside the new directory, and returns the list of files in that directory. 
Fill in the gaps to create a file "script.py" in the directory "PythonPrograms".'''

import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  d=directory
  cd=os.getcwd()
  fn=os.path.join(cd,d)
  if os.path.isdir(fn) == False:
    os.mkdir(d)
    

  # Create the new file inside of the new directory
  os.chdir(d)
  with open (filename,"w+") as file:
    pass

  # Return the list of files in the new directory
  return os.listdir(fn)

print(new_directory("PythonPrograms", "script.py"))
