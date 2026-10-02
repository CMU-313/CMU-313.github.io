from datetime import datetime, date, timedelta
import yaml

def add_business_days(start_date, add_days, current_year):
    rem_days_to_add = add_days
    current_date = datetime.strptime(start_date, "%a %b %d").replace(year=current_year)
    
    while rem_days_to_add > 0:
        current_date += timedelta(days=1)
        weekday = current_date.weekday()
        if weekday >= 5:
            continue
        rem_days_to_add -= 1

    return current_date

class LineBreakDumper(yaml.SafeDumper):
    # Reference: https://github.com/yaml/pyyaml/issues/127
    def write_line_break(self, data=None):
        super().write_line_break(data)

        if len(self.indents) == 1:
            super().write_line_break()
    
    def ignore_aliases(self, data):
        return True

with open('schedule.yaml', 'r') as file:
    schedule = yaml.safe_load(file)

today = datetime.now()

# Go back to the most recent Sunday
todays_weekday = (today.weekday() + 1) % 7
start_date = today - timedelta(todays_weekday)

projects = []
recitation = None
lectures = []

if schedule: 
    week_start_date = None
    current_date = start_date

    for schedule_day in schedule:
        schedule_date = datetime.strptime((schedule_day['date']+ ' ' + str(today.year)), "%a %b %d %Y").replace(year=current_date.year)
        if not week_start_date and schedule_date > current_date:
            # We're at the current week!
            week_start_date = schedule_date
        elif week_start_date and schedule_date >= week_start_date + timedelta(weeks=1):
            # We left the current week
            break
        
        if schedule_day['homework']['name'] != '':
            projects.append(schedule_day['homework'])
            projects[-1]['date'] = schedule_day['date']
            projects[-1]['end_date'] = add_business_days(schedule_day['date'], schedule_day['homework']['numDays'], current_date.year)

        if week_start_date:
            if schedule_day['lecture']['name'] != '':
                lectures.append(schedule_day['lecture'])
                lectures[-1]['date'] = schedule_day['date']

                if schedule_day['reading']['name'] != '':
                    lectures[-1]['reading'] = schedule_day['reading']

            if schedule_day['recitation']['name'] != '':
                recitation = schedule_day['recitation']
                recitation['date'] = schedule_day['date']

projects = list(filter(lambda project: project['end_date'] > today, projects))

output = {
    "projects": projects,
    "recitation": recitation,
    "lectures": lectures
}

with open(r'this_week.yaml', 'w') as file:    
    documents = yaml.dump(output, file, Dumper=LineBreakDumper, default_flow_style=False)
