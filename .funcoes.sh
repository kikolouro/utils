#GIT

alias gcm='git commit --message'
alias ga='git add .'
alias gs='git status'
alias gp='git pull'
alias gpr='git push'
alias gprf='git push --force'
alias gc='git checkout'

#Docker
alias dosca='docker stop $(docker ps -a -q)'
alias dorca='docker rm $(docker ps -a -q)'
alias doria='docker rmi $(docker images -q)'

#Misc
alias ll="ls -al"
alias pwgen="python3 ~/util/pwgen.py"
alias shrug="echo \"¯\\_(ツ)_/¯\""