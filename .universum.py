#!/usr/bin/env python3.7

from universum.configuration_support import Configuration, Step

configs = Configuration([
    Step(name='Run script', command=['python', 'run.py', 'pass']),
    dict(name="Pylint check", code_report=True, command=[
        "python", "-m", "universum.analyzers.pylint", "--python-version", "3.7",
        "--result-file", "${CODE_REPORT_FILE}", "--files", "*.py"
    ])
])

if __name__ == '__main__':
    print(configs.dump())
