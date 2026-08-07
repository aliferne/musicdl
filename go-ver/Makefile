#####################
# sources
#####################
BUILD_DIR=build
CORE_DIR=core WEB_DIR=web
TUI_DIR=tui
BINARY=$(BUILD_DIR)/musicdl
GOENTRY=main.go

GOSRC += $(GOENTRY)

#####################
# build cmds & flags
#####################
# NOTE: requires input to configure maybe, especially for android, CGO_ENABLED should be 1
GOOS=linux
GOARCH=amd64

GORUN=go run
GOBUILD=go build -o
GOTEST=go test

#####################
# cmds
#####################
.PHONY: all build run test

all: build

build:
	mkdir -p $(BUILD_DIR)
	GOOS=$(GOOS) GOARCH=$(GOARCH) $(GOBUILD) $(BINARY) $(GOSRC)

run:
	mkdir -p $(BUILD_DIR)
	GOOS=$(GOOS) GOARCH=$(GOARCH) $(GORUN) $(GOENTRY)

test:
	@echo "test"
