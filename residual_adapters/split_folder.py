from os import path, listdir
import pathlib
import random
import shutil


def ratio(input, output="output", seed=1337, ratio=(.8, .1, .1)):
    # make up for some impression
    assert round(sum(ratio), 5) == 1
    assert len(ratio) in (2, 3)

    for class_dir in list_dirs(input):
        split_class_dir_ratio(class_dir, output, ratio, seed)


def copy_files(files_type, class_dir, output):
    """Copies the files from the input folder to the output folder
    """
    # get the last part within the file
    class_name = path.split(class_dir)[1]
    for (files, folder_type) in files_type:
        full_path = path.join(output, folder_type, class_name)

        pathlib.Path(full_path).mkdir(parents=True, exist_ok=True)
        for f in files:
            shutil.copy2(f, full_path)


def list_files(directory):
    """Returns all files in a given directory
    """
    return [f for f in pathlib.Path(directory).iterdir() if f.is_file() and not f.name.startswith('.')]


def list_dirs(directory):
    """Returns all directories in a given directory
    """
    return [f for f in pathlib.Path(directory).iterdir() if f.is_dir()]


def setup_files(class_dir, seed):
    """Returns shuffled files
    """
    # make sure its reproducible
    random.seed(seed)

    files = list_files(class_dir)

    files.sort()
    random.shuffle(files)
    return files


def split_class_dir_ratio(class_dir, output, ratio, seed):
    """Splits one very class folder
    """
    files = setup_files(class_dir, seed)

    split_train = int(ratio[0] * len(files))
    split_val = split_train + int(ratio[1] * len(files))

    li = split_files(files, split_train, split_val, len(ratio) == 3)
    copy_files(li, class_dir, output)


def split_files(files, split_train, split_val, use_test):
    """Splits the files along the provided indices
    """
    files_train = files[:split_train]
    files_val = files[split_train:split_val] if use_test else files[split_train:]

    li = [(files_train, 'train'), (files_val, 'val')]

    # optional test folder
    if use_test:
        files_test = files[split_val:]
        li.append((files_test, 'test'))
    return li


ratio('/home/sihui/Documents/home_office_resize', output="/home/sihui/Documents/homeoffice_split", ratio=(.6, .2, .2))