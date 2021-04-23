
---
title: 'Layui 2.6.5 发布，修复和优化组件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4959'
author: 开源中国
comments: false
date: Fri, 23 Apr 2021 09:53:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4959'
---

<div>   
<div class="content">
                                                                    
                                                        <p>layui（谐音：类 UI) 是一套开源的 Web UI 解决方案，采用自身经典的模块化规范，并遵循原生 HTML/CSS/JS 的开发方式，极易上手，拿来即用。其风格简约轻盈，而组件优雅丰盈，从源代码到使用方法的每一处细节都经过精心雕琢，非常适合网页界面的快速开发。layui 区别于那些基于 MVVM 底层的前端框架，却并非逆道而行，而是信奉返璞归真之道。准确地说，它更多是面向后端开发者，你无需涉足前端各种工具，只需面对浏览器本身，让一切你所需要的元素与交互，从这里信手拈来。</p> 
<p><strong>更新日志：</strong></p> 
<ul> 
 <li>[修复] layer 组件在 Ajax 等场景下，存在概率性无法关闭层的问题</li> 
 <li>[优化] layer 组件的 close 和 closeAll 方法，第二个参数可传入回调，用于层被关闭后的操作</li> 
 <li>[修复] layer 组件的 photos 层对动态生成的图片无法识别的问题</li> 
 <li>[优化] layer 组件的 photos 相关样式，上下切换图标调整到页面左右边缘，图片描述和序号调整到页面底部</li> 
 <li>[修复] form 组件的 name="arr[]" 在元素动态插入后出现序号异常的问题 <a href="https://gitee.com/sentsin/layui/issues/I3HY4U" target="_blank">#I3HY4U -Gitee</a></li> 
 <li>[优化] laytpl 组件，支持解析复杂反斜杠 #780 -Github</li> 
 <li>[修复] upload 组件当开启进度条且拖拽文件上传时出现报错问题</li> 
 <li>[修复] table 组件当 cols 表头设置了 templet 为函数时，存在返回 &#123;多余字段: "NaN"&#125; 的问题</li> 
 <li>[优化] table 组件的自动渲染</li> 
 <li>[优化] 底层 layui.link() 方法</li> 
</ul>
                                        </div>
                                      
</div>
            