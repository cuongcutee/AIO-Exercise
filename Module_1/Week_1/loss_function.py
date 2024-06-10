import math
import random

def exercise3():
   nums_sample = input("number of samples (integer number) which are generated: ")
   if nums_sample.isnumeric() == False:
      print("number of sample must be an integer number")
      return
   loss_name=input("loss name: ")
   total_loss = 0
   for i in range(int(nums_sample)):
      if loss_name=="MAE":
         pred = random.uniform(0,10)
         target = random.uniform(0,10)
         loss = math.fabs((target-pred))
         total_loss+=loss
      if loss_name=="MSE":
         pred = random.uniform(0,10)
         target = random.uniform(0,10)
         loss = (target-pred)**2
         total_loss += loss
      print(f'sample: {i}, pred: {pred}, target: {target}, loss: {loss} ')
   final_loss = total_loss/int(nums_sample)
   print(f'final {loss_name}: {final_loss}')
 



