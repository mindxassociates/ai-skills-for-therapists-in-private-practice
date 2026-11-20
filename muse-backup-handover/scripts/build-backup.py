#!/usr/bin/env python3
"""Muse 备份与交接：全量打包脚本（核心 + 项目 + 全部媒体）

用法：
  build-backup.py --out <zip路径> --password-file <密码文件> [--core-only] [--dry-run]
  build-backup.py --verify <zip路径> --password-file <密码文件> [--wrong-password-file <错密码文件>]

要点：
- 直接从源路径打包，不做全量复制；排除构建产物、验证环境、重复工作副本。
- AES-256 加密（pyzipper WZ_AES），ZIP64，文件名 UTF-8。
- 密码只从 --password-file 读（专用密钥文件，600 权限，与备份分开放），
  绝不写进日志、MANIFEST、记忆或邮件；脚本不打印密码。
- 生成 MANIFEST.txt（放进 ZIP 根目录）：日期、范围、排除清单、文件数、
  总字节数、分目录大小、完整文件清单（相对路径 + 字节数）。
- 恢复手册默认取本 Skill 的 references/resurrection-letter-template.md，
  也可用 --letter 指定已按用户情况写好的那份。

依赖：pyzipper（没有就先装：python3 -m venv /tmp/mbh-venv
  && /tmp/mbh-venv/bin/pip install pyzipper）。
"""
import argparse
import datetime
import os
import sys

try:
    import pyzipper
except ImportError:
    print("缺少 pyzipper，请先装：python3 -m venv /tmp/mbh-venv && "
          "/tmp/mbh-venv/bin/pip install pyzipper", file=sys.stderr)
    raise SystemExit(2)

HOME = os.path.expanduser("~")
SKILL_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_LETTER = os.path.join(SKILL_ROOT, "references", "resurrection-letter-template.md")

# 排除：目录名（任意层级）
EXCLUDE_DIRS = {
    "node_modules", "__pycache__", ".venv", "venv", ".cache", ".git",
    ".agent-desktop", "agents",  # 运行期 agent 目录
    "backup-resurrection",       # 备份工作目录本身（venv/脚本/中间产物不进备份）
    "browser_downloads",         # 可重新下载的浏览器下载物
}
# 排除：顶层 workspace 子目录（构建产物/验证环境/可重装物）
EXCLUDE_TOP = {
    "fw-venv", "asr-venv", "nodes",  # venv 与节点二进制
}
# 排除：文件后缀与文件名
EXCLUDE_SUFFIXES = (".pyc", ".pyo", ".DS_Store",)
EXCLUDE_FILES = {"Thumbs.db", ".DS_Store"}
# 连接器安装包与二进制：只留文档与配置
EXCLUDE_CONNECTOR_SUBDIRS = {"app", "extracted"}
EXCLUDE_BINARY_SUFFIXES = (".deb", ".so", ".dylib", ".dll", ".exe", ".pth.tar")


def is_excluded(rel_path, is_dir):
    """rel_path：相对家目录的路径，如 workspace/custom-skills/x 或 MEMORY.md"""
    parts = rel_path.split(os.sep)
    name = parts[-1]
    if is_dir and name in EXCLUDE_DIRS:
        return True
    if len(parts) >= 2 and parts[0] == "workspace" and parts[1] in EXCLUDE_TOP:
        return True
    if "custom-connectors" in parts:
        if is_dir and name in EXCLUDE_CONNECTOR_SUBDIRS:
            return True
        if not is_dir and name.endswith(EXCLUDE_BINARY_SUFFIXES):
            return True
    if not is_dir:
        if name in EXCLUDE_FILES or name.endswith(EXCLUDE_SUFFIXES):
            return True
    return False


def collect(core_only=False, letter=None):
    """返回 [(磁盘绝对路径, zip内相对路径)]，已按排除清单过滤、按路径排序。"""
    items = []
    core_files = ["SOUL.md", "IDENTITY.md", "AGENTS.md", "USER.md", "MEMORY.md",
                  "TOOLS.md", "PROACTIVE_PREFERENCES.md"]
    for f in core_files:
        p = os.path.join(HOME, f)
        if os.path.exists(p):
            items.append((p, os.path.join("core", f)))
    for d in ["dreams", "memory"]:
        root = os.path.join(HOME, d)
        if not os.path.isdir(root):
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = sorted(x for x in dirnames
                                 if not is_excluded(os.path.relpath(os.path.join(dirpath, x), HOME), True))
            for fn in sorted(filenames):
                p = os.path.join(dirpath, fn)
                rel = os.path.relpath(p, HOME)
                if not is_excluded(rel, False):
                    items.append((p, os.path.join("core", rel)))
    letter = letter or DEFAULT_LETTER
    if letter and os.path.exists(letter):
        items.append((letter, "RESURRECTION-LETTER.md"))
    elif letter:
        print(f"恢复手册不存在，已跳过：{letter}", file=sys.stderr)
    if not core_only:
        root = os.path.join(HOME, "workspace")
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = sorted(x for x in dirnames
                                 if not is_excluded(os.path.relpath(os.path.join(dirpath, x), HOME), True))
            for fn in sorted(filenames):
                p = os.path.join(dirpath, fn)
                rel = os.path.relpath(p, HOME)
                if not is_excluded(rel, False):
                    items.append((p, rel))
    items.sort(key=lambda t: t[1])
    return items


