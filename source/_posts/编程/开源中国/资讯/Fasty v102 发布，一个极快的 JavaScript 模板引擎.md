
---
title: 'Fasty v1.0.2 发布，一个极快的 JavaScript 模板引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7017'
author: 开源中国
comments: false
date: Mon, 30 May 2022 14:39:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7017'
---

<div>   
<div class="content">
                                                                                            <h2 style="margin-left:0px; margin-right:0px; text-align:left">Fasty 一个极快的 JavaScript 模板引擎</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Fasty 是一个简约、超快的 JavaScript 模板引擎， 它使用了非常独特的缓存技术，从而获得接近 JavaScript 极限的运行性能，并且同时支持 NodeJS 和浏览器。</p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">Fasty 的渲染速度，超过很多市面上的 JavaScript 引擎 100 倍以上。</p> 
</blockquote> 
<h2 style="margin-left:0; margin-right:0; text-align:left">Fasty 特点</h2> 
<ul> 
 <li>1、极高性能：Fasty 会直接把模板内容编译成 JavaScript 源码执行，而不是使用正则替换，因此，Fasty 的渲染性能超过很多其他模板引擎 100 倍或以上。</li> 
 <li>2、极度简单：Fasty 只内置了输出指令<span> </span><code>&#123;&#123; &#125;&#125;</code><span> </span>和 逻辑指令<span> </span><code>&#123;&#123;~ &#125;&#125;</code></li> 
 <li>3、非常灵活：Fasty 直接与 JavaScript 打通，比如当我们引用 JQuery 之后，可以直接这样使用<span> </span><code>&#123;&#123; $("#id").text() &#125;&#125;</code></li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">使用方法</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>示例1</strong></p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><strong>var</strong> <span>template</span> <span>=</span> <span>'</span><span style="color:#dd1144"><div> hello &#123;&#123; name &#125;&#125; </div></span><span>'</span></span>
<span><strong>var</strong> <span>data</span> <span>=</span> <span>&#123;</span><span style="color:#008080">name</span><span>:</span> <span>"</span><span style="color:#dd1144">fasty</span><span>"</span><span>&#125;</span></span>

<span><strong>var</strong> <span>fasty</span> <span>=</span> <strong style="color:#000000">new</strong> <span>Fasty</span><span>();</span></span>
<span><strong>var</strong> <span>result</span> <span>=</span> <span>fasty</span><span>.</span><span>render</span><span>(</span><span>template</span><span>,</span><span>data</span><span>);</span></span>
<span><span style="color:#888888">// result: <div> hello fasty </div></span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>示例2</strong></p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><strong>var</strong> <span>template</span> <span>=</span> <span>'</span><span style="color:#dd1144"> &#123;&#123;attr&#125;&#125; hello &#123;&#123; func1(name) &#125;&#125; ---</span><span>'</span></span>
<span><strong>var</strong> <span>data</span> <span>=</span> <span>&#123;</span><span style="color:#008080">name</span><span>:</span> <span>"</span><span style="color:#dd1144">fasty</span><span>"</span><span>&#125;</span></span>

