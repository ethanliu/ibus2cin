SHELL = /bin/sh
APP_NAME = ibus2cin
DIST_DIR = dist
BIN_DIR = bin

# Force CGO off for truly static, portable binaries
export CGO_ENABLED = 0

.PHONY: all clean macos linux windows

all: clean macos linux windows

macos: darwin-arm64 darwin-amd64
linux: linux-arm64 linux-amd64
windows: win-arm64 win-amd64

# macOS
darwin-arm64: tidy
	$(call build_go,darwin,arm64,)
darwin-amd64: tidy
	$(call build_go,darwin,amd64,)

# Linux
linux-arm64: tidy
	$(call build_go,linux,arm64,)
linux-amd64: tidy
	$(call build_go,linux,amd64,)

# Windows
win-arm64: tidy
	$(call build_go,windows,arm64,.exe)
win-amd64: tidy
	$(call build_go,windows,amd64,.exe)

define build_go
	$(eval OS := $(1))
	$(eval ARCH := $(2))
	$(eval EXT := $(3))
	@echo "Building $(OS)-$(ARCH)..."
	@[ -d "$(BIN_DIR)" ] || mkdir -p "$(BIN_DIR)"
	@[ -d "$(DIST_DIR)" ] || mkdir -p "$(DIST_DIR)"
	GOOS=$(OS) GOARCH=$(ARCH) go build -trimpath -o $(BIN_DIR)/$(APP_NAME)$(EXT)
	tar zcf $(DIST_DIR)/$(APP_NAME)-$(OS)-$(ARCH).tar.gz -C $(BIN_DIR) $(APP_NAME)$(EXT)
endef

tidy:
	go mod tidy
	go mod download

clean:
	@-rm -fr $(BIN_DIR)/*
	@-rm -fr $(DIST_DIR)/*