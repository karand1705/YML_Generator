import os

print('Welcome to Command to YML Conversion')
#f=open('docker-compose.yml', 'w+')

def create():
    f=open('docker-compose.yml', 'w+')
    f.write("version: '3'\n")
    f.write("services:\n");
    f.close()
    yes='y'
    tab='  '
    while yes=='y' or yes=='Y':
	    f=open('docker-compose.yml', 'a+')
	    dockeros=input('Enter container name: ')
	    tab='  '
	    f.write(tab+dockeros+":\n")
	    images=input('Enter the image name: ')
	    f.write(tab+tab+"image: "+images+"\n");
	    f.write(tab+tab+"restart: always\n");
	    isenv=input('Do you want to set Environment variable?(y/n)')
	    if isenv=='y' or isenv=='Y':
		    f.write(tab+tab+"environment:\n")
	    while isenv=='y' or isenv=='Y':
		    name=input('Name of env variable: ')
		    value=input('Value of variable: ')
		    f.write(tab+tab+tab+name+": "+value+"\n")
		    isenv=input('More (y/n): ')
	    isvol=input('Do you have volume(y/n): ')
	    if isvol=='y' or isvol=='Y':
		    f.write(tab+tab+"volumes:\n")
	    while isvol=='y' or isvol=='Y':
		    volname=input('Volume name or path: ')
		    dest=input('Destination: ')
		    f.write(tab+tab+tab+'- '+volname+':'+dest+"\n")
		    isvol=input('More (y/n): ')
	    isdepend=input('Any dependencies(y/n): ')
	    if isdepend=='y' or isdepend=='Y':
		    f.write(tab+tab+"depends_on:\n")
	    while isdepend=='y' or isdepend=='Y':
		    val=input('Enter dependent value: ')
		    f.write(tab+tab+tab+'- '+val+"\n")
		    isdepend=input('More (y/n): ')
	    redirport=input('Do you want to redirect ports(y/n): ')
	    if redirport=='y' or redirport=='Y':
		    f.write(tab+tab+"ports:\n")
	    while redirport=='y' or redirport=='Y':
		    val=input('Write host port and destination port( eg 8080:80) ')
		    f.write(tab+tab+tab+'- '+val+"\n")
		    redirport=input('More (y/n) :')
	    print('Generating yml file...')
	    f.close()
	    print('Container added successfully..')
	    yes=input("\n\nWant to create more container?(y/n) ")
	    
def execute():
    os.system('sudo docker-compose up -d')

def listcomposer():
    os.system('sudo docker-compose ps')
    
def welcome():
    while 1:
        inp=int(input("WELCOME TO DOCKER COMPOSER\n\n[1] Create yml file\n[2] execute yml\n[3] List Running containers\n[4] Exit\n"))
        if inp==1:
            create()
        elif inp==2:
            execute()
        elif inp==3:
            listcomposer()
        else:
            exit()
          
welcome()
