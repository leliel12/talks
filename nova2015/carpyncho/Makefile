
all: build


build:
	rst2pdf slide.rst -s slide.style -o slide.pdf --fit-background scale -b1;

view: build
	evince slide.pdf

