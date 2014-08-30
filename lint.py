#!/usr/bin/python

"""lint.py: Lint utility for the WK-index project"""

import json
import os
import logging
import os.path

from optparse import OptionParser

__title__ = 'wk-lint'
__version__ = '0.0.1'
__author__ = "Eddie Blundell <eblundell@gmail.com>"
__credits__ = []


logging.basicConfig(level=logging.ERROR)

log = logging.getLogger(__name__)
lint_log = logging.getLogger("lint")


class LintRule():
    """Lint rule base class, used to specify lint rules.. for example required
    property or field value etc"""
    LEVEL = 'error'

    @staticmethod
    def lint(script):
        pass


class Linter():

    def __init__(self):
        self._rules = []
        self._file_count = 0
        self._scripts = {}

    def locate_scripts(self, directory):
        log.info("Loading directory %s", directory)

        for file_name in os.listdir(directory):
            log.info("Loading %s", file_name)
            full_path = os.path.join(directory, file_name)

            self._scripts[file_name] = self.load_script(file_name, full_path)
            self._file_count += 1

    def load_script(self, file_name, path):
        script_json = None

        try:
            script = open(path, 'r')
            script_json = script.read()
            self.lint(file_name, script_json)
        except (IOError):
            log.error("couldn't read %s", file_name)
        finally:
            script.close()

        return script_json

    def lint(self, file_name, script_json):
        try:
            json.loads(script_json)
        except ValueError as e:
            lint_log.error("file: %s error: %s", file_name, e)

    def concat(self, output_file):
        pass


if __name__ == "__main__":
    parser = OptionParser()

    parser.add_option("-o", "--output-file", dest="output_file")
    parser.add_option("-l", "--level",  dest="level", default="error")
    parser.add_option("-d", "--dir", dest="directory", default="scripts")

    (options, args) = parser.parse_args()

    linter = Linter()
    linter.locate_scripts(options.directory)

    for (name, script) in linter._scripts.iteritems():
        linter.lint(name, script)