<span><strong>var</strong> <span>fasty</span> <span>=</span> <strong style="color:#000000">new</strong> <span>Fasty</span><span>(&#123;</span></span>
<span>    <span style="color:#888888">//共享的模板数据 或者 方法</span></span>
<span>    <span style="color:#008080">share</span> <span>:</span> <span>&#123;</span></span>
<span>        <span style="color:#008080">attr</span><span>:</span><span>'</span><span style="color:#dd1144">text...</span><span>'</span><span>,</span></span>
<span>        <span style="color:#008080">func1</span><span>:</span><strong>function</strong> <span>(</span><span>v</span><span>)&#123;</span></span>
<span>            <strong style="color:#000000">return</strong> <span>v</span> <span>+</span> <span>"</span><span style="color:#dd1144"> kiss~~</span><span>"</span></span>
<span>        <span>&#125;,</span></span>
<span>    <span>&#125;</span></span>
<span><span>&#125;);</span></span>

<span><strong>var</strong> <span>result</span> <span>=</span> <span>fasty</span><span>.</span><span>render</span><span>(</span><span>template</span><span>,</span><span>data</span><span>);</span></span>
<span><span style="color:#888888">// result: text... hello fasty kiss~~</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<h2 style="margin-left:0; margin-right:0; text-align:left">Fasty 语法</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left">输出</h3> 
<div style="text-align:left"> 
 <div> 
  <pre><span>// #1 变量</span>
<span>&#123;&#123;~ var x = 100&#125;&#125;</span>
<span>&#123;&#123;x&#125;&#125;</span>
<span>//输出: 100</span>


<span>// #2 字符串</span>
<span>&#123;&#123;"hello world"&#125;&#125;</span>
<span>//输出：hello world</span>


<span>// #3 安全输出，对 html 进行 escape</span>
<span>&#123;&#123;# "<div> hello world </div>"&#125;&#125;</span>
<span>//输出：&lt;div&gt; hello world &lt;/div&gt;</span>


<span>// #4 强制转换 html 输出</span>
<span>&#123;&#123;! "&lt;div&gt; hello world &lt;/div&gt;"&#125;&#125;</span>
<span>//输出：<div> hello world </div></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<h2 style="margin-left:0; margin-right:0; text-align:left">变量定义</h2> 
<div style="text-align:left"> 
 <div> 
  <pre><span>#1</span>
<span>&#123;&#123;~ var a =100&#125;&#125;</span>

<span>#2</span>
<span>&#123;&#123;~ var a =100,b = 200,c=300&#125;&#125;</span>

<span>#3</span>
<span>#&#123;&#123;~ let a =100&#125;&#125;</span>

<span>#4</span>
<span>#&#123;&#123;~ let a =100,b=200,c=300&#125;&#125;</span>

<span>#4</span>
<span>#&#123;&#123;~ const a =100&#125;&#125;</span>

<span>#5</span>
<span>#&#123;&#123;~ const a =100,b=200,c=300&#125;&#125;</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<h3 style="margin-left:0; margin-right:0; text-align:left">if-else</h3> 
<div style="text-align:left"> 
 <div> 
  <pre><span>&#123;&#123;~ if (x == 100) &#125;&#125;</span>

<span>&#123;&#123;~ elseif(x == 200) &#125;&#125;</span>

<span>&#123;&#123;~ else if(x == 300) &#125;&#125;</span>

<span>&#123;&#123;~ else &#125;&#125;</span>

<span>&#123;&#123;~ end &#125;&#125;</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">同时支持 'elseif' or 'else if'</p> 
</blockquote> 
<h3 style="margin-left:0; margin-right:0; text-align:left">for 循环</h3> 
<div style="text-align:left"> 
 <div> 
  <pre><span>// #1</span>
<span>&#123;&#123;~ for (item of array) &#125;&#125;</span>

<span>&#123;&#123;~end&#125;&#125;</span>

<span>// #2</span>
<span>&#123;&#123;~ for (item in array) &#125;&#125;</span>

<span>&#123;&#123;~end&#125;&#125;</span>

<span>// #3</span>
<span>&#123;&#123;~ for (let item of array) &#125;&#125;</span>

<span>&#123;&#123;~end&#125;&#125;</span>

<span>// #4</span>
<span>&#123;&#123;~ for (const item in array) &#125;&#125;</span>

<span>&#123;&#123;~end&#125;&#125;</span>

<span>// #5</span>
<span>&#123;&#123;~ for (key of Object.keys(item) )&#125;&#125;</span>

<span>&#123;&#123;~end&#125;&#125;</span>

<span>// #6</span>
<span>&#123;&#123;~ for (var x = i;x < 100;x++) &#125;&#125;</span>

<span>&#123;&#123;~ end &#125;&#125;</span>

<span>// #7</span>
<span>&#123;&#123;~ for (item of someMethodInvoke().other()) &#125;&#125;</span>

<span>&#123;&#123;~end&#125;&#125;</span>

<span>// #8</span>
<span>&#123;&#123;~ for (var x = i;x < someMethodInvoke().other();x++) &#125;&#125;</span>

<span>&#123;&#123;~ end &#125;&#125;</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<h3 style="margin-left:0; margin-right:0; text-align:left">安全访问</h3> 
<div style="text-align:left"> 
 <div> 
  <pre><span>#1</span>
<span>&#123;&#123;a?.b?.c&#125;&#125;</span>

<span>#2</span>
<span>&#123;&#123;a.bbbb?().ccc?.ddd&#125;&#125;</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<h3 style="margin-left:0; margin-right:0; text-align:left">初始化配置</h3> 
<div style="text-align:left"> 
 <div> 
  <pre><span><strong>var</strong> <span>options</span> <span>=</span> <span>&#123;</span></span>
<span>    <span style="color:#888888">//共享模板方法和数据</span></span>
<span>    <span style="color:#008080">share</span> <span>:</span> <span>&#123;</span></span>
<span>        <span style="color:#008080">attr</span><span>:</span><span>'</span><span style="color:#dd1144">text...</span><span>'</span><span>,</span></span>
<span>        <span style="color:#008080">func1</span><span>:</span><strong>function</strong> <span>(</span><span>v</span><span>)&#123;</span></span>
<span>            <strong style="color:#000000">return</strong> <span>v</span> <span>+</span> <span>"</span><span style="color:#dd1144"> kiss~~</span><span>"</span></span>
<span>        <span>&#125;,</span></span>
<span>    <span>&#125;,</span></span>
<span>    <span style="color:#888888">// 是否是共享数据优先</span></span>
<span>    <span style="color:#888888">// 默认 false，即： render 方法传入的 data 数据优先</span></span>
<span>    <span style="color:#008080">shareDataFirst</span><span>:</span> <strong>false</strong><span>,</span> <span style="color:#888888">//default is false</span></span>
<span>    </span>
<span>    <span style="color:#888888">//是否开启安全访问，这个功能不支持 IE 浏览器</span></span>
<span>    <span style="color:#888888">//IE 下需要设置为 false，同时配置 false 后会得到更高的运行性能</span></span>
<span>    <span style="color:#008080">safelyAccess</span><span>:</span> <strong>true</strong><span>,</span></span>

<span>    <span style="color:#888888">//自定义 html 安全输出方法</span></span>
<span>    <span style="color:#888888">//当使用 &#123;&#123;# ... &#125;&#125; 的时候使用该方法转换</span></span>
<span>    <span style="color:#008080">$escape</span><span>:</span><strong>function</strong> <span>(</span><span>html</span><span>)&#123;</span><strong style="color:#000000">return</strong> <span>html</span><span>&#125;,</span></span>

<span>    <span style="color:#888888">//自定义 unescape 方法</span></span>
<span>    <span style="color:#888888">//当使用 &#123;&#123;! ... &#125;&#125; 的时候使用该方法转换</span></span>
<span>    <span style="color:#008080">$unescape</span><span>:</span><strong>function</strong> <span>(</span><span>value</span><span>)&#123;</span><strong style="color:#000000">return</strong> <span>value</span><span>&#125;</span></span>
<span><span>&#125;</span></span>

<span><strong>var</strong> <span>fasty</span> <span>=</span> <strong style="color:#000000">new</strong> <span>Fasty</span><span>(</span><span>options</span><span>);</span></span>
<span><span>fast</span><span>.</span><span>render</span><span>(</span><span>template</span><span>,</span><span>data</span><span>)</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<h2 style="margin-left:0; margin-right:0; text-align:left">作者</h2> 
<ul> 
 <li>Micahel (<a href="https://www.oschina.net/action/GoToLink?url=mailto%3Afuhai999%40gmail.com" target="_blank">fuhai999@gmail.com</a>) - 小码科技</li> 
 <li>Wechat: wx198819880</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">License</h2> 
<p style="color:#40485b; margin-left:0em; margin-right:0em; text-align:left">Fasty is licensed under the MIT License.</p> 
<h2>开源地址</h2> 
<p><a href="https://gitee.com/fuhai/fasty">https://gitee.com/fuhai/fasty</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            