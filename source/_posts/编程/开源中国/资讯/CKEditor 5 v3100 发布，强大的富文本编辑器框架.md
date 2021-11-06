
---
title: 'CKEditor 5 v31.0.0 发布，强大的富文本编辑器框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5269'
author: 开源中国
comments: false
date: Sat, 06 Nov 2021 07:57:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5269'
---

<div>   
<div class="content">
                                                                                            <div style="margin-left:0; margin-right:0"> 
 <div style="margin-left:0; margin-right:0"> 
  <div style="margin-left:0; margin-right:0"> 
   <p style="margin-left:0; margin-right:0">CKEditor 5 是一个强大的富文本编辑器框架，具有模块化架构、现代集成和协作编辑等功能。CKEditor 5 v31.0.0 正式发布，更新内容如下：</p> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>引入<span> </span><code>Command#affectsData</code><span> </span>属性，用于指示在写权限受限的编辑器模式下，某个命令是否应该保持启用。</li> 
    <li>提及功能获得了输入触发字符后自定义列表中的最大项目数的功能。</li> 
    <li>新的协作功能示例已经可用： 
     <ul style="margin-left:0; margin-right:0"> 
      <li>对于 React 集成，将实现上下文功能，以及看门狗功能；</li> 
      <li>对于编辑器外的评论与离线评论；</li> 
     </ul> </li> 
    <li>评论和导出到 Word 的功能图标被改进</li> 
    <li>在代码块的末尾点击三次回车，现在需要转义</li> 
   </ul> 
   <h3>错误修复：</h3> 
   <ul style="margin-left:0; margin-right:0"> 
    <li>如果链接在块的边缘，链接、提及、内联图像和评论标记不能被鼠标拖动选择</li> 
    <li>在取消表格中的文本链接后，表格的气球不再呈现在错误的地方</li> 
    <li>当外部表格单元被选中时，嵌套的小部件选择手柄不再可见</li> 
    <li>HTML 嵌入 UI 现在可以正确反映只读状态。</li> 
   </ul> 
   <h3>主要变化：</h3> 
   <ul style="margin-left:0; margin-right:0"> 
    <li><code>html-embed</code>：<span> </span><code>InsertHtmlEmbedCommand</code>和<span> </span><code>UpdateHtmlEmbedCommand</code>已经被<span> </span><code>HtmlEmbedCommand</code>所取代，它现在负责这两项任务。该命令可以通过<span> </span><code>editor.execute( 'htmlEmbed' )</code><span> </span>执行</li> 
   </ul> 
   <p style="margin-left:0; margin-right:0">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fckeditor%2Fckeditor5%2Freleases" target="_blank">https://github.com/ckeditor/ckeditor5/releases</a> </p> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            