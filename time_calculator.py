def add_time(start, duration, day=False):
    new_time = ''
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

    #
    start_merid = (start.split())[1]
    start_hour = (((start.split())[0]).split(':'))[0]
    start_min = (((start.split())[0]).split(':'))[1]
    #print('the start:', start_hour, start_min, start_merid, day)

    #
    dur_hour = (duration.split(':'))[0]
    dur_min = (duration.split(':'))[1]
    #print('the duration:', dur_hour, dur_min)

    #
    new_hour = int(start_hour)
    new_min = int(start_min)
    new_merid = start_merid

    # 
    if day is not False :
        for i in range(len(days)) :
            if days[i] == day.lower() :
                new_day = i
                num_days = 0
            
    #
    def add_one_hour() :
        nonlocal new_hour, new_merid, new_day, num_days
        if (new_hour + 1) > 12 :
            new_hour = 1
        else :
            new_hour = new_hour + 1
        if new_hour == 12 :
            if new_merid == 'AM' :
                new_merid = 'PM'
            else :
                new_merid = 'AM'
                if day is not False :
                    num_days = num_days + 1
                    if new_day + 1 > 6 :
                        new_day = 0
                    else :
                        new_day = new_day + 1

    #
    for i in range(int(dur_hour)) :
        add_one_hour()
        #print('the hour loop:', new_hour, new_min, new_merid, days[new_day])

    
    #
    for i in range(int(dur_min)) :
        if (new_min + 1) > 59 :
            new_min = 0
            add_one_hour()
        else :
            new_min = new_min + 1
        #print('the min loop:', new_hour, new_min, new_merid, days[new_day])
    
    #
    
    if new_min < 10 :
        new_min = f'''0{new_min}'''
    else :
        new_min = str(new_min)
        
    new_time = f'''{new_hour}:{new_min} {new_merid}'''

    if day is not False :
        new_time = new_time + f''', {days[new_day].capitalize()}'''

    if num_days > 0 :
        if num_days == 1 :
            new_time = new_time + ' (next day)'
        else :
            new_time = new_time + f''' ({num_days} days later)'''

    return new_time