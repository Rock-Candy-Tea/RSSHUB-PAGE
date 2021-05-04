
---
title: 'CKEditor 5 v27.1.0 发布，支持表和块引用嵌套'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-fd83e36ff59e987c443f58d2eb13189a02a.png'
author: 开源中国
comments: false
date: Mon, 03 May 2021 09:24:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-fd83e36ff59e987c443f58d2eb13189a02a.png'
---

<div>   
<div class="content">
                                                                                            <p>CKEditor 5 v27.1.0 已经发布，支持表和块引用嵌套，对已被废弃的 HTML 对齐属性引入了传统的支持。所有这些都是为了提高向后的兼容性，并支持一些软件（如电子邮件应用程序）可能仍然生成的旧的、HTML4 格式的内容。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-fd83e36ff59e987c443f58d2eb13189a02a.png" referrerpolicy="no-referrer"></p> 
<p><strong>支持嵌套表</strong></p> 
<p>从 27.1.0 版本开始，CKEditor 5 支持在其他表格的单元格中嵌套表格，并且可以将图像和文本放在一起。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-a66d783ee26a7ae95bf18faa2694cd3735c.gif" referrerpolicy="no-referrer"></p> 
<p><strong>块引用嵌套</strong></p> 
<p>在这个版本中，CKEditor 5 将正确地显示嵌套的块引用。支持块引用嵌套是为了向后兼容加载已有的内容，例如在 CKEditor 4 中创建的内容。此外，还基本支持通过拖放功能或粘贴的方式将一个块引用嵌套到另一个块引用中。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-021adba239228f0e20f48e32f5ef0671220.png" referrerpolicy="no-referrer"></p> 
<p><strong>对 align </strong><strong>属性的传统支持 </strong></p> 
<p>align 属性源于旧的 HTML 规范，用于设置一个对象（图像、文本部分或其他）对周围内容的对齐，随着 HTML5 规范的出台而被取消，但仍然经常被使用。CKEditor 5 现在支持对该属性的正确处理。如果使用 align 进行格式化的内容被加载到编辑器中，该属性将被正确读取并转换为现代格式。</p> 
<p><strong>新的块填充模式</strong></p> 
<p>从 27.1.0 版本开始，CKEditor 5 在 DOM 转换器以及 HTML、XML 和 Markdown 数据处理器中引入了一种新的块填充模式，称为 markedNbsp。如果处理器被设置为使用标记的填充器，它将插入被跨度包裹的填充器（<span data-ck-filler="true">&nbsp;<span>）。这种新的填充模式允许更精确地处理块填充物，因此它们不会泄漏到编辑器内容中。</p> 
<p><strong>用附加属性更好地上传 </strong></p> 
<p>该版本在 ImageUploadEditing 中引入了 uploadComplete 事件，允许根据从上传适配器中获取的数据定制图像元素。这可能意味着为图像设置自定义属性。<br> 另外，upload() 方法现在可以解析为一个带有额外属性和 urls 哈希值的对象。这可能会影响所有依赖于 SimpleUploadAdapter 上传机制的集成，因此是一个小的突破性改变。</p> 
<p>更多详细内容请查看更新公告。</p>
                                        </div>
                                      
</div>
            