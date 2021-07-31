#! /bin/bash
sudo apt update && sudo apt upgrade -y

sudo apt install zsh -y

sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" 

git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

cp .zshrc ~/.zshrc

cp .funcoes.sh ~/
chmod +x ~/.funcoes.sh

sudo mkdir -p /usr/share/util
sudo chown -R $USER:$USER /usr/share/util
cp util/pwgen.py /usr/share/util/pwgen.py