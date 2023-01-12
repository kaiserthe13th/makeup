from types import ModuleType

import pytest
from makeup.module_loader import Module
from makeup.tasks import TaskInfo

MODULE2LOAD = 'tests/assets/module2load'
MODULE2LOAD_NOT_HERE = 'tests/assets/module2load_not_here'

def test_module_load():
    m = Module(MODULE2LOAD)
    assert isinstance(m.m, ModuleType)
    assert m.m.example_task is not None
    assert m.m.some_helper(1) == 2

def test_module_load_file_not_found():
    with pytest.raises(FileNotFoundError):
        Module(MODULE2LOAD_NOT_HERE)

def test_module_tasks():
    m = Module(MODULE2LOAD)
    assert all(hasattr(i, '_makeup_task') for i in m.tasks())
    assert all(isinstance(i._makeup_task, TaskInfo) for i in m.tasks())
