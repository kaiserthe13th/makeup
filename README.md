# MakeUp 💄

<p align="center">
    <strong>Build your projects with ease and style🎨!</strong>
</p>

> **WARNING:** This project is at *very experimental* stages.

MakeUp is an easy to use language agnostic build tool inspired by the likes of [make](https://www.gnu.org/software/make/), [CMake](https://github.com/Kitware/CMake), [SCons](https://github.com/SCons/scons) intended to be easy to use while retaining high customizability.

## Getting Started ⚡

1. Install makeup 🚀
  ```console
  $ pip install pymakeup
  or
  $ poetry add pymakeup
  
  Not yet, for now do:
  $ git clone https://github.com/kaiserthe13th/makeup.git
  $ cd makeup
  $ pip install .
  ```
2. Start a new project 📜
  
  ```console
  $ makeup --new [your_project]
  or
  $ makeup --init
  ```
3. Create a task 🎮
  ```py
  from typing import Union
  from functools import reduce

  @task()
  def add(*args: Union[int, float]):
      print(reduce(lambda x, y: x + y, args, 0))
  ```
4. Use it as you please
  ```console
  $ makeup add 2 2
  4
  $ makeup add 1.2 2.4
  3.6
  ```

## Features 🎯

- Make style task creation and execution, with the programmatic capabilities of Python
- Much more versatile, not just a build tool, but also a task runner
- Tasks with defaults, arguments and keyword arguments in the command line
- Just write what type you want, it will be validated and processed for you
- Easy access the environment (with .env support)

## 💡 Philosophy

I've always liked [make](https://www.gnu.org/software/make/), [CMake](https://github.com/Kitware/CMake) and [SCons](https://github.com/SCons/scons). However I always had my frustrations with them. CMake and Scons are complicated and have steep learning curves. And CMake isn't versatile. make while more versatile isn't so much when it is a pain to do if-elses, it can't take arguments without workarounds. It is too simple.

As a solution to all of this, I started developing a middle ground. One that will be easy to learn, yet capable. A system taking advantage of the capabilities of Python and able to realize the effectiveness of type annotations.
