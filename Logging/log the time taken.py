
from datetime import datetime 

dateFrom='2022-10-20 16:07:43'
dateTo='2022-10-20 16:08:44'
keywordForTimeTaken='Total time taken : '
keyword='END IsPredefinedMembersExists'
timeTaken=''
number = 0

f = open("after.txt","r",encoding="utf-8")
w = open("script.txt", "w", encoding="utf-8")

for line in f:
    if (line.__contains__(keyword)):
        number=number+1
        words = line.split('|')
        
        datetimevalue = words[0][words[0].find('[')+1 : words[0].find('.')]

 
        datetimevalue_obj = datetime.strptime(datetimevalue, '%Y-%m-%d %H:%M:%S')
        dateFrom_obj = datetime.strptime(dateFrom, '%Y-%m-%d %H:%M:%S')
        dateTo_obj = datetime.strptime(dateTo, '%Y-%m-%d %H:%M:%S')

        if(datetimevalue_obj >= dateFrom_obj and datetimevalue_obj < dateTo_obj):
            for x in words:
                if(x.__contains__(keywordForTimeTaken)):
                    timeTaken = x.replace(keywordForTimeTaken,'').strip().replace("00:00:","")
            
            string = str(number) + "\t" + datetimevalue + "\t" + words[0].replace(words[0][words[0].find('[')+1 : words[0].find(']')], "").replace('[]','').strip() + "\t" + keyword + "\t" + timeTaken + "\n"
            w.write(string)
    # line = line.replace("\n", "")
    # string = "\""+line+"\", " 
f.close()
w.close()


