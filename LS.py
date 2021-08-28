"""

A basic linear classifer example that uses the pyoplot library to help  us visualize the data classification.


"""

import numpy as np
import matplotlib.pyplot as plt

class points:
    def __init__(self, arr=None, x=None, y=None, category = None):
        self.x = []
        self.y = []
        self.category = category
        if (arr == None and x != None and y != None):
            self.x.append(x)
            self.y.append(y)
        elif (arr == None and x == None and y == None):
            return
        else:
            for pair in arr:
                self.x.append(pair[0])
                self.y.append(pair[1])

    def add_cordinate(self, x=None, y=None, arr=None):
        if (x != None and y != None):
            self.x.append(x)
            self.y.append(y)
        elif (arr != None):
            print("printing arr" + format(arr))
            for pair in arr:
                self.x.append(pair[0])
                self.y.append(pair[1])

    def isEmpty(self):
      if(len(self.x) == 0):
        return True
      else:
        return False

    def print_pairs(self):
        for el in range(0, len(self.x)):
            print("x= " + str(self.x[el]) + " y = " + str(self.y[el]))


def calculate_errors(c1, c2, threshold):
    #true positives and true negatives
    tp = 0
    tn = 0
    fp = 0
    fn = 0

    for ind in range (0, len(c1.x)):
      #get points from both groups
      x_1 = c1.x[ind]
      y_1 = c1.y[ind]
      

      x_2 = c2.x[ind]
      y_2 = c2.y[ind]

      print("x_1 = "+str(x_1))
      print("threshold x = "+str(threshold.x[0]))

      #test against the threshold

      if(x_1 > threshold.x[0] and y_1 > threshold.y[0]):
        category_1 = "C1"
      else:
        category_1 = "C2"
        
      if(x_2 > threshold.x[0] and y_2 > threshold.y[0]):
        category_2 = "C1"
      else:
        category_2 = "C2"

      if(category_1 == "C1"):
        tp += 1
      else:
        fp += 1
      
      if(category_2 == "C2"):
        tn += 1
      else:
        fn += 1
        
    result = 100 * ( (float (tn+ tp) ) / (float (tn+tp+fp+fn)) )
    print("Accuracy of threshold is... " + str(result))

#THRESHOLD setting function / General x and y input getting function
def get_xy(argument,msg = "Enter the X and Y Value"):
  if(argument == "XY" or argument == "xy"):
    print(msg)
    x = get_xy("X")
    y = get_xy("Y")
    return x, y
    
  if(argument == "X" or argument == "x"):
    x_in = input("""Enter the X value :\n""")
    try:
      x_in = float(x_in)
    except:
      print("error!")
    if(isinstance(x_in, int) or isinstance(x_in,float)):
      return float(x_in)
    else:
      return get_xy("X")
      
  if(argument == "Y" or argument == "y"):
    y_in = input("""Enter the Y value : \n""")
    try:
      y_in = float(y_in)
    except:
      print("error!")
    if(isinstance(y_in, int) or isinstance(y_in,float)):
      return float(y_in)
    else:
      return get_xy("Y")


def display_graph(group1, group2, threshold, container1, container2):
  plt.xlim([0, 5])
  plt.ylim([0, 5])

  plt.plot(group1.x, group1.y, "ro", label = group1.category)
  plt.plot(group2.x, group2.y, "bv", label = group2.category)

  if(container1.isEmpty() == False):
    plt.plot(container1.x, container1.y, "r*", label = container1.category)
  if(container2.isEmpty() == False):
    plt.plot(container2.x, container2.y, "b*", label = container2.category)

  plt.plot(threshold.x[0], threshold.y[0], "g*", label = "threshold")
  plt.xlabel("X")
  plt.ylabel("Y")
  plt.legend()
  plt.show()

#This function takes a points and categorizes them according to the category passed.
def classify (p, threshold, category1, category2):
  categorized_group1 = points()
  categorized_group1.category = category1
  categorized_group2 = points()
  categorized_group2.category = category2
  for i in range(0,len(p.x)):
    if(p.x[i] > threshold.x[0] and p.y[i] > threshold.y[0]):
      categorized_group1.add_cordinate(x = p.x[i], y = p.y[i])
    else:
      categorized_group2.add_cordinate(x = p.x[i], y = p.y[i])
  
  return categorized_group1, categorized_group2


def main():

  #Our C1 and C2 coordinate arrays
  C1_test = points({(2, 2), (3, 2), (2, 3)}, category = "C1")
  C2_test = points({(1, 2), (1, 1), (2, 1)} , category = "C2")
  
  #set threshold
  xth = yth = 0
  threshold = points(x = xth, y = yth)
  exit = False
  user_data_points = points()

  while exit == False:


    main_menu = ""
    main_menu += "MAIN MENU \n"
    main_menu += """Press "d" to display graph (Part a) \n"""
    main_menu += """Press "s" to set the threshold and test it's accuracy (Part b and c) \n"""
    main_menu += """Press "n" to add data points (Part d) \n"""   
    main_menu += """Press "x" to exit the program \n \n \n"""   

    main_input = input(main_menu)

    if(main_input == "d"):
      if(not(user_data_points.isEmpty())):
        print("Array is not empty")
        C1_training , C2_training = classify(user_data_points, threshold, "C1 Detected", "C2 Detected")
        display_graph(C1_test, C2_test, threshold, C1_training , C2_training )
      else:
        C1_training=points()
        C2_training=points()
        display_graph(C1_test, C2_test, threshold, C1_training , C2_training )

    if(main_input == "s"):
      in_x, in_y = get_xy("XY", "SET THRESHOLD")
      threshold.x[0] = in_x
      threshold.y[0] = in_y
      calculate_errors(C1_test, C2_test, threshold)

    if(main_input == "n"):
      while True:
        in_x, in_y = get_xy( "XY", "Enter Data point")
        user_data_points.add_cordinate(x = in_x, y = in_y)
        inn = input(""" To enter another point press "y" \n Else press any other button to exit this menu """)

        if(inn != "y"):
          break;

    if(main_input == "x"):
      break;



if __name__== "__main__":
  main()
