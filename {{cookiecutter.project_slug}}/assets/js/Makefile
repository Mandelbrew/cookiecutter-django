#@IgnoreInspection BashAddShebang
##
#
# Usage
#
#   $ make            # install dependencies and compile files
#   $ make build      # compile files
#   $ make clean      # remove target files
#   $ make distclean  # remote target and build files

##
#
# Variables
#

BIN_DIR := bin
SRC_DIR := src

SRC_EXT := js
TARGET_EXT := js

TARGET := $(BIN_DIR)/main.$(TARGET_EXT)
SRC := $(SRC_DIR)/main.$(SRC_EXT)
DEPS := $(shell find $(SRC_DIR) -type f -name '*.$(SRC_EXT)' )

NPM := npm
NPM_BIN := $(shell $(NPM) bin)

WEBPACK := $(NPM_BIN)/webpack
WEBPACK_FLAGS := --debug --devtool sourcemap --output-pathinfo

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
#
# Phony targets - when the target-side of a definition is just a label, not
# a file. Ensures it runs properly even if a file by the same name exists.

.PHONY: all
all: setup build

.PHONY: setup
setup:
	@printf '\t%s\n' "npm magic..."
	@$(NPM) install

.PHONY: build
build: $(TARGET)

.PHONY: clean
clean:
	@printf '\t%s\n' "removing $(BIN_DIR)..."
	@rm -rf $(BIN_DIR)

.PHONY: distclean
distclean: clean
	@printf '\t%s\n' "removing node_modules..."
	@rm -rf node_modules

$(TARGET): $(SRC) $(DEPS)
	@mkdir -p $(@D)
	@printf '\t%s\n' "webpack magic..."
	@$(WEBPACK) $(WEBPACK_FLAGS)

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

