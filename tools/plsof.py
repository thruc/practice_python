import os
import sys
import re

TCP_PROC_FILE="/proc/net/tcp"

def get_inode(hx):
    """
    渡されたポートを使用しているソケットファイルを特定しinodeを返却する
    """
    inode_num = 0
    with open(TCP_PROC_FILE, mode="r") as fd:
        for line in fd:
            ll = line.strip().split()[1].split(":")
            if len(ll) == 1:
                continue
            if hx == int(ll[1], 16):
                inode_num = line.strip().split()[9]
    return inode_num if inode_num else None


def get_dir_list(path):
    """
    渡されたパス配下のディレクトリをリストで返す
    """
    files = os.listdir(path)
    return [f for f in files if os.path.isdir(os.path.join(path, f))]


def get_hardlink_list(proc_dir_list, inode_num):
    for path in proc_dir_list:
        for files in os.listdir(f"/proc/{path}/fd"):
            try:
                r = os.readlink(f"/proc/{path}/fd/{files}")
                if "socket" in r and r[8:-1] == inode_num:
                    print(path, r, r[8:-1])
            except FileNotFoundError as e:
                # Todo : エラー処理
                pass


def main(argv):
    pattern = "[0-9]*$"
    inode_num = get_inode(int(argv[1]))
    if inode_num is None:
        print("but port")
        sys.exit(1)

    path = "/proc/"
    proc_dir_list = [f for f in get_dir_list(path) if re.match(pattern, f)]
    l = get_hardlink_list(proc_dir_list, inode_num)


if __name__ == "__main__":
    main(sys.argv)
