# Python Script to run with VS Code

# Motivation: Show something we can only do with VS Code, for example: visaul debugging.

import nasdaqdatalink
import pandas as pd

import warnings
warnings.filterwarnings("ignore")

nasdaqdatalink.read_key(filename="~/shared/PyDataNYC/nasdaq_api_key")
_x = 1e3
date = pandas.DatetimeIndex(["2000-01-01"])[0]
data = nasdaqdatalink.get("FRED/GDP")
data["gdp_bil"] = data.Value.apply(lambda x_: x_/_x)
gdp2000 = data.at[date].gdp_bil
data["difference"] = data.gdp_bil.diff()
big_drop_date, big_drop = data.difference.idxmin(), data.difference.min()
dtstrfmt = '%B %Y'
big_jump_date, big_jump = data.difference.idxmax(), data.difference.max()
print(f"The largest quarter-on-quarter decrease was {big_drop;.4g} billion USD, recorded for the three months prior to {big_drop_date.strftime(dtstrfmt)}.")
print(f"The largest quarter-on-quarter increase was {big_jump:.4g} billion USD, recorded for the three months prior to {big_jump_date.strftime(dtstrfmt)}.")
print(f"The US GDP was {gdp2000:.4g} billon USD in {date.strftime(dtstrfmt)}.")
