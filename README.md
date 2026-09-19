# 河北大学选修课《操作系统实验》Antigravity 专属 Skill
# HBU OS Elective Lab Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform: Antigravity](https://img.shields.io/badge/Antigravity-Skill-blue.svg)](https://antigravity.google)
[![Compatible: WPS & Word](https://img.shields.io/badge/Office-WPS%20%7C%20Word-green.svg)](https://www.wps.cn)

> 适用于河北大学（HBU）电子信息工程学院等本科《操作系统实验》（选修课）报告自动编写、格式排版、照片去水印与避坑的全套经验与自动化工具库。

---

## ✨ 核心特性

- 🎯 **符合大二选修课真实水平**：文风严谨踏实，拒绝过度晦涩学术化，真实呈现普通偏优秀（良好偏上）的工科作业口吻。
- 🚫 **彻底根除彩色字**：严格遵循 Word/WPS 默认纯黑文字规范，文档内部 0 `<w:color>` 标签，杜绝 AI 痕迹。
- 📑 **原模板 6 行大表格 100% 保全**：完全基于河大官方报告模板的大框架填充，保持学院教师批改视觉习惯。
- 📄 **多余空白页（第 2 页空白）自动消灭**：分析并解决了封面分页符与空行溢出导致第 2 页出现空白页的问题。
- 🖼️ **翻拍照片去水印与尺寸控制**：自带图片预处理工具，自动裁切手机相机水印（realme/iPhone 等）与非屏幕边框，自动自适应排版。
- 📚 **全课程实验大纲覆盖**：沉淀了实验一至实验七（进程控制、同步互斥、调度、银行家算法、内存管理、页面置换、磁盘调度）的核心题库与要点。

---

## 📁 目录结构

```text
.
├── SKILL.md                          # Antigravity 技能主定义（YAML Frontmatter + SOP）
├── README.md                         # 项目使用说明书
├── LICENSE                           # MIT 开源协议
├── scripts/                          # 自动化工具箱
│   ├── build_report.py               # 报告核心构建器（防空白页、去颜色标签）
│   └── crop_photos.py                # 照片水印/黑边裁剪与等比缩放脚本
├── references/                       # 核心规范与知识库
│   ├── report_standard.md            # 排版规范与语言深度定位指南
│   ├── cover_fields.md               # 封皮字段映射与下划线保全
│   ├── os_labs_overview.md           # 实验一至实验七项目速查与作答要点
│   └── troubleshooting.md            # WPS / Word 常见排版故障排查手册
└── resources/
    └── template_structure.xml        # 河大官方 6 行主表格 XML 参考骨架
```

---

## 🚀 安装与使用方式

### 方式一：作为 Google Antigravity Skill 全局使用（推荐）

将本项目克隆至 Antigravity 全局技能目录：

```bash
git clone https://github.com/eryuemu/hbu-os-lab-skill.git ~/.gemini/config/skills/hebei-university-os-lab-skill
```

在对话中直接对 Antigravity Agent 发送需求即可自动触发：
> “根据操作系统实验指导书和这几张截图，帮我写一下实验二的实验报告”

---

### 方式二：命令行独立使用脚本

1. **预处理翻拍照片（去相机水印与边框）**：
```bash
python3 scripts/crop_photos.py -i /path/to/photos -o /path/to/clean_images --crop_bottom 0.06
```

2. **校验 DOCX 报告规范（检查是否含彩色字）**：
```bash
python3 -c "
import zipfile, re
with zipfile.ZipFile('你的实验报告.docx') as z:
    colors = re.findall(r'<w:color[^>]*/>', z.read('word/document.xml').decode('utf-8'))
    print('Color tags found:', len(colors))
"
```

---

## ⚠️ 隐私声明与合规提醒

1. 本仓库所有示例数据均已完成脱敏处理（姓名、学号等均使用虚拟占位符）。
2. 本工具仅用于辅助个人学习、格式排版与实验记录整理，请严格遵守所在高校学术诚信规范，切勿直接抄袭。

---

## 📄 License

本项目基于 [MIT License](LICENSE) 开源。
