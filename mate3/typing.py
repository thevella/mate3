import typing as t

from .sunspec import model_base as MB
from . import read
from . import field_values as FV

Model = t.TypeVar('Model', bound=MB.Model)
ModelValues = t.TypeVar('ModelValues', bound=FV.ModelValues)