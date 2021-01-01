# Zsh configuration

# Turn off all beeps
unsetopt BEEP

# Enable colors and change prompt:
autoload -U colors && colors
PS1="%F{9}[%F{10}%n%F{9}@%F{10}%m %F{12}%c%F{9}]%f$ "

# Misc options
stty stop undef
setopt autocd
bindkey -v
export KEYTIMEOUT=1

# Shell history options
setopt INC_APPEND_HISTORY
setopt HIST_IGNORE_ALL_DUPS
HISTFILE=$HOME/.config/shell/zsh_history
HISTSIZE=1000
SAVEHIST=2000

# Set the default editors to nvim
export EDITOR="nvim"
export VISUAL="nvim"

# Shortcuts to edit and source this file
alias ec="$EDITOR $HOME/.zshrc"
alias sc="source $HOME/.zshrc"

# If the alias file is present, load it
[[ -f $HOME/.config/shell/aliasrc ]] && source $HOME/.config/shell/aliasrc

# Plugins
# source $HOME/.config/shell/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source $HOME/.config/shell/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
ZSH_AUTOSUGGEST_STRATEGY=(history completion)
