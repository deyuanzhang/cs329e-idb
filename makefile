FILES :=                              \
    models.html                      \
    IDB3.log                       \
    test.py                        \
    models.py                    \
    .gitignore                    \
    requirements.txt                     \
    README.md                   \

ifeq ($(shell uname), Darwin)          # Apple
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else ifeq ($(CI), true)                # Travis CI
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3
    AUTOPEP8 := autopep8
else ifeq ($(shell uname -p), unknown) # Docker
    PYTHON   := python                # on my machine it's python
    PIP      := pip3.5
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := python -m pydoc        # on my machine it's pydoc 
    AUTOPEP8 := autopep8
else                                   # UTCS
    PYTHON   := python3.5
    PIP      := pip3
    PYLINT   := pylint3
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
endif


.pylintrc:
	$(PYLINT) --disable=locally-disabled --reports=no --generate-rcfile > $@

models.html: models.py
	$(PYDOC) -w models

IDB3.log:
	git log > IDB3.log

check:
	@not_found=0;                                 \
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
    echo "success";

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -rf __pycache__

config:
	git config -l

format:
	$(AUTOPEP8) -i test.py
	$(AUTOPEP8) -i models.py

scrub:
	make clean
	rm -f  models.html
	rm -f  IDB3.log

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

reunserver:
	$(PYTHON) test.py

reqs:
	pip install -r requirements.txt

test: models.html IDB3.log check runtests