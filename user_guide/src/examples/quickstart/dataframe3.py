import polars as pl
import numpy as np

df = pl.DataFrame({"x": np.arange(0, 8), "y": ["A", "A", "A", "B", "B", "C", "X", "X"]})