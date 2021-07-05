# Kikolouro's Utils

---
# Configuring Ubuntu Environment
---
## Terminator

1. Install Terminator from App Store.

2. Import config file **Terminator/config** to ~/.config/terminator/config.

## Oh-my-zsh Shell

1. Install zsh shell.
    ```sudo apt install zsh```

2. Installing oh-my-zsh.
    ` sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" `

3. oh-my-zsh Auto-suggestion. 
    1. Clone git repository
        `git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions`
    
    2. Edit config file.
        `nano ~/.zshrc`

    3. On plugins add.
        `zsh-autosuggestions`

## Shell Helper

1. Copy **.funcoes.sh** to home folder
    ```cp .funcoes.sh ~/```

2. Give executable permisions on file
    ```chmod +x ~/.funcoes.sh```

3. Edit **~/.zshrc** and add the code below to end of the file:
    ```source ~/.funcoes.sh```

## Miscellaneous

- Background picture: background.png