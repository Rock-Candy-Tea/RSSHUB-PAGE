
---
title: 'nodejs 如何实现控制台打印高亮代码'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d3c6b350af041d680b429a5f0cc55f2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 10 May 2021 06:10:56 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d3c6b350af041d680b429a5f0cc55f2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>当代码运行报错时，我们会打印错误，错误中有堆栈信息，可以定位到对应的代码位置。但有的时候我们希望能够更直接准确的打印报错位置的代码。比如这样：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d3c6b350af041d680b429a5f0cc55f2~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个可以使用 @babel/code-frames 来做到：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123; codeFrameColumns &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'@babel/code-frame'</span>);

<span class="hljs-keyword">const</span> res = codeFrameColumns(code, &#123;
  <span class="hljs-attr">start</span>: &#123; <span class="hljs-attr">line</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">column</span>: <span class="hljs-number">1</span> &#125;,
  <span class="hljs-attr">end</span>: &#123; <span class="hljs-attr">line</span>: <span class="hljs-number">3</span>, <span class="hljs-attr">column</span>: <span class="hljs-number">5</span> &#125;,
&#125;, &#123;
  <span class="hljs-attr">highlightCode</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">message</span>: <span class="hljs-string">'这里出错了'</span>
&#125;);

<span class="hljs-built_in">console</span>.log(res);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有没有感觉比较神奇，它是怎么做到的打印出上面的代码格式的（code frame）？</p>
<p>本文我们就来探究下原理。</p>
<p>主要会解答三个问题：</p>
<ul>
<li>如何打印出标记相应位置代码的 code frame（就是上图的打印格式）</li>
<li>如何实现语法高亮</li>
<li>如何在控制台打印颜色</li>
</ul>
<h2 data-id="heading-0">如何打印 code frame</h2>
<p>我们先不管高亮，实现这样的格式的打印：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8ac279789904a669148430c7089f184~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>有啥思路没？</p>
<p>其实也比较容易想到，传入了源代码、标记开始和结束的行列号，那么我们就能够计算出显示标记（marker）的行是哪些，以及这些行的哪些列，然后依次对每一行代码做处理，如果本行没有标记则保持原样，如果本行有标记的话，那么就在开始打印一个 marker <code>“>”</code>，并且在下面打印一行 marker <code>"^"</code>，最后一个标记行还要打印错误信息。</p>
<p>我们来看一下 @babel/code-frame 的实现：</p>
<p><strong>首先，分割字符串成每一行的数组，然后根据传入的位置计算出 marker 所在的位置。</strong></p>
<p>比如图中第二行的第 1 到 12 列，第三行的 0 到 5 列。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dda49d8bf08549458b2266a912b37042~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>然后对每一行做处理，如果本行有标记，则拼成 marker + gutter（行号） + 代码的格式，下面再打印一行 marker，最后的 marker 行打印 message。没有标记不处理。</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc7dcce653e5479382e6f697008c96aa~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样最终拼出的就是这样的 code frame：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8ac279789904a669148430c7089f184~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们实现了 code frame 的拼接，暂时忽略了高亮，那么怎么做语法高亮呢？</p>
<h2 data-id="heading-1">如何实现语法高亮</h2>
<p>实现语法高亮需要理解代码，但是如果只是高亮，词法分析就足够了。babel 也是这么做的，@babel/highlight 包里面完成了高亮代码的逻辑。</p>
<p>先看效果：</p>
<pre><code class="copyable">const a = 1;
const b = 2;
console.log(a + b);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的源码被分成了 token 数组：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">[
  [ <span class="hljs-string">'whitespace'</span>, <span class="hljs-string">'\n'</span> ], [ <span class="hljs-string">'keyword'</span>, <span class="hljs-string">'const'</span> ],
  [ <span class="hljs-string">'whitespace'</span>, <span class="hljs-string">' '</span> ],  [ <span class="hljs-string">'name'</span>, <span class="hljs-string">'a'</span> ],
  [ <span class="hljs-string">'whitespace'</span>, <span class="hljs-string">' '</span> ],  [ <span class="hljs-string">'punctuator'</span>, <span class="hljs-string">'='</span> ],
  [ <span class="hljs-string">'whitespace'</span>, <span class="hljs-string">' '</span> ],  [ <span class="hljs-string">'number'</span>, <span class="hljs-string">'1'</span> ],
  [ <span class="hljs-string">'punctuator'</span>, <span class="hljs-string">';'</span> ],  [ <span class="hljs-string">'whitespace'</span>, <span class="hljs-string">'\n'</span> ],
  [ <span class="hljs-string">'keyword'</span>, <span class="hljs-string">'const'</span> ], [ <span class="hljs-string">'whitespace'</span>, <span class="hljs-string">' '</span> ],
  [ <span class="hljs-string">'name'</span>, <span class="hljs-string">'b'</span> ],        [ <span class="hljs-string">'whitespace'</span>, <span class="hljs-string">' '</span> ],
  [ <span class="hljs-string">'punctuator'</span>, <span class="hljs-string">'='</span> ],  [ <span class="hljs-string">'whitespace'</span>, <span class="hljs-string">' '</span> ],
  [ <span class="hljs-string">'number'</span>, <span class="hljs-string">'2'</span> ],      [ <span class="hljs-string">'punctuator'</span>, <span class="hljs-string">';'</span> ],
  [ <span class="hljs-string">'whitespace'</span>, <span class="hljs-string">'\n'</span> ], [ <span class="hljs-string">'name'</span>, <span class="hljs-string">'console'</span> ],
  [ <span class="hljs-string">'punctuator'</span>, <span class="hljs-string">'.'</span> ],  [ <span class="hljs-string">'name'</span>, <span class="hljs-string">'log'</span> ],
  [ <span class="hljs-string">'bracket'</span>, <span class="hljs-string">'('</span> ],     [ <span class="hljs-string">'name'</span>, <span class="hljs-string">'a'</span> ],
  [ <span class="hljs-string">'whitespace'</span>, <span class="hljs-string">' '</span> ],  [ <span class="hljs-string">'punctuator'</span>, <span class="hljs-string">'+'</span> ],
  [ <span class="hljs-string">'whitespace'</span>, <span class="hljs-string">' '</span> ],  [ <span class="hljs-string">'name'</span>, <span class="hljs-string">'b'</span> ],
  [ <span class="hljs-string">'bracket'</span>, <span class="hljs-string">')'</span> ],     [ <span class="hljs-string">'punctuator'</span>, <span class="hljs-string">';'</span> ],
  [ <span class="hljs-string">'whitespace'</span>, <span class="hljs-string">'\n'</span> ]
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>token 怎么分的呢？</p>
<p>一般来说词法分析就是有限状态自动机（DFA），但是这里实现比较简单，是通过正则匹配的：</p>
<p>js-tokens 这个包暴露出来一个正则，一个函数，正则是用来识别 token 的，其中有很多个分组，而函数里面是对不同的分组下标返回了不同的类型，这样就能完成 token 的识别和分类。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/807b2110f764402fae59a952053acb26~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在 @babel/highlight 包里也是这样用的：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d30814b33d804996836b3eece6a67154~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>（正则来做词法分析有很多限制条件，比如不能处理递归的情况，所以这种方式不是通用的，通用词法分析还是得用状态机 DFA。）</p>
<p>有了分类之后，不同 token 显示不同颜色，建立个 map 就行了。</p>
<p>@babel/highlight 也是这么做的：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d6accf8c55c426dbf8b7d44df45f1e2~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们知道了怎么做语法高亮，使用 chalk 的 api 就可以打印颜色，那控制台打印颜色的原理是什么呢？</p>
<h2 data-id="heading-2">如何在控制台打印颜色</h2>
<p>控制台打印的是 <a href="https://tool.oschina.net/commons?type=4" target="_blank" rel="nofollow noopener noreferrer">ASCII 码</a>，并不是所有的编码都对应可见字符，ASCII 码有一部分字符是对应控制字符的，比如 27 是 ESC，就是我们键盘上的 ESC 键，是 escape 的缩写，按下它可以完成一些控制功能，这里我们可以通过打印 ESC 的 ASCII 码来进入控制打印颜色的状态。</p>
<p>格式是这样的：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e7d7a92f6c0459f83bcb9a9ce779a81~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>打印一个 <code>ESC</code> 的 ASCII 码，之后是 <code>[</code> 代表开始，<code>m</code> 代表结束，中间是用 <code>;</code> 分隔的 n 个控制字符，可以控制很多样式，比如前景色、背景色、加粗、下划线等等。</p>
<p>ESC 的 ASCII 码是 27，有好几种写法：一种是字符表示的 <code>\e</code> ，一种是 16 进制的 <code>\0x1b</code>（27 对应的 16进制），一种是 8 进制的 <code>\033</code>，这三种都表示 ESC。</p>
<p>我们来试验一下： 1 表示加粗、36 表示前景色为青色、4 表示下划线，下面三种写法等价：</p>
<pre><code class="hljs language-shell copyable" lang="shell">\e[36;1;4m
\033[36;1;4m
\0x1b[36;1;4m
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们来试一下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eca9c62870414489890c9570b889636b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
都打印了正确的样式！</p>
<p>当然，加了样式还要去掉，可以加一个 <code>\e[0m</code> 就可以了（<code>\033[0m</code>,<code>\0x1b[0m</code> 等价）。</p>
<p>chalk（nodejs 的在终端打印颜色的库）的不同方法就是封装了这些 ASCII 码的颜色控制字符。</p>
<p>上面每行代码被高亮过以后的代码是：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d91383b4f5854e178c16be243a09a851~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样也就实现了不同颜色的打印。</p>
<h2 data-id="heading-3">总结</h2>
<p>至此，我们能实现开头的效果了：支持 code frame 的打印，支持语法高亮，能够打印颜色</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d3c6b350af041d680b429a5f0cc55f2~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>本文我们探究了这种效果的实现原理，先从 code frame 是怎么拼接的，然后每一行的代码是怎么做高亮的，之后是高亮具体是怎么打印颜色的。</p>
<p>不管是 code frame 的打印，还是语法高亮或者控制台打印颜色，都是特别常见的功能，希望这篇文章能够帮你彻底掌握这 3 方面的原理。</p></div>  
</div>
            