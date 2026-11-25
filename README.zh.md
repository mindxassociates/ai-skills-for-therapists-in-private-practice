# 私人执业心理咨询师 AI 技能集

[English](README.md) | 中文版

这是一套为个人执业和团体执业的心理咨询师准备的、可复用的 AI 智能体技能（skills），共 21 个。每个技能都是一个独立的文件夹，你可以把它交给自己的 AI 智能体（Muse、ChatGPT，或任何能读取 Markdown 文件的智能体）——智能体会按照文件夹里的操作手册，用你自己的账号、你自己的数据、你自己的配置来完成工作。

本仓库不包含任何真实机构的经营数据。每个技能发布前都经过脱敏处理：没有姓名、邮箱、账号 ID、收费标准，也没有任何来访者信息。

## 最快的使用方式：把本仓库链接粘贴给你的 AI 智能体

你不需要自己下载任何文件。**复制本仓库链接 `https://github.com/mindxassociates/ai-skills-for-therapists-in-private-practice`，粘贴给你的 AI 智能体，并告诉它你想用哪个技能**，例如：

> “用这个仓库里的 Solo Consult Booking Kit（个人执业版初步咨询预约）帮我搭建预约系统：https://github.com/mindxassociates/ai-skills-for-therapists-in-private-practice”

有能力的智能体会自己抓取技能、阅读其中的 `SKILL.md`、和你完成设置访谈，然后动手搭建。下面的下载方式适用于智能体无法抓取链接、或你更愿意自己处理文件的情况。

## 免费自助使用 —— 也可以付费请人安装

本仓库的每个技能都可以**免费**自助使用，没有期限。技能本身就是写给 AI 智能体带你一步步完成的。

