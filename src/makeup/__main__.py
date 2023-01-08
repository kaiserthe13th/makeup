from argparse import ArgumentParser
from typing import List
from makeup.module_loader import Module

__version__ = "0.1.0"
ap = ArgumentParser(
    'makeup',
    description='Build your projects with ease and style🎨!',
)

ap.add_argument('-v', '--verbose', action='count', help="Increase verbosity by 1", default=0)
ap.add_argument('-q', '--quiet', action='count', help="Decrease verbosity by 1", default=0)
ap.add_argument('-m', '--module', nargs=1, help="The module which holds the tasks", default='makeup_tasks')
ap.add_argument('-V', '--version', action='store_true', help="Display program version and exit")

ap.add_argument('task', help="The task to run", nargs='?', default=None)
ap.add_argument('argv', help="Arguments for the task", nargs='*', default=None)

ap.add_argument('-l', '--list', dest='cmd', action='store_const', const='list', help='List tasks in module')

args = ap.parse_args()

args.verbosity = args.verbose - args.quiet
del args.verbose  # type: ignore
del args.quiet  # type: ignore

def pretty_name(x: str) -> str: return ''.join(map(lambda x: '-' if x == '_' else x, x))
def reverse_pretty(x: str) -> str: return ''.join(map(lambda x: '_' if x == '-' else x, x))
def separate_argv(argv: List[str]):
    args, kwargs = [], {}
    for i in argv:
        val = i.split('=', maxsplit=1)
        if len(val) > 1 and all(map(lambda x: not x.isspace(), val[0])) and val[0] != '':
            kwargs[reverse_pretty(val[0])] = val[1]
        else:
            args.append(val[0])
    return args, kwargs

def main():
    if args.version:
        if args.verbosity > -1:
            print(f"{ap.prog} {__version__}")
            if args.verbosity > 0:
                print(f"Copyright (C) Kerem Göksu <superkerem13@gmail.com>")
                print(f"License: MIT")
            if args.verbosity > 1:
                print("\nBuild your projects with ease and style🎨!")
        else:
            print(__version__)
    else:
        if args.cmd == 'list':
            print('available tasks:')
            taskmod = Module(args.module)
            for task in taskmod.tasks():
                print('-', pretty_name(task.__name__))
        elif args.task:
            taskmod = Module(args.module)

            argv, kwargv = separate_argv(args.argv)

            for task in taskmod.tasks():
                if args.task in (task.__name__, pretty_name(task.__name__)):
                    task(*argv, **kwargv)
                    break
            else:
                ap.error(f"task not found: {args.task}")
        else:
            ap.error("the following arguments are required: task")


if __name__ == '__main__':
    main()
