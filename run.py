import sys

my_file = sys.argv[1]

f = open(my_file, 'r')
out_file = open('out.txt', 'w')
for line in f:
    ret_type = ''
    var_name = ''
    temp = line.strip(';\n').split(' ')
    if (temp[0].lower() == 'private' or temp[0].lower() == 'public' or temp[0].lower() == 'protected'):
        ret_type = temp[1]
        var_name = temp[2]
    else:
        ret_type = temp[0]
        var_name = temp[1]
    getter = '{}public {} get{}() {{ return this.{}; }}'.format('    ', ret_type, var_name.title(), var_name)
    setter = '{}public void set{}({} {}) {{ this.{} = {}; }}'.format('    ', var_name.title(), ret_type, var_name, var_name, var_name)
    out_file.write(getter)
    out_file.write('\n')
    out_file.write(setter)
    out_file.write('\n')

f.close()
out_file.close()
