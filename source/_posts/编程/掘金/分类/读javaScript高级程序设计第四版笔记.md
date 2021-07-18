
---
title: '读javaScript高级程序设计第四版笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9118'
author: 掘金
comments: false
date: Sat, 17 Jul 2021 22:46:42 GMT
thumbnail: 'https://picsum.photos/400/300?random=9118'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">let 和var区别</h2>
<p><code>let</code>声明的范围是块作用域，<code>var</code>声明范围是函数作用域；</p>
<p><code>let</code>也不允许同一个块作用域中出现冗余声明；</p>
<p>对声明冗余报错不会因混用<code>let</code>和<code>var</code>而受影响，这两个关键字声明的并不是不用类型的变量，他们只是指出变量在相关作用域如何存在;</p>
<p><code>var</code>可以变量提升；<code>let</code> 不可以(严格来讲，let也会被提升)，在<code>let</code>声明之前的执行瞬间被称为“暂时性死区”</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span>(<span class="hljs-literal">true</span>)&#123;
    <span class="hljs-keyword">var</span> name = <span class="hljs-string">'chc'</span>;
    <span class="hljs-keyword">var</span> name;
    <span class="hljs-keyword">let</span> name;<span class="hljs-comment">//SyntaxError</span>
    <span class="hljs-keyword">let</span> age = <span class="hljs-number">18</span>;
    <span class="hljs-keyword">let</span> age; <span class="hljs-comment">//SynctaxError;标识符age已经声明过了</span>
    <span class="hljs-keyword">var</span> age;<span class="hljs-comment">//SyntaxError</span>
    <span class="hljs-built_in">console</span>.log(name);<span class="hljs-comment">//chc</span>
    <span class="hljs-built_in">console</span>.log(age);<span class="hljs-comment">//18</span>
