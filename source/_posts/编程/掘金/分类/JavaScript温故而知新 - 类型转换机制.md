
---
title: 'JavaScript温故而知新 - 类型转换机制'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/502ae65d55de43c8921a6f602de7a4cf~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 03:06:19 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/502ae65d55de43c8921a6f602de7a4cf~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:25px;margin-bottom:5px;border-left:5px solid #773098&#125;.markdown-body h1,.markdown-body h2&#123;display:inline-block;font-weight:700;padding-left:10px&#125;.markdown-body h2&#123;font-size:18px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:16px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;border-radius:6px;display:block;margin:20px auto;object-fit:contain;box-shadow:2px 4px 7px #999&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-size:12px;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#d89cf6&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第7天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h2 data-id="heading-0">概述</h2>
<p>JS中有六种简单数据类型：undefined、null、boolean、string、number、symbol，以及引用类型：object</p>
<p>但是我们在声明的时候只有一种数据类型，只有到运行期间才会确定当前类型</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> x = y ? <span class="hljs-number">1</span> : a;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，x的值在编译阶段是无法获取的，只有等到程序运行时才能知道</p>
<p>虽然变量的数据类型是不确定的，但是各种运算符对数据类型是有要求的，如果运算子的类型与预期不符合，就会触发类型转换机制</p>
<p>常见的类型转换有：</p>
<ul>
<li>
<p>强制转换（显式转换）</p>
</li>
<li>
<p>自动转换（隐式转换）</p>
</li>
</ul>
<h2 data-id="heading-1">显式转换</h2>
<p>显式转换，即我们很清楚可以看到这里发生了类型的转变，常见的方法有：</p>
<ul>
<li>
<p>Number()</p>
</li>
<li>
<p>parseInt()</p>
</li>
<li>
<p>String()</p>
</li>
<li>
<p>Boolean()</p>
</li>
</ul>
<h3 data-id="heading-2">Number()</h3>
<p>将任意类型的值转化为数值</p>
<p>先给出类型转换规则：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/502ae65d55de43c8921a6f602de7a4cf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>实践一下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Number</span>(<span class="hljs-number">324</span>) <span class="hljs-comment">// 324</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>字符串：如果可以被解析为数值，则转换为相应的数值</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Number</span>(<span class="hljs-string">'324'</span>) <span class="hljs-comment">// 324</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>字符串：如果不可以被解析为数值，返回 NaN</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Number</span>(<span class="hljs-string">'324abc'</span>) <span class="hljs-comment">// NaN</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>空字符串转为0</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Number</span>(<span class="hljs-string">''</span>) <span class="hljs-comment">// 0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>布尔值：true 转成 1，false 转成 0</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Number</span>(<span class="hljs-literal">true</span>) <span class="hljs-comment">// 1</span>

<span class="hljs-built_in">Number</span>(<span class="hljs-literal">false</span>) <span class="hljs-comment">// 0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>undefined：转成 NaN</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Number</span>(<span class="hljs-literal">undefined</span>) <span class="hljs-comment">// NaN</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>null：转成0</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Number</span>(<span class="hljs-literal">null</span>) <span class="hljs-comment">// 0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对象：通常转换成NaN(除了只包含单个数值的数组)</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Number</span>(&#123;<span class="hljs-attr">a</span>: <span class="hljs-number">1</span>&#125;) <span class="hljs-comment">// NaN</span>

<span class="hljs-built_in">Number</span>([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]) <span class="hljs-comment">// NaN</span>

<span class="hljs-built_in">Number</span>([<span class="hljs-number">5</span>]) <span class="hljs-comment">// 5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面可以看到，Number转换的时候是很严格的，只要有一个字符无法转成数值，整个字符串就会被转为NaN</p>
<h3 data-id="heading-3">parseInt()</h3>
<p>parseInt相比Number，就没那么严格了，parseInt函数逐个解析字符，遇到不能转换的字符就停下来</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">parseInt</span>(<span class="hljs-string">'32a3'</span>) <span class="hljs-comment">//32</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">String()</h3>
<p>可以将任意类型的值转化成字符串</p>
<p>给出转换规则图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a2fff74945447359d6ee3ec3f67bb2d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>实践一下：</p>
<p>数值：转为相应的字符串</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">String</span>(<span class="hljs-number">1</span>) <span class="hljs-comment">// "1"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>字符串：转换后还是原来的值</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">String</span>(<span class="hljs-string">"a"</span>) <span class="hljs-comment">// "a"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>布尔值：true转为字符串"true"，false转为字符串"false"</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">String</span>(<span class="hljs-literal">true</span>) <span class="hljs-comment">// "true"</span>

<span class="hljs-comment">//undefined：转为字符串"undefined"</span>

<span class="hljs-built_in">String</span>(<span class="hljs-literal">undefined</span>) <span class="hljs-comment">// "undefined"</span>

<span class="hljs-comment">//null：转为字符串"null"</span>

<span class="hljs-built_in">String</span>(<span class="hljs-literal">null</span>) <span class="hljs-comment">// "null"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">对象</h3>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-built_in">String</span>(&#123;<span class="hljs-attr">a</span>: <span class="hljs-number">1</span>&#125;) <span class="hljs-comment">// "[object Object]"</span>

