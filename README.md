# ibus2cin is a tool to export from IBus table for Boshiamy to cin table.

嘸蝦米表格版權上的問題不再贅述，但似乎並非所有版本的嘸蝦米都有附上 cin 表格，例如 Boshiamy X1 for Mac 也只有安裝後才能取出的 liu-uni*.tab，而編碼後的檔案轉換上也麻煩一點，所幸行易官方也提供了其他不同平台的輸入法，其中 IBus 所使用的輸入法參考檔為 sqlite 格式，也比較容易在不同平台上轉換，所以這篇在說明如何將 IBus 中的參考檔轉出 cin 表格備用，往後有在不同平台上使用時，要再次轉換也比較方便，而且 IBus 版本中的表格是含有 rvfs 字根的。

請閱讀表格授權聲明，也別忘記合法使用者的權利

> 本公司授權合法持有嘸蝦米輸入法 7.0 非試用版之使用者自行利用，惟使用者不得任意更改此表格中每個字的編碼規則以及本套件之任何內容，亦不得以轉換格式或片段節錄等任何方法重新散佈！此表格授權使用範圍與使用者持有之授權合約書所載範圍相同，其他未載明之事項，一律依原授權合約書內容辦理之。

## Requirements
- boshiamy-ibus.tar.gz - 請由[行易網站下載 IBus](http://boshiamy.com/member_download.php) (需登入網站會員)
- ibus2cin - 簡單的轉換程式，可由文末下載
- sqlite3 - Mac/*nix 系統大部份已內建，Windows 版本則已含在下載檔中。或請至 [sqlite.org](http://www.sqlite.org/download.html) 下載 command-line shell.

## Getting Started
boshiamy-ibus.tar.gz 解壓縮後，有四個表格參考檔，分別是:

- boshiamy_c.db - 簡體輸入，即 ,,C 模式
- boshiamy_ct.db - 繁體輸入簡體輸出，即 ,,CT 模式
- boshiamy_j.db - 日文輸入，即 ,,J 模式
- boshiamy_t.db - 繁體輸入，即 ,,T 一般模式

解壓縮 ibus2cin.zip 後，分別有以下檔案

- header.txt - cin 表格需要的設定部份
- ibus2cin.bat - 給 Windows 使用的執行檔
- ibus2cin.sh - 給 Mac/*nix 使用的執行檔
- parse.sql - 匯出使用的 sqlite3 query 命令
- sqlite3.exe - 給 Windows 使用的 sqlite3 執行檔。

## Usage
選擇你想要轉換的 IBus 參考檔，以下都以繁體輸入 boshiamy_t.db 為例。
將 boshiamy_t.db 複製到剛剛解開的 ibus2cin 資料夾中，接下來的動作都要在命令列執行。

##### Syntax
    ibus2cin IBus表格檔案名稱 產生的cin檔案名稱

##### on Mac
    sh ./ibus2cin.sh boshiamy_t.db boshiamy_t.cin

##### on Windows
    ibus2cin.bat boshiamy_t.db boshiamy_t.cin

新產生的 boshiamy_t.cin 使是所需要的 cin 表格。如果你轉換的不是一般模式的繁體，那麼在轉換後你可能會需要修改 cin 檔頭的兩個設定，或是轉換前先行修改 header.txt，兩個設定是 %ename 及 %cname 分別只是指該字根代表的輸入法的英/中文識別，並不影響輸入法的行為。 .cin 為一般的文字檔，使用任何的純文字編輯器皆可，例如記事本，存檔時請確認儲存為 UTF-8 格式。

而當然的，如果想要在 iPhone, iPad 上使用，將此檔案至 [zhim! converter](http://creativecrap.com/app/zhim-extended-dictionary-converter) 進行轉換即可。

## Troubleshooting

由於 sqlite3 需要有可寫入權限的檔案系統，所以如果在轉換時遇到下面的錯誤訊息，請除了檢查 *.db 檔案的寫入權限之外，也請檢查 ibus2cin 資料夾的寫入權限。

> file is encrypted or is not a database then most probably your code is accessing a SQLite3 database.

