
import sys

# pega o nome do arquivo da linha de comando
report_file_name = sys.argv[1]

# abre o arquivo de entrada
report_file = open(report_file_name, "r")

# abre o arquivo de saida
output_file = open( "saida.csv", "w" )

# pega as linhas do arquivo
report_lines = report_file.readlines()

# pega numero de linhas do relatorio
num_lines = len(report_lines)

i = 0
while i < num_lines:
	# pega a iesima linha do relatorio
	line = report_lines[i]
	# verifica se a linha contem '*FAULT BUS:'
	if line.find('*FAULT BUS:') > 0:
		output_line = ""
		# separa as palavras da linha
		line_parts = line.split()
		# o nome do painel eh a terceira palavra da linha
		panel_name = line_parts[2]
		# adiciona o painel na linha de saida
		output_line += panel_name + ";"
		# pula 5 linhas
		i += 5
		# pega a linha do relatorio com os valores
		line = report_lines[i]
		# divide as palavras da linha
		line_parts = line.split()
		# percorre os valores da linha. O primeiro valor eh a 4a palavra
		for n in range(3, 8):
			output_line += line_parts[n] + ";" # adiciona o valor na linha de saida
			
		# joga a linha de saida pra dentro do arquivo de saida	
		output_file.write( output_line + "\n" )
	# passa pra proxima linha
	i += 1
	
# fecha o arquivo de saida
output_file.close()