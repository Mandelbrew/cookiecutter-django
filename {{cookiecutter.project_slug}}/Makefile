#@IgnoreInspection BashAddShebang
##
#
# Usage
#
#   $ make            # compile files that need compiling
#   $ make clean all  # remove target files and recompile from scratch
#   $ make watch      # watch the filesystem for changes and recompile

##
#
# Variables
#

APP_NAME := $(shell basename $(CURDIR))
APP_DIR := application
APP_STATIC := $(APP_DIR)/static

ASSETS := assets
ASSETS_CSS := $(ASSETS)/css
ASSETS_JS := $(ASSETS)/js
ASSETS_IMG := $(ASSETS)/img
ASSETS_FONTS := $(ASSETS)/fonts

CSS_SRC := $(ASSETS_CSS)/bin
CSS_TARGET := $(APP_STATIC)/css

JS_SRC := $(ASSETS_JS)/bin
JS_TARGET := $(APP_STATIC)/js

IMG_SRC := $(ASSETS_IMG)
IMG_TARGET := $(APP_STATIC)/img

FONTS_SRC := $(ASSETS_FONTS)
FONTS_TARGET := $(APP_STATIC)/fonts

SECRETS := ~/.secrets/$(APP_NAME)/bash.export

##
#
# Targets
#
# The format goes:
#
#   target: list of dependencies
#     commands to build target
#
# If something isn't re-compiling double-check the changed file is in the
# target's dependencies list.

# Phony targets - when the target-side of a definition is just a label, not
# a file. Ensures it runs properly even if a file by the same name exists.

#
# All
#

.PHONY: all
all: setup build

#
# Setup
#

.PHONY: setup
setup: setup-secrets setup-css setup-js

.PHONY: setup-secrets
setup-secrets: $(SECRETS)

$(SECRETS):
	@mkdir -p $(@D)
	@chmod 700 $(@D)
	@touch $@
	@openssl rand -hex 32 > tmp_db_password
	@openssl rand -hex 32 > tmp_django_secret
	@echo "export POSTGRES_PASSWORD=$$(cat tmp_db_password)" >> $@
	@echo "export DJANGO_DB_PASSWORD=$$(cat tmp_db_password)" >> $@
	@echo "export DJANGO_SECRET_KEY=$$(cat tmp_django_secret)" >> $@
	@rm tmp_db_password tmp_django_secret

.PHONY: setup-css
setup-css:
	@$(MAKE) -C $(ASSETS_CSS) setup

.PHONY: setup-js
setup-js:
	@$(MAKE) -C $(ASSETS_JS) setup

#
# Build
#

.PHONY: build
build: build-css build-js build-img build-fonts

.PHONY: build-css
build-css:
	@$(MAKE) -C $(ASSETS_CSS) build
	@rsync -a $(CSS_SRC)/ $(CSS_TARGET)/

.PHONY: build-js
build-js:
	@$(MAKE) -C $(ASSETS_JS) build
	@rsync -a $(JS_SRC)/ $(JS_TARGET)/

.PHONY: build-img
build-img:
	@printf '\t%s\n' "syncing $(IMG_TARGET)..."
	@rsync -a $(IMG_SRC)/ $(IMG_TARGET)/

.PHONY: build-fonts
build-fonts:
	@printf '\t%s\n' "syncing $(FONTS_TARGET)..."
	@rsync -a $(FONTS_SRC)/ $(FONTS_TARGET)/

#
# Clean
#

.PHONY: clean
clean: clean-css clean-js clean-img clean-fonts

.PHONY: clean-css
clean-css:
	@$(MAKE) -C $(ASSETS_CSS) clean
	@printf '\t%s\n' "removing $(CSS_TARGET)..."
	@rm -rf $(CSS_TARGET)

.PHONY: clean-js
clean-js:
	@$(MAKE) -C $(ASSETS_JS) clean
	@printf '\t%s\n' "removing $(JS_TARGET)..."
	@rm -rf $(JS_TARGET)

.PHONY: clean-img
clean-img:
	@printf '\t%s\n' "removing $(IMG_TARGET)..."
	@rm -rf $(IMG_TARGET)

.PHONY: clean-fonts
clean-fonts:
	@printf '\t%s\n' "removing $(FONTS_TARGET)..."
	@rm -rf $(FONTS_TARGET)

#
# Distclean
#

.PHONY: distclean
distclean: distclean-css distclean-js distclean-img distclean-fonts

.PHONY: distclean-css
distclean-css:
	@$(MAKE) -C $(ASSETS_CSS) distclean
	@printf '\t%s\n' "removing $(CSS_TARGET)..."
	@rm -rf $(CSS_TARGET)

.PHONY: distclean-js
distclean-js:
	@$(MAKE) -C $(ASSETS_JS) distclean
	@printf '\t%s\n' "removing $(JS_TARGET)..."
	@rm -rf $(JS_TARGET)

.PHONY: distclean-img
distclean-img:
	@printf '\t%s\n' "removing $(IMG_TARGET)..."
	@rm -rf $(IMG_TARGET)

.PHONY: distclean-fonts
distclean-fonts:
	@printf '\t%s\n' "removing $(FONTS_TARGET)..."
	@rm -rf $(FONTS_TARGET)

#
# Misc
#

.PHONY: list
list:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

##
#
# Reference
#
# $@ - the target filename.
# $% - the target member name.
# $< - the filename of the first prerequisite.
# $? - space-delimited prerequisites.
# $^ - space-delimited prerequisites. Named member only for archive members.
# $+ - like $^ but prerequisites listed more than once are duplicated in the order they were listed
# $| - space-delimited order-only prerequisites.
# $* - The stem with which an implicit rule matches
# $(@D) The directory part of the file name of the target, with the trailing slash removed.
# $(@F) The file part of the file name of the target.
# $(<D) The directory part of the file name of the prerequisite, with the trailing slash removed.
# $(<F) The file part of the file name of the prerequisite.
# @ - suppress output of command.


