from tempfile import NamedTemporaryFile
import shutil
import csv
from datetime import datetime

from cv2 import namedWindow


def UpdatePresence(name):

    filename = "data/attendance.csv"
    tempfile = NamedTemporaryFile(mode="w", delete=False)

    fields = ["Name", "Time"]

    with open(filename, "r") as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames=fields)
        writer = csv.DictWriter(tempfile, fieldnames=fields)
        for row in reader:
            if row["Name"] == str(name):
                now = datetime.now()
                dtString = now.strftime("%H:%M:%S")
                row["Name"], row["Time"] = name, dtString
            row = {"Name": row["Name"], "Time": row["Time"]}
            writer.writerow(row)

    shutil.move(tempfile.name, filename)
