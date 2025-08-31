import os,sys,platform
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('chmod +x exo')
    os.system('./exo')
elif bit == '32bit':
    os.system('chmod +x exo32')
    os.system('./exo32')
else:
    print('device not supported')
