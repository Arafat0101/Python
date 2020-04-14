from pathlib import Path

# Absolute Path
#Local Hard Drive Directory path
    #C:\Program Files\Microsoft
    # /usr/local/bin/mac

# Relative path
    #its project directory path

#path = Path("ecommerce")
#print(path.exists())

#path = Path("emails")
#print(path.mkdir())
#print(path.rmdir())

path = Path()
print(path.glob('*')) #All Files and All dir
print(path.glob('*.*')) #All Files
print(path.glob('*.py')) #All py Files

for file in path.glob('*'):
    print(file)
