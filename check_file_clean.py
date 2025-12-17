import pandas as pd
import numpy as np

# REPLACE THIS with your actual file path
file_path = C:\Users\mateu\Downloads\BMW sales data (2010-2024) (1) (1).csv

try:
    # Load the dataset
    df = pd.read_csv(file_path)
    print("✅ Data Loaded Successfully.\n")
    print(f"Dataset Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    print("-" * 40)

    # 1. Check for Standard Missing Values (NaN/Null)
    missing_counts = df.isnull().sum()
    total_missing = missing_counts.sum()
    
    if total_missing > 0:
        print("\n⚠️  MISSING VALUES FOUND:")
        print(missing_counts[missing_counts > 0])
    else:
        print("\n✅ No standard missing values (NaN) found.")

    # 2. Check for Entirely Empty Rows
    empty_rows = df.isnull().all(axis=1).sum()
    if empty_rows > 0:
        print(f"\n⚠️  Found {empty_rows} rows that are completely empty.")
    else:
        print("✅ No completely empty rows found.")

    # 3. Check for Entirely Empty Columns
    empty_cols = df.columns[df.isnull().all()].tolist()
    if empty_cols:
        print(f"\n⚠️  Found completely empty columns: {empty_cols}")
    else:
        print("✅ No completely empty columns found.")

    # 4. Check for 'Hidden' Empty Strings (e.g., " " or "")
    # This checks text columns for cells that are not NaN but contain only whitespace
    print("\n🔍 Checking for hidden empty strings in text columns...")
    found_hidden = False
    for col in df.select_dtypes(include=['object']):
        # Coerce to string, strip whitespace, check if length is 0
        empty_str_count = df[col].astype(str).str.strip().eq('').sum()
        if empty_str_count > 0:
            print(f"   -> Column '{col}' has {empty_str_count} empty string values.")
            found_hidden = True
    
    if not found_hidden:
        print("✅ No hidden empty strings found.")

    # 5. Check for Duplicate Rows
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        print(f"\n⚠️  Found {duplicates} duplicate rows.")
    else:
        print("\n✅ No duplicate rows found.")

except FileNotFoundError:
    print("❌ Error: The file was not found. Please check the 'file_path' variable.")
except Exception as e:
    print(f"❌ An error occurred: {e}")