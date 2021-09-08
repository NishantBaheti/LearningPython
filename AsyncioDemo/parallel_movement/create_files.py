import os 


n_files = 50
path = './storage/source'
ext = 'csv'
for i in range(n_files):
    f_name = f'a_{i}.{ext}'
    with open(os.path.join(path,f_name),'w') as file:

        file.write('Hello')
