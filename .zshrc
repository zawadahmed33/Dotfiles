# Prompt customization
PROMPT='%F{blue}[%~]%f %F{green}->%f '

# Load colors
autoload -U colors && colors

# History
HISTSIZE=10000
SAVEHIST=10000
HISTFILE=~/.zsh_history
HISTDUP=erase
setopt appendhistory
setopt sharehistory
setopt hist_ignore_space
setopt hist_ignore_all_dups
setopt hist_save_no_dups
setopt hist_ignore_dups
setopt hist_find_no_dups

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
