def IOU(Reframe,GTframe):
    """
    input:
    ReFrame:(x1,y1,x1',y1')  左上角 右下角坐标，若给出w，h可直接替换变量
    GTFrame:(x2,y2,x2',y2')
    """
    x1 = Reframe[0]
    y1 = Reframe[1]
    x1_= Reframe[2]
    y1_= Reframe[3]
    width1 = abs(x1_-x1)
    height1 = abs(y1_-y1)

    x2 = GTframe[0]
    y2 = GTframe[1]
    x2_ = GTframe[2]
    y2_ = GTframe[3]
    width2 = abs(x2_ - x2)
    height2 = abs(y2_ - y2)


    insection_w=width1+width2-(max(x1+width1,x2+width2)-min(x1,x2))
    insection_h=height1+height2-(max(y1+height1,y2+height2)-min(y1,y2))

    if(insection_w<=0 or insection_h<=0):
        IOU_S=0
    else:
        IOU_S=(insection_w*insection_h)/(width1*height1+width2*height2-insection_w*insection_h)
    return IOU_S
print(IOU((0,1,1,0),(-1,1,0,0)))
