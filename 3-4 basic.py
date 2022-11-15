import csv
import manage.team_information as team_info

columns = ["성", "이름", "소속", "국적", "나이"]

with open("members.csv","w") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=columns)
    writer.writeheader()
    writer.writerows(team_info.members)


loaded_members =[]
with open("members.csv","r") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        loaded_members.append(row)

print(loaded_members)