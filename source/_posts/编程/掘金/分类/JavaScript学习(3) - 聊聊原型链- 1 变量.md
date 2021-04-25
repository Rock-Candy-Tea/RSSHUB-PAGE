
---
title: 'JavaScript学习(3) - 聊聊原型链- 1. 变量'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1517'
author: 掘金
comments: false
date: Sat, 24 Apr 2021 19:10:30 GMT
thumbnail: 'https://picsum.photos/400/300?random=1517'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><blockquote>
<p>《JavaScript高级程序设计（第三版）》学习笔记</p>
<p><a href="https://github.com/SHENLing0628/JavaScriptStudy" target="_blank" rel="nofollow noopener noreferrer">Github笔记链接（持续更新中，欢迎star，转载请标注来源）</a></p>
</blockquote>
<blockquote>
<p><strong>笔记目录：</strong></p>
<p><a href="https://juejin.cn/post/6954898562761097229" target="_blank">JavaScript学习(1) - JavaScript历史回顾</a></p>
<p><a href="https://juejin.cn/post/6954911303819345934" target="_blank">JavaScript学习(2) - 基础语法知识</a></p>
<p><a href="https://juejin.cn/post/6954927427155935262" target="_blank">JavaScript学习(3)- 聊聊原型链- 1. 变量</a></p>
</blockquote>
<hr>
<p><em><strong>关键词：JavaScript变量、基本类型、引用类型、instanceof、typeof、Object、Array</strong></em></p>
<p><strong>学习思路：学习原型链，需要先了解变量的知识，然后学习对象的创建、对象的原型，最后才是继承的关系</strong></p>
<h1 data-id="heading-0">1. 变量的基本概念</h1>






























<table><thead><tr><th></th><th>基本类型</th><th>引用类型</th></tr></thead><tbody><tr><td>概念</td><td>简单数据段</td><td>可能由多个值构成的对象</td></tr><tr><td>数据类型</td><td>Undefined, Null, Boolean, Number, String</td><td>Object</td></tr><tr><td>赋值</td><td>var name = 13</td><td>var name = new Object()<br>name.age = 13</td></tr><tr><td><strong>复制引用</strong></td><td>Var num2 = num1<br>num1和num2相互独立，改变num1不影响num2</td><td>var obj2 = obj1<br>改变obj1会影响obj2，实际引用的相同对象</td></tr></tbody></table>
<h1 data-id="heading-1">2. 基本类型</h1>








































<table><thead><tr><th>数据类型</th><th>英文表达式</th><th>typeOf 返回结果</th></tr></thead><tbody><tr><td>未定义</td><td>undefined</td><td>"undefined"</td></tr><tr><td>布尔值</td><td>Boolean</td><td>"boolean"</td></tr><tr><td>字符串</td><td>String</td><td>"string"</td></tr><tr><td>数值</td><td>Number</td><td>"number"</td></tr><tr><td>Null</td><td>Null</td><td>"object"</td></tr><tr><td>函数</td><td>function</td><td>"function"</td></tr></tbody></table>
<h1 data-id="heading-2">3. 引用类型</h1>
<blockquote>
<p><strong>常见的引用类型：Object, Array, Date, RegExp, Function</strong></p>
<p>也可以通过自定义构造函数创建自定义的引用类型，但是自定义类型本质上都是继承于默认的引用类型</p>
</blockquote>
<h2 data-id="heading-3">3.1 检测引用类型 - instanceof</h2>
<p>使用typeof并不能检测出具体是什么引用类型（object, array, date.....)</p>
<p><em>例如：null和object的typeof值都是object，无法区分</em></p>
<ol>
<li>判断具体类型 - <strong>instanceof</strong> - 返回true/false</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// instanceof样例</span>
<span class="hljs-keyword">var</span> o = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>()

