class AlarmClock:
    def __init__(self, current_time, alarm_time, toggle_alarm):
        self.time = current_time
        self.toggle_alarm = toggle_alarm
        self.alarm_time = alarm_time
        self.current_alarm_time()
        self.set_alarm_time()
        self.alarm_on_off()      

    def current_alarm_time(self):
        print(f'The new time is {self.time}')

    def alarm_on_off(self):
        if self.toggle_alarm == True:
            print('Alarm is on')
        elif self.toggle_alarm == False:
            print('Alarm is off')
        
    def set_alarm_time(self):
        print(f'The alarm is set to {self.alarm_time}')

