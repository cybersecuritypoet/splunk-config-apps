import json
import jinja2
import yaml
import os
import sys


def load_vars(vars_file):
    with open(vars_file) as f:
        file = f.read()
        if(os.path.splitext(vars_file)[1] == ".json"):
            try:
                obj = json.loads(file)
            except json.decoder.JSONDecodeError as ex:
                print("JSON error: "+ex.msg+" line: "+str(ex.lineno)+" column: "+str(ex.colno)+" (char: "+str(ex.pos)+") ; file: "+vars_file)
                print('! Exiting (21).')
                exit(21)
        elif(os.path.splitext(vars_file)[1] == ".yaml"):
            try:
                obj = yaml.safe_load(file)
            except:
                print("Exception while loading YAML")
                raise
                exit(21)
        else:
            print("Unknown file extension: "+os.path.splitext(vars_file)[1]+" ; Supported extensions: yaml, json.")
            exit(23)
        return obj

def render_data(apps_path,vars):
    print ("Vars: "+str(vars))
    for root, dirs, files in os.walk(apps_path):
        for e in files:
            file_path = os.path.join(root,e)
            if os.path.isfile(file_path):
                with open(file_path,"r") as file:
                    try:
                        j2template = jinja2.Environment(loader=jinja2.FileSystemLoader(file_path)).from_string(file.read())
                    except jinja2.exceptions.TemplateSyntaxError as ex:
                        print("!  Template error : "+ex.message+" In file: "+file_path+" ; line: "+str(ex.lineno))
                        print("! Exiting (4).")
                        exit(4)
                    try:
                        content = j2template.render(vars)
                    except jinja2.exceptions.UndefinedError as ex:
                        print('! Template error : '+ex.message+' In file: '+file_path)
                        print('! Exiting (5).')
                        exit(5)
                    except TypeError as ex:
                        print('! Type error : '+str(ex.args)+' In file: '+file_path)
                        print('! Exiting (5).')
                        exit(5)
                    file.close()
                with open(file_path,"w") as file:
                    print('+ Writing: '+file_path)
                    file.write(content)
                    file.close()
def main():
	apps_path = ""
	vars_file = ""

	if(len(sys.argv) <= 2):
		print("Please provide arguments: overwrite-names.py <apps_path> <vars_file>")
		exit(1)
	apps_path = sys.argv[1]
	vars_file = sys.argv[2]

	if(not os.path.exists(apps_path)):
		print("No such directory: "+apps_path)
		exit(2)
	if(not os.path.exists(vars_file)):
		print("No such file: "+vars_file)
		exit(2)
		
	vars = load_vars(vars_file)
	render_data(apps_path,vars)

main()