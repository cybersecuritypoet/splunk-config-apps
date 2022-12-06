import json
import jinja2
import yaml
import os
import sys
import argparse

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

def fix_group(group, globals):
	if "prefix" not in group.keys():
		group["prefix"] = globals["prefix"]
	if "postfix" not in group.keys():
		group["postfix"]= globals["postfix"]
	return group

def fix_app(app, group, globals):
	if "prefix" not in app.keys():
		if group is not None and "prefix" in group.keys():
			app["prefix"] = group["prefix"]
		else:
			app["prefix"] = globals["prefix"]
	if "postfix" not in app.keys():
		if group is not None and "postfix" in group.keys():
			app["postfix"] = group["postfix"]
		else:
			app["postfix"] = globals["postfix"]
	if "name" not in app.keys():
		app["name"] = app["prefix"]+app["template"]+app["postfix"]
	if "SSL" in app.keys():
		app["SSL"] = merge_obj(globals["SSL"],app["SSL"])
	return app


def load_data(cfg_file,quiet=False):
	global_apps = {}
	groups = {}
	with open(cfg_file) as f:
		data = f.read()
		if(os.path.splitext(cfg_file)[1] == ".json"):
			try:
				obj = json.loads(data)
			except json.decoder.JSONDecodeError as ex:
				if not quiet:
					print("JSON error: "+ex.msg+" line: "+str(ex.lineno)+" column: "+str(ex.colno)+" (char: "+str(ex.pos)+") ; file: "+cfg_file)
					print('! Exiting (21).')
				exit(21)
		elif(os.path.splitext(cfg_file)[1] == ".yaml"):
			try:
				obj = yaml.safe_load(data)
			except:
				if not quiet:
					print("Exception while loading YAML")
				raise
				exit(21)
		else:
			if not quiet:
				print("Unknown file extension: "+os.path.splitext(cfg_file)[1]+" ; Supported extensions: yaml, json.")
			exit(23)
		verify_config(obj)
		if "apps" in obj["globals"].keys():
			for app in obj["globals"]["apps"]:
				global_apps[app["name"]] = fix_app(app,None,obj["globals"])
		for group in obj["groups"]:
			group = fix_group(group,obj["globals"])
			groups[group["name"]] = group.copy()
			groups[group["name"]]["apps"] = {}
			if "apps" in obj["globals"].keys():
				for app in obj["globals"]["apps"]:
					groups[group["name"]]["apps"][app["name"]] = fix_app(app,None,obj["globals"])
			for app in group["apps"]:
				app = fix_app(app, group, obj["globals"])
				if app["name"] in global_apps.keys():
					groups[group["name"]]["apps"][app["name"]]=merge_obj(global_apps[app["name"]],app)
				else:
					groups[group["name"]]["apps"][app["name"]]=app
	return groups

def render_data(groups,tpl_path,apps_sources_tpl_path,out_path,quiet=False):
	for group in groups.values():
		if "path" not in group.keys():
			group["path"] = group["name"]
		group_path = os.path.join(out_path,group["path"])
		os.makedirs(group_path, 0o700, True )
		if (apps_sources_tpl_path is not None and "source_apps" in group.keys()):
			for source_app in group["source_apps"]:
				if not ("skip" in source_app.keys() and source_app["skip"] == True ):
					source_apps_tpl_path = os.path.join(apps_sources_tpl_path,source_app["template"])
					app_out_path = os.path.join(group_path,source_app["name"])
					for root, dirs, files in os.walk(source_apps_tpl_path):
						for e in files:
							file_path = os.path.join(root,e)
							if os.path.isfile(file_path):
								with open(file_path,"r") as tpl:
									if not quiet:
										print('. Rendering: '+file_path)
									try:
										j2template = jinja2.Environment(loader=jinja2.FileSystemLoader(apps_sources_tpl_path)).from_string(tpl.read())
									except jinja2.exceptions.TemplateSyntaxError as ex:
										if not quiet:
											print("!  Template error : "+ex.message+" In file: "+file_path+" ; line: "+str(ex.lineno))
											print("! Exiting (4).")
										exit(4)
									dir_path = os.path.join(app_out_path,os.path.relpath(root,source_apps_tpl_path))
									os.makedirs(dir_path,0o700,True)
									with open(os.path.join(dir_path,e),"w") as f:
										try:
											content = j2template.render(conf=source_app, undefined=jinja2.StrictUndefined)
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
										if not quiet:
											print('+ Writing: '+os.path.join(dir_path,e))
										f.write(content)
		if (tpl_path is not None and "apps" in group.keys()):
			for app in group["apps"].values():
				if not ("skip" in app.keys() and app["skip"] == True ):
					app_tpl_path = os.path.join(tpl_path,app["template"])
					app_out_path = os.path.join(group_path,app["name"])
					for root, dirs, files in os.walk(app_tpl_path):
						for e in files:
							file_path = os.path.join(root,e)
							if os.path.isfile(file_path):
								with open(file_path,"r") as tpl:
									if not quiet:
										print('. Rendering: '+file_path)
									try:
										j2template = jinja2.Environment(loader=jinja2.FileSystemLoader(tpl_path)).from_string(tpl.read())
									except jinja2.exceptions.TemplateSyntaxError as ex:
										if not quiet:
											print("!  Template error : "+ex.message+" In file: "+file_path+" ; line: "+str(ex.lineno))
											print("! Exiting (4).")
										exit(4)
									dir_path = os.path.join(app_out_path,os.path.relpath(root,app_tpl_path))
									os.makedirs(dir_path,0o700,True)
									with open(os.path.join(dir_path,e),"w") as f:
										try:
											content = j2template.render(conf=app, undefined=jinja2.StrictUndefined)
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
										if not quiet:
											print('+ Writing: '+os.path.join(dir_path,e))
										f.write(content)

def main():
	tpl_path = "../apps/"
	cfg_file = ""
	out_path = "../compiled_apps/"
	apps_sources_tpl_path = None
	quiet = False

	argparser = argparse.ArgumentParser(description = "Generates PKI install scripts")

	argparser.add_argument( "config", help = "Configuration file")
	argparser.add_argument( "out_path", help = "Path where resulting apps will be written")
	argparser.add_argument( "apps_template_path", help = "Application template path")
	argparser.add_argument( "apps_sources_template_path", help = "Application (sources) template path")
	argparser.add_argument("-q", "--quiet", action='store_true', help="Quiet output")

	args = argparser.parse_args()

	if args.quiet:
		quiet = True
	if args.config:
		cfg_file = args.config
	if args.out_path:
		out_path = args.out_path
	if args.apps_template_path:
		tpl_path = args.apps_template_path
	if args.apps_sources_template_path:
		apps_sources_tpl_path = args.apps_sources_template_path
		

	

	if(not os.path.exists(cfg_file)):
		print("No such file: "+cfg_file)
		exit(2)
	if(not os.path.exists(tpl_path)):
		print("No such directory: "+tpl_path)
		exit(2)
	if(apps_sources_tpl_path is not None and not os.path.exists(apps_sources_tpl_path)):
		print("No such directory: "+apps_sources_tpl_path)
		exit(2)
		
	groups = load_data(cfg_file,quiet)
	render_data(groups,tpl_path,apps_sources_tpl_path,out_path,quiet)

main()