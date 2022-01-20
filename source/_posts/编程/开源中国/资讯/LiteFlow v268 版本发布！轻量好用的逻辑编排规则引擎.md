
---
title: 'LiteFlow v2.6.8 版本发布！轻量好用的逻辑编排规则引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-3b5f9037d22f0494ca68984318819b0981b.jpg'
author: 开源中国
comments: false
date: Thu, 20 Jan 2022 13:41:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-3b5f9037d22f0494ca68984318819b0981b.jpg'
---

<div>   
<div class="content">
                                                                                            <p><img height="383" src="https://oscimg.oschina.net/oscnet/up-3b5f9037d22f0494ca68984318819b0981b.jpg" width="900" referrerpolicy="no-referrer"></p> 
<h2>前言</h2> 
<p>LiteFlow v2.6.8正式发布！Release版本已上中央仓库，官网文档也作了更新支持。</p> 
<p>2022年的第一个迭代版本。这个版本相关的issue有挺多的。基本都来自于社区小伙伴的建议。</p> 
<p>这个版本的重头戏就是底层解析模块的重构，以往有很多地方不太合理，LiteFlow本身的初衷就是为解耦业务模块而生，为优雅代码而生，但是本身自己在解析构建模块却抽象的不够好，我自己也觉得有点讽刺。所以在2.6.8版本中，花了大精力重新写了解析构建模块。同时也有了版本新特性：可以动态构建流程链路。</p> 
<p>2021年社区突破了500人，微信已经开了二群，同时项目也获得了2021年度中国开源最受欢迎的30大开源项目之一。2022年继续这份执着和热爱。有想加入社区群的小伙伴，可以在公众号里加我好友，我会拉你进群。</p> 
<h2>关于项目</h2> 
<p>LiteFlow是一个轻量级的规则引擎，可以很巧妙的去解耦你复杂的业务逻辑，进行热编排，即时调整策略。</p> 
<p>如果你是第一次知道这个项目，可以去官网或相关的主页进行了解</p> 
<blockquote> 
 <p>项目官网:</p> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fliteflow.yomahub.com" target="_blank">https://liteflow.yomahub.com</a></p> 
 <p>gitee托管仓库：</p> 
 <p><a href="https://gitee.com/dromara/liteFlow">https://gitee.com/dromara/liteFlow</a></p> 
 <p>github托管仓库：</p> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdromara%2Fliteflow" target="_blank">https://github.com/dromara/liteflow</a></p> 
</blockquote> 
<h2>v2.6.8更新列表</h2> 
<p>特性 #I4GS07 代码动态组件装配的特性</p> 
<p><a href="https://gitee.com/dromara/liteFlow/issues/I4GS07">https://gitee.com/dromara/liteFlow/issues/I4GS07</a></p> 
<p>特性 #I4QWH7 支持循环依赖</p> 
<p><a href="https://gitee.com/dromara/liteFlow/issues/I4QWH7">https://gitee.com/dromara/liteFlow/issues/I4QWH7</a></p> 
<p>增强 #I4OQIX 组件执行轨迹日志级别调整</p> 
<p><a href="https://gitee.com/dromara/liteFlow/issues/I4OQIX">https://gitee.com/dromara/liteFlow/issues/I4OQIX</a></p> 
<p>增强 #I4OTK4 希望finally组件可以获取到then组件的异常对象</p> 
<p><a href="https://gitee.com/dromara/liteFlow/issues/I4OTK4">https://gitee.com/dromara/liteFlow/issues/I4OTK4</a></p> 
<p>增强 #I4PJKP when标签中默认的errorResume改为false</p> 
<p><a href="https://gitee.com/dromara/liteFlow/issues/I4PJKP">https://gitee.com/dromara/liteFlow/issues/I4PJKP</a></p> 
<p>增强 #I4PTY4 修复CopyOnWriteHashMap可能存在的Bug</p> 
<p><a href="https://gitee.com/dromara/liteFlow/issues/I4PTY4">https://gitee.com/dromara/liteFlow/issues/I4PTY4</a></p> 
<p>增强 #I4QV69 QLExpressScriptExecutor加载缓存脚本有线程安全问题</p> 
<p><a href="https://gitee.com/dromara/liteFlow/issues/I4QV69">https://gitee.com/dromara/liteFlow/issues/I4QV69</a></p> 
<p>增强 #I4QWJK 重构parser逻辑，解决的代码冗余问题</p> 
<p><a href="https://gitee.com/dromara/liteFlow/issues/I4QWJK">https://gitee.com/dromara/liteFlow/issues/I4QWJK</a></p> 
<p>增强 #I4R5UI 升级LiteFlow的相关第三方依赖jar包的版本</p> 
<p><a href="https://gitee.com/dromara/liteFlow/issues/I4R5UI">https://gitee.com/dromara/liteFlow/issues/I4R5UI</a></p> 
<p>修复 #I4RF0A 解决有些场景里启动时SpringAware后加载的问题</p> 
<p><a href="https://gitee.com/dromara/liteFlow/issues/I4RF0A">https://gitee.com/dromara/liteFlow/issues/I4RF0A</a></p> 
<p>修复 #I4QOP6 when超时时抛出的错是NPT</p> 
<p><a href="https://gitee.com/dromara/liteFlow/issues/I4QOP6">https://gitee.com/dromara/liteFlow/issues/I4QOP6</a></p> 
<p>修复 #I4PA2A 在NodeComponent的isAccess中获取tag失败</p> 
<p><a href="https://gitee.com/dromara/liteFlow/issues/I4PA2A">https://gitee.com/dromara/liteFlow/issues/I4PA2A</a></p>
                                        </div>
                                      
</div>
            