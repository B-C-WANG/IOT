import os

device_file_path='/dev/input'

def show_device():
    os.chdir(device_file_path)
    for i in os.listdir(os.getcwd()):
        name_path=device_file_path+i+'/device/name'
        if os.path.isfile(namepath):
            print 'name:%s,device:%s'%(i,file(name_path).read())
show_device
