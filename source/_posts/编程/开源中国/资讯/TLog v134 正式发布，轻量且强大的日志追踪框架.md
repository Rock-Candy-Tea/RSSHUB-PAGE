
---
title: 'TLog v1.3.4 正式发布，轻量且强大的日志追踪框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-680a612ae0e801a404399b83dde8bd84ce7.png'
author: 开源中国
comments: false
date: Wed, 03 Nov 2021 12:23:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-680a612ae0e801a404399b83dde8bd84ce7.png'
---

<div>   
<div class="content">
                                                                                            <h2>一</h2> 
<p>TLog 1.3.4版本正式发布！相关文档也已做了更新。</p> 
<p>TLog是一款日志工具，十分钟即可接入，支持众多的框架和主流RPC，你几乎不需要做什么，TLog能自动你的日志进行增强，让你的日志马上升级，微服务之间的日志变得可追溯！</p> 
<blockquote> 
 <p>gitee托管仓库：</p> 
 <p><a href="https://gitee.com/dromara/TLog">https://gitee.com/dromara/TLog</a></p> 
 <p>github托管仓库：</p> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdromara%2FTLog" target="_blank">https://github.com/dromara/TLog</a></p> 
 <p>项目主页：</p> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyomahub.com%2Ftlog%2F" target="_blank">https://yomahub.com/tlog/</a></p> 
</blockquote> 
<h2>二</h2> 
<p>从1.3.0到1.3.4，TLog主要围绕着2个方面展开迭代，小的新特性和底层代码的部分重构和优化。</p> 
<p>版本一直用小步走的方式进行迭代，每次迭代的issue不会太多。这也和我的精力有关，维护2个开源项目和写文章的确精力比较分散，催更的小伙伴请见谅。</p> 
<p>我顺便看了下，TLog从1.0.0开源以来，总共已经发行了30个版本，加上这个版本就是31个版本。目前TLog核心功能相对于已经很稳定了，性能也和原生日志几乎没有差别，每一次迭代都是一次进步。只为了让开发者能更方便的使用。</p> 
<p><img height="1796" src="https://oscimg.oschina.net/oscnet/up-680a612ae0e801a404399b83dde8bd84ce7.png" width="1080" referrerpolicy="no-referrer"></p> 
<h2>三</h2> 
<p><strong>1.3.4版本更新点如下:</strong></p> 
<p>特性: #I4F9Y5 支持spring的 @Scheduled定时器</p> 
<p><a href="https://gitee.com/dromara/TLog/issues/I4F9Y5">https://gitee.com/dromara/TLog/issues/I4F9Y5</a></p> 
<p>增强: #I4FC3T 改善自定义标签的底层实现，使用表达式引擎来实现</p> 
<p><a href="https://gitee.com/dromara/TLog/issues/I4FC3T">https://gitee.com/dromara/TLog/issues/I4FC3T</a></p> 
<p>修复: #I4F4SL 解决在logback的MDC模式下，有多个%X的情况下会重复输出标签的问题</p> 
<p><a href="https://gitee.com/dromara/TLog/issues/I4F4SL">https://gitee.com/dromara/TLog/issues/I4F4SL</a></p> 
<h2>四</h2> 
<p>如果你在使用TLog中有任何问题，可以加入交流讨论群进行询问，也可以在gitee/github的issue里进行记录。</p>
                                        </div>
                                      
</div>
            