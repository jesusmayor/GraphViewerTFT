import os

files = [f for f in os.listdir('.') if os.path.isfile(f)]
with open('somefile.txt', 'a') as the_file:
    for f in files:
        str_new = "{ name: '"+f.rsplit( ".", 1 )[ 0 ] +"' },\n"
        the_file.write(str_new)
        print (str_new)