import flet as ft

def main(page: ft.Page):
    page.title = '✅ Lista de Tarefas'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    tarefas = ft.Column()

    def adicionar_tarefa(e):
        if campo_tarefa.value.strip() != '':
            tarefas.controls.append(ft.Text(campo_tarefa.value))
            campo_tarefa.value = ''
            page.update()

    campo_tarefa = ft.TextField(label='Digite uma tarefa', width=300)
    botao_adicionar = ft.ElevatedButton('Adicionar', on_click=adicionar_tarefa)

    page.add(
        ft.Text('📋 Lista de Tarefas', style='headlineMedium'),
        campo_tarefa,
        botao_adicionar,
        tarefas
    )

ft.app(target=main)
