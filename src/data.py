# Extract Data script originally written by Marco Vieto. Modified by Jia Wei for this project.
import os
from pathlib import Path
import pandas as pd
import datetime

from clean import clean_dataset

absolute_path = Path().resolve()
raw_path = Path('data/raw')
full_raw_path = absolute_path / raw_path
processed_path = Path('data/processed')
full_processed_path = absolute_path / processed_path
final_path = Path('data/final')
full_final_path = absolute_path / final_path

folder_names = [
    folder
    for folder in os.listdir(full_raw_path)
    if os.path.isdir(os.path.join(full_raw_path, folder))
]

def convert_timestamp_to_date(ts):
    ts_seconds = ts / 1000.0
    return datetime.datetime.fromtimestamp(ts_seconds).strftime("%Y-%m-%d %H:%M:%S.%f")


def load_data():
    df = pd.DataFrame()
    for folder_name in folder_names:
        folder_path = os.path.join(full_raw_path, folder_name)
        subfolder_names = [
            subfolder
            for subfolder in os.listdir(folder_path)
            if not subfolder.startswith("control") and subfolder not in ["T022"]
            if os.path.isdir(os.path.join(folder_path, subfolder))
        ]

        subfolder_names.sort()

        for subfolder_name in subfolder_names:
            subfolder_path = os.path.join(folder_path, subfolder_name)

            txt_file_names = [
                file for file in os.listdir(subfolder_path) if file.endswith(".txt")
            ]

            subject_info = {}
            for file_name in txt_file_names:
                file_path = os.path.join(subfolder_path, file_name)
                with open(file_path, "r", encoding="windows-1252") as file:
                    content = (
                        file.read()
                        .replace(" ", "")
                        .replace("años", "")
                        .replace("Mujer", "F")
                        .replace("Varón", "M")
                        .replace("Diestro", "R")
                        .replace("Diestra", "R")
                        .replace("Control", "Y")
                    )

                    for i in range(len(content.split("."))):
                        if i == 0:
                            subject_info["Gender"] = content.split(".")[i]
                        elif i == 1:
                            subject_info["Age"] = content.split(".")[i]
                        elif i == 2:
                            subject_info["Hand"] = content.split(".")[i]
                        elif i == 3:
                            subject_info["Control"] = content.split(".")[i]

            svc_folders = [
                folder
                for folder in os.listdir(subfolder_path)
                if os.path.isdir(os.path.join(subfolder_path, folder))
            ]

            for svc_folder in svc_folders:
                svc_folder_path = os.path.join(subfolder_path, svc_folder)

                svc_folder_file_names = [
                    file for file in os.listdir(svc_folder_path) if file.endswith(".svc")
                ]

                for svc_file in svc_folder_file_names:
                    svc_data = pd.read_csv(
                        os.path.join(svc_folder_path, svc_file),
                        sep=" ",
                        skiprows=1,
                        header=None,
                    )

                    svc_data["subject"] = subfolder_name
                    svc_data["session"] = svc_file

                    if "Controles30jun14" in subfolder_path:
                        svc_data["control"] = "Y"
                        svc_data["hand"] = subject_info.get("Hand", None)
                        svc_data["gender"] = subject_info.get("Gender", None)
                        svc_data["age"] = subject_info.get("Age", None)
                    else:
                        svc_data["control"] = "N"
                        hand = "L"
                        if subfolder_name in [
                            "T001",
                            "T002",
                            "T005",
                            "T006",
                            "T008",
                            "T009",
                            "T014",
                            "T020",
                            "T021",
                            "T036",
                        ]:
                            hand = "R"

                        svc_data["hand"] = hand

                    df = pd.concat([df, svc_data])

    df.rename(
        columns={
            0: "x_coordinate",
            1: "y_coordinate",
            2: "timestamp",
            3: "state",
            4: "azimuth",
            5: "altitude",
            6: "pressure",
        },
        inplace=True,
    )

    df["date"] = df["timestamp"].apply(convert_timestamp_to_date)

    df = df[
        [
            "subject",
            "gender",
            "age",
            "hand",
            "x_coordinate",
            "y_coordinate",
            "timestamp",
            "state",
            "date",
            "azimuth",
            "altitude",
            "pressure",
            "control",
            "session",
        ]
    ]
    return df

def save_data(df):
    print(f"In total, there are {len(df['subject'].unique())} subjects in this dataset")
    print(f"There are {len(df[(df.control == 'Y')]['subject'].unique())} healthy subjects and {len(df[(df.control == 'N')]['subject'].unique())} sick subjects in this dataset")
    print(f"In total, there are {len(list(df['session'].unique()))} sessions in this dataset")
    print(f"There are {len(df[(df.control == 'Y')]['session'].unique())} healthy sessions and {len(df[(df.control == 'N')]['session'].unique())} sick sessions in this dataset")
    df.to_csv(f"{full_processed_path}/data_cleaned.csv", index=False)


if __name__ == "__main__":
    df = load_data()
    df = clean_dataset(df)
    save_data(df)
