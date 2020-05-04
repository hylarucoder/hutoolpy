import time

from prevenger.contrib.progress import GeneratorProgressBar


def process(value):
    time.sleep(0.01)
    return value


def test_generator_progress_bar():
    def process_tasks_gene(tasks):
        for task in tasks:
            task_result = process(task)
            yield task_result

    tasks = [1, 2, 3]
    gene = process_tasks_gene(tasks)
    GeneratorProgressBar(0, len(tasks), 1, gene).begin()
    gene = process_tasks_gene(tasks)
    GeneratorProgressBar(0, None, 1, gene).begin()
