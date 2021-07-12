
---
title: '判断变量类型的方法（上）：js中的数据类型1'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6694ebef1d984e05bfaffd2beec34e0b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 08:10:48 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6694ebef1d984e05bfaffd2beec34e0b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">1. js一共6种数据类型：</h3>
<ul>
<li>5中基本数据类型（也叫做简单数据类型）</li>
</ul>
<blockquote>
<p>Undefined <strong>Null</strong> Boolean Number String</p>
</blockquote>
<ul>
<li>1种复杂数据类型</li>
</ul>
<blockquote>
<p>Object</p>
</blockquote>
<h3 data-id="heading-1">2. typeof操作符检测结果</h3>
<ul>
<li>"undefined" // 这个值未定义，声明了没有给值</li>
<li>"boolean" // 这个值是布尔值</li>
<li>"string" // 这个值是字符串</li>
<li>"number" // 这个值是数值</li>
<li>"object" // 这个值是对象或null</li>
<li>"function" // 这个值是函数</li>
</ul>
<h3 data-id="heading-2">3. Null类型</h3>
<p>Null类型是第二个只有一个值的数据类型（另一个是Undefined）,这个特殊的值是null。</p>
<h4 data-id="heading-3">null的使用</h4>
<p>如果定义的变量准备在将来用于保存对象，那么最好将该变量初始化为null而不是其它值。这样一来，只要检查null值就可以知道相应的变量是否已经保存了一个对象的引用，如下面的例子所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span>(car != <span class="hljs-literal">null</span>)&#123;
 <span class="hljs-comment">// 对car 对象执行某些操作</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">typeof检测null值时会返回"object"</h4>
<p>从逻辑上讲，null值表述一个空对象指针，而这正是使用<strong>typeof检测null值时会返回"object"的原因</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6694ebef1d984e05bfaffd2beec34e0b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">undefined == null 为true</h4>
<p><strong>实际上，undefined值派生自null值，因此ECMA-262规定测试它们的相等性测试要返回true</strong></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c24e2f04f02c4a5e9370607e58359f1f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">4. Boolean类型</h3>
<ul>
<li>该类型只有两个字面值：true 和 false</li>
</ul>
<h4 data-id="heading-7">- 数据类型对应转换规则表</h4>



































<table><thead><tr><th>数据类型</th><th>转换为true的值</th><th>转换为false的值</th></tr></thead><tbody><tr><td>Boolean</td><td>true</td><td>false</td></tr><tr><td>String</td><td>任何非空字符串</td><td>"" (空字符串，注意，如果字符串有空格也不是空字符串)</td></tr><tr><td>Number</td><td>任何非零数字值（包括无穷大）</td><td>0和NaN</td></tr><tr><td>Object</td><td>任何对象</td><td>null</td></tr><tr><td>Undefined</td><td></td><td>undefined</td></tr></tbody></table>
<h3 data-id="heading-8">5. Number类型</h3>
<h4 data-id="heading-9">进制的表示</h4>
<h5 data-id="heading-10">- 10进制，</h5>
<p>最基本的数值字面量格式，可以直接在代码输入
<code>var intNum = 55 </code></p>
<h5 data-id="heading-11">- 8进制：</h5>
<p>八进制的字面值第一位必须是0,后面是8进制序列（0-7）</p>
<blockquote>
<p>在严格模式下无效，支持严格模式的JavaScript引擎会抛出错误</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> octalNum1 = <span class="hljs-number">070</span>  <span class="hljs-comment">// 八进制的56</span>
<span class="hljs-keyword">var</span> octalNum2 = <span class="hljs-number">079</span>  <span class="hljs-comment">// 无效的八进制值，接续为 79</span>
<span class="hljs-keyword">var</span> octalNum3 = <span class="hljs-number">08</span>   <span class="hljs-comment">// 无效的八进制，解析为8</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-12">- 16进制</h5>
<p>十六进制的前两位是0x,后面是16进制序列（0-9及A-F）,字母A-F也可以小写</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> hexNum1 = <span class="hljs-number">0xA</span>  <span class="hljs-comment">// 16进制的10</span>
<span class="hljs-keyword">var</span> hexNum2 = <span class="hljs-number">0x1f</span>  <span class="hljs-comment">// 16进制的31</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>在进行算术运算时，所有的8进制以及16进制表示的数值最终都会被转成16进制数值</p>
</blockquote>
<h4 data-id="heading-13">NaN</h4>
<p>Not a Number 是一个特殊的数值，这个数值便是一个本来要返回数值的操作数未返回数值的情况（这样就不会抛出错误了）</p>
<h5 data-id="heading-14">NaN的特点：</h5>
<ol>
<li>任何涉及NaN的操作（例如NaN/10）都会返回NaN。</li>
<li>NaN和任何值都不相等，包括NaN本身</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78a296558b9b4ab0a366c7ca23b9412f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-15">isNaN()函数</h5>
<ol>
<li>isNaN()在接收一个值之后，会尝试将这个值转换为数值。某些不是数值的值会直接转换为数值，例如字符串"10"或Boolean值</li>
<li>任何不能被转为数值的值都会导致这个函数返回true</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7eafd1a68bd84777b94c5b251bd8eb73~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-16">数值转换</h4>
<ol>
<li>有三个函数可以将非数值转换为数值：</li>
</ol>
<ul>
<li>Number()</li>
<li>parseInt()</li>
<li>parseFolat()</li>
</ul>
<p>Number()可以用于任何数据类型
parseInt()、parseFlost() 专门用于把字符串转换成数值
2. Number() 函数转换规则如下</p>
<ul>
<li>
<p>如果是Boolean值，true和false将分别转换为1和0</p>
</li>
<li>
<p>如果是数字值，只是简单的传入和返回</p>
</li>
<li>
<p><strong>如果是null值，返回0</strong></p>
</li>
<li>
<p><strong>如果是undefined值，返回NaN</strong></p>
</li>
<li>
<p>如果是字符串，遵循下列规则</p>
<pre><code class="copyable">1. 如果字符串中只包含数字(包括前面带正负号的情况)，则将其转换为10进制值,"011"会变成11（注意，前导0被忽略了）
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cba3feb003414bcab68531b29c2aae48~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">2. 如果字符串中包含有效的浮点格式，如"1.1"，则将其转换为对应的浮点数值（同样，也会忽略前导0）
3. 如果字符串中包含有效的16进制格式，例如"0xf",则将其转换为相同大小的10进制整数值
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f527cc433554e90b8dbd84a3c59d38a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">4、如果字符串是空的（不包含任何字符或者空格字符也是可以的），则将其转换为0
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96a39bfa7f244ad38d544b08c745579e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">5. 如果字符串中包含除上述格式之外的字符，将其转换为NaN
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6cebc87c4db54301935f353603262d54~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">6. 如果是对象，则调用对象的valueOf()方法，然后按照前面的规则转换返回的值。如皋转换的结果是NaN，则调用对象的toString()方法，然后再次依照前面的规则转换返回的字符串值
<span class="copy-code-btn">复制代码</span></code></pre>
<p>未完待续---</p>
<p>摘自：
《Javascript 高级程序设计 （第三版）》</p></div>  
</div>
            