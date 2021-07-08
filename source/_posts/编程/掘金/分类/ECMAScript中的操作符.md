
---
title: 'ECMAScript中的操作符'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4826'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 22:24:46 GMT
thumbnail: 'https://picsum.photos/400/300?random=4826'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;overflow:hidden;line-height:1.75;font-size:15px;background-image:linear-gradient(90deg,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0),linear-gradient(1turn,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0);background-size:20px 20px;background-position:50%;padding-top:0!important&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;position:relative;display:flex;border-bottom:5px solid #6d4e00;line-height:35px;letter-spacing:1px;font-size:25px;padding-left:25px;color:#664900;text-shadow:1px 1px 1px #8a6200;padding-bottom:0&#125;.markdown-body h1:before&#123;content:"";display:flex;position:absolute;left:0;top:3px;bottom:0;margin:auto;width:20px;height:20px;background-size:20px 20px;background-image:url("data:image/png;base64,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")&#125;.markdown-body h2&#123;position:relative;padding:0 0 0 20px;font-size:20px;font-weight:700;color:#614500&#125;.markdown-body h2:before&#123;content:"";position:absolute;top:3px;bottom:0;left:0;background-image:url("data:image/png;base64,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");background-size:100% 100%;background-repeat:no-repeat;width:15px;height:15px;margin:auto&#125;.markdown-body h3&#123;width:100%;text-align:left;margin:20px 10px 0 0;font-size:18px;font-weight:700;display:inline-block;padding-left:10px;padding-bottom:0;border-left:5px solid #8f6600;color:#614500&#125;.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-weight:700;color:#a37400&#125;.markdown-body h4&#123;font-size:17px&#125;.markdown-body h5,.markdown-body h6&#123;display:flex;align-items:center&#125;.markdown-body h5:after,.markdown-body h6:after&#123;display:inline-block;border:2px solid #fff6e0;color:rgba(189,134,0,.5);border-radius:50%;text-align:center;margin-left:5px&#125;.markdown-body h5&#123;font-size:14px&#125;.markdown-body h5:after&#123;content:"5";width:15px;height:15px;line-height:15px;font-size:13px&#125;.markdown-body h6&#123;font-size:12px&#125;.markdown-body h6:after&#123;content:"6";width:13px;height:13px;line-height:13px;font-size:12px&#125;.markdown-body p&#123;color:#412c0c;letter-spacing:1px;font-weight:400&#125;.markdown-body img&#123;max-width:100%;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#755300;font-weight:400;border-bottom:1px solid #755300;font-weight:bolder;text-decoration:none&#125;.markdown-body table&#123;width:100%!important;margin:0;font-size:12px;width:auto;max-width:100%;overflow:auto;border-collapse:collapse;border-spacing:0&#125;.markdown-body table img&#123;box-shadow:none&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body thead tr th&#123;text-align:center&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px;box-sizing:border-box;border:1px solid rgba(72,42,10,.1)&#125;.markdown-body blockquote&#123;position:relative;text-size-adjust:100%;line-height:25px;font-weight:400;border-radius:10px;font-style:normal;text-align:left;box-sizing:inherit;border:1px solid #ffd87a;background-color:rgba(189,134,0,.5);margin:20px 0;padding:20px&#125;.markdown-body blockquote p&#123;color:#fff6e0;letter-spacing:2px;margin:0&#125;.markdown-body blockquote:after,.markdown-body blockquote:before&#123;position:absolute;color:#cc9100;font-size:34px;font-weight:700&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:5px&#125;.markdown-body blockquote:after&#123;content:"❞";right:5px;bottom:-5px&#125;.markdown-body strong&#123;color:#c28a00;font-weight:bolder&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;color:#c28a00&#125;.markdown-body em strong&#123;font-style:normal;color:#c28a00;background-color:#8a6200&#125;.markdown-body s&#123;color:#c28a00&#125;.markdown-body hr&#123;border-top:1px solid #805b00&#125;.markdown-body code,.markdown-body li code,.markdown-body p code&#123;color:#996d00;background-color:rgba(130,98,0,.3)&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit;color:#858585;font-family:bold;letter-spacing:1px&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection,.markdown-body img::selection&#123;color:rgba(189,134,0,.5);background-color:#fff&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body pre>code::selection&#123;background-color:rgba(189,134,0,.5)&#125;.markdown-body .math .math-inline::selection,.markdown-body blockquote::selection,.markdown-body ol::selection,.markdown-body p::selection,.markdown-body strong::selection,.markdown-body table::selection,.markdown-body ul::selection&#123;background-color:rgba(189,134,0,.5)&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一元操作符</h2>
<p>只能操作一个值的操作符叫做<strong>一元操作符</strong></p>
<ol>
<li>
<p>递增和递减。递增和递减操作符借鉴自C，而且有两个版本：前置型和后置型</p>
<ol>
<li>
<p>前置型：操作符位于要操作的变量之前。执行前置型递增和递减操作时，变量的值都是在语句被求值以前改变的</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> age = <span class="hljs-number">29</span>;
<span class="hljs-keyword">var</span> anotherAge = --age + <span class="hljs-number">2</span>
<span class="hljs-built_in">console</span>.log(age) <span class="hljs-comment">// 28</span>
<span class="hljs-built_in">console</span>.log(anotherAge) <span class="hljs-comment">// 30</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>后置型：操作符位于要操作的变量之后。后置型递增和递减操作是在包含它们的语句被求值之后才执行的</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> num1 - <span class="hljs-number">2</span>;
<span class="hljs-keyword">var</span> num2 = <span class="hljs-number">20</span>
<span class="hljs-keyword">var</span> num3 = num1-- + num2; <span class="hljs-comment">// 22</span>
<span class="hljs-keyword">var</span> num4 = num1 + num2; <span class="hljs-comment">// 21</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>以上4个操作符对任何值都适用，即可以用于字符串、布尔值、浮点数值和对象。遵循下列规则：</p>
<ul>
<li>在应用于一个包含有效数字字符的字符串时，先将其转换为数字值，再执行加减1的操作。字符串变量变成数值变量</li>
<li>在应用于一个不包含有数字字符的字符串时，将变量的值设置为NaN。字符串变量变成数值变量</li>
<li>在应用于布尔值false时，先将其转换为0再执行加减1的操作。布尔值变量变成数值变量</li>
<li>在应用于布尔值true时，先将其转换为0再执行加减1的操作。布尔值变量变成数值变量</li>
<li>在应用于浮点数值时，执行加减1的操作</li>
<li>在应用于对象时，先调用对象的valueOf()方法以取得一个可供操作的值，然后对该值应用上述规则。如果是NaN，则调用toString()方法后再应用上述规则。对象变量变成数值变量</li>
</ul>
<p>上述规则验证：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> s1 = <span class="hljs-string">"2"</span>;
<span class="hljs-keyword">var</span> s2 = <span class="hljs-string">"z"</span>;
<span class="hljs-keyword">var</span> b = <span class="hljs-literal">false</span>;
<span class="hljs-keyword">var</span> f = <span class="hljs-number">1.1</span>;
<span class="hljs-keyword">var</span> o = &#123;
    <span class="hljs-attr">valueOf</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>
    &#125;
