# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

import json

__metaclass__ = type

class MakeAnswers:
    """
    Write submitted answers and unit tests to Python files
    """

    def __init__(self):
        problems = json.load(file("problems.json"))
        answers = json.load(file("answers.json"))
        test_cases = json.load(file("test_cases.json"))

        answers_fh = open("answers.py", "w")
        answers_fh.write("## generated code, don't edit, use make_answers.py to generate\n\n")

        test_fh = open("test_answers.py", "w")
        test_fh.write("## generated code, don't edit, use make_answers.py to generate\n\nfrom answers import *\n\n")

        for section, questions in problems.items():
            answers_fh.write("\n\n# {}\n\n".format(section))
            test_fh.write("\n\n# {}\n\n".format(section))

            for href, name in questions:
                answers_fh.write(answers[name].replace("  ", "    ")+'\n\n')

                for i, case in enumerate(set(test_cases[name])):
                    call, expected = case.split(" → ")
                    test_fh.write("def test_{}_{}():\n    assert {} == {}\n\n".format(name, i, call, expected))


if __name__ == "__main__":
    MakeAnswers()
