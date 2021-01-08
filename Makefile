SHELL = /bin/sh

.PHONY: usage all clean

default: usage

all: clean x86 amd64

x86: clean darwin386 linux386 win386
	@make cleanbin

amd64: clean darwin linux win
	@make cleanbin

usage:
	@echo "make [OPTION]"
	@echo
	@echo "OPTIONS:"
	@echo "	all - Bull x86 and amd64 arch"
	@echo "	x86 - Build ony 386 arch"
	@echo "	amd64 - Build only amd64 arch"

config:
	@[ -d "bin" ] || mkdir -p "bin"
	@[ -d "dist" ] || mkdir -p "dist"

clean: config cleanbin
	@-rm -fr dist/*

cleanbin:
	@-rm -fr bin/*

darwin386:
	$(call build,darwin,386)

darwin:
	$(call build,darwin,amd64)

linux386:
	$(call build,linux,386)

linux:
	$(call build,linux,amd64)

win386:
	$(info Building windows-x86)
	@GOOS=windows GOARCH=386 CGO_ENABLED=1 CC=/usr/local/opt/mingw-w64/bin/i686-w64-mingw32-gcc go build -o bin/ibus2cin.exe
	@tar zcf dist/ibus2cin-windows-386.tar.gz -C bin ibus2cin.exe

win:
	$(info Building windows-amd64)
	@GOOS=windows GOARCH=amd64 CGO_ENABLED=1 CC=/usr/local/opt/mingw-w64/bin/x86_64-w64-mingw32-gcc go build -o bin/ibus2cin.exe
	@tar zcf dist/ibus2cin-windows-amd64.tar.gz -C bin ibus2cin.exe

define build
	$(eval OS := $(1))
	$(eval ARCH := $(2))
	$(info Building ${OS}-${ARCH})
	@GOOS=${OS} GOARCH=${ARCH} go build -o bin/ibus2cin
	@tar zcf dist/ibus2cin-${OS}-${ARCH}.tar.gz -C bin ibus2cin
endef

