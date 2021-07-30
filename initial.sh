#! /bin/bash
sudo apt update && sudo apt upgrade -y

sudo apt install zsh gnome-tweaks -y

sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" 

git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

cp .zshrc ~/.zshrc

cp .funcoes.sh ~/
chmod +x ~/.funcoes.sh

mkdir -p /usr/share/util
cp pwgen.py /usr/share/util/pwgen.py

wget https://github.com/dracula/gtk/archive/master.zip -P /tmp/master.zip

wget https://github.com/dracula/gtk/files/5214870/Dracula.zip -P /tmp/master.zip
unzip /tmp/master.zip/master.zip -d /usr/share/themes
sudo unzip /tmp/master.zip/Dracula.zip -d /usr/share/icons


gsettings set org.gnome.desktop.interface gtk-theme "Dracula"
gsettings set org.gnome.desktop.wm.preferences theme "Dracula"
gsettings set org.gnome.desktop.interface icon-theme "Dracula"

gnome-tweaks &