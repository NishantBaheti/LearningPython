'''
app.py

file system scripts.
'''
import asyncio
import os
import shutil
import sys
import time
import random

def list_files(path: str, files: list = None)->list:
    """List of files recursively.

    Args:
        path (str): path.
        files (list, optional): list of files. Defaults to None.

    Returns:
        list: list of files
    """

    files = files or []

    contents = os.listdir(path)
    for content in contents:
        t_path = os.path.join(path, content)
        if os.path.isfile(t_path):
            files.append(t_path)
        else:
            files = list_files(t_path, files)
    return files

def extension_segregation(files_list: list)->dict:
    """Segregate files based on extensions.

    Args:
        files_list (list): files list.

    Returns:
        dict: segregated files object.
    """

    seg_obj = {
        "badfiles": []
    }
    for file in files_list:
        file_parts = file.split(os.path.sep)[-1].split('.')
        if len(file_parts) > 1:
            ext = file_parts[-1]
            if ext in seg_obj:
                seg_obj[ext].append(file)
            else:
                seg_obj[ext] = [file]
        else:
            seg_obj["badfiles"].append(file)
    return seg_obj

def make_dir(path: str, dir_name: str):
    """Make directory.

    Args:
        path (str): path to dir.
        dir_name (str): directory name.
    """
    dir_path = os.path.join(path, dir_name)
    os.makedirs(dir_path, exist_ok=True)


def move_content_sync(source: str, target: str):
    """Move content.

    Args:
        source (str): source path.
        target (str): target path.
    """
    shutil.copy(source, target)

    # adding this random sleep for real time scenario
    # that this copy will take certain time
    time.sleep(random.randint(1,5)) # it can take upto 5 seconds


def move_files_sync(file_obj: dict, dest_path: str):
    """Move files synchronously.

    Args:
        file_obj (dict): files object.
        dest_path (str): destination path.
    """
    for ext in file_obj:
        make_dir(dest_path, ext)

    for ext in file_obj:
        ext_path = os.path.join(dest_path, ext)
        for file in file_obj[ext]:
            move_content_sync(file, ext_path)

async def move_content_async(source: str, target: str):
    """Move content.

    Args:
        source (str): source path.
        target (str): target path.
    """
    shutil.copy(source, target)

    # adding this random sleep for real time scenario
    # that this copy will take certain time
    await asyncio.sleep(random.randint(1,5))

async def move_files_async(file_obj: dict, dest_path: str):
    """Move files asynchronously.

    Args:
        file_obj (dict): files object.
        dest_path (str): destination path.
    """
    for ext in file_obj:
        make_dir(dest_path, ext)

    task_list = []
    for ext in file_obj:
        ext_path = os.path.join(dest_path, ext)
        for file in file_obj[ext]:
            task_list.append(move_content_async(file, ext_path))

    await asyncio.gather(*task_list)

if __name__ == '__main__':
    source_path = sys.argv[1]
    target_path = sys.argv[2]


    start = time.time()
    files = list_files(path=source_path)
    file_obj = extension_segregation(files_list=files)


    # for scenario of moving 50 files
    # where every move takes from 1 to 5 seconds


    # syncronous total time taken : 146.13251948356628
    # move_files_sync(file_obj, target_path)

    # asyncronous total time taken : 5.008042812347412
    asyncio.run(move_files_async(file_obj, target_path))

    end = time.time()
    print("total time taken :",end - start)
