from hutoolpy.timing import timethis


class GeneratorProgressBar:
    """
    用于 Profile 快速 timing 某段代码
    def process(a):
        import time
        time.sleep(1)
        return a
    原先函数为
    def process_tasks(tasks):
        for task in tasks:
            v = process(task)
    tasks = [task1,task2,task3]
    process_tasks(tasks)
    调整函数为生成器
    def process_tasks_gene(tasks):
        for task in tasks:
            v = process(task)
            yield v
    tasks = [task1,task2,task3]
    gene = process_tasks_gene(tasks)
    GeneratorProgressBar(0,len(tasks),1,gene).start()
    """

    def __init__(self, start=0, stop=None, step=1, generator=None):
        self.current = 0
        self.start = start
        self.stop = stop
        self.step = step
        if not generator:
            raise ValueError("generator not found")
        self.generator = generator
        pass

    @timethis
    def log(self, msg):
        if self.stop is None:
            print("{:<30}".format(self.current), msg)
        else:
            print("进度为百分比为 {:<30.2f}".format(self.current / self.stop * 100), msg)
        self.current += self.step

    def begin(self):
        for msg in self.generator:
            self.log(msg)
