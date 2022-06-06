
---
title: 'LiteFlow v2.7.0 版本发布，小而强大的规则引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://www.oschina.net/news/198593/images/1.png'
author: 开源中国
comments: false
date: Mon, 06 Jun 2022 03:26:00 GMT
thumbnail: 'https://www.oschina.net/news/198593/images/1.png'
---

<div>   
<div class="content">
                                                                                            <h2>一</h2> 
<p>LiteFlow的重大更新版本v2.7.0今天正式发布！</p> 
<p>同时对于2.7.0的版本，整个文档很多章节也重新写了，补了很多文档。这次的文档比之前更加详细。对用户更加友好了。</p> 
<p>对于2.6.X版本的用户，这次保留了以前的文档。您可以继续使用。2.6.14将成为2.6.X的最后一个稳定版本。</p> 
<p>新的版本去除了Slot的概念。取而代之的是用户能用任意的类去变成上下文。这和slot本质是差不多的，但是用户能在上下文上可以任意扩展了。</p> 
<p>LiteFlow是一个轻量，快速，稳定可编排的JAVA开源规则引擎。如果你是第一次知道这个项目，可以去官网或相关的主页进行了解：</p> 
<blockquote> 
 <p>项目官网:</p> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fliteflow.yomahub.com" target="_blank">https://liteflow.yomahub.com</a></p> 
 <p>gitee托管仓库：</p> 
 <p><a href="https://gitee.com/dromara/liteFlow">https://gitee.com/dromara/liteFlow</a></p> 
 <p>github托管仓库：</p> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdromara%2Fliteflow" target="_blank">https://github.com/dromara/liteflow</a></p> 
</blockquote> 
<h2>二</h2> 
<p>发布新版本之际正好是上海2个多月疫情后的首个复工日，在被封了2个多月后，没有任何时候比现在更想去上班。。。</p> 
<p>所以这次新版本发布，我改版了官网。在暗黑了一年半之后，LiteFlow官网终于支持了白天模式。去旧迎新，迎接光明。官网相比之前，厚重感少了不少，更加简洁了。不知道你们觉得如何呢。</p> 
<p><img alt src="https://www.oschina.net/news/198593/images/1.png" referrerpolicy="no-referrer"><img alt src="https://oscimg.oschina.net/oscnet/up-0a11b71828e8472d8adc9e09a0ea2e57e41.png" referrerpolicy="no-referrer"></p> 
<p>曾经有小伙伴和我吐槽，暗黑模式看的眼睛疼。这次我终于兑现了。</p> 
<h2>三</h2> 
<p>这次更新列表如下：</p> 
<pre><code>特性 #I588BO 对Slot模型的重构，在用户使用中去除Slot模型的概念，引入上下文的概念

https://gitee.com/dromara/liteFlow/issues/I588BO

特性 #I4U5S3 liteFlow日志级别打印开关设置

https://gitee.com/dromara/liteFlow/issues/I4U5S3

增强 #I58VVV 对core的package结构进行整理

https://gitee.com/dromara/liteFlow/issues/I58VVV

增强 #I595MU 在slot的元数据里增加每个组件执行的耗时和是否成功结果

https://gitee.com/dromara/liteFlow/issues/I595MU

增强 #I56ZQ3 打印步骤与执行时间

https://gitee.com/dromara/liteFlow/issues/I56ZQ3

增强 #I5A55K 在NodeComponent里重新加上beforeProcess和afterProcess方法

https://gitee.com/dromara/liteFlow/issues/I5A55K

增强 #I5851Y 对启动初始化的报错进行区分下，现在报错粒度太粗

https://gitee.com/dromara/liteFlow/issues/I5851Y

增强 #I5851R 对自定义组件名进行trim，防止开发者手误有空格

https://gitee.com/dromara/liteFlow/issues/I5851R

修复 #I4XRBA 关于when和then混合使用时(有any和isAccess的情况下)，then的节点先执行的问题

https://gitee.com/dromara/liteFlow/issues/I4XRBA

修复 #I4TJB0 自定义的Slot类必须有无惨构建

https://gitee.com/dromara/liteFlow/issues/I4TJB0

修复 #I4I730 this.setIsEnd(true)主动终止,2.6.4中抛出的异常ChainEndException还是打印error日志

https://gitee.com/dromara/liteFlow/issues/I4I730
</code></pre> 
<h2>四</h2> 
<p>如果你对这个项目感兴趣或是使用中遇到问题，可以加社区群进行反馈，社区群非常活跃，有不少开源和业界大佬，也能进行一些技术课题上的讨论，希望对技术感兴趣的你能加入社区。</p> 
<p>加群方式为：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fliteflow.yomahub.com%2Fpages%2F73c2c3%2F" target="_blank">https://liteflow.yomahub.com/pages/73c2c3/</a></p> 
<p>开源不易，为了开源项目的更好推广，如果你的项目中用了LiteFlow框架并且还觉得不错的话，希望可以在以下地址登记你的公司，登记的公司都会更新到文档中的用户一栏中。</p> 
<p>登记链接为：<a href="https://gitee.com/dromara/liteFlow/issues/I3CM7N">https://gitee.com/dromara/liteFlow/issues/I3CM7N</a></p>
                                        </div>
                                      
</div>
            