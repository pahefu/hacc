
all:
	@echo ">> Creating proxy scripts"
	@mkdir -p bin
	@mkdir -p tests

	@python generate.py
	@chmod +x ./bin/*

clean:
	rm -r bin tests

install:
	@echo "Installing binary files"
	@mkdir -p $(INSTALL_BIN)
	cp bin/* $(INSTALL_BIN)/
