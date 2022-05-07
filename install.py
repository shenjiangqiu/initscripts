# first, get the os infomation
import os
import sys
import platform
import subprocess
import shutil
import getpass
import time
import re
import config_ohmyzsh
# get the current os
os_info = platform.system()
print(os_info)
# install the dependencies
if os_info == 'Darwin':
    # Step 1: install brew and some basic packages
    ## find if brew is in path
    brew_path = shutil.which('brew')
    if brew_path is not None:
        print('brew is installed')
    else:
        print('brew is not installed')
        print('installing brew')
        subprocess.call(
            ['bash', '-c', '$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)'])

    ## install some utiles
    print('Installing some utiles...')
    subprocess.call(['brew', 'install', 'wget', "starship", "git",
                    "ripgrep", "bat", "tokei", "exa", "fd", "procs", "zsh","gnu-sed","miniconda","autojump","thefuck"])
    ## init conda: conda init 
    subprocess.call(['conda', 'init', 'zsh'])
    subprocess.call(["conda","create","-n","sjq"])


    # Step 2: install ohmyzsh
    print('Installing ohmyzsh...')
    config_ohmyzsh.install()

    # Step 3: install rust
    ## test if rustup is in path
    rustup_path = shutil.which('rustup')
    if rustup_path is not None:
        print('rustup is installed')
    else:
        ## install rustup
        print('rustup is not installed')
        print('installing rustup')
        subprocess.call(['curl', '-sSf', 'https://sh.rustup.rs', '|', 'bash'])
        ## rustup default stable
        subprocess.call(['rustup', 'default', 'stable'])
        ## add ~/.cargo/bin to PATH in .zshrc
        with open(os.path.expanduser('~/.zshrc'), 'a') as f:
            f.write('\n')
            f.write('export PATH="$HOME/.cargo/bin:$PATH"')
            f.write('\n')
    # now we cargo good to go
    print('cargo is installed')

    
else:
    if os_info != 'Linux':
        print('Unsupported OS')
        sys.exit(1)
    # install dependencies
    print('Installing dependencies...')
    # test if miniconda is installed
    if os.path.exists('miniconda'):
        print('Miniconda is already installed')
    else:
        # install miniconda
        print('Installing miniconda...')
        subprocess.call(
            ['bash', '-c', 'curl -o miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh && bash miniconda.sh -b -p $HOME/miniconda'])
        # remove the miniconda.sh
        os.remove('miniconda.sh')
    # test if rustup is installed
    if os.path.exists('rustup'):
        print('Rustup is already installed')
    else:
        # install rustup
        print('Installing rustup...')
        subprocess.call(
            ['bash', '-c', 'curl https://sh.rustup.rs -sSf | sh -s -- -y'])
        # rustup default to stable
        subprocess.call(['rustup', 'default', 'stable'])
        cargo_packages = ["exa", "du-dust", "zoxid", "bat", "procs",
                          "fd-find", "huniq", "tp-note", "t-rec", "diffsitter", ""]
        # cargo install some
