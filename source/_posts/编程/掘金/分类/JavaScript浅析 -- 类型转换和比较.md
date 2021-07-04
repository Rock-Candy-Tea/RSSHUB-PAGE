
---
title: 'JavaScript浅析 -- 类型转换和比较'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7699'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 22:17:43 GMT
thumbnail: 'https://picsum.photos/400/300?random=7699'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>先看看如下几个问题，如果都能答对且知道为什么那么可以不用接着往下看了（当然想要接着看我是不会拒绝的哈哈）：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-string">''</span> == <span class="hljs-number">1</span>); <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">' '</span> == <span class="hljs-number">1</span>); <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-literal">true</span> == <span class="hljs-number">1</span>); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-literal">true</span> == <span class="hljs-string">'1'</span>); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-literal">true</span> == <span class="hljs-string">'2'</span>); <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">' '</span> == <span class="hljs-literal">true</span>); <span class="hljs-comment">// false</span>

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"0"</span> == <span class="hljs-literal">true</span>); <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"0"</span> == <span class="hljs-literal">false</span>); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"00"</span> == <span class="hljs-literal">false</span>); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"0.00"</span> == <span class="hljs-literal">false</span>); <span class="hljs-comment">// true</span>

<span class="hljs-built_in">console</span>.log(<span class="hljs-literal">undefined</span> == <span class="hljs-literal">null</span>);  <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-literal">null</span> == <span class="hljs-string">'null'</span>); <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(&#123;&#125; == <span class="hljs-literal">true</span>);  <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log([] == <span class="hljs-literal">true</span>);  <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> obj = &#123; 
  <span class="hljs-attr">a</span>: <span class="hljs-number">0</span>, 
  <span class="hljs-attr">valueOf</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;<span class="hljs-keyword">return</span> <span class="hljs-number">1</span>&#125; 
&#125; 
<span class="hljs-built_in">console</span>.log(obj==<span class="hljs-string">'[object Object]'</span>);  <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(obj==<span class="hljs-number">1</span>);  <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(obj==<span class="hljs-literal">true</span>);  <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (<span class="hljs-string">""</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'empty'</span>)
&#125; <span class="hljs-comment">// 无</span>

<span class="hljs-keyword">if</span> (<span class="hljs-string">" "</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'blank'</span>)
&#125; <span class="hljs-comment">// blank</span>

<span class="hljs-keyword">if</span> ([<span class="hljs-number">0</span>]) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'array'</span>)
&#125; <span class="hljs-comment">// array</span>

<span class="hljs-keyword">if</span>(<span class="hljs-string">'0.00'</span>)&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'0.00'</span>)
&#125; <span class="hljs-comment">// 0.00</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相信看了上面的题，一些初学的小伙伴已经开始怀疑人生了，不急不急，我们下面就先讲讲两个知识点，然后最后我们再来一一解析题目，到时候就很好理解了。</p>
<h3 data-id="heading-0">一、数据类型的互相转换</h3>
<p><strong>1. 其他类型转成Number</strong></p>





























<table><thead><tr><th>数据类型</th><th>转为值</th></tr></thead><tbody><tr><td>String</td><td>纯数字的字符串转为对应的数字，空字符串和空格字符串是0，其他字符变成NaN</td></tr><tr><td>Boolean</td><td>true为1，false为0</td></tr><tr><td>Object</td><td>调用valueOf()的返回结果，没有则返回toString()结果，若对象没有valueOf()和toString()则返回NaN</td></tr><tr><td>null</td><td>返回0</td></tr><tr><td>undefined</td><td>返回NaN</td></tr></tbody></table>
<ul>
<li>Number([])返回0，Number([3])返回3，Number([1, 2])返回NaN。</li>
</ul>
<p><strong>2. 其他类型转成String</strong></p>





























<table><thead><tr><th>数据类型</th><th>转为值</th></tr></thead><tbody><tr><td>Number</td><td>转为对应数字的字符串形式，NaN是“NaN”</td></tr><tr><td>Boolean</td><td>true为"true"，false为"false"</td></tr><tr><td>Object</td><td>返回toString()的返回值，默认是“[object Object]”</td></tr><tr><td>null</td><td>返回"null"</td></tr><tr><td>undefined</td><td>返回"undefined"</td></tr></tbody></table>
<p><strong>3. 其他类型转成Boolean</strong></p>



































