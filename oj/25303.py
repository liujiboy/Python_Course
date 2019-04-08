#定义一个class存储开始milking和结束milking时间
class milking():
    def __init__(self,start,end):
        self.start=start
        self.end=end
    #定义<运算符
    def __lt__(self,other):
        return self.start<other.start
#读取数据并放置在milkings列表中
n=int(input())
milkings=[]
for i in range(n):
    line=input().split()
    milkings.append(milking(int(line[0]),int(line[1])))
#按照开始milking的时间对milkings进行排序（__lt__函数）
milkings.sort()
maxMilingTime=0
maxIdelTime=0
start=milkings[0].start #第0个milking的开始时间
end=milkings[0].end #第0个milking的结束时间
for i in range(1,len(milkings)):
    #第i个milking的开始时间与上一个milking结束时间的差值
    val=milkings[i].start-end 
    if val<=0: #若差值小于等于0，说明两者相交
        if milkings[i].end>end: #第i个milking结束时间包含了上一个结束时间
            end=milkings[i].end
    else: #反之两者不相交，说明中间有idel time
        if maxMilingTime<end-start: #计算最大milking time间隔
            maxMilingTime=end-start
        if maxIdelTime<val: #计算最大idel time间隔
            maxIdelTime=val
        start=milkings[i].start 
        end=milkings[i].end
if maxMilingTime<end-start: #循环退出后还要计算最后一次
	maxMilingTime=end-start
print(maxMilingTime,maxIdelTime)