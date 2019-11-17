
import csv

this_student_id=""
this_class=""
this_vote=""
jonesvote=0
dravenvote=0
smithvote=0

file_to_open="class_election.csv"


with open(file_to_open, "r") as this_csv_file:
    this_csv_reader = csv.reader(this_csv_file, delimiter=',')
    header = next(this_csv_reader)
    print(header)


    for line in this_csv_reader:
        

        this_student_id=line[0]
        this_vote=line[1]
       
        if this_vote=="Smith":
            smithvote=smithvote+1
        if this_vote=="Jones":
            jonesvote=jonesvote+1
        if this_vote=="Draven":
            dravenvote=dravenvote+1

print ("Draven: " + str(dravenvote))
print ("Smith: " + str(smithvote))
print ("Jones: " + str(jonesvote)) 

if dravenvote>smithvote and dravenvote>jonesvote:
        print("Draven Wins!")
if smithvote>dravenvote and smithvote>jonesvote:
        print("Smith Wins!")
if jonesvote>dravenvote and jonesvote>smithvote:
        print("Jones Wins!")
 

        
           
        