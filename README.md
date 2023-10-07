# FileManipulatorProgram-2

「File Manipulator Program(2)」の問題の解答・サンプルプログラム

問題URL：[https://recursionist.io/dashboard/course/21/lesson/1086](https://recursionist.io/dashboard/course/21/lesson/1086)

## 起動時の引数指定方法
- `reverse inputpath outputpath`: inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成します。 
- `copy inputpath outputpath`: inputpath にあるファイルのコピーを作成し、outputpath として保存します。 
- `duplicate-contents inputpath n`: inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製します。 
- `replace-string inputpath needle newstring`: inputpath にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換えます。

※起動時の引数について入力されているかのみチェックしてます。（基本的にInputファイルのパス等は合ってるものと処理してます。）
