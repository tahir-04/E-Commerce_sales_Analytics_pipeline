def validate_not_empty(df, name):
    if df.empty:
        raise Exception(
            f"{name} is empty"
        )
    
def validate_columns(
    df,
    expected_columns
):
    missing = [
        col
        for col in expected_columns
        if col not in df.columns
    ]

    if missing:
        raise Exception(
            f"Missing columns: {missing}"
        )
    
def validate_duplicates(
    df,
    key_column
):
    duplicates = df[
        key_column
    ].duplicated().sum()

    print(
        f"{key_column} duplicates:",
        duplicates
    )