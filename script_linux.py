import subprocess

#Variavel
comando = "ls -l /var/www/html"
comando2 = "ls -la > ./lista_de_arquivos.txt"
comando3 = "sleep 10 && echo 'Execução concluída!'"
# executa o comando em segundo plano
subprocess.Popen(comando3, shell=True)

# comando2 com saída redirecionada para um arquivo
# executa o comando e redireciona a saída para um arquivo
subprocess.call(comando2, shell=True)

# executa o comando e captura a saída
saida = subprocess.check_output(comando, shell=True)
print(saida.decode('utf-8'))