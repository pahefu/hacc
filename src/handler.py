this_app_name = "Haiku c/cpp proxy" 
this_cmd_ptr = None


def run_command(args):
	global cmd
	global this_cmd_ptr
	args[0] = cmd #nifty replacement here
	if Config.props["debug_params"][0]=="1":
		print ("[%s] Debug params: "%this_app_name + " ".join(args))
	this_cmd_ptr = subprocess.Popen(args,stdout=subprocess.PIPE,  stderr=subprocess.STDOUT)
	return iter(this_cmd_ptr.stdout.readline, b'')

def proxyfy_cmd(args):
	
	Config.parse_file()

	final_args = []	
	removed_args = []

	smart_linking_active = (Config.props["smart_linking_detection"][0]=="1")
	linking_detected = False
	linking_detection_flags = ["-o", "-fPIC"]
	
	#no smart linking detection, so add always
	if(not smart_linking_active):
		linking_detected = True 

	for arg in args:
		if arg in Config.props["removed_args"] : removed_args.append(arg)
		else: final_args.append(arg)
		if smart_linking_active and arg in linking_detection_flags:
			linking_detected = True
			

	# skip the added args, in case of simple command call
	if (len(args)>1): 
		final_args = final_args + Config.props["added_flags"]
		if smart_linking_active and linking_detected:
			print("[%s]"% this_app_name + " Detected linking mode")
		if linking_detected:
			final_args = final_args + Config.props["added_libs"]

	if(len(removed_args)!=0):
		print("[%s]"% this_app_name + " Removed these non compatible args: %s" % ",".join(removed_args))

	for line in run_command(final_args):
		print(line[:-1])

	this_cmd_ptr.poll()
	if this_cmd_ptr.returncode != 0:
		print("[%s]"% this_app_name + " Error when compiling. exiting with code: %s" % this_cmd_ptr.returncode)
		sys.exit(this_cmd_ptr.returncode)
	sys.exit(0)

if __name__ == "__main__":
	proxyfy_cmd(sys.argv)
