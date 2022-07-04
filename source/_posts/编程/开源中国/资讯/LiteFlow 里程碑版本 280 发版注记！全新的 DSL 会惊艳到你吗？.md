
---
title: 'LiteFlow 里程碑版本 2.8.0 发版注记！全新的 DSL 会惊艳到你吗？'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://www.oschina.net/news/201728/images/cover.png'
author: 开源中国
comments: false
date: Mon, 04 Jul 2022 12:32:00 GMT
thumbnail: 'https://www.oschina.net/news/201728/images/cover.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt src="https://www.oschina.net/news/201728/images/cover.png" referrerpolicy="no-referrer"></p> 
<p><img height="383" src="https://oscimg.oschina.net/oscnet/up-64f2bfd7bd3c944c7097bd0c6493b121404.png" width="900" referrerpolicy="no-referrer"></p> 
<h2>一</h2> 
<p><img height="2624" src="https://oscimg.oschina.net/oscnet/up-d4542996153234d7dfa0bd64f00aff21a18.png" width="3848" referrerpolicy="no-referrer"></p> 
<p>New version! 2.8.0 go!!!</p> 
<p>这是我在提交中央仓库前写下的简短description。我希望这个版本能把LiteFlow带向更远的地方。</p> 
<p>曾经在半年前就计划的新的DSL计划，但是因为底层还不完善，花了半年时间几乎重写了整个底层慢慢迭代，在今天终于完成全新DSL！</p> 
<p><strong>LiteFlow今天正式推出里程碑版本2.8.0！</strong>正式迈入了2.8.X系列。这次LiteFlow带来了全新设计的规则表达式，带来质的飞跃！任何复杂的DAG图用LiteFlow去编排都已经是轻而易举的事了。</p> 
<p>并且2.8.0在规则层面是向下兼容的。如果你在用之前的版本，只需很小的代价便可切换到2.8.X中。在官网中也提供了升级版本的说明文档。</p> 
<p>如果你是第一次见到LiteFlow，那么我可以给你这么形容：</p> 
<p><strong>LiteFlow是一个灵动的，高成长性的，社区驱动的，丝滑且正在变得越来越好用的国产开源规则引擎。</strong></p> 
<p>你如果对LiteFlow感兴趣的话，请移步官网进行了解：</p> 
<blockquote> 
 <p>官网：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fliteflow.yomahub.com%2F" target="_blank">https://liteflow.yomahub.com/</a></p> 
 <p>Gitee托管仓库：<a href="https://gitee.com/dromara/liteFlow">https://gitee.com/dromara/liteFlow</a></p> 
 <p>Github托管仓库：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdromara%2Fliteflow" target="_blank">https://github.com/dromara/liteflow</a></p> 
</blockquote> 
<h2>二</h2> 
<p>值得一提的是，在LiteFlow 2.8.0发布的前几天，LiteFlow终于收获了开源中国的GVP的认可。感谢官方平台对LiteFlow项目的推荐和肯定。</p> 
<p><img height="1488" src="https://oscimg.oschina.net/oscnet/up-66ae2e35dd484006f959a2650897756e776.jpg" width="2350" referrerpolicy="no-referrer"></p> 
<h2>三</h2> 
<p>这次不仅推出了全新的DSL，还增强了大量的功能，这次版本的issue数量可能是发版最多的一次。</p> 
<p>本次2.8.0更新列表如下：</p> 
<pre><code>特性 #I5CW7I 【版本特性】构造全新的EL规则表达式

https://gitee.com/dromara/liteFlow/issues/I5CW7I

特性 #I5CHYH 提供多上下文支持的特性

https://gitee.com/dromara/liteFlow/issues/I5CHYH

特性 #I5CJHI 支持requestId的自定义生成器

https://gitee.com/dromara/liteFlow/issues/I5CJHI

增强 #I5BR8P 组件打印信息，希望能定制带上别名

https://gitee.com/dromara/liteFlow/issues/I5BR8P

增强 #I4TGGV 子流程中的finally节点没有执行

https://gitee.com/dromara/liteFlow/issues/I4TGGV

增强 #I5BGGK 引入的dom4j 1.6.1版本报安全性问题，麻烦升级一下

https://gitee.com/dromara/liteFlow/issues/I5BGGK

增强 #I5BR5M chain重名的检测

https://gitee.com/dromara/liteFlow/issues/I5BR5M

增强 #I5BRFN 提取公共方法减少重复代码，去除魔法值

https://gitee.com/dromara/liteFlow/issues/I5BRFN

增强 #I5BVCU 改变核心结构，Condition也成为一个可执行单元

https://gitee.com/dromara/liteFlow/issues/I5BVCU

增强 #I5C3OC 增加xml的dtd文件，从而提供格式输入提示和较验

https://gitee.com/dromara/liteFlow/issues/I5C3OC

增强 #I5CHYJ 去除FlowExecutor中直接返回上下文的执行方法

https://gitee.com/dromara/liteFlow/issues/I5CHYJ

增强 #I5CW1E 调整LiteflowConfig包装类型

https://gitee.com/dromara/liteFlow/issues/I5CW1E

增强 #I5D89I 内部新增switchCondition，把选择组件独立出来做，更好的扩展

https://gitee.com/dromara/liteFlow/issues/I5D89I

增强 #I5DEGQ 增加Switch的节点类型，以替换cond节点的的定义

https://gitee.com/dromara/liteFlow/issues/I5DEGQ

增强 #I5E17C 对parser结构提取公共方法减少重复代码

https://gitee.com/dromara/liteFlow/issues/I5E17C

修复 #I58VZD 流程多次使用同一个条件组件问题

https://gitee.com/dromara/liteFlow/issues/I58VZD

修复 #I4IOLB when在解析时某些情况下不会合并

https://gitee.com/dromara/liteFlow/issues/I4IOLB
</code></pre> 
<h2>四</h2> 
<p>关于全新DSL的学习和如何使用，大家可以去官网查看。</p> 
<p>2.8.X是兼容之前的规则写法的，对于旧版本如何升级到新版本，在官网中也作了详细的说明。</p> 
<p>我相信好的文档一定是开源项目一个非常重要的部分，所以，新版本之中我们对文档增补了大量的内容，来帮助大家更好的理解这个框架。大家如果在阅读过程中对文档内容有任何建议也欢迎在社区群告诉我们。</p> 
<p>LiteFlow有一个非常好的社区群，如果你在使用中有任何疑问，都可以在社区群里进行提问，一般是有问必答。一直以来，LiteFlow始终以社区为根本，所有的迭代方向都是由社区驱动的。社区也有很多的开源作者，公众号大佬。如果你想加入社区，可以在以下地址找到加入社区群的方式：</p> 
<blockquote> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fliteflow.yomahub.com%2Fpages%2F73c2c3%2F" target="_blank">https://liteflow.yomahub.com/pages/73c2c3/</a></p> 
</blockquote> 
<h2>五</h2> 
<p>未来LiteFlow会以更快的速度进行迭代，在LiteFlow的RoadMap中，一直被大家催的UI编排会在3.0的时候以生态插件的形式和大家见面。当然这中间还有2.9.X版本，以目前的迭代速度，这一天应该不会太远。</p> 
<p>请大家继续关注，感谢一路走来支持LiteFlow的你们，我们会努力把国产的规则引擎做到极致。</p>
                                        </div>
                                      
</div>
            