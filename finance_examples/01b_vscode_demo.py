# Python Script to run with VS Code

# Motivation: Show something we can only do with VS Code, for example: visaul debugging.

import numpy as np
import pandas as pd

df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)

dfgb = df.groupby("A")[["C", "D"]].sum()

print(dfgb)