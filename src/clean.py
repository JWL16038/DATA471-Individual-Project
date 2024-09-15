# Clean data script originally written by Marco Vieto. Modified by Jia Wei for this project.

def clean_control_sessions(df):
    control_sessions_to_remove = {
        "C01": ["u00003s00002_hw00001.svc"],
        "C02": ["u00004s00001_hw00001.svc"],
        "C03": ["u00005s00001_hw00001.svc"],
        "C04": ["u00006s00001_hw00001.svc"],
        "C05": ["u00007s00001_hw00001.svc"],
        "C06": ["u00008s00001_hw00001.svc"],
        "C07": ["u00009s00001_hw00001.svc"],
        "C08": ["u00010s00001_hw00001.svc"],
        "C09": ["u00011s00001_hw00001.svc"],
        "C10": ["u00012s00001_hw00001.svc"],
    }

    # Remove records from control_sessions_to_remove
    for subject, sessions in control_sessions_to_remove.items():
        df = df[~((df.subject == subject) & (df.session.isin(sessions)))]

    # Clean C07, u00012s00001_hw000012 session
    df = df[
    ~(
            (df["y_coordinate"] < 5000)
            & (df["session"] == "u00009s00001_hw000012.svc")
            & (df.subject == "C07")
        )
    ]

    # Clean C08, u00010s00001_hw000011 session
    df = df[
        ~(
            (df["y_coordinate"] > 8000)
            & (df["session"] == "u00010s00001_hw000011.svc")
            & (df.subject == "C08")
        )
    ]

    # Clean C09, u00011s00001_hw000011 session
    df = df[
        ~(
            (df["y_coordinate"] > 7000)
            & (df["session"] == "u00011s00001_hw000011.svc")
            & (df.subject == "C09")
        )
    ]

    # Clean C10, u00012s00001_hw000012 session
    df = df[
        ~(
            (df["y_coordinate"] < 5000)
            & (df["session"] == "u00012s00001_hw000012.svc")
            & (df.subject == "C10")
        )
    ]

    # Clean C07, u00012s00001_hw000012 session
    df = df[
        ~(
            (df["y_coordinate"] < 5000)
            & (df["session"] == "u00009s00001_hw000012.svc")
            & (df.subject == "C07")
        )
    ]

    # Clean C08, u00010s00001_hw000011 session
    df = df[
        ~((df["y_coordinate"] > 8000)
        & (df["session"] == "u00010s00001_hw000011.svc")
        & (df.subject == "C08"))
    ]

    # Clean C09, u00011s00001_hw000011 session
    df = df[
        ~(
            (df["y_coordinate"] > 7000)
            & (df["session"] == "u00011s00001_hw000011.svc")
            & (df.subject == "C09")
        )
    ]

    # Clean C10, u00012s00001_hw000012 session
    df = df[
        ~(
            (df["y_coordinate"] < 5000)
            & (df["session"] == "u00012s00001_hw000012.svc")
            & (df.subject == "C10")
        )
    ]

    # Remove C07, u00009s00001_hw00002 session, only one data point
    df = df[
        ~(
            (df.session== "u00009s00001_hw00002.svc")
            & (df.subject == "C07")
        )
    ]

    # Remove T001, u00009s00001_hw00002 session, only one data point
    df = df[~((df.session == "u00005s00001_hw00003.svc") & (df.subject == "T001"))]

    # Remove C01, u00003s00002_hw000011 session state 0 and pressure also 0
    df = df[
        ~(
            (df.session == "u00003s00002_hw000011.svc")
            & (df.subject == "C01")
            & (df.state == 0)
        )
    ]
    return df


