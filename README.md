# 						图片转换工具

## 一、功能的实现

​		只需要点击添加按钮，选择图片（JPG、PNG、JPEG、BMP等），便可以在右侧文本框中识别出图片的文字。点击文本框便可以编辑识别出来的文字，适合排版，可以连续添加多张图片，都会往文本框中添加文字，直到点击还原按钮，便会将文本框中的文字全部删除，也能点击复制，实现一键复制文本框所有内容。

## 二、作品的来源

​		该作品主要是我在华为云上免费领取了一个通用文字识别OCR，加上编写文档时总是在百度上遇到不可复制的文档，所以就草率的编写了这个小工具。

## 三、实现原理

​		页面设计通过PyQT5实现简单的窗口。

​		文字识别通过华为OCRSDK接口实现。

