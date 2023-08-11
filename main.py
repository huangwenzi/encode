# 每次读取的数量 
OneReadCount = 1024   
def to_file(in_file, out_file):     
    # 打开要保存的文件    
    with open(out_file, "wb") as wf:         
        # 读取数据         
        with open(in_file, "rb") as rf:             
            while True:                 
                data = rf.read(OneReadCount)                 
                if not data:                     
                    break                 
                data_len = len(data)                 
                to_list = []                 
                for i in range(data_len):                     
                    # 转换数据                     
                    to_list.append(~data[i] & 0xff)                 
                wf.write(bytes(to_list))
to_file("utils.so", "utils.zip")
# to_file(in_file, out_file)
