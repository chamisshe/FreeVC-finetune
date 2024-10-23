# Finetuning FreeVC


FreeVC is an open source **Voice Conversion** model, released in 2022 ([Code](https://github.com/OlaWod/FreeVC) | [Paper](https://arxiv.org/abs/2210.15418)). This Repository contains a [Jupyter Notebook](finetune_freevc.ipynb0) that takes you through all the steps of **finetuning** FreeVC for a particular speaker.

><details>
>
>**<summary>What is Voice Conversion?</summary>**
> 
> The goal of voice conversion is to make a recorded utterance of *speaker A* sound like it's being said by *speaker B*. To do so, we essentially want to remove the speaker-specific features of speaker A from the recording, and replace them with speaker B's features. This is different from similar technology such as voice cloning, which achieves a similar output, but on the basis of text-to-speech.
>
></details>

## Prerequisites & Installation

> [!WARNING]
> You'll need to run the following snippets of code before you to run the notebook for the first time.

> [!NOTE]
> The installation steps and the notebook are designed and tested for Linux (WSL Ubuntu) only. It may also work on Windows or Mac, but the commands for the installation would differ significantly and the notebook is not guaranteed to work.

### Linux

#### Python 3.9

Check if Python 3.9 is already installed:

```bash
python3.9 -V
```

Otherwise, install it as follows:
```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update && sudo apt upgrade
sudo apt-get install python3.9
```


#### FFmpeg

Check if FFmpeg is installed:
```bash
ffmpeg -version
```

Otherwise, install it as follows:
```bash
sudo apt update
sudo apt install ffmpeg
```

#### Venv

Next, as is standard procedure, we want to install the required modules inside a Virtual Environment (or venv). Because different projects have different dependencies, we want to keep them from interfering with each other.

```python
python3.9 -m venv .venv-freevc && source ./.venv-freevc/bin/activate
```

For now, only install the `ipykernel` package, which allows us to run Jupyter. The remaining requirements will be installed when running the notebook.

```python
pip install ipykernel
```