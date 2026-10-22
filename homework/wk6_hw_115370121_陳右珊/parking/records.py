import random
from datetime import datetime,timedelta

def generate_records(n:int,seed:int=2026) ->list:
    """計算車輛進出場紀錄"""    
    random.seed(seed)
    base =datetime(2026,10,20,7,0)
    result=[]
    for i in range (1,n+1):
        t_in = base + timedelta(minutes=random.randint(0,600))
        t_out = t_in+timedelta(minutes=random.randint(10,600))
        r =random.random()
        if r<0.3:
            member ="Y"
        else:
            member="N"
        plate = f"CAR-{i:03d}"
        line = f"{plate},{t_in.strftime('%Y-%m-%d %H:%M')},{t_out.strftime('%Y-%m-%d %H:%M')},{member}"
        result.append(line)
    return result

def parse_record(line:str)->tuple:
    """回傳（車牌，進場，出場，分鐘數，是否會員）"""
    plate, s_in, s_out, member = line.split(",")
    t_in = datetime.strptime(s_in, "%Y-%m-%d %H:%M")
    t_out = datetime.strptime(s_out, "%Y-%m-%d %H:%M")
    minutes = int((t_out - t_in).total_seconds() // 60)
    return plate, t_in, t_out, minutes, member == "Y"