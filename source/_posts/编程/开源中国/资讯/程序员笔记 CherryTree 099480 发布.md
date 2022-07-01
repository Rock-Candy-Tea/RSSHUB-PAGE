
---
title: '程序员笔记 CherryTree 0.99.48.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0119/070828_IWDo_4937141.png'
author: 开源中国
comments: false
date: Fri, 01 Jul 2022 07:05:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0119/070828_IWDo_4937141.png'
---

<div>   
<div class="content">
                                                                                            <p>CherryTree 0.99.48 现已发布。CherryTree 是一个支持无限层级分类的笔记软件，Python 编写，支持富文本编辑和代码高亮，支持 Linux 和 Windows 平台。数据采用 sqlite 或 XML 存储，支持密码保护，支持从 NoteCase、KeepNote、Knowit、Tomboy、TuxCards、Treepad、Leo 等笔记软件导入数据。</p> 
<p><img alt height="342" src="https://static.oschina.net/uploads/space/2022/0119/070828_IWDo_4937141.png" width="500" referrerpolicy="no-referrer"></p> 
<p><img alt height="342" src="https://static.oschina.net/uploads/space/2022/0119/070833_Gy9G_4937141.png" width="500" referrerpolicy="no-referrer"></p> 
<p>此版本更新内容如下：</p> 
<ul> 
 <li>在导出到 html 和 pdf 时添加了对从右到左语言的支持 (#2044, #1668, #698)</li> 
 <li>为了在导出到 html 时支持从右到左的语言，生成的 html 文本行不再是 LINE<br/> 而是 <p>LINE</p></li> 
 <li>在导出到 pdf 时修复了指向 non ascii anchor name 的 node+anchor 的链接</li> 
 <li>修复在 Wndows 下导出到 pdf 的问题，node/node+anchor 的链接和目的地不在 pdf 中</li> 
 <li>在 Windows 上，导出为 pdf，修复了对文件/文件夹的链接；non ascii 路径的链接被禁用，因为当前会使库崩溃</li> 
 <li>改进了对渲染 LatexBoxes 所需的缺失可执行文件的检测。这些依赖项不再是强制性的 (#2033)</li> 
 <li>添加帮助用户再次显示隐藏菜单栏 (#1927, #2054)</li> 
 <li>在最新的表格单元格上按 Tab 现在会添加一个新表格行并移动到其第一个单元格</li> 
 <li>修复了在 linux 和 windows 之间移动的文件和文件夹以及文档的相对链接问题</li> 
 <li>在导出到 html 和 txt 多个文件时，现在将节点 id 附加到文件名以支持同名的多个节点</li> 
 <li>添加了对 solidity 的语法高亮支持（#2030）</li> 
 <li>在域名 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fgiuspen.com" target="_blank">giuspen.com</a> 出现问题后，域名更改为 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fgiuspen.net" target="_blank">giuspen.net</a> 并且 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fgiuspen.com" target="_blank">giuspen.com</a> 最终将消失</li> 
 <li>已完成支持 appimage 的工作，因此第一个 appimage 将很快可供下载 (#2025)</li> 
</ul> 
<p>详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgiuspen%2Fcherrytree%2Fblob%2Fmaster%2Fchangelog.txt" target="_blank">https://github.com/giuspen/cherrytree/blob/master/changelog.txt</a> </p> 
<p> </p>
                                        </div>
                                      
</div>
            