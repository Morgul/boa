from copy import copy

from colorama import Fore, Style

from .feature import Feature
from .exceptions import exceptions


class Suite():
    def __init__(self, description, indent):
        self.description = description
        self.indent = copy(indent)

        self._before = None
        self._after = None

    def __call__(self, *args, **kwargs):
        return self.feature(*args, **kwargs)

    def __enter__(self):
        if self.indent == 0:
            print "\n"
        else:
            print ""

        self._printWithIndent(Style.BRIGHT + "{}" + Style.RESET_ALL)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.indent == 0:
            print "----------------------------------------------"
            print Fore.GREEN + ("  {}/{} Succeeded"
                    + Fore.RESET
                    + ","
                    + Fore.RED
                    + " {} Failed"
                    + Fore.RESET
                    + ","
                    + Fore.CYAN
                    + " {} Skipped"
                    + Fore.RESET
                ).format(Feature.getSucceededCount(), Feature.getTestCount(), Feature.getFailedCount(), Feature.getSkippedCount())
            idx = 1
            for ex in exceptions:
                print "\n" + str(idx) + ')' + Fore.RED + ' {}'.format(ex['feature']) + Fore.RESET
                print "{}".format(ex['exception'])
                #print "Got EX:", ex['feature'], ex['exception']
                idx += 1
        return False

    #-------------------------------------------------------------------------------------------------------------------
    # API
    #-------------------------------------------------------------------------------------------------------------------

    def before(self, func):
        self._before = func
        return func

    def after(self, func):
        self._after = func
        return func

    def feature(self, description):
        feat = Feature(description, self.indent + 2)
        feat.before = self._before
        feat.after = self._after

        return feat

    def skip(self, description):
        return Feature(description, self.indent + 2, skip=True)

    #-------------------------------------------------------------------------------------------------------------------
    # Aliases
    #-------------------------------------------------------------------------------------------------------------------

    def _(self, *args, **kwargs):
        return self.skip(*args, **kwargs)

    def it(self, *args, **kwargs):
        return self.feature(*args, **kwargs)

    #-------------------------------------------------------------------------------------------------------------------

    def _printWithIndent(self, fmt):
        print "".join([" " for i in range(self.indent)]) + fmt.format(self.description)
