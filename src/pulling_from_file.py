import re
import os

#the output file uses quotes " to separate reviews
#some of the reviews have quotes within, which when put into the output file appear as ""
#to read back file in list, when splitting via ", this would cause problems, so "" was replaced with ∥
#∥ was not present as a character in the output file before

#basic structure of reading in is:
#read in line as list
#if the first character is a ", then start putting the review in a list
#the below regex can handle the
#the second line usually starts the review or has (for some reason) an integer
#if line is only an integer, skip it
#
pattern_first_line = r'(½|★{1,5}|★{1,4}½)\s+(Rewatched by|Added by|Watched by)([\s\S]*?)(\d{1,2}\s\w{3}\s\d{4})'
pattern_like_number = r'^(\d{1,3})\s+like[s]?'

master_review_list = []
single_review = []
temp_string = ""
with open(os.getcwd()+'\\output.txt','r', encoding='utf-8') as file:
    while True:
        line = file.readline()
        if not line:
            break
        elif line[0] == '\"':
            single_review = []
            if len(line) < 10:
                line = line.strip('\"').strip('\n')
                temp = file.readline()
                line = line + " " + temp.strip('\n')
            else:
                line = line.strip('\"').strip('\n')
            match = re.match(pattern_first_line, line)
            if match is None:
                print("Help")
            single_review.append(match.group(1))
            single_review.append(match.group(2))
            single_review.append(match.group(3))
            single_review.append(match.group(4))
            temp_string = ""
            continue
        elif len(line) <= 3 and line[len(line)-1] != '\"':
            continue
        elif line[len(line)-2] != '\"':
            if line[len(line)-1] == '\n':
                temp_string = temp_string + " " + line.strip('\n')
            else:
                temp_string = temp_string + line
        elif line[len(line)-2] == '\"':
            if re.match(pattern_like_number, line) is None:
                line = line.strip('\"').strip('\n')
                temp_string = temp_string + line
                single_review.append(temp_string)
                master_review_list.append(single_review)
            else:
                single_review.append(temp_string)
                master_review_list.append(single_review)

def printList(someList):
    for i in someList:
        print(i)

def getRatingCounts():
    halfStarCount = 0
    oneStarCount = 0
    oneAndHalfStarCount = 0
    twoStarCount = 0
    twoAndHalfStarCount = 0
    threeStarCount = 0
    threeAndHalfStarCount = 0
    fourStarCount = 0
    fourAndHalfStarCount = 0
    fiveStarCount = 0

    '''Get number of each star rating in list'''
    for review in master_review_list:
        if "★★★★★" in review:
            fiveStarCount += 1
        elif "★★★★½" in review:
            fourAndHalfStarCount += 1
        elif "★★★★" in review:
            fourStarCount += 1
        elif "★★★½" in review:
            threeAndHalfStarCount += 1
        elif "★★★" in review:
            threeStarCount += 1
        elif "★★½" in review:
            twoAndHalfStarCount += 1
        elif "★★" in review:
            twoStarCount += 1
        elif "★½" in review:
            oneAndHalfStarCount += 1
        elif "★" in review:
            oneStarCount += 1
        else:
            halfStarCount += 1

    print ("5-Star Reviews:   " + str(fiveStarCount))
    print ("4.5-Star Reviews: " + str(fourAndHalfStarCount))
    print ("4-Star Reviews:   " + str(fourStarCount))
    print ("3.5-Star Reviews: " + str(threeAndHalfStarCount))
    print ("3-Star Reviews:   " + str(threeStarCount))
    print ("2.5-Star Reviews: " + str(twoAndHalfStarCount))
    print ("2-Star Reviews:   " + str(twoStarCount))
    print ("1.5-Star Reviews: " + str(oneAndHalfStarCount))
    print ("1-Star Reviews:   " + str(oneStarCount))
    print ("0.5-Star Reviews: " + str(halfStarCount))
    #END getRatingCounts

'''def ratingToNum():
    newList = master_review_list
    tempNum = 0
    for review in newList:
        if "★★★★★" in review:
            tempNum = review.find("★")
            review = review[:tempNum] + review[tempNum+5:]
        elif "★★★★½" in review:
            tempNum = review.find("★")
            review = review[:tempNum] + review[tempNum+5:]
        elif "★★★★" in review:
            tempNum = review.find("★")
            review = review[:tempNum] + review[tempNum+4:]
        elif "★★★½" in review:
            tempNum = review.find("★")
            review = review[:tempNum] + review[tempNum+4:]
        elif "★★★" in review:
            tempNum = review.find("★")
            review = review[:tempNum] + review[tempNum+3:]
        elif "★★½" in review:
            tempNum = review.find("★")
            review = review[:tempNum] + review[tempNum+ 3:]
        elif "★★" in review:
            tempNum = review.find("★")
            review = review[:tempNum] + review[tempNum+2:]
        elif "★½" in review:
            tempNum = review.find("★")
            review = review[:tempNum] + review[tempNum+2:]
        elif "★" in review:
            tempNum = review.find("★")
            review = review[:tempNum] + review[tempNum+1:]
        else:
            tempNum = review.find("½")
            review = review[:tempNum] + review[tempNum+1:]
    return newList'''


#newList = ratingToNum()
#getRatingCounts()

printList(master_review_list)
#printList(newList)



