/* 
    ja_langdata.hpp
    English language pack of DetExploit.
    DetExploit (https://github.com/moppoi5168/DetExploit)
    Licensed by GPL License
*/

#define WELCOME_MESSAGE "   Hello, W0rld!! DetExploit v1.4-alphaへようこそ！ :D"

/* Used in exploitdb.py */
#define EXPLOITDB_DOWNLOAD_INTRO "   ExploitDBから脆弱性情報をダウンロードしています。"
#define EXPLOITDB_DOWNLOAD_SUCCESS "   ダウンロード完了。"
#define EXPLOITDB_DOWNLOAD_FAILED "   エラー: ExploitDBの脆弱性情報ダウンロードが失敗しました。"
#define EXPLOITDB_EXTRACT_WIN "   次のファイルからWindows環境の脆弱性のみを抽出しています: "
#define EXPLOITDB_EXTRACT_SUCCESS "   抽出に成功しました。"

/* Used in jvn.py */
#define JVN_DOWNLOAD_INTRO "   JVNから脆弱性情報をダウンロードしています。"
#define JVN_DOWNLOAD_ALERT_ONE "   この処理には時間がかかる可能性があります。"
#define JVN_DOWNLOAD_ALERT_TWO "   プログラムを終了しないでください。"
#define JVN_DOWNLOAD_PROGRESS "   ダウンロード成功: "
#define JVN_DOWNLOAD_SUCCESS "   ダウンロード完了。"

/* Used in nvd.py */
#define NVD_DOWNLOAD_INTRO "   NVDから脆弱性情報をダウンロードしています。"
#define NVD_DOWNLOAD_SUCCESS "   ダウンロード完了。"

/* Used in winupdate.py */
#define WINUPD_SCAN_INTRO "   インストールされていないアップデートを検索しています。"

/* Used in * (Scan Phase) */
#define DETECT_ALERT "   << 警告 :: 脆弱なアプリケーションを検知しました >>"
#define DETECT_UPDATE_ALERT "   << 警告 :: インストールされていないWindows Updateを検知しました >>"
#define APP_NAME "   << アプリケーション名: "
#define APP_VERSION "   << アプリケーションのバージョン:"
#define UPDATE_NAME "   << アップデート名:  "
#define DETECT_USING_EXPLOITDB "   << 使用したデータベース: ExploitDB >>"
#define DETECT_USING_JVN "   << 使用したデータベース: Japan Vulnerability Notes >>"
#define DETECT_USING_NVD "   << 使用したデータベース: National Vulnerability Database >>"
#define OBJECT_LEVEL "   << オブジェクトレベル:"

/* Used in report.py */
#define LEVEL_DANGER "危険"
#define LEVEL_WARNING "警告"
#define LEVEL_CAUTION "注意"
#define EDB "ExploitDB"
#define JVN "JVN"
#define NVD "NVD"
#define REPORT_FORMAT_READ_ERROR_ONE "エラー: スキャンレポート出力方式が正しく設定されていません。config.iniを確認してください。"
#define REPORT_FORMAT_READ_ERROR_TWO "エラー: 初期値(HTML)が使用されます。"
#define REPORT_OUTPUT_INFO_ONE "   レポートは次のファイルに正常に出力されました: ../reports/detexploit_report_"
#define REPORT_OUTPUT_INFO_TWO " "


/* GUI */
#define FIRST_MSG "スキャンボタンをクリックしてスタートしてください。"
#define OP_START "オペレーションが開始しました。"
#define EXPLOITDB_EXTRACT_GUI "Windowsの脆弱性をデータから抽出しています。"
#define EXPLOITDB_PARSE "ExploitDB脆弱性データを解析しています。"
#define WMI_APP_RET "WMIからアプリケーション情報を取得しています。"
#define REG_APP_RET "レジストリからアプリケーション情報を取得しています。"
#define SCAN_MSG_ONE "外部の情報とローカルマシンの情報を使用してスキャンしています。"
#define SCAN_MSG_TWO "未適用のWindows Updateを検索しています。"
#define SCAN_END "完了。"
#define GEN_REPORT "指定されたフォーマットでレポートを出力中。"

#define RESONE "   結果: "
#define RESTWO " 個の脆弱なアプリケーション、未インストールのアップデートが検知されました。"

#define LANGPACK_SIGNATURE "DetExploit Japanese LP"
