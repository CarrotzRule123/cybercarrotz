import json
space = {'MON':'    ', 'TUE':'      ', 'WED':'    ', 'THU':'     ', 'FRI':'        ', 'CODE': '   ', 'PSWD': ' '}

class Timetable:
    def __init__(self):
        self.days = {'MON':[], 'TUE':[], 'WED':[], 'THU':[], 'FRI':[]}

    def parse(self, data):
        self.days = json.loads(data)

    def update(self):
        data = 'TIMETABLE:\n'
        for day in self.days:
            data = data + day
            if len(self.days[day]) == 0:
                data = data + space[day] + '*No class*' + '\n'
            for i in range(0, len(self.days[day])):
                text = self.days[day][i]
                nbsp = '              '
                if i == 0 :
                    nbsp = space[day]
                if text[-1] == 'b':
                    text = self.bold(text[:-2])
                elif text[-1] == 's':
                    text = self.strike(text[:-2])
                else:
                    text = text[:-2]
                data = data + nbsp + text + '\n'
            if day == 'FRI' :
                data = data + '\n'
        data = data[:-1]
        return data

    def add(self, day, course, time, state):
        self.days[day].append(course + ' ' + time + ' ' + state)

    def remove(self, day, index):
        self.days[day].pop(index - 1)

    def edit(self, day, index, course, time, state):
        self.days[day][index - 1] = course + ' ' + time + ' ' + state

    def strike(self, txt):
        return '~~' + txt + '~~'
    
    def bold(self, txt):
        return '**' + txt + '**'       
