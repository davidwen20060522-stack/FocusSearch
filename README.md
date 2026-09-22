# FocusSearch

FocusSearch 是一个轻量级的 Python 命令行多平台搜索工具。输入关键词并选择平台后，程序会生成对应的搜索地址，并在默认浏览器中直接打开搜索结果。

## 当前功能

- 命令行交互界面
- 支持中文、空格和特殊字符的 URL 编码
- 支持抖音、小红书、B 站和百度搜索
- 支持 `ALL` 模式，一次打开全部平台的搜索结果
- 检查无效的平台编号
- 完成搜索后可继续输入下一组关键词
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

运行后输入搜索内容，再选择搜索平台：

```text
[1] 抖音
[2] 小红书
[3] B站
[4] 百度
[5] ALL
```

输入 `1` 至 `4` 会打开对应平台；输入 `5` 会依次打开四个平台。输入其他内容时，程序会显示错误提示并结束。

## 项目结构

```text
FocusSearch/
├── main.py       # 命令行界面、输入处理和平台选择
├── searchway.py  # 各搜索平台的 URL 与浏览器调用
├── CHANGELOG.md  # 版本更新记录
└── README.md
```

## 工作原理

1. 使用 `input()` 获取搜索关键词。
2. 使用 `urllib.parse.quote()` 将关键词编码为 URL 安全格式。
3. 根据编号调用 `searchway.py` 中对应的平台函数。
4. 使用 `webbrowser.open_new()` 打开搜索结果页。
5. 搜索完成后返回输入页面，继续下一次搜索。

## 更新记录

详细更新内容请查看 [CHANGELOG.md](CHANGELOG.md)。

## 后续计划

- 优化函数和变量的命名规范
- 使用字典减少平台选择代码的重复
- 改进跨平台清屏行为
- 增加图形界面

## 说明

这是一个用于学习 Python 输入处理、条件判断、循环、函数、模块、URL 编码和浏览器调用的练习项目。
