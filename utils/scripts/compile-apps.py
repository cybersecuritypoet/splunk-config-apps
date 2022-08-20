import json
import jinja2
import os
import sys


def merge_obj(obj1, obj2):
	new_obj = {}
	new_obj.update(obj1)
	new_obj.update(obj2)
	return new_obj

def verify_config(conf):
	if "globals" not in conf.keys():
		print("Missing globals definition in config")
		exit(2)
	if "SSL" not in conf["globals"].keys():
		print("Missing SSL definition in globals")
		exit(2)
	if "prefix" not in conf["globals"].keys():
		print("Missing globals prefix definition in config")
		exit(2)
	if "postfix" not in conf["globals"].keys():
		print("Missing globals postfix definition in config")
		exit(2)
	if "groups" not in conf.keys():
		print("Missing groups definition in config")
		exit(2)
	for group in conf["groups"]:
		if "apps" not in group.keys():
			print("Missing apps definition in group")
			exit(2)
		if "name" not in group.keys():
			print("Missing name definition in group")
			exit(2)

def fix_group(group):
	if "prefix" not in group.keys():
		group["prefix"] = ""
	if "postfix" not in group.keys():
		group["postfix"] = ""
	return group

def fix_app(app, globals):
	if "prefix" not in app.keys():
		app["prefix"] = globals["prefix"]
	if "postfix" not in app.keys():
		app["postfix"] = globals["postfix"]
	if "name" not in app.keys():
		app["name"] = app["prefix"]+app["template"]+app["postfix"]
	if "SSL" in app.keys():
		app["SSL"] = merge_obj(globals["SSL"],app["SSL"])
	return app


def load_data(cfg_file):
	global_apps = {}
	groups = {}
	with open(cfg_file) as f:
		data = f.read()
		obj = json.loads(data)
		verify_config(obj)
		for app in obj["globals"]["apps"]:
			global_apps[app["name"]] = fix_app(app,obj["globals"])
		for group in obj["groups"]:
			group = fix_group(group)
			groups[group["name"]] = group.copy()
			groups[group["name"]]["apps"] = {}
			for app in obj["globals"]["apps"]:
				groups[group["name"]]["apps"][app["name"]] = fix_app(app,obj["globals"])
			for app in group["apps"]:
				app = fix_app(app,obj["globals"])
				if app["name"] in global_apps.keys():
					groups[group["name"]]["apps"][app["name"]]=merge_obj(global_apps[app["name"]],app)
				else:
					groups[group["name"]]["apps"][app["name"]]=app
	return groups

def render_data(groups,tpl_path,out_path):
	for group in groups.values():
		if "path" not in group.keys():
			group["path"] = group["name"]
		group_path = os.path.join(out_path,group["path"])
		os.makedirs(group_path, 0o700, True )
		for app in group["apps"].values():
			if not ("skip" in app.keys() and app["skip"] == True ):
				app_tpl_path = os.path.join(tpl_path,app["template"])
				app_out_path = os.path.join(group_path,app["name"])
				for root, dirs, files in os.walk(app_tpl_path):
					for e in files:
						file_path = os.path.join(root,e)
						if os.path.isfile(file_path):
							with open(file_path,"r") as tpl:
								print('. Rendering: '+file_path)
								try:
									j2template = jinja2.Environment(loader=jinja2.FileSystemLoader(tpl_path)).from_string(tpl.read())
								except jinja2.exceptions.TemplateSyntaxError as ex:
									print("!  Template error : "+ex.message+" In file: "+file_path+" ; line: "+str(ex.lineno))
									print("! Exiting (4).")
									exit(4)
								dir_path = os.path.join(app_out_path,os.path.relpath(root,app_tpl_path))
								os.makedirs(dir_path,0o700,True)
								with open(os.path.join(dir_path,e),"w") as f:
									try:
										content = j2template.render(conf=app, undefined=jinja2.StrictUndefined)
									except jinja2.exceptions.UndefinedError as ex:
										print('! Template error : '+ex.message+' In file: '+file_path)
										print('! Exiting (5).')
										exit(5)
									except TypeError as ex:
										print('! Type error : '+str(ex.args)+' In file: '+file_path)
										print('! Exiting (5).')
										exit(5)
									print('+ Writing: '+os.path.join(dir_path,e))
									f.write(content)

def main():
	tpl_path = "../apps/"
	cfg_file = ""
	out_path = "../compiled_apps/"

	if(len(sys.argv) <= 1):
		print("Please provide at least 1 argument: compile-apps.py <cfg_file> [out_path] [tpl_path]")
		exit(1)

	if(len(sys.argv) >=2):
		cfg_file = sys.argv[1]
	if(len(sys.argv) >=3):
		out_path = sys.argv[2]
	if(len(sys.argv) >=4):
		tpl_path = sys.argv[3]

	if(not os.path.exists(cfg_file)):
		print("No such file: "+cfg_file)
		exit(2)
	if(not os.path.exists(tpl_path)):
		print("No such directory: "+tpl_path)
		exit(2)
		
	groups = load_data(cfg_file)
	render_data(groups,tpl_path,out_path)

main()