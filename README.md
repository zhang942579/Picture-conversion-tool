# 						图片转换工具

## 一、功能的实现

​		只需要点击添加按钮，选择图片（JPG、PNG、JPEG、BMP等），便可以在右侧文本框中识别出图片的文字。点击文本框便可以编辑识别出来的文字，适合排版，可以连续添加多张图片，都会往文本框中添加文字，直到点击还原按钮，便会将文本框中的文字全部删除，也能点击复制，实现一键复制文本框所有内容。

## 二、作品的来源

​		该作品主要是我在华为云上免费领取了一个通用文字识别OCR，加上编写文档时总是在百度上遇到不可复制的文档，所以就草率的编写了这个小工具。

## 三、实现原理

​		页面设计通过PyQT5实现简单的窗口。

​		文字识别通过华为OCRSDK接口实现。

## 四、下载

​		dist/main 这个文件夹存放的是打包成exe文件的，直接下载该文件夹中的所有文件，也可以下载dist.zip压缩文件，在电脑中解压便可以在main文件夹中找到并双击main.exe来运行该工具

​		resource该文件夹存放的是主要代码，启动代码是main.py

## 五、更改的东西

​		添加了离线模式，不过exe打包不来训练模型，所以离线模式只放在了代码中。
