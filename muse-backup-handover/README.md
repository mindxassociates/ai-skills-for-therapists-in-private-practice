# Muse 备份与交接

把一个 Muse 的人格、记忆和资料备份下来，迁移到新的 Muse 上并恢复。交接以验证问答为准：新 Muse 答对才算恢复成功。

> 本技能为 MIT 许可的开源技能（上游仓库：https://github.com/chengfeiai/muse-backup-handover），在此合集里镜像收录，方便一并取用；版权与许可见 `LICENSE`。

## 快速开始

把 `references/backup-prompt.md` 里的五步提示词直接发给你的 Muse，方括号里的内容换成自己的再发。

## 它做什么

1. 先清点，不打包：分类列出人设、身份、记忆、规则、常用提示词、技能、关键项目资料，报清单、总大小和遗漏项，等你确认再动手。
2. 写《恢复手册》：放进备份最上层，写给新的助手，含阅读顺序、合作方式、必须遵守的规则、验证问题和预期答案。
3. 打包成 AES-256 加密 ZIP：文件名带日期，密码由你在本地设置，只用英文字母、数字、符号，16 位以上。
4. 保存到 Muse 之外：目的地由你定，账号关联、上传、发送、定期任务都先征得你的同意。
5. 验证并逐项报告：正确密码能打开，错误密码打不开，解压后核对文件数与清单一致，保存到外部后核对文件名和大小。

## 安装

```sh
npx skills add https://github.com/chengfeiai/muse-backup-handover --skill muse-backup-handover
```

装完重开一次 Agent 会话。也可以手动装：

```sh
git clone https://github.com/chengfeiai/muse-backup-handover.git
cp -r muse-backup-handover ~/workspace/custom-skills/
```

## 目录结构

```text
muse-backup-handover/
  SKILL.md                                  # Skill 正文：五步方法
  skill.yaml                                # Skill 描述信息
  README.md                                 # 本文件
  LICENSE                                   # MIT
  references/
    backup-prompt.md                        # 五步提示词，可直接发给 Muse
    resurrection-letter-template.md         # 《恢复手册》模板
  scripts/
    build-backup.py                         # 打包脚本：AES-256 加密 ZIP + MANIFEST
```

## 打包脚本用法

```sh
# 先装依赖（只需要一次）
python3 -m venv /tmp/mbh-venv
/tmp/mbh-venv/bin/pip install pyzipper

# 只清点，不写 ZIP
/tmp/mbh-venv/bin/python scripts/build-backup.py \
  --out /tmp/dummy.zip --password-file /dev/null --dry-run

# 打包（密码文件只存密码一行，权限 600，与备份分开放）
/tmp/mbh-venv/bin/python scripts/build-backup.py \
  --out ~/muse-backup-YYYYMMDD.zip --password-file ~/.mbh-password

# 校验：正确密码能打开，错误密码打不开
/tmp/mbh-venv/bin/python scripts/build-backup.py \
  --verify ~/muse-backup-YYYYMMDD.zip --password-file ~/.mbh-password \
  --wrong-password-file /tmp/wrong-password.txt
```

## 安全要点

- 密码、验证码、API Key 一律不进备份、不进聊天。
- 备份不向第三方分享，不发公开链接。
- 聊天记录原文、登录态、定时任务无法迁移，新账号上需要重建。
- 打包前核对目的地剩余空间是否装得下备份，装不下先停下来报告。

## 实测记录

- 2026-11-19 空跑实测：排除构建产物与缓存后，135,558 个文件，共 41.37 GB（原始 403,058 个文件、49 GB）。
- 同日最小核心实测：142 个文件，AES-256 ZIP 生成成功，正确密码校验通过，错误密码被拒绝。
- 已知限制：免费云盘通常只有 15 GB，装不下几十 GB 的全量备份，目的地需要扩容或换地方。

## License

MIT，见 LICENSE。