&#125;
<span class="hljs-built_in">console</span>.log(s1++); <span class="hljs-comment">// 2</span>
<span class="hljs-built_in">console</span>.log(s1); <span class="hljs-comment">// 3</span>
<span class="hljs-built_in">console</span>.log(s2++); <span class="hljs-comment">// NaN</span>
<span class="hljs-built_in">console</span>.log(s2); <span class="hljs-comment">// NaN</span>
<span class="hljs-built_in">console</span>.log(b++); <span class="hljs-comment">// 0</span>
<span class="hljs-built_in">console</span>.log(b); <span class="hljs-comment">// 1</span>
<span class="hljs-built_in">console</span>.log(f--); <span class="hljs-comment">// 1.1</span>
<span class="hljs-built_in">console</span>.log(f); <span class="hljs-comment">// 0.1000000000000009</span>
<span class="hljs-built_in">console</span>.log(o--); <span class="hljs-comment">// -1</span>
<span class="hljs-built_in">console</span>.log(o); <span class="hljs-comment">// -2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>一元加和减操作符</p>
<p>一元加和减操作符主要用于基本的算术运算，也可以用于转换数据类型，即在对非数值应用一元操作符时，该操作符会像Number()转型函数一样对这个值执行转换。布尔值false和true将被转换为0和1，字符串值会被按照一组特殊的规则进行解析，对象是先调用它们的valueOf()或toString()方法，再转换得到的值。以一元加操作符为例：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> s1 = <span class="hljs-string">"01"</span>;
<span class="hljs-keyword">var</span> s2 = <span class="hljs-string">"1.1"</span>;
<span class="hljs-keyword">var</span> s3 = <span class="hljs-string">"z"</span>;
<span class="hljs-keyword">var</span> b = <span class="hljs-literal">false</span>;
<span class="hljs-keyword">var</span> f = <span class="hljs-number">1.1</span>;
<span class="hljs-keyword">var</span> o = &#123;
    <span class="hljs-attr">valueOf</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>
    &#125;
