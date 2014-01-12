LIBS  = -I/usr/include/python2.7
CFLAGS = -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing

C_FILES1 := $(wildcard simpyx/*.c)
C_FILES2 := $(wildcard simpyx/resources/*.c)

PY_FILES1 := $(wildcard simpyx/*.py)
PY_FILES2 := $(wildcard simpyx/resources/*.py)

PYX_FILES1 := $(wildcard simpyx/*.pyx)
PYX_FILES2 := $(wildcard simpyx/resources/*.pyx)

all:
	python setup.py build_ext --inplace

cythonize: $(PY_FILES1) $(PY_FILES2) $(PYX_FILES1) $(PYX_FILES2)
	cython -a -X profile=True $^		

compile: $(C_FILES1) $(C_FILES2)
	gcc $^ $(CFLAGS) $(LIBS)

clean:
	@rm -f *.out
	@rm -f simpyx/*.c simpyx/*.o simpyx/*.so simpyx/*.html simpyx/*.pyc
	@rm -f simpyx/resources/*.c simpyx/resources/*.o simpyx/resources/*.so simpyx/resources/*.html simpyx/resources/*.pyc
	@rm -rf build
