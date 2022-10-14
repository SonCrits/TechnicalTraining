from xmlrpc import client

server_url = 'http://localhost:8015'
db_name = 'odoo15_6'
username = 'admin'
password = 'admin'
common = client.ServerProxy('%s/xmlrpc/2/common' %server_url)
user_id = common.authenticate(db_name, username, password, {})
models = client.ServerProxy('%s/xmlrpc/2/object' %server_url)
if user_id:
    search_domain = []

    # search students
    students_ids = models.execute_kw(db_name, user_id, password, 'education.student', 'search',
                                    [search_domain],{'limit': 5})
    print('Student ids found:', students_ids)

    # read data students
    students_data = models.execute_kw(db_name, user_id, password, 'education.student',
                                    'read', [students_ids, ['name', 'email']])
    print("Students data:", students_data)
else:
    print('Wrong credentials')
