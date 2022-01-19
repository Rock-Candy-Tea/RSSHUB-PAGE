
---
title: '程序员笔记 CherryTree 0.99.45 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0119/070828_IWDo_4937141.png'
author: 开源中国
comments: false
date: Wed, 19 Jan 2022 07:09:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0119/070828_IWDo_4937141.png'
---

<div>   
<div class="content">
                                                                                            <p>CherryTree 0.99.45 现已发布。CherryTree 是一个支持无限层级分类的笔记软件，Python 编写，支持富文本编辑和代码高亮，支持 Linux 和 Windows 平台。数据采用 sqlite 或 XML 存储，支持密码保护，支持从 NoteCase、KeepNote、Knowit、Tomboy、TuxCards、Treepad、Leo 等笔记软件导入数据。</p> 
<p><img height="479" src="https://static.oschina.net/uploads/space/2022/0119/070828_IWDo_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p><img height="479" src="https://static.oschina.net/uploads/space/2022/0119/070833_Gy9G_4937141.png" width="700" referrerpolicy="no-referrer"></p> 
<p>此版本更新内容如下：</p> 
<ul> 
 <li>修复了 0.99.44 中引入的对话框消息中的标签问题（#1890，#1897）</li> 
 <li>修复删除行或列后表格单元格失去焦点 (#194)</li> 
 <li>添加了用空格替换制表符的操作；更改执行代码图标以播放符号</li> 
 <li>修复了打印/导出到 pdf 的代码缩进标签，始终使用 8 个空格作为标签宽度，忽略设置</li> 
 <li>修复了打印/导出到 pdf 的纯文本的代码框，以使用纯文本配置的字体</li> 
 <li>修复了代码框中的粘贴文本在启用自动调整大小的情况下被留在错误的滚动位置上的问题</li> 
 <li>添加现有功能的可配置性，以自动尝试将 CamelCase 文本链接到具有相同名称的节点中</li> 
 <li>在首选项对话框中增加了搜索键盘快捷键的可能性：只需关注列表并输入部分描述 (#1833)</li> 
 <li>添加了在你键入时禁用自动 url 链接生成的可能性 - 不在首选项对话框中，请在 config.cfg 中查找“url_autolink”</li> 
 <li>将缩进/取消缩进的默认键盘快捷键，从 Shift+Ctrl+'>'/'<' 更改为 Ctrl+'>'/'<' (#1901)</li> 
 <li>修复了从 zim 导入的问题，在导入的节点中删除了不需要的 header data；添加了缺少的默认 zim notes 文件夹 (#1870)</li> 
 <li>修复顶部菜单中的 alt 访问键：确保唯一性并添加 missing (#1865)</li> 
 <li>修复了在搜索多个节点时，如果代码框被设置为不自动展开，则仅在 Windows 上崩溃 (#1729)</li> 
 <li>修复 RTL (阿拉伯语) 链接无效的问题 (#1889)</li> 
 <li>添加了印度印地语</li> 
</ul> 
<p><span style="color:#333333">更新说明：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgiuspen%2Fcherrytree%2Fblob%2Fmaster%2Fchangelog.txt" target="_blank">https://github.com/giuspen/cherrytree/blob/master/changelog.txt</a></p>
                                        </div>
                                      
</div>
            