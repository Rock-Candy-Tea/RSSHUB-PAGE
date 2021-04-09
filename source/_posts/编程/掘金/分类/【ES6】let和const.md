
---
title: '【ES6】let和const'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0358c5fcfc2844e28b346193d321cf94~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 08 Apr 2021 07:57:25 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0358c5fcfc2844e28b346193d321cf94~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>ES6新增的两个命令，用于声明变量，let类似于var，const用于声明常量。</p>
<h1 data-id="heading-0">一、let</h1>
<h3 data-id="heading-1">1. let声明的变量只在所在的代码块内有效</h3>
<pre><code class="hljs language-js copyable" lang="js">&#123;
    <span class="hljs-keyword">let</span> a = <span class="hljs-number">10</span>;
    <span class="hljs-keyword">var</span> b = <span class="hljs-number">1</span>
&#125;

a <span class="hljs-comment">// ReferenceError: a is not defined</span>
b <span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码块外调用两个变量，let声明的变量报错</p>
<h3 data-id="heading-2">2. let声明的变量不存在变量提升</h3>
<p>var声明的变量可以在声明前使用，值为undefined,这种现象称为“变量提升”。let命令改变了这种行为，<code>let所声明的变量一定要在声明后使用，否则会报错</code></p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0358c5fcfc2844e28b346193d321cf94~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>var声明的变量在脚本开始运行时就已存在，但是没有值，所以输出undefined</p>
<h3 data-id="heading-3">3. 暂时性死区(Temporal Dead Zone, TDZ)</h3>
<p>ES6规定，如果区块中存在let和const命令，则这个区块对这些命令声明的变量从一开始就形成封闭作用域，只要在声明之前使用这些变量，就会报错。
<img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/425c0bd593174b10ae2021a20aad4680~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">4.不允许重复声明</h3>
<p>let不允许在相同作用域内声明同一个变量</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/51215c9006834189b8458a843a53e661~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-5">二、const命令</h1>
<p>const声明一个只读常量，一旦声明，常量的值就不能改变,这意味着const一旦声明常量，就<code>必须立即初始化</code></p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/853d8818946845d0aa21a7e05af81577~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><code>const本质</code></p>
<p><strong>const实际上保证的是变量指向的那个内存地址不得改动</strong>。</p>
<p>对于简单类型的数据（number、string、boolean）而言，值就保存在变量指向的内存地址中，因此等同于变量；对于复合类型的数据而言，变量指向的内存地址保存的只是一个指针，const只是保证这个指针是固定的，至于指向的数据结构是否可变，这完全不能控制。</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f687a0c20a944938ec750d29003b2db~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-6">三、运用场景</h1>
<ul>
<li>let在for循环中的运用</li>
</ul>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3312d807b43f423d8758b394678d6ff0~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>变量i通过var声明，则i在全局范围内有效且只有一个变量i,每次循环，变量i的值都会发生改变。当调用函数的时候，console.log(i)中的i指向全局的i，导致运行时输出的是最后一轮的i值。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            