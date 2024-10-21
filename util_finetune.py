import os
import shutil

# function that gets the last (most recent) checkpoint from the model - needed when converting audio (i.e. at inference time)
def get_max_checkpoint(modelname: str):
    """
    get the latest checkpoint for a model. 
    """
    gen_checkpoints = [file for file in os.listdir(f"./checkpoints/{modelname}") if file.startswith("G") and file.endswith(".pth")]
    max_pt = max([int(file.removeprefix("G_").removesuffix(".pth")) for file in gen_checkpoints])
    checkpoint = f'./checkpoints/{modelname}/G_{max_pt}.pth'
    return checkpoint

def move_all_files(src, dst):
    """
    move all files within the directory src to dst
    """
    files = os.listdir(src)
    if not os.path.exists(dst): 
        os.mkdir(dst)
    for f in files:
        src_path = os.path.join(src, f)
        dst_path = os.path.join(dst, f)
        shutil.move(src_path, dst_path)