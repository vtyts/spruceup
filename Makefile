.PHONY: env install clean

env:
	conda create -n spruceup python==3.11.*

install:
	pip install .