<span class="hljs-built_in">String</span>([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]) <span class="hljs-comment">// "1,2,3"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">Boolean()</h3>
<p>可以将任意类型的值转为布尔值，转换规则如下：</p>
<p>实践一下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Boolean</span>(<span class="hljs-literal">undefined</span>) <span class="hljs-comment">// false</span>

<span class="hljs-built_in">Boolean</span>(<span class="hljs-literal">null</span>) <span class="hljs-comment">// false</span>

<span class="hljs-built_in">Boolean</span>(<span class="hljs-number">0</span>) <span class="hljs-comment">// false</span>

<span class="hljs-built_in">Boolean</span>(<span class="hljs-literal">NaN</span>) <span class="hljs-comment">// false</span>

<span class="hljs-built_in">Boolean</span>(<span class="hljs-string">''</span>) <span class="hljs-comment">// false</span>

<span class="hljs-built_in">Boolean</span>(&#123;&#125;) <span class="hljs-comment">// true</span>

<span class="hljs-built_in">Boolean</span>([]) <span class="hljs-comment">// true</span>

<span class="hljs-built_in">Boolean</span>(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Boolean</span>(<span class="hljs-literal">false</span>)) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">隐式转换</h2>
<p>在隐式转换中，我们可能最大的疑惑是 ：何时发生隐式转换？</p>
<p>我们这里可以归纳为两种情况发生隐式转换的场景：</p>
<ul>
<li>
<p>比较运算（==、!=、>、<）、if、while需要布尔值地方</p>
</li>
<li>
<p>算术运算（+、-、*、/、%）</p>
</li>
</ul>
<p>除了上面的场景，还要求运算符两边的操作数不是同一类型</p>
<p>自动转换为布尔值</p>
<p>在需要布尔值的地方，就会将非布尔值的参数自动转为布尔值，系统内部会调用Boolean函数</p>
<p>可以得出个小结：</p>
<ul>
<li>
<p>undefined</p>
</li>
<li>
<p>null</p>
</li>
<li>
<p>false</p>
</li>
<li>
<p>+0</p>
</li>
<li>
<p>-0</p>
</li>
<li>
<p>NaN</p>
</li>
<li>
<p>""</p>
</li>
</ul>
<p>除了上面几种会被转化成false，其他都换被转化成true</p>
<p>自动转换成字符串</p>
<p>遇到预期为字符串的地方，就会将非字符串的值自动转为字符串</p>
<p>具体规则是：先将复合类型的值转为原始类型的值，再将原始类型的值转为字符串</p>
<p>常发生在+运算中，一旦存在字符串，则会进行字符串拼接操作</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">'5'</span> + <span class="hljs-number">1</span> <span class="hljs-comment">// '51'</span>

<span class="hljs-string">'5'</span> + <span class="hljs-literal">true</span> <span class="hljs-comment">// "5true"</span>

<span class="hljs-string">'5'</span> + <span class="hljs-literal">false</span> <span class="hljs-comment">// "5false"</span>

<span class="hljs-string">'5'</span> + &#123;&#125; <span class="hljs-comment">// "5[object Object]"</span>

<span class="hljs-string">'5'</span> + [] <span class="hljs-comment">// "5"</span>

<span class="hljs-string">'5'</span> + <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>)</span>&#123;&#125; <span class="hljs-comment">// "5function ()&#123;&#125;"</span>

<span class="hljs-string">'5'</span> + <span class="hljs-literal">undefined</span> <span class="hljs-comment">// "5undefined"</span>

<span class="hljs-string">'5'</span> + <span class="hljs-literal">null</span> <span class="hljs-comment">// "5null"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>自动转换成数值</p>
<p>除了+有可能把运算子转为字符串，其他运算符都会把运算子自动转成数值</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">'5'</span> - <span class="hljs-string">'2'</span> <span class="hljs-comment">// 3</span>

<span class="hljs-string">'5'</span> * <span class="hljs-string">'2'</span> <span class="hljs-comment">// 10</span>

<span class="hljs-literal">true</span> - <span class="hljs-number">1</span>  <span class="hljs-comment">// 0</span>

<span class="hljs-literal">false</span> - <span class="hljs-number">1</span> <span class="hljs-comment">// -1</span>

<span class="hljs-string">'1'</span> - <span class="hljs-number">1</span>   <span class="hljs-comment">// 0</span>

<span class="hljs-string">'5'</span> * []    <span class="hljs-comment">// 0</span>

<span class="hljs-literal">false</span> / <span class="hljs-string">'5'</span> <span class="hljs-comment">// 0</span>

<span class="hljs-string">'abc'</span> - <span class="hljs-number">1</span>   <span class="hljs-comment">// NaN</span>

<span class="hljs-literal">null</span> + <span class="hljs-number">1</span> <span class="hljs-comment">// 1</span>

<span class="hljs-literal">undefined</span> + <span class="hljs-number">1</span> <span class="hljs-comment">// NaN</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>null转为数值时，值为0 。undefined转为数值时，值为NaN</p></div>  
</div>
            