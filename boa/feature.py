# coding: utf-8
import traceback
from colorama import Fore, Style

from .exceptions import exceptions

tests = 0
failed = 0
skipped = 0
succeeded = 0

class Feature():
    def __init__(self, description, indent=2, skip=False):
        global tests

        self.description = description
        self.skip = skip
        self.indent = indent
        self.before = None
        self.after = None

        tests += 1

    def __call__(self, *args, **kwargs):
        return self.run(*args, **kwargs)

    def run(self, func):
        global failed, succeeded, skipped
        if(self.skip):
            skipped += 1
            self._printWithIndent(Fore.CYAN + "- {}" + Fore.RESET)
        else:
            try:
                succeeded += 1
                if callable(self.before):
                    self.before()
                func()
                if callable(self.after):
                    self.after()
                self._printWithIndent(Fore.GREEN + "✓" + Fore.RESET + " {}")

            except Exception as ex:
                failed += 1
                self._printWithIndent(Fore.RED + "x {}" + Fore.RESET)
                exceptions.append({'feature': self.description, 'exception': traceback.format_exc()})

        return func

    def _printWithIndent(self, fmt):
        print "".join([" " for i in range(self.indent)]) + fmt.format(self.description)

    @staticmethod
    def getTestCount():
        global tests
        return tests

    @staticmethod
    def getSucceededCount():
        global succeeded
        return succeeded

    @staticmethod
    def getFailedCount():
        global failed
        return failed

    @staticmethod
    def getSkippedCount():
        global skipped
        return skipped
