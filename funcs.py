def msg_short(msg):
    sent=''
    array=[]
    while len(msg):
        index=msg.find('.')
        if len(sent)+index+2<2000:
            sent+=msg[:index+1]
            msg=msg[index+1:]
        else:
            array.append(str(sent))
            sent=''
    array.append(str(sent))
    return array