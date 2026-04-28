# ibus2cin

[![GitHub release](https://img.shields.io/github/v/release/ethanliu/ibus2cin?color=green)](https://github.com/ethanliu/ibus2cin/releases/)

將行易官網提供的嘸蝦米 iBus 表格，轉換為一般通用的 CIN 表格工具程式

如果您先前曾使用 v2 之前的版本，請重新以 v2 重新產生新的 CIN 表格檔。  
舊版有兩個字根判斷錯誤，因此有些符號會無法組字。

## 使用方式

將 ibus2cin 或 ibus2cin.exe 與自行易官網下載的 iBus 檔案解壓縮後，存放於同一個資料夾。  
開啟終端機或命令列視窗，切換至此資料夾下後執行 ibus2cin，Windows 平台則是執行 ibus2cin.exe

    $ ./ibus2cin
    ibus2cin - version 2.1.0
    Convert iBus Boshiamy databases into standard .cin tables.
    Source: https://github.com/ethanliu/ibus2cin

    Usage:
    ./ibus2cin [OPTIONS] <iBus-db-file>

    Options:
    -o string
            Output file path (default "[iBus-file].cin")
    -v string
            Boshiamy cin table version (1.1 or 2.1) (default "2.1")

    Example:
    ./ibus2cin -v 2.1 -o boshiamy.cin boshiamy_t.db

### 什麼是 iBus

[iBus](https://zh.wikipedia.org/wiki/IBus) 是在 Linux 平台下的輸入法框架之一。  
例如奇摩輸入法、gcin、香草輸入法、Frankie / OkidoKey 等，分別為在不同平台下的輸入法框架，皆以使用輸入法表格檔來支援各種輸入法。

### 如何取得嘸蝦米 iBus 表格檔

請於行易官方網站，登入會員後，進入[會員下載專區](http://boshiamy.com/member_download.php)，於 Linux 支援區塊，選擇 IBus table 或 IBus (ibus-table > 1.8.0) 任一版本。
檔案下載解壓縮後，僅需副檔名為 db 的檔案，此則為 iBus 表格檔。

- boshiamy_c.db - 簡體輸入，即 ,,C 模式
- boshiamy_ct.db - 繁體輸入簡體輸出，即 ,,CT 模式
- boshiamy_j.db - 日文輸入，即 ,,J 模式
- boshiamy_t.db - 繁體輸入，即 ,,T 一般模式


### 如何區分嘸蝦米表格檔版本

於會員下載專區，點選該項目的相關資訊，再點選版本說明，即可看到嘸蝦米表格檔實際版本。   
目前行易官網所提供的版本

- boshiamy-ibus-1-8-x.tar.gz 版本 2.1
- boshiamy-ibus.tar.gz 版本 1.1

# Build

Install ming-w64 for building windows platform

    brew install ming-w64

Build with make, check Makefile for detail or `make` for usage

    make all

# Changelog

### 3.0.0

- added: python + tk

### 2.0.2 - 2020-05-25

- changed: text description and typo
- fixed: pass "Println arg list ends with redundant newline" test warning

### 2.0.1 - 2019-09-17

- changed: selkey starts from 0 instead of 1

### 2.0.0 - 2018-07

- changed: rewrite everything in Golang.
- fixed: incorrect characters
