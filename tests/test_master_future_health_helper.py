from __future__ import absolute_import

# Put Pip Imports Here:
from freezegun import freeze_time


class Foo:
    @freeze_time('2017-12-31')
    def qux(self):
        pass

    def quux(self):
        pass
