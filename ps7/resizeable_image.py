import imagematrix

class ResizeableImage(imagematrix.ImageMatrix):



    #zadanie z MIT 6.006 zad. 7 - znajdz linie w obrazie o najmieszej energi
    def best_seam(self):

        #Funkcja zwraca najmiejsza wartosc w liscie wraz z jego indeksem
        # @start lista wartosci
        # @return: min_index, min_value - index najmiejszej wartosci w liscie i najmiejsza wartosc w liscie  
        def min_and_index(*values):
            import operator

            min_index, min_value = min(enumerate(list(values)), key=operator.itemgetter(1))
            return min_index, min_value


        height = self.height
        width = self.width

        #funckja obliczajaca energie
        energy_function = lambda x,y: self.energy(x,y)

        INFINITY = float("inf")

        # dp - tablica zawierajaca subsolucje 
        # zmemolizowane wartosci obliczen subsolucji dla danego punkty (linia o najmiejsze energi)
        # parent_table - pablica wskazujaca na poprzednika o najmiejszej wartosci
        # parent table: poprzedni rzad, podaj jaki punkt w stosunku do danego x,  0 - punkt x-1, 1 - punkt x, 2 punkt x+1
        dp = [[INFINITY for col in range(height)] for row in range(width)]
        parent_table = [[INFINITY for col in range(height)] for row in range(width)]



        #oblicz wartosci subproblemow (linia o najmiejsze energi) i umiesc je w tablicy
        #zapisz takze poprzednika, poprzedni punkt o najmiejsze wartosci energi linii
        for y in range(height):
            for x in range(width):
                if y == 0:
                    dp[x][y] = energy_function(x,y)
                    parent_table[x][y] = None 
                elif x == 0:
                    min_index, min_value = min_and_index( INFINITY, dp[x][y-1], dp[x+1][y-1] ) 
                    parent_table[x][y] = min_index
                    dp[x][y] = min_value + energy_function(x,y)
                elif x == width-1:
                    min_index, min_value = min_and_index(dp[x-1][y-1], dp[x][y-1] , INFINITY )
                    parent_table[x][y] = min_index
                    dp[x][y] = min_value + energy_function(x,y)
                else:    
                   min_index, min_value = min_and_index(dp[x-1][y-1], dp[x][y-1] ,dp[x+1][y-1] )
                   parent_table[x][y] = min_index
                   dp[x][y] = min_value + energy_function(x,y)


        #znajdz punkt na samymy dole ekrany, ktory konczy linie o najmiejszej energi
        # czyli wartosc w tablicy dp ostatni rzad o najmiejszej energi            
        min_value = dp[0][height-1]
        min_index = 0
        for x in range(width):
            if dp[x][height-1] < min_value:
                min_value = dp[x][height-1]
                min_index = x


        
        #zwroc linie o najmiejszej energi
        return_table = []        

        x = min_index
        for y in range(height-1, -1, -1):
            return_table.insert(0, (x,y))
            parent_index = parent_table[x][y]
            if parent_index == 0:
                x -= 1
            elif parent_index == 1:
                x==x
            elif parent_index == 2:
                x += 1

        return return_table



    def remove_best_seam(self):
        self.remove_seam(self.best_seam())        






