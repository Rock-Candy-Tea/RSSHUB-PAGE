
---
title: 'LiteFlow v2.8.5 发版注记'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://www.oschina.net/news/images/cover.png'
author: 开源中国
comments: false
date: Mon, 29 Aug 2022 03:19:00 GMT
thumbnail: 'https://www.oschina.net/news/images/cover.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt src="https://www.oschina.net/news/images/cover.png" referrerpolicy="no-referrer"><img height="762" src="https://oscimg.oschina.net/oscnet/up-488127065dc70e9cfb9354da14bdeca2c4b.png" width="1794" referrerpolicy="no-referrer"></p> 
<h2>一</h2> 
<p>LiteFlow v2.8.5今天正式发布！完全兼容2.8.X版本。</p> 
<p>同时IDEA插件LiteFlowX 1.0.4今天同时发布！大家可在插件市场里进行下载/更新。</p> 
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
<p>这次带来的版本特性是条件表达式的增加，也就是在EL流程语法中支持了IF...ELIF...ELSE的用法。</p> 
<p>具体如何用，请参照文档中<code>EL规则的写法/条件表达式</code>这一章。</p> 
<p>同时2.8.5版本增强了若干功能，其中解决了一直诟病的EL语法报错太过于单一的问题。现在会有更加详细的报错提示。</p> 
<p>截止到2.8.5为止，LiteFlow一共拥有了933个测试用例！庞大的测试用例让LiteFlow更加稳定和健壮。</p> 
<p>LiteFlow从之前就保证了至少1月两更的频率，目前社区超过了1000人，star接近了2.8k。社区非常活跃，各种公众号大佬，开源作者也在群里。如果你想加入社区，可以在LiteFlow的官网点击<code>加入群聊</code>。</p> 
<p>官网更是准备了官方PPT，以供使用者进行公司内部分享。赶紧来看看吧。</p> 
<h2>二</h2> 
<p>本次更新列表如下：</p> 
<p> </p> 
<pre><code>特性 #I5KTST IF三元符语法的添加以及IF ELIF ELSE语法的添加

https://gitee.com/dromara/liteFlow/issues/I5KTST

增强 #I5O22X 增加EL解析中的报错详细信息

https://gitee.com/dromara/liteFlow/issues/I5O22X

增强 #I5MZJY 解决循环调用同步的隐式流程，参数只能取一次的问题

https://gitee.com/dromara/liteFlow/issues/I5MZJY

修复 #I5NH56 switch组件对于cglib代理过的bean目前处理的不够全面

https://gitee.com/dromara/liteFlow/issues/I5NH56

修复 I5NFV3 在zk集群中多个zk地址不生效的bug

https://gitee.com/dromara/liteFlow/issues/I5NFV3
</code></pre> 
<p> </p> 
<p><img height="500" src="https://oscimg.oschina.net/oscnet/up-f348543c0b757f3db81b52e88b3805f65c2.jpg" width="900" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            