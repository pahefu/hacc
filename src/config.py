import os
import os.path
import sys
import subprocess


class Config:
	
	config_file = "/boot/home/config/settings/hacc.conf"

	props = {}
	
	props["default_removed_args"] = ["-ldl","-lrt","-rdynamic","-pthread"]
	props["removed_args"] = []
	props["added_flags"] = []
	props["added_libs"] = []	

	props["smart_linking_detection"] = ["1"]
	props["debug_params"] = ["1"]

	@staticmethod
	def reset_file():
		config_file = Config.config_file
		props = Config.props
		if os.path.isfile(config_file):
			os.remove(config_file)

		props["default_removed_args"] = ["-ldl","-lrt","-rdynamic","-pthread"]
		props["removed_args"] = []
		props["added_flags"] = []
		props["added_libs"] = []	

		props["smart_linking_detection"] = ["1"]
		props["debug_params"] = ["1"]

		#set defaults	
		props["removed_args"] = [k for k in props["default_removed_args"]]

	
		Config.save_file()
	
	@staticmethod
	def parse_file():
		config_file = Config.config_file
		props = Config.props

		if os.path.isfile(config_file):
			try:
                        	with open(config_file, "rb") as f:
                                	lines = f.read().split("\n")
	                        for l in lines:
        	                        if l.count("=")==0:
                	                        continue
                        	        key,val = l.split("=")
                                	key = key.strip()
	                                val = [v for v in val.split(" ") if len(v)>0]
        				props[key]=val                        

	                except Exception, err:
        	                print("[ERROR] Failed to read the config file. Error was: %s" % err)
		else:
			Config.reset_file()

	@staticmethod
	def save_file():
		config_file = Config.config_file
		props = Config.props
		try:

			with open(config_file,"wb+") as f:
				for k in props.keys():
					data = "%s=%s\n" % (k, " ".join(props[k]))
					f.write(data)
		except Exception,err:
			print("[Error] Failed to save the config file")
				
	
