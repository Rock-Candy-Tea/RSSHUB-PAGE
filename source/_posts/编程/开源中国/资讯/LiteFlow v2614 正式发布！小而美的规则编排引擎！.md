
---
title: 'LiteFlow v2.6.14 正式发布！小而美的规则编排引擎！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-74c8d25ecc579cb4e0f30ece613ecaec476.jpg'
author: 开源中国
comments: false
date: Mon, 16 May 2022 14:23:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-74c8d25ecc579cb4e0f30ece613ecaec476.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img height="383" src="https://oscimg.oschina.net/oscnet/up-74c8d25ecc579cb4e0f30ece613ecaec476.jpg" width="900" referrerpolicy="no-referrer"></p> 
<h2>一</h2> 
<p>LiteFlow v2.6.14今天正式发布！</p> 
<p>之前有很多人说组件的定义能不能不要那么耦合化，Java的单继承机制让组件无法再继承另外的类了。希望我这里做下调整。</p> 
<p>在2.6.14这个版本中LiteFlow支持了声明式组件，也是这个版本的最主要的特性。</p> 
<p>声明式组件让使用者在定义组件时有了一种新的选择。同时这个对我来说，也是为以后全面迈向声明式打下了一个基础。</p> 
<p>更加方便，更加解耦，更加轻量同时更加强大是LiteFlow这个框架一直追求的。</p> 
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
<p>这个版本做了很长时间。声明式内部主要使用动态代理来实现。起初使用cglib，但是后来发现了cglib的一堆坑，查官方文档花了不少时间。后来果断抛弃了cglib，转而投向了byteBuddy。用了之后才发现byteBuddy果真是动态代理的一大神器，从功能上来说，比cglib强了不少，后续打算专门出篇文章来讲下byteBuddy这个字节码处理框架。</p> 
<p>新特性介绍以及文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fliteflow.yomahub.com%2Fdocs%2Fuser-detail-guide%2Fuser-detail-guide-declare-component" target="_blank">https://liteflow.yomahub.com/docs/user-detail-guide/user-detail-guide-declare-component</a></p> 
<p>新的版本测试用例已经增加到了384个，更多的测试用例，是大家放心使用LiteFlow的基础。每发布一个版本，我也会进行大量测试用例的撰写，用以保证质量。如果遇到小的问题，可以到群里进行反馈，我会第一时间进行修复。</p> 
<p><img alt src="https://www.oschina.net/news/196034/images/1.png" referrerpolicy="no-referrer"></p> 
<p><img height="906" src="https://oscimg.oschina.net/oscnet/up-3b173b8bbfd4a0ee8d78355d26539e1f7d1.png" width="1720" referrerpolicy="no-referrer"></p> 
<h2>三</h2> 
<p>本次更新列表如下：</p> 
<pre><code>特性 #I54VBS 从设计上改善NodeComponent，支持声明式组件

https://gitee.com/dromara/liteFlow/issues/I54VBS

增强 #I57IEJ requestId更换算法，看上去更加整洁

https://gitee.com/dromara/liteFlow/issues/I57IEJ

修复 #I576ZY 修复processor异常后 ICmpAroundAspect里面的aferProcess不能正常执行的问题

https://gitee.com/dromara/liteFlow/issues/I576ZY
</code></pre> 
<h2>四</h2> 
<p>如果你对这个项目感兴趣或是使用中遇到问题，可以加社区群进行反馈，社区群非常活跃，有不少开源和业界大佬，也能进行一些技术课题上的讨论，希望对技术感兴趣的你能加入社区。</p> 
<p>加群方式为：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fliteflow.yomahub.com%2Fblog%2Fgroup-chat" target="_blank">https://liteflow.yomahub.com/blog/group-chat</a></p> 
<p>开源不易，为了开源项目的更好推广，如果你的项目中用了LiteFlow框架并且还觉得不错的话，希望可以在以下地址登记你的公司，登记的公司都会更新到文档中的用户一栏中。</p> 
<p><a href="https://gitee.com/dromara/liteFlow/issues/I3CM7N">https://gitee.com/dromara/liteFlow/issues/I3CM7N</a></p> 
<p>当然你也可以选择请我喝杯咖啡:P，这会是对我以及我努力成果的最大肯定！</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fliteflow.yomahub.com%2Fblog%2Fdonation" target="_blank">https://liteflow.yomahub.com/blog/donation</a></p>
                                        </div>
                                      
</div>
            