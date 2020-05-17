import csv

def writeCSV(sentence):
    f = open('C:\\Users\\01097\\PycharmProjects\\untitled\\csv\\write.csv', 'a', newline='')
    #f = open('/home/ubuntu/capstone-2020-4/src/csv/write.csv', 'a', newline='')
    wr = csv.writer(f)
    wr.writerow([sentence])


    f.close()

def writeTXT(sentence, FILE_PATH):
    f = open(FILE_PATH, 'a', encoding='utf-8')
    #f = open('/home/ubuntu/capstone-2020-4/src/csv/write.csv', 'a', encoding = 'utf-8')
    data = sentence + "\n"
    f.write(data)

    f.close()

def stampTime(FILE_PATH, word, start, start_nano, end, end_nano, cnt):
    f = open(FILE_PATH, 'a', encoding='utf-8')
    # f = open('/home/ubuntu/capstone-2020-4/src/csv/write.csv', 'a', encoding = 'utf-8')
    f.write(str(word) + "/" + str(round(start*1000 + (start_nano/1000000)) + 50000*cnt) + "/" + str(round(end*1000 + (end_nano/1000000)) + 50000*cnt)) # ms로 단위 변환
    f.write("\n")

    f.close()


def printTime(t):
    f = open('C:\\Users\\01097\\PycharmProjects\\untitled\\csv\\write.csv', 'a', newline='')
    wr = csv.writer(f)
    wr.writerow([str(t) + ":00 ~ " + str(t+5) + ":00"])


    f.close()


#printTime(3)
#writeCSV("33")