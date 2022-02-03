from glob import glob
import cv2 
from os import listdir
from time import time

def get_data_from_folder(main_folder): 
  for i in class_names: 
    files = glob(main_folder+"/"+i+"/*") 
    for f in files:
      image = cv2.imread(f) 
      image = cv2.resize(image,(IMG_SIZE,IMG_SIZE))
      grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
      blur = cv2.GaussianBlur(grey_image, (21, 21), 0)
      sketch = cv2.divide(grey_image, blur, scale=256.0)
      cv2.imwrite(f, sketch)  
      global number_of_images
      number_of_images+=1 

print("Here is a list of a few image datasets:",end = '')
print('\n')

list_of_files = []
for i in listdir():
  if not i.endswith('.py') and not i.endswith('.zip') and not i.endswith('.rar'): 
    list_of_files.append(i)                                                       
    print(i)
print('\n',end = '')

while True: 
    choice = input('Which of these would you like to convert to pencil sketches ')
    if choice not in list_of_files:
        print("Sorry, couldn't find ",choice,".",sep = '')
        continue
    else:
        break

list_of_class_names = glob(choice+'\*') 
class_names = []
IMG_SIZE = 224
path=choice+'\\'
for j in list_of_class_names:
  class_names.append(j.replace(path,'')) 

number_of_images=0
start=time() 
get_data_from_folder(choice) 
stop=time() 
time_taken = "{:.2f}".format(stop-start)

print('It took ',time_taken," s to convert all ",number_of_images," images in the '",choice,"' folder.",sep = '')
print("You may open now open the '",choice,"' folder to see the results.",sep = '')
