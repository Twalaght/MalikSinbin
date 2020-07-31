# ~/.bashrc

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Bash shell options
HISTCONTROL=ignoreboth
HISTSIZE=1000
HISTFILESIZE=2000
shopt -s histappend
shopt -s checkwinsize

# TODO - Make dependant on the existence of the wal folder
# Set the desired PS1, the coloured version uses green and blue
PS1="\[\033[01;32m\][\u@\h \[\033[01;34m\]\W\[\033[01;32m\]]\[\033[00m\]\$ "	# Coloured
# PS1="[\u@\h \W]\$ "								# Uncoloured


# Some aliases for convenience
alias ls="ls --color=auto"	# Coloured output
alias grep="grep --color=auto"	# Coloured output
alias ll="ls -hl"		# Human readable sizes, in a list
alias la="ls -hA"		# Human readable sizes, show hidden
alias lal="ls -hlA"		# Human readable sizes, in a list, show hidden
alias cp="cp -i"		# Confirm before overwriting
alias mv="mv -i"		# Confirm before overwriting
alias df="df -h"		# Readable sizes

alias p="sudo pacman"
alias v="nvim"
alias sv="sudo nvim"
alias r="ranger"
alias sr="sudo ranger"
alias ka="killall"
alias g="git"


# Binds
bind 'set bell-style none'
