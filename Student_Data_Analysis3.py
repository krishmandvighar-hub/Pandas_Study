import pandas as pd
data={
    "roll":[101,102,103,104,105,106,107,108,109,110],
    "name":["Amit","Neha","Ravi","Pooja","Karan","Sneha","Vikas","Anjali","Rahul","Priya"],
    "Class":["10A","10A","10B","10B","10A","10B","10A","10B","10A","10B"],
    "Maths":[94,85,65,92,65,82,35,75,87,89],
    "Science":[90,98,78,65,95,85,81,94,75,98],
    "English":[85,65,95,58,53,98,56,69,84,90]
}
df = pd.DataFrame(data)
#1.create a new column total marks.
df["total"]=df[["Maths","Science","English"]].sum(axis=1)
print(df)
#2.create a new column of per
df["per"]=df["total"]/3
print(df)
#3.Find the highest total marks.
print("highest marks: ",df["total"].max())
print(df[df["total"]==df["total"].max()])
#4.Find the lowest total marks.
print("lowest marks: ",df["total"].min())
#5.find average marks of maths
print("average marks of maths : ",df["Maths"].mean())
#6.find average marks of all subjects
print(df[["Maths","Science","English"]].mean())
#7.count total student in each class
print(df.groupby("Class").size())

# OR
print(df["Class"].value_counts())

#8.find class wise average percentage
print(df.groupby("Class")["per"].mean())
print("student score verey well marks in science")
