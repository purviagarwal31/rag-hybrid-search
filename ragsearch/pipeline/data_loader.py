import pandas as pd
import os
from django.conf import settings

def load_dataset(filename="arxiv_ai_dataset.csv"):
    filepath = os.path.join(settings.BASE_DIR, 'data', filename)

    try:
        df = pd.read_csv(filepath)
        print(f"✅ Loaded dataset with {len(df)} records")

        # ✅ Rename 'summary' to 'abstract' for consistency
        df.rename(columns={'summary': 'abstract'}, inplace=True)

        # ✅ Ensure 'title' and 'abstract' exist
        df.dropna(subset=['title', 'abstract'], inplace=True)
        df.drop_duplicates(subset='abstract', inplace=True)

        print(f"✅ Cleaned dataset: {len(df)} records after cleaning")
        return df

    except FileNotFoundError:
        print("❌ Dataset not found.")
        return pd.DataFrame()
