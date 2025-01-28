import os
import tkinter as tk
from tkinter import messagebox, simpledialog

# Arquivo onde as tarefas serão salvas
arquivo_tarefas = "tarefas.txt"

# Função para criar uma nova tarefa
def criar_tarefa():
    nova_tarefa = simpledialog.askstring("Criar Tarefa", "Digite a nova tarefa:")
    if nova_tarefa:
        with open(arquivo_tarefas, "a") as arquivo:
            arquivo.write(nova_tarefa + "\n")
        messagebox.showinfo("Sucesso", f"Tarefa '{nova_tarefa}' criada com sucesso!")

# Função para atualizar uma tarefa existente
def atualizar_tarefa():
    if not os.path.exists(arquivo_tarefas):
        messagebox.showwarning("Aviso", "Nenhuma tarefa encontrada para atualizar.")
        return
    
    with open(arquivo_tarefas, "r") as arquivo:
        tarefas = arquivo.readlines()
    
    if not tarefas:
        messagebox.showinfo("Sem Tarefas", "Não há tarefas para atualizar.")
        return
    
    # Exibir tarefas para o usuário
    tarefas_formatadas = "\n".join([f"{i+1}. {t.strip()}" for i, t in enumerate(tarefas)])
    indice = simpledialog.askinteger("Atualizar Tarefa", f"Tarefas disponíveis:\n{tarefas_formatadas}\n\nDigite o número da tarefa que deseja atualizar:")
    
    if indice and 1 <= indice <= len(tarefas):
        nova_tarefa = simpledialog.askstring("Nova Descrição", "Digite a nova descrição da tarefa:")
        if nova_tarefa:
            tarefas[indice - 1] = nova_tarefa + "\n"
            with open(arquivo_tarefas, "w") as arquivo:
                arquivo.writelines(tarefas)
            messagebox.showinfo("Sucesso", "Tarefa atualizada com sucesso!")
    else:
        messagebox.showerror("Erro", "Número inválido.")

# Função para excluir uma tarefa
def excluir_tarefa():
    if not os.path.exists(arquivo_tarefas):
        messagebox.showwarning("Aviso", "Nenhuma tarefa encontrada para excluir.")
        return
    
    with open(arquivo_tarefas, "r") as arquivo:
        tarefas = arquivo.readlines()
    
    if not tarefas:
        messagebox.showinfo("Sem Tarefas", "Não há tarefas para excluir.")
        return
    
    # Exibir tarefas para o usuário
    tarefas_formatadas = "\n".join([f"{i+1}. {t.strip()}" for i, t in enumerate(tarefas)])
    indice = simpledialog.askinteger("Excluir Tarefa", f"Tarefas disponíveis:\n{tarefas_formatadas}\n\nDigite o número da tarefa que deseja excluir:")
    
    if indice and 1 <= indice <= len(tarefas):
        tarefa_excluida = tarefas.pop(indice - 1).strip()
        with open(arquivo_tarefas, "w") as arquivo:
            arquivo.writelines(tarefas)
        messagebox.showinfo("Sucesso", f"Tarefa '{tarefa_excluida}' excluída com sucesso!")
    else:
        messagebox.showerror("Erro", "Número inválido.")

# Função para sair do programa
def sair():
    janela.destroy()

# Configuração da janela principal
janela = tk.Tk()
janela.title("Gerenciador de Tarefas")

# Botões para cada funcionalidade
btn_criar = tk.Button(janela, text="Criar Tarefa", command=criar_tarefa, width=20)
btn_criar.pack(pady=10)

btn_atualizar = tk.Button(janela, text="Atualizar Tarefa", command=atualizar_tarefa, width=20)
btn_atualizar.pack(pady=10)

btn_excluir = tk.Button(janela, text="Excluir Tarefa", command=excluir_tarefa, width=20)
btn_excluir.pack(pady=10)

btn_sair = tk.Button(janela, text="Sair", command=sair, width=20)
btn_sair.pack(pady=10)

# Inicia o loop da interface gráfica
janela.mainloop()
