from keras.datasets import mnist 
import matplotlib.pyplot as plt
import random
import numpy as np

def filter_original_sets(images,labels):
  boo_ind = []
  el_is = 0
  for el in labels:
    if(el == 0 or el == 1):
      boo_ind.append(True)
    else:
      boo_ind.append(False)

  filtered_labels_arr = labels[boo_ind]
  filtered_img_arr = images[boo_ind,:,:]
  return filtered_img_arr, filtered_labels_arr

def sub_plot_fun(images, labels):
  plt.figure()
  for i in range(1,11):
    digit = i - 1
    #create an array where only images that match labels = digits are kept.
    filtered_indexes = images[labels == digit,:,:]
    #create an array where only labels that match labels = digit are kept.
    filtered_labels = labels[labels == digit]
    plt.subplot(2,5,i)
    r = random.randint(0, filtered_indexes.shape[0])
    specific_img = filtered_indexes[r,:,:]
    #Select a single label index = random number from 0 to the total number of elements in our filtered array.
    specific_label = filtered_labels[r]
    plt.imshow(specific_img,cmap='gray')
    plt.title('Label: ' + str(specific_label))
    print(filtered_indexes.shape)
  plt.show()

def avg_data(npp):
  avg_arr_test = []
  count = 0
  for e in npp:
    sum = 0
    for i in range(0,3):
      for j in range(0,3):
        sum +=e[i][j]
    avg_arr_test.append(((sum)/9))
  return avg_arr_test

def calculate_accuracy(threshold, values, labels_arr):
  tp = 0
  tn = 0
  fp = 0
  fn = 0
  count = 0
  for el in values:
    if(el > threshold):
      if(labels_arr[count] == 1):
        tp = tp+1
      else:
        fp = fp+1
    else:
      if(labels_arr[count] == 0):
        tn = tn+1
      else:
        fn = fn+1
    count = count+1
  t = (tp + tn)/(tp+tn+fp+fn)
  print("The accuracy of the threshold is : " + str(t))

def main():
  #returns four tuples representing my training and testing set
  (x_train, y_train), (x_test, y_test) = mnist.load_data()
  
  #print the number of elements in training and testing sets
  print("There are " + str(x_train.shape[0])+ " Images in the TRAIN data set")
  print("There are " + str(x_test.shape[0])+ " Images in the TEST data set")

  print("\n FILTERING DATA SETS for digits 2, 1 and 0.... \n")

  x_train, y_train = filter_original_sets(x_train, y_train)
  (x_test, y_test) = filter_original_sets(x_test, y_test)
  print("There are " + str(x_train.shape[0])+ " Images in the TRAIN data set")
  print("There are " + str(x_test.shape[0])+ " Images in the TEST data set")

  print("\n Creating validation set... \n")

  num_train_img = x_train.shape[0]
  train_indices = np.arange(0, x_train.shape[0])
  train_indices_shuffled = np.random.permutation(train_indices)

  #update X and Y train with shuffled indices
  x_train = x_train[train_indices_shuffled,:,:]
  y_train = y_train[train_indices_shuffled]

  #select 20 percent of the set for validation.
  x_valid = x_train[0 : int(0.2*num_train_img),:,:]
  y_valid = y_train[0 : int(0.2*num_train_img)]

  #set the remainer 80 percent onto the x/y train
  x_train = x_train[int(0.2*num_train_img):,:,:]
  y_train = y_train[int(0.2*num_train_img):]

  #Transforming all images into the 3x3 grid
  x_test = x_test[:,13:16,13:16]
  x_valid = x_valid[:,13:16,13:16]
  x_train = x_train[:,13:16,13:16]


  print("There are " + str(x_train.shape[0])+ " Images in the TRAIN data set")
  print("There are " + str(x_valid.shape[0])+ " Images in the VALIDATION set")
  print("There are " + str(x_test.shape[0])+ " Images in the TEST data set")

  print(x_test.shape)


  print("\n Averaging the data... \n")

  avg_arr_train = []
  count = 0
  for e in x_train:
    sum = 0
    for i in range(0,3):
      for j in range(0,3):
        sum +=e[i][j]
    avg_arr_train.append(((sum)/9))
    count = count + 1
 
  avg_arr_test = []
  count = 0
  for e in avg_arr_test:
    sum = 0
    for i in range(0,3):
      for j in range(0,3):
        sum +=e[i][j]
    avg_arr_test.append(((sum)/9))

  avg_arr_test = []
  count = 0
  for e in avg_arr_test:
    sum = 0
    for i in range(0,3):
      for j in range(0,3):
        sum +=e[i][j]
    avg_arr_test.append(((sum)/9))

  print("\n Selecting 500 images from our training set... \n")

  plt.xlim([0, 510])
  plt.ylim([min(avg_arr_train), max(avg_arr_train)+10])

#I need 4 arrays (2) in order to store the x and y coordinates of the two categories (0s and 1s)
  x_1 = []
  y_1 = []

  x_2 = []
  y_2 = []
  count = 0
  for g in range(0,500):
    choice = random.randint(0, len(avg_arr_train))
    #print("Value: "+ str(avg_arr_train[g]) + " label: " + str(y_train[g]))
    if(str(y_train[g]) == "1"):
      #print("1 detected")
      x_1.append(count)
      y_1.append(avg_arr_train[g])
    if(str(y_train[g]) == "0"):
      #print("0 detected")
      x_2.append(count)
      y_2.append(avg_arr_train[g])
    count = count + 1
  
  print("\n Plotting the data... \n")

  plt.xlabel("X")
  plt.ylabel("Average Value")
  plt.plot(x_1, y_1, "ro", label = "Digit 1s")
  plt.plot(x_2, y_2, "bv", label = "Digit 0s")
  plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
  plt.tight_layout()
  plt.show()


  x =  float(input("\n Please Enter a Threshold to calculate accuracy... \n"))
  
  #Ask for a threshold

  print("\n Calculating Accuracy based on the Threshold... \n")

  calculate_accuracy(x,avg_arr_train, y_train)
  
  #Calculate threshold





if __name__== "__main__":
  main()

