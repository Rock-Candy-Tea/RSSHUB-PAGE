
---
title: 'CKEditor 5 v30.0.0 发布，强大的富文本编辑器框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3149'
author: 开源中国
comments: false
date: Fri, 08 Oct 2021 07:16:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3149'
---

<div>   
<div class="content">
                                                                    
                                                        <p>CKEditor 5 是一个强大的富文本编辑器框架，具有模块化架构、现代集成和协作编辑等功能。CKEditor 5 v30.0.0 正式发布，更新内容如下：</p> 
<h3>主要变化</h3> 
<ul> 
 <li><code>config.toolbar.viewportTopOffset</code> 属性被移至 <code>config.ui.viewportOffset</code>，现在它接受一个对象。</li> 
</ul> 
<h3>次要变化</h3> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2F%40ckeditor%2Fckeditor5-engine" target="_blank">engine</a></strong>: <code>Matcher</code> 类在处理提供给 <code>match()</code> 和 <code>matchAll()</code> 方法的 <code>Element</code> 时更加严格。现在它将不接受其他 <code>Node</code></li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2F%40ckeditor%2Fckeditor5-html-support" target="_blank">html-support</a></strong>: <code>html-support/converters~disallowedAttributesConverter</code> 这个公共 helper 函数已被删除，因为过滤不允许的元素和属性的方法发生了变化</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2F%40ckeditor%2Fckeditor5-widget" target="_blank">widget</a></strong>: widget 实用程序中删除了 <code>centeredBalloonPositionForLongWidgets()</code> helper，使用 <code>BalloonPanelView.defaultPositions.viewportStickyNorth</code> 代替</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2F%40ckeditor%2Fckeditor5-widget" target="_blank">widget</a></strong>: <code>toWidgetEditable()</code> 现在将为可编辑元素设置高亮处理。如果在自定义插件中使用此方法进行转换，则当该元素上有标记时，它可能会影响您的元素样式。</li> 
</ul> 
<h3><strong>功能</strong></h3> 
<ul> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2F%40ckeditor%2Fckeditor5-autoformat" target="_blank">autoformat</a></strong>: 允许通过按退格键恢复文本转换</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2F%40ckeditor%2Fckeditor5-html-support" target="_blank">html-support</a></strong>: 为图像功能添加了 General HTML Support 集成</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2F%40ckeditor%2Fckeditor5-image" target="_blank">image</a></strong>: 允许使用退格键来撤销自动插入图片的转换</li> 
 <li><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2F%40ckeditor%2Fckeditor5-ui" target="_blank">ui</a></strong>: 在 <code>BalloonPanelView.defaultPositions</code> 中引入了一个新的位置类型 <code>viewportStickyNorth</code></li> 
 <li>引入了 <code>editor.ui.viewportOffset</code> 属性</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fckeditor%2Fckeditor5%2Freleases" target="_blank">https://github.com/ckeditor/ckeditor5/releases</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            