import importlib
import importlib.util
import sys
from types import ModuleType
from .tasks import TaskInfo


class Module:
    def __init__(self, module: str) -> None:
        self._m_name = module
        self.m = self._load_module()
        self.__tasks_cache = []

    def _load_module(self) -> ModuleType:
        spec = importlib.util.spec_from_file_location(self._m_name, f'./{self._m_name}.py')
        if spec:
            taskmod = importlib.util.module_from_spec(spec)
            sys.modules[self._m_name] = taskmod
            if spec.loader:
                spec.loader.exec_module(taskmod)

            return taskmod
        raise ImportError(f"Failed to import {self._m_name}")

    def tasks(self):
        if self.__tasks_cache:
            yield from self.__tasks_cache
            return
        for i in self.m.__dir__():
            j = getattr(self.m, i)
            if hasattr(j, "_makeup_task") and isinstance(j._makeup_task, TaskInfo):
                self.__tasks_cache.append(j)
                yield j

    def collect_tasks(self):
        if not self.__tasks_cache:
            for _ in self.tasks():
                pass
        return self.__tasks_cache
