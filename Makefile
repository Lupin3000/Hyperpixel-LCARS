CURRENT_DIR := $(shell pwd)

help:
	@echo "Usage: $ make <target>"
	@echo " > rectangle : installation for hyperpixel 4.0 rectangle"
	@echo " > round     : installation for hyperpixel 2.1 round"
	@echo " > square    : installation for hyperpixel 4.0 square"

rectangle:
	@echo "[RUN]: Start installation for Hyperpixel 4.0 rectangle"
	make install
	# ...

round:
	@echo "[RUN]: Start installation for Hyperpixel 2.1 round"
	make install
	# ...

square:
	@echo "[RUN]: Start installation for Hyperpixel 4.0 square"
	make install
	# ...

install:
	make deps
	make fonts
	make autostart

deps:
	@echo "[RUN]: Install dependencies"
	# sudo apt install -y python3-pil python3-pil.imagetk
	pip install -r $(CURRENT_DIR)/requirements.txt

fonts:
	@echo "[RUN]: Install fonts"
	# mkdir ~/.fonts/
	# cp $(CURRENT_DIR)/fonts/*.ttf ~/.fonts/

autostart:
	@echo "[RUN]: Create autostart"
	# mkdir -p ~/.config/autostart