def clean_noncontrol_sessions(df):
    non_control_sessions_to_remove = {
        "T005": ["u00009s00001_hw00001.svc"],
        "T006": ["u00010s00001_hw00003.svc"],
    }

    # Remove records from control_sessions_to_remove
    for subject, sessions in non_control_sessions_to_remove.items():
        df = df[~((df.subject == subject) & (df.session.isin(sessions)))]


    # Clean T001,
    df = df[
        ~(
            ((df["y_coordinate"] < 6_100) | (df["x_coordinate"] > 4_700))
            & (df["session"] == "u00005s00001_hw00004.svc")
            & (df.subject == "T001")
        )
    ]

    df = df[
        ~(
            (
                (df["x_coordinate"] > 3_300)
                | ((df["y_coordinate"] > 6_500) & (df["x_coordinate"] < 400))
            )
            & (df["session"] == "u00005s00001_hw00002.svc")
            & (df.subject == "T001")
        )
    ]

    # Clean T002,
    df = df[
        ~(
            (df["x_coordinate"] > 3_000)
            & (df["session"] == "u00006s00001_hw00004.svc")
            & (df.subject == "T002")
        )
    ]

    # Clean T005,
    df = df[
        ~(
            (df["y_coordinate"] > 5_500)
            & (df["session"] == "u00009s00001_hw000011.svc")
            & (df.subject == "T005")
        )
    ]

    # Clean T006,
    df = df[
        ~(
            (
                ((df["x_coordinate"] < 3_700) & (df["y_coordinate"] < 2_500))
                | (df["y_coordinate"] > 6_000)
            )
            & (df["session"] == "u00010s00001_hw00002.svc")
            & (df.subject == "T006")
        )
    ]

    df = df[
        ~(
            (df["y_coordinate"] < 6_000)
            & (df["session"] == "u00010s00001_hw00001.svc")
            & (df.subject == "T006")
        )
    ]

    # Clean T008,
    df = df[
        ~(
            (df["y_coordinate"] > 4_850)
            & (df["session"] == "u00013s00001_hw00001.svc")
            & (df.subject == "T008")
        )
    ]

    # Clean T009,
    df = df[
        ~(
            (df["y_coordinate"] < 8_450)
            & (df["session"] == "u00014s00001_hw00001.svc")
            & (df.subject == "T009")
        )
    ]

    # Clean T011,
    df = df[
        ~(
            (df["x_coordinate"] > 3_100)
            & (df["session"] == "u00004s00001_hw00003.svc")
            & (df.subject == "T011")
        )
    ]

    df = df[
        ~(
            (df["y_coordinate"] < 6_000)
            & (df["session"] == "u00004s00001_hw00002.svc")
            & (df.subject == "T011")
        )
    ]

    df = df[
        ~(
            (df["x_coordinate"] > 2_000)
            & (df["session"] == "u00004s00001_hw00005.svc")
            & (df.subject == "T011")
        )
    ]

    # Clean T012,
    df = df[
        ~(
            (df["y_coordinate"] < 6_000)
            & (df["session"] == "u00005s00001_hw00002.svc")
            & (df.subject == "T012")
        )
    ]

    # Clean T013,
    df = df[
        ~(
            ((df["y_coordinate"] > 5_000) | (df["x_coordinate"] > 3_300))
            & (df["session"] == "u00006s00001_hw00003.svc")
            & (df.subject == "T013")
        )
    ]

    df = df[
        ~(
            (df["x_coordinate"] > 3_000)
            & (df["session"] == "u00006s00001_hw00005.svc")
            & (df.subject == "T013")
        )
    ]

    df = df[
        ~(
            (df["x_coordinate"] > 2_800)
            & (df["session"] == "u00006s00001_hw00004.svc")
            & (df.subject == "T013")
        )
    ]

    # Clean T014,
    df = df[
        ~(
            (df["y_coordinate"] > 5_500)
            & (df["session"] == "u00007s00001_hw00001.svc")
            & (df.subject == "T014")
        )
    ]

    df = df[
        ~(
            (df["y_coordinate"] < 6_500)
            & (df["session"] == "u00007s00001_hw00002.svc")
            & (df.subject == "T014")
        )
    ]

    # Clean T015,
    df = df[
        ~(
            ((df["y_coordinate"] >= 4_230) & (df["x_coordinate"] <= 4_260))
            & (df["session"] == "u00008s00001_hw00001.svc")
            & (df.subject == "T015")
        )
    ]

    # Clean T018,
    df = df[
        ~(
            ((df["x_coordinate"] < 4_100) | (df["x_coordinate"] > 6_500))
            & (df["session"] == "u00009s00001_hw00001.svc")
            & (df.subject == "T018")
        )
    ]

    # Clean T020,
    df = df[
        ~(
            (df["x_coordinate"] > 3_500)
            & (df["session"] == "u00011s00001_hw00004.svc")
            & (df.subject == "T020")
        )
    ]

    df = df[
        ~(
            ((df["x_coordinate"] > 3_100) | (df["x_coordinate"] < 1_850))
            & (df["session"] == "u00011s00001_hw00003.svc")
            & (df.subject == "T020")
        )
    ]

    df = df[
        ~(
            ((df["x_coordinate"] > 6_500) | (df["y_coordinate"] > 5_000))
            & (df["session"] == "u00011s00001_hw00001.svc")
            & (df.subject == "T020")
        )
    ]

    # Clean T021,
    df = df[
        ~(
            (df["y_coordinate"] < 3_000)
            & (df["session"] == "u00014s00001_hw00004.svc")
            & (df.subject == "T021")
        )
    ]

    df = df[
        ~(
            (df["x_coordinate"] > 3_500)
            & (df["session"] == "u00014s00001_hw00003.svc")
            & (df.subject == "T021")
        )
    ]

    # Clean T023,
    df = df[
        ~(
            (df["x_coordinate"] > 3_000)
            & (df["session"] == "u00016s00001_hw00004.svc")
            & (df.subject == "T023")
        )
    ]

    df = df[
        ~(
            (df["y_coordinate"] > 5_000)
            & (df["session"] == "u00016s00001_hw00001.svc")
            & (df.subject == "T023")
        )
    ]

    df = df[
        ~(
            (df["y_coordinate"] < 6_000)
            & (df["session"] == "u00016s00001_hw00002.svc")
            & (df.subject == "T023")
        )
    ]

    df = df[
        ~(
            (df["x_coordinate"] > 3_000)
            & (df["session"] == "u00016s00001_hw00003.svc")
            & (df.subject == "T023")
        )
    ]

    # Clean T025,
    df = df[
        ~(
            (df["y_coordinate"] > 6_000)
            & (df["session"] == "u00017s00001_hw00001.svc")
            & (df.subject == "T025")
        )
    ]

    df = df[
        ~(
            (df["y_coordinate"] < 6_000)
            & (df["session"] == "u00017s00001_hw00002.svc")
            & (df.subject == "T025")
        )
    ]

    df = df[
        ~(
            (df["x_coordinate"] > 4_000)
            & (df["session"] == "u00017s00001_hw00003.svc")
            & (df.subject == "T025")
        )
    ]

    df = df[
        ~(
            (df["x_coordinate"] > 3_000)
            & (df["session"] == "u00017s00001_hw00004.svc")
            & (df.subject == "T025")
        )
    ]

    df = df[
        ~(
            (df["x_coordinate"] > 3_000)
            & (df["session"] == "u00017s00001_hw00005.svc")
            & (df.subject == "T025")
        )
    ]

    # Clean T026,
    df = df[
        ~(
            (df["x_coordinate"] > 3_500)
            & (df["session"] == "u00019s00001_hw00004.svc")
            & (df.subject == "T026")
        )
    ]

    df = df[
        ~(
            (df["x_coordinate"] > 3_500)
            & (df["session"] == "u00019s00001_hw00005.svc")
            & (df.subject == "T026")
        )
    ]

    df = df[
        ~(
            (df["x_coordinate"] < 3_900)
            & (df["session"] == "u00019s00001_hw00001.svc")
            & (df.subject == "T026")
        )
    ]

    df = df[
        ~(
            (df["y_coordinate"] < 6_000)
            & (df["session"] == "u00019s00001_hw00002.svc")
            & (df.subject == "T026")
        )
    ]

    df = df[
        ~(
            (df["x_coordinate"] > 3_500)
            & (df["session"] == "u00019s00001_hw00003.svc")
            & (df.subject == "T026")
        )
    ]

    # Clean T027,
    df = df[
        ~(
            (df["x_coordinate"] > 3_250)
            & (df["session"] == "u00020s00001_hw00004.svc")
            & (df.subject == "T027")
        )
    ]

    df = df[
        ~(
            (df["y_coordinate"] > 5_500)
            & (df["session"] == "u00020s00001_hw00001.svc")
            & (df.subject == "T027")
        )
    ]

    # Clean T028,
    df = df[
        ~(
            (df["y_coordinate"] < 8_800)
            & (df["session"] == "u00021s00001_hw00001.svc")
            & (df.subject == "T028")
        )
    ]

    df = df[
        ~(
            (df["y_coordinate"] < 6_000)
            & (df["session"] == "u00021s00001_hw00003.svc")
            & (df.subject == "T028")
        )
    ]

    df = df[
        ~(
            (df["x_coordinate"] > 3_500)
            & (df["session"] == "u00021s00001_hw00002.svc")
            & (df.subject == "T028")
        )
    ]

    df = df[
        ~(
            (df["x_coordinate"] < 4_000)
            & (df["session"] == "u00021s00001_hw00005.svc")
            & (df.subject == "T028")
        )
    ]

    # Clean T029,
    df = df[
        ~(
            (df["x_coordinate"] < 4_000)
            & (df["session"] == "u00022s00001_hw00005.svc")
            & (df.subject == "T029")
        )
    ]

    df = df[
        ~(
            (df["x_coordinate"] < 4_000)
            & (df["session"] == "u00022s00001_hw00004.svc")
            & (df.subject == "T029")
        )
    ]

    df = df[
        ~(
            (df["y_coordinate"] < 9_100)
            & (df["session"] == "u00022s00001_hw00001.svc")
            & (df.subject == "T029")
        )
    ]

    df = df[
        ~(
            (df["y_coordinate"] < 6_000)
            & (df["session"] == "u00022s00001_hw00003.svc")
            & (df.subject == "T029")
        )
    ]

    df = df[
        ~(
            (df["x_coordinate"] > 3_170)
            & (df["session"] == "u00022s00001_hw00002.svc")
            & (df.subject == "T029")
        )
    ]
    return df


def clean_dataset(df):
    df = df.groupby(["subject", "session"]).filter(lambda x: len(x) > 1)

    # Fix incorrect value
    df["x_coordinate"] = df["x_coordinate"].replace("I5413", "5413")

    # Convert x_coordinate column to int64
    df["x_coordinate"] = df["x_coordinate"].astype("int64")
    df = clean_control_sessions(df)
    df = clean_noncontrol_sessions(df)
    return df