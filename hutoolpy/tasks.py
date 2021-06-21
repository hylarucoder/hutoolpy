import typing as t


class TaskRegister:
    task_map: dict

    def __init__(self):
        self.task_map = {}

    def add_task(self, name, func, **options):
        self.task_map[name] = func

    def task(self, name, **options):
        def decorator(f: t.Callable) -> t.Callable:
            self.add_task(name, f, **options)
            return f

        return decorator

    def list_tasks(self):
        print(self.task_map)

    def run_tasks(self):
        for k, v in self.task_map.items():
            print(k, v())

    def send_task(self, name):
        print(self.task_map)


register = TaskRegister()


@register.task("simple tasks")
def task():
    print("simple tasks")


register.list_tasks()
register.run_tasks()
