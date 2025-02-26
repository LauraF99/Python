def lerArquivo(nomeArquivo):
    try:
        with open(nomeArquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print("Conteúdo do arquivo:")
            print(conteudo)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nomeArquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao tentar ler o arquivo: {e}")


nomeArquivo = "relatorio.pdf"
lerArquivo(nomeArquivo)