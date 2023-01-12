from makeup.tasks import TaskInfo, task

@task()
def _task(): pass

@task()
def documented_task():
    """Documentation go brr..."""

@task(name='your_renamed_task')
def renamed_task(): pass

def test_task_has_taskinfo():
    assert hasattr(_task, '_makeup_task')
    assert isinstance(_task._makeup_task, TaskInfo)
    assert hasattr(renamed_task, '_makeup_task')
    assert isinstance(renamed_task._makeup_task, TaskInfo)
    assert hasattr(documented_task, '_makeup_task')
    assert isinstance(documented_task._makeup_task, TaskInfo)

def test_task_is_renamed():
    assert renamed_task._makeup_task.name == 'your_renamed_task'

def test_unnamed_task_has_func_name():
    assert _task._makeup_task.name == '_task'

def test_undocumented_task_none():
    assert _task._makeup_task.doc is None

def test_documented_task_doc():
    assert isinstance(documented_task._makeup_task.doc, str)
    assert documented_task._makeup_task.doc == """Documentation go brr..."""
