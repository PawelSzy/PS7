import operator


def best_seam():
    raise NotImplemented
    height = self.height
    width = self.width

    dp = [[float("inf") for row in range(width)] for col in range(height)]
    parent_table = [[float("inf") for row in range(width)] for col in range(height)]

    index_values = (dp[x-1,y-1], dp[x,y-1] ,dp[x+1,y-1] )

    #energy_function = lambda x,y: self.energy(x,y)



    for y in range(height):
        for x in range(width):
            if y == 0:
                dp[x][y] = energy_function(x,y)
                parent_table[x][y] = None 
            elif x == 0:
                min_index, min_value = min_and_index( float("inf"), dp[ x, y-1 ], dp[x+1, y-1 ] ) 
                parent_table[x][y] = min_index
                dp[x][y] = min_value + energy_function(x,y)
            elif x == width-1:
                min_index, min_value = min_and_index(dp[x-1,y-1], dp[x,y-1] , float("inf") )
                parent_table[x][y] = min_index
                dp[x][y] = min_value + energy_function(x,y)
            else:    
               min_index, min_value = min_and_index(dp[x-1,y-1], dp[x,y-1] ,dp[x+1,y-1] )
               parent_table[x][y] = min_index
               dp[x][y] = min_value + energy_function(x,y)


    min_value = dp[0][height-1]
    min_index = 0
    for x in range(width):
        if dp[x][height-1] < min_value:
            min_value = dp[x][height-1]
            min_index = x


    
    
    return_table = []        

    x = min_index
    for y in range(height-1, -1, -1):
        return_table.insert(0, (x,y))
        parent_index = index_values[x][y]
        if parent_index == 0:
            x -= 1
        elif parent_index == 1:
            x==x
        elif parent_index == 2:
            x += 1

    return return_table




    def min_and_index(*values):
        min_index, min_value = min(enumerate(list(values)), key=operator.itemgetter(1))
        return (min_index, min_value)



print "Start"
print best_seam()


