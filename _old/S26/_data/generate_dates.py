from datetime import datetime, date, timedelta
import yaml

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

def get_input_datetime(prompt):
    while True:
        try:
            print(prompt)
            input_date = input().split("/")
            return datetime(int(input_date[2]), int(input_date[0]), int(input_date[1]))
        except IndexError as e:
            print(f"Error occurred in processing date input: {e}")
            pass

start_date = get_input_datetime("Enter semester start date (mm/dd/yyyy):")
end_date = get_input_datetime("Enter semester end date (mm/dd/yyyy):")

dict_file = []
for single_date in daterange(start_date, end_date):
    if (single_date.weekday() > 4):
        continue

    str_date = single_date.strftime("%a %b %d")
    dict_file.append({
        "date": str_date, 
        "lecture": {
            "name": "",
            "link": ""
        },
        "recitation": {
            "name": "",
            "slides": "",
            "handout": "",
            "quiz": ""
        }, 
        "reading": {
            "name": "",
            "link": ""
        }, 
        "homework": {
            "name": "",
            "deadline": "",
            "link": "",
            "numDays": 0
        }
    })

class LineBreakDumper(yaml.SafeDumper):
    # Reference: https://github.com/yaml/pyyaml/issues/127
    def write_line_break(self, data=None):
        super().write_line_break(data)

        if len(self.indents) == 1:
            super().write_line_break()

with open(r'schedule.yaml', 'w') as file:    
    yaml.dump(dict_file, file, Dumper=LineBreakDumper, default_flow_style=False)