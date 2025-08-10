.PHONY: env install clean

env:
	conda create -n spr python==3.11.*

install:
	pip install .
