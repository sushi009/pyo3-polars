import polars as pl
from extend_polars import parallel_jaccard

df = pl.DataFrame({
    "list_a": [[1, 2, 3], [5, 5]],
    "list_b": [[1, 2, 3, 8], [5, 1, 1]]
})

print(df)
print(parallel_jaccard(df, "list_a", "list_b"))