如果你不想自己动手，也可以付费请开发这套技能的机构团队**亲手为你安装**：在你自己的账号里、按你自己的配置完成搭建，测试通过后交付给你使用。费用取决于你选择的技能和机构规模——请加入 [Mind X社区](https://community.mindx.us/)，或通过 [mindx.us](https://mindx.us/) 联系我们，了解安装服务。

## 如何下载某个技能（zip 压缩包）

**下载整套合集：** 在本页面点击绿色的 **Code** 按钮 → **Download ZIP**。解压后，里面的每一个文件夹就是一个完整的技能。

**只下载一个技能：** GitHub 没有提供按文件夹下载的按钮，可以用以下任一方式：

1. **最简单——文件夹下载小工具：** 打开该技能的文件夹（见下方表格中的链接），复制浏览器地址栏里的地址，粘贴到 [download-directory.github.io](https://download-directory.github.io/)，它会生成只包含该文件夹的 zip 压缩包。
2. **用 Git：** `git clone https://github.com/mindxassociates/ai-skills-for-therapists-in-private-practice.git` —— 然后只保留你需要的那一个文件夹，其余删掉即可。
3. **让你的 AI 智能体来下载：** 把技能文件夹的 GitHub 链接发给你的智能体，说“把这个文件夹下载为 zip”——大多数编程类智能体都能完成。

下载后，把**解压后的整个文件夹**（包括其中的 `references` 子文件夹，一个文件都不要少）交给你的 AI 智能体——见下方“如何使用技能”。

## 技能一览

| 技能 | 功能简介 |
|---|---|
| [Solo Consult Booking Kit](solo-consult-booking-kit/)（个人执业版初步咨询预约） | 为**个人执业**的咨询师搭建一套支持 HIPAA 合规要求的初步咨询预约系统，基于 Google Workspace + Apps Script：公开预约页面、空闲时间管理、咨询控制台，不需要为预约平台按月付费。从文件夹里的 `README.md` 开始，或把 `PROMPT.md` 粘贴给你的智能体。 |
| [Group Consult Booking Kit](group-consult-booking-kit/)（团体执业版初步咨询预约） | 预约系统的**团体执业**版本：一个公开预约页面，按执业州、保险签约、语言和年龄组把潜在来访者分流给合适的咨询师；另有咨询师自助应用和管理控制台。从 `README.md` 或 `PROMPT.md` 开始。 |
| [Practice Books Kit](practice-books-kit/)（机构账目） | 心理咨询机构的记账 + 薪酬发放：把银行/信用卡账单交给你的智能体，它会把每一笔交易归类到一套专为咨询师设计的收支类别中，生成月度损益表（P&L)，并给出一份可视化财务 + 薪酬应用的规格说明，让智能体为你搭建。 |
| [Practice CRM Kit](practice-crm-kit/)（客户线索管理） | 为心理咨询机构打造的线索（潜在来访者）跟踪 CRM：流程看板（新建 → 已联系 → 已预约咨询 → 已完成咨询 → 已发送入组材料 → 已开始咨询，并设有“不匹配 / 已婉拒 / 无回应 / 已转介”等真实出口）、从预约系统、咨询结果表、网站表单和每小时邮箱自动导入线索、每条线索自带跟进事项与到期日，并区分团体角色权限——管理员可见全部，咨询师只能看到分配给自己的线索，且备注字段在服务器端即被剥离。系统内不放任何临床记录，也不自动向外发送消息。从 `README.md` 或 `PROMPT.md` 开始。 |
| [Therapist ISO Tracker](therapist-iso-tracker/)（求推荐帖追踪） | 扫描你加入的 Facebook 咨询师群组里的 “ISO”（征求推荐）来访者帖子，按你的档案（所在州、服务人群、保险、专长）进行匹配，并起草可直接复制粘贴的回复，由你本人发布。严格只读——它不会替你发帖、评论或发消息。先填写 `config.md` 和 `references/provider-profile.md`。 |
| [Referral Network Kit](referral-network-kit/)（转介网络） | 在 Google Workspace + Apps Script 上搭建一个“活的”转介目录：一张推荐同行电子表格，实时渲染为公开、可搜索的目录页面（照片卡片、筛选、一键复制咨询师信息方便粘贴到转介消息中），外加供本机构咨询师使用的内部添加表单和可选的公开“求推荐”表单——带姓名防重复校验，每次提交都会给管理员发邮件通知。从 `README.md` 或 `PROMPT.md` 开始。 |
| [Secure Messages Kit](secure-messages-kit/)（安全消息门户） | 一套归你自己所有的安全消息门户，替代按月付费的安全通讯订阅：来访者用邮箱 + 6 位验证码登录，从业者用姓名 + PIN 码登录，外部合作方只能看到自己参与的会话；通知邮件不带任何消息内容；附件经校验后以不共享方式存储；带哈希链审计日志——并且诚实地写明其局限（不是端到端加密；机构管理员可以访问消息内容）。从 `README.md` 或 `PROMPT.md` 开始。 |
| [Between Sessions Kit](between-sessions-kit/)（会谈之间 · 来访者练习与提醒系统） | 搭建一套归你自己所有的**来访者会谈外练习系统**，替代按席位收费的平台订阅，基于 Google Workspace + Apps Script：双语练习与提醒库（100+ 项），咨询师在 PIN 码登录的应用里布置练习，来访者点开专属链接即可完成（无需注册账号、无需下载应用、**完全不用短信**）；提醒只用邮件、每 15 分钟运行一次，并按**来访者所在时区**发送；提前提交会自动抵扣待完成的提醒，不会重复催促；需要关注的提交会进入待查看队列；另有每晚的提醒看门狗和每周工作簿备份。从 `README.md` 或 `PROMPT.md` 开始。 |
| [Simple EHR Kit](simple-ehr-kit/)（简易自费电子病历） | 在 Google Workspace + Apps Script + Sheets 上搭建一套归你自己所有的**简易自费电子病历系统**，替代按席位收费的 EHR 订阅：来访者档案与排期（使用你自己的视频链接、邮件提醒）、可自定义的记录模板（一键沿用上次记录、签署锁定）、专属链接的来访者门户与电子入组材料、带付款链接的账单，以及一键生成的 PDF 超级账单（superbill）供来访者自行申请网络外报销。**设计上仅限自费**——不提交保险理赔、不查保险资格、不处理 ERA 回执。为多位咨询师共用而设计的速度方案：每个机构独立安装一份，Sheets 只作轻量索引、记录正文存放在 Drive 中，并按年归档。从 `README.md` 或 `PROMPT.md` 开始。 |
| [CE Records Kit](ce-records-kit/)（继续教育学分记录） | 让继续教育记录在整个续证周期内始终处于可续证状态，适用于持有一个或多个执照的情况：经核实的各执照要求清单、以证书为准的课程跟踪表、与官方上报系统（如 CE Broker 或你所在州的对应系统）对账并只补录缺失课程、按类别分别呈现缺口的状态报告。智能体永远不会替你作出声明（attestation）或提交续证。从 `README.md` 或 `PROMPT.md` 开始。 |
| [Practice Website Kit](practice-website-kit/)（机构网站） | 用 **Astro + PagesCMS + Cloudflare Pages** 搭建机构网站：快速的静态网站（首页、咨询师介绍、服务、收费、常见问题、博客/资源），通过网页表单而不是改代码来编辑内容，免费托管在你自己的域名下——预约、目录等功能以嵌入方式接入你现有的系统，带结构化数据和 llms.txt，每条联系路径上都有危机热线。从 `README.md` 或 `PROMPT.md` 开始。 |
| [Auto-Created Listing Takedown Kit](auto-created-listing-takedown-kit/)（自动生成黄页条目下架工具包） | 查找并移除**你从未创建过的黄页条目**：一些网站抓取 NPPES 公开注册数据，自动生成咨询师主页——有时甚至是整站的小型网站——并编造营业时间、错误的专业方向和虚假预约按钮。内容包括按 NPI 和法定姓名盘点、逐站下架手册（包括 Dr. Leonardo 的“认领以下架”流程）、验证链接的完成纪律、向 FTC / Google / 主机商 / 注册商提交滥用举报，以及每月自动巡查，让已下架的页面不再复活。从 `README.md` 或 `PROMPT.md` 开始。 |
| [Retell Virtual Receptionist Kit](retell-virtual-receptionist-kit/)（AI 电话接待员） | 为个人或团体执业机构搭建 **Retell AI 电话接待员**：一条总机线路，按咨询师名册进行匹配，可选多语言，通过安全桥接连接你自己的预约系统，实时查询空档并完成预约；带结构化通话成本记录、隐私与危机处理护栏、先用免费方式充分测试，再逐条线路切换目录或总机号码。从 `README.md` 或 `PROMPT.md` 开始。 |
| [Insurance Payer Credentialing](insurance-payer-credentialing/)（保险签约准入） | 一套可重复、可审计的工作流程，用于直接与保险公司和 EAP 签约准入：每位从业者的材料清单、按支付方分别准备的提交资料包、结果记录——并把团体签约状态与个人准入状态分开记录，绝不把团体合同误认为某位咨询师已经获准。它只负责准备提交——未经你的明确批准，什么都不会发送。从 `README.md` 或 `PROMPT.md` 开始。 |
| [Practice Chatbot Kit](practice-chatbot-kit/)（机构网站智能客服） | 为你的网站搭建双语的机构协调员聊天机器人：先按执业州匹配，再按专长、保险、语言和年龄组匹配；把匹配成功的访客引导到你自己的预约链接；只根据你自己的帮助中心内容回答常见问题；收费与保险问题一律转人工，绝不引用未公开的收费；访客透露危机情况时，停止预约流程并提供 988 危机资源。从 `README.md` 或 `PROMPT.md` 开始。 |
| [Snoooz Inbox Automation Kit](snoooz-inbox-automation-kit/)（Snoooz 邮箱自动化） | 为个人或小型执业机构设置 Snoooz.ai 邮箱自动化：黄页与 Psychology Today 咨询邮件的自动回复，按年龄、来访者类型、保险、所在地、危机情况、形式和收费逐项把关；EAP 咨询处理；现有来访者与账单问题的分流；标签与排除规则——附空白配置模板，并要求在任何邮件自动发送前先通过模拟测试。从 `README.md` 或 `PROMPT.md` 开始。 |
| [Brilliant Directories Publishing Kit](brilliant-directories-publishing-kit/)（Brilliant Directories 黄页发布） | 在 Brilliant Directories 上创建、改版和修复黄页/SEO 页面而不翻车：先隐藏再创建；正文只能从已排版的源文件整段替换，绝不改写转述；对咨询师卡片、结构化数据和 hreflang 做精确的线上核验；以及 noindex 陷阱的正确处理顺序——先公开、再取消勾选 NoIndex、刷新站点、核验线上 robots 标签后再申请收录。从 `README.md` 或 `PROMPT.md` 开始。 |
| [Client Tool Publishing Kit](client-tool-publishing-kit/)（来访者工具发布） | 把双语互动来访者工具（练习册、追踪表、心理教育工具）从 zip 文件部署到你自己域名下的 GitHub Pages，挑选无版权问题的封面图，并登记到你的工具索引表格的双语页签中——分享前先核验两个线上链接都可正常打开。从 `README.md` 或 `PROMPT.md` 开始。 |
| [Apps Script Deploy Kit](apps-script-deploy-kit/)（Apps Script 接口部署） | 用你自己的 OAuth 客户端通过 Apps Script 接口部署 Google Apps Script 网页应用，不再往编辑器里粘贴代码：推送准确的文件、回读核对、创建版本、升级**现有**部署（绝不生成新链接），并从线上页面验证。其他工具包的应用都靠它部署。从 `README.md` 或 `PROMPT.md` 开始。 |
| [Apps Script Build Checklist Kit](apps-script-build-checklist-kit/)（Apps Script 搭建检查清单） | 一份上线前检查清单，收录 Apps Script 在真实运行中最容易出事的缺陷：清单文件里的邮件权限范围、与浏览器全局变量重名的顶层变量、PIN 验证契约不一致、表单部分保存丢数据、用显示名而不是稳定 ID 关联记录、电子表格时区导致时间戳偏移——每项都给出修复方法和最终巡查步骤。从 `README.md` 或 `PROMPT.md` 开始。 |
| [Muse Backup & Handover](muse-backup-handover/)（Muse 备份与交接） | 一个额外的通用技能，与执业业务无关：把你的 Muse 智能体的人设、记忆和资料打包成 AES-256 加密 ZIP，并通过《恢复手册》和验证问答交接给新的 Muse——新助手答对问题才算交接成功。本技能按其 MIT 许可从上游项目镜像收录（见其 `LICENSE`）。从 `README.md` 开始。 |

## 如何使用技能

1. **选一个技能**——不需要下载整个仓库。
2. **最快：把本仓库链接粘贴给你的 AI 智能体**并说出技能名称（见本页顶部）。也可以把整个文件夹交给你的智能体：
   - 支持原生技能的智能体：把文件夹安装/复制为一个技能。
   - 编程工作区类智能体：把文件夹放进你的工作区，让智能体读取其中的 `SKILL.md`。
   - 纯聊天类智能体：把文件夹里的全部 `.md` 文件上传，并使用起始提示词（各工具包内附有现成的 `PROMPT.md`）。
3. **先完成设置访谈/配置。** 每个技能在真正搭建或运行之前，都会先询问你自己机构的具体情况（域名、收费、保险签约、群组等）。这一步不要跳过，也永远不要让智能体替你猜测薪酬、保险或收费数字。
4. **上线前先审核。** 这些技能产出的是草稿、规格说明和可直接粘贴的文件。除非你明确批准，部署、提交和发送都应由你本人完成。

## 关于 HIPAA 的说明

预约类工具包设计为在**已签署 BAA（业务伙伴协议）的 Google Workspace 账号**内运行——这一前提写在每个工具包的开头；只要有真实来访者数据流经系统，这一条没有例外。软件提供的是支持 HIPAA 合规的防护措施，而不是合规认证；本仓库的任何技能都不提供合规认证。搭建前请先阅读每个技能的 `references/security-and-hipaa.md`。

## 参与贡献 / 反馈

这些技能来自一家正在实际运营的团体执业机构，分享出来是希望同行不必重复造轮子。如果你在自己的机构里改编了某个技能并做出了改进，欢迎提交 pull request，或开一个 issue 说明你改了什么。
