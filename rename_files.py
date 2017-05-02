import os

def read_files():
    file_list = os.listdir("C:\Users\kgaddam\Desktop\Python\prank");
    #print file_list;
    saved_path = os.getcwd();
    os.chdir(r"C:\Users\kgaddam\Desktop\Python\prank")
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None,"0123456789"));

read_files()
