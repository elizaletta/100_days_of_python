import math
def paint_calc(width, height, cover):
    number_of_cans = math.ceil((width * height) / cover)
    print(f"You will need {number_of_cans} cans of paint.")

paint_calc(width=5, height=7, cover=5)