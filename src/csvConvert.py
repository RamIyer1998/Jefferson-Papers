import csv
import os
import sys
import dateutil.parser as dparser
import re
from datetime import datetime



def main():
    with open('jeff_data.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Filename', 'From', 'To', 'Date', 'Randolph/LoC'])
        f.close()
    
    write("Jefferson Papers/From_Jefferson")
    write("Jefferson Papers/To_Jefferson")
            
        

def write(directory):
    files = os.listdir(directory)
    for file in files:
        source = "LoC"
        new_file=file
        if file[0:2] == "R.":
            source = "Randolph"
            new_file = file[3: ]
        x = re.search("(jan(uary)?|feb(ruary)?|mar(ch)?|apr(il)?|may|jun(e)?|jul(y)?|aug(ust)?|sep(tember)?|oct(ober)?|nov(ember)?|dec(ember)?)(.)?\s+\d{1,2},(\s+\d{4}|\d{4})", file)
        if x is not None:
            time = file[x.start():x.end()]
            dt_object = dparser.parse(time).strftime('%Y-%m-%d')

            if directory == "Jefferson Papers/From_Jefferson":
                start = file.find("to")+3
                end = x.start()-2

                recipient = file[start: end]
                with open('jeff_data.csv', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([file, "thomas jefferson", recipient, dt_object, source])
                    f.close()

            else:
                if new_file == "george washington to madame de lafayette, march 15, 1793.txt":
                    with open('jeff_data.csv', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([file, "george washington", "madame de lafayette", "1797-11-XX", source])
                        f.close()
                    continue
            
                elif new_file == "henry dearborn to state governors, january 17, 1809, circular letter.txt":
                    with open('jeff_data.csv', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([file, "henry dearborn", "state governors", "1797-11-XX", source])
                        f.close()
                    continue

                elif new_file == "senate, february 1, 1791, resolution on redemption of american citizens held by algiers.txt":
                    with open('jeff_data.csv', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([file, "senate", "", "1797-11-XX", source])
                        f.close()
                    continue
            
                elif new_file == "cabinet to george washington, august 5, 1793, report.txt":
                    with open('jeff_data.csv', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([file, "george washington's cabinet", "george washington", "1797-11-XX", source])
                        f.close()
                    continue

                elif new_file == "from the president, april 4, 1791.txt":
                    with open('jeff_data.csv', 'a') as f:
                        writer = csv.writer(f)
                        writer.writerow([file, "george washington", "", "1797-11-XX", source])
                        f.close()
                    continue

                composer = new_file[0:file.find("to")-1]

                with open('jeff_data.csv', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([file, composer, "thomas jefferson", dt_object, source])
                    f.close()



        else:
            if file == "thomas jefferson to uriah tracy, january 1806.txt" or new_file == "thomas jefferson to uriah tracy, january 1806.txt":
                with open('jeff_data.csv', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([file, "thomas jefferson", "uriah tracy", "1806-01-XX", source])
                    f.close()
                continue

            elif file == "memoir.txt" or new_file == "memoir.txt":
                with open('jeff_data.csv', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([file, "thomas jefferson", "", "XXXX-XX-XX", source])
                    f.close()
                continue

            elif file == "to colonel mathews, october, 1779.txt" or new_file == "to colonel mathews, october, 1779.txt":
                with open('jeff_data.csv', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([file, "thomas jefferson", "colonel mathews", "1779-10-XX", source])
                    f.close()
                continue

            elif file == "to dr. gem 1792.txt" or new_file == "to dr. gem 1792.txt":
                with open('jeff_data.csv', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([file, "thomas jefferson", "dr. gem", "1792-XX-XX", source])
                    f.close()
                continue

            elif file == "memoranda taken on a journey from paris in 1787.txt" or new_file == "memoranda taken on a journey from paris in 1787.txt":
                with open('jeff_data.csv', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([file, "thomas jefferson", "", "1787-XX-XX", source])
                    f.close()
                continue

            elif file == "to economie politique et diplomatique.txt" or new_file == "to economie politique et diplomatique.txt": 
                with open('jeff_data.csv', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([file, "thomas jefferson", "economie politique et diplomatique", "XXXX-XX-XX", source])
                    f.close()
                continue

            elif file == "thomas jefferson, march 1809, statement on appointments.txt" or new_file == "thomas jefferson, march 1809, statement on appointments.txt":
                with open('jeff_data.csv', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([file, "thomas jefferson", "", "1809-03-XX", source])
                    f.close()
                continue

            elif file == "james monroe to thomas jefferson, november 1797.txt" or new_file == "james monroe to thomas jefferson, november 1797.txt":
                with open('jeff_data.csv', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([file, "james monroe", "thomas jefferson", "1797-11-XX", source])
                    f.close()
                continue

            elif file == ".DS_Store":
                continue

            
            
            print(file)

    





if __name__ == '__main__':
    main()