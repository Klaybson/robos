import subprocess

#Variavel
comando = "ls -l /var/www/html"
comando2 = "ls -la > ./lista_de_arquivos.txt"

# executa o comando em segundo plano
subprocess.Popen(comando, shell=True)

# comando2 com saída redirecionada para um arquivo
# executa o comando e redireciona a saída para um arquivo
subprocess.call(comando2, shell=True)

