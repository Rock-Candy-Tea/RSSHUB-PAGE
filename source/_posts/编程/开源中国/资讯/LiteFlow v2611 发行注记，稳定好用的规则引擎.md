
---
title: 'LiteFlow v2.6.11 发行注记，稳定好用的规则引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-3d8cb5f476d7ca58beea8da23c25731705a.png'
author: 开源中国
comments: false
date: Mon, 14 Mar 2022 12:28:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-3d8cb5f476d7ca58beea8da23c25731705a.png'
---

<div>   
<div class="content">
                                                                                            <p><img height="760" src="https://oscimg.oschina.net/oscnet/up-3d8cb5f476d7ca58beea8da23c25731705a.png" width="1798" referrerpolicy="no-referrer"></p> 
<h2>前言</h2> 
<p>LiteFlow v2.6.11版本正式发布！依赖包已发布中央仓库，文档做了大量的更新和补漏。</p> 
<p>其实单看本次更新的Issue确实没多少，但是代码量却不少。主要工作花在结构依赖的改动上，和大量细节代码的优化上。同时我终于下决心恶补了下LiteFlow的测试用例，从100来个测试用例补到了289个。</p> 
<p>新版本现在终于可以在非Spring的体系中也可以方便的使用LiteFlow了，可能有小伙伴会有疑惑，非Spring体系的项目还有必要支持么，还有人在用非Spring体系搭建项目吗？</p> 
<p>其实本人一开始也有这个疑惑，但是最终促使我改的原因并不是有人在用非Spring体系用不了LiteFlow，而是从项目结构来说，核心包强依赖一个第三方框架，始终让我觉得这不是一个好的设计。如何用一套核心代码，在不同体系的系统框架下生效，而不是用硬代码去强判断环境，也是我想尝试的。所以就开始改变模块依赖结构。</p> 
<p>在改的过程中，也让我有机会把以前细节做的不好的地方又重写了一遍。顺便对几乎所有的场景都补了测试用例。测试用例补的同事又反过来让我发现了一些细枝末节的bug，在这个版本的开发中，我就这样来来回回的重构，改bug，写测试用例。</p> 
<p>废话了那么多，只想告诉你们，v2.6.11应该会是一个稳定的版本(话也不能说太死，就怕打脸:P)。</p> 
<p>如果你是第一次知道这个项目，可以去官网或相关的主页进行了解</p> 
<blockquote> 
 <p>项目官网:</p> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fliteflow.yomahub.com" target="_blank">https://liteflow.yomahub.com</a></p> 
 <p>gitee托管仓库：</p> 
 <p><a href="https://gitee.com/dromara/liteFlow">https://gitee.com/dromara/liteFlow</a></p> 
 <p>github托管仓库：</p> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdromara%2Fliteflow" target="_blank">https://github.com/dromara/liteflow</a></p> 
</blockquote> 
<h2>关于测试用例</h2> 
<p>其实关于如何更好的理解LiteFlow的每个特性，我更建议大家去PULL下源码，结合下文档自己跑下测试用例。会理解的更为透彻。</p> 
<p>测试用例目前总共有5个模块，大部分场景都有覆盖。</p> 
<p><img height="1000" src="https://oscimg.oschina.net/oscnet/up-e7669578b9779d378d36a3ac067d059abfa.png" width="682" referrerpolicy="no-referrer"></p> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-3530f090e061c5f3932ca45e39c65dd4b53.png" width="2070" referrerpolicy="no-referrer"></p> 
<h2>关于文档</h2> 
<p>随着新版本发布，我对文档也进行一小部分的重整。把部分章节进行了合并归类，使新手阅读起来，更加条理清晰，同时也对文档进行了查缺补漏，补充了一些文档。</p> 
<p>另外我每天在群里回答小伙伴提出的各种问题，时间一长，有很多人问出的问题都非常类似。为了避免重复问题的答应，我把大家经常问的问题整理了一下，并到了<code>问题汇总和答疑</code>中。希望小伙伴提问题，可以先在这章寻找下有没有你想要的答案，如果没有再在群里提问。</p> 
<p><img height="1942" src="https://oscimg.oschina.net/oscnet/up-9f4c621209a10693100a42c3bfa78d6cd85.png" width="3284" referrerpolicy="no-referrer"></p> 
<h2>v2.6.11更新日志</h2> 
<p>特性 I4UPWG 模块架构调整，支持非Spring的项目使用</p> 
<p><a href="https://gitee.com/dromara/liteFlow/issues/I4UPWG">https://gitee.com/dromara/liteFlow/issues/I4UPWG</a></p> 
<p>增强 I4VTWB 代码动态构建规则,setClazz方法使用全限定名不太友好</p> 
<p><a href="https://gitee.com/dromara/liteFlow/issues/I4VTWB">https://gitee.com/dromara/liteFlow/issues/I4VTWB</a></p> 
<p>增强 I4TIWM whenExecutors目前不用注入到spring上下文中了</p> 
<p><a href="https://gitee.com/dromara/liteFlow/issues/I4TIWM">https://gitee.com/dromara/liteFlow/issues/I4TIWM</a></p> 
<p>修复 I4VEV2 用spring扫描组件，但是流程用动态代码创建，会出现slot无法分配的bug</p> 
<p><a href="https://gitee.com/dromara/liteFlow/issues/I4VEV2">https://gitee.com/dromara/liteFlow/issues/I4VEV2</a></p> 
<p>修复 I4VGCN 在非spring环境下，LiteflowConfigGetter无法获取到原始的config实例</p> 
<p><a href="https://gitee.com/dromara/liteFlow/issues/I4VGCN">https://gitee.com/dromara/liteFlow/issues/I4VGCN</a></p> 
<h2>支持</h2> 
<p>为了开源项目的更好推广，如果你的项目中用了LiteFlow框架并且还觉得不错的话，希望可以在以下地址登记你的公司，登记的公司都会更新到文档中的用户一栏中。</p> 
<p><a href="https://gitee.com/dromara/liteFlow/issues/I3CM7N">https://gitee.com/dromara/liteFlow/issues/I3CM7N</a></p> 
<p>当然你也可以选择请我喝杯咖啡:P，这会是对我以及我努力成果的最大肯定！</p> 
<p>请我喝咖啡地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fliteflow.yomahub.com%2Fblog%2Fdonation" target="_blank">https://liteflow.yomahub.com/blog/donation</a></p>
                                        </div>
                                      
</div>
            