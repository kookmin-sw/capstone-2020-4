import csv

def writeCSV(sentence):
    f = open('C:\\Users\\01097\\PycharmProjects\\untitled\\csv\\write.csv', 'a', newline='')
    wr = csv.writer(f)
    wr.writerow(["1", sentence])


    f.close()