&#125;
<span class="hljs-built_in">console</span>.log(name);<span class="hljs-comment">//chc</span>
<span class="hljs-built_in">console</span>.log(age);<span class="hljs-comment">//ReferenceError:age没有定义</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">const</h2>
<p>使用cosnt声明变量必须同时初始化为某个值，已经声明，在其生命周期的任何时候都不能在重新赋予新值；</p>
<p>赋值为对象的const变量不能再被重新赋值为其他引用值，但对象的键则不受限制</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> a = &#123;&#125;;
a = &#123;&#125;;<span class="hljs-comment">//TypeError</span>
<span class="hljs-keyword">const</span> b = &#123;&#125;;
b.name = <span class="hljs-string">'chc'</span>;
<span class="hljs-built_in">console</span>.log(b.name);<span class="hljs-comment">//‘chc'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果想让整个对象都不能修改，可以使用<code>Object.freeze()</code>,这样再给属性赋值时虽然不会报错，但会静默失败：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> c = <span class="hljs-built_in">Object</span>.freeze(&#123;&#125;);
c.name = <span class="hljs-string">'chc'</span>;
<span class="hljs-built_in">console</span>.log(c.name);<span class="hljs-comment">//undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">javaScript变量类型</h2>
<p>javaScript变量可以保存两种类型的值：原始值和引用值。</p>
<p>原始值可能是以下6种数据类型之一：</p>
<ul>
<li>Underfined</li>
<li>Null</li>
<li>Boolean</li>
<li>Number</li>
<li>String</li>
<li>Symbol</li>
</ul>
<p>引用值：</p>
<ul>
<li>Object</li>
</ul>
<p>原始值和引用值特点如下：</p>
<ul>
<li>原始值大小固定，因此保存在栈内存上</li>
<li>从一个变量到另一个变量复制原始值会创建该值的第二个副本</li>
<li>引用值是对象，存储在堆内存中</li>
<li>包含引用值得变量实际上只包含指向相应对象得一个指针，而不是对象本身</li>
<li>从一个变量到另一个变量复制引用值只会复制指针，因此结果是两个变量都指向同一个对象</li>
<li>typeof操作符可以确定值的原始类型，而instanceof操作符用于确保值的引用类型</li>
</ul>
<h1 data-id="heading-3">数值的方法</h1>
<h2 data-id="heading-4">数值格式化为字符串(toFixed())</h2>
<ul>
<li>
<p><code>toFixed()</code>方法返回包含指定小数点位数的数值字符串,如果数值本身的小数位超过了参数指定的位数，则四舍五入到最接近的小数位：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> num = <span class="hljs-number">10</span>;
<span class="hljs-built_in">console</span>.log(num.toFixed(<span class="hljs-number">2</span>));<span class="hljs-comment">//'10.00'</span>
<span class="hljs-keyword">let</span> num2 = <span class="hljs-number">10.005</span>;
<span class="hljs-built_in">console</span>.log(num2.toFixed(<span class="hljs-number">2</span>));<span class="hljs-comment">//'10.01'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><code>toExponential()</code>,返回以科学计数法表示的数值字符串，接受一个参数，表示结果中的小数的位数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> num = <span class="hljs-number">10</span>;
<span class="hljs-built_in">console</span>.log(num.toExponential(<span class="hljs-number">1</span>));<span class="hljs-comment">//'1.0e+1'</span>
<span class="hljs-built_in">console</span>.log(num.toExponential(<span class="hljs-number">2</span>));<span class="hljs-comment">//'1.00e+1'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>toPrecision()方法会根据情况返回最合理的输出结果，可能是固定长度，也可能是科学计数法形式。接受一个参数，表示结果中数字的总位数（不包含指数）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> num = <span class="hljs-number">99</span>;
<span class="hljs-built_in">console</span>.log(num.toPrecision(<span class="hljs-number">1</span>));<span class="hljs-comment">//'1e+2'</span>
<span class="hljs-built_in">console</span>.log(num.toPrecision(<span class="hljs-number">2</span>));<span class="hljs-comment">//'1.0e+2'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>本质上，<code>toPrecison()</code>方法会根据数值的精度来决定调用<code>toFixed()</code>还是<code>toExponential()</code>。为了以正确的小数位精确表示数值，这三个方法都会向上或向下舍入。</p>
<h2 data-id="heading-5">isInteger()和isSafeInteger()</h2>
<ul>
<li>
<p>Es6新增了Number.isInteger()方法，用于辨别一个数值是否保存为整数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Number</span>.isInteger(<span class="hljs-number">1</span>));<span class="hljs-comment">//true</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Number</span>.isInteger(<span class="hljs-number">1.000</span>));<span class="hljs-comment">//true</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Number</span>.isInteger(<span class="hljs-number">1.01</span>));<span class="hljs-comment">//false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>Number.MIN_SAFE_INTEGER(-2^53+1) ~ Number.MIN_SAFE_INTEGER(2^53-1)为IEEE754数值格式的一个特殊的数值范围,为鉴别整数是否在这个范围内，可以使用Number.isSafeInteger()方法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Number</span>.isSafeInteger(数值))<span class="hljs-comment">//true or false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h1 data-id="heading-6">字符串的方法</h1>
<h2 data-id="heading-7">字符串位置方法(indexOf())</h2>
<p>有两个方法用于在字符串中定位子字符串：</p>
<ul>
<li>
<p><code>indexOf()</code>方法从字符串开头查找子字符串</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> stringValue = <span class="hljs-string">'hello world'</span>
<span class="hljs-built_in">console</span>.log(stringValue.indexOf(<span class="hljs-string">'o'</span>));<span class="hljs-comment">//4</span>
<span class="hljs-comment">//第二个参数表示开始查找的位置</span>
<span class="hljs-built_in">console</span>.log(stringValue.indexOf(<span class="hljs-string">'0'</span>,<span class="hljs-number">6</span>));<span class="hljs-comment">//7</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><code>lastIndexOf()</code>方法从字符串末尾开始查找子字符串</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> stringValue = <span class="hljs-string">'hello world'</span>;
<span class="hljs-built_in">console</span>.log(stringValue.lastIndexOf(<span class="hljs-string">'o'</span>));<span class="hljs-comment">//7</span>
<span class="hljs-comment">//第二个参数表示从末尾开始往前数排除在查找范围的字符串</span>
<span class="hljs-built_in">console</span>.log(stringValue.lastIndexOf(<span class="hljs-string">'0'</span>,<span class="hljs-number">6</span>));<span class="hljs-comment">//4</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-8">判断字符串是否包含子字符串</h2>
<p>ECMAScript6增加了3个用于判断子字符串是否包含另一个字符串的方法：</p>
<ul>
<li>
<p>startsWith()检查开始于索引0的匹配项</p>
</li>
<li>
<p>endsWith()检查开始于索引（string.length - substring.length)的匹配项，</p>
</li>
<li>
<p>includex()检查整个字符串</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> message = <span class="hljs-string">'foobarbaz'</span>
<span class="hljs-built_in">console</span>.log(message.startsWith(<span class="hljs-string">'foo'</span>));<span class="hljs-comment">//true</span>
<span class="hljs-built_in">console</span>.log(message.startsWith(<span class="hljs-string">'bar'</span>));<span class="hljs-comment">//false</span>
<span class="hljs-built_in">console</span>.log(message.endsWith(<span class="hljs-string">'baz'</span>));<span class="hljs-comment">//true</span>
<span class="hljs-built_in">console</span>.log(message.endsWith(<span class="hljs-string">'bar'</span>));<span class="hljs-comment">//false</span>
<span class="hljs-built_in">console</span>.log(message.includes(<span class="hljs-string">'bar'</span>));<span class="hljs-comment">//true</span>
<span class="hljs-built_in">console</span>.log(message.includes(<span class="hljs-string">'qux'</span>));<span class="hljs-comment">//false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>startsWith(),includes()方法添加第二个参数,表示开始搜索的位置。如果传入第二个参数，则意为着这两个方法会从指定位置向字符串末尾搜索，忽略该位置之前的所有字符。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> message = <span class="hljs-string">'foobarbaz'</span>;
<span class="hljs-built_in">console</span>.log(message.startsWith(<span class="hljs-string">'foo'</span>));<span class="hljs-comment">//true</span>
<span class="hljs-built_in">console</span>.log(message.startsWith(<span class="hljs-string">'foo'</span>,<span class="hljs-number">1</span>));<span class="hljs-comment">//false</span>
<span class="hljs-built_in">console</span>.log(message.includes(<span class="hljs-string">'bar'</span>));<span class="hljs-comment">//true</span>
<span class="hljs-built_in">console</span>.log(message.includes(<span class="hljs-string">'bar'</span>,<span class="hljs-number">4</span>))<span class="hljs-comment">//false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>endsWith()方法接收第二个参数，表示应该当作字符串末尾的位置。如果不提供这个参数，那么默认就是字符串的长度。如果提供这个参数，那么就好像字符串只有那么多字符一样：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> message = <span class="hljs-string">'foobarbaz'</span>;
<span class="hljs-built_in">console</span>.log(message.endsWith(<span class="hljs-string">'bar'</span>));<span class="hljs-comment">//false</span>
<span class="hljs-built_in">console</span>.log(message.endsWith(<span class="hljs-string">'bar'</span>,<span class="hljs-number">6</span>));<span class="hljs-comment">//true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-9">trim()方法</h2>
<p>这个方法会创建字符串的一个副本，删除前后所有的空格，在返回结果。</p>
<p>另外，trimLeft()和trimRight()方法分别用于从字符串开始和末尾清理空格符</p>
<h2 data-id="heading-10">repeat()方法</h2>
<p>这个方法接收一个整数参数，表示要将字符串复制多少次，然后返回拼接所有副本后的结果。</p>
<h2 data-id="heading-11">padStart()和padEnd()方法</h2>
<p>1.该连个方法会复制字符串，如果原字符串小于指定长度，则在相应一边填充字符，直至满足长度条件；</p>
<p>2.这连个方法的第一个参数是长度，第二个参数是可选的填充字符串，默认为空格</p>
<p>3.可选的第二个参数并不限于一个字符，如果提供了多个字符的字符串，则会将提供的字符串拼接并截断以匹配指定的长度。</p>
<p>4.此外，如果长度小于或等于原字符串长度，则会返回原始字符串</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> strigValue = <span class="hljs-string">'foo'</span>
<span class="hljs-built_in">console</span>.log(stringValue.padStart(<span class="hljs-number">6</span>));<span class="hljs-comment">//'   foo'//foo前有三个空格</span>
<span class="hljs-built_in">console</span>.log(stringValue.padStart(<span class="hljs-number">9</span>,<span class="hljs-string">'.'</span>));<span class="hljs-comment">//'......foo'</span>
<span class="hljs-built_in">console</span>.log(stringValue.padEnd(<span class="hljs-number">6</span>));<span class="hljs-comment">//'foo   '//foo后有三个空格</span>
<span class="hljs-built_in">console</span>.log(stringValue.padEnd(<span class="hljs-number">9</span>,<span class="hljs-string">'.'</span>));<span class="hljs-comment">//'foo......'</span>

