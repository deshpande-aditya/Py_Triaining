import ctypes
import time

img0= r"C:\Users\Lenovo\PycharmProjects\Py_training\images\lake1.jpg"
img1=r"C:\Users\Lenovo\PycharmProjects\Py_training\images\lake3.jpg"

images = [img0, img1]
print("hello Aditya")

localtime = time.asctime( time.localtime(time.time()))
print("Date and Time Details: " + str(localtime))


n = int(input("Enter n(0-1): "))
if n>=0 and n<=1:
    print("you chose: " + str(n))
    ctypes.windll.user32.SystemParametersInfoW(1, 0, images[n], 0)
    print("wallpaper " , n , "successfully applied")
else:
    print("Wrong input for wallpaper - you chose: " , n)
