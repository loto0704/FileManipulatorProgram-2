import sys
from collections import namedtuple
import shutil


def main() -> None:
    args = get_argv()  # 引数取得

    if args.command == "reverse":
        """逆順にしてエクスポート"""
        with open(args.input_path, "r", encoding="utf-8") as rf:
            f_string = rf.read()

        with open(args.output_path, "w", encoding="utf-8") as wf:
            wf.write(f_string[::-1])

    elif args.command == "copy":
        """ファイルコピー"""
        shutil.copyfile(args.input_path, args.output_path)
        return

    elif args.command == "duplicate-contents":
        """Inputファイルの内容をN回複製して追記"""
        with open(args.input_path, "r", encoding="utf-8") as rf:
            f_string = rf.read()

        strs = []
        for i in range(args.number):
            strs.append(f_string)

        with open(args.input_path, "a", encoding="utf-8") as wf:
            wf.write("\n")
            wf.write("\n".join(strs))

    elif args.command == "replace-string":
        """特定文字列を置換して上書き"""
        with open(args.input_path, "r", encoding="utf-8") as rf:
            f_string = rf.read()

        w_string = f_string.replace(args.old_str, args.new_str)

        with open(args.input_path, "w", encoding="utf-8") as wf:
            wf.write(w_string)


def get_argv() -> namedtuple:
    """引数を整理"""
    CommandLineArgs = namedtuple("CommandLineArgs",
                                 ["command", "input_path", "output_path", "number", "old_str", "new_str"])
    command = sys.argv[1]

    if command == "reverse" or command == "copy":
        cmd_args = CommandLineArgs(command=command, input_path=sys.argv[2], output_path=sys.argv[3], number="",
                                   old_str="", new_str="")
    elif command == "duplicate-contents":
        cmd_args = CommandLineArgs(command=command, input_path=sys.argv[2], output_path="", number=int(sys.argv[3]),
                                   old_str="", new_str="")
    elif command == "replace-string":
        cmd_args = CommandLineArgs(command=command, input_path=sys.argv[2], output_path="", number="",
                                   old_str=sys.argv[3], new_str=sys.argv[4])
    else:
        print("第一引数がヒットしませんでした。再起動してやり直してください。")
        sys.exit()

    return cmd_args


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("引数が指定されてません。引数を指定してから再度実行してください。")
        sys.exit()

    main()
