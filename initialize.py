# REVERT FOLDERS & FILES TO INITIAL STATES (post installation, pre-notebook)
# does the following:
# delete ./chunks
# delete ./data
# delete DUMMY (symlink)
# delete
import shutil
import os
import argparse
from os.path import join

ROOT=os.path.dirname(__file__)

def delete_thing(path):
    if not os.path.exists(path):
        return None
    if os.path.islink(path):
        print("jajaja")
        os.unlink(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)
    elif os.path.isfile(path):
        os.remove(path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--leave_chunks', action='store_true',
        default=False)
    args = parser.parse_args()

    # remove ./chunks
    if not args.leave_chunks:
        delete_thing(join(ROOT, "chunks"))

    # remove symlink
    delete_thing(join(ROOT, "DUMMY"))
    # remove ./data
    delete_thing(join(ROOT, "data"))
    
    # print(os.path.exists(join(ROOT, "DUMMY")))
    # print(os.path.isabs(join(ROOT, "DUMMY")))
    # print(os.path.isdir(join(ROOT, "DUMMY")))
    # print(os.path.isfile(join(ROOT, "DUMMY")))
    # print(os.path.islink(join(ROOT, "DUMMY")))
    # print(os.path.ismount(join(ROOT, "DUMMY")))

    # remove finetuning filelists
    for file in ["finetune-train.txt", "finetune-test.txt", "finetune-val.txt"]:
        delete_thing(join(ROOT, "filelists", file))

