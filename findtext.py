import os, sys, urllib.request
from progress.bar import IncrementalBar
term_size = os.get_terminal_size()
def text_fsearch(path,pattern):
    frcount=sum(len(files) for _, _, files in os.walk(path))
    print(f'''\nПошук в такій кількості файлів: {frcount}\n ''')
    files_s=[]
    fcount=0
    fscount=0
    fncount=0
    fstcount=0
    filebool=False
    filesscount=0
    bar = IncrementalBar('Пошук у файлах: ', max = frcount)
    term_size = os.get_terminal_size()
    print('=' * term_size.columns)
    for root, dirs, files in os.walk(path):
        for file in files:
                with open(os.path.join(root, file), 'rb+') as in_put:
                    filebool=False
                    filesscount=0
                    for row, line in enumerate(in_put):
                        if pattern in str(line):
                            fstcount+=1
                            filesscount+=1
                            if(filebool):
                                print(f'''\nПошуковий текст: {pattern}\nЗнайдений текст: {line.decode()}\nНомер стрічки: {row + 1}''')
                            else:
                                print(f'''\nФайл: {os.path.join(root, file)}\nПошуковий текст: {pattern}\nЗнайдений текст: {line.decode()}\nНомер стрічки: {row + 1}''')
                            filebool=True
                            # print(f'''\nФайл: {os.path.join(root, file)}\nПошуковий текст: {pattern}\nЗнайдений текст: {line.decode()}\nНомер стрічки: {row + 1}''')
                            
                            term_size = os.get_terminal_size()
                    if(filesscount):
                            print(f'''\nКількість знахідок у файлі: {filesscount}''')  
                    if(filebool):
                        fcount+=1
                        print('=' * term_size.columns)
                    fscount+=1
                    bar.next()
    print(f'''\nКількість знайдених файлів: {fcount}\nКількість знахідок: {fstcount}''')
    print(f'''Кількість файлів у яких не знайдено: {fscount-fcount}''')
    print(f'''Загальна кількість файлів: {fscount}\n''')
    print('=' * term_size.columns)
    bar.finish()

if len(sys.argv) > 2:
    print('=' * term_size.columns)
    print(f'Вказано шлях:\n{sys.argv[1]}\nВказано текст:\n{sys.argv[2]}')
    print('=' * term_size.columns)
    text_fsearch(sys.argv[1],sys.argv[2])

while True:
    folder=input('Вкажіть шлях де шукати:\n')
    if(folder=="exit"):
        exit()
    textfind=input('текст який знайти:\n')
    print('=' * term_size.columns)
    print('Вказано шлях:\n'+folder+'\nВказано текст:\n'+textfind)
    print('=' * term_size.columns)
    text_fsearch(folder,textfind)