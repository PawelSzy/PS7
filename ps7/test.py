import resizeable_image
import unittest


print "test"

class EnergyTable:

    def __init__(self, height, width, energy_function):
         # instance variable unique to each instance
        self.table = [[float("inf") for col in range(height)] for row in range(width)]
        self.height = height   
        self.width = width
        self.energy_function = energy_function 


    def energy(self, x, y):
        return self.energy_function(x,y) 

    #zwraca poprzednika  najmiejsze energi
    #poprzednik - punkt z poprzedniej linijki oddalono o nie mniej niz     
    def subsolution(self, i,j):

        solution = ( self.solution(i, j-1), (i, j-1) )
        sol2 = ( self.solution(i-1, j-1), (i-1, j-1) )
        if sol2[0] < solution[0]:
            solution = sol2
        sol3 = ( self.solution(i+1, j-1) + self.energy(i, j), (i+1, j-1) )
        if sol3[0] < solution[0]:
            solution = sol3

        return solution

    def solution(self, i,j):

        if i < 0 or j < 0:
            return float("inf")

        if i == 0:
            return self.energy(i,j)


        if i >= self.width or j >= self.height :
            return float("inf")        

        if self.table[i][j] != float("inf") :
            return self.table[i][j]
        else:
            solution = min( self.solution(i, j-1), self.solution(i-1, j-1), self.solution(i+1, j-1) + self.energy(i, j) )
            self.table[i][j] = solution
            return solution

    def min_solution(self):
        #znajdz solution o najnizszej enerdze, min_dp w ostatnim rzedzie
        solution = (self.solution(x, height-1), (x, height-1) ) 
        for x in range(self.width):
            sol2 = (self.solution(x, height-1), (x, height-1)  )
            if sol2[0] < solution[0]:
                solution = sol2    


        #obliczylem min_dp, teraz musze podac liste np:. [(5,0), (5,1), (6,2)....... (min_dp) ]
        x = solution[1][0]       
        y = height
        min_energy_beam = [ solution[1] ]       
        while y >= 0:
            subsolution = self.subsolution(x, y)
            min_energy_beam.append( subsolution[1] )
            x = subsolution[1][1]
            y = subsolution[1][1]

        return solution[::-1]


# def  energy_function(x,y):
# 		table = [ [2, 1, 3], [5, 1, 6], [8,9, 1]]
# 		return table[x][y]


# energy_table = EnergyTable(3,3, energy_function)

# print energy_table.energy(2,1)

# unittest.TestCase.assertEqual( energy_table.energy(2,1), 9 )


class EnergyClassTest(unittest.TestCase):
		
	def test_energy_function(self):

		def  energy_function(x,y):
			table = [ [2, 1, 3], [5, 1, 6], [8,9, 1]]
			return table[x][y]

		energy_table = EnergyTable(3,3, energy_function)

		super(EnergyClassTest, self).assertEqual(energy_table.energy(2,1), 9)

		print energy_table.table
		print "***************"
		print energy_table.solution(1,1)
		print energy_table.solution(2,1)
		#self.assertEqual( energy_table.energy(2,1), 9 )

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()