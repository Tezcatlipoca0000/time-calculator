def add_time(start, duration, day=False):
    new_time = ''
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

    #
    start_merid = (start.split())[1]
    start_hour = (((start.split())[0]).split(':'))[0]
    start_min = (((start.split())[0]).split(':'))[1]
    print('the start:', start_hour, start_min, start_merid)

    #
    dur_hour = (duration.split(':'))[0]
    dur_min = (duration.split(':'))[1]
    print('the duration:', dur_hour, dur_min)

    #
    new_hour = int(start_hour)
    new_min = int(start_min)
    new_merid = start_merid

    #
    for i in range(int(dur_hour)) :
        if (new_hour + 1) > 12 :
            new_hour = 1
            if new_merid == 'AM' :
                new_merid = 'PM'
            else :
                new_merid = 'AM'
        else :
            new_hour = new_hour + 1

    
    #
    for i in range(int(dur_min)) :
        if (new_min + 1) > 59 :
            new_min = 0
            if (new_hour + 1) > 12 :
                new_hour = 1
                if new_merid == 'AM' :
                    new_merid = 'PM'
                else :
                    new_merid = 'AM'
            else :
                new_hour = new_hour + 1
        else :
            new_min = new_min + 1
    

    new_time = f'''{new_hour}:{new_min} {new_merid}'''

    return new_time