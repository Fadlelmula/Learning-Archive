import OS
filelist = OS.listdir('.')
print(filelist)
savefile = open('filelist.txt', 'w')
os.chdir('/tmp')
for file in filelist:
    print(file)
    os.rename(file, '/tmp/' + file)
    os.chdir('/tmp')