import csv

def writeCSV(sentence):
    #f = open('C:\\Users\\01097\\PycharmProjects\\untitled\\csv\\write.csv', 'a', newline='')
    f = open('/home/ubuntu/capstone-2020-4/src/textData/write.csv', 'a', newline='')
    wr = csv.writer(f)
    wr.writerow([sentence])


    f.close()

def writeTXT(sentence):
    #f = open('C:\\Users\\01097\\PycharmProjects\\untitled\\csv\\write.txt', 'a')
    f = open('/home/ubuntu/capstone-2020-4/src/textData/write.txt', 'a')
    data = sentence + "\n"
    f.write(data)

    f.close()

def printTime(t):
    f = open('C:\\Users\\01097\\PycharmProjects\\untitled\\csv\\write.csv', 'a', newline='')
    wr = csv.writer(f)
    wr.writerow([str(t) + ":00 ~ " + str(t+5) + ":00"])


    f.close()


printTime(3)
writeCSV("33")