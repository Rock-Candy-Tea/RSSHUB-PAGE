
---
title: '你知道 ES6~ES12等叫法是怎么来的吗？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f124ce78ad7f46c5a7615887935614e6~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 31 Aug 2021 07:29:25 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f124ce78ad7f46c5a7615887935614e6~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第31天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<blockquote>
<p>你知道 ES6~ES12等叫法是怎么来的吗？</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f124ce78ad7f46c5a7615887935614e6~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">前言</h2>
<p>作为一名前端开发，学习 JavaScript 自是天经地义的事，但是，JavaScript 的发展历史是怎样的，恐怕有相当一部分人都不太了解。</p>
<p>我们常常听别人说并且自己也会说 ES6、ES7……ES12，那么，这些叫法到底是怎么来的？</p>
<p>今天，我们就来总结一下这些有关 JavaScript 的发展历程。</p>
<p>通过阅读本文，你将了解以下知识：</p>
<ul>
<li>ECMA 是什么</li>
<li>ECMAScript 是什么</li>
<li>JavaScript 的由来</li>
<li>ES5 ~ ES12 的意义</li>
</ul>
<h2 data-id="heading-1">关于 ECMA</h2>
<p>ECMA 全称为 <code>European Computer Manufacturers Association</code>，翻译过来就是“欧洲计算机制造商协会”，是一个成立于 1961 年的、极具影响力的国际组织。</p>
<p>但是，因为计算机的国际化，ECMA 的标准牵涉到很多其他国家，因此于 1994 年改名为 <strong><code>Ecma国际</code></strong>，以表明其国际性。</p>
<p><code>Ecma国际</code> 专门制定信息和通信系统的标准和报告，以促进和规范信息通信技术与消费电子产品。</p>
<p>迄今为止，<code>Ecma国际</code> 主动贡献了超过 400 个标准和 100 个技术报告，其中大约三分之二以上被定为国际标准，在国际上得到了广泛使用。</p>
<h2 data-id="heading-2">关于 JavaScript</h2>
<p>JavaScript 在 1995 年由 Netscape （网景）公司的Brendan Eich（布兰登·艾奇），在网景导航者浏览器上首次设计实现而成，最初将其脚本语言命名为 LiveScript。</p>
<p>因为Netscape 与 Sun（升阳）合作，为了营销考虑，Netscape 与 Sun 微系统达成协议，希望它外观看起来像 Java（毕竟当时 Java 属于当红炸子鸡），因此取名为 JavaScript，但实际上它的语法风格与 Self 及 Scheme 较为接近。</p>
<p>JavaScript 发展之初，微软也推出了 JScript（主要用于 IE 浏览器）来迎战 JavaScript，当时还有 Adobe 的 ActionScript。为了统一标准，实现互用，1997年，在 Ecma国际 的协调下，由 Netscape、Sun、微软、Borland 组成的工作组确定统一标准——ECMA-262(ISO/IEC 16262)，该标准定义了叫做ECMAScript 的全新脚本语言。</p>
<p>完整的 JavaScript 实现包含三个部分：</p>
<ul>
<li>ECMAScript</li>
<li>文档对象模型（DOM）</li>
<li>浏览器对象模型（BOM）</li>
</ul>
<h2 data-id="heading-3">关于 ECMAScript</h2>
<p>ECMAScript 是一种由 <code>Ecma国际</code> 在 1997 年通过 <code>ECMA-262(ISO/IEC 16262)</code> 标准化的脚本程序设计语言。它描述了 JavaScript的语法和基本对象，是 JavaScript 的标准。</p>
<p>ECMAScript 实际上是一种脚本在语法和语义上的标准，JavaScript，JScript 和 ActionScript 中声明变量，操作数组等语法完全一样，因为它们都是 ECMAScript。但是在操作浏览器对象等方面又有各自独特的方法，这些都是各自语言的扩展。</p>
<p>自 2015 年以来，ECMAScript 的发展及其版本如下所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d987d6a3cf1646c69258564a200e31c6~tplv-k3u1fbpfcp-watermark.image" alt="image-20210831230601389" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过这图，大家应该知道平常所说的 ES6 之类的是怎么来的了吧。</p>
<p>我们一般将 2015 年之前的版本统称为 ES5，不会详细去区分到底是 1~5 中的哪个。</p>
<p>符合ECMA-262 标准的实现有：</p>
<ul>
<li>Microsoft 公司的 JScript。</li>
<li>Mozilla 的 JavaScript-C（C 语言实现），现名 SpiderMonkey。</li>
<li>Mozilla 的 Rhino（Java 实现）。</li>
<li>Digital Mars 公司的 DMDScript。</li>
<li>Google 公司的 V8。</li>
<li>WebKit。</li>
</ul>
<h2 data-id="heading-4">总结</h2>
<p>总结一下上面的内容：</p>
<ul>
<li>JavaScript 最初是由网景公司的布兰登·艾奇所实现。</li>
<li>JavaScript 是甲骨文公司的注册商标。Ecma国际以 JavaScript 为基础制定了 ECMAScript 标准。</li>
<li>Ecma国际专门制定信息和通信系统的标准和报告，ECMAScript 只是它所制定标准中的一个。</li>
<li>ESCMScript 是 JavaScript 的标准，描述了 JavaScript 的语法和基本对象。</li>
<li>完整的 JavaScript 实现包含三个部分：ECMAScript、DOM 和 BOM。</li>
</ul>
<p>~</p>
<p>~本文完，感谢阅读！</p>
<p>~</p>
<blockquote>
<p>学习有趣的知识，结识有趣的朋友，塑造有趣的灵魂！</p>
<p>大家好，我是〖<a href="https://juejin.cn/user/2893570333750744/posts" target="_blank" title="https://juejin.cn/user/2893570333750744/posts">编程三昧</a>〗的作者 <strong>隐逸王</strong>，我的公众号是『<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fyinyiwang%2FblogImages%2Fraw%2Fmaster%2Fimages%2F20210604%2520%2F19-26-03-txvEvM.png" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/yinyiwang/blogImages/raw/master/images/20210604%20/19-26-03-txvEvM.png" ref="nofollow noopener noreferrer">编程三昧</a>』，欢迎关注，希望大家多多指教！</p>
<p>你来，怀揣期望，我有墨香相迎！ 你归，无论得失，唯以余韵相赠！</p>
<p>知识与技能并重，内力和外功兼修，理论和实践两手都要抓、两手都要硬！</p>
</blockquote></div>  
</div>
            