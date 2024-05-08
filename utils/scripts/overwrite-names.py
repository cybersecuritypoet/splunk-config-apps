import json
import jinja2
import yaml
import os
import argparse
import re

def load_vars(vars_file,quiet=False):
    with open(vars_file) as f:
        file = f.read()
        if(os.path.splitext(vars_file)[1] == ".json"):
            try:
                obj = json.loads(file)
            except json.decoder.JSONDecodeError as ex:
                if not quiet:
                    print("JSON error: "+ex.msg+" line: "+str(ex.lineno)+" column: "+str(ex.colno)+" (char: "+str(ex.pos)+") ; file: "+vars_file)
                    print('! Exiting (21).')
                exit(21)
        elif(os.path.splitext(vars_file)[1] == ".yaml" or os.path.splitext(vars_file)[1] == ".yml"):
            try:
                obj = yaml.safe_load(file)
            except:
                if not quiet:
                    print("Exception while loading YAML")
                raise
                exit(21)
        else:
            if not quiet:
                print("Unknown file extension: "+os.path.splitext(vars_file)[1]+" ; Supported extensions: yml/yaml, json.")
            exit(23)
        return obj

def render_data(apps_path,vars,path_regex=None,quiet=False,list=False):
    if not quiet:
        print ("Vars: "+str(vars))
    for root, dirs, files in os.walk(apps_path):
        for e in files:
            file_path = os.path.join(root,e)
            if os.path.isfile(file_path) and (path_regex == None or path_regex.match(file_path)):
                orig_content=None
                with open(file_path,"r") as file:
                    if not quiet:
                        print('+ Reading: '+file_path)
                    orig_content = file.read()
                    try:
                        j2template = jinja2.Environment(loader=jinja2.FileSystemLoader(file_path)).from_string(orig_content)
                    except jinja2.exceptions.TemplateSyntaxError as ex:
                        if not quiet:
                            print("!  Template error : "+ex.message+" In file: "+file_path+" ; line: "+str(ex.lineno))
                            print("! Exiting (4).")
                        exit(4)
                    try:
                        content = j2template.render(vars)
                    except jinja2.exceptions.UndefinedError as ex:
                        if not quiet:
                            print('! Template error : '+ex.message+' In file: '+file_path)
                            print('! Exiting (5).')
                        exit(5)
                    except TypeError as ex:
                        if not quiet:
                            print('! Type error : '+str(ex.args)+' In file: '+file_path)
                            print('! Exiting (5).')
                        exit(5)
                    file.close()
                if ( orig_content != None and orig_content != content):
                        with open(file_path,"w") as file:
                                if not quiet:
                                        print('+ Writing: '+file_path)
                                if list:
                                        print(file_path)
                                file.write(content)
                                file.close()
def main():

    apps_path = ""
    vars_file = ""
    quiet = False
    list = False
    path_regex = None

    argparser = argparse.ArgumentParser(description = "Generates PKI install scripts")

    argparser.add_argument( "apps", help = "Applications Path")
    argparser.add_argument( "vars", help = "Variables file")
    argparser.add_argument( "-f", "--filter", nargs='?', help = "Filter processed files using")
    argparser.add_argument("-q", "--quiet", action='store_true', help="Quiet output")
    argparser.add_argument("-l", "--list", action='store_true', help="List modified files")
    args = argparser.parse_args()

    if args.quiet:
        quiet = True
    if args.apps:
        apps_path = args.apps
    if args.vars:
        vars_file = args.vars
    if args.list:
        list = True
    if args.filter is not None:
        path_regex = re.compile(args.filter)
        
    if(not os.path.exists(apps_path)):
        print("No such directory: "+apps_path)
        exit(2)
    if(not os.path.exists(vars_file)):
        print("No such file: "+vars_file)
        exit(2)
        
    vars = load_vars(vars_file,quiet)
    render_data(apps_path,vars,path_regex,quiet,list)

main()