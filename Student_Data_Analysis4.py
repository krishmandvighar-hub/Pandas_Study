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
#Fitering :-

#1.show students scoring more than 80 in maths
print(df[df["Maths"]>80])#filter
#OR
print(df.query("Maths>80"))#method of filtering

#2.show students scoring less than 70 in science.
print(df.query("Science<70"))

#3.show students whose percentage is above 75.
df["total"]=df[["Maths","Science","English"]].sum(axis=1)
df["per"]=df["total"]/3
print(df.query("per>75"))
#4.show student class A
print(df[df["Class"]=="10A"])
#5.show student class B and perc above 80
print(df[(df["Class"]=="10B") & (df["per"]>80)])
#6.students by total ascending .
print(df.sort_values(by="total"))
#7.students by total descending .
print(df.sort_values(by="total",ascending=False))
#8.display top 5 student
print(df.sort_values(by="total",ascending=False).head(5))
#9.display bottom 3 student
print(df.sort_values(by="total",ascending=False).tail(3))
