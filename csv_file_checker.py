import csv,sys

def main():

    filename = 'some.csv'
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        try:
            for row in reader:
                print(row)
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

main()

