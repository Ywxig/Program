class Drow():

    def Feet(Long, Case1, Case2):
        d = Long
        i = 0
        l = []
        while i != Long:
            i = i + 1
            d = d - 1
            w = Case2 * d
            case = "Writeln('" + Case1 * i + w + "');"
            MediumLong = Long / 3
            FoodCase1 = Case1 * int(MediumLong)
            I = i - int(MediumLong) + 1
            FoodCase2 = Case2 * I
            l.append(case)

        rez = '\n'.join(l)
        return rez
            
    def Spruce(Long, Case1, Case2):
        d = Long
        i = 0
        l = []
        while i != Long:
            i = i + 1
            d = d - 1
            w = Case2 * d
            case = "Writeln('" + w + Case1 * i + Case1 * i + w + "');"
            MediumLong = Long / 3
            FoodCase1 = Case1 * int(MediumLong)
            I = i - int(MediumLong) + 1
            FoodCase2 = Case2 * I
            stap = "Writeln('" + FoodCase2 + FoodCase1 + FoodCase1 + FoodCase2 + "');"
            l.append(case)
            
        i = 0
        LongFood = Long % 3
        if LongFood == 0:
            LongFood = 2
        while i != LongFood:
            i = i + 1
            l.append(stap)

        rez = '\n'.join(l)
        return rez
            
'''
Drow.Spruce(50, '-', '_')

Это пример как нужно приминять данную функцию!
'''
Drow.Spruce(15, '#', ' ')
