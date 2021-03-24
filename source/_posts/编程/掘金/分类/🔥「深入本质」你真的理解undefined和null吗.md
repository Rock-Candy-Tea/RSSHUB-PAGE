
---
title: '🔥「深入本质」你真的理解undefined和null吗'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e13ef6e64254455fb9b1ccb3156b145b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 23 Mar 2021 19:21:08 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e13ef6e64254455fb9b1ccb3156b145b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><code>undefined</code>和<code>null</code>在js中非常常见，而且两者都代表"空"的含义，但又有细微的差异，这俩每天都能见到的东西，你真的了解它们吗？来和Blue一起，重新认识<code>undefined</code>和<code>null</code>吧</p>
<blockquote>
<p>undefined和null在使用中几乎可以等同（除了判断时），但探究内部的原理有助于加深对程序的理解</p>
</blockquote>
<p>本文将包含以下内容</p>
<ul>
<li>undefined和null都是空，但又不是一个东西，<strong>JS为什么要搞两个空</strong>？</li>
<li>undefined是什么？什么时候出现undefined？</li>
<li>null是什么？什么时候用到null？</li>
<li>undefined和null的本质</li>
<li>如何正确使用undefined和null</li>
</ul>
<h1 data-id="heading-0">快速介绍</h1>
<p>首先，<code>undefined</code>和<code>null</code>都是假值（falsy），都能作为条件进行判断，所以在<strong>绝大多数情况下两者在使用上没有区别</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">if</span>(<span class="hljs-literal">undefined</span>)&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'真的'</span>);
&#125;<span class="hljs-keyword">else</span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'假的'</span>);  <span class="hljs-comment">//执行</span>
&#125;

<span class="hljs-keyword">if</span>(<span class="hljs-literal">null</span>)&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'真的'</span>);
&#125;<span class="hljs-keyword">else</span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'假的'</span>);  <span class="hljs-comment">//执行</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>甚至连官方都**“很贴心”的让null和undefined判定为相等**</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log(<span class="hljs-literal">null</span>==<span class="hljs-literal">undefined</span>); <span class="hljs-comment">//true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么，<code>undefined</code>和<code>null</code>是不是完全相同呢？不是</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//松散比较(loose equality)</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-literal">null</span> == <span class="hljs-literal">undefined</span>); <span class="hljs-comment">//true</span>

<span class="hljs-comment">//严格比较(strict equality)</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-literal">null</span> === <span class="hljs-literal">undefined</span>); <span class="hljs-comment">//false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的例子可以看出</p>
<ul>
<li>
<p><code>undefined</code>和<code>null</code>并不是同一个东西，严格比较会判定为不相等</p>
</li>
<li>
<p>它们到底是什么、有什么区别、如何影响我们是用呢</p>
</li>
</ul>
<h1 data-id="heading-1">重新认识undefined</h1>
<h2 data-id="heading-2">什么时候出现undefined</h2>
<p>字面上，<code>undefined</code>就是"未定义"的意思，所以当我们没有定义一个东西之前，它就是undefined</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//a并未定义过</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">typeof</span> a);  <span class="hljs-comment">//"undefined"</span>

<span class="hljs-comment">//注意，这里只能使用typeof，直接使用a会造成报错</span>
<span class="hljs-built_in">console</span>.log(a);  <span class="hljs-comment">//Uncaught ReferenceError: a is not defined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们知道js是弱类型的，所以变量本身没有类型，变量内存储的数据才有，所以当一个变量没有任何数据时，它也是<code>undefined</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//定义但未赋值</span>
<span class="hljs-keyword">let</span> a;

<span class="hljs-built_in">console</span>.log(a);  <span class="hljs-comment">//undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>undefined</code>是js的原始数据类型之一，我们也可以直接把undefined赋值给变量</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> a=<span class="hljs-literal">undefined</span>;

<span class="hljs-built_in">console</span>.log(a); <span class="hljs-comment">//undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，不只变量，函数中也出现undefined</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//1-参数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">blueFn</span>(<span class="hljs-params">a, b</span>)</span>&#123;
  <span class="hljs-built_in">console</span>.log(a, b);
&#125;

blueFn(<span class="hljs-number">12</span>);  <span class="hljs-comment">//12, undefined——因为b没有传值，所以是undefined</span>


<span class="hljs-comment">//2-返回值</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">blueFn1</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">return</span>;
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">blueFn2</span>(<span class="hljs-params"></span>)</span>&#123;
  
