
---
title: '测试 js 方法运行时间'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4261c703c715439994c60a3ddf22f407~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 19 Jul 2021 23:54:45 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4261c703c715439994c60a3ddf22f407~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">testFunctionTime</span>(<span class="hljs-params">fn</span>) </span>&#123;
　　<span class="hljs-keyword">var</span> start = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime();
　　<span class="hljs-keyword">if</span> (fn) fn();
　　<span class="hljs-keyword">var</span> end = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime();
　　<span class="hljs-built_in">console</span>.log(end-start);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但当遇上 ajax 和 img.onload 的时候那就很尴尬了...</p>
<p>于是我找到了 console.time(label) 和 console.timeEnd(label)，非常 nice ！</p>
<p>在开始的地方写上 console.time("测试 fn 速度: ") ，在结束的地方写上 console.timeEnd("测试 fn 速度: ") </p>
<p>label 得相同，然后你就懂了呀，来，互相伤害</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4261c703c715439994c60a3ddf22f407~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ad1ef2ff3044cb9a1fe3913c622a343~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>此外，我也对 console 产生了一点兴趣就去测试了更多它的方法，列几个个人最近用的较多的：</p>
<p>console.count(label)  输出运行次数</p>
<p>console.table(object|array)  输出表格形态的数据（在动态绘制的检查时用的较多）</p>
<p>console.group(label) 和 console.groupEnd(label) 将 console 结果进行分组（分类及减少输出版面，但也加大了我们的脑回路呀）（group = groupCollapsed 是一样的）</p>
<p>console.trace() 检测方法的调用来源，超级赞</p>
<p>console.profile(label) 和 console.profileEnd(label) 是 time 的升级版，不但测速，直接测性能了，需要到 profile 面板里面才能看到结果</p>
<p>console.assert(boolean, string) 提示报错可以少个判断</p>
<p>其实 console.error(), console.info(), console.warn() 实在用得少，用好了应该还是很赞的...吧</p>
<p>至于其他方法个人感觉就很鸡肋了，如果你也感兴趣，也可以去搜搜看。</p>
<p> </p>
<p>此外，有个装逼的好方法，console.log 可以带样式哟，赶紧试试吧</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"%cHello"</span>,<span class="hljs-string">"color:red"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><br>
\</p></div>  
</div>
            