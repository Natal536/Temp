from pathlib import Path
import pandas as pd

root = Path(r"C:\Users\user\Students\CREMA-D")
#This is for show
files = [
    "finishedResponses.csv",
    "finishedEmoResponses.csv",
    "finishedResponsesWithRepeatWithPractice.csv",
    "processedResults/summaryTable.csv",
    "processedResults/tabulatedVotes.csv",
    "VideoDemographics.csv",
]

for filename in files:
    df = pd.read_csv(root / filename, low_memory=False)

    print(f"\n{'=' * 75}")
    print(filename, df.shape)

    for column in df.columns:
        values = df[column].dropna()
        unique_count = values.nunique()

        print(
            f"{column:25} "
            f"dtype={str(df[column].dtype):8} "
            f"missing={df[column].isna().sum():6} "
            f"unique={unique_count:7} "
            f"examples={values.drop_duplicates().head(8).tolist()}"
        )