&#125;
s1 = +s1
s2 = +s2
s3 = +s3
b = +b
f = +f
o = +o
<span class="hljs-built_in">console</span>.log(s1) <span class="hljs-comment">// 1</span>
<span class="hljs-built_in">console</span>.log(s2) <span class="hljs-comment">// 1.1</span>
<span class="hljs-built_in">console</span>.log(s3) <span class="hljs-comment">// NaN</span>
<span class="hljs-built_in">console</span>.log(b) <span class="hljs-comment">// 0</span>
<span class="hljs-built_in">console</span>.log(f) <span class="hljs-comment">// 1.1</span>
<span class="hljs-built_in">console</span>.log(o) <span class="hljs-comment">// -1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<h2 data-id="heading-1">布尔操作符</h2>
<p>布尔操作符一共有3个：非（NOT）、与（AND）和或（OR）</p>
<ol>
<li>
<p>逻辑非。由一个英文叹号(!)表示，可以用于ECMAScript中的任何值。无论操作数是个什么数据类型，这个操作符都会返回一个布尔值。逻辑非操作符首先会将它的操作数转换为一个布尔值，然后对其求反。遵循一下规则</p>
<ul>
<li>如果操作数是一个对象，返回false</li>
<li>如果操作数是一个空字符串，返回true</li>
<li>如果操作数是一个非空字符串，返回false</li>
<li>如果操作数是数值0，返回true</li>
<li>如果操作数是任意非0数值（包括Infinity)，返回false</li>
<li>如果操作数是null，返回true</li>
<li>如果操作数是NaN，返回true</li>
<li>如果操作数是undefined，返回true</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log(!<span class="hljs-literal">false</span>); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(!<span class="hljs-string">"blue"</span>); <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(!<span class="hljs-string">""</span>); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(!<span class="hljs-number">0</span>); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(!<span class="hljs-literal">undefined</span>); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(!<span class="hljs-literal">null</span>); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(!<span class="hljs-literal">NaN</span>); <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(!<span class="hljs-number">12345</span>); <span class="hljs-literal">false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>逻辑与。操作符由两个和号（&&）表示，有两个操作数。逻辑与操作可以应用与任何类型的操作数，而不仅仅是布尔值。在有一个操作数不是布尔值的情况下，逻辑与操作就不一定返回布尔值；此时，它遵循以下规则：</p>
<ul>
<li>如果第一个操作数是对象，则返回第二个操作数</li>
<li>如果第二个操作数是对象，则只有在第一个操作数的求值结果为true的情况下才会返回该对象</li>
<li>如果两个操作数都是对象，则返回第二个操作数</li>
<li>如果第一个操作数是null，则返回null</li>
<li>如果第一个操作数是NaN，则返回NaN</li>
<li>如果第一个操作数是undefined，则返回undefined</li>
</ul>
<p>逻辑与操作属于短路操作，即如果第一个操作数能够决定结果，那么就不会再对第二个操作数求值</p>
</li>
<li>
<p>逻辑或。操作符由两个竖线符号(||)表示，有两个操作数。与逻辑与操作相似，如果有一个操作数不是布尔值，逻辑或也不一定返回布尔值；此时，它遵循以下规则：</p>
<ul>
<li>如果第一个操作数是对象，则返回第一个操作数</li>
<li>如果第一个操作数的求值结果为false，则返回第二个操作数</li>
<li>如果两个操作数都是对象，则返回第一个操作数</li>
<li>如果两个操作数都是null，则返回null</li>
<li>如果两个操作数都是NaN，则返回NaN</li>
<li>如果两个操作数都是undefined，则返回undefined</li>
</ul>
<p>与逻辑与操作符相似，逻辑或操作符也是短路操作。也就是说，如果第一个操作数的求值结果为true，就不会对第二个操作数求值了</p>
</li>
</ol>
<h2 data-id="heading-2">乘性操作符</h2>
<p>ECMAScript定义了3个乘性操作符：乘法、除法和求模。如果参与乘性计算的某个操作数不是数值，后台会先使用Number()转型函数将其转换为数值，如：空字符串将被当作0，布尔值true将被当作1</p>
<ol>
<li>乘法。操作符由一个星号(*)表示，用于计算两个数值的乘积。在处理特殊值情况下，乘法操作符遵循下列特殊的规则：
<ul>
<li>如果操作数都是数值，执行常规的乘法计算，即两个正数或两个负数相乘的结果还是正数，而如果只有一个操作数有符号那么结果就是负数。如果乘积超过了ECMAScript数值的表示范围，则返回Infinity或-Infinity</li>
<li>如果有一个操作数是NaN，则结果是NaN</li>
<li>如果是Infinity与0相乘，则结果是NaN</li>
<li>如果是Infinity与非0数值相乘，则结果是Infinity或-Infinity，取决于有符号操作数的符号</li>
<li>如果是Infinity与Infinity相乘，则结果是Infinity</li>
<li>如果有一个操作数不是数值，则在后台调用Number()将其转换为数值，然后在应用上面的规则</li>
</ul>
</li>
<li>除法。操作符由一个斜线符号(/)表示，执行第二个操作数除第一个操作数的计算。遵循一下规则：
<ul>
<li>如果操作数都是数值，执行常规的除法计算，即两个正数或两个负数相除结果还是正数；如果只有一个操作数有符号，那么结果就是负数。如果超过了ECMAScript数值的表示范围，则返回Infinity或-Infinity</li>
<li>如果有一个操作数是NaN，则结果是NaN</li>
<li>如果是Infinity被Infinity除，则结果是NaN</li>
<li>如果是0被0除，则结果是NaN</li>
<li>如果是非零的有限数被零除，则结果是Infinity或-Infinity，取决于有符号操作数的符号</li>
<li>如果是Infinity被任何非零数值除，则结果是Infinity或-Infinity，取决于有符号操作数的符号</li>
<li>如果有一个操作数不是数值，则在后台调用Number()将其转换为数值，然后再应用上面的规则</li>
</ul>
</li>
<li>求模（余数）。操作符由一个百分号(%)表示。遵循以下规则：
<ul>
<li>如果操作数都是数值，执行常规的除法计算，返回除得的余数</li>
<li>如果被除数是无穷大值而除数是有限大的数值，则结果是NaN</li>
<li>如果被除数是有限大的数值而除数是零，则结果是NaN</li>
<li>如果是Infinity被Infinity除，则结果是NaN</li>
<li>如果被除数是有限大的数值而除数是无穷大的数值，则结果是被除数</li>
<li>如果被除数是零，则结果是零</li>
<li>如果有一个操作数不是数值，则在后台调用Number()将其转换为数值，然后在应用上面规则</li>
</ul>
</li>
</ol>
<h2 data-id="heading-3">加性操作符</h2>
<p>与乘性操作符类似，加性操作符也会在后台转换不同的数据类型。</p>
<ol>
<li>
<p>加法。加法操作符由加号（+）表示。如果两个操作数都是数值，执行常规的加法计算，然后根据下列规则返回结果：</p>
<ul>
<li>如果有一个操作数是NaN，则结果是NaN</li>
<li>如果是Infinity加Infinity，则结果是Infinity</li>
<li>如果是-Infinity加-Infinity，则结果是-Infinity</li>
<li>如果是Infinity加-Infinity，则结果是NaN</li>
<li>如果是+0加+0，则结果是+0</li>
<li>如果是-0加-0，则结果是-0</li>
<li>如果是+0加-0，则结果是0</li>
</ul>
<p>如果有一个操作数是字符串，那么就要应用如下规则：</p>
<ul>
<li>如果两个操作数都是字符串，则将第二个操作数与第一个操作数拼接起来</li>
<li>如果只有一个操作数是字符串，则将另一个操作数转换为字符串，然后再将两个字符串拼接起来</li>
<li>如果有一个操作数是对象、数值或布尔值，则调用它们的toString()方法取得相应的字符串值，然后再应用前面关于字符串的规则</li>
<li>如果是undefined和null，则分别调用String()函数并取得字符串"undefined"和"null"</li>
</ul>
</li>
<li>
<p>减法。减法操作符由减号（-）表示，与加法操作符类似，遵循以下规则：</p>
<ul>
<li>如果两个操作符都是数值，则执行常规的算术减法操作并返回结果</li>
<li>如果有一个操作数是NaN，则结果是NaN</li>
<li>如果是Infinity减Infinity，则结果是NaN</li>
<li>如果是-Infinity减-Infinity，则结果是NaN</li>
<li>如果是Infinity减-Infinity，则结果是Infinity</li>
<li>如果是-Infinity将Infinity，则结果是-Infinity</li>
<li>如果是+0减+0，则结果是+0</li>
<li>如果是-0减+0，则结果是-0</li>
<li>如果是-0减-0，则结果是+0</li>
<li>如果有一个操作数是字符串、布尔值、null或undefined，则现在后台调用Number()函数将其转换为数值，然后再根据前面的规则执行减法计算。如果转换结果是NaN，则减法的结果就是NaN</li>
<li>如果有一个操作数是对象，则调用对象的valueOf()方法以取得表示该对象的数值。如果得到的值是NaN，则减法结果就是NaN。如果对象没有valueOf()方法，则调用其toString()方法并将得到的字符串转换为数值</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> result1 = <span class="hljs-number">5</span> - <span class="hljs-literal">true</span>
<span class="hljs-keyword">var</span> result2 = <span class="hljs-literal">NaN</span> - <span class="hljs-number">1</span>
<span class="hljs-keyword">var</span> result3 = <span class="hljs-number">5</span> - <span class="hljs-number">3</span>
<span class="hljs-keyword">var</span> result4 = <span class="hljs-number">5</span> - <span class="hljs-string">""</span>
<span class="hljs-keyword">var</span> result5 = <span class="hljs-number">5</span> - <span class="hljs-string">"2"</span>
<span class="hljs-keyword">var</span> result6 = <span class="hljs-number">5</span> - <span class="hljs-literal">null</span>
<span class="hljs-built_in">console</span>.log(result1) <span class="hljs-comment">// 4, true被转换为1</span>
<span class="hljs-built_in">console</span>.log(result2) <span class="hljs-comment">// NaN</span>
<span class="hljs-built_in">console</span>.log(result3) <span class="hljs-comment">// 2</span>
<span class="hljs-built_in">console</span>.log(result4) <span class="hljs-comment">// 5, 空字符串被转换为0</span>
<span class="hljs-built_in">console</span>.log(result5) <span class="hljs-comment">// 3，字符串2被转换为数字2</span>
<span class="hljs-built_in">console</span>.log(result6) <span class="hljs-comment">// 5，因为null被转换为了0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<h2 data-id="heading-4">关系操作符</h2>
<p>关系操作符有小于（<）、大于（>）、小于等于（<=）和大于等于（>=）四个关系比较。当关系操作符的操作数使用了非数值时，也要进行数据转换或完成某些奇怪的操作。相应规则如下：</p>
<ul>
<li>如果两个操作数都是数值，则执行数值比较</li>
<li>如果两个操作数都是字符串，则比较两个字符串对应的字符编码值</li>
<li>如果一个操作数是数值，则将另一个操作数转换为一个数值，然后执行数值比较</li>
<li>如果一个操作数是对象，则调用这个对象的valueOf()方法，用得到的结果按照前面的的规则进行比较。如果对象没有valueOf()方法，则调用toString()方法，并用得到的结果根据前面的规则执行比较</li>
<li>如果一个操作数是布尔值，则先将其转换为数值，然后再执行比较</li>
</ul>
<p>在比较字符串时，实际比较的是两个字符串中对应位置的每个字符的字符编码值。经过这么一番比较之后，再返回一个布尔值。大写字母的字符编码小于小写字母的字符编码。</p>
<h2 data-id="heading-5">相等操作符</h2>
<p>两组操作符：<strong>相等和不相等</strong>——先转换再比较；<strong>全等和不全等</strong>——仅比较而不转换</p>
<ol>
<li>
<p>相等和不相等。相等操作符由两个等于号（==）表示，如果两个操作数相等，则返回true；不相等操作符由叹号后跟等于号（!=）表示，如果两个操作数不相等，则返回true。这两个操作符都会先转换操作数（通常称为<strong>强制转型</strong>），然后再比较它们的相等性。在转换不同数据类型时，遵循以下基本规则：</p>
<ul>
<li>如果一个操作数是布尔值，则在比较相等性之前先将其转换为数值——false转换为0，true转换为1</li>
<li>如果一个操作数是字符串，另一个操作数是数值，在比较相等性之前先将字符串转换为数值</li>
<li>如果一个操作数是对象，另一个操作数不是，则调用对象的valueOf()方法，用得到的基本类型值按照前面的规则进行比较</li>
</ul>
<p>这两个操作符在进行比较时要遵循下列规则</p>
<ul>
<li>null和undefined事相等的</li>
<li>比较相等性之前，不能将null和undefined转换成其他任何值</li>
<li>如果有一个操作数是NaN，则相等操作符返回false，而不相等操作符返回true。即使两个操作数都是NaN，则相等操作符也返回false；因为按照规则，NaN不等于NaN</li>
<li>如果两个操作数都是对象，则比较它们是不是同一个对象。如果两个操作数都指向同一个对象，则相等操作符返回true；否则，返回false</li>
</ul>
</li>
<li>
<p>全等和不全等。全等操作符由3个等于号（===）表示，它只在两个操作数未经转换就相等的情况下返回true。不全等操作符有一个叹号后跟两个等于号（!==）表示，它在两个操作数未经转换就不相等的情况下返回true。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> result1 = (<span class="hljs-string">"55"</span> == <span class="hljs-number">55</span>)
<span class="hljs-keyword">var</span> result2 = (<span class="hljs-string">"55"</span> === <span class="hljs-number">55</span>)
<span class="hljs-keyword">var</span> result3 = (<span class="hljs-string">"55"</span> != <span class="hljs-number">55</span>)
<span class="hljs-keyword">var</span> result4 = (<span class="hljs-string">"55"</span> !== <span class="hljs-number">55</span>)
<span class="hljs-built_in">console</span>.log(result1) <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(result2) <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(result3) <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(result4) <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<h2 data-id="heading-6">条件操作符</h2>
<p>语法：<code>var max = (num1 > num2) ? num1 : num2</code></p>
<p>以上例子中，max中将会保存一个最大的值，表达式的意思是：如果num1大于num2（关系表达式返回true），则将num1的值赋给max；如果num1小于或等于num2（关系表达式返回false），则将num2的值赋给max</p>
<h2 data-id="heading-7">赋值操作符</h2>
<p>赋值操作符由等于号（=）表示，其作用就是把右侧的值赋给左侧的变量。如果在等号前面再添加乘性操作符、加性操作符或位操作符，就可以完成复合赋值操作。每个主要的算术操作符（以及个别的其他操作符）都有对应的复合赋值操作符。这些操作符如下所示：</p>
<ul>
<li>乘/赋值——*=</li>
<li>除/赋值——/=</li>
<li>模/赋值——%=</li>
<li>加/赋值——+=</li>
<li>减/赋值——-=</li>
<li>左移/赋值——<<=</li>
<li>有符号右移/赋值——>>=</li>
<li>无符号右移/赋值——>>>=</li>
</ul>
<h2 data-id="heading-8">逗号操作符</h2>
<p>逗号操作符可以在一条语句中执行多个操作，如：<code>var num1=1, num2=2, num3=3;</code>。</p>
<p>逗号操作符还可以用于赋值，在用于赋值时，逗号操作符总会返回表达式中的最后一项。如：<code>var num= (5, 6, 1, 4, 7, 0); // num值为0</code></p></div>  
</div>
            