"""Input from files

The ``Input`` Space includes References that hold input values read from
the Excel input file, *input.xlsx*.
It also includes a few Cells to loock up values from the Referneces.

The References in this Space refer to `ExcelRange`_ objects.
The `ExcelRange` objects hold values read from ranges in the input
Excel file, *input.xlsx*. `ExcelRange`_ objects are Python's mapping objects,
so they support most methods that :obj:`dict` has, and can be
converted to :obj:`dict`. The table below lists the References
and their associated named ranges in *input.xlsx*.

==================== ====================
 References            Named ranges
==================== ====================
PolicyData             PolicyData
MortalityTables        MortalityTables
AssumptionTables       AsmpByDuration
Scenarios              Scenarios
DiscountRate           LargePolDiscount
==================== ====================


.. rubric:: References in this Space

Attributes:
    PolicyData: `ExcelRange`_ object holding policy data. The data
        is read from *PolicyData* range in *input.xlsx*.


    ProductSpec: `ExcelRange`_ object holding the data of product specs.
        The data is read from *ProductSpecTable* range in *input.xlsx*.

    Assumption: `ExcelRange`_ object holding the data of the assumption table.
        The data is read from *AssumptionTable* range in *input.xlsx*.

    MortalityTables: `ExcelRange`_ object holding the data of mortality Tables.
        The data is read from *MortalityTables* range in *input.xlsx*.

    AssumptionTables: `ExcelRange`_ object holding the data of assumptions by duration.
        The data is read from *AsmpByDuration* range in *input.xlsx*.

    Scenarios: `ExcelRange`_ object holding the data of economic scenarios.
        The data is read from *Scenarios* range in *input.xlsx*.

    DiscountRate: `ExcelRange`_ object holding the data of premium discount.
        The data is read from *LargePolDiscount* range in *input.xlsx*.


.. _ExcelRange:
   https://docs.modelx.io/en/latest/reference/dataspec.html#excelrange

.. _mapping:
   https://docs.python.org/3/glossary.html#term-mapping

"""

from modelx.serialize.jsonvalues import *

_formula = None

_bases = []

_allow_none = True

_spaces = []

# ---------------------------------------------------------------------------
# Cells

def AsmpLookup(asmp, prod=None, polt=None, gen=None):
    """Look up assumptions"""
    return Assumption.get((asmp, prod, polt, gen), None)


def SpecLookup(spec, prod=None, polt=None, gen=None):
    """Look up product specs"""
    return ProductSpec.get((spec, prod, polt, gen), None)


def TableLastAge(): 

    result = MortalityTables.idxmax()
    result.name = 'TableLastAge'
    return result


# ---------------------------------------------------------------------------
# References

PolicyData = ("Pickle", 2310405372040)

MortalityTables = ("Pickle", 2310405297480)

AssumptionTables = ("Pickle", 2310405213128)

Scenarios = ("Pickle", 2310406037576)

DiscountRate = ("Pickle", 2310411300616)

PremWaiverCost = ("Pickle", 2310411307208)

Assumption = ("Pickle", 2310411951624)

ProductSpec = ("Pickle", 2310411969480)