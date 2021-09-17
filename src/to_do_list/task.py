import datetime
from tabulate import tabulate


class Task:

    def __init__(self, title, content, assign_to, status):
        self.title = title
        self.content = content
        self.assign_to = assign_to
        self.status = status
        self.create_date = datetime.datetime.now().strftime('%YY/%m/%d %H:%M:%S')

    @property
    def get(self):
        return {'title': self.title, 'content': self.content, 'assign_to': self.assign_to,
                'status': self.status, 'create_date': self.create_date}


class AssignmentTask:

    def __init__(self):
        self.tasks = {}
        self.fields = {
            'title': {
                'name': 'Title of task: ',
                'options': [],
                'required': True
            },
            'content': {
                'name': 'Content of task: ',
                'options': [],
                'required': True
            },
            'assign_to': {
                'name': 'Assign task to: ',
                'options': [],
                'required': True
            },
            'status': {
                'name': 'Status of task: ',
                'options': ['approved', 'reproved', 'in_progress', 'complete'],
                'required': True
            }
        }

    def valide_data(self, field):
        data_field = input(self.fields[field]['name'])
        if self.fields[field]['required'] and len(data_field) == 0:
            return self.valide_data(field)
        elif len(self.fields[field]['options']) > 0:
            if not data_field in self.fields[field]['options']:
                print(f'Digit to valid options {",".join(self.fields[field]["options"])}')
                return self.valide_data(field)
            else:
                return data_field
        else:
            return data_field

    def create(self):
        id_task = max(self.tasks.keys()) + 1 if len(self.tasks) > 0 else 1
        element = {}
        for field in self.fields:
            data_field = self.valide_data(field)
            element[field] = data_field
        object_task = Task(title=element['title'], content=element['content'],
                           assign_to=element['assign_to'], status=element['status'])
        self.tasks[id_task] = object_task
        print('Create success')
        return True

    def get(self):
        headers = ['Title of task', 'Content of task', 'Assign task to', 'Status of task', 'Date created']
        results = []
        for task in self.tasks:
            result = [self.tasks[task].title, self.tasks[task].content, self.tasks[task].assign_to,
                      self.tasks[task].status, self.tasks[task].create_date
                      ]
            results.append(result)
        print(tabulate(results, headers=headers))
        return True
