#!/home/student/nsd1905/bin/python
'''备份

1. 需要支持完全和增量备份
2. 周一执行完全备份
3. 其他时间执行增量备份
4. 备份文件需要打包为tar文件并使用gzip格式压缩

'''


from time import strftime
import os
import tarfile
import hashlib
import  pickle
def check_md5(fname):
    m = hashlib.md5()
    with open(fname,'rb') as fobj:
        while 1:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()

def full_backup(src, dst, md5file):
    fname = os.path.basename(src)
    fname = '%s_full_%s.tar.gz' % (fname,strftime('%Y%m%d'))
    fname = os.path.join(dst,fname)

    #打包
    tar = tarfile.open(fname, 'w:gz')
    tar.add(src)
    tar.close()

    #计算每个文件的md5值
    md5dict = {}
    for path, folders, files in os.walk(src):
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)

    #把字典写入文件
    with open(md5file,'wb') as fobj:
        pickle.dump(md5dict, fobj)



def incr_back(src, dst, md5file):
    fname = os.path.basename(src)
    fname = '%s_incr_%s.tar.gz' % (fname, strftime('%Y%m%d'))
    fname = os.path.join(dst, fname)

    #计算当前的md5值
    md5dict = {}
    for path, folders, files in os.walk(src):
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)

    #取出前一天的值
    with open(md5file,'rb') as fobj:
        old_md5 = pickle.load(fobj)

    #将新增的和改动的文件打包
    tar = tarfile.open(fname,'w:gz')
    for key in md5dict:
        if old_md5.get(key) != md5dict[key]:
            tar.add(key)
    tar.close()

if __name__ == '__main__':
    src = '/tmp/demo/security'
    dst = '/tmp/demo/backup'
    md5file = '/tmp/demo/backup/md5.data'
    if strftime('%a') == 'Mon':
        full_backup(src, dst, md5file)
    else:
        incr_back(src, dst, md5file)
                                                                                                                                            68,9         底端
