
---
title: 'LiteFlow v2.8.3发版注记，轻量优雅的国产规则引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-e1c9123ecf016ab65d21c885ddb7da200a5.png'
author: 开源中国
comments: false
date: Wed, 27 Jul 2022 11:18:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-e1c9123ecf016ab65d21c885ddb7da200a5.png'
---

<div>   
<div class="content">
                                                                                            <p><img height="700" src="https://oscimg.oschina.net/oscnet/up-e1c9123ecf016ab65d21c885ddb7da200a5.png" width="1674" referrerpolicy="no-referrer"></p> 
<h2>一</h2> 
<p>LiteFlow v2.8.3今天正式发布！完全兼容2.8.X版本。</p> 
<p>我们始终在坚持让这个框架更好用，更加人性化。</p> 
<p>所有的issue均来自于社区，LiteFlow是一个由社区驱动的开源项目。我们的社区非常活跃，有很多人正在以各种方式帮助这个项目变的越来越好。</p> 
<p><strong>LiteFlow是一个灵动的，高成长性的，社区驱动的，丝滑且正在变得越来越好用的国产开源规则引擎。</strong></p> 
<p>如果你是第一次知道这个项目，可以去官网或相关的主页进行了解：</p> 
<blockquote> 
 <p>项目官网:</p> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fliteflow.yomahub.com" target="_blank">https://liteflow.yomahub.com</a></p> 
 <p>gitee托管仓库：</p> 
 <p><a href="https://gitee.com/dromara/liteFlow">https://gitee.com/dromara/liteFlow</a></p> 
 <p>github托管仓库：</p> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdromara%2Fliteflow" target="_blank">https://github.com/dromara/liteflow</a></p> 
</blockquote> 
<h2>二</h2> 
<p>这个版本增加了一个特性，原先有小伙伴反应特殊的组件名不能定义，这个版本新增了一个包装语法<code>node</code>，能彻底解决这个问题。并且新推出了替补节点概念。通过自定义一个替补节点，可以让不存在的节点也能有兜底功能。</p> 
<p>相关文档：</p> 
<blockquote> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fliteflow.yomahub.com%2Fpages%2F2df3d9%2F" target="_blank">https://liteflow.yomahub.com/pages/2df3d9/</a></p> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fliteflow.yomahub.com%2Fpages%2F79289a%2F" target="_blank">https://liteflow.yomahub.com/pages/79289a/</a></p> 
</blockquote> 
<p>这个版本另外增强了脚本组件的获取流程参数的场景，重构了parser的代码，更加优雅。</p> 
<p>LiteFlow v2.8.3版本的测试用例达到了888个，好吉利的数字！</p> 
<p><img height="274" src="https://oscimg.oschina.net/oscnet/up-fa10ed71a5839647d178d73c176d1e45fb6.png" width="872" referrerpolicy="no-referrer"></p> 
<p>我们每次发版，都会跑通所有的测试用例和进行压力测试。Release的版本都可以放心升级！</p> 
<h2>三</h2> 
<p>本次的更新列表如下：</p> 
<pre><code>特性 #I5IA5U 提供节点包装语法+替补节点的功能

https://gitee.com/dromara/liteFlow/issues/I5IA5U

增强 #I5IOC5 LiteFlowResponse提供errorCode的功能

https://gitee.com/dromara/liteFlow/issues/I5IOC5

增强 #I5IJLN 支持脚本里获取requestData

https://gitee.com/dromara/liteFlow/issues/I5IJLN

增强 #I5I1QH 重构查找解析器的代码

https://gitee.com/dromara/liteFlow/issues/I5I1QH
</code></pre> 
<p> </p>
                                        </div>
                                      
</div>
            