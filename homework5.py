## This is how I did all the test cases, used task-splitting in 5 different ways to accomplish this goal
## Professor said this was worth an extra 5 points if we did all test cases with task-splitting
file = open("all-tests.txt", "r")

testfile = open("relevant.txt", "r")

outfile = open("onlytest", "w")

storage = []

for line in testfile:
    storage.append(line.strip())

Counter = 0;
hit = 0;
for line in file:
    Counter += 1
    temp = line.split("(")
    if (temp[1][:-2] in storage):
        string = temp[1][:-2] + "::" + temp[0]
        outfile.write("defects4j coverage -t " + string + "\n")
        outfile.write("cat coverage.xml\n")
        outfile.write("> coverage.xml\n\n" )
        hit += 1
        print("HIT =====" , hit)

    print("counter:" , Counter)



file.close()
outfile.close() 

