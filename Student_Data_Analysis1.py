import pandas as pd
data={
    "roll":[100,102,103,104,105,106,107,108,109,110],
    "name":["Amit","Neha","Ravi","Pooja","Karan","Sneha","Vikas","Anjali","Rahul","Priya"],
    "Class":["10A","10A","10B","10B","10A","10B","10A","10B","10A","10B"],
    "Maths":[75,85,65,92,65,82,35,75,87,89],
    "Science":[52,65,78,94,38,64,81,94,75,98],
    "English":[85,65,49,58,53,98,75,69,84,90]
}
df=pd.DataFrame(data)
df["total"]=df[["Maths","Science","English"]].sum(axis=1)

#1.assign Rank Based on total marks.
df["Rank"]=df["total"].rank(ascending=False)
print(df)

#2.Find topper of class 10A.
topper_10A=df[df["Class"]=="10A"].sort_values(by="total",ascending=False).head(1)
print(topper_10A)

#3.Find topper of class 10B.
topper_10B=df[df["Class"]=="10B"].sort_values(by="total",ascending=False).head(1)
print(topper_10B)

#4.Find Overall topper.
topper_overall=df.sort_values(by="total",ascending=False).head(1)
print(topper_overall)

#5.find second highest scorer.
second_top=df.sort_values(by="total",ascending=False).iloc[1]
print(second_top)
#6.create grade column
df["per"]=df["total"]/3

print(df)
def grade(x):
    if x>=90:
        return "A"
    elif x>=80:
        return "B"
    elif x>=70:
        return "C"
    else :
        return "D"
df["Grade"]=df["per"].apply(grade)
print(df)
#7.count students in each grade.

print(df["Grade"].value_counts())
#8.count all student with grade A.
print(df[df["Grade"]=="A"])
#9.find classs wise total marks average:
print(df.groupby("Class")["total"].mean())
#10.find classs wise total maths average:
print(df.groupby("Class")["Maths"].mean()) 
#11.find maximum marks in each class
print(df.groupby("Class")["total"].max())
#12.find minimum marks in each class
print(df.groupby("Class")["total"].min())
#13.count number of students per grade in each class.
print(df.groupby(["Class", "Grade"]).size())
