
---
title: 'JS实用篇复习笔记（4）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0bbe2ac11a6a412a923053f02ec6144d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 23:43:39 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0bbe2ac11a6a412a923053f02ec6144d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1、比较大小</h2>
<p>1、比较返回值为 布尔值</p>
<pre><code class="copyable">alert( 2 > 1 ); // true (correct)
alert( 2 == 1 ); // false(wrong) 
alert( 2 != 1 ); // true (correct)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>可将比较结果赋值</li>
</ul>
<pre><code class="copyable">let result = 5 > 4; // assign the result of the comparison alert( result ); // true
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、字符串比较</p>
<p>字符串是一个字母一个字母的比较</p>
<pre><code class="copyable">alert( 'Z' > 'A' ); // true 
alert( 'Glow' > 'Glee' ); // true 
alert( 'Bee' > 'Be' ); // true
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、不同类型值比较</p>
<p><code>比较不同类型的值时</code>，JavaScript 会将值<code>转换为数字</code></p>
<pre><code class="copyable">alert( '2' > 1 ); // true, string '2' becomes a number 2 
alert( '01' == 1 ); // true, string '01' becomes a number 1
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>神奇的事情</li>
<li>因为 0/’0‘ 都会转为 0</li>
</ul>
<pre><code class="copyable">let a = 0; alert( Boolean(a) ); // false
let b = "0"; alert( Boolean(b) ); // true
alert(a == b); // true!
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4、严格相等 ===</p>
<ul>
<li><code>一般常用 === </code>比较少用 == 在 == null 时会使用</li>
</ul>
<pre><code class="copyable">alert( 0 === false ); // false, because the types are different
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>神奇的事情</li>
<li>记住这个 特殊的事情 值<code>null</code>和彼此<code>undefined</code>相等<code>==</code>，不等于任何其他值</li>
</ul>
<pre><code class="copyable">`null/undefined`转换为数字：`null`变成`0`，而`undefined`变成`NaN`

alert( null == undefined ); // true

alert( undefined > 0 ); // false (1)
alert( undefined < 0 ); // false (2) 
alert( undefined == 0 ); // false (3)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">9 > 3 → true 
"app" > "pine" → false  字符串为字符比较 a < p
"2" > "19" → true       字符串间从第一个开始比较  2 > 1 为 true
undefined == null → true  
undefined === null → false   `null`和彼此`undefined`相等`==`，不等于任何其他值
null == "\n0\n" → false
null === +"\n0\n" → false

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">2、if 条件判断</h2>
<ul>
<li>
<p><code>if(...)</code>语句计算括号中的条件，如果结果为<code>true</code>，则执行代码块</p>
</li>
<li>
<p>三元表达式 （简化if else if ）</p>
</li>
</ul>
<pre><code class="copyable">let result = condition ? value1 : value2;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>可以 将多个三元 连接起来，不过一般不这样用，维护性差</p>
</li>
<li>
<p>来个小问题  会打印吗 ？</p>
</li>
<li>
<p>当然 前提是 我们已经知道 除了空字符串（并且<code>"0"</code>不为空）之外的任何字符串都将出现<code>true</code>在逻辑上下文中</p>
</li>
</ul>
<pre><code class="copyable">if ("0") &#123; alert( 'Hello' ); &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">3、神奇运算符</h2>
<p>1、??</p>
<ul>
<li>什么意思 ？</li>
</ul>
<p><code>a ?? b</code>：</p>
<ul>
<li>如果<code>a</code>已定义，则<code>a</code>，</li>
<li>如果<code>a</code>未定义，则<code>b</code>.</li>
</ul>
<pre><code class="copyable">let user; 
alert(user ?? "Anonymous"); // Anonymous (user not defined) user没有赋值 

let user = "John"; 
alert(user ?? "Anonymous"); // John (user defined) user赋值了 选这个



<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、和 || && 连用</p>
<pre><code class="copyable">let x = 1 && 2 ?? 3; // Syntax error

let x = (1 && 2) ?? 3; // Works
alert(x);  // 2

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0bbe2ac11a6a412a923053f02ec6144d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">4、循环 loop</h2>
<p>1、while</p>
<ul>
<li><code>condition</code>是真的，<code>code</code>但循环体中的 会被执行</li>
</ul>
<pre><code class="copyable">while (condition) &#123; // code // so-called "loop body" &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>单行正文不需要花括号</li>
</ul>
<pre><code class="copyable">let i = 3; 
while (i) alert(i--);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>do...while</li>
</ul>
<pre><code class="copyable">do &#123; // loop body &#125; while (condition);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、for</p>
<ul>
<li>最常用的循环方式</li>
</ul>
<pre><code class="copyable">for (begin; condition; step) &#123; // ... loop body ... &#125;

for (let i = 0; i < 3; i++) &#123; // shows 0, then 1, then 2 alert(i); &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>请注意，必须存在两个<code>for</code>分号<code>;</code>。否则会出现语法错误</li>
<li>但 for的三部分 都可以省略</li>
<li>那么 下面这个会打印 什么内容 ？</li>
</ul>
<pre><code class="copyable">for (;;) &#123; // repeats without limits &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>继续下一次 循环  continue ... break</li>
</ul>
<p>该<code>continue</code>指令是<code>break</code>. 它不会停止整个循环。相反，它停止当前迭代并强制循环开始新的循环（如果条件允许）</p>
<ul>
<li>来个问题 这个打印啥 ？</li>
</ul>
<pre><code class="copyable">let i = 3; while (i) &#123; alert( i-- ); &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>再来两个</li>
</ul>
<pre><code class="copyable">let i = 0; while (++i < 5) alert( i ); //++在前 立马加

let i = 0; while (i++ < 5) alert( i );// ++在后 先使用之前的值

for (let i = 0; i < 5; i++) alert( i );
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、switch  case</p>
<ul>
<li>将<code>switch</code>有一个或多个<code>case</code>模块和一个可选的默认值</li>
<li>这个 在 redux 使用 也比较多 在 reducer中 进行 不同 actions的判断 并且处理</li>
</ul>
<pre><code class="copyable">switch(x) &#123; 
case 'value1': // if (x === 'value1') 
    ... [break] 
case 'value2': // if (x === 'value2') 
    ... [break] 
default: 
    ... [break] 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// 这是个例子 你说他打印出什么 ？ 

let a = 2 + 3; 
switch (a) &#123;
case 3: alert( 'Too small' ); 
    break; 
case 4: alert( 'Exactly!' ); 
    break;
case 5: alert( 'Too big' ); 
    break; 
default: 
    alert( "I don't know such values" ); &#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            