import sys
import os

def generate_file(file_name, content_file, cmd_to_run):

	with open("./config.py") as source:
		config_data = source.read()

	with open(content_file) as source:
		handler_data = source.read()
	
	with open("./bin/%s" % file_name, "wb+") as f:
		f.write("#!/bin/python\n\n")
		f.write("cmd = \"%s\"\n\n" % cmd_to_run)
		f.write(config_data+"\n")
		f.write(handler_data+"\n")


def generate_tests():
	with open("./tests/test.c","wb+") as f:
		f.write("#include <stdio.h>\n\n int main(){ printf(\"C Test\\n\"); return 0; }");

	with open("./tests/test.cpp","wb+") as f:
		f.write("#include <iostream>\n\n using namespace std;\n int main(){ cout<<(\"CPP Test\")<<endl; return 0; }");



if __name__ == "__main__":
	handler = "./handler.py"
	configurer = "./configurer.py"

	generate_file("hagcc", handler, "gcc")
	generate_file("hacc", handler, "cc")
	generate_file("hac++", handler, "c++")
	generate_file("hag++", handler, "g++")
	generate_file("hacpp", handler, "cpp")
	generate_file("hacc_conf", configurer, "")
	generate_tests()