&#125;

blueFn1();  <span class="hljs-comment">//undefined——return没写东西，类似于变量没赋值</span>
blueFn2();  <span class="hljs-comment">//undefined——连return都没有，跟变量没有声明过差不多</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对象中也会出现<code>undefined</code>，当我们是用一个不存在的属性时，会得到undefined作为值（ts等强类型语言会直接报错）</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> blue=&#123;<span class="hljs-attr">age</span>: <span class="hljs-number">18</span>, <span class="hljs-attr">gender</span>: <span class="hljs-string">'male'</span>&#125;;

<span class="hljs-built_in">console</span>.log(blue.height); <span class="hljs-comment">//undefined——因为就没有叫height的东西</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结一下，<code>undefined</code>会出现的场景有五种</p>
<ul>
<li>真的是没定义（仅typeof可用）</li>
<li>定义了但没赋值</li>
<li>直接赋值或返回undefined</li>
<li>函数空return或者干脆没有return</li>
<li>没有对应属性</li>
</ul>
<h2 data-id="heading-3">undefined是什么？——被迫的替代方案</h2>
<p>经过上面的梳理其实我们可以看出——<strong><code>undefined</code>就是没有值</strong>，不论是没赋值、没传参、没返回、没这个属性，都会导致系统无法找到对应的内容，从而返回undefined作为"替代选项"</p>
<h1 data-id="heading-4">重新认识null</h1>
<p><code>null</code>和<code>undefined</code>不同，<code>null</code>不是没得选才出来，<strong>想使用<code>null</code>必须主动要求</strong></p>
<h2 data-id="heading-5">什么时候出现null</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//变量</span>
<span class="hljs-keyword">let</span> name;
<span class="hljs-built_in">console</span>.log(name);  <span class="hljs-comment">//undefined</span>

<span class="hljs-keyword">let</span> name=<span class="hljs-string">'blue'</span>;
<span class="hljs-built_in">console</span>.log(name);  <span class="hljs-comment">//null</span>



<span class="hljs-comment">//函数-参数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn1</span>(<span class="hljs-params">a</span>)</span>&#123;
  <span class="hljs-built_in">console</span>.log(a);
&#125;
fn1(); <span class="hljs-comment">//undefined</span>
fn1(<span class="hljs-literal">null</span>); <span class="hljs-comment">//null</span>



<span class="hljs-comment">//函数-返回值</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn2</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">return</span>; <span class="hljs-comment">//undefined</span>
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn2</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>; <span class="hljs-comment">//undefined</span>
&#125;

<span class="hljs-comment">//对象属性</span>
<span class="hljs-keyword">const</span> person=&#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'blue'</span>&#125;;
<span class="hljs-built_in">console</span>.log(person1.age); <span class="hljs-comment">//undefined</span>

<span class="hljs-keyword">const</span> person=&#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'blue'</span>, <span class="hljs-attr">age</span>: <span class="hljs-literal">null</span>&#125;;
<span class="hljs-built_in">console</span>.log(person1.age); <span class="hljs-comment">//null</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">null是什么？——主动选择为空</h2>
<p>通过上面的例子，咱们能看出一个有意思的现象——<strong>咱们不明说由系统来猜时，会得到<code>undefined</code>；而<code>null</code>则需要我们主动要求才给</strong></p>
<h1 data-id="heading-7">所以，这俩啥区别？</h1>
<p><strong><code>null</code>是一个普通值，需要主动使用</strong>，和12、'abc'、false没多大区别</p>
<ul>
<li>只有主动使用时，<code>null</code>才会出现</li>
<li>没有声明<code>null</code>不会自己蹦出来</li>
</ul>
<p><strong><code>undefined</code>是一个特殊值</strong>，是js中最后的备选方案</p>
<ul>
<li>当我们向js要求一个“不存在的东西”时，会得到<code>undefined</code>（例如：没赋值的变量、没return的函数、没传的参数）</li>
</ul>
<h2 data-id="heading-8">undefined与null的本质</h2>
<p>相对来说，<strong><code>null</code>更接近其他语言的空</strong>、而<code>undefined</code>则是js特有的机制</p>
<h3 data-id="heading-9">null本质上是个零，undefined本质上是个特殊对象</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Number</span>(<span class="hljs-literal">null</span>); <span class="hljs-comment">//0</span>
<span class="hljs-built_in">Number</span>(<span class="hljs-literal">undefined</span>); <span class="hljs-comment">//NaN</span>

