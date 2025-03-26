import polars as pl

try:
    # Read the TSV file without interpreting quote characters
    df = pl.read_csv(
        'name.basics.tsv',
        separator='\t',
        ignore_errors=True,  # Skip rows with parsing errors
        infer_schema_length=10000,  # Increase schema inference sample size
        quote_char=None  # Disable quote parsing
    )

    # Show the first few rows
    print("First few rows:")
    print(df.head())

except FileNotFoundError:
    print("Error: File not found. Make sure name.basics.tsv exists in the current directory.")
except Exception as e:
    print(f"Error: {e}")
