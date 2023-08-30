from pathlib import Path
path_to_dir = Path('media/')

def check_if_stem_exist(dir):
    stems = []
    for i in dir.iterdir():
        if i.is_file():
            if not i.stem in stems:
                stems.append(i.stem)
            else:
                print(i)
        else:
            check_if_stem_exist(Path(i))

check_if_stem_exist(path_to_dir)


