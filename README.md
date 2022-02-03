# **Pencil-sketches**
### Introduction
There are multiple reasons as to why someone would want to change a coloured image to a pencil
sketch. One could perform this operation on an image dataset to extract important or significant
features from the images. It could be used for pattern recognition and image morphology. It reduces the
amount of data in an image and preserves the structural property of the image in the dataset.
It could also be used purely for aesthetic reasons. A few people find the need to convert their images to
a pencil sketch as it takes up less memory in comparison to the original image. Another reason for
converting the original image is to eradicate the colours and the colour noise.
The basic idea of converting to a pencil sketch is to first convert from RGB to grayscale, though this is
not the only change being made. The main goal is to detect the edges of all the significant features in
the image.
Anyone who wants a pencil sketch version of one of the datasets available, could simply run the code
and choose their desired image dataset to get a pencil sketch version of the same. So another reason for
this project is simply for the entertainment of the user who wishes to have pencil sketch versions of any
of the image datasets present in the same folder as the code itself.

###Design & Implementation
To start off, we’ve imported the glob function from the glob module, opencv module, listdir function
from os and time function from the time module. All the folders (excluding zip files and the .py files) 
in the current working directory are displayed using the listdir function. The user is asked
which dataset they’d like to convert to pencil sketches and the chosen dataset is passed through
the get_data_from_folder() function. Here, the glob function is used to create an iterator containing the
path locations of all the images. 
```
list_of_files = []
for i in listdir():
  if not i.endswith('.py') and not i.endswith('.zip') and not i.endswith('.rar'):
    list_of_files.append(i)
    print(i)
print('\n',end = ' ')
while True:
  choice = input('which of these would you like to convert to pencil sketches ')
  if choice not in list_of_files:
    print("Sorry, couldn't find ",choice,".",sep = ' ')
    continue
  else:
    break
```
And each image is first resized, so as to maintain consistency,
converted to a grayscale image and blurred using the gaussian blur function. The kernel size we found
best suitable for the task is (21,21). Then the blurred image is divided with the grayscale image to get
the desired result. All the converted images are saved by the same file name as the original images
hence replacing them. 
```
for i in class_names:
  files = glob(main_folder+"/"+i+"/*")
  for f in files: #iterates through the the 'files' list
    image = cv2.imread(f) #read the image
    image = cv2.resize(image,(IMG_SIZE,IMG_SIZE))
    grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey_image, (21, 21), 0)
    sketch = cv2.divide(grey_image, blur, scale=256.0)
    cv2.imwrite(f, sketch) 
    global number_of_images
    number_of_images+=1 #counts the number of images
```
The time taken for the whole task to be performed is noted to see how efficient
the program is. After the function is executed a prompt appears on the terminal window asking the user
to open the image dataset to see the results.

