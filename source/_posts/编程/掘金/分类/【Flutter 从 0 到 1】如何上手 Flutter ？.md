
---
title: '【Flutter 从 0 到 1】如何上手 Flutter ？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c54894fe6d747f0b09b84dbf8b277b9~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 17 Aug 2021 01:04:44 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c54894fe6d747f0b09b84dbf8b277b9~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文已参与掘金创作者训练营第三期「高产更文」赛道，详情查看：<a href="https://juejin.cn/post/6994417198164869133" title="https://juejin.cn/post/6994417198164869133" target="_blank">掘力计划｜创作者训练营第三期正在进行，「写」出个人影响力</a>。</p>
<h1 data-id="heading-0">前言</h1>
<p><a href="https://juejin.cn/column/6995160230476644366" target="_blank" title="https://juejin.cn/column/6995160230476644366">【Flutter 从 0 到 1】</a> 这个专栏记录了我是如何从零基础开始学习 Flutter，以及在学习过程中踩过的坑，到最后输出一份属于自己的项目模板的过程。写这个专栏的目的也是为了让初学 Flutter 的朋友避免走一些弯路，能尽快的学会 Flutter 以及它的生态。</p>
<p>这里存放该专栏的文章顺序，每次发布新文章时，会更新每篇文章的这里：</p>
<blockquote>
<p>第一篇：<a href="https://juejin.cn/post/6997010270048485390" target="_blank" title="https://juejin.cn/post/6997010270048485390">为什么选择 Flutter ？</a><br>
第二篇：<a href="https://juejin.cn/post/6997322140248702990" target="_blank" title="https://juejin.cn/post/6997322140248702990">如何上手 Flutter ？</a>  <— 你的当前位置<br>
第三篇：Flutter 简单的工程化<br>
第N篇：...</p>
</blockquote>
<h1 data-id="heading-1">Start Game</h1>
<h2 data-id="heading-2">Dart</h2>
<p>在线运行 Dart 代码：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdartpad.dartlang.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://dartpad.dartlang.org/" ref="nofollow noopener noreferrer">dartpad.dartlang.org/</a> ，学习阶段直接在上面运行代码就可以。</p>
<p>官网 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdart.dev%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://dart.dev/" ref="nofollow noopener noreferrer">dart.dev/</a> ，中文官网 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdart.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://dart.cn/" ref="nofollow noopener noreferrer">dart.cn/</a> ，但是我都不看，哎，就是玩儿~</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c54894fe6d747f0b09b84dbf8b277b9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我首先看的是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fflutterchina.club%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://flutterchina.club/" ref="nofollow noopener noreferrer">Flutter中文网</a> 的开源书籍 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fbook.flutterchina.club%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://book.flutterchina.club/" ref="nofollow noopener noreferrer">《Flutter 实战》</a>中 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fbook.flutterchina.club%2Fchapter1%2Fdart.html" target="_blank" rel="nofollow noopener noreferrer" title="https://book.flutterchina.club/chapter1/dart.html" ref="nofollow noopener noreferrer">Dart语言简介</a> 部分 ，章节很少（只有变量、函数、异步、Stream、对比其他语言，这 5 个小节），能让我这个会 JS 的人直接上手 Dart。</p>
<p>看了这个之后，我其实直接就去学 Flutter 去了，学到一半发现一部分 Dart 语法看不懂的时候，又倒回去系统的学习。所有这里我还是建议一步一个脚印的来，直接先去系统的学习 Dart 语言。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42b8af7c815143b6a12a028cf7c34c7d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>比较喜欢这一份教程：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.kancloud.cn%2Fmarswill%2Fdark2_document%2F709087" target="_blank" rel="nofollow noopener noreferrer" title="https://www.kancloud.cn/marswill/dark2_document/709087" ref="nofollow noopener noreferrer">Dart2 中文文档</a></p>
<p>你要问我为啥喜欢，我其实也不知道... 找到自己一篇满意的教程，看就完了，反正有官网在哪儿兜底呢对吧</p>
<h2 data-id="heading-3">Flutter</h2>
<h3 data-id="heading-4">安装 Flutter 的开发环境</h3>
<p>第一步，安装 Flutter 的开发环境。看的是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fflutterchina.club%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://flutterchina.club/" ref="nofollow noopener noreferrer">Flutter中文网</a> 的开源书籍 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fbook.flutterchina.club%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://book.flutterchina.club/" ref="nofollow noopener noreferrer">《Flutter 实战》</a>中 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fbook.flutterchina.club%2Fchapter1%2Finstall_flutter.html%23_1-3-1-%25E5%25AE%2589%25E8%25A3%2585flutter" target="_blank" rel="nofollow noopener noreferrer" title="https://book.flutterchina.club/chapter1/install_flutter.html#_1-3-1-%E5%AE%89%E8%A3%85flutter" ref="nofollow noopener noreferrer">搭建Flutter开发环境</a> 部分和技术胖的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fjspang.com%2Fdetailed%3Fid%3D41%23toc210" target="_blank" rel="nofollow noopener noreferrer" title="https://jspang.com/detailed?id=41#toc210" ref="nofollow noopener noreferrer">Flutter免费视频第一季-环境搭建</a></p>
<p>为啥搭建开发环境看了两份教程？我记得好像是每篇文章中都有一点不足，我把两篇文章结合了一下，具体是啥不足，我给忘了，时间有点久远了...</p>
<p>看了这两篇教程后，我自己综合总结了一份 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F95060323" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/95060323" ref="nofollow noopener noreferrer">Windows下搭建Flutter的Android开发环境教程</a>，如果是 Windows 环境的朋友直接看我的这一份也是可以的。</p>
<h3 data-id="heading-5">开始学习 Flutter</h3>
<p>第二步，就是真正的开始学习 Flutter 教程了</p>
<p>官网 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fflutter.dev%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://flutter.dev/" ref="nofollow noopener noreferrer">flutter.dev/</a> ，Flutter中文网提供的文档 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fflutterchina.club%2Fdocs%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://flutterchina.club/docs/" ref="nofollow noopener noreferrer">flutterchina.club/docs/</a> ，Flutter中文资源网提供文档 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fflutter.cn%2Fdocs" target="_blank" rel="nofollow noopener noreferrer" title="https://flutter.cn/docs" ref="nofollow noopener noreferrer">flutter.cn/docs</a> ，但是我还是都不看，哎，就是玩儿~</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18b46bbe37084566836845808c9b2f63~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我看是前文提到的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fflutterchina.club%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://flutterchina.club/" ref="nofollow noopener noreferrer">Flutter中文网</a> 的开源书籍 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fbook.flutterchina.club%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://book.flutterchina.club/" ref="nofollow noopener noreferrer">《Flutter 实战》</a></p>
<p>我读了它的第一章起步、第二章第一个Flutter应用、第三章基础组件的前两节，然后就跳到了第十一章文件操作与网络请求。</p>
<p>为啥诸如第三章的后半部分和第四章我不看了？因为有点点枯燥，这部分大多讲的是 Widget 的用法（有点点类似于教你如何在 Vue 中使用 ElementUI 框架一样），我觉得用到的时候再去看比较节约时间，前期留个印象，大致知道 Flutter 提供了哪些常用的 Widget 就好。</p>
<p>当然，你能坚持把整份文档肝下来，那...那你确实牛x！</p>
<h3 data-id="heading-6">开始实践</h3>
<p>还是前文提到的技术胖的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fjspang.com%2Fdetailed%3Fid%3D58%23toc22" target="_blank" rel="nofollow noopener noreferrer" title="https://jspang.com/detailed?id=58#toc22" ref="nofollow noopener noreferrer">Flutter免费视频</a>， 直接看第二到第四季 + 20个小例子。看完能让你熟悉常用的 Widget、常用的布局、路由相关知识。</p>
<p><em>不喜欢图文教程的朋友可以去哔哩哔哩找一下技术胖的视频教程，都是和图文教程配套的。</em></p>
<p>到这儿其实你已经能上手 Flutter 了，不过如果有其他领域开发经验的朋友可能会第一时间想到：“我目前掌握的大多是 Flutter 本身提供基础知识，写写小 demo 还凑合，如果拿来做大项目，是远远不够用的”</p>
<p>是的。因为你目前还不具备一些常见的“工程化”方案，譬如 HTTP 模块：我们往往不直接使用官方提供的原生 HTTP API，而是去使用第三方的 Dio 插件，并且我们还要基于 Dio 插件进行二次封装，使其变得更加好用。</p>
<p>像这些东西，下一篇文章我们再详细的说。</p>
<p>所以，下一篇文章见。</p></div>  
</div>
            