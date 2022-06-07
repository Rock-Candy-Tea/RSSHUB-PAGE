
---
title: 'LiteFlow v2.7.1 版本发布 & 新版官网上线'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-472e30bdb240c1537441a2a330265eae53d.jpg'
author: 开源中国
comments: false
date: Tue, 07 Jun 2022 13:49:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-472e30bdb240c1537441a2a330265eae53d.jpg'
---

<div>   
<div class="content">
                                                                                            <h2 style="margin-left:0; margin-right:0; text-align:left"><img height="383" src="https://oscimg.oschina.net/oscnet/up-472e30bdb240c1537441a2a330265eae53d.jpg" width="900" referrerpolicy="no-referrer"></h2> 
<h2 style="margin-left:0; margin-right:0; text-align:left">一</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">LiteFlow 的重大更新版本 v2.7.1 今天正式发布！</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">同时对于 2.7.1 的版本，整个文档很多章节也重新写了，补了很多文档。这次的文档比之前更加详细。对用户更加友好了。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">对于 2.6.X 版本的用户，这次保留了以前的文档。您可以继续使用。2.6.14 将成为 2.6.X 的最后一个稳定版本。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">新的版本去除了 Slot 的概念。取而代之的是用户能用任意的类去变成上下文。这和 slot 本质是差不多的，但是用户能在上下文上可以任意扩展了。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">还增加了一个重要特性，就是组件事件的回调。根据这个特性可以玩出更多的花样。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">LiteFlow 是一个轻量，快速，稳定可编排的 JAVA 开源规则引擎。如果你是第一次知道这个项目，可以去官网或相关的主页进行了解：</p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">项目官网:</p> 
 <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fliteflow.yomahub.com" target="_blank">https://liteflow.yomahub.com</a></p> 
 <p style="margin-left:0; margin-right:0">gitee 托管仓库：</p> 
 <p style="margin-left:0; margin-right:0"><a href="https://gitee.com/dromara/liteFlow">https://gitee.com/dromara/liteFlow</a></p> 
 <p style="margin-left:0; margin-right:0">github 托管仓库：</p> 
 <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdromara%2Fliteflow" target="_blank">https://github.com/dromara/liteflow</a></p> 
</blockquote> 
<h2 style="margin-left:0; margin-right:0; text-align:left">二</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">发布新版本之际正好是上海 2 个多月疫情后的首个复工日，在被封了 2 个多月后，没有任何时候比现在更想去上班。。。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">所以这次新版本发布，我改版了官网。在暗黑了一年半之后，LiteFlow 官网终于支持了白天模式。去旧迎新，迎接光明。官网相比之前，厚重感少了不少，更加简洁了。不知道你们觉得如何呢。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="file" src="https://oscimg.oschina.net/oscnet/up-b0330d41bee8b6c25170d3bb577351f0ebf.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">曾经有小伙伴和我吐槽，暗黑模式看的眼睛疼。这次我终于兑现了。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">三</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">这次更新列表如下：</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code>特性 <span style="color:#6f42c1">#I588BO</span> 对<span style="color:#d73a49">Slot</span>模型的重构，在用户使用中去除<span style="color:#d73a49">Slot</span>模型的概念，引入上下文的概念

<span style="color:#d73a49">https</span>:<span style="color:#6a737d">//gitee.com/dromara/liteFlow/issues/I588BO</span>

特性 <span style="color:#6f42c1">#I5AYM5</span> 组件事件回调特性支持

<span style="color:#d73a49">https</span>:<span style="color:#6a737d">//gitee.com/dromara/liteFlow/issues/I5AYM5</span>

特性 <span style="color:#6f42c1">#I4U5S3</span> <span style="color:#d73a49">liteFlow</span>日志级别打印开关设置

<span style="color:#d73a49">https</span>:<span style="color:#6a737d">//gitee.com/dromara/liteFlow/issues/I4U5S3</span>

