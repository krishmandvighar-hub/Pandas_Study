import pandas as pd
data={
    "roll":[101,102,103,104,105,106,107,108,109,110],
    "name":["Amit","Neha","Ravi","Pooja","Karan","Sneha","Vikas","Anjali","Rahul","Priya"],
    "Class":["10A","10A","10B","10B","10A","10B","10A","10B","10A","10B"],
    "Maths":[94,85,65,92,65,82,35,75,87,89],
    "Science":[90,98,78,65,95,85,81,94,75,98],
    "English":[85,15,95,58,53,98,56,69,84,90]
}
df = pd.DataFrame(data)
#1.find student who scored above average in math.
avr_maths=df["Maths"].mean()
print(avr_maths)
print(df[df["Maths"]>avr_maths])
#2.Find students scoring highest in each subject.
print(df.nlargest(1,("Maths"))[["name","Maths"]])
print(df.nlargest(1,("Science"))[["name","Science"]])
print(df.nlargest(1,("English"))[["name","English"]])
#3.find the correlation between the maths and science marks
print(df["Maths"].corr(df["Science"]))
#4.show passed student and find pass percentage (assume pass marks=40)
passed=df[(df["Maths"]>=40)&(df["Science"]>=40)&(df["English"]>=40)]
print(passed)
pass_perc=len(passed)/len(df)*100
print(pass_perc)
#5.show failed students (less than 40 in any subject)df[]
failed=df[(df["Maths"]<40)|(df["Science"]<40)|(df["English"]<40)]
print(failed[["name","Maths","Science","English"]])
#Add bonus + 5
df["English"]=df["English"]+5
print(df)
#7.Replace marks below 35 with 35
df[["Maths","Science","English"]]=df[["Maths","Science","English"]].clip(lower=35)
print(df)

