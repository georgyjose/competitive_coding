path = "input_for_largest_product_in_a_grid.txt"

b = []

with open(path,"r") as a:
    b = [list(map(int,i.split())) for i in a]