增强 <span style="color:#6f42c1">#I58VVV</span> 对<span style="color:#d73a49">core</span>的<span style="color:#d73a49">package</span>结构进行整理

<span style="color:#d73a49">https</span>:<span style="color:#6a737d">//gitee.com/dromara/liteFlow/issues/I58VVV</span>

增强 <span style="color:#6f42c1">#I595MU</span> 在<span style="color:#d73a49">slot</span>的元数据里增加每个组件执行的耗时和是否成功结果

<span style="color:#d73a49">https</span>:<span style="color:#6a737d">//gitee.com/dromara/liteFlow/issues/I595MU</span>

增强 <span style="color:#6f42c1">#I56ZQ3</span> 打印步骤与执行时间

<span style="color:#d73a49">https</span>:<span style="color:#6a737d">//gitee.com/dromara/liteFlow/issues/I56ZQ3</span>

增强 <span style="color:#6f42c1">#I5A55K</span> 在<span style="color:#d73a49">NodeComponent</span>里重新加上<span style="color:#d73a49">beforeProcess</span>和<span style="color:#d73a49">afterProcess</span>方法

<span style="color:#d73a49">https</span>:<span style="color:#6a737d">//gitee.com/dromara/liteFlow/issues/I5A55K</span>

增强 <span style="color:#6f42c1">#I5851Y</span> 对启动初始化的报错进行区分下，现在报错粒度太粗

<span style="color:#d73a49">https</span>:<span style="color:#6a737d">//gitee.com/dromara/liteFlow/issues/I5851Y</span>

增强 <span style="color:#6f42c1">#I5851R</span> 对自定义组件名进行<span style="color:#d73a49">trim</span>，防止开发者手误有空格

<span style="color:#d73a49">https</span>:<span style="color:#6a737d">//gitee.com/dromara/liteFlow/issues/I5851R</span>

修复 <span style="color:#6f42c1">#I4XRBA</span> 关于<span style="color:#d73a49">when</span>和then混合使用时(有any和isAccess的情况下)，then的节点先执行的问题

<span style="color:#005cc5">https</span>:<span style="color:#6a737d">//gitee.com/dromara/liteFlow/issues/I4XRBA</span>

修复 #I4TJB0 自定义的Slot类必须有无惨构建

<span style="color:#005cc5">https</span>:<span style="color:#6a737d">//gitee.com/dromara/liteFlow/issues/I4TJB0</span>

修复 #I4I730 this.setIsEnd(true)主动终止,<span>2.6</span>.<span>4</span>中抛出的异常ChainEndException还是打印error日志

<span style="color:#005cc5">https</span>:<span style="color:#6a737d">//gitee.com/dromara/liteFlow/issues/I4I730</span>

修复 #I5AVD2 修复全局切面中拿不到组件的别名了

<span style="color:#005cc5">https</span>:<span style="color:#6a737d">//gitee.com/dromara/liteFlow/issues/I5AVD2</span>

修复 #I5AYI1 修复默认值提醒有误差

<span style="color:#005cc5">https</span>:<span style="color:#6a737d">//gitee.com/dromara/liteFlow/issues/I5AYI1</span>
</code></pre> 
<h2 style="margin-left:0; margin-right:0; text-align:left">四</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">如果你对这个项目感兴趣或是使用中遇到问题，可以加社区群进行反馈，社区群非常活跃，有不少开源和业界大佬，也能进行一些技术课题上的讨论，希望对技术感兴趣的你能加入社区。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">加群方式为：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fliteflow.yomahub.com%2Fpages%2F73c2c3%2F" target="_blank">https://liteflow.yomahub.com/pages/73c2c3/</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">开源不易，为了开源项目的更好推广，如果你的项目中用了 LiteFlow 框架并且还觉得不错的话，希望可以在以下地址登记你的公司，登记的公司都会更新到文档中的用户一栏中。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">登记链接为：<a href="https://gitee.com/dromara/liteFlow/issues/I3CM7N">https://gitee.com/dromara/liteFlow/issues/I3CM7N</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            