import sys
import inspect

from audit.Audit import Audit
from audit.RLA import RLA
from audit.Bayesian import Bayesian


def get_audits():
    audits = []

    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            audits.append(obj)

    return audits
