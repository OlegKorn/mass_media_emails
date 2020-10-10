import requests as req
import io, csv, re



'''
emails_checked = []

u = 'https://www.liveinternet.ru/rating/ru/media/today.tsv?page='

for i in range(1, 21):
    url = u + str(i)
    print('========================')
    print(url)
    print('========================')

    r = req.get(url)

    f = io.StringIO(r.text)
    rd = csv.reader(f, delimiter='\t', quotechar='"')

    for row in rd:
        if len(row) != 0:
            try:
                site = 'https://' + row[1]
                print(site)

                rq = req.get(site)
                soup = bs(rq.content, 'html.parser')
                
                email_re = re.compile(r'[-\w]+@\w+\.\w+')
                emails = email_re.findall(rq.text)

                if emails:
                    for e in emails:
                        if not e in emails_checked:
                            emails_checked.append(e)

            except: 
                pass

'''
file = 'G:/Desktop/test.txt'
f = open(file, 'w')
emails_checked = []

u = 'https://www.liveinternet.ru/rating/ru/media/today.tsv?page='

for i in range(1, 21):
    url = u + str(i)
    print('========================')
    print(url)
    print('========================')

    r = req.get(url)

    f = io.StringIO(r.text)
    rd = csv.reader(f, delimiter='\t', quotechar='"')

    for row in rd:
        if len(row) != 0:
            try:
                site = 'https://' + row[1]
                print(site)

                rq = req.get(site)
                                
                email_re = re.compile(r'[-\w]+@\w+\.\w+')
                emails = email_re.findall(rq.text)

                if emails:
                    print(emails)
                    for e in emails:                       
                        if not e in emails_checked:
                            emails_checked.append(e)
                            _ = e + ', '
                            print(_)
                            f.write(_)

            except: 
                pass

print(emails_checked)
