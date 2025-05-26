scores = [23, 45, 61, 75, 77]

myFile = open("Scores.txt", "w")
for i in range(len(scores)):
    myFile.write(str(scores[i]) + ",")
myFile.close()

scores_back = []
myFile = open("Scores.txt", "r")
scores_back = myFile.read().split(",")
myFile.close()