import csv

def writeCSV(sentence):
    f = open('write.csv', 'w', newline='')
    wr = csv.writer(f)
    wr.writerow([1, 'test', sentence])

    f.close()

writeCSV("abcd")