<table><thead><tr><th>数据类型</th><th>转为true的值</th><th>转为false的值</th></tr></thead><tbody><tr><td>Number</td><td>任何非零数字（包括无穷大）</td><td>0、-0和NaN</td></tr><tr><td>String</td><td>任何非空字符</td><td>“”（空字符串）</td></tr><tr><td>Object</td><td>任何对象</td><td>无</td></tr><tr><td>null</td><td>无</td><td>null</td></tr><tr><td>undefined</td><td>无</td><td>undefined</td></tr></tbody></table>
<h3 data-id="heading-1">二、数据类型的比较</h3>
<p>首先强调一点，这里所讲的是==比较，而不是===比较，因为只有==在互相比较的时候会进行隐式转换再做比较，而具体规则如下：</p>
<ol>
<li>Number、String、Boolean三者的互相比较，都先转换为数字再进行比较。</li>
<li>Object和其他作比较，调用toPrimitive的返回值进行比较（先尝试调用 .valueOf 方法获取结果。 如果没定义，再尝试调用 .toString方法获取结果）。</li>
<li>null和undefined的比较不做转换，且null==undefined返回true（null===undefined返回false）。</li>
<li>NaN不与任何值相等，即使NaN==NaN返回的也是false。</li>
</ol>
<h3 data-id="heading-2">三、答案解析</h3>
<p>好了，根据上面所讲的两点，现在我们再来看看开始的题目，一一解释下：</p>
<ol>
<li>首先看这些题目：</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-string">''</span> == <span class="hljs-number">1</span>); <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">' '</span> == <span class="hljs-number">1</span>); <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-literal">true</span> == <span class="hljs-number">1</span>); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-literal">true</span> == <span class="hljs-string">'1'</span>); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-literal">true</span> == <span class="hljs-string">'2'</span>); <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">' '</span> == <span class="hljs-literal">true</span>); <span class="hljs-comment">// false</span>

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"0"</span> == <span class="hljs-literal">true</span>); <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"0"</span> == <span class="hljs-literal">false</span>); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"00"</span> == <span class="hljs-literal">false</span>); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"0.00"</span> == <span class="hljs-literal">false</span>); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据 <strong>"Number、String、Boolean三者的互相比较，都先转换为数字再进行比较"</strong>，所以上面的几个比较全都会先进行数字转换，而Number('')、Number(' ')、Number('0')、Number('00')、Number('0.00)都是0，Number(true)是1、Number(false)是0。这个时候题目实际上就变成下面这样：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-number">0</span> == <span class="hljs-number">1</span>); <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">0</span> == <span class="hljs-number">1</span>); <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span> == <span class="hljs-number">1</span>); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span> == <span class="hljs-number">1</span>); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span> == <span class="hljs-number">2</span>); <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">0</span> == <span class="hljs-number">1</span>); <span class="hljs-comment">// false</span>

<span class="hljs-built_in">console</span>.log(<span class="hljs-number">0</span> == <span class="hljs-number">1</span>); <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">0</span> == <span class="hljs-number">0</span>); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">0</span> == <span class="hljs-number">0</span>); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">0</span> == <span class="hljs-number">0</span>); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样做了转换之后的比较是不是就一目了然了？
2. 根据比较规则的第2点 <strong>“Object和其他作比较，调用toPrimitive的返回值进行比较（先尝试调用 .valueOf 方法获取结果。 如果没定义，再尝试调用 .toString方法获取结果）”</strong>，由于Number(&#123;&#125;)为NaN，Number([])为0，下面的题目</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(&#123;&#125; == <span class="hljs-literal">true</span>);  <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log([] == <span class="hljs-literal">true</span>);  <span class="hljs-comment">// false</span>

<span class="hljs-keyword">var</span> obj = &#123; 
  <span class="hljs-attr">a</span>: <span class="hljs-number">0</span>, 
  <span class="hljs-attr">valueOf</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;<span class="hljs-keyword">return</span> <span class="hljs-number">1</span>&#125; 
&#125; 
<span class="hljs-built_in">console</span>.log(obj==<span class="hljs-string">'[object Object]'</span>);  <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(obj==<span class="hljs-number">1</span>);  <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(obj==<span class="hljs-literal">true</span>);  <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就变成</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-literal">NaN</span> == <span class="hljs-number">1</span>);  <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">0</span> == <span class="hljs-number">1</span>);  <span class="hljs-comment">// false</span>

<span class="hljs-keyword">var</span> obj = &#123; 
  <span class="hljs-attr">a</span>: <span class="hljs-number">0</span>, 
  <span class="hljs-attr">valueOf</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;<span class="hljs-keyword">return</span> <span class="hljs-number">1</span>&#125; 
&#125; 
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span> == <span class="hljs-literal">NaN</span>);  <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span> == <span class="hljs-number">1</span>);  <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span> == <span class="hljs-number">1</span>);  <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>根据转换规则第3点 <strong>“null和undefined的比较不做转换，且null==undefined返回true”</strong>，下面就不用解释了吧？</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-literal">undefined</span> == <span class="hljs-literal">null</span>);  <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-literal">null</span> == <span class="hljs-string">'null'</span>); <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>而对于这种if的判断，我们可以直接转换成Boolean。由于任何对象和任何非空字符串的布尔值都是true，有Boolean('')为false，Boolean(' ')、Boolean([0])、Boolean(&#123;&#125;)为true。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span> (<span class="hljs-string">""</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'empty'</span>)
&#125; <span class="hljs-comment">// 无</span>

<span class="hljs-keyword">if</span> (<span class="hljs-string">" "</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'blank'</span>)
&#125; <span class="hljs-comment">// blank</span>

<span class="hljs-keyword">if</span> ([<span class="hljs-number">0</span>]) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'array'</span>)
&#125; <span class="hljs-comment">// array</span>

<span class="hljs-keyword">if</span>(<span class="hljs-string">'0.00'</span>)&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'0.00'</span>)
&#125; <span class="hljs-comment">// 0.00</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>最后补充两道题：</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(!<span class="hljs-string">" "</span> == <span class="hljs-literal">true</span>);  <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(!<span class="hljs-string">" "</span> == <span class="hljs-literal">false</span>);  <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于“!取反”的优先级高于“==”，所以先做布尔转化，有Boolean(" ")为true，!Boolean(" ")为false。则转化成如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-literal">false</span> == <span class="hljs-literal">true</span>);  <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-literal">false</span> == <span class="hljs-literal">false</span>);  <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时由于是两个布尔值做比较所以就不用再做转化数字的操作。over~</p></div>  
</div>
            