<span class="hljs-built_in">console</span>.log(stringValue.padStart(<span class="hljs-number">8</span>,<span class="hljs-string">'bar'</span>));<span class="hljs-comment">//'barbafoo'</span>
<span class="hljs-built_in">console</span>.log(stringValue.padStart(<span class="hljs-number">2</span>));<span class="hljs-comment">//'foo'</span>
<span class="hljs-built_in">console</span>.log(stringValue.padEnd(<span class="hljs-number">8</span>,<span class="hljs-string">'bar'</span>));<span class="hljs-comment">//'foobarba'</span>
<span class="hljs-built_in">console</span>.log(stringValue.padEnd(<span class="hljs-number">2</span>));<span class="hljs-comment">//'foo'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">join()方法</h2>
<p><code>join()</code>方法接收一个参数，即字符串分隔符，返回包含所有项的字符串。来看下面的例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> colors = [<span class="hljs-string">'red'</span>,<span class="hljs-string">'blue'</span>,<span class="hljs-string">'green'</span>]
<span class="hljs-built_in">console</span>.log(colors.join(<span class="hljs-string">","</span>));<span class="hljs-comment">//red,blue,green</span>
<span class="hljs-built_in">console</span>.log(colors.join(<span class="hljs-string">"||"</span>));<span class="hljs-comment">//red||blue||green</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">replace(）方法</h2>
<p>这个方法接收两个参数：</p>
<p>1.第一个参数可以是一个RegExp对象或一个字符串，</p>
<p>2.第二个参数可以是一个字符串或一个函数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> text = <span class="hljs-string">'cat,bat,sat,fat'</span>;
<span class="hljs-keyword">let</span> result = text.replace(<span class="hljs-string">'at'</span>,<span class="hljs-string">'ond'</span>);
<span class="hljs-built_in">console</span>.log(result);<span class="hljs-comment">//'cond,bat,sat,fat'</span>
<span class="hljs-keyword">let</span> result2 = text.repace(<span class="hljs-regexp">/at/g</span>,<span class="hljs-string">'ong'</span>);
<span class="hljs-built_in">console</span>.log(result2);<span class="hljs-comment">//'cond,bond,sond,fond'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>replace()的第二个参数可以是一个函数。在只有一个匹配项时，这个函数会收到三个参数：</p>
<ul>
<li>
<p>与整个模式匹配的字符串</p>
</li>
<li>
<p>匹配项在字符串中的开始位置</p>
</li>
<li>
<p>整个字符串</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">htmlEscape</span>(<span class="hljs-params">text</span>)</span>&#123;
<span class="hljs-keyword">return</span> text.replace(<span class="hljs-regexp">/[<>"&]/g</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">match,pos,originalText</span>)</span>&#123;
<span class="hljs-comment">//console.log(march)//< " " > < ></span>
        <span class="hljs-keyword">switch</span>(match)&#123;
<span class="hljs-keyword">case</span> <span class="hljs-string">'<'</span>:<span class="hljs-keyword">return</span> <span class="hljs-string">'<'</span>;
<span class="hljs-keyword">case</span> <span class="hljs-string">'>'</span>:<span class="hljs-keyword">return</span> <span class="hljs-string">'>'</span>;
<span class="hljs-keyword">case</span> <span class="hljs-string">'&'</span>:<span class="hljs-keyword">return</span> <span class="hljs-string">'&amp;'</span>;
<span class="hljs-keyword">case</span> <span class="hljs-string">'\"'</span>:<span class="hljs-keyword">return</span> <span class="hljs-string">'&quot;'</span>;
&#125;
&#125;)
&#125;
<span class="hljs-built_in">console</span>.log(htmlEscape(<span class="hljs-string">'<p class=\"greeting\">hello world</p>'</span>));
<span class="hljs-comment">//<p class=&quot;greeting&quot;>hello world</p></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">localeCompare()方法</h2>
<p>这个方法比较两个字符串，返回如下3个值得一个：</p>
<ul>
<li>
<p>如果按照字母表顺序，原字符串应排在参数字符串前头，则返回负值 -1</p>
</li>
<li>
<p>如果两个比较得字符串相等，则返回0</p>
</li>
<li>
<p>如果按照字母表顺序，原字符串应排在参数字符串后头，则返回正值 1</p>
</li>
<li>
<p>如果第一个字母相等则比较下一个，一直到字符串末尾</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> sv = <span class="hljs-string">'yellow'</span>;
<span class="hljs-built_in">console</span>.log(sv.localeCompare(<span class="hljs-string">'brick'</span>));<span class="hljs-comment">//1</span>
<span class="hljs-built_in">console</span>.log(sv.localcompare(<span class="hljs-string">'yellow'</span>));<span class="hljs-comment">//0</span>
<span class="hljs-built_in">console</span>.log(sv.localcompare(<span class="hljs-string">'yao'</span>));<span class="hljs-comment">//1</span>
<span class="hljs-built_in">console</span>.log(sv.localcompare(<span class="hljs-string">'yfo'</span>));<span class="hljs-comment">//-1</span>
<span class="hljs-built_in">console</span>.log(sv.localcompare(<span class="hljs-string">'zoo'</span>));<span class="hljs-comment">//-1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-15">URL编码方法</h2>
<p><code>encodeURI()</code>和<code>encodeURIComponent()</code>方法用于编码统一资源标识符：</p>
<p><code>encodeURI()</code>方法用于对整个URI进行编码；</p>
<p><code>encodeURIComponent()</code>方法用于编码URI中单独得组件；</p>
<p>这连个方法得主要区别是：</p>
<p><code>encodeURI()</code>不会编码属于URI组件得特殊字符，比如冒号，斜杠，问号，井号。</p>
<p><code>encodeURIConponent()</code>会编码他发现的所有非标准字符。</p>
<p><code>decodeURI()</code>和<code>decodeURIComponent()</code>与上述两个方法相对，</p>
<p><code>decodeURI()</code>只对使用<code>encodeURI()</code>编码过的字符解码</p>
<p><code>decodeURIComponent()</code>解码所有被<code>encodeURIComponent()</code>编码的字符，基本上就是解码所有特殊值。</p>
<h1 data-id="heading-16">Math</h1>
<p>ECMAScript提供了Math对象作为保存数学公式，信息和计算的地方。</p>
<p>Math对象提供了一些辅助计算的属性和方法。</p>
<h2 data-id="heading-17">min()和max()方法</h2>
<p>min()和max()方法用与确定一组数值中的最小值和最大值。可接收任意多个参数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> max = <span class="hljs-built_in">Math</span>.max(<span class="hljs-number">3</span>,<span class="hljs-number">54</span>,<span class="hljs-number">32</span>,<span class="hljs-number">16</span>);
<span class="hljs-built_in">console</span>.log(max);<span class="hljs-comment">//54</span>
<span class="hljs-keyword">let</span> min = <span class="hljs-built_in">Math</span>.min(<span class="hljs-number">3</span>,<span class="hljs-number">54</span>,<span class="hljs-number">32</span>,<span class="hljs-number">16</span>);
<span class="hljs-built_in">console</span>.log(min);<span class="hljs-comment">//3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">舍入方法</h2>
<ul>
<li><code>Math.ceil()</code>方法始终向上舍入为最接近的整数。</li>
<li><code>Math.floor()</code>方法始终向下舍入最接近的整数。</li>
<li><code>Math.round()</code>方法执行四舍五入</li>
<li><code>Math.fround()</code>方法返回数值最接近的单精度(32位)浮点值表示</li>
</ul>
<h2 data-id="heading-19">random()方法</h2>
<p>Math.random()方法返回一个0~1范围内的随机数，其中包含0但不包含1。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> num = <span class="hljs-built_in">Math</span>.floor(<span class="hljs-built_in">Math</span>.random()*<span class="hljs-number">10</span>+<span class="hljs-number">1</span>);<span class="hljs-comment">//1~10的值</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果是为了加密而需要生成随机数（传给生成器的输入需要较高的不确定性），那么建议使用window.crypto.getRandomValues()</p>
<h1 data-id="heading-20">Array</h1>
<p>1.<code>Array.from()</code>用于将类数组结构转换为数组实例：</p>
<ul>
<li>该方法的第一个参数是一个类数组对象，即任何可迭代的结构，或者有一个length属性和可索引元素的结构。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//字符串会被拆分为但字符数组</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Array</span>.from(<span class="hljs-string">'matt'</span>));<span class="hljs-comment">//['m','a','t','t']</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Array</span>.from(<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>));<span class="hljs-comment">//[1,2,3,4]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>第二个可选的映射函数参数。这个函数可以直接增强新数组的值。</li>
<li>第三个可选参数，用于指定映射函数中this的值。但这个重写的this值在箭头函数中不适用</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> a1 = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>];
<span class="hljs-keyword">const</span> a2 = <span class="hljs-built_in">Array</span>.from(a1,<span class="hljs-function"><span class="hljs-params">x</span>=></span>x**<span class="hljs-number">2</span>);
<span class="hljs-keyword">const</span> a3 = <span class="hljs-built_in">Array</span>.from(a1,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">x</span>)</span>&#123;
    <span class="hljs-keyword">return</span> x**<span class="hljs-built_in">this</span>.exponent
&#125;,&#123;<span class="hljs-attr">exponent</span>:<span class="hljs-number">2</span>&#125;)
<span class="hljs-built_in">console</span>.log(a2);<span class="hljs-comment">//[1,4,9,16]</span>
<span class="hljs-built_in">console</span>.log(a3);<span class="hljs-comment">//[1,4,9,16]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.<code>Array.of()</code>用于将一组参数转换为数组实例</p>
<p>​该方法可以把一组参数转换为数组，这个方法用于替代在ES6之前常用的Array.prototype.slice.call(arguments),一种异常笨拙的将arguments对象转换为数组的写法：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Array</span>.of(<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>));<span class="hljs-comment">//[1,2,3,4]</span>
<span class="hljs-comment">//和Array()做对比</span>
<span class="hljs-built_in">Array</span>.of(<span class="hljs-number">1</span>);<span class="hljs-comment">//[1]</span>
<span class="hljs-built_in">Array</span>(<span class="hljs-number">1</span>);<span class="hljs-comment">//表示创建了长度为1的空数组</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Array</span>.of(<span class="hljs-literal">undefined</span>));<span class="hljs-comment">//[undefined]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.<code>Array.isArray()</code>方法用于判断一个值是否是数组</p>
<h2 data-id="heading-21">迭代器方法</h2>
<ul>
<li>
<p>keys()返回数组索引的迭代器</p>
</li>
<li>
<p>values()返回数组元素的迭代器</p>
</li>
<li>
<p>entries()返回索引/值对的迭代器</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> a = [<span class="hljs-string">'foo'</span>,<span class="hljs-string">'bar'</span>,<span class="hljs-string">'baz'</span>,<span class="hljs-string">'qux'</span>]
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Array</span>.from(a.keys()))<span class="hljs-comment">//[ 0, 1, 2, 3 ]</span>
<span class="hljs-built_in">console</span>.log(a.values())<span class="hljs-comment">//Object [Array Iterator] &#123;&#125;</span>

