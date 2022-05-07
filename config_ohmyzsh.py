import shutil
import os
import subprocess


def install(os_info):
    if os_info == 'Darwin':
        # cp ./res/.zshrc to ~
        shutil.copy('./res/.zshrc', os.path.expanduser('~/.zshrc'))
        # cp dir ./res/.oh-my-zsh to ~
        shutil.copytree('./res/.oh-my-zsh', os.path.expanduser('~/.oh-my-zsh'))
        # cp dir ./res/.zsh_func to ~
        shutil.copytree('./res/.zsh_func', os.path.expanduser('~/.zsh_func'))
        # cp dir ./res/.zsh_scripts to ~
        shutil.copytree('./res/.zsh_scripts',
                        os.path.expanduser('~/.zsh_scripts'))
        # pip install thefuck autojump
        print('ohmyzsh is installed')
        pass
