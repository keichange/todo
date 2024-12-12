import flet as ft

class ToDoApp(ft.Column):
    def __init__(self):
        super().__init__()
        self.new_task = ft.TextField(hint_text="what's needs to be done", expand=True  )
        self.tasks_view = ft.Column()
        self.width=600
        self.controls = [
            ft.Row(
                controls=[
                    self.new_task,
                    ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=self.add_clicked)
                ]
            ),
            self.tasks_view
        ]
    
    def add_clicked(self, e):
        self.tasks_view.controls.append(ft.Checkbox(label=self.new_task.value))
        self.new_task.value = ""
        self.update()

def main(page: ft.Page):
    page.title="ToDoApp"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    todo = ToDoApp()

    page.add(todo)

ft.app(main)
