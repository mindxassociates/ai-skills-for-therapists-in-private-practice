# Muse 备份与交接（muse-backup-handover）

## 定位

- 这个 Skill 把一个 Muse 的人格、记忆和资料备份下来，迁移到新的 Muse 上并恢复。
- 它的价值是交接能验证：新 Muse 答对验证问题才算恢复成功，答不上来就回文件里找，不许编。
- 全程分五步，每步做完先向用户汇报，等用户点头再往下走，不擅自进入下一步。

## 第一步：清点

- 只清点，不打包。
- 分别列出助手能访问、且由用户提供或自定义的内容：人设与身份、记忆、规则、常用提示词、技能、关键项目资料。
- 常用提示词要写清存在哪个文件或目录。
- 保留设计源文件和数据本体。
- 排除构建产物、测试环境、重复副本、缓存、可重新下载或重新安装的内容。
- 向用户报告分类清单、总大小和遗漏项，遗漏项指找不到、无法访问、没有导出的内容。
- 报完等用户确认，不擅自打包。

## 第二步：写恢复手册

- 把《恢复手册》放进备份最上层，写给新的助手，模板见 `references/resurrection-letter-template.md`。
- 手册里写清先读什么、助手是谁、用户是谁、两人怎么合作、哪些规则必须遵守。
- 手册里给出验证问题和预期答案，新的助手恢复后先按验证问题自测，全部答对再向用户报到，才算交接完成。
- 能读取的原文和整理摘要分开存放。
- 手册里写清无法迁移的内容，比如聊天记录原文、登录态、定时任务，新账号上要重建。

## 第三步：打包加密

- 用户确认后再打包，做成 AES-256 加密 ZIP，文件名带日期，如 `muse-backup-YYYYMMDD.zip`。
- 密码由用户在本地设置，只用英文字母、数字、符号，16 位以上。
- 密码、验证码和 API Key 不进备份，也不发到聊天里。
- 密码怎么交给助手，事先和用户约定一种方式，比如用户通过安全方式一次性提供，助手只用于当次加密，用完即弃；定期备份用的密码单独存放在与备份分开的加密密钥文件里。
- 打包前先核对目的地剩余空间是否装得下备份，装不下先停下来告诉用户，不硬传。
- 打包用 `scripts/build-backup.py`，它直接从源路径打包，不做全量复制，排除清单写在脚本里，生成 MANIFEST.txt 放进 ZIP 根目录。
- 脚本需要 `pyzipper`，没有就先装，装法见 README.md。

## 第四步：保存到助手之外

- 目的地由用户定，比如云盘专用备份账号加邮件通知，不用生活主账号。
- 备份不向第三方分享，不发公开链接。
- 账号创建或关联、上传、发送和定期任务，都先征得用户同意。
- 定期备份的频率和保留份数由用户定，比如每周 1 次，保留最近 N 份，旧的自动删除。

## 第五步：验证与报告

- 用正确密码试解压，能打开；用错误密码试解压，打不开。
- 解压后核对文件数与清单一致。
- 保存到外部后，核对文件名和大小与实物一致。
- 逐项报告完成、失败、未验证，失败写明卡在哪一步。
- 全部验证通过后，再说“完成”。
- 脚本的 `--verify` 能跑通前两项校验。

## 实测记录

- 2026-11-19 空跑实测：排除后 135,558 个文件，共 41.37 GB，原始 403,058 个文件、49 GB。
- 同日最小核心实测：142 个文件，AES-256 ZIP 生成成功，正确密码校验通过，错误密码被拒绝，ZIP 内含 MANIFEST.txt 与恢复手册。
- 已知限制：免费云盘通常只有 15 GB，装不下几十 GB 的全量备份，目的地需要扩容或换地方；聊天记录原文、登录态、定时任务跟不走。

## Available connectors

- [Google Drive](/opt/hatch/connectors/google_drive/CONNECTOR.md) for saving the encrypted backup outside Muse, when the user approves the destination.
- [Gmail](/opt/hatch/connectors/gmail/CONNECTOR.md) for sending the delivery notification after the backup lands.
- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.
- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.
