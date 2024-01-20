
# ストップウォッチ

意外とストップウォッチだけのアプリが無かったため、作成いたしました。このアプリではhhhh:mm:ss表示になっています。(最近のアプリは24時間を超えてから1dとなる)

# DEMO

![image](https://github.com/mizugamiaqua/stopwatch/assets/77522368/60fe594e-2451-4f00-80a4-87d43ca32803)


# Features

Point1:何と言っても9999時間99分59までカウントできること！意外と他のアプリだと、24時間経つと1dというような表示になるので時間を測りたい方はおすすめです。
Point2:アプリを消しても再度起動すると、続きからになります。
Point3:時間が保存されているのはtxtファイル！そのため、始めたい時間を自分で変更できます。

# Requirement

tkinter(tk)
time
threading
pyinstaller(.exe化する場合) 

# Installation

##ライブラリのインストール方法

Pythonのパッケージをインストールする際に"tcl/tk and IDEL"にチェックを入れておく！
time,threadingは標準ライブラリです。

```
pip install pyinstaller
```

# Usage

実行方法

```bash
python stopwatch.py
```

# Note

pyinstallerで起動するときは不要なライブラリを追加しないようにしましょう。

# Author

作成情報を列挙する

* 作成者:Syosei
* Twitter:@mizugamiaqua
