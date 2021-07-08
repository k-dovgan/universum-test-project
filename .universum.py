#!/usr/bin/env python

from universum.configuration_support import Configuration, Step

configs = Configuration([
    Step(name='Run script', command=['python3.7', 'run.py', 'pass'], artifacts="execution.log"),
    dict(name="Pylint check", code_report=True, command=[
        "python3.7", "-m", "universum.analyzers.pylint", "--result-file", "${CODE_REPORT_FILE}", "--files", "*.py"
    ])
])

if __name__ == '__main__':
    print(configs.dump())