def build_manifest(items, core_only):
    total = 0
    per_top = {}
    lines = []
    lines.append("Muse 备份 MANIFEST")
    lines.append(f"生成时间：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"范围：{'最小核心' if core_only else '全量（核心+项目+全部媒体）'}")
    lines.append("排除：node_modules / __pycache__ / .venv / venv / .cache / .git / agents 运行目录 /")
    lines.append("      browser_downloads / fw-venv / asr-venv / nodes / 连接器安装包与二进制（.deb/.so等）/")
    lines.append("      backup-resurrection 工作目录本身 / .pyc / .DS_Store / Thumbs.db")
    lines.append("加密：AES-256（WZ_AES），ZIP64，文件名 UTF-8")
    lines.append("恢复顺序：先读 RESURRECTION-LETTER.md，再按信中顺序读 core/ 与 workspace/")
    lines.append("")
    for src, arc in items:
        try:
            size = os.path.getsize(src)
        except OSError:
            size = -1
        total += max(size, 0)
        top = arc.split(os.sep)[0]
        per_top[top] = per_top.get(top, 0) + max(size, 0)
        lines.append(f"{size}\t{arc}")
    lines.append("")
    lines.append(f"文件数：{len(items)}")
    lines.append(f"总字节数：{total}（约 {total / 1024 / 1024 / 1024:.2f} GB）")
    lines.append("分目录大小（字节）：")
    for top in sorted(per_top):
        lines.append(f"  {top}: {per_top[top]}（约 {per_top[top] / 1024 / 1024:.2f} MB）")
    return "\n".join(lines) + "\n", len(items), total


def read_password(path):
    with open(path, "r", encoding="utf-8") as f:
        pw = f.read().strip()
    if not pw:
        raise SystemExit("密码文件为空")
    if any(ord(c) > 127 for c in pw):
        raise SystemExit("密码含非 ASCII 字符：为避免 Windows 乱码，请只用英文字母、数字、符号")
    return pw.encode("utf-8")


def do_build(args):
    items = collect(core_only=args.core_only, letter=args.letter)
    manifest, count, total = build_manifest(items, args.core_only)
    print(f"待打包：{count} 个文件，共约 {total / 1024 / 1024 / 1024:.2f} GB")
    if args.dry_run:
        print("dry-run：只清点，不写 ZIP")
        print(f"文件数：{count}\n总字节数：{total}")
        return
    pw = read_password(args.password_file)
    out = args.out
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    with pyzipper.AESZipFile(out, "w", compression=pyzipper.ZIP_DEFLATED,
                             encryption=pyzipper.WZ_AES) as zf:
        zf.setpassword(pw)
        zf.writestr("MANIFEST.txt", manifest.encode("utf-8"))
        done = 0
        for src, arc in items:
            try:
                zf.write(src, arc)
            except OSError as e:
                print(f"跳过无法读取：{arc}（{e}）", file=sys.stderr)
                continue
            done += 1
            if done % 20000 == 0:
                print(f"  已写入 {done}/{count} ...")
    print(f"完成：{out}（{count} 个文件，清单见 ZIP 内 MANIFEST.txt）")
    print(f"实物大小：{os.path.getsize(out)} 字节")


def do_verify(args):
    pw = read_password(args.password_file)
    with pyzipper.AESZipFile(args.verify) as zf:
        zf.setpassword(pw)
        bad = zf.testzip()
        names = zf.namelist()
        print(f"正确密码：testzip 通过（坏文件：{bad}），共 {len(names)} 个条目，"
              f"含 MANIFEST.txt：{'MANIFEST.txt' in names}，"
              f"含 RESURRECTION-LETTER.md：{'RESURRECTION-LETTER.md' in names}")
        sample = zf.read("MANIFEST.txt")[:200].decode("utf-8", "replace")
        print("MANIFEST 开头：", sample.splitlines()[0] if sample else "(空)")
    if args.wrong_password_file:
        wrong = read_password(args.wrong_password_file)
        try:
            with pyzipper.AESZipFile(args.verify) as zf:
                zf.setpassword(wrong)
                zf.read("MANIFEST.txt")
            print("错误密码：仍能打开——校验失败！")
            raise SystemExit(1)
        except RuntimeError:
            print("错误密码：被拒绝（符合预期）")
        except Exception as e:
            print(f"错误密码：被拒绝（{type(e).__name__}，符合预期）")


def main():
    ap = argparse.ArgumentParser(description="Muse 备份与交接打包脚本")
    ap.add_argument("--out", help="输出 ZIP 路径")
    ap.add_argument("--password-file", help="密码文件路径（专用密钥文件）")
    ap.add_argument("--letter", help="恢复手册路径（默认用本 Skill 的模板）")
    ap.add_argument("--core-only", action="store_true", help="只打包最小核心，用于测试")
    ap.add_argument("--dry-run", action="store_true", help="只清点，不写 ZIP")
    ap.add_argument("--verify", help="校验已生成的 ZIP 路径")
    ap.add_argument("--wrong-password-file", help="错误密码文件（校验用）")
    args = ap.parse_args()
    if args.verify:
        if not args.password_file:
            ap.error("--verify 需要 --password-file")
        do_verify(args)
    else:
        if not args.out or not args.password_file:
            ap.error("打包需要 --out 与 --password-file")
        do_build(args)


if __name__ == "__main__":
    main()