alert(o <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span>)
alert(o <span class="hljs-keyword">instanceof</span> Constructor)
alert(o <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">RegExp</span>)  
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>对于某些类型，同样可用自身的类型检测方法</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// Array类型 - 检测方法：Array.isArray()</span>
alert(<span class="hljs-built_in">Array</span>.isArray(colors)) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">3.2 Object类型</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 创建Object</span>
<span class="hljs-comment">// 1. new一个Object对象，使用Object构造函数，并添加属性</span>
<span class="hljs-keyword">var</span> person = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>()
person.name = <span class="hljs-string">"Cindy"</span>
person.age = <span class="hljs-number">27</span>

<span class="hljs-comment">// 2. 对象字面量法 - 用JSON对象的方式直接创建</span>
<span class="hljs-keyword">var</span> person = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"Cindy"</span>,
  <span class="hljs-attr">age</span>: <span class="hljs-number">27</span>
&#125;
<span class="hljs-comment">// 备注：对象字面量法不设置属性值创建时，同 new Object() 相同</span>
<span class="hljs-keyword">var</span> person = &#123;&#125; <span class="hljs-comment">// 和 new Object() 相同</span>

<span class="hljs-comment">// 对象访问方法</span>
person.name     <span class="hljs-comment">// 输出：Cindy</span>
person[<span class="hljs-string">"name"</span>]  <span class="hljs-comment">// 输出：Cindy - 方括号传入string的方法便于传入变量，以动态获取对象中不同值</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">3.3 Array类型</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 创建方法</span>
<span class="hljs-comment">// 1. new一个Array对象，使用Array构造函数</span>
<span class="hljs-keyword">var</span> colors = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>()
<span class="hljs-keyword">var</span> colors = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-number">20</span>)
<span class="hljs-keyword">var</span> colors = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>(<span class="hljs-string">'red'</span>, <span class="hljs-string">'blue'</span>, <span class="hljs-string">'yellow'</span>)
<span class="hljs-keyword">var</span> colors = <span class="hljs-built_in">Array</span>(<span class="hljs-string">"Gray"</span>) <span class="hljs-comment">// 可以不用new</span>

<span class="hljs-comment">// 2. 数组字面量法</span>
<span class="hljs-keyword">var</span> colors = []
<span class="hljs-keyword">var</span> colors = [<span class="hljs-string">'red'</span>, <span class="hljs-string">'blue'</span>, <span class="hljs-string">'yellow'</span>]


<span class="hljs-comment">// 对象访问方法</span>
<span class="hljs-comment">// 1. Array对象包含length属性</span>
alert(colors.length) <span class="hljs-comment">// 3</span>

<span class="hljs-comment">// 2. Array对象可用下角标引用</span>
colors[<span class="hljs-number">0</span>] = <span class="hljs-string">"gray"</span>
alert(colors[<span class="hljs-number">0</span>]) <span class="hljs-comment">// 输出：“gray”</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">3.4 Date类型</h2>
<ul>
<li>推荐momentjs库进行时间日期转换</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 创建一个日期对象，自动获取当前日期</span>
<span class="hljs-keyword">var</span> now = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()

<span class="hljs-comment">// 接收日期表示字符串，转换为相应日期毫秒数</span>
<span class="hljs-built_in">Date</span>.parse(<span class="hljs-string">"6/13/2008"</span>)

<span class="hljs-comment">// 日期格式化</span>
toDateString()       <span class="hljs-comment">// 以特定实现的格式显示星期几、月、日和年</span>
toTimeString()       <span class="hljs-comment">// 以特定实现的格式显示时、分、秒和时区</span>
toLocaleDateString() <span class="hljs-comment">// 以特定于地区的格式显示星期几、月、日和年</span>
toLocaleTimeString() <span class="hljs-comment">// 以特定于地区的格式显示时、分、秒</span>
toUTCString()        <span class="hljs-comment">// 以特定实现的格式显示UTC日期</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">3.5 RegExp类型</h2>
<p>使用类似Perl语法，创建正则表达式</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> expression = <span class="hljs-regexp">/ pattern /</span> flag
<span class="copy-code-btn">复制代码</span></code></pre>
<p>flag - 表名正则表达式行为：</p>
<ol>
<li>g - 全局模式，应用于所有字符串</li>
<li>i - 不区分大小写</li>
<li>m - 多行模式，到达一行文本末尾时还会继续查找下一行中是否存在与模式匹配的项</li>
</ol>
<h2 data-id="heading-8">3.6 Function类型（本章节中简要说明，将会在闭包章节中详细说明）</h2>
<h3 data-id="heading-9">3.6.1 函数声明方法</h3>
<blockquote>
<p><strong>解析器会率先读取函数声明，添加到执行环境中，故调用时，代码可写在函数声明之前</strong></p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 函数声明 - 语法：</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">funName</span> (<span class="hljs-params">arg0, arg1, arg2</span>) </span>&#123;
  <span class="hljs-comment">// 函数体</span>
&#125;

<span class="hljs-comment">// 函数声明提升 - 调用语句可以在函数声明之前，因为执行前代码会先读取函数声明</span>
sayHi()
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sayHi</span>(<span class="hljs-params"></span>) </span>&#123;
  alert(<span class="hljs-string">'Hi'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">3.6.2 函数表达式法</h3>
<blockquote>
<p><strong>解析器无法对函数声明进行提升，率先添加到执行环境，故调用时，必须写在表达式之后</strong></p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 函数表达式 - 语法 - 将一个匿名函数赋值给一个变量</span>
<span class="hljs-comment">// 匿名函数：function没有命名</span>
<span class="hljs-keyword">var</span> funName = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">arg0, arg1, arg2</span>) </span>&#123;
  <span class="hljs-comment">// 函数体</span>
&#125;

<span class="hljs-comment">// 函数表达式不能进行函数声明提升，调用要在表达式后面</span>
<span class="hljs-keyword">var</span> sayHi = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123; 
  alert(<span class="hljs-string">'Hi'</span>)
&#125;
sayHi()
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">3.6.3 关于function需要注意的问题：</h3>
<ol>
<li>function指针引用</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 指针引用</span>
<span class="hljs-keyword">var</span> sum2 = sum1 <span class="hljs-comment">// sum1和sum2均指向同一个function内容</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>function没有重载</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 用指针解释function没有重载</span>
<span class="hljs-keyword">var</span> add1 = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">num</span>) </span>&#123; <span class="hljs-keyword">return</span> num + <span class="hljs-number">100</span> &#125;
add1 = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">num</span>) </span>&#123; <span class="hljs-keyword">return</span> num + <span class="hljs-number">200</span> &#125; <span class="hljs-comment">//创建第二个函数的时候，实际上覆盖了第一个引用，故没有重载</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            