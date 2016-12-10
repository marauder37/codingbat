# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

import json
import os
import shutil
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

__metaclass__ = type


class GrabCode:
    """
    Save problems, test cases, and submitted answers from codingbat.com
    """

    BASE_HREF = "http://codingbat.com"
    nombre = "mabcat@e.mab.pm"
    contrasena = "*"

    sections = []
    problems = {}
    test_cases = {}
    answers = {}

    def __init__(self):
        self.load()

        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1120, 1000)

        self.login()
        self.get_sections()
        self.get_problems()
        self.get_answers()

    def login(self):
        self.driver.get(self.BASE_HREF)
        self.driver.find_element_by_name('uname').send_keys(self.nombre)
        self.driver.find_element_by_name('pw').send_keys(self.contrasena)
        self.driver.find_element_by_name('dologin').click()

    def get_answers(self):
        for section_name, section in self.problems.items():
            for href, name in section:
                self.get_test_cases(href, name)
                self.get_my_answer(href, name)

    def get_my_answer(self, href, name):
        if name not in self.answers:
            self.answers[name] = []

        self.driver.get(self.BASE_HREF + href)
        sleep(0.5)
        answer = self.driver.execute_script("return document.ace_editor.getValue();")
        self.answers[name] = answer.strip()
        self.dump()

    def get_test_cases(self, href, name):
        if name not in self.test_cases:
            self.test_cases[name] = []

        self.driver.get(self.BASE_HREF + href)

        soup = BeautifulSoup(self.driver.page_source, "lxml")
        for body_text in soup.select("table div.minh"):
            for sibling in body_text.next_siblings:
                if "→" in sibling:
                    self.test_cases[name].append(sibling)
        self.dump()

        self.driver.find_element_by_class_name('go').click()
        sleep(2)

        soup = BeautifulSoup(self.driver.page_source, "lxml")

        for test in soup.select('#tests td'):
            if "→" in test.get_text():
                print(test.get_text())
                self.test_cases[name].append(test.get_text())

        self.dump()

    def get_problems(self):
        problems = []

        for href, name in self.sections:
            self.driver.get(self.BASE_HREF + href)
            soup = BeautifulSoup(self.driver.page_source, "lxml")
            for problem in soup.select("div.tabin table a"):
                problems.append((
                    problem.get('href'),
                    problem.get_text()
                ))
            self.problems[name] = problems

    def get_sections(self):
        sections = []

        self.driver.get(self.BASE_HREF + "/python")
        soup = BeautifulSoup(self.driver.page_source, "lxml")

        for section in soup.find_all("div", class_="summ"):
            sections.append((
                section.find('a').get('href'),
                section.find('span', class_='h2').get_text()
            ))
        print(sections)

    def load(self):
        for var in ["problems", "test_cases", "answers", "sections"]:
            fn = var + ".json"
            if os.path.exists(fn):
                setattr(self, var, json.load(open(fn)))

    def dump(self):
        for var in ["problems", "test_cases", "answers", "sections"]:
            data = getattr(self, var)
            fn = var + ".json"
            if os.path.exists(fn):
                shutil.move(fn, fn+".bak")

            with open(fn, "w") as fh:
                json.dump(data, fh, sort_keys=True, indent=2, separators=(',', ': '))


if __name__ == "__main__":
    GrabCode()
