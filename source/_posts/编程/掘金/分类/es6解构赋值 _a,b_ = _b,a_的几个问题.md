
---
title: 'es6解构赋值 _a,b_ = _b,a_的几个问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8860'
author: 掘金
comments: false
date: Mon, 09 Aug 2021 19:16:42 GMT
thumbnail: 'https://picsum.photos/400/300?random=8860'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>相比于传统方法需要一个额外变量来进行值交换，使用解构进行值交换十分方便。但是我想到几个问题：</p>
<h2 data-id="heading-0">1、解构赋值有没有节省空间呢？</h2>
<pre><code class="hljs language-Javascript copyable" lang="Javascript"><span class="hljs-comment">// 传统</span>

<span class="hljs-keyword">let</span> c = b;

b = a;

a = c;

<span class="hljs-comment">// 解构</span>

[a, b] = [b, a];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先思考如下操作：</p>
<pre><code class="hljs language-Javascript copyable" lang="Javascript"><span class="hljs-keyword">let</span> a = <span class="hljs-number">1</span>, b = <span class="hljs-number">2</span>;

[a, b] = [b=a, a=<span class="hljs-number">3</span>];<span class="hljs-comment">//1 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以分析出解构赋值的过程应当为</p>
<ol>
<li>以从左到右的顺序计算右侧数组的值，得到数组</li>
<li>以从左到右的顺序，将右侧数组的值赋给左侧</li>
</ol>
<p>可以看到解构复制的过程中会有一个包含两个元素的临时数组，并没有比传统方法节省空间，甚至空间会比传统方法更多一个int值大小的空间。</p>
<h2 data-id="heading-1">2、解构赋值有没有更快呢？</h2>
<p>话不多讲，直接上代码：</p>
<pre><code class="hljs language-Javascript copyable" lang="Javascript"><span class="hljs-keyword">const</span> times = <span class="hljs-number">3000000000</span>;

<span class="hljs-keyword">let</span> a = <span class="hljs-number">1</span>, b = <span class="hljs-number">2</span>;

<span class="hljs-keyword">let</span> time1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime();

<span class="hljs-keyword">while</span> (i++ < times) &#123;

  [a, b] = [b, a];

  <span class="hljs-keyword">let</span> c = b;

  b = a;

  a = c;

  <span class="hljs-keyword">let</span> d = b;

  b = a;

  a = d;

&#125;

<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime() - time1); <span class="hljs-comment">// 4300左右</span>

time1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime();

<span class="hljs-keyword">while</span> (i-- >= <span class="hljs-number">0</span>) &#123;

  [a, b] = [b, a];

  [a, b] = [b, a];

  <span class="hljs-keyword">let</span> c = b;

  b = a;

  a = c;

&#125;

<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime() - time1); <span class="hljs-comment">// 6400左右</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，解构交换值的速度更慢。按照常理猜测一下，可能是解构赋值需要申请临时数组，然后遍历数组对等号左侧的变量进行赋值，在此期间还需要检测数组元素是否为undefined，这一过程较为费时。</p>
<h2 data-id="heading-2">3、一个有趣（挠头）的发现</h2>
<pre><code class="hljs language-Javascript copyable" lang="Javascript"><span class="hljs-keyword">while</span> (i++ < times) &#123;

  [a, b] = [b, a];

  [a, b] = [b, a];

  <span class="hljs-keyword">let</span> c = b;

  b = a;

  a = c;

&#125;

<span class="hljs-keyword">while</span> (i++ < times) &#123;

  [a, b] = [b, a];

  [a, b] = [b, a];

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>肉眼观察，上面的循环内操作更多，应当耗时更多，结果却是在公司mbp上运行，前者耗时显著更少，在个人windows电脑上运行，二者耗时几乎一致。经过分析只知道可能与JIT有关，却不知道具体原因。希望有大佬可以为萌新解惑呀～</p>
<p>欢迎关注「 字节前端 ByteFE 」</p>
<p>简历投递联系邮箱「<a href="https://link.juejin.cn/?target=mailto%3Atech%40bytedance.com" target="_blank" title="mailto:tech@bytedance.com" ref="nofollow noopener noreferrer">tech@bytedance.com</a>」</p></div>  
</div>
            