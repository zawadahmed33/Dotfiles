# Prompt customization

PROMPT='%F{green}[%~] =>%f '

# Load colors

autoload -U colors && colors

# History

HISTSIZE=10000
SAVEHIST=10000
HISTFILE=~/.zsh_history

# Auto complete

autoload -U compinit
zstyle ':completion:*' menu select
zmodload zsh/complist
compinit
_comp_options+=(globdots)

# Aliases
alias ls="ls --color"

# Load zsh-syntax-highlighting

source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
