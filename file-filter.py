import os, shutil, pathlib,stat
import os.path
def move_dir(src: str, dst: str):
    files=os.listdir(src)
    extensions=set()
    for i in files:
        temp=i.split(".")[-1]
        extensions.add(temp)
    for i in extensions:
        # if not os.path.exists(i):
        try: 
            pathlib.Path(i).mkdir(parents=True, exist_ok=True)
        except OSError:
            print(f"Directory {i} already exists")
    for i in files:
        if not os.path.isdir(i):
            try:
                shutil.move(os.path.join(src, i), os.path.join(dst, i.split(".")[-1],i))
            except FileNotFoundError:
                print(f"File {i} not found")
move_dir(os.getcwd(),os.getcwd())
