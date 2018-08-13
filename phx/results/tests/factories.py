from factory.fuzzy import FuzzyText
from factory_djoy import CleanModelFactory

from ..models import Result


class ResultFactory(CleanModelFactory):
    summary = FuzzyText()
    results = FuzzyText()
    results_url = 'http://example.com'

    class Meta:
        model = Result
