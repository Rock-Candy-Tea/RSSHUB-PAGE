
---
title: 'JavaScript继承之老王的焦虑'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2927'
author: 掘金
comments: false
date: Tue, 22 Jun 2021 01:25:05 GMT
thumbnail: 'https://picsum.photos/400/300?random=2927'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>话说有个人叫老王</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">let</span> dad = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"老王"</span>,
    <span class="hljs-attr">family</span>:<span class="hljs-string">"王氏家族"</span>
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有一天他想生个儿子，可是老王他自己也生不出来，于是他跪了七天七夜求上天怜悯，玉皇大帝于心不忍便赐给他一台儿子制造机</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sonCreator</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>玉皇大帝说，只要把这台机器注入你的血统，制造出来的就是你的儿子，老王听罢千恩万谢，随即将自己的血统注入机器</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">sonCreator.prototype = dad;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来老王就开始制造儿子了</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">let</span> son = <span class="hljs-keyword">new</span> sonCreator();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>老王问儿子，你哪家的？</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">son.family; <span class="hljs-comment">//王氏家族</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>老王又问你的名字是啥啊？</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">son.name; <span class="hljs-comment">//老王</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>老王一看大吃一惊，怎么跟我名字一样，小王微微一笑回答道：“你没给我起名字啊，我只好通过制造机找到你的名字先用着了”。老王顿悟，原来是这样啊，我给你起个名字不就完了。</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">son.name = <span class="hljs-string">"小王"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>起完名字，老王转头一想，为何不在制造儿子的时候就把名字起好呢？顺便把生日也记录一下，于是老王把儿子制造机一顿修改</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sonCreator</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">this</span>.name = <span class="hljs-string">"小王"</span> + <span class="hljs-built_in">Math</span>.random();
    <span class="hljs-built_in">this</span>.time = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后把儿子回炉重造了</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">son = <span class="hljs-keyword">new</span> sonCreator();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这下老王很开心，又制造了几个儿子</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">s2 = <span class="hljs-keyword">new</span> sonCreator();<span class="hljs-comment">//&#123; name: '小王0.47669241584207844', time: 1624352962928 &#125;</span>
s3 = <span class="hljs-keyword">new</span> sonCreator();<span class="hljs-comment">//&#123; name: '小王0.12036476430215615', time: 1624352962928 &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这下老王有3个儿子了，大儿子son调了个皮，偷偷给老王扣了个绿帽子</p>
<pre><code class="hljs language-jsx copyable" lang="jsx">son.__proto__.family = <span class="hljs-string">"八氏家族"</span>;
son.family; <span class="hljs-comment">// "八氏家族";</span>
s2.family;  <span class="hljs-comment">// "八氏家族";</span>
s3.family;  <span class="hljs-comment">// "八氏家族";</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>老王很奇怪，儿子也改不了制造机的血统信息啊？这是咋回事呢，老王赶紧问玉帝，玉帝告诉他儿子的__proto__和儿子制造器的prototype是一样的，都指向了老王自己，不仅可以访问到老王，还可以给老王带绿帽子，这可如何是好？各位读者，如何才能让小王既完整的继承老王的血统，又没办法给老王戴绿帽子呢？</p></div>  
</div>
            