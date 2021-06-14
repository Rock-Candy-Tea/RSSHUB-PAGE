
---
title: '看看 TypeScript4.3 带来了哪些新特性'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ab59d0aeb8443f996dec0d471fb2f21~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 13 Jun 2021 17:42:47 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ab59d0aeb8443f996dec0d471fb2f21~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0"><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ab59d0aeb8443f996dec0d471fb2f21~tplv-k3u1fbpfcp-watermark.image" alt="导出图片Sun Jun 13 2021 23_10_21 GMT+0800 (中国标准时间).png" loading="lazy" referrerpolicy="no-referrer"></h2>
<h2 data-id="heading-1">theme: fancy
highlight: a11y-dark</h2>
<p>自从跳槽以后，工作上接触 TS 也是越来越多，所以对 TS 关注也是有所增加。社会上有种效应叫做“视网膜效应”，说的是越关注什么就越出现什么，当你开始对某些方面增加关注时，相同的事物就会在你眼前不断出现。TS 对于近期的我而言，便是如此。</p>
<hr>
<p>好了废话不多说，近期也是关注到 TypeScript4.3 发布了，简单给大家介绍下该版本。</p>
<p>当然，如果你还不清楚什么是 TypeScript，小编这里也不会科普。（因为我猜你打不到我 emmm...）感兴趣的小伙伴可以去官网 get 一下啦。</p>
<p>最新版的 TS4.3，需要使用或者更新的伙伴，直接通过 npm 或者 yarn 下载/更新即可。</p>
<p>接下来让我带着愉悦的心情，一起 see see Typescript4.3 给我们带来了啥新特性？你好奇吗？（小编写完了，所以不好奇了，小声 BB）</p>
<h2 data-id="heading-2">新特性预览</h2>
<ul>
<li>支持将属性单独读写指定类型</li>
<li>增加了关键字 overrride，以保证基础类中的方法不会被覆盖</li>
<li>模版字符串类型的改进</li>
<li>扩展了类中可被赋予#private #name 的元素，使它们在运行时能够真正私有化。除了属性以外，方法和访问器也可以被赋予私有名称。</li>
<li>ConstructorParameters 类型帮助现在可以在抽象类中使用。</li>
<li>泛型的上下文范围得到缩小。</li>
<li>Always-Truthy 检查</li>
<li>static 静态索引签名</li>
<li>.tsbuildinfo 文件大小优化减少，加快构建速度</li>
<li>--incremental 和 --watch 中计算优化，提高编译速度</li>
<li>导入、导出语句优化</li>
<li>编辑器支持@link 标签</li>
<li>非 js 文件文件路径跳转，获取快速信息</li>
<li>lib.d.ts 变更</li>
</ul>
<p>下面简单聊聊其中几个变化。</p>
<h3 data-id="heading-3">增加了关键字 overrride</h3>
<p>在扩展类时，我们很容易覆盖原有基础类的方法。
比如：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animals</span> </span>&#123;
  eat () &#123;
    <span class="hljs-comment">// ...</span>
  &#125;
  sleep () &#123;
    <span class="hljs-comment">// ...</span>
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Pig</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Animals</span> </span>&#123;
  eat () &#123;
    <span class="hljs-comment">// ...</span>
  &#125;
  sleep () &#123;
    <span class="hljs-comment">// ...</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>继承之后如果是这样的处理方案，无法知悉使用者是添加对应的新的方法亦或是覆盖现有基础类上的方法。这便是 Ts4.3 添加 override 关键字的原因。</p>
<pre><code class="copyable">class Pig extends Animals &#123;
  override eat () &#123;
    // ...
  &#125;
  override sleep () &#123;
    // ...
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当一个方法标记为 override 时，Ts 总是会确保基类中存在同名方法。</p>
<p>同时，Ts4.3 提供一个新的选项 --noImplicitOverride，开启此选项后，重写超类的任何方法将会抛错，除非显式使用关键字 override。</p>
<h3 data-id="heading-4">.tsbuildinfo 文件大小优化</h3>
<p>Ts4.3 中，.tsbuildinfo 文件的优化，归功于内部格式的优化，即创建使用了数字标示符的表，而不再是完整路径等来做处理。</p>
<p>该文件的优化减少体积，毋庸置疑也意味着构建速度的大大提高。</p>
<h3 data-id="heading-5">导入导出优化</h3>
<p>在现有使用的版本里，我们知道导入的时候如果不写 from 路径的话很难为我们自动匹配可能需要导入的文件列表。</p>
<p>而在 Ts4.3 中，这一块做的更加智能了，哪怕你只是 coding 下 import 关键字，也会自动为你匹配可能需要导入的文件列表以及补全对应的文件路径。大大提升了开发者日常开发导入模块的痛点，可以在最新的 vs code 中去尝试了！为 Ts 团队点赞 👍。</p>
<h3 data-id="heading-6">支持 link 标签快速获取信息</h3>
<p>Ts4.3 以后，将完全可以理解@link 标签，并尝试解析它们所链接到的生命，这将意味着我们可以直接通过悬停@link 标签来获得快速信息。在支持的编辑器里，也可以一键跳转到对应的函数声明中。将会是十分便捷的一项新功能。</p>
<h3 data-id="heading-7">lib.d.ts 改变</h3>
<p>兼容来删除没有浏览器实现的 api，虽然我们平常可能不一定用到。</p>
<ul>
<li>Account</li>
<li>AssertionOptions</li>
<li>RTCStatsEventInit</li>
<li>MSGestureEvent</li>
<li>DeviceLightEvent</li>
<li>MSPointerEvent</li>
<li>ServiceWorkerMessageEvent</li>
<li>WebAuthentication
以上的均在接下来的版本里从 lib.d.ts 中删除。</li>
</ul>
<p>本文只是做一个简短的介绍，相关更加详尽的介绍还得靠各位德智体美劳优异的小朋友们。<a href="https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-3.html" title="TypeScript4.3" target="_blank" rel="nofollow noopener noreferrer">传送门</a></p>
<hr>
<p>据本台可靠消息，虽然 TypeScript4.3 刚发布，但是相关团队已经在开展 TpyeScript4.4 的工作了。就问问你还学的动么？</p></div>  
</div>
            