
---
title: 'PESCMS DOC 2.0 发布，系统重构'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1527'
author: 开源中国
comments: false
date: Tue, 10 Aug 2021 02:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1527'
---

<div>   
<div class="content">
                                                                                            <p>我们很高兴地宣布PESCMS DOC v2.0.0 的到来。历史2个多月，我们将系统重构，让大家更好地编写文档，让万物有迹可查，让问题得到专业的解决方案</p> 
<h2>主要特征</h2> 
<ul> 
 <li> <p>集成富文本编辑器和MarkDown编辑器。</p> </li> 
 <li> <p>权限管理、阅读权限。</p> </li> 
 <li> <p>无限层级的文档</p> </li> 
 <li> <p>通过接口编写PESCMS DOC文档（后续更新支持）</p> </li> 
 <li> <p>根据API请求，编写或生成文档（后续更新支持）</p> </li> 
</ul> 
<h2>运行环境</h2> 
<ul> 
 <li> <p>PHP7.0及以上版本</p> </li> 
 <li> <p>Mysql5.5及以上版本</p> </li> 
 <li> <p>现代浏览器</p> </li> 
</ul> 
<h2>为什么重构？</h2> 
<p>DOC1.x版本早期的数据库设计是基于论坛结构形式。文档节点也沿用此逻辑，导致文档只能创建二级，限制了文档编写的精细度。其次，1.X版本将管理和文档模板集合在一起，对于编写模板主题来说不是一个很好的设定。综合各方面考虑，决定重构了DOC系统。</p> 
<h3>新旧主要差异对比</h3> 
<ol> 
 <li> <p>新版移除双击编辑文档模式，改为后端编辑模式。</p> </li> 
 <li> <p>支持2种形式的编辑器，随时切换编辑器，写作格式不局限于一种。</p> </li> 
 <li> <p>权限管理和阅读权限。设定不同账户，不同内容。</p> </li> 
 <li> <p>无限层级编写文档，三种形式文档：文章、目录和外链。满足文档编写的多样性和减少重复文档的编写。</p> </li> 
 <li> <p>模板主题、应用插件的支持。</p> </li> 
</ol> 
<h2>期待</h2> 
<p>DOC2.0版本重构完成后，后续还有不少工作需要继续完善。例如：导出功能、更加细化的阅读权限、模板主题和应用插件的补充……敬请期待后续的更新！</p> 
<h2>下载和示例</h2> 
<p>PESCMS DOC 可以从<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.pescms.com%2Fdownload%2F3.html" target="_blank">官网</a>下载，或者直接下载<a href="https://gitee.com/fallBirds/PESCMS-DOC" target="_self">源码</a>。查阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocument.pescms.com%2Farticle%2F4.html" target="_blank">文档</a>获取更详尽的内容。我们也提供<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc.pescms.com" target="_blank">PESCMS DOC演示站</a>。</p>
                                        </div>
                                      
</div>
            