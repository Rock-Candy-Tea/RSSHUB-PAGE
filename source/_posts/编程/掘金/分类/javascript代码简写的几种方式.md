
---
title: 'javascript代码简写的几种方式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b1413b504ba4fbda6f7170f238e6e54~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 15 Aug 2021 01:43:13 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b1413b504ba4fbda6f7170f238e6e54~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>“<strong>这是我参与8月更文挑战的第15天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong>”</p>
<p>本文主要介绍一些工作中常用的JavaScript编码技巧。非常有用，建议大家看完赶快实践，keep it in your mind!</p>
<p>首先推荐一个vscode的插件，Quokka.js,调试代码神器，插件的作用是：立即执行你键入的JavaScript代码或者TypeScript代码</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b1413b504ba4fbda6f7170f238e6e54~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">箭头函数</h2>
<p>简写规则：</p>
<ol>
<li>只有一个参数，小括号可以不写</li>
<li>返回值只有一个，花括号和return可以不写</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> arr=[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>]

arr.filter(<span class="hljs-function">(<span class="hljs-params">item</span>)=></span>&#123;
    <span class="hljs-keyword">return</span> item ><span class="hljs-number">1</span>
&#125;)

<span class="hljs-comment">//只有一个参数，小括号可以不写</span>
arr.filter(<span class="hljs-function"><span class="hljs-params">item</span>=></span>&#123;
    <span class="hljs-keyword">return</span> item><span class="hljs-number">1</span>
&#125;)
<span class="hljs-comment">//返回值只有一个，花括号和return可以不写</span>
arr.filter(<span class="hljs-function"><span class="hljs-params">item</span>=></span>item><span class="hljs-number">1</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">掌握数组常见操作方法</h2>
<p>掌握数组常见方法，记在脑子里，不要写的时候再去看API了，这样可以有效提升编码效率，毕竟这些方法每天都在用</p>
<ul>
<li>every</li>
<li>some</li>
<li>filter</li>
<li>map</li>
<li>forEach</li>
<li>find</li>
<li>findIndex</li>
<li>reduce</li>
<li>includes</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed9d203b983c4054b1d2f8aa3a4ca7f3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">掌握字符串常用操作函数</h2>
<ul>
<li>trim</li>
<li>startsWidth</li>
<li>includes</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> str=<span class="hljs-string">"Hello JueJue  "</span>
<span class="hljs-comment">//包含子串</span>
<span class="hljs-built_in">console</span>.log(str.includes(<span class="hljs-string">"Hello"</span>))
<span class="hljs-comment">// 以子串开头</span>
<span class="hljs-built_in">console</span>.log(str.startsWith(<span class="hljs-string">"Hello"</span>))
<span class="hljs-comment">// 去除收尾空格</span>
<span class="hljs-built_in">console</span>.log(str.trim())
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">延展运算符</h2>
<p>很有用的哟，下面介绍两个使用场景：
对数组进行解构</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//数组去重</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">removeRepeat</span>(<span class="hljs-params">arr</span>)</span>&#123;
    <span class="hljs-keyword">return</span>  [...new <span class="hljs-built_in">Set</span>(arr)]
&#125;
<span class="hljs-comment">//数组求最大值</span>
<span class="hljs-built_in">Math</span>.max(...arr)
<span class="hljs-built_in">Math</span>.min(...arr)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对对象进行解构</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//react  用于一次传入多个属性</span>
<span class="hljs-keyword">let</span> props=&#123;<span class="hljs-attr">name</span>:<span class="hljs-string">'Ben'</span>,<span class="hljs-attr">age</span>:<span class="hljs-number">10</span>,<span class="hljs-attr">sex</span>:<span class="hljs-number">0</span>&#125;
<span class="hljs-keyword">const</span> greeting=<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Greeting</span> &#123;<span class="hljs-attr">...props</span>&#125; /></span></span>

<span class="hljs-comment">//组合对象 这种情况可以使用Object.assign代替</span>
<span class="hljs-keyword">let</span> defaultParams=&#123;
    <span class="hljs-attr">pageSize</span>:<span class="hljs-number">1</span>,
    <span class="hljs-attr">pageNumber</span>:<span class="hljs-number">10</span>,
    <span class="hljs-attr">sort</span>:<span class="hljs-number">1</span>
&#125;

<span class="hljs-keyword">let</span> reqParams=&#123;
    ...defaultParams,
    <span class="hljs-attr">phone</span>:<span class="hljs-string">'15196255885'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">对象简写</h2>
<p>对象的key和value同名，可以只写key,可以少些很多代码哟</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> id,age,sex

<span class="hljs-keyword">let</span> person=&#123;
    id,
    age,
    sex
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">解构赋值</h2>
<ul>
<li>用于函数参数</li>
<li>用于对对象进行解构</li>
</ul>
<p>可以少些一些代码哟</p>
<pre><code class="copyable">class Spirit&#123;
    constructor(&#123;x=0,y=0,w=10,h=10,rotate=0&#125;)&#123;//函数参数结构
        this.x=x
        this.y=y
        this.w=w
        this.h=h
        this.rotate=rotate
    &#125;
    draw()&#123;
        const &#123;x,y,w,h,rotate&#125;=this
        console.log("draw -> x,y,w,h,rotate", x,y,w,h,rotate)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">掌握数据类型转换的方法</h2>
<p>写JS的人一般没有类型观念，对于Number和String的区分不太敏感，其实JS的数据类型还是挺重要的，不注意的话就有可能会出错，所以希望大家记住下面的方法</p>
<h3 data-id="heading-7">Number和String类型互转</h3>
<p>我一般喜欢使用构造函数转</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Number</span>(<span class="hljs-string">'001'</span>)  <span class="hljs-comment">//-> 1</span>
<span class="hljs-built_in">String</span>(<span class="hljs-string">'1'</span>)   <span class="hljs-comment">// ->1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">保留n位小数</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">cutNumber</span>(<span class="hljs-params">value,n=<span class="hljs-number">2</span></span>)</span>&#123;<span class="hljs-comment">//默认保留2位小数</span>
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Number</span>(value).toFixed(n)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            