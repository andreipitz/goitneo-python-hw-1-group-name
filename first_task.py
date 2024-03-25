from datetime import datetime,timedelta

def get_birthdays_per_week(users):
    birthdays_per_week = {} , []
    today = datetime.now()
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        this_year_birthday = birthday.replace(year=today.year)
        if this_year_birthday < today:
            this_year_birthday = this_year_birthday.replace(year= today.year + 1)
        diff_days = (this_year_birthday - today).days()
        if 0 <= diff_days < 7:
            birthday = this_year_birthday.strftime("%A")
            if birthday == 'Saturday' or birthday == 'Sunday':
                birthday = 'Monday'
        birthdays_per_week[birthday].append(name)
    for day,name in birthdays_per_week:
        print(f'{ day }')        

 
utilizatori = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)},
    {"name": "Jill Valentine", "birthday": datetime(1974, 11, 30)},
    {"name": "John Doe", "birthday": datetime(1990, 3, 12)} 
]       
get_birthdays_per_week(utilizatori)
