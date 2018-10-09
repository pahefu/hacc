def print_usage():
	print("Pahefu's Haiku C/Cpp proxy\n")
	print("usage: hacc-conf key=\"value\"\n")
	print("Key values:")
	print("\treset : Reset file to default values")
	print("\tlist : Shows current values in file")
	print("\tremove : Removes libs or flags from compilation")
	print("\tadd_flags : Adds headers or defines to the compilation (always)")
	print("\tadd_libs : Adds libs to the compilation (if linking detected)")
	print("\tdebug : Shows/hides the params passed to the linker")
	print("\tsmart_linking : Enables/disables linking instead of compiling detection")
	
def user_val_to_bool(val):
	final_val = "0"
	val = val[0].lower()
	if val=="true" or val=="yes" or val=="1" or val=="active":
		final_val = "1"
	return final_val

def parse_arg_to_config(args):
	data_changed = False

	Config.parse_file()

	if len(args)==1:
		print_usage()
		return
	
	val = args[1]
	if "=" not in val and val.lower() not in ["reset","list"]:
		print("Error: Param format is not ok\n")
		print_usage()
		return

	# fix the reset and list commands not conforming to rule
	if "=" not in val: 
		val+="=" 

	key,val = val.split("=")
	key = key.strip().lower()
	val = val.split(" ")
	if key=="reset":
		Config.reset_file()
		return
	elif key == "list":
		for k in Config.props.keys():
			print("%s = %s" % (k, Config.props[k]))
		return
	elif key=="remove":
		Config.props["removed_args"]=val
		data_changed = True
	elif key =="add_flags":
		Config.props["added_flags"]=val
		data_changed = True
	elif key =="add_libs":
		Config.props["added_libs"]=val
		data_changed = True
	elif key =="debug":
		Config.props["debug_params"]=[user_val_to_bool(val)]
		data_changed = True
	elif key =="smart_linking":
		Config.props["smart_linking_detection"]=[user_val_to_bool(val)]
		data_changed = True

	if data_changed:
		Config.save_file()
	else:
		print("Error: Key '%s' not known\n" % key)
		print_usage()

if __name__ == "__main__":
        parse_arg_to_config(sys.argv)

