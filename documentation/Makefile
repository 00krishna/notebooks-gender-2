.DEFAULT_GOAL := build

help:
	@echo ""
	@echo "Available Tasks:"
	@echo "	clean					Clean directory and remove intermediate files"
	@echo "	build					Compile and build latex file"
	@echo "	clean-all				Clean directory including pdfs or other compiled outputs"

build:
	@echo "Compiling latex file to pdf ..."
	latexmk -pdf

clean:
	@echo "Cleaning Directory ..."
	latexmk -c

clean-all:
	latexmk -C
