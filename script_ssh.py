import paramiko

# define as informações de conexão SSH
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
host = "192.168.1.149"
port = 22
username = "klaybson"
password = "darepo12"

# faz login no servidor
ssh.connect(host, port, username, password)

# executa o comando em segundo plano
comando = "nohup systemctl stop apache2 &"
stdin, stdout, stderr = ssh.exec_command(comando)

# fecha a conexão SSH
ssh.close()
