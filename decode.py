import zipfile

def decodeZipFile(savepath,zfile,password):
    try:
        with zipfile.ZipFile(zfile) as z:
            z.extractall(path=savepath,pwd=password.encode('utf-8'))
            print('decode password sucessfully,password is %s'% (password))
            return True
    except:
        print('faild')
        return False

if __name__=='__main__':
    f = open("code.txt") #读取密码字典
    lines = f.readlines() #读取每一行的密码
    for line in lines:
        password = line.strip('\n') #去掉每一行里面的‘\n’
        sucess = decodeZipFile('./','1.zip',password)
        if(sucess):
            break

