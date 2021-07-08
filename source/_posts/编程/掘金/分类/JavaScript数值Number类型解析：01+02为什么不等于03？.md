
---
title: 'JavaScript数值Number类型解析：0.1+0.2为什么不等于0.3？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/995eef1bde074a5f8b780d99ba5ab986~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 01:57:12 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/995eef1bde074a5f8b780d99ba5ab986~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">从一道面试题"0.1+0.2 === 0.3"，看JavaScript数值Number类型解析</h1>
<h2 data-id="heading-1">分析（原来JS的Number是Double）</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">0.1</span> + <span class="hljs-number">0.2</span> <span class="hljs-comment">// 0.30000000000000004;</span>
<span class="hljs-number">0.1</span>+<span class="hljs-number">0.2</span> === <span class="hljs-number">0.3</span> <span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从代码的运行结果来看，显然0.1+0.2是不等于0.3的那么导致这种结果的原因是什么呢？</p>
<pre><code class="hljs language-js copyable" lang="js">JavaScript权威指南第六版-第<span class="hljs-number">3</span>章类型”说明，在JavaScript当中对于数字<span class="hljs-built_in">Number</span>类型的表示采用的是 “IEEE <span class="hljs-number">754</span> 标准
定义的双精度<span class="hljs-number">64</span>位格式” 和其他编程语言（如C，Java）不同，JavaScript不区分整数值和浮点数值，所有数值在JavaScript
中均用双精度浮点数值表示（相当于C，Java中的double），所以在进行数字运算的时候要特别注意精度缺失问题。
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">IEEE 754标准</h2>
<p>简单介绍“IEEE 754”规范，<code>IEEE 754”采用双精度存储（double-precision 64-bit format IEEE 754 values）</code>占用64 bit</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/995eef1bde074a5f8b780d99ba5ab986~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">意义：</h3>
<ul>
<li>s(sign) 1位用来表示符号位(正负数)</li>
<li>e(exponent) 11位用来表示指数</li>
<li>m(mantissa) 52位用来表示尾数</li>
</ul>
<h2 data-id="heading-4">JavaScript中数字的存储机制</h2>
<p><code>(s) * (m) * (2^e)</code>
<br></p>
<blockquote>
<p>根据ECMAScript 5 规范，e 的范围是 [-1074, 971]，这样可以得出 js 能表示的最大值为1 * (2^53 - 1) * (2^971) = 1.7976931348623157e+308，而这个值恰好是 Number.MAX_VALUE 的值；同理可以推出 js 能表示的大于 0 的最小值是1 * 1 * (2 ^ -1074) = 5e-324，这个值恰好是 Number.MIN_VALUE 的值。</p>
</blockquote>
<h2 data-id="heading-5">那么浮点数在运算时又为什么会造成精度缺失呢？</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">0.1</span> >> <span class="hljs-number">0.0001</span> <span class="hljs-number">1001</span> <span class="hljs-number">1001</span> <span class="hljs-number">1001.</span>..无限循环
<span class="hljs-number">0.2</span> >> <span class="hljs-number">0.0011</span> <span class="hljs-number">0011</span> <span class="hljs-number">0011</span> <span class="hljs-number">0011</span>...无限循环
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于存储空间的有限，于是只能模仿十进制进行四舍五入了，但是二进制只有 0 和 1 两个，于是变为 0 舍 1 入。这即是计算机中部分浮点数运算时出现误差，丢失精度的根本原因。</p>
<h2 data-id="heading-6">大整数的精度丢失</h2>
<p>大整数的精度丢失和浮点数本质上是一样的，尾数位最大是 52 位，因此 JS 中能精准表示的最大整数是 Math.pow(2, 53)，十进制即 9007199254740992。</p>
<p>大于 9007199254740992 的可能会丢失精度</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">9007199254740992</span> + <span class="hljs-number">1</span>
<span class="hljs-comment">// 丢失 9007199254740992</span>
<span class="hljs-number">9007199254740992</span> + <span class="hljs-number">2</span>
<span class="hljs-comment">// 未丢失 9007199254740994</span>
<span class="hljs-number">9007199254740992</span> + <span class="hljs-number">3</span>
<span class="hljs-comment">// 丢失 9007199254740996</span>
<span class="hljs-number">9007199254740992</span> + <span class="hljs-number">4</span>
<span class="hljs-comment">// 未丢失 9007199254740996</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">回到问题</h2>
<p><code>那么为什么0.1+0.2不等于0.3呢？</code></p>
<ul>
<li>因为 计算机 的存储原理,造成计算机在存储浮点数时,存储的不是准确数值,存储的是一个近似数值,显示时,显示为一个浮点数值效果；</li>
<li>当浮点数直接参与计算或者参与比较时,实际参与预算或者比较的数值,也是近似值；</li>
<li>就造成了计算或者比较时,一定会存在误差,这个误差在特殊情况下会表现出误差的结果；</li>
</ul>
<p>ps：JavaScript中规定，即使使用科学计数法，数据类型也是浮点数类型，浮点数的误差/浮点数的精确丢失</p>
<h3 data-id="heading-8">模拟计算</h3>
<p>先将 0.1 和 0.2 转化成二进制，对于十进制转二进制，整数部分<code>除二取余，倒序排列</code>，小数部分<code>乘二取整，顺序排列</code></p>
<p>0.1 转化为二进制0.0 0011 0011 0011 0011 0011 0011 … （0011循环）</p>
<p>0.2 转化为二进制0.0011 0011 0011 0011 0011 0011 0011 … （0011循环）</p>
<p>然后根据<code>IEEE 754标准 (s) * (m) * (2^e)</code>来表示</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 0.1</span>
e = -<span class="hljs-number">4</span>;
m = <span class="hljs-number">1.1001100110011001100110011001100110011001100110011010</span> (<span class="hljs-number">52</span>位)

