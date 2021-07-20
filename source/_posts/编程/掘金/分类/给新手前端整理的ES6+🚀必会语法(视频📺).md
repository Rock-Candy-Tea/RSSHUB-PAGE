
---
title: '给新手前端整理的ES6+🚀必会语法(视频📺)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dafe8a507b9b49f6884d7a1969da8e77~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 19 Jul 2021 17:11:09 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dafe8a507b9b49f6884d7a1969da8e77~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>下面都是开发<strong>🔥必用</strong>的语法.</p>
<h2 data-id="heading-0">let</h2>
<p>定义变量, 区别于"var", 他所声明的变量只在"let"所在的代码块内有效, 总之一句话: "var"就不要用了, 都替换成"let".</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
  <span class="hljs-keyword">let</span> a = <span class="hljs-number">10</span>;
  <span class="hljs-keyword">var</span> b = <span class="hljs-number">1</span>;
&#125;

a <span class="hljs-comment">// ReferenceError: a is not defined.</span>
b <span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">const</h2>
<p>定义常量, 定义后的变量不可修改</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> PI = <span class="hljs-number">3.1415</span>;
PI <span class="hljs-comment">// 3.1415</span>

PI = <span class="hljs-number">3</span>;
<span class="hljs-comment">// TypeError: Assignment to constant variable.</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">数组解构赋值</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> [a, b, c] = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];

<span class="hljs-comment">// 等价</span>
<span class="hljs-keyword">let</span> a = <span class="hljs-number">1</span>;
<span class="hljs-keyword">let</span> b = <span class="hljs-number">2</span>;
<span class="hljs-keyword">let</span> c = <span class="hljs-number">3</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">对象的解构赋值</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> &#123; foo, bar &#125; = &#123; <span class="hljs-attr">foo</span>: <span class="hljs-string">'aaa'</span>, <span class="hljs-attr">bar</span>: <span class="hljs-string">'bbb'</span> &#125;;
foo <span class="hljs-comment">// "aaa"</span>
bar <span class="hljs-comment">// "bbb"</span>

<span class="hljs-keyword">let</span> &#123; x, y, ...z &#125; = &#123; <span class="hljs-attr">x</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">y</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">a</span>: <span class="hljs-number">3</span>, <span class="hljs-attr">b</span>: <span class="hljs-number">4</span> &#125;;
x <span class="hljs-comment">// 1</span>
y <span class="hljs-comment">// 2</span>
z <span class="hljs-comment">// &#123; a: 3, b: 4 &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">函数参数的解构赋值</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">[x, y]</span>)</span>&#123;
  <span class="hljs-keyword">return</span> x + y;
&#125;
add([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>]); <span class="hljs-comment">// 3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">move</span>(<span class="hljs-params">&#123;x, y&#125; = &#123; x: <span class="hljs-number">0</span>, y: <span class="hljs-number">0</span> &#125;</span>) </span>&#123;
  <span class="hljs-keyword">return</span> [x, y];
&#125;
move(&#123;<span class="hljs-attr">x</span>: <span class="hljs-number">3</span>, <span class="hljs-attr">y</span>: <span class="hljs-number">8</span>&#125;); <span class="hljs-comment">// [3, 8]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">模板字符串</h2>
<p>字符串中可以优雅的插入变量.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> a = <span class="hljs-string">'你好'</span>;
<span class="hljs-keyword">const</span> b = <span class="hljs-string">`<span class="hljs-subst">$&#123;a&#125;</span> Vue`</span>;
<span class="hljs-comment">// b == '你好vue'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">函数参数默认值</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">a,b=<span class="hljs-number">1</span></span>)</span>&#123;
<span class="hljs-keyword">return</span> a+b;
&#125;

add(<span class="hljs-number">3</span>) <span class="hljs-comment">// 4</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">箭头函数</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">a</span>(<span class="hljs-params"></span>)</span>&#123;
<span class="hljs-keyword">return</span> <span class="hljs-string">'你好'</span>
&#125;

<span class="hljs-comment">// 箭头函数</span>
<span class="hljs-keyword">const</span> a = <span class="hljs-function">()=></span>&#123;
<span class="hljs-keyword">return</span> <span class="hljs-string">'你好'</span>;
&#125;

<span class="hljs-comment">// 还可以更简单</span>
<span class="hljs-keyword">const</span> a = <span class="hljs-function">()=></span><span class="hljs-string">'你好'</span>


<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">数组的扩展运算符</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 等价于 console.log(1,2,3);</span>
<span class="hljs-built_in">console</span>.log(...[<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]);

<span class="hljs-comment">// 合并数组</span>
<span class="hljs-keyword">const</span> a = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>];
<span class="hljs-keyword">const</span> b = [...a,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>]; <span class="hljs-comment">// [1,2,3,4,5]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">对象属性的简洁表示法</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> a = <span class="hljs-number">1</span>;

<span class="hljs-keyword">const</span> obj = &#123;<span class="hljs-attr">a</span>: <span class="hljs-number">1</span>&#125;;
<span class="hljs-comment">// 简写</span>
<span class="hljs-keyword">const</span> obj = &#123;a&#125;;  <span class="hljs-comment">// &#123;a: 1&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">对象方法的简洁表示法</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> obj = &#123;
  <span class="hljs-attr">say</span>:<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">'你好!'</span>;
  &#125;
