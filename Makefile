PY?=python3
PELICAN?=pelican
PELICANOPTS=

BASE_DIR=$(CURDIR)
INPUT_DIR=$(BASE_DIR)/content
OUTPUT_DIR=$(BASE_DIR)/output
CONF_FILE=$(BASE_DIR)/pelicanconf.py

THEME_DIR=$(BASE_DIR)/ncoda_theme
SASS_DIR=$(BASE_DIR)/bulma_theme
MAIN_SASS_FILE=$(SASS_DIR)/main.scss
CSS_DIR=$(OUTPUT_DIR)/theme/css
MAIN_CSS_FILE=$(CSS_DIR)/main.css
CSS_SOURCEMAP=$(CSS_DIR)/main.css.map


help:
	@echo 'Makefile for ncodamusic.org                                               '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make build-css                      (re)generate the CSS only          '
	@echo '   make build-html                     (re)generate the HTML only         '
	@echo '   make build                          (re)generate the web site          '
	@echo '   make publish                        generate using production settings '
	@echo '   make netlify-publish                generate using settings for Netlify'
	@echo '   make clean                          remove contents of output directory'
	@echo '                                                                          '


clean:
	@rm -rf $(OUTPUT_DIR)/*


node_modules/bulma/bulma.sass:
	yarn


build-html: $(OUTPUT_DIR)/index.html
$(OUTPUT_DIR)/index.html: pelicanconf.py $(INPUT_DIR)/**/*.rst $(THEME_DIR)/templates/**/*.html $(THEME_DIR)/templates/*.html
	$(PELICAN) $(INPUT_DIR) -o $(OUTPUT_DIR) -s $(CONF_FILE) $(PELICAN_OPTS)


build-css: $(MAIN_CSS_FILE)
$(MAIN_CSS_FILE): node_modules/bulma/bulma.sass $(SASS_DIR)/*.scss
	@rm -rf $(CSS_DIR)/*
	@mkdir -p $(CSS_DIR)
	sassc --output-style=compressed $(MAIN_SASS_FILE) $(MAIN_CSS_FILE)


build-css-debug: $(CSS_SOURCEMAP)
$(CSS_SOURCEMAP): node_modules/bulma/bulma.sass $(SASS_DIR)/*.scss
	@rm -rf $(CSS_DIR)/*
	@mkdir -p $(CSS_DIR)
	sassc --output-style=expanded --sourcemap $(MAIN_SASS_FILE) $(MAIN_CSS_FILE)


build: build-css build-html


publish: clean build


netlify-publish: publish


.PHONY: build-css help clean publish netlify-publish
