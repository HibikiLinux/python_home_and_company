
name = input("username:")
age = input("age:")
job = input("job:")
salary =input("salary:")
info ='''
-------%s-------
name:%s
age:%s
job:%s
salary:%s
'''%(name,name,age,job,salary)
print(info)

info2 = '''-------{_name}-------
name:{_name}
age:{_age}
job:{_job}
salary:{_salary}
'''.format(_name=name,_age=age,_job=job,_salary=salary)
print(info2)