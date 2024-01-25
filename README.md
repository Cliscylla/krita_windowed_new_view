## README ##
[English readme](#markdown-header-english)
## Windowed new view - 适用于Krita 5.0+的简易插件 ##
v1.0 发布  
v1.1 可以分配快捷键了  
v1.2 修复选中图层组时无法使用插件的问题（activationFlags：10000→0001），感谢krita-artists论坛的@freyalupen  

### 用途 ###
点击时新建当前文档的新视图，并自动窗口化和设为置顶

### 安装 ###
1. 下载zip压缩包  
2. 使用Krita菜单中的工具→脚本→从文件导入 Python 插件
3. 选择压缩包，并确认
4. 重启Krita
5. 工具→脚本里面多出来一个Open windowed new view选项
6. 单击运行

在确认安装成功之后，你就可以删除第一步下载的zip文件了  
如果安装失败的话（绝无可能！），手动将windowed_new_view文件夹和windowed_new_view.desktop粘贴进

C:\Users\\*用户名*\AppData\Roaming\krita\pykrita

并重启Krita, 随后在设置→配置Krita→Python插件管理 中勾选 Windowed new view 启用插件，再次重启Krita即可  

这是所有Krita插件通用的安装方式  
### 插件信息 ###

* 测试版本： Krita 5.1.5-5.2
* 电脑没有爆炸
* 作者：库里斯库拉（号在Acfun）

### 其他 ###
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

可以直接用Krita的脚本调试工具运行，你可以利用这些代码去开发类似的功能。  

### 鸣谢 ###
* [SubWindowOrganizer](https://github.com/wojtryb/kritaSubwindowOrganizer)
* [さいとう なおき 老师](https://www.youtube.com/@saitonaoki2)
* bing ai 帮我查文档（同时也贡献了bug）


---
### English
## Windowed new view - An extension for Krita 5.0+ ##
v1.0 release  
v1.1 It can now be assigned a shortcut key  
v1.2 Fixed the issue of not being able to use plugins when selecting a layer group, (activationFlags changed：10000→0001), many thanks to @freyalupen in krita-artists forums!

### Function ###
Creates a new view of the current document when clicked, automatically windowed it and set 'Always on top'.

### Installation ###
1. Download the zip archive 
2. Use Tools → Scripts → Import Python Plugin from File in the Krita menu
3. Select the zip and confirm
4. Restart Krita
5. Tools→Scripts now has an Open windowed new view option
6. Click

After installing successfully, you can delete the zip file you downloaded at the first step.  
This is the general installation method for Krita python plugins.  

If the installation fails (impossible!), manually copy&paste the windowed_new_view folder and windowed_new_view.desktop into

C:\Users\\*Username*\AppData\Roaming\krita\pykrita

and restart Krita. Open Settings > configure Krita > Python Plugin Manager, check the column with the name 'Windowed new view' to enable the plugin.

Restart Krita again, done.

### Some Information ###

* Tested with Krita 5.1.5-5.2
* My computer didn't explode
* Author: me(Cliscylla)

### Others ###
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

You can run it in the built-in Scripter directly. Feel free to make use of it if you want to implement something similar.

### Special Thanks ###
* [SubWindowOrganizer](https://github.com/wojtryb/kritaSubwindowOrganizer)
* My drawing teacher [さいとう なおき](https://www.youtube.com/@saitonaoki2)
* bing ai for helping me look up the documentations (and also for contributing bugs)
