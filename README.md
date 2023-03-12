# README #
[English readme](#markdown-header-English)
## Windowed new view - 适用于Krita 5.0+的简易插件 ##

### 用途 ###
点击时新建当前文档的新视图，并自动窗口化和设为置顶

### 安装 ###
1. 下载zip压缩包
2. 使用Krita菜单中的工具→脚本→从文件导入 Python 插件
3. 弹出对话框，点击“是”
4. 重启Krita
5. 工具→脚本里面多出来一个Open windowed new view选项
6. 单击运行

如果安装失败的话（绝无可能！），手动将windowed_new_view文件夹和windowed_new_view.desktop粘贴进

C:\Users\\**用户名**\AppData\Roaming\krita\pykrita

并重启Krita, 随后在设置→配置Krita→Python插件管理 中勾选 Windowed new view启用插件，再次重启Krita即可

### 插件信息 ###

* 测试版本： Krita 5.1.5
* 电脑没有爆炸
* 作者：库里斯库拉（Acfun）

### 其他 ###
因为功能太简单了，所以我没有写配置快捷键的代码。
这个插件的核心代码是
```python
import krita
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMdiSubWindow

# Get the current document and active view
doc = krita.Krita.instance().activeDocument()

# Create a new view for the document
new_view = krita.Krita.instance().activeWindow().addView(doc)

# Get the subwindow of the new view
subWindow = new_view.window().qwindow().centralWidget().currentWidget().activeSubWindow()

# Show windowed subwindow
subWindow.showNormal()

# Check the 'Always on top' option
menu = subWindow.children()[0]
menu.actions()[5].trigger()
```      
你可以直接用Krita的脚本调试工具运行，或许可以将它保存为.py文件并且用工具→常用脚本快捷键 分配快捷键？

### 鸣谢 ###
* [SubWindowOrganizer](https://github.com/wojtryb/kritaSubwindowOrganizer)
* [さいとう なおき 老师](https://twitter.com/_NaokiSaito)
* bing ai 帮我查文档（同时也贡献了bug）

---
### English
## Windowed new view - An extension for Krita 5.0+ ##

### Function ###
Creates a new view of the current document when clicked, automatically windowed it and set 'Always on top'.

### Installation ###
1. Download the zip archive
2. Use Tools → Scripts → Import Python Plugin from File in the Krita menu
3. A dialog box will pop up, click "Yes"
4. Restart Krita
5. Tools→Scripts now has an Open windowed new view option
6. Click

If the installation fails ( impossible! ), manually copy&paste the windowed_new_view folder and windowed_new_view.desktop into

C:\Users\\**Username**\AppData\Roaming\krita\pykrita

and restart Krita. Open Settings > configure Krita > Python Plugin Manager, check the column with the name 'Windowed new view' to enable the plugin.

Restart Krita again, done.

### Some Information ###

* Tested with Krita 5.1.5
* My computer didn't explode
* Author: me(Cliscylla)

### Others ###
I didn't think it was necessary, so I didn't code the feature for assigning shortcuts. But it's up to you.
The core of the plugin is:
```python
import krita
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMdiSubWindow

# Get the current document and active view
doc = krita.Krita.instance().activeDocument()

# Create a new view for the document
new_view = krita.Krita.instance().activeWindow().addView(doc)

# Get the subwindow of the new view
subWindow = new_view.window().qwindow().centralWidget().currentWidget().activeSubWindow()

# Show windowed subwindow
subWindow.showNormal()

# Check the 'Always on top' option
menu = subWindow.children()[0]
menu.actions()[5].trigger()
```      

You can run it in the built-in Scripter directly, probably you can also save those code in a .py file and then assign a keyboard shortcut for it with Ten Scripts.

### Special Thanks ###
* [SubWindowOrganizer](https://github.com/wojtryb/kritaSubwindowOrganizer)
* My drawing teacher [さいとう なおき](https://twitter.com/_NaokiSaito)
* bing ai for helping me look up the documentations (and also for contributing bugs)