<span class="hljs-comment">//Object [Array Iterator] &#123;&#125;</span>
<span class="hljs-comment">//[[ 0, 'foo' ],[ 1, 'bar' ],[ 2, 'baz' ],[ 3, 'qux' ]]</span>
<span class="hljs-built_in">console</span>.log(a.entries())
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> item <span class="hljs-keyword">of</span> a.entries())&#123;
<span class="hljs-built_in">console</span>.log(item)<span class="hljs-comment">//[ 0, 'foo' ],[ 1, 'bar' ],[ 2, 'baz' ],[ 3, 'qux' ]</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-22">复制和填充方法</h2>
<p><code>copyWithin()</code>批量复制方法，<code>fill()</code>填充数组方法</p>
<p>这两个方法的函数签名类似，都需要指定既有数组实例上的一个范围，包含开始索引，不包含结束索引。使用这个方法不会改变数组的大小。</p>
<h3 data-id="heading-23">fill()方法</h3>
<p><code>fill()</code>方法可以向一个已有的数组中插入全部或部分相同的值。</p>
<ul>
<li>
<p>开始索引用于指定开始填充的位置，它是可选的。</p>
</li>
<li>
<p>如果不提供结束索引，则一直填充到数组末尾。</p>
</li>
<li>
<p>负值索引从数组末尾开始计算。也可以将负索引想象成数组长度加上它得到的一个正索引：</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> zeroes = [<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>,<span class="hljs-number">0</span>];
<span class="hljs-comment">//用五填充整个数组</span>
zeroes.fill(<span class="hljs-number">5</span>);
<span class="hljs-built_in">console</span>.log(zeroes);<span class="hljs-comment">//[5,5,5,5,5]</span>
zeroes.fill(<span class="hljs-number">0</span>)<span class="hljs-comment">//重置</span>
<span class="hljs-comment">//用6填充索引大于等于3的元素</span>
zeroes.fill(<span class="hljs-number">6</span>,<span class="hljs-number">3</span>)
<span class="hljs-built_in">console</span>.log(zeroes)<span class="hljs-comment">//[0,0,0,6,6]</span>
zeroes.fill(<span class="hljs-number">0</span>)<span class="hljs-comment">//重置</span>
zeroes.fill(<span class="hljs-number">7</span>,<span class="hljs-number">1</span>,<span class="hljs-number">3</span>)<span class="hljs-comment">//用7填充大于等于1且小于3的元素</span>
<span class="hljs-built_in">console</span>.log(zeroes)<span class="hljs-comment">//0,7,7,0,0]</span>
zeroes.fill(<span class="hljs-number">0</span>)<span class="hljs-comment">//重置</span>
<span class="hljs-comment">//用8填充大于等于1且小于4的元素</span>
zeroes.fill(<span class="hljs-number">8</span>,-<span class="hljs-number">4</span>,-<span class="hljs-number">1</span>);
<span class="hljs-built_in">console</span>.log(zeroes);<span class="hljs-comment">//[0,8,8,8,0]</span>
zeroes.fill(<span class="hljs-number">4</span>,<span class="hljs-number">3</span>,<span class="hljs-number">10</span>)
<span class="hljs-built_in">console</span>.log(zeroes);<span class="hljs-comment">//[0,0,0,4,4]</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24">copyWithin()方法</h3>
<p><code>copyWithin()</code>会按照指定范围浅复制数组中的部分内容，然后将它们插入到指定索引开始的位置。</p>
<p>开始索引和结束索引则与fill()使用同样的计算方法：</p>
<pre><code class="hljs language-js copyable" lang="js">ints = [<span class="hljs-number">0</span>,<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>,<span class="hljs-number">7</span>,<span class="hljs-number">8</span>,<span class="hljs-number">9</span>]
ints.copyWithin(<span class="hljs-number">5</span>);
<span class="hljs-built_in">console</span>.log(ints);<span class="hljs-comment">//[0,1,2,3,4,0,1,2,3,4]</span>
ints.copyWithin(<span class="hljs-number">0</span>,<span class="hljs-number">5</span>);
<span class="hljs-built_in">console</span>.log(ints);<span class="hljs-comment">//[5,6,7,8,9,5,6,7,8,9]</span>
ints.copyWithin(<span class="hljs-number">4</span>,<span class="hljs-number">0</span>,<span class="hljs-number">3</span>);
<span class="hljs-built_in">console</span>.log(ints);<span class="hljs-comment">//[0,1,2,3,0,1,2,7,8,9]</span>
ints.copyWithin(-<span class="hljs-number">4</span>,-<span class="hljs-number">7</span>,-<span class="hljs-number">3</span>);
console0.log(ints);<span class="hljs-comment">//[0,1,2,3,4,5,3,4,5,6]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-25">栈方法</h2>
<h3 data-id="heading-26">push()方法和pop()方法</h3>
<p><code>push()</code>方法接收任意数量的参数，并将它们添加到数组末尾，返回数组的最新长度。</p>
<p><code>pop()</code>方法则用于删除数组的最后一项，同时减少数组的length值，返回被删除的项。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> colors = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Array</span>();
<span class="hljs-keyword">let</span> count = colors.push(<span class="hljs-string">'red'</span>,<span class="hljs-string">'green'</span>);
<span class="hljs-built_in">console</span>.log(count)<span class="hljs-comment">//2</span>
count = colors.push(<span class="hljs-string">'black'</span>);
<span class="hljs-built_in">console</span>.log(count)<span class="hljs-comment">//1</span>
<span class="hljs-keyword">let</span> item = colors.pop();
<span class="hljs-built_in">console</span>.log(item)<span class="hljs-comment">//black</span>
<span class="hljs-comment">//通过下表添加</span>
colors[<span class="hljs-number">3</span>] = <span class="hljs-string">'black'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-27">队列方法</h2>
<h3 data-id="heading-28">shift()方法和unshift()方法</h3>
<p><code>shift()</code>方法，它会删除数组的第一项并返回它，然后数组长度减一</p>
<p><code>unshift()</code>就是执行跟<code>shift()</code>相反的操作：在数组开头添加任意多个值，然后返回新的数组长度。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> colors = [<span class="hljs-string">'red'</span>,<span class="hljs-string">'blue'</span>,<span class="hljs-string">'green'</span>]
<span class="hljs-keyword">let</span> item = colors.shift();
<span class="hljs-built_in">console</span>.log(item)<span class="hljs-comment">//red</span>
<span class="hljs-built_in">console</span>.log(colors);<span class="hljs-comment">//['blue','green']</span>
<span class="hljs-keyword">let</span> count = colors.unshift(<span class="hljs-string">'black'</span>);
<span class="hljs-built_in">console</span>.log(count);<span class="hljs-comment">//1</span>
<span class="hljs-built_in">console</span>.log(colors);<span class="hljs-comment">//['black','blue','green']</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-29">排序方法</h2>
<h3 data-id="heading-30">reverse()方法</h3>
<p><code>reverse()</code>方法就是将数组元素反向排序</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> values = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>]
values.reverse();
<span class="hljs-built_in">console</span>.log(values);<span class="hljs-comment">//5,4,3,2,1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-31">sort()方法</h3>
<ul>
<li>
<p><code>sort()</code>会按照升序重新排列数组元素，即最小的值在前面，最大的值在后面</p>
</li>
<li>
<p>为此，<code>sort()</code>会在每一项上调用<code>String()</code>转型函数，然后比较字符串来决定顺序。</p>
</li>
<li>
<p>即使数组的元素都是数值，也会先把数组转换为字符串再比较、排序。</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> values = [<span class="hljs-number">0</span>,<span class="hljs-number">1</span>,<span class="hljs-number">5</span>,<span class="hljs-number">10</span>,<span class="hljs-number">15</span>]
values.sort();
<span class="hljs-built_in">console</span>.log(values);<span class="hljs-comment">//0,1,10,15,5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了更好的解决排序问题，<code>sort()</code>方法可以接收一个__比较函数__。</p>
<p>比较函数接收两个参数：</p>
<ul>
<li>如果第一个参数应该排在第二个参数前面，就返回负值；</li>
<li>如果两个参数相等，就返回0；</li>
<li>如果第一个参数应该排在第二个参数后面，就返回正值。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//升序，把返回值改下就能实现升序</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">compare</span>(<span class="hljs-params">value1,value2</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(value1 < value2)&#123;
        <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>
    &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(value1 > value2)&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>;
    &#125;<span class="hljs-keyword">else</span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-number">0</span>
    &#125;
