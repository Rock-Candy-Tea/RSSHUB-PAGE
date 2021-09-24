
---
title: 'LiteFlow 2.6.0 正式版发行注记'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7532'
author: 开源中国
comments: false
date: Fri, 24 Sep 2021 14:25:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7532'
---

<div>   
<div class="content">
                                                                                            <h2>前言</h2> 
<p>LiteFlow在今年8月发布了2.6.0-BETA1版本。时隔一个月，我们今天发布了LiteFlow 2.6.0的正式版本~。</p> 
<p>其实这算不上高效，因为还有其他项目要忙。但是看着LiteFlow社区的快速增长，我之后会保持一个月发一个版本的频率。</p> 
<p>感谢社区的小伙伴在使用过程中给LiteFlow提供了诸多建议和issue，我每个版本的迭代主要就来自于你们的issue。而且越来越多的童鞋愿意贡献社区，我相信这是一个正向的循环。</p> 
<p>LiteFlow的起初是为了公司的一个业务量身定制的中间件，但是和其他项目不同的是，从一开始，LiteFlow就向着开源的方向去进行的，所以没有历史包袱，也没有内部依赖问题。在进行了几十个版本的迭代后，目前LiteFlow已经可以达到生产级别的应用。也有很多公司引入了此框架作为核心业务的驱动器。</p> 
<p>但我相信，LiteFlow还可以做更多的东西，这些仅仅是一个基础。</p> 
<p>如果你是第一次知道LiteFlow这款框架，可以移步以下链接进行了解：</p> 
<blockquote> 
 <p>LiteFlow官网：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyomahub.com%2Fliteflow" target="_blank">https://yomahub.com/liteflow</a></p> 
 <p>Gitee仓库托管主页：<a href="https://gitee.com/dromara/liteFlow">https://gitee.com/dromara/liteFlow</a></p> 
 <p>Github仓库托管主页：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdromara%2Fliteflow" target="_blank">https://github.com/dromara/liteflow</a></p> 
</blockquote> 
<p>也可以看我之前发布的一篇介绍LiteFlow这个框架的文章</p> 
<blockquote> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2Fxyydmtk_a5R1zbg3EeORaw" target="_blank">https://mp.weixin.qq.com/s/xyydmtk_a5R1zbg3EeORaw</a></p> 
</blockquote> 
<h2>2.6.0正式版本</h2> 
<p>这次LiteFlow重构了部分底层核心代码，更加稳定且优雅。同时带来了2个新特性，2个增强，修复了4个bug</p> 
<p><strong>更新日志如下：</strong></p> 
<p>特性 #I4892Y 提供私有投递特性，slot这种结构体系，对于多个子线程进入同一个组件的情况下，不容易区分不同的传值。无法做到重用组件</p> 
<p><a href="https://gitee.com/dromara/liteFlow/issues/I4892Y">https://gitee.com/dromara/liteFlow/issues/I4892Y</a></p> 
<p>特性 #I49FDK 中断重试目前是全局的，希望增加针对个别组件和特定exception</p> 
<p><a href="https://gitee.com/dromara/liteFlow/issues/I49FDK">https://gitee.com/dromara/liteFlow/issues/I49FDK</a></p> 
<p>增强 #I49JP1 DataBus中SlotSize的大小不支持动态扩展，无法应对高并发下的流量突增</p> 
<p><a href="https://gitee.com/dromara/liteFlow/issues/I49JP1">https://gitee.com/dromara/liteFlow/issues/I49JP1</a></p> 
<p>增强 #I45QAJ 支持自定义的zkNodePath</p> 
<p><a href="https://gitee.com/dromara/liteFlow/issues/I45QAJ">https://gitee.com/dromara/liteFlow/issues/I45QAJ</a></p> 
<p>修复 #I49EHH setIsEnd设计的不合理性</p> 
<p><a href="https://gitee.com/dromara/liteFlow/issues/I49EHH">https://gitee.com/dromara/liteFlow/issues/I49EHH</a></p> 
<p>修复 #I4BAJC setIsEnd结束的流程不需要进行重试</p> 
<p><a href="https://gitee.com/dromara/liteFlow/issues/I4BAJC">https://gitee.com/dromara/liteFlow/issues/I4BAJC</a></p> 
<p>修复 #I49L1S 初始化DataBus的数据槽索引QUEUE大小的时候容量设置有问题</p> 
<p><a href="https://gitee.com/dromara/liteFlow/issues/I49L1S">https://gitee.com/dromara/liteFlow/issues/I49L1S</a></p> 
<p>修复 #I46U6Y 自定义JsonParse,调用flowExecutor的reloadRule,抛出异常</p> 
<p><a href="https://gitee.com/dromara/liteFlow/issues/I46U6Y">https://gitee.com/dromara/liteFlow/issues/I46U6Y</a></p> 
<h2>蓝图</h2> 
<p>我承诺会在2.7.0版本中推出UI插件进行可视化编排，这个计划依旧不会改变。</p> 
<p>但是在2.7.0之前，可能还会有1到2个版本进行迭代。所以，大家也不用催我哈。如果有UI方面擅长的小伙伴且愿意贡献开源社区，也请和我联系。因为我并不擅长UI前端，也不愿意学了。。。因为懒。。已经放弃。</p> 
<h2>关于贡献</h2> 
<p>社区有很多小伙伴很热心的要参与贡献，我会在之后把贡献准则更新到官网上。</p> 
<p>达成准则即成为commiter。</p>
                                        </div>
                                      
</div>
            