&#125;; 
<span class="hljs-comment">// 简写,可以省略":function"</span>
<span class="hljs-keyword">const</span> obj = &#123;
  say ()&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">'你好!'</span>;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">对象属性名表达式</h2>
<p>对象的属性名可以支持变量.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> a = <span class="hljs-string">'abc'</span>;
<span class="hljs-keyword">let</span> obj = &#123;&#125;;
obj[<span class="hljs-string">`<span class="hljs-subst">$&#123;a&#125;</span>123`</span>] = <span class="hljs-number">1</span>;
<span class="hljs-built_in">console</span>.log(obj) <span class="hljs-comment">// &#123;abc123:1&#125;;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">链判断运算符(?)</h2>
<p>实现对"<strong>?</strong>"左边的表达式是否为null或者undefined的判断, 如果是立即停止判断, 返回undefined或null.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> firstName = (message
  && message.body
  && message.body.user
  && message.body.user.firstName);

<span class="hljs-comment">// 简写</span>
<span class="hljs-keyword">const</span> fristName = message?.body?.user?.firstName;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">Null判断运算符(??)</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">console</span>.log(<span class="hljs-number">0</span> ?? <span class="hljs-number">1</span>); <span class="hljs-comment">// 0</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-literal">false</span> ?? <span class="hljs-number">1</span>); <span class="hljs-comment">// false</span>

<span class="hljs-built_in">console</span>.log(<span class="hljs-literal">undefined</span> ?? <span class="hljs-number">1</span>); <span class="hljs-comment">// 1</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-literal">null</span> ?? <span class="hljs-number">1</span>); <span class="hljs-comment">// 1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很显然只有"??"前面的值是null或undefined才返回"??"后面的值.</p>
<h2 data-id="heading-14"></h2>
<h2 data-id="heading-15">Promise</h2>
<p>Promise 是异步编程的一种解决方案，比传统的解决方案"回调函数和事件"更合理.
在这里大概了解下即可, 主要是为了讲解后面的"<strong>async/await</strong>", 因为在开发中我们使用的第三方插件很多都是封装成Promise格式的, 初期需要自己封装的需求很少.</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 封装代码成Promise格式</span>
<span class="hljs-keyword">const</span> promiseA = <span class="hljs-function">()=></span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">resolve, reject</span>) </span>&#123;
  
  <span class="hljs-comment">// === 你的代码 ===</span>
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-number">0.5</span> < <span class="hljs-built_in">Math</span>.random())&#123;
    resolve(<span class="hljs-string">'成功'</span>);
    &#125; <span class="hljs-keyword">else</span> &#123;
    reject(<span class="hljs-string">'失败'</span>);
    &#125;
&#125;,<span class="hljs-number">200</span>);
  <span class="hljs-comment">// === 你的代码 ===</span>
  
&#125;);

<span class="hljs-comment">// 执行</span>
promiseA().then(<span class="hljs-function"><span class="hljs-params">value</span>=></span>&#123;
<span class="hljs-comment">// '成功' == value</span>
  <span class="hljs-built_in">console</span>.log(value);
&#125;).catch(<span class="hljs-function"><span class="hljs-params">error</span>=></span>&#123;
<span class="hljs-comment">// '失败' == error</span>
  <span class="hljs-built_in">console</span>.log(error);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">async/await</h2>
<p>执行Promise函数"更优雅". 用上面封装"promiseA函数"为例:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">funA</span>(<span class="hljs-params"></span>)</span>&#123;
  promiseA().then(<span class="hljs-function"><span class="hljs-params">value</span>=></span>&#123;
    <span class="hljs-built_in">console</span>.log(value);
  &#125;).catch(<span class="hljs-function"><span class="hljs-params">error</span>=></span>&#123;
    <span class="hljs-built_in">console</span>.log(error);
  &#125;);
&#125;

<span class="hljs-comment">// 改写, 需要用try/catch来捕获"reject"触发的异常</span>
<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">funA</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">try</span>&#123;
    <span class="hljs-keyword">const</span> value = <span class="hljs-keyword">await</span> promiseA();
    <span class="hljs-built_in">console</span>.log(value);
  &#125; <span class="hljs-keyword">catch</span>(error)&#123;
    <span class="hljs-built_in">console</span>.log(error);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">更多</h2>
<p>在这里我只是给大家讲解了几个常用的语法, 更多请参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fes6.ruanyifeng.com%2F%23docs%2Flet" target="_blank" rel="nofollow noopener noreferrer" title="https://es6.ruanyifeng.com/#docs/let" ref="nofollow noopener noreferrer">阮一峰老师的教程</a>
​</p>
<h2 data-id="heading-18">⚡ 在线视频</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1Yw411o7gc%3Fp%3D4" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1Yw411o7gc?p=4" ref="nofollow noopener noreferrer">www.bilibili.com/video/BV1Yw…</a></p>
<h2 data-id="heading-19">微信群</h2>
<p>感谢大家的阅读, 如有疑问可以加我微信, 我拉你进入<strong>微信群</strong>(由于腾讯对微信群的200人限制, 超过200人后必须由群成员拉入)</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dafe8a507b9b49f6884d7a1969da8e77~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            