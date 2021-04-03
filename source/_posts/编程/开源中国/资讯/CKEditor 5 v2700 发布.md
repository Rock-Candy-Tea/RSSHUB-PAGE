
---
title: 'CKEditor 5 v27.0.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-e68f4720f661417aabee0b7f6e99523d24c.png'
author: 开源中国
comments: false
date: Fri, 02 Apr 2021 23:57:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-e68f4720f661417aabee0b7f6e99523d24c.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>CKEditor 5 v27.0.0 已经发布，包含拖放功能、语言功能扩展、待办事项功能优化等内容。</p> 
<p><img alt height="349" src="https://oscimg.oschina.net/oscnet/up-e68f4720f661417aabee0b7f6e99523d24c.png" width="620" referrerpolicy="no-referrer"></p> 
<h4>安全问题修复</h4> 
<p>在内部审查中，CKEditor 5 发现了一个正则表达式拒绝服务（ReDoS）漏洞（CVE-2021-21391）。该漏洞允许滥用特定的正则表达式。这可能会导致性能显著下降，导致浏览器标签页冻结。该问题已在本版本中修复，尽管这是一个影响较小的问题，只影响受害者的浏览器性能，没有数据泄露的风险，但仍强烈建议升级。</p> 
<h4>支持拖放</h4> 
<p>现在在文本编辑器中支持拖放，包括支持文本的拖放、移动块状对象（包括表格或图片）。此外，新功能还扩展了粘贴功能，支持从编辑器之外拖动 HTML 内容或纯文本，并将其放到需要的地方。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-eca86d6cd2bb410c2035b45d039f2c273c7.gif" referrerpolicy="no-referrer"></p> 
<h4>文本部分语言</h4> 
<p>CKEditor 5 提供了对不同 UI 语言的支持，以及从左到右和从右到左的语言方向，同时还提供了优质的拼写和语法检查。在当前版本中，通过新的文本部分语言功能扩展了对语言相关功能的支持。它允许通过工具栏下拉菜单为选定的内容部分定义特定的语言，提供可配置的语言列表供其选择。该功能还可以自动设置文本方向。<br> <img alt height="253" src="https://oscimg.oschina.net/oscnet/up-4b225efb24e4ab802fb3ff0e25b1bc483aa.png" width="777" referrerpolicy="no-referrer"></p> 
<h4>冒泡事件</h4> 
<p>该版本引入了 view.Document 事件的冒泡，类似于 DOM 中冒泡的工作方式。事件冒泡是一种处理嵌套元素和连接到同一事件但在不同上下文中的监听器的机制。这个功能支持对许多以前必须依赖优先级属性的监听器重新进行优先级排序。新的解决方案可以根据文档的树形结构更好地控制用户输入影响内容的方式。</p> 
<h4>改进待办事项和自动格式化功能</h4> 
<p>待办事项列表功能支持创建一个带有标签的交互式复选框列表。列表项可以通过一个工具栏按钮插入到内容中，或者通过自动格式化功能来实现。</p> 
<p><img alt height="186" src="https://oscimg.oschina.net/oscnet/up-264ff78783093dde34be3fe2621ce596de2.gif" width="771" referrerpolicy="no-referrer"></p> 
<p>详细内容请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fckeditor.com%2Fblog%2Fckeditor-5-v27.0.0-with-drag-and-drop-text-part-language-and-bubbling-events%2F" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            