# DetExploit v0.7α

![ScreenShot1](sshot.jpg)

** DetExploit v0.6αのスクリーンショット **

[English Version README is right here (英語版のREADMEを表示)](README.md)

## 目次

<!-- TOC -->

- [DetExploit v0.7α](#detexploit-v07α)
    - [目次](#目次)
    - [概要](#概要)
    - [デモ](#デモ)
    - [実行に必要なライブラリ等](#実行に必要なライブラリ等)
    - [実行方法](#実行方法)
    - [サポートしているデータベース](#サポートしているデータベース)
    - [ライセンス](#ライセンス)
    - [開発者へ連絡](#開発者へ連絡)

<!-- /TOC -->

## 概要

DetExploitはシステム上に存在する脆弱なアプリケーションを検知して、ユーザーに通知するソフトウェアです。

近年のサイバー攻撃で使用されるほとんどの脆弱性が一年以上前に攻撃コードなどが公開されているものだというのは皆さんご存知だと思います。

そんな状況ならば未知の脅威に対処するための技術よりも既知の脅威に対処するための技術が発展するべきだと私は考えました。

本プロジェクトは採択されれば私の[未踏ジュニア](https://jr.mitou.org/)のテーマ作品になる予定です。

私は本プロジェクトが発展して、大規模なOSSになることを願い開発を続けていきます。

## デモ

+ デモ映像 (v0.5, クリックするとYouTubeにジャンプします)

[![Alt text](https://img.youtube.com/vi/aIMhaA_ysUY/0.jpg)](https://www.youtube.com/watch?v=aIMhaA_ysUY)

## 実行に必要なライブラリ等

+ Windows環境 (Windows 10でテスト済み)
+ Python 3.x (Python 3.7でテスト済み)
+ requirements.txtに書かれているモジュール (pip install -r requirements.txt)
+ [Win32Com (PyWin32: Python for Windows extensions)](https://github.com/mhammond/pywin32/releases)

## 実行方法

ビルドした実行形式のファイルは現在配布していません。 
正式リリース版の公開と同時に配布を開始する予定です。

```
# 依存するライブラリ等のインストール
C:\path\to\DetExlopit>pip install -r requirements.txt
# CUI版の実行 (PATHの設定が必要です)
C:\path\to\DetExlopit>python main.py
# GUI版の実行 (PATHの設定が必要です)
C:\path\to\DetExploit>python gui.py
```

## サポートしているデータベース

+ [ExploitDB](exploit-db.com/)
+ [JVN (Japan Vulnerability Notes)](https://jvn.jp/)
+ 随時追加予定

## ライセンス

GPL License

## 開発者へ連絡

+ MOPI (Email: [moppoi5168@gmail.com](mailto:moppoi5168@gmail.com) / Twitter: [@naogramer](https://twitter.com/naogramer))
