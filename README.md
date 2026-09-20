# FocusSearch

FocusSearch 是一个轻量级的 Python 命令行搜索工具。用户输入关键词并选择搜索平台后，程序会自动生成对应的搜索地址，并在默认浏览器中打开搜索结果。

## 当前功能

- 命令行交互界面
- 支持中文、空格和特殊字符的 URL 编码
- 显示编码前的原始搜索关键词
- 支持抖音搜索
- 自动调用默认浏览器打开搜索结果

## 运行环境

- Windows
- Python 3.10 或更高版本
- 无需安装第三方依赖

## 使用方法

```bash
git clone https://github.com/davidwen20060522-stack/FocusSearch.git
cd FocusSearch
python main.py
```

按照提示输入搜索内容，然后输入平台编号 `1`，程序会在默认浏览器中打开对应的抖音搜索结果。

## 项目结构

```text
FocusSearch/
├── main.py       # 命令行界面与输入处理
├── searchway.py  # 搜索平台 URL 与浏览器调用
└── README.md
```

## 工作原理

1. 使用 `input()` 获取搜索关键词。
2. 使用 `urllib.parse.quote()` 将关键词编码为 URL 安全格式。
3. 根据用户选择调用对应的搜索平台。
4. 使用 `webbrowser.open_new()` 打开搜索结果页。

## 后续计划

- 增加 B 站、小红书等搜索平台
- 处理无效的平台编号
- 将平台配置重构为字典或独立模块
- 增加图形界面
- 优化跨平台清屏行为

## 说明

这是一个用于学习 Python 输入处理、函数、模块、URL 编码和浏览器调用的练习项目。