&#125;
<span class="hljs-keyword">let</span> values = [<span class="hljs-number">0</span>,<span class="hljs-number">1</span>,<span class="hljs-number">5</span>,<span class="hljs-number">10</span>,<span class="hljs-number">15</span>]
values.sort(compare);
<span class="hljs-built_in">console</span>.log(values);<span class="hljs-comment">//0,1,5,10,15</span>
#OR
values.sort(<span class="hljs-function">(<span class="hljs-params">a,b</span>) =></span> a < b ? <span class="hljs-number">1</span> : a > b ? -<span class="hljs-number">1</span> : <span class="hljs-number">0</span>)
<span class="hljs-built_in">console</span>.log(values):<span class="hljs-comment">//15,10,5,1,0</span>
#OR
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">compare</span>(<span class="hljs-params">value1,value2</span>)</span>&#123;
    <span class="hljs-comment">//升序</span>
    <span class="hljs-keyword">return</span> value1 - value2
    <span class="hljs-comment">//降序</span>
   <span class="hljs-comment">// return value2 - value1</span>
&#125;
<span class="hljs-keyword">let</span> values = [<span class="hljs-number">0</span>,<span class="hljs-number">1</span>,<span class="hljs-number">5</span>,<span class="hljs-number">10</span>,<span class="hljs-number">15</span>]
<span class="hljs-built_in">console</span>.log(values.sort(compare))<span class="hljs-comment">//[0,1,5,10,15]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-32">Object</h1>
<h2 data-id="heading-33">Object.assign()合并对象</h2>
<p>这个方法接收一个目标对象和一个或多个源对象作为参数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> dest,src,result1;
dest = &#123;&#125;
src = &#123;<span class="hljs-attr">id</span>:<span class="hljs-string">'src'</span>&#125;
result1 = <span class="hljs-built_in">Object</span>.assign(dest,src)
dest.aaa = <span class="hljs-string">'bbb'</span>
result1.bbb = <span class="hljs-string">'aaa'</span>
<span class="hljs-built_in">console</span>.log(dest,result1)
<span class="hljs-comment">//&#123; id: 'src', aaa: 'bbb', bbb: 'aaa' &#125; &#123; id: 'src', aaa: 'bbb', bbb: 'aaa' &#125;</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面代码可知：</p>
<ul>
<li>Object.assign()实际上对每个源对象执行的是浅复制。</li>
</ul>
<h2 data-id="heading-34">Object.is()</h2>
<p>有些特殊情况即使是===操作符也无能为力</p>
<p>这个方法与===很像，必须接收两个参数：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.is(<span class="hljs-literal">true</span>,<span class="hljs-number">1</span>))<span class="hljs-comment">//false</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.is(&#123;&#125;,&#123;&#125;))<span class="hljs-comment">//false</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.is(+<span class="hljs-number">0</span>,-<span class="hljs-number">0</span>))<span class="hljs-comment">//false</span>
<span class="hljs-built_in">console</span>.log(+<span class="hljs-number">0</span> === -<span class="hljs-number">0</span>)<span class="hljs-comment">//true</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.is(<span class="hljs-literal">NaN</span>,<span class="hljs-literal">NaN</span>))<span class="hljs-comment">//true</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-literal">NaN</span> === <span class="hljs-literal">NaN</span>)<span class="hljs-comment">//false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-35">结构赋值</h2>
<h3 data-id="heading-36">对象的解构</h3>
<p>可以在一条语句中使用嵌套数据实现一个或多个赋值操作。</p>
<p>简单地说，对象解构就是使用与对象匹配的结构来实现对象属性赋值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> person = &#123;
    <span class="hljs-attr">name</span>:<span class="hljs-string">'matt'</span>,
    <span class="hljs-attr">age</span>:<span class="hljs-number">19</span>
