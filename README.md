# MC截图自动加水印

Windows平台，给Minecraft截图自动加水印，适用于[商弦](https://guc1010.top)，可以自行修改适配其他用途。

> 低创自用作品，依赖过多，有更好的方法请指教

## 使用方法

### 下载内容

点 `Code` > `Download Zip` 下载此仓库，将压缩包中的内容解压至你的Minecraft游戏目录（与`options.txt`、`servers.dat`等文件在同一目录），例：`D:\MC\MCJE\.minecraft\versions\1.21-Fabric\`

### 安装Python3

运行必需，安装方法略

### 安装inkscape

此软件用于将svg矢量图转为png。

1. 安装 inkscape（https://inkscape.org/release/）
1. 检查 inkscape 是否安装到了`C:\Program Files\Inkscape\bin\inkscape.exe`，如果不是，打开`watermark.py`手动将`inkscape_path = 'C:/Program Files/Inkscape/bin/inkscape'`修改为正确路径。

### 下载RoboIntern

此软件用于监测新增截图自动执行水印脚本。

1. 下载 RoboIntern（https://robointern.tech/release/RoboIntern.zip）
1. 解压至任意目录，双击打开`RoboIntern.exe`
1. 点右上角的加号，弹出Add Task窗口
1. 在Actions选项卡点右上角的加号左边的侧边栏Search actions...处搜索Python，点击Run a Python script
1. 右侧在Python exe path中找到你安装的Python.exe，Script path填入`watermark.py`的绝对路径（例：`D:\MC\MCJE\.minecraft\versions\1.21-Fabric\watermark.py`），Description随便填，填完点右下角Add action
1. 切换到Triggers选项卡，点加号，左边栏选File status > File created
1. 右侧File path填`<你的截图文件夹>\*`，例：`D:\MC\MCJE\.minecraft\versions\1.21-Fabric\screenshots\*`，填完点右下角`Add trigger`
1. 切换到Options选项卡，在Task name处随便填个名字，右下角点Add task
1. 看到我们的任务出现在列表中了，检查右下角是Start scheduling还是Stop scheduling，如果是前者则点一下，如果是后者则已经在正常运行。

### 使用

本脚本自动读取Minecraft日志文件中的玩家名、Iris配置文件中的光影名、截图日期，无需手动输入。不支持其他光影模组。

1. 进入商弦服务器（mc.guc1010.top）
2. 使用`/sy <水印标题>`命令，会提示「截图水印标题已设为：<水印标题>」
3. 按F2截图
4. 检查`watermarks`文件夹中是否生成了带水印的截图。
5. 如果上次设置了水印标题，下次进服时会提示「截图水印标题已设为：<水印标题>」
6. 想要生成无标题的水印，使用`/sy`命令，会提示「截图水印标题已清除。」

