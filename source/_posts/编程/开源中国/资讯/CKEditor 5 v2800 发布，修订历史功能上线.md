
---
title: 'CKEditor 5 v28.0.0 发布，修订历史功能上线'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-e9330098d5f954fc6aacc4728dcfd1d55b9.png'
author: 开源中国
comments: false
date: Sat, 12 Jun 2021 06:43:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-e9330098d5f954fc6aacc4728dcfd1d55b9.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>CKEditor 5 v28.0.0 已经发布。这是一个顶级的文档版本管理工具，允许用户完全控制编辑过程。该版本带来了期待已久的修订历史功能，允许用户完全控制编辑过程，扩展了表格功能，并且支持标题以及默认的表格和表格单元格样式。此外还包括一些错误修复。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-e9330098d5f954fc6aacc4728dcfd1d55b9.png" referrerpolicy="no-referrer"></p> 
<h4>修订历史</h4> 
<p>这个新功能可以维护完整的文档修订历史记录。它可以让编辑器创建按内容的时间顺序命名的修订版，支持在修订预览中快速、方便地访问历史版本，并可以比较修订版本，以及一键恢复之前的修订版本。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-bcab0ae0a28cf24b78f93f3ff3aebce7063.JPEG" referrerpolicy="no-referrer"></p> 
<p>修订版预览显示已引入的修改（插入和删除）和在跟踪修改模式下添加的未解决的修改建议。它还显示了在给定的修订中引入的修改的总数。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-5bfe8f9f21daa0b13e8d160493c563f7f87.JPEG" referrerpolicy="no-referrer"></p> 
<h4>表格支持标题和默认属性</h4> 
<p>该版本增加了对表格标题的支持，标题会告知读者表格的内容。从可访问性的角度来看，使用标题也是有益的，因为它们可以被屏幕阅读器读取。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-a757e905ccc16a772bdcef413aa28a18269.gif" referrerpolicy="no-referrer"></p> 
<p>除此以外，表格样式功能现在还允许配置编辑器中的表格的默认外观。这些是在样式表中预定义的，并传递给编辑器配置。自定义的默认样式将被应用到你的表格中，并在 "表格属性" 和 "表格单元属性" 中可见，用户可以对其进行更改。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-66a97f1217298c9b9996a2cc177046b76f3.JPEG" referrerpolicy="no-referrer"></p> 
<h4>引入包元数据和 HTML 输出指南</h4> 
<p>该版本引入了包元数据。包元数据是一组与 CKEditor 5 相关的数据，描述分布在 npm 包中的插件。它允许外部构建器自动检测插件并构建它们，例如，通过CKEditor 5 在线构建器。这些数据应该保存在位于 npm 上发布的软件包根部的特殊的 ckeditor5-metadata.json 文件中。此外，推出了 DX 改进，可以记录所有CKEditor 5 功能的 HTML 输出。</p> 
<h4>现在可以在只读模式下导出为 PDF 和 Word</h4> 
<p>以前，当 WYSIWYG 编辑器在只读模式下工作时，所有的工具栏项目都会被禁用，作为阻止内容编辑的一部分。然而，这也会阻止导出到 Word 和导出到 PDF 的功能，尽管它们不与内容直接相关。从 v28.0.0 版本开始，这些功能在只读模式下将不再被阻止，使用户即使不能编辑，也能将编辑的内容导出到选定的文件格式。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-008b99372e4477be8b00c7433e6de0b3cb9.JPEG" referrerpolicy="no-referrer"></p> 
<h4>为数据模式项目定义新的 allowChildren 属性</h4> 
<p>在 v28.0.0 之前，用新的子集扩展模式定义是一个两步的过程，只能通过使用 allowIn 属性来实现。而该版本编辑器版本引入了 allowChildren 属性。这个额外的机制使得有可能利用一个更简单的解决方案，在新的模式定义注册期间提供 allowChildren 属性，在那里你可以为模型设置子代。</p> 
<p>更多详细内容，请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fckeditor.com%2Fblog%2Frevision-history-is-officially-live-ckeditor-5-v28.0.0-released%2F" target="_blank">官方公告</a>。</p>
                                        </div>
                                      
</div>
            