&#125;
<span class="hljs-keyword">let</span> &#123;<span class="hljs-attr">name</span>:personName,<span class="hljs-attr">age</span>:personAge&#125; = person;
<span class="hljs-built_in">console</span>.log(personName);<span class="hljs-comment">//matt</span>
<span class="hljs-built_in">console</span>.log(personAge);<span class="hljs-comment">//19</span>
#OR
<span class="hljs-keyword">let</span> &#123;name,age&#125; = person;
<span class="hljs-built_in">console</span>.log(name);<span class="hljs-comment">//matt</span>
<span class="hljs-built_in">console</span>.log(age);<span class="hljs-comment">//19</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解构赋值不一定与对象的属性匹配。赋值的时候可以忽略某些属性，而如果引用的属性不存在，则该变量的值就是undefined：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> person = &#123;
    <span class="hljs-attr">name</span>:<span class="hljs-string">'matt'</span>,
    <span class="hljs-attr">age</span>:<span class="hljs-number">19</span>
&#125;
<span class="hljs-keyword">let</span> &#123;name,job&#125; = person;
<span class="hljs-built_in">console</span>.log(name);<span class="hljs-comment">//matt</span>
<span class="hljs-built_in">console</span>.log(job);<span class="hljs-comment">//undefined</span>
#OR
<span class="hljs-keyword">let</span> &#123;name,job = <span class="hljs-string">'aaa'</span>&#125; = person
<span class="hljs-built_in">console</span>.log(name);<span class="hljs-comment">//matt</span>
<span class="hljs-built_in">console</span>.log(job);<span class="hljs-comment">//aaa</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>解构在内部使用函数ToObject()（不能在运行时环境中直接访问）把源数据结构转换为对象</p>
<p>这也意味着（根据ToObject()的定义）, null和undefined不能被解构，否则会抛出错误。</p>
<p>解构并不要求变量必须在解构表达式中声明。</p>
<p>不过，如果是给事先声明的变量赋值，则赋值表达式必须包含在一对__括号__中：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> personName,personAge;
<span class="hljs-keyword">let</span> person = &#123;
<span class="hljs-attr">name</span>:<span class="hljs-string">'matt'</span>,
<span class="hljs-attr">age</span>:<span class="hljs-number">19</span>
&#125;;
(&#123;<span class="hljs-attr">name</span>:personName,<span class="hljs-attr">age</span>:personAge&#125; = person)<span class="hljs-comment">//必须用括号包裹</span>
<span class="hljs-built_in">console</span>.log(personName,personAge)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-37">嵌套解构</h3></div>  
</div>
            