<span class="hljs-comment">// 0.2</span>
e = -<span class="hljs-number">3</span>;
m = <span class="hljs-number">1.1001100110011001100110011001100110011001100110011010</span> (<span class="hljs-number">52</span>位)

<span class="hljs-comment">//这里的m指的是小数点后的52位，e为m的指数，小数点前的整数部分就是隐藏位s来表示符号</span>
<span class="hljs-comment">//如果发现指数e不一致时，一般采用右移，因为即使右边溢出了，损失的精度远远小于左移时的溢出</span>
<span class="hljs-comment">//转化之后进行求和</span>

e = -<span class="hljs-number">3</span>; m = <span class="hljs-number">0.1100110011001100110011001100110011001100110011001101</span> (<span class="hljs-number">52</span>位)
+
e = -<span class="hljs-number">3</span>; m = <span class="hljs-number">1.1001100110011001100110011001100110011001100110011010</span> (<span class="hljs-number">52</span>位)
<span class="hljs-comment">// 得到</span>
e = -<span class="hljs-number">3</span>; m = <span class="hljs-number">10.0110011001100110011001100110011001100110011001100111</span> (<span class="hljs-number">52</span>位)
<span class="hljs-comment">// 保留一位整数</span>
e = -<span class="hljs-number">2</span>; m = <span class="hljs-number">1.00110011001100110011001100110011001100110011001100111</span> (<span class="hljs-number">53</span>位)
<span class="hljs-comment">// 发现超过了52位，于是要做四舍五入，因为无法区分哪个更接近，于是规则是保留偶数的一个，得到最终的二进制数</span>
m=<span class="hljs-number">1.0011001100110011001100110011001100110011001100110100</span> (<span class="hljs-number">52</span>位)
<span class="hljs-comment">// 然后得到最终的二进制数</span>
<span class="hljs-number">1.0011001100110011001100110011001100110011001100110100</span> * <span class="hljs-number">2</span>^-<span class="hljs-number">2</span> = <span class="hljs-number">0.010011001100110011001100110011001100110011001100110100</span>
<span class="hljs-comment">// 现在转化为十进制，二进制小数转化为十进制的方法是小数点后 第一位 *2 ^ -1，第二位 *2 ^ -2，以此类推</span>
<span class="hljs-comment">// 可以利用等比数列求和公式，最终求得十进制数为0.30000000000000004</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">结论</h2>
<p>所以0.1 + 0.2 的最终结果是0.30000000000000004</p></div>  
</div>
            