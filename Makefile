PY?=python3
PELICAN?=pelican
PELICANOPTS=

BASE_DIR=$(CURDIR)
INPUT_DIR=$(BASE_DIR)/content
OUTPUT_DIR=$(BASE_DIR)/output
CONF_FILE=$(BASE_DIR)/pelicanconf.py

THEME_DIR=$(BASE_DIR)/ncoda_theme
# SASS_DIR=$(THEME_DIR)/static/css
# MAIN_SASS_FILE=$(SASS_DIR)/main.scss
# CSS_DIR=$(OUTPUT_DIR)/static/css
# MAIN_CSS_FILE=$(CSS_DIR)/main.css
# CSS_SOURCEMAP=$(CSS_DIR)/main.css.map

AMAZEUI_DIR=$(BASE_DIR)/amazeui
AMAZEUI_GULP=$(AMAZEUI_DIR)/node_modules/.bin/gulp
AMAZEUI_TASKS=$(AMAZEUI_DIR)/tools/tasks


help:
	@echo 'Makefile for ncodamusic.org                                               '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make amazeui                        (re)generate amazeUI theme         '
	@echo '   make build                          (re)generate the web site          '
	@echo '   make publish                        generate using production settings '
	@echo '   make netlify-publish                generate using settings for Netlify'
	@echo '   make clean                          remove contents of output directory'
	@echo '                                                                          '


clean:
	@rm -rf $(OUTPUT_DIR)/*

install-amazeui-deps: $(AMAZEUI_DIR)/node_modules/.bin/gulp
$(AMAZEUI_DIR)/node_modules/.bin/gulp:
	cd $(AMAZEUI_DIR) && npm install

amazeui:
	rm -f $(AMAZEUI_TASKS)/config.json
	ln -s $(AMAZEUI_TASKS)/config-ncodamusic.json $(AMAZEUI_TASKS)/config.json
	cd $(AMAZEUI_DIR) && $(AMAZEUI_GULP) customize
	rm $(AMAZEUI_TASKS)/config.json

build-html: $(OUTPUT_DIR)/index.html
$(OUTPUT_DIR)/index.html: $(INPUT_DIR)/**/*.rst $(THEME_DIR)/templates/**/*.html $(THEME_DIR)/templates/*.html
	$(PELICAN) $(INPUT_DIR) -o $(OUTPUT_DIR) -s $(CONF_FILE) $(PELICAN_OPTS)


# build-sass: $(MAIN_CSS_FILE)
# $(MAIN_CSS_FILE): $(SASS_DIR)/*.scss
# 	@rm -rf $(CSS_DIR)/*
# 	@mkdir -p $(CSS_DIR)
# 	sassc --output-style=compressed $(MAIN_SASS_FILE) $(MAIN_CSS_FILE)


# build-sass-debug: $(CSS_SOURCEMAP)
# $(CSS_SOURCEMAP): $(SASS_DIR)/*.scss
# 	@rm -rf $(CSS_DIR)/*
# 	@mkdir -p $(CSS_DIR)
# 	sassc --output-style=expanded --sourcemap $(MAIN_SASS_FILE) $(MAIN_CSS_FILE)


build: amazeui build-html


# publish: clean build-html $(MAIN_CSS_FILE) images
# 	rm -rf $(CSS_DIR)/*.scss
publish: clean build


netlify-publish: install-amazeui-deps publish


.PHONY: amazeui help clean publish netlify-publish install-amazeui-deps
