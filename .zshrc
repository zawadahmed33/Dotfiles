# Prompt customization
PROMPT='%F{blue}[%~]%f %F{green}->%f '

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
alias ls="ls -la --color"

# Load zsh-autosuggestions
source /usr/share/zsh/plugins//zsh-autosuggestions/zsh-autosuggestions.zsh

# Load zsh-syntax-highlighting
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
