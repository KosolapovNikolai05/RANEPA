import pandas as ps
import matplotlib.pyplot as plt

def solve1Task():
    allData = ps.read_excel('projectTable.xlsx')
    provinces = allData['points']
    hist = provinces.hist(grid=False, color="pink", bins=120, ec="red")
    plt.title("Гистограмма: Баллы")
    plt.show()

def solve2Task():
    allData = ps.read_excel('projectTable.xlsx')
    provinces = allData['price']
    hist = provinces.hist(grid=False, color="#8ac1ff", bins=120, ec="navy", )
    plt.title("Гистограмма: Цены")
    plt.xlim(0, 300)
    plt.show()

def solve3Task():
    allData = ps.read_excel('projectTable.xlsx')
    provinces = allData['variety']
    data = dict()
    vars = list()

    for x in provinces:
        if (x not in vars):
            vars.append(x)

    numbers = list()
    provincesList = list(provinces)
    for q in vars:
        numbers.append(provincesList.count(q))
        data.update({q: provincesList.count(q)})

    dataF = dict(sorted(data.items(), key=lambda t: t[1], reverse=True))
    k = list(dataF.keys())
    v = list(dataF.values())
    for q in range(0, len(numbers) - 6):
        plt.bar(k[q:q + 4], v[q:q + 4])
        plt.show()
        q = q + 6

def solve4Task():
    allData = ps.read_excel('projectTable.xlsx')
    provinces = allData['province']
    data = dict()
    vars = list()

    for x in provinces:
        if (x not in vars):
            vars.append(x)

    numbers = list()
    provincesList = list(provinces)
    for q in vars:
        numbers.append(provincesList.count(q))
        data.update({q: provincesList.count(q)})

    dataF = dict(sorted(data.items(), key=lambda t: t[1], reverse=True))
    k = list(dataF.keys())
    v = list(dataF.values())
    for q in range(0, len(numbers) - 6):
        plt.bar(k[q:q + 4], v[q:q + 4])
        plt.show()
        q = q + 6

