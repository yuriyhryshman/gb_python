from datetime import datetime, time


class Data:

    def __init__(self, date_str):
        self.date = date_str

    @classmethod
    def division(cls, date_str):
        this_date = []
        date_str = date_str.split('-')
        for el in date_str:
            this_date.append(int(el))
        return this_date

    @staticmethod
    def validation(date_str):
        try:
            valid_date = datetime.strptime(date_str, '%d-%m-%Y')
            return valid_date
        except ValueError:
            print('Неправильная дата!')


dat = Data('24-12-2021')
print(dat.division(dat.date))
print(f'Указанная дата: {dat.validation(dat.date)}')