<span class="hljs-number">12</span>+<span class="hljs-literal">null</span>; <span class="hljs-comment">//12</span>
<span class="hljs-number">12</span>+<span class="hljs-literal">undefined</span>; <span class="hljs-comment">//NaN</span>


<span class="hljs-comment">//跟数字比较会更加明显</span>
-<span class="hljs-number">5</span><<span class="hljs-literal">null</span>; <span class="hljs-comment">//true——null是0，-5<0</span>

-<span class="hljs-number">5</span><<span class="hljs-literal">undefined</span>;  <span class="hljs-comment">//false</span>
-<span class="hljs-number">5</span>><span class="hljs-literal">undefined</span>;  <span class="hljs-comment">//false</span>
-<span class="hljs-number">5</span>==<span class="hljs-literal">undefined</span>; <span class="hljs-comment">//false</span>
<span class="hljs-comment">//undefined就不是数字，跟数字没有可比性</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，我猜肯定有人会说——“不对啊，Blue，null的type才是Object啊”，这个简单，因为<strong>js里充满了作者的主观规定，仅此而已</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//null的类型是object，没错</span>
<span class="hljs-keyword">typeof</span> <span class="hljs-literal">null</span>; <span class="hljs-comment">//"object"</span>

<span class="hljs-comment">//但这只是作者硬性规定null的类型罢了</span>
<span class="hljs-comment">//不然怎么解释</span>
<span class="hljs-number">12</span>+<span class="hljs-literal">null</span>  <span class="hljs-comment">//12</span>
<span class="hljs-number">5</span>-<span class="hljs-literal">null</span>  <span class="hljs-comment">//5</span>
<span class="hljs-number">8</span>*<span class="hljs-literal">null</span>  <span class="hljs-comment">//0</span>
<span class="hljs-number">19</span>&<span class="hljs-literal">null</span> <span class="hljs-comment">//0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-10">有讲解有应用，完美</h1>
<p>通过上面我们基本弄明白了null和undefined，那有没有什么使用上的区别呢？不多，但是有</p>
<h2 data-id="heading-11">默认参数与undefined、null</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//age参数有默认值——也就是说，不传就是18</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">blue</span>(<span class="hljs-params">age=<span class="hljs-number">18</span></span>)</span>&#123;
  <span class="hljs-built_in">console</span>.log(age);
&#125;


<span class="hljs-comment">//传个undefined跟没传一样，系统认为“没有”和undefined等价</span>
blue(<span class="hljs-literal">undefined</span>);  <span class="hljs-comment">//18</span>

<span class="hljs-comment">//传null就是有了，不会触发默认值</span>
blue(<span class="hljs-literal">null</span>);  <span class="hljs-comment">//null</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">解构赋值与undefined、null</h2>
<p>类似于参数，其实解构赋值也有类似的情况</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> [a=<span class="hljs-number">1</span>,b=<span class="hljs-number">2</span>]=[<span class="hljs-literal">undefined</span>, <span class="hljs-literal">null</span>];

<span class="hljs-comment">//undefined就是没给——触发默认值</span>
<span class="hljs-built_in">console</span>.log(a);  <span class="hljs-comment">//1</span>

<span class="hljs-comment">//null是给了，但是空——不触发默认值</span>
<span class="hljs-built_in">console</span>.log(b);  <span class="hljs-comment">//null</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-13">总结</h1>
<p>是时候梳理一遍Blue讲过的东西了，那么首先</p>
<p><img alt="15-三连" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e13ef6e64254455fb9b1ccb3156b145b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li><code>null</code>是主动使用，<code>undefined</code>是被动的备选手段</li>
<li><code>null</code>本质上是零，<code>undefined</code>本质上是个对象（js作者规定了type而已）</li>
<li>判断<code>null</code>和<code>undefined</code>时，应永远使用严格判断（===）</li>
<li>js中“没有传”、“没有给”和<code>undefined</code>基本等价；而<code>null</code>是有值的——例如：默认参数</li>
</ul>
<h2 data-id="heading-14">有bug？想补充？</h2>
<p>感谢大家观看这篇教程，有任何问题或想和Blue交流，请直接留言，发现文章有任何不妥之处，也请指出，提前感谢</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            