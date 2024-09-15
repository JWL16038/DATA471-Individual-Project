from statistics import mean


def get_mean_sessions(df):
    control_subjects = df[(df.control == 'Y')]['subject'].unique()
    noncontrol_subjects = df[(df.control == 'N')]['subject'].unique()
    control_sessions = []
    noncontrol_sessions = []
    for c in control_subjects:
        sessions = len(df[(df.control == 'Y') & (df.subject == c)]['session'].unique())
        control_sessions.append(sessions)
    for c in noncontrol_subjects:
        sessions = len(df[(df.control == 'N') & (df.subject == c)]['session'].unique())
        noncontrol_sessions.append(sessions)
    # print(control_sessions, noncontrol_sessions)
    return mean(control_sessions), mean(noncontrol_sessions)
