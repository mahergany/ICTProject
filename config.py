import pandas as pd

databaseName = "db.sqlite"
tableName = "students"
directoryName = "known_encodings"

timeTable = {
    "0900": ["MATH161", None, "CS110lab", "CS110", "CS110"],
    "1000": ["MATH111", None, "CS110lab", "CS110", "HU107"],
    "1100": ["HU108", "MATH111", "CS110lab", "MATH111", "CS100"],
    "1200": ["HU108", "CS100", "MATH161", "MATH111", None],
    "1300": [None, None, None, None, None],
    "1400": [None, "CS100lab", "HU108", None, None],
    "1500": [None, "CS100lab", None, "HU107", None],
    "1600": [None, "CS100lab", None, None, None]
}

timeTable = pd.DataFrame(
    timeTable, index=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])


# print(set([item for item in timeTable.items()]))
courses = set()
[[courses.add(i) for i in item if i is not None] for item in timeTable.values]
