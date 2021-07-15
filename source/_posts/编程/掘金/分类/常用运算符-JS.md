
---
title: '常用运算符-JS'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7440'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 23:03:53 GMT
thumbnail: 'https://picsum.photos/400/300?random=7440'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>前端小白的学习笔记，如有错误请各位大佬指出，万分感谢！！！</p>
</blockquote>
<h4 data-id="heading-0">1.  数学运算符</h4>
<h5 data-id="heading-1">1.1 加性运算符  （含隐式转换）</h5>
<p><strong>加法+</strong></p>
<ul>
<li>
<p>加号两侧的操作数有任何一个属于字符类型（String），加号为字符串拼接作用；</p>
</li>
<li>
<p>算数相加</p>
<ul>
<li>
<p>Number类型</p>
<ul>
<li>操作数都是 数值 ，按照加法运算；</li>
<li>如果有一个操作数是NaN，那么结果为NaN</li>
</ul>
</li>
<li>
<p>null / undefined / true / false / 对象 / 数组   =>   进行隐式类型转换</p>
<ul>
<li>
<p>对象隐式转换规则：</p>
<p>如果操作数是对象，首先会转换为原始值（toPrimitive函数，日期对象会调用<code>toString()</code>，其他对象会调用<code>valueOf()</code>，），得到的原始值不再被强制转换为数字或字符串。在这种约束下，对象转为原始值基本都是字符串（如果你没有重写<code>valuOf()</code>或者<code>toString()</code>方法），再进行加法操作。</p>
</li>
<li>
<p>加法例子：</p>
</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log(<span class="hljs-string">'10'</span> + <span class="hljs-number">1</span>);       <span class="hljs-comment">// '101'</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span> + <span class="hljs-number">2</span> + <span class="hljs-string">'3'</span>);    <span class="hljs-comment">// '33'</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span> + <span class="hljs-literal">NaN</span>);        <span class="hljs-comment">// NaN  (Number)</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span> + <span class="hljs-literal">true</span>);       <span class="hljs-comment">// 2    (Number)</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span> + <span class="hljs-literal">false</span>);      <span class="hljs-comment">// 1    (Number)</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span> + <span class="hljs-literal">null</span>);       <span class="hljs-comment">// 1    (Number)</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span> + <span class="hljs-literal">undefined</span>);  <span class="hljs-comment">// NaN  (Number)</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span> + []);       <span class="hljs-comment">// '1'</span>
<span class="hljs-built_in">console</span>.log([] + <span class="hljs-number">1</span>);       <span class="hljs-comment">// '1'</span>
<span class="hljs-built_in">console</span>.log([] + []);      <span class="hljs-comment">// ''</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span> + [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>]);  <span class="hljs-comment">// '11,2,3'</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span> + &#123;&#125;);          <span class="hljs-comment">// '1[object Object]'</span>
<span class="hljs-built_in">console</span>.log(&#123;&#125; + <span class="hljs-number">1</span>);          <span class="hljs-comment">// '[object Object]1'</span>
<span class="hljs-built_in">console</span>.log(&#123;&#125; + &#123;&#125;);         <span class="hljs-comment">// '[object Object][object Object]'</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span> + &#123;<span class="hljs-attr">name</span>:<span class="hljs-string">'li'</span>&#125;); <span class="hljs-comment">// '1[object Object]'</span>
<span class="hljs-built_in">console</span>.log([] + &#123;&#125;);                <span class="hljs-comment">// '[object Object]'</span>
<span class="hljs-built_in">console</span>.log(&#123;&#125; + []);                <span class="hljs-comment">// '[object Object]'</span>
<span class="hljs-built_in">console</span>.log([<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>] + &#123;<span class="hljs-attr">name</span>:<span class="hljs-string">'li'</span>&#125;);  <span class="hljs-comment">// '1,2,3[object Object]'</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>() + <span class="hljs-number">1</span>);         <span class="hljs-comment">// 'Fri Jul 09 2021 10:36:29 GMT+0800 (中国标准时间)1'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
</ul>
<p><strong>减法-</strong></p>
<ul>
<li>
<p>Number类型</p>
<ul>
<li>操作数都是 数值 ，按照减法运算；</li>
<li>如果有一个操作数是NaN，那么结果为NaN</li>
</ul>
</li>
<li>
<p>String、null、undefined、true、false</p>
<ul>
<li>如果操作数的类型不是Number类型，将按照隐形类型转化转化为Number类型，在进行操作。</li>
</ul>
<p>备：加法与减法都是加性运算符，a-b 可以看作 a+(-b)</p>
</li>
</ul>
<h5 data-id="heading-2">1.2 乘性运算符</h5>
<p><strong>乘法</strong>*</p>
<ul>
<li>
<p>Number类型</p>
<ul>
<li>操作数都是 数值 ，按照乘法运算；</li>
<li>如果有一个操作数是NaN，那么结果为NaN</li>
</ul>
</li>
<li>
<p>String、null、undefined、true、false</p>
<ul>
<li>如果操作数的类型不是Number类型，将按照隐形类型转化转化为Number类型，再进行操作。</li>
</ul>
</li>
</ul>
<p><strong>除法 /</strong></p>
<ul>
<li>
<p>同上</p>
</li>
<li>
<p>除数不能为0，否则结果为 Infinity 或 -Infinity</p>
</li>
<li>
<p>被除数和除数都是0，结果为 NaN</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span> / <span class="hljs-number">0</span>); <span class="hljs-comment">// Infinity</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">0</span> / <span class="hljs-number">1</span>); <span class="hljs-comment">// 0</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">0</span> / <span class="hljs-number">0</span>); <span class="hljs-comment">// NaN</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p><strong>取模 %</strong></p>
<ul>
<li>
<p>Number类型</p>
<ul>
<li>如果左右两侧均是数值，则进行除法计算，结果返回余数</li>
<li>任何一侧为NaN，则结果返回NaN</li>
<li>只要除数是0，则结果返回NaN</li>
</ul>
</li>
<li>
<p>如果有一侧不为Number类型，则（根据对应的规则）转为数字类型后，再进行计算。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span> % <span class="hljs-number">0</span>) <span class="hljs-comment">// NaN</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">0</span> % <span class="hljs-number">1</span>) <span class="hljs-comment">// 1</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">0</span> % <span class="hljs-number">0</span>) <span class="hljs-comment">// NaN</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>案例：用于判断奇偶数，表格隔行变色</p>
</li>
</ul>
<h5 data-id="heading-3">1.3 一元运算符</h5>
<p><strong>加号 + 、 减号 -</strong></p>
<ul>
<li>操作数是Number类型，无影响（不论是正号还是负号，对NaN都是无影响）</li>
</ul>
<ul>
<li>
<p>操作数是其他类型，它具有转化成Number类型的功能，效果与<code>Number(...)</code> 相同。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log(+[]);    <span class="hljs-comment">// 0</span>
<span class="hljs-built_in">console</span>.log(+[<span class="hljs-number">1</span>]);   <span class="hljs-comment">// 1</span>
<span class="hljs-built_in">console</span>.log(+[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>]); <span class="hljs-comment">// NaN  [1,2]原始值为'1,2'，转化为Number类型为NaN</span>
<span class="hljs-built_in">console</span>.log(+&#123;&#125;);    <span class="hljs-comment">// NaN</span>
<span class="hljs-built_in">console</span>.log(-<span class="hljs-literal">undefined</span>)  <span class="hljs-comment">// NaN</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p><strong>隐式类型转换</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> str = <span class="hljs-string">'123'</span>;
<span class="hljs-built_in">console</span>.log(str + <span class="hljs-number">2</span>);    <span class="hljs-comment">// 1232</span>
<span class="hljs-built_in">console</span>.log(+str + <span class="hljs-number">2</span>);   <span class="hljs-comment">// 125  => '123'转化为Number类型</span>

<span class="hljs-keyword">var</span> num1 = <span class="hljs-number">10</span>;
<span class="hljs-keyword">var</span> num2 = <span class="hljs-number">20</span>;
<span class="hljs-built_in">console</span>.log(num1 + num2);      <span class="hljs-comment">// 30</span>
<span class="hljs-built_in">console</span>.log(num1 + <span class="hljs-string">''</span> + num2); <span class="hljs-comment">// 1020  => 转化为字符串拼接</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-4">1.4 递增递减运算符</h5>
<ul>
<li>
<p>++ & --</p>
</li>
<li>
<p>前置型：num1基础上，进行+1的操作，然后和num2进行相加</p>
</li>
<li>
<p>后置型：num1基础上，和num2进行相加，在计算之前，并没有发生自增的情况,计算完成之后再自增。</p>
</li>
<li>
<p>如果有一侧不为Number类型，则（根据对应的规则）转为数字类型后，再进行计算。</p>
</li>
</ul>
<h5 data-id="heading-5">1.5 案例</h5>
<ul>
<li>0.1 + 0.2  =>  （0.1 * 10 + 0.2 * 10）/10（判断小数位数，方法并不全面，可以去了解一下浮点精度问题）</li>
</ul>
<h4 data-id="heading-6">2. 赋值运算符</h4>
<ul>
<li>=  、 +=  、  -=  、 *=  、 /=  、 %=</li>
</ul>
<h4 data-id="heading-7">3. 比较运算符</h4>
<h5 data-id="heading-8">3.1 关系操作符</h5>
<ul>
<li><  、 >  、 <=  、 >=</li>
</ul>
<ul>
<li>关系操作符（比较操作符），最终返回的结果是一个布尔值</li>
<li>Number 类型，直接比较；如果比较中出现了NaN，那么结果就是false</li>
<li>String 类型
<ul>
<li>一侧是字符串，按照相应规则进行转换</li>
<li>两侧均为字符串，按照UniCode编码进行判断，字符串的比较是逐位比较的，不用关心字符串长度</li>
</ul>
</li>
<li>null 、undefined、true、false，根据对应的规则进行转换。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log(<span class="hljs-string">'3'</span> < <span class="hljs-number">17</span>);      <span class="hljs-comment">// true    Number('3') => 3 => 3<17</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'abc'</span> < <span class="hljs-number">3</span>);     <span class="hljs-comment">// false   Number('abc') => NaN => NaN<3</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'3'</span> < <span class="hljs-string">'17'</span>);    <span class="hljs-comment">// false   ('3').codePointAt() < ('1').codePointAt()  逐位比较</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'abc'</span> < <span class="hljs-string">'3'</span>);   <span class="hljs-comment">// false   ('a').codePointAt() < ('3').codePointAt()  逐位比较</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">3</span> > <span class="hljs-number">2</span> > <span class="hljs-number">1</span>);     <span class="hljs-comment">// false   从左向右依次比较，3>2 为 true, true>1 为 false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-9">3.2 相等运算符</h5>
<ul>
<li>==相等 、 !=不等  、===全等 、!==不全等</li>
</ul>
<p><strong>相等</strong></p>
<ul>
<li>NaN不等于任何类型的数值，包括自己本身，返回false</li>
<li>两侧均为String类型，比较UniCode字符编码值</li>
<li>两侧均为Number类型数值，比较值是否相同</li>
<li>两侧均为Object类型，则比较地址是否一致</li>
<li>null == undefined 返回true</li>
<li>一侧是String，一侧是Number,将String转换为Number类型再进行比较</li>
<li>如果一侧是Boolean，则将布尔值转换为Number类型后，再比较;</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log(<span class="hljs-string">'ABC'</span> == <span class="hljs-string">'abc'</span>);  <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-literal">NaN</span> == <span class="hljs-literal">NaN</span>)       <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'123'</span> == <span class="hljs-number">123</span>)     <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-literal">null</span> == <span class="hljs-literal">undefined</span>)<span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-literal">false</span> == <span class="hljs-number">0</span>)       <span class="hljs-comment">// true</span>

<span class="hljs-keyword">let</span> obj1 = &#123;<span class="hljs-attr">x</span>:<span class="hljs-number">10</span>&#125;;       
<span class="hljs-keyword">let</span> obj2 = &#123;<span class="hljs-attr">x</span>:<span class="hljs-number">10</span>&#125;;
<span class="hljs-keyword">let</span> obj3 = obj1;
<span class="hljs-built_in">console</span>.log(obj1 == obj2);    <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(obj1 == obj3);    <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>全等</strong></p>
<ul>
<li>值是否相等</li>
<li>类型是否相等</li>
</ul>
<p><strong>不等、不全等 与 相等、全等的结果相反</strong></p>
<h4 data-id="heading-10">4. 逻辑运算符</h4>
<p><strong>与 &&</strong></p>
<ul>
<li>
<p>看左侧的操作数：进行隐式类型的转换，转为Boolean类型，true / false</p>
<ul>
<li>
<p>false ，返回左侧的操作数</p>
</li>
<li>
<p>true ， 返回右侧的操作数</p>
</li>
</ul>
</li>
</ul>
<p><strong>或 ||</strong></p>
<ul>
<li>
<p>看左侧的操作数：0，进行隐式类型的转换，转为Boolean类型，true / false</p>
<ul>
<li>
<p>true ，返回左侧的操作数</p>
</li>
<li>
<p>false， 返回右侧的操作数</p>
</li>
</ul>
</li>
</ul>
<p><strong>非 ！</strong></p>
<ul>
<li>取反，只作用于一个操作数，得到的结果一定是个boolean</li>
<li>!! 两次取反相当于类型转换Boolean()</li>
<li>作用在一个条件上，所以也是一元运算符的成员之一</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span> && <span class="hljs-number">2</span>);    <span class="hljs-comment">// 2</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">0</span> && <span class="hljs-number">2</span>);    <span class="hljs-comment">// 0</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span> || <span class="hljs-number">2</span>);    <span class="hljs-comment">// 1</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">0</span> || <span class="hljs-number">2</span>);    <span class="hljs-comment">// 2</span>
<span class="hljs-built_in">console</span>.log(!<span class="hljs-literal">true</span>);     <span class="hljs-comment">// false</span>
<span class="hljs-built_in">console</span>.log(!<span class="hljs-number">0</span>);        <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(!!<span class="hljs-number">100</span>);     <span class="hljs-comment">// true</span>
<span class="hljs-built_in">console</span>.log(!&#123;&#125;);       <span class="hljs-comment">// false  =>  Object类型，结果返回false (所有对象均为true)</span>
<span class="hljs-built_in">console</span>.log(!<span class="hljs-string">''</span>);       <span class="hljs-comment">//true    =>  空字符串，结果返回true</span>
<span class="hljs-built_in">console</span>.log(!<span class="hljs-string">'abc'</span>);    <span class="hljs-comment">// false  =>  非空的字符串，结果返回false</span>
<span class="hljs-built_in">console</span>.log(!<span class="hljs-literal">NaN</span>);      <span class="hljs-comment">// true   =>  NaN，返回true</span>
<span class="hljs-built_in">console</span>.log(!<span class="hljs-number">100</span>);      <span class="hljs-comment">// false  =>  非0数值，返回false</span>
<span class="hljs-built_in">console</span>.log(!<span class="hljs-literal">null</span>);     <span class="hljs-comment">// true   =>  null 或 undefined，返回true</span>
<span class="hljs-built_in">console</span>.log(!<span class="hljs-literal">undefined</span>);<span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            