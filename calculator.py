#!/usr/bin/env python3
import sys
import csv 

class Args(object):

        def __init__(self):
                args = sys.argv[1:]
                self.c=args[args.index('-c')+1]
                self.d=args[args.index('-d')+1]
                self.o=args[args.index('-o')+1]

args = Args()

class Config(object):

        def __init__(self):
               self.config = self._read_config()
        def _read_config(self):
                config = {'s': 0}
                with open(args.c) as f:
                        for i in f.readlines():
                                l = i.split('=')
                                m, n = l[0].strip(), float(l[1].strip())
                                if n > 1:
                                        config[m] = n
                                else:
                                        config['s'] += n
                return config

config = Config().config

class UserData(object):

        def __init__(self):
                with open(args.d) as f:
                        data = list(csv.reader(f))
                self.userdata = data

userdata = UserData().userdata

def calc(id, salary):
        salary = int(salary)
        shebao = salary * config.get('s')
        if salary < config.get('JiShuL'):
                shebao = config.get('JiShuL') * config.get('s')
        if salary > config.get('JiShuH'):
                shebao = config.get('JiShuH') * config.get('s')
        nashuie = salary - shebao - 3500
        if nashuie<=0:
                shuie = 0
        elif nashuie<1500:
                shuie = nashuie * 0.03
        elif nashuie<4500:
                shuie = nashuie * 0.1-105
        elif nashuie<9000:
                shuie = nashuie * 0.2-555
        elif nashuie<35000:
                shuie = nashuie * 0.25-1005
        elif nashuie<55000:
                shuie = nashuie * 0.3-2755
        elif nashuie<80000:
                shuie = nashuie * 0.35-5505
        else:
                shuie = nashuie * 0.45-13505
        return [id, salary, format(shebao, '.2f'), format(shuie, '.2f'), format(salary-shebao-shuie, '.2f')]

with open('gongzi.csv','w') as f:
        for i in userdata:
                salary = int(i[1])
                csv.writer(f).writerow(calc(i[0], salary))
