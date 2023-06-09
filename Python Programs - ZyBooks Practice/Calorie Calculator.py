# Jordan Allen

class FoodItem:
    def __init__(self, name='None', fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    # create the FoodItems class and insert the __init__ constructor to initialize the instance variables for name,
    # fat, carbs, and protein. Use the self parameter as the first instance to access and/or modify the current
    # variables.

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == '__main__':  # use this program
    defaultFoodItem = FoodItem()  # get values and create food item by using constructors parameters
    foodName = input()
    foodFat = float(input())
    foodCarbs = float(input())
    foodProtein = float(input())

    userFoodItem = FoodItem(foodName, foodFat, foodCarbs, foodProtein)
    numberServings = float(input())

    defaultFoodItem.print_info()  # call function to print empty result
    print('Number of calories for {:.2f} serving(s): {:.2f}\n'.format
          (numberServings, defaultFoodItem.get_calories(numberServings)))

    userFoodItem.print_info()  # call function to print input results
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format
          (numberServings, userFoodItem.get_calories(numberServings)))
