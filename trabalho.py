import paramiko
import requests
import pyautogui

# define as informações de conexão SSH
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
host = "172.28.2.122"
port = 22
username = "root"
password = "darepo12"

# define as informações de sistema

url = "http://172.28.2.122"

# faz uma requisição GET na URL e verifica o status de resposta
try:
    response = requests.get(url)
    response.raise_for_status()  # levanta uma exceção se o status code for diferente de 200
    pyautogui.alert('Página ok!')
except:
    pyautogui.alert('Melhor conferir!')
    # faz login no servidor
    ssh.connect(host, port, username, password)
    # executa o comando em segundo plano
    comando = "nohup systemctl start httpd &"
    stdin, stdout, stderr = ssh.exec_command(comando)
    # fecha a conexão SSH
    ssh.close()
