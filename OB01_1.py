# Задача: Создай класс `Task`, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task():
    def __init__(self):
      self.tasks = []

    def add_task (self, description, deadline, status):
        self.tasks.append({'description': description, 'deadline':deadline, 'status': status})
        print(f"Задача {self.tasks[-1]} добавлена")

    def show_tasks(self):
        print("Tекущие задачи:")
        for task in self.tasks:
            if task['status'] == "не выполнено":
                print(f"{task['description']} - {task['deadline']}")

    def accomplish_task(self, description):
        for task in self.tasks:
            if task['description'] == description:
                task['status'] = "выполнено"
                print (f"Задача {description} выполнена")

t = Task()
t.add_task("Купить продукты",  "15.01.2025", "не выполнено")
t.add_task("Позвонить другу",  "16.01.2025", "не выполнено")
t.add_task("Погулять с собакой",  "14.01.2025", "не выполнено")
t.show_tasks()
t.accomplish_task("Погулять с собакой")
t.show_tasks()
