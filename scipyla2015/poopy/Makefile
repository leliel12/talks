
all: build


build:
	rst2pdf poster.rst -s poster.style -o poster.pdf --use-floating-images --fit-background scale;

view: build
	evince poster.pdf

