fpath+=~/.zsh_scripts
fpath+=$HOME/conda-zsh-completion

export RUSTC_WRAPPER=sccache
# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH
if type brew &>/dev/null; then
  fpath+=$(brew --prefix)/share/zsh/site-functions

  autoload -Uz compinit
  compinit
fi

fpath+=~/.oh-my-zsh/functions/

autoload -Uz compinit
compinit

path+=$HOME/.gem/ruby/3.0.0/bin
# Path to your oh-my-zsh installation.
export ZSH="/Users/sjq/.oh-my-zsh"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="af-magic"

plugins=(fzf brew git autojump direnv thefuck cp zsh-autosuggestions history-substring-search)

source $ZSH/oh-my-zsh.sh


[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
export HOMEBREW_GITHUB_API_TOKEN=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


# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/opt/homebrew/Caskroom/miniconda/base/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/opt/homebrew/Caskroom/miniconda/base/etc/profile.d/conda.sh" ]; then
        . "/opt/homebrew/Caskroom/miniconda/base/etc/profile.d/conda.sh"
    else
        export PATH="/opt/homebrew/Caskroom/miniconda/base/bin:$PATH"
    fi
fi
unset __conda_setup
conda activate sjq
# <<< conda initialize <<<
alias vim=nvim
alias ls=exa
test -e "${HOME}/.iterm2_shell_integration.zsh" && source "${HOME}/.iterm2_shell_integration.zsh"

