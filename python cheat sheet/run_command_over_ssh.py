def runCommandOverSSH(command, server):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    if server == 'server':
        ssh.connect(config('SSH_SERVER_MAIL'), 22, username=config('SSH_USERNAME_MAIL'), password=config('SSH_PASSWORD_MAIL'), look_for_keys=False)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
    ssh_stdin.close()
    return ssh_stdout