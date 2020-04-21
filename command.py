from getopt import getopt
def ph() :
    h='''命令行帮助：
    start.py -h/-?/--help   显示命令行帮助信息
    start.py [-i <输入>] [-d <下载方式>] [-p <p数>] [-m <boolean>] [--ac <boolean>] [--dm <boolean>] [--ad <boolean>] [-r <boolean>] [-y/-n] [--yf/--nf] [--mc avc/hev] [--ar/--nar] [--ax <number>] [--as <number>] [--ak <number>] [--ab/--nab] [--fa none/prealloc/trunc/falloc]
    -i <输入>   av/bv/ep/ss号或者视频链接
    -d <下载方式>   下载方式：1.当前弹幕2.全弹幕3.视频4.当前弹幕+视频5.全弹幕+视频
    -p <p数>    要下载的P数(两个p数可用,连接)，使用a全选，输入为ep号时可用b选择该ep号
    -m <boolean>    是否默认下载最高画质
    --ac <boolean>  是否开启继续下载功能
    --dm <boolean>  是否启用弹幕过滤
    --ad <boolean>  是否在合并完成后删除文件
    -r <boolean>    是否在下载失败后重新下载
    -y  覆盖所有重复文件
    -n  不覆盖重复文件
    --yf    使用ffmpeg
    --nf    不使用ffmpeg
    --mc avc/hev    默认下载最高画质偏好编码器
    --ar    使用aria2c下载
    --nar   不使用aria2c下载
    --ax <number>   aria2c单个服务器最大连接数即-x的参数，范围为1-16
    --as <number>   aria2c单个文件最大连接数即-s的参数，范围为1-*
    --ak <number>   aria2c文件分片大小即-k的参数，范围为1-1024，单位为M
    --ab    在使用aria2c下载时使用备用网址
    --nab   在使用aria2c下载时不使用备用网址
    --fa none/prealloc/trunc/falloc 在使用arai2c下载时预分配方式即--file-allocation的参数
    注1：如出现相同的选项，只有第一个会生效
    注2：命令行参数的优先级高于settings.json里的设置
    注3：ffmpeg和aria2c需要自行下载并确保放入当前文件夹或者放入环境变量PATH指定的目录中'''
    print(h)
def gopt(args) :
    re=getopt(args,'h?i:d:p:m:r:yn',['help','ac=','dm=','ad=','yf','nf','mc=','ar','nar','ax=','as=','ak=','ab','nab','fa='])
    rr=re[0]
    r={}
    for i in rr:
        if i[0]=='-h' or i[0]=='-?' or i[0]=='--help':
            ph()
            exit()
        if i[0]=='-i' and not 'i' in r:
            r['i']=i[1]
        if i[0]=='-d' and not 'd' in r and i[1].isnumeric() and int(i[1])>0 and int(i[1])<6 :
            r['d']=int(i[1])
        if i[0]=='-p' and not 'p' in r :
            r['p']=i[1]
        if i[0]=='-m' and not 'm' in r :
            if i[1].lower()=='true' :
                r['m']=True
            elif i[1].lower()=='false' :
                r['m']=False
        if i[0]=='--ac' and not 'ac' in r:
            if i[1].lower()=='true' :
                r['ac']=True
            elif i[1].lower()=='false' :
                r['ac']=False
        if i[0]=='--dm' and not 'dm' in r:
            if i[1].lower()=='true' :
                r['dm']=True
            elif i[1].lower()=='false' :
                r['dm']=False
        if i[0]=='--ad' and not 'ad' in r:
            if i[1].lower()=='true' :
                r['ad']=True
            elif i[1].lower()=='false' :
                r['ad']=False
        if i[0]=='-r' and not 'r' in r:
            if i[1].lower()=='true' :
                r['r']=True
            elif i[1].lower()=='false' :
                r['r']=False
        if i[0]=='-y' and not 'y' in r:
            r['y']=True
        if i[0]=='-n' and not 'y' in r:
            r['y']=False
        if i[0]=='--yf' and not 'yf' in r:
            r['yf']=True
        if i[0]=='--nf' and not 'yf' in r:
            r['yf']=False
        if i[0]=='--mc' and not 'mc' in r:
            if i[1]=='avc' :
                r['mc']=True
            elif i[1]=='hev' :
                r['mc']=False
        if i[0]=='--ar' and not 'ar' in r:
            r['ar']=True
        if i[0]=='--nar' and not 'ar' in r:
            r['ar']=False
        if i[0]=='--ax' and not 'ax' in r:
            if i[1].isnumeric() :
                i2=int(i[1])
                if i2<17 and i2>0 :
                    r['ax']=i2
        if i[0]=='--as' and not 'as' in r:
            if i[1].isnumeric() :
                i2=int(i[1])
                if i2>0 :
                    r['as']=i2
        if i[0]=='--ak' and not 'ak' in r:
            if i[1].isnumeric() :
                i2=int(i[1])
                if i2>0 and i2<1025 :
                    r['ak']=i2
        if i[0]=='--ab' and not 'ab' in r:
            r['ab']=True
        if i[0]=='--nab' and not 'ab' in r:
            r['ab']=False
        if i[0]=='--fa' and not 'fa' in r:
            if i[1]=='none' or i[1]=='prealloc' or i[1]=='trunc' or i[1]=='falloc':
                r['fa']=i[1]
    return r
if __name__ == "__main__":
    import sys
    print(sys.argv)
    if len(sys.argv)==1 :
        print('该文件仅供测试命令行输入使用，请运行start.py')
    else :
        print(gopt(sys.argv[1:]))
