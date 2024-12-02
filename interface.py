from coletar_dados import descompactar_e_ler_arquivo  
from tkinter import *
from tkinter import filedialog, messagebox
import pandas as pd
import rarfile 
import os


def upload_file():
    # Solicitar usuário escolha um arquivo
    file_path = filedialog.askopenfilename(filetypes=[("RAR Files", "*.rar")])
    
    if file_path:
        pasta_destino = 'pasta_destino'
        
        try:
            # Usar função existente para descompactar e tratar os arquivos
            descompactar_e_ler_arquivo(file_path, pasta_destino)
            
            # Exibe mensagem de sucesso
            messagebox.showinfo("Sucesso", f"Arquivo processado com sucesso! Arquivos extraídos para: {pasta_destino}")
        except Exception as e:
            # Exibe mensagem de erro caso ocorra algum problema
            messagebox.showerror("Erro", f"Ocorreu um erro ao processar o arquivo: {e}")


def processar_arquivo(file_path):
    # Organizar o código para chamar seu código de processamento de dados
    df = pd.read_csv(file_path, delimiter=";")
    # Organizar para fazer os tratamentos necessários nos dados
    df.to_excel('./output/CLIENTES.xlsx', index=False)
    # Operações para salvar os arquivos de Processos
    print("Arquivos gerados com sucesso.")

# Interface principal
janela = Tk()
janela.geometry("350x150")
janela.title("Backup e Processamento de Dados")

texto_orientacao = Label(janela, text="Selecione o arquivo desejado para fazer a migração dos dados ")
texto_orientacao.grid(column=0, row=0, padx=10, pady=30)

upload_button = Button(janela, text="Selecionar Arquivo", command=upload_file)
upload_button.grid(column=0, row=1, padx=10, pady=10)

janela.mainloop()
