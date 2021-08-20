
---
title: '【Flutter 从 0 到 1】了解 Flutter 的生态'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/415c651a592847008dbe7e55b1ee2b02~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 19 Aug 2021 03:29:14 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/415c651a592847008dbe7e55b1ee2b02~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文已参与掘金创作者训练营第三期「高产更文」赛道，详情查看：<a href="https://juejin.cn/post/6994417198164869133" title="https://juejin.cn/post/6994417198164869133" target="_blank">掘力计划｜创作者训练营第三期正在进行，「写」出个人影响力</a>。</p>
<h1 data-id="heading-0">前言</h1>
<p><a href="https://juejin.cn/column/6995160230476644366" target="_blank" title="https://juejin.cn/column/6995160230476644366">【Flutter 从 0 到 1】</a> 这个专栏记录了我是如何从零基础开始学习 Flutter，以及在学习过程中踩过的坑，到最后输出一份属于自己的项目模板的过程。写这个专栏的目的也是为了让初学 Flutter 的朋友避免走一些弯路，能尽快的学会 Flutter 以及它的生态。</p>
<p>这里存放该专栏的文章顺序，每次发布新文章时，会更新每篇文章的这里：</p>
<blockquote>
<p>第一篇：<a href="https://juejin.cn/post/6997010270048485390" target="_blank" title="https://juejin.cn/post/6997010270048485390">为什么选择 Flutter ？</a><br>
第二篇：<a href="https://juejin.cn/post/6997322140248702990" target="_blank" title="https://juejin.cn/post/6997322140248702990">如何上手 Flutter ？</a><br>
第三篇：<a href="https://juejin.cn/post/6998100716879347743/" target="_blank" title="https://juejin.cn/post/6998100716879347743/">了解 Flutter 的生态</a>  <code><— 你的当前位置</code><br>
第四篇：Flutter 简单的工程化<br>
第N篇：...</p>
</blockquote>
<h1 data-id="heading-1">Start Game</h1>
<h2 data-id="heading-2">了解 Flutter 的生态</h2>
<p><a href="https://juejin.cn/post/6882315352009605128" target="_blank" title="https://juejin.cn/post/6882315352009605128">一文道尽 Flutter 最新最全的学习资料</a>，这篇文章里列举了很多常见的 Flutter 第三方插件，遇到相关需求后，可以先去文章里找找看有没有合适插件。</p>
<p>然后这个是官方提供的一些插件：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fflutter%2Fplugins" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/flutter/plugins" ref="nofollow noopener noreferrer">github.com/flutter/plu…</a> 。</p>
<p>如果上面两个都找不到你需要的插件的话，就去 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.dev%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.dev/" ref="nofollow noopener noreferrer">pub.dev/</a> 这个网站搜索（类似于前端的 npm 仓库）。</p>
<p>说到这儿，不得不吐槽，好多三方插件的文档一言难尽...... 简直就是：<strong>听君一席话，如听一席话。</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/415c651a592847008dbe7e55b1ee2b02~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>对了，Flutter 本身更偏向是一个 UI 层的框架，很多功能，特别是要与原生平台（Android 和 iOS）打交道的功能，就要去依赖第三方的插件，如果没有相关的插件，那可能就要 <strong>"自己动手，丰衣足食"</strong> 了。</p>
<p>如何开发插件，可以看上一篇文章提到的任意一份文档中的<strong>插件开发相关章节</strong>就行：</p>
<blockquote>
<p>官网：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fflutter.dev%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://flutter.dev/" ref="nofollow noopener noreferrer">flutter.dev/</a> <br>
Flutter中文网提供的文档：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fflutterchina.club%2Fdocs%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://flutterchina.club/docs/" ref="nofollow noopener noreferrer">flutterchina.club/docs/</a> <br>
Flutter中文资源网提供文档：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fflutter.cn%2Fdocs" target="_blank" rel="nofollow noopener noreferrer" title="https://flutter.cn/docs" ref="nofollow noopener noreferrer">flutter.cn/docs</a> <br>
开源书籍：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fbook.flutterchina.club%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://book.flutterchina.club/" ref="nofollow noopener noreferrer">《Flutter 实战》</a>  <code><— 我更喜欢看这份文档</code></p>
</blockquote>
<h2 data-id="heading-3">题外话</h2>
<p>说到 UI 框架，我必须得提一嘴</p>
<p>事情是这样的，由于我有 Web 端 Vue 框架的经验，所以我最开始学习 Flutter 的时候，上手体验了一些 Widget 时。就在想："哎，有没有像 ElementUI 框架一样的现成 UI 库，这样我就不用再去繁琐的调整样式了"。</p>
<p>就去 GitHub 上找了找，有是有，只是提供的功能都比较少，文档欠缺，且多是英文。</p>
<p>之后随着对 Flutter 的了解加深，发现 Flutter 其实不是特别需要 UI 库，多是使用自带的 Widget，但是像一些常见的业务场景，比如 <strong>swiper 轮播图</strong>，这种还是有非常好用的第三方开源组件，就可以直接拿来用。</p>
<p>所以，如果有想找一个功能完善，文档齐全的 UI 框架的朋友，可以先省省了。</p>
<p>但是这里还是提两个 UI 框架，有需要的朋友自己去了解：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fflutterchina%2Fflukit" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/flutterchina/flukit" ref="nofollow noopener noreferrer">flukit</a> 和 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fionicfirebaseapp%2Fgetwidget" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/ionicfirebaseapp/getwidget" ref="nofollow noopener noreferrer">getwidget</a></p>
<h2 data-id="heading-4">工具类</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FSky24n%2Fflustars" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Sky24n/flustars" ref="nofollow noopener noreferrer">github.com/Sky24n/flus…</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FSky24n%2Fcommon_utils" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/Sky24n/common_utils" ref="nofollow noopener noreferrer">github.com/Sky24n/comm…</a></p>
<p>这两个都是我用过的，感觉还比较好用。当然，工具类可以自己写，也不用看啥文档，说简单点，就是事先写好的一些类和函数。</p>
<h2 data-id="heading-5">听君一席话，如听一席话</h2>
<p>哈哈哈哈哈，这篇文章本来应该是 "Flutter 简单的工程化" ，但是我觉得还是应该先去了解 Flutter 有哪些常用的三方插件，然后再学习搭建一个简易的项目模板比较合适，就把这篇文章横插了进来。</p>
<p>所以，如果你觉得这篇文章水了点，那麻烦你自信点！这篇文章确实水！</p></div>  
</div>
            