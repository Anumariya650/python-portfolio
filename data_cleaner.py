import pandas as pd
def clean_csv (input_file,output_file):
    df = pd.read_csv(input_file)
    df = df.drop_duplicates()
    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
    for col in df.columns:
        if "date" in col.lower():
            df[col] = pd.to_datetime(df[col], errors='coerce').dt.strftime('%Y-%m-%d')
    df.to_csv(output_file,index=False)
    print(f"Cleaned csv is saved in {output_file}")
if __name__ == "__main__":
    clean_csv("dirty_csv","cleaned_csv")



