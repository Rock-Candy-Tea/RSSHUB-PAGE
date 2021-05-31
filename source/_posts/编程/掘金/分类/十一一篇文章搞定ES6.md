
---
title: '十一.一篇文章搞定ES6'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3684'
author: 掘金
comments: false
date: Thu, 27 May 2021 09:08:29 GMT
thumbnail: 'https://picsum.photos/400/300?random=3684'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><h2 data-id="heading-0">一.let 和 const 命令</h2>
<blockquote>
<ul>
<li>let和const都能够声明块级作用域，用法和var是类似的，let的特点是不会变量提升，而是被锁在当前块中。</li>
<li>const 声明的就是常量，保证<code>指针是固定</code>的;</li>
<li>
<ul>
<li>1.使用 const 声明常量，一旦声明，就必须<code>立即初始化</code>，不能留到以后赋值</li>
</ul>
</li>
<li>
<ul>
<li>2.const 声明的常量，允许在<strong>不重新赋值</strong>的情况下修改它的值,所以基本数据类型是不能修改，但是引用数据类型是可以修改的。</li>
</ul>
</li>
<li>
<ul>
<li>3.不知道用 let 和 const 优先用 const。</li>
</ul>
</li>
<li>
<ul>
<li><strong>详细解读</strong>const 其实保证的不是变量的值不变，而是保证变量指向的<code>内存地址</code>所保存的数据不允许改动，对于简单类型（数值 number、字符串 string 、布尔值 boolean）,值就保存在变量指向的那个内存地址，因此 const 声明的简单类型变量等同于常量。而复杂类型（对象 object，数组 array，函数 function），变量指向的内存地址其实是保存了一个指向实际数据的指针，所以 const 只能保证指针是固定的，至于指针指向的数据结构变不变就无法控制了，所以使用 const 声明复杂类型对象时要慎重。</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> person = &#123; <span class="hljs-attr">username</span>: <span class="hljs-string">'Alex'</span> &#125;;
  <span class="hljs-comment">// person = &#123;&#125;;报错</span>
  person.username = <span class="hljs-string">'ZhangSan'</span>;<span class="hljs-comment">//不报错 </span>
 <span class="hljs-built_in">console</span>.log(person);
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<p><strong>let、const 与 var 的区别:</strong></p>
<blockquote>
<p>1.重复声明</p>
<ul>
<li>var 允许重复声明，let、const 不允许</li>
</ul>
<p>2.变量提升</p>
<ul>
<li>var 会提升变量的声明到当前作用域的顶部</li>
<li>let、const 不存在变量提升</li>
</ul>
<p>3.暂时性死区</p>
<ul>
<li>只要作用域内存在 let、const，它们所声明的变量或常量就自动“绑定”这个区域，不再受到外部作用域的影响</li>
<li>let、const 存在暂时性死区</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> name=<span class="hljs-string">'jack'</span>;
&#123;
 name=<span class="hljs-string">'bob'</span>;
 <span class="hljs-keyword">let</span> name;    <span class="hljs-comment">//Uncaught ReferenceError: Cannot access 'name' before initialization</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>ES6 中,如果区块中存在 let 和 const 命令，这个区块对这些命令声明的变量，从一开始就形成了封闭作用域。因为JS清楚地感知到了 name 是用 let 声明在当前这个代码块内的，所以会给这个变量 name 加上了暂时性死区的限制，它就不往外探出头了。<br></li>
<li>那么，如果我们把上面的let name;去掉，程序也将正常运行， name 的值也被成功修改为了bob，就是正常地按照作用域链的规则，向外探出头去了。</li>
</ul>
<p>4.window 对象的属性和方法:</p>
<blockquote>
<p>全局作用域中，var 声明的变量，以及通过 function 声明的函数，会自动变成 window 对象的属性或方法,let、const 不会。</p>
</blockquote>
<p>5.块级作用域</p>
<blockquote>
<p>var 没有块级作用域，let/const 有块级作用域。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">&#123;&#125;
<span class="hljs-keyword">for</span>()&#123;&#125;
<span class="hljs-keyword">while</span>()&#123;&#125;
<span class="hljs-keyword">do</span>&#123;&#125;<span class="hljs-keyword">while</span>()
<span class="hljs-keyword">if</span>()&#123;&#125;
<span class="hljs-keyword">switch</span>()&#123;&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125;<span class="hljs-comment">//函数只有在执行时才生成函数作用域</span>
<span class="hljs-keyword">const</span> person = &#123;
        <span class="hljs-attr">getAge</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;&#125;
     &#125;;<span class="hljs-comment">//对象没有块级作用域</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<h3 data-id="heading-1">小题：点击哪个按钮就显示当前索引</h3>
<p>方案一：行不通</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"ie=edge"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>let 和 const 的应用<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
      <span class="hljs-selector-tag">body</span> &#123;
        <span class="hljs-attribute">padding</span>: <span class="hljs-number">50px</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">150px</span>;
      &#125;

      <span class="hljs-selector-class">.btn</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">margin-right</span>: <span class="hljs-number">20px</span>;
        <span class="hljs-attribute">font-size</span>: <span class="hljs-number">80px</span>;
        <span class="hljs-attribute">cursor</span>: pointer;
      &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn"</span>></span>0<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn"</span>></span>1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn"</span>></span>2<span class="hljs-tag"></<span class="hljs-name">button</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
      <span class="hljs-keyword">var</span> btns = <span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">".btn"</span>);
      <span class="hljs-comment">// 方案一：不行（var）</span>

      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < btns.length; i++) &#123;
        <span class="hljs-comment">/*
       首先： 进来就一轮循环
        i=0，按钮0绑定事件
        i=1，按钮1绑定事件
        i=2，按纽2绑定事件
        i=3，不绑定了
        所以，i=3了
        然后：点击任何一个按钮都会打印3
        */</span>
        btns[i].addEventListener(
          <span class="hljs-string">"click"</span>,
          <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            <span class="hljs-built_in">console</span>.log(i); <span class="hljs-comment">//3</span>
          &#125;,
          <span class="hljs-literal">false</span>
        );
      &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>方案二：可行(立即执行)</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> btns = <span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">".btn"</span>);

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < btns.length; i++) &#123;
  (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">index</span>) </span>&#123;
    btns[index].addEventListener(
      <span class="hljs-string">"click"</span>,
      <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(index);
      &#125;,
      <span class="hljs-literal">false</span>
    );
  &#125;)(i);
&#125;
<span class="hljs-comment">/*
for循环遍历的过程中，立即执行函数会形成三个作用域，同时会将i=0，1，2分别传入到函数作用域中，
以index=0，1，2的形式存入，当用户点击按钮时，就会打印相应的数字。
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>方案三：可行(let)</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> btns = <span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">".btn"</span>);

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < btns.length; i++) &#123;
  btns[i].addEventListener(
    <span class="hljs-string">"click"</span>,
    <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-built_in">console</span>.log(i);
    &#125;,
    <span class="hljs-literal">false</span>
  );
&#125;
<span class="hljs-comment">/*
1.循环遍历会创建三个块级作用域，
2.点击事件会在当前的块级作用域内创建函数作用域，同时触发函数打印i
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">二.模板字符串</h2>
<ul>
<li>1.模板字符串相当于加强版的字符串，用反引号 `,除了作为普通字符串，还可以用来定义多行字符串，还可以在字符串中加入变量和表达式</li>
<li>2.模板字符串中，所有的空格、换行或缩进都会被保留在输出之中</li>
<li>3.模板字符串的注入
<strong>只要最终可以得出一个值的就可以通过 $&#123;&#125; 注入到模板字符串中</strong></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> username = <span class="hljs-string">"alex"</span>;
<span class="hljs-keyword">const</span> person = &#123; <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>, <span class="hljs-attr">sex</span>: <span class="hljs-string">"male"</span> &#125;;
<span class="hljs-keyword">const</span> getSex = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">sex</span>) </span>&#123;
  <span class="hljs-keyword">return</span> sex === <span class="hljs-string">"male"</span> ? <span class="hljs-string">"男"</span> : <span class="hljs-string">"女"</span>;
&#125;;
<span class="hljs-keyword">const</span> info = <span class="hljs-string">`<span class="hljs-subst">$&#123;username&#125;</span>, <span class="hljs-subst">$&#123;person.age + <span class="hljs-number">2</span>&#125;</span>, <span class="hljs-subst">$&#123;getSex(person.sex)&#125;</span>`</span>;
<span class="hljs-built_in">console</span>.log(info);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">三.箭头函数</h2>
<h3 data-id="heading-4">1.箭头函数的结构</h3>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">const</span>/<span class="hljs-keyword">let</span> 函数名 = 参数 => 函数体
      <span class="hljs-keyword">const</span> add = <span class="hljs-function">() =></span> &#123;&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">2.箭头函数简化</h3>
<pre><code class="hljs language-js copyable" lang="js">- 单个参数可以省略圆括号
  <span class="hljs-keyword">const</span> add = <span class="hljs-function"><span class="hljs-params">x</span> =></span> &#123;&#125;;
- 单行函数体可以省略花括号以及 <span class="hljs-keyword">return</span>
  <span class="hljs-keyword">const</span> add = <span class="hljs-function">(<span class="hljs-params">x, y</span>) =></span> x + y;
- 如果箭头函数返回单行对象，可以在 &#123;&#125; 外面加上 ()，让浏览器不再认为那是函数体的花括号
  <span class="hljs-keyword">const</span> add = <span class="hljs-function">(<span class="hljs-params">x, y</span>) =></span> ( &#123;<span class="hljs-attr">value</span>: x + y&#125; );
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">3.this 指向</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-number">1.</span>全局作用域中的 <span class="hljs-built_in">this</span> 指向
     <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>); <span class="hljs-comment">// window</span>

<span class="hljs-number">2.</span>一般函数（非箭头函数）中的 <span class="hljs-built_in">this</span> 指向
      <span class="hljs-comment">// 'use strict';</span>
      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>); 
        <span class="hljs-comment">// 严格模式就指向 undefined</span>
        <span class="hljs-comment">// undefined->window（非严格模式下）</span>
      &#125;
      add();
     
     
<span class="hljs-number">3.</span>点击事件的<span class="hljs-built_in">this</span>指向
      <span class="hljs-built_in">document</span>.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
         <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>);  <span class="hljs-comment">//this指向document</span>
       &#125;;
   
      <span class="hljs-comment">// 只有在函数调用的时候 this 指向才确定，不调用的时候，不知道指向谁</span>
      <span class="hljs-comment">// this 指向和函数在哪儿调用没关系，只和谁在调用有关</span>
      <span class="hljs-comment">// 没有具体调用对象的话，this 指向 undefined，在非严格模式下，转向 window</span>
      
<span class="hljs-number">4.</span>箭头函数中的 <span class="hljs-built_in">this</span> 指向
    箭头函数没有自己的 <span class="hljs-built_in">this</span>，所以会一层一层的往外找，最后找到<span class="hljs-built_in">window</span>，他的<span class="hljs-built_in">this</span>指向<span class="hljs-built_in">window</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">4.不适用箭头函数的场景</h3>
<ul>
<li>1.箭头函数不能作为构造函数</li>
<li>2.需要 this 指向调用对象的时候，不能用箭头函数
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-built_in">document</span>.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>);
  &#125;;
  <span class="hljs-built_in">document</span>.addEventListener(
    <span class="hljs-string">'click'</span>,
    <span class="hljs-function">() =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>); <span class="hljs-comment">//window</span>
    &#125;,
    <span class="hljs-literal">false</span>
  );
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>3.需要使用 arguments 的时候
箭头函数中没有 arguments</li>
</ul>
<h3 data-id="heading-8">5.箭头函数的应用（3-11）</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>箭头函数的应用<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
      <span class="hljs-selector-tag">body</span> &#123;
        <span class="hljs-attribute">padding</span>: <span class="hljs-number">50px</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">250px</span>;
        <span class="hljs-attribute">font-size</span>: <span class="hljs-number">30px</span>;
      &#125;

      <span class="hljs-selector-id">#btn</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">margin-right</span>: <span class="hljs-number">20px</span>;
        <span class="hljs-attribute">font-size</span>: <span class="hljs-number">30px</span>;
        <span class="hljs-attribute">cursor</span>: pointer;
      &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"btn"</span>></span>开始<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"result"</span>></span>0<span class="hljs-tag"></<span class="hljs-name">span</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
      <span class="hljs-keyword">const</span> btn = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"btn"</span>);
      <span class="hljs-keyword">const</span> result = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"result"</span>);
      <span class="hljs-keyword">const</span> timer = &#123;
        <span class="hljs-attr">time</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">start</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
          <span class="hljs-comment">// this</span>
          btn.addEventListener(
            <span class="hljs-string">"click"</span>,
            <span class="hljs-function">() =></span> &#123;
              <span class="hljs-comment">// this</span>
              <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">() =></span> &#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>);
                <span class="hljs-built_in">this</span>.time++;
                result.innerHTML = <span class="hljs-built_in">this</span>.time;
              &#125;, <span class="hljs-number">1000</span>);
            &#125;,
            <span class="hljs-literal">false</span>
          );
        &#125;,
      &#125;;

      timer.start();
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">四.解构赋值</h2>
<blockquote>
<p>解构赋值是指解析某一数据的结构，将我们想要的东西提取出来，赋值给变量或常量；</p>
</blockquote>
<h3 data-id="heading-10">4.1 数组解构赋值</h3>
<blockquote>
<p>数组解构赋值非常简单，遵循模式匹配原则就可以了，如果不需要结构的用逗号跳过即可。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">   <span class="hljs-comment">//   1.模式（结构）匹配</span>
       [] = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];

   <span class="hljs-comment">//    2.索引值相同的完成赋值</span>
       <span class="hljs-keyword">const</span> [a, b, c] = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
       <span class="hljs-built_in">console</span>.log(a, b, c);

  <span class="hljs-comment">//     3.不取的，可以直接用逗号跳过</span>
      <span class="hljs-keyword">const</span> [a, [, , b], c] = [<span class="hljs-number">1</span>, [<span class="hljs-number">2</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>], <span class="hljs-number">3</span>];
      <span class="hljs-built_in">console</span>.log(a, b, c);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">4.1.1 默认值:</h4>
<blockquote>
<ul>
<li>1.只有当一个数组成员严格等于（===）undefined 时，对应的默认值才会生效</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">const</span> [a = <span class="hljs-number">1</span>, b = <span class="hljs-number">2</span>] = [<span class="hljs-number">3</span>, <span class="hljs-number">0</span>];<span class="hljs-comment">//3 0</span>
 <span class="hljs-keyword">const</span> [a = <span class="hljs-number">1</span>, b = <span class="hljs-number">2</span>] = [<span class="hljs-number">3</span>, <span class="hljs-literal">null</span>]; <span class="hljs-number">3</span> <span class="hljs-literal">null</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>2.如果默认值是表达式，默认值表达式是惰性求值的</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">const</span> func = <span class="hljs-function">() =></span> &#123;
       <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"我被执行了"</span>);
      <span class="hljs-keyword">return</span> <span class="hljs-number">2</span>;
   &#125;;
  <span class="hljs-comment">// const [x = func()] = [1]; // x=1 且不执行函数</span>
 <span class="hljs-keyword">const</span> [x = func()] = []; <span class="hljs-comment">//执行函数体代码</span>
<span class="hljs-built_in">console</span>.log(x); <span class="hljs-comment">//2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<h4 data-id="heading-12">4.1.2 应用</h4>
<ul>
<li>1.常见的类数组的解构赋值</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//arguments</span>
<span class="hljs-keyword">const</span> [a, b] = <span class="hljs-built_in">arguments</span>;
<span class="hljs-built_in">console</span>.log(a, b);

<span class="hljs-comment">//NodeList</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">'p'</span>));
 <span class="hljs-keyword">const</span> [p1, p2, p3] = <span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">'p'</span>);
 <span class="hljs-built_in">console</span>.log(p1, p2, p3);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>2.函数参数的解构赋值</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">let</span> [x, y] = [<span class="hljs-number">1</span>, <span class="hljs-number">1</span>];
      <span class="hljs-keyword">const</span> add = <span class="hljs-function">(<span class="hljs-params">[x = <span class="hljs-number">0</span>, y = <span class="hljs-number">0</span>]</span>) =></span> x + y;
      <span class="hljs-built_in">console</span>.log(add([x, y]));
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>3.交换变量的值</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">let</span> x = <span class="hljs-number">1</span>;
      <span class="hljs-keyword">let</span> y = <span class="hljs-number">2</span>;
<span class="hljs-comment">/*
       之前的做法
       let tmp = x;
       x = y;
       y = tmp;
       console.log(x, y);
*/</span>
       [x, y] = [y, x];
      <span class="hljs-built_in">console</span>.log(x, y);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">4.2 对象解构赋值</h3>
<h4 data-id="heading-14">4.2.1 基本结构</h4>
<pre><code class="copyable">1.模式（结构）匹配
       &#123;&#125;=&#123;&#125;
       
2.属性名相同的完成赋值
  const &#123; age, username &#125; = &#123; username: 'Alex', age: 18 &#125;;
  const &#123; age: age, username: username &#125; = &#123; username: 'Alex', age: 18 &#125;;
  
3.可以取别名
      const &#123; age: age, username: uname &#125; = &#123; username: 'Alex', age: 18 &#125;;
      console.log(age, uname);//解构赋值之后再赋值给uname
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">4.2.2 默认值</h4>
<ul>
<li>默认值(=)的生效条件
对象的属性值严格等于 undefined 时，对应的默认值才会生效
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">const</span> &#123; age = <span class="hljs-number">16</span>, <span class="hljs-attr">username</span>: uname &#125; = &#123; <span class="hljs-attr">username</span>: <span class="hljs-string">"Alex"</span> &#125;;
    <span class="hljs-built_in">console</span>.log(age, uname);<span class="hljs-comment">//16 alex</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<ul>
<li>
<p>2.默认值表达式是惰性求值的</p>
</li>
<li>
<p>3.将一个已经声明的变量用于解构赋值
如果将一个已经声明的变量用于对象的解构赋值，整个赋值需在圆括号中进行，防止被当成块级作用域</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">let</span> x = <span class="hljs-number">2</span>;
(&#123; x &#125; = &#123; <span class="hljs-attr">x</span>: <span class="hljs-number">1</span> &#125;);
<span class="hljs-built_in">console</span>.log(x);    <span class="hljs-comment">//1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-16">4.2.3 对象解构赋值的应用</h4>
<ul>
<li>1.函数参数的解构赋值</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">     <span class="hljs-keyword">const</span> PersonInfo = <span class="hljs-function">(<span class="hljs-params">user</span>) =></span> <span class="hljs-built_in">console</span>.log(user.username, user.age);
     PersonInfo((&#123; age, <span class="hljs-attr">username</span>: username &#125; = &#123; <span class="hljs-attr">username</span>: <span class="hljs-string">"alex"</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">18</span> &#125;)); <span class="hljs-comment">//alex 18 使用了解构后的值</span>
     
     <span class="hljs-keyword">const</span> person = <span class="hljs-function">(<span class="hljs-params">&#123; age = <span class="hljs-number">0</span>, username = <span class="hljs-string">"ZhangSan"</span> &#125;</span>) =></span><span class="hljs-built_in">console</span>.log(username, age);
     person(&#123;&#125;); <span class="hljs-comment">//ZhangSan 0  使用了默认值</span>
     person(&#123; <span class="hljs-attr">username</span>: <span class="hljs-string">"alex"</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">18</span> &#125;); <span class="hljs-comment">//alex 18 使用了解构后的值</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>2.复杂的嵌套</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">const</span> obj = &#123;
        <span class="hljs-attr">x</span>: <span class="hljs-number">1</span>,
        <span class="hljs-attr">y</span>: [<span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>],
        <span class="hljs-attr">z</span>: &#123;
          <span class="hljs-attr">a</span>: <span class="hljs-number">5</span>,
          <span class="hljs-attr">b</span>: <span class="hljs-number">6</span>,
        &#125;,
      &#125;;
      <span class="hljs-keyword">const</span> &#123; x, y, z &#125; = obj;
      <span class="hljs-built_in">console</span>.log(x, y, z);<span class="hljs-comment">//  1   [2,3,4]  &#123;a:5,b:6&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">const</span> obj = &#123;
        <span class="hljs-attr">x</span>: <span class="hljs-number">1</span>,
        <span class="hljs-attr">y</span>: [<span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>],
        <span class="hljs-attr">z</span>: &#123;
          <span class="hljs-attr">a</span>: <span class="hljs-number">5</span>,
          <span class="hljs-attr">b</span>: <span class="hljs-number">6</span>,
        &#125;,
      &#125;;
      <span class="hljs-keyword">const</span> &#123;
        y,
        <span class="hljs-attr">y</span>: [, yy],
        z,
        <span class="hljs-attr">z</span>: &#123; b &#125;,
      &#125; = obj;
      <span class="hljs-built_in">console</span>.log(yy, y, z, b); <span class="hljs-comment">//3   [2,3,4]  &#123;a:5,b:6&#125; 6</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">4.3 字符串的解构赋值</h3>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-comment">// 字符串可以按照数组形式的解构赋值</span>
      <span class="hljs-keyword">const</span> [a, b, , , c] = <span class="hljs-string">"hello"</span>;
      <span class="hljs-built_in">console</span>.log(a, b, c); <span class="hljs-comment">//h e o</span>
      
      <span class="hljs-comment">// 字符串可以按照对象形式的解构赋值（可以按照索引值和length）</span>
      <span class="hljs-keyword">const</span> &#123; <span class="hljs-number">0</span>: d, <span class="hljs-number">1</span>: e, length &#125; = <span class="hljs-string">"hello"</span>;
      <span class="hljs-built_in">console</span>.log(d, e, length); <span class="hljs-comment">//h e 5</span>
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"hello"</span>.length); <span class="hljs-comment">//5</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">五.对象字面量增强</h2>
<h3 data-id="heading-19">5.1 属性简写</h3>
<blockquote>
<p>ES6 允许在大括号里面，直接写入变量和函数，作为对象的属性和方法。这样的书写更加简洁。</p>
<blockquote>
<p>键名和变量或常量名一样的时候，可以只写一个</p>
<pre><code class="hljs language-js copyable" lang="js">   <span class="hljs-keyword">const</span> age = <span class="hljs-number">18</span>;
      <span class="hljs-keyword">const</span> person = &#123;
          <span class="hljs-comment">// age: age日常写法</span>
      age  <span class="hljs-comment">//简洁写法</span>
   &#125;;
     <span class="hljs-built_in">console</span>.log(person);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>方法可以省略冒号和 function 关键字</p>
<pre><code class="hljs language-js copyable" lang="js">     <span class="hljs-keyword">const</span> person = &#123;
       <span class="hljs-comment">// speak: function () &#123;&#125;之前写法</span>
      <span class="hljs-function"><span class="hljs-title">speak</span>(<span class="hljs-params"></span>)</span> &#123;&#125;<span class="hljs-comment">//简洁表示法</span>
     &#125;;
     <span class="hljs-built_in">console</span>.log(person);
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
</blockquote>
<h3 data-id="heading-20">5.2.方括号语法增强</h3>
<blockquote>
<p>1.方括号语法可以写在对象字面量中</p>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">const</span> prop = <span class="hljs-string">'age'</span>;
      <span class="hljs-keyword">const</span> person = &#123;
        [prop]: <span class="hljs-number">18</span>
      &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.方括号中可以放什么?</p>
<blockquote>
<ul>
<li>$&#123;&#125;</li>
<li>[值或通过计算可以得到值的（表达式）]</li>
</ul>
</blockquote>
<p>3.方括号语法和点语法的区别:</p>
<blockquote>
<pre><code class="copyable"> 点语法是方括号语法的特殊形式
 const person = &#123;&#125;;
 person.age 等价于 person['age']
 属性名由数字、字母、下划线以及 $ 构成，并且数字还不能打头的时候可以使用点语
 合法标识符可以用来作为变量或常量名
 当你的属性或方法名是合法标识符时，可以使用点语法，其他情况下请使用方括号语法
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
</blockquote>
<h2 data-id="heading-21">六.函数参数默认值</h2>
<blockquote>
<ul>
<li>调用函数的时候传参了，就用传递的参数；如果没传参，或者明确的传递 undefined 作为参数，就用默认值；</li>
<li>接收很多参数的时候,接收一个对象作为参数</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> logUser = <span class="hljs-function">(<span class="hljs-params">&#123; username = <span class="hljs-string">'zhangsan'</span>, age = <span class="hljs-number">0</span>, sex = <span class="hljs-string">'male'</span> &#125; = &#123;&#125;</span>) =></span>
<span class="hljs-built_in">console</span>.log(username, age, sex);
logUser();
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<h2 data-id="heading-22">七.剩余参数与展开运算符</h2>
<p>剩余/扩展运算符同样也是ES6一个非常重要的语法，使用3个点（...），后面跟着一个含有iterator接口的数据结构</p>
<h3 data-id="heading-23">7.1 剩余参数</h3>
<blockquote>
<ul>
<li>剩余参数语法允许将不确定数量的参数表示为数组。</li>
<li>剩余参数永远是个数组，即使没有值，也是空数组.</li>
<li>剩余参数只能是最后一个参数，之后不能再有其他参数，否则会报错</li>
<li>剩余参数不一定非要作为函数参数使用</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">     <span class="hljs-keyword">const</span> add = <span class="hljs-function">(<span class="hljs-params">x, y, ...args</span>) =></span> &#123;
       <span class="hljs-built_in">console</span>.log(x, y, args);
     &#125;;
     add(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>); <span class="hljs-comment">//1 2  [3, 4, 5]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<h4 data-id="heading-24">7.1.1 箭头函数的剩余参数</h4>
<blockquote>
<blockquote>
<blockquote>
<p>对于箭头函数来说，没有 arguments，使用剩余参数替代 arguments 获取实际参数，此时不能省略圆括号；</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> add = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;
<span class="hljs-built_in">console</span>.log(args);
&#125;;
add(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
</blockquote>
</blockquote>
<h4 data-id="heading-25">7.1.2  剩余参数的应用</h4>
<ul>
<li>1.完成 add 函数</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">const</span> add = <span class="hljs-function">(<span class="hljs-params">...args</span>) =></span> &#123;
         <span class="hljs-keyword">let</span> sum = <span class="hljs-number">0</span>;

         <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < args.length; i++) &#123;
           sum += args[i];
         &#125;

       <span class="hljs-keyword">return</span> sum;
       &#125;;

       <span class="hljs-built_in">console</span>.log(add(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>2.与解构赋值结合使用
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">const</span> [num, ...args] = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>];
    <span class="hljs-keyword">const</span> func = <span class="hljs-function">(<span class="hljs-params">&#123; x, y, ...z &#125;</span>) =></span> &#123;&#125;;
    func(&#123; <span class="hljs-attr">a</span>: <span class="hljs-number">3</span>, <span class="hljs-attr">x</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">y</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">b</span>: <span class="hljs-number">4</span> &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-26">7.2 数组展开运算符</h3>
<blockquote>
<p>将一个数组转为用逗号分隔的参数序列,该运算符主要用于函数调用。<br>
<strong>区分剩余参数和展开运算符</strong></p>
<blockquote>
<p>根本区别 :</p>
<blockquote>
<pre><code class="copyable">  展开运算符把数组`转化为参数`
  [3,1,2]->3,1,2
  剩余参数把剩余`参数转化为数组`
  3,1,2->[3,1,2]
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
</blockquote>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">const</span> arr1 = [<span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>];
      <span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, ...arr1, <span class="hljs-number">7</span>, <span class="hljs-number">8</span>, <span class="hljs-number">9</span>];
      <span class="hljs-built_in">console</span>.log(arr);<span class="hljs-comment">//[1, 2, 3, 4, 5, 6, 7, 8, 9]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Math</span>.min(...[<span class="hljs-number">3</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>]));
<span class="hljs-comment">// ES5 的写法</span>
<span class="hljs-built_in">Math</span>.max.apply(<span class="hljs-literal">null</span>, [<span class="hljs-number">14</span>, <span class="hljs-number">3</span>, <span class="hljs-number">77</span>])

<span class="hljs-comment">// ES6 的写法</span>
<span class="hljs-built_in">Math</span>.max(...[<span class="hljs-number">14</span>, <span class="hljs-number">3</span>, <span class="hljs-number">77</span>])

<span class="hljs-comment">// 等同于</span>
<span class="hljs-built_in">Math</span>.max(<span class="hljs-number">14</span>, <span class="hljs-number">3</span>, <span class="hljs-number">77</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-27">7.2.1 替代函数的 apply 方法</h4>
<p>由于扩展运算符可以展开数组，所以不再需要apply方法，将数组转为函数的参数了</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// ES5 的写法</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params">x, y, z</span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
&#125;
<span class="hljs-keyword">var</span> args = [<span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>];
f.apply(<span class="hljs-literal">null</span>, args);

<span class="hljs-comment">// ES6的写法</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f</span>(<span class="hljs-params">x, y, z</span>) </span>&#123;
  <span class="hljs-comment">// ...</span>
&#125;
<span class="hljs-keyword">let</span> args = [<span class="hljs-number">0</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>];
f(...args);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-28">7.2.2 数组展开运算符的应用</h4>
<ul>
<li>1.复制数组</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">       <span class="hljs-keyword">const</span> a = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>];
       <span class="hljs-keyword">const</span> c = [...a];
       a[<span class="hljs-number">0</span>] = <span class="hljs-number">3</span>;
       <span class="hljs-built_in">console</span>.log(a);<span class="hljs-comment">//[3,2]</span>
       <span class="hljs-built_in">console</span>.log(c);<span class="hljs-comment">//[1,2]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>2.合并数组(浅拷贝)</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr1 = [<span class="hljs-string">'a'</span>, <span class="hljs-string">'b'</span>];
<span class="hljs-keyword">const</span> arr2 = [<span class="hljs-string">'c'</span>];
<span class="hljs-keyword">const</span> arr3 = [<span class="hljs-string">'d'</span>, <span class="hljs-string">'e'</span>];

<span class="hljs-comment">// ES5 的合并数组</span>
arr1.concat(arr2, arr3);
<span class="hljs-comment">// [ 'a', 'b', 'c', 'd', 'e' ]</span>

<span class="hljs-comment">// ES6 的合并数组</span>
[...arr1, ...arr2, ...arr3]
<span class="hljs-comment">// [ 'a', 'b', 'c', 'd', 'e' ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>3.字符串转为数组</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">       <span class="hljs-built_in">console</span>.log([...<span class="hljs-string">'alex'</span>]);<span class="hljs-comment">//['a','l','e','x']</span>
       <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'alex'</span>.split(<span class="hljs-string">''</span>));<span class="hljs-comment">//es6之前</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>4.常见的类数组转化为数组</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-number">4.1</span> <span class="hljs-built_in">arguments</span>
       <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">func</span>(<span class="hljs-params"></span>) </span>&#123;
         <span class="hljs-built_in">console</span>.log([...arguments]);
       &#125;
       func(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>);

    <span class="hljs-number">4.2</span> NodeList
      <span class="hljs-built_in">console</span>.log([...document.querySelectorAll(<span class="hljs-string">'p'</span>)]);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<ol start="5">
<li>实现了 Iterator 接口的对象</li>
</ol>
</li>
</ul>
<blockquote>
<p>任何定义了遍历器（Iterator）接口的对象（参阅 Iterator 一章），都可以用扩展运算符转为真正的数组。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> nodeList = <span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">'div'</span>);
<span class="hljs-keyword">let</span> array = [...nodeList];
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-29">7.3 对象展开运算符的基本用法</h3>
<p>对象的扩展运算符（...）用于取出参数对象的所有可遍历属性，拷贝到当前对象之中。</p>
<h4 data-id="heading-30">1. 展开对象(复制对象)</h4>
<ul>
<li>对象不能直接展开，必须在 &#123;&#125; 中展开</li>
<li>对象的展开：把属性罗列出来，用逗号分隔，放到一个 &#123;&#125; 中，构成新对象</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">const</span> apple = &#123;
        <span class="hljs-attr">color</span>: <span class="hljs-string">"红色"</span>,
        <span class="hljs-attr">shape</span>: <span class="hljs-string">"球形"</span>,
        <span class="hljs-attr">taste</span>: <span class="hljs-string">"甜"</span>,
      &#125;;
      <span class="hljs-keyword">const</span> Ob = &#123; ...apple &#125;;
      <span class="hljs-built_in">console</span>.log(Ob);
      <span class="hljs-built_in">console</span>.log(Ob === apple); <span class="hljs-comment">//false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-31">2.合并对象</h4>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">const</span> apple = &#123;
        <span class="hljs-attr">color</span>: <span class="hljs-string">'红色'</span>,
        <span class="hljs-attr">shape</span>: <span class="hljs-string">'球形'</span>,
        <span class="hljs-attr">taste</span>: <span class="hljs-string">'甜'</span>
      &#125;;
      <span class="hljs-keyword">const</span> pen = &#123;
        <span class="hljs-attr">color</span>: <span class="hljs-string">'黑色'</span>,
        <span class="hljs-attr">shape</span>: <span class="hljs-string">'圆柱形'</span>,
        <span class="hljs-attr">use</span>: <span class="hljs-string">'写字'</span>
      &#125;;
       <span class="hljs-built_in">console</span>.log(&#123; ...apple, ...pen &#125;);
       <span class="hljs-comment">//   新对象拥有全部属性，相同属性，后者覆盖前者</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-32">3. 用户参数和默认参数</h4>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">const</span> logUser = <span class="hljs-function"><span class="hljs-params">userParam</span> =></span> &#123;
        <span class="hljs-keyword">const</span> defaultParam = &#123;
          <span class="hljs-attr">username</span>: <span class="hljs-string">'ZhangSan'</span>,
          <span class="hljs-attr">age</span>: <span class="hljs-number">0</span>,
          <span class="hljs-attr">sex</span>: <span class="hljs-string">'male'</span>
        &#125;;
        <span class="hljs-keyword">const</span> param = &#123; ...defaultParam, ...userParam &#125;;
        <span class="hljs-built_in">console</span>.log(param.username);
      &#125;;
      logUser();
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-33">4.注意事项</h4>
<blockquote>
<ul>
<li>
<ol>
<li>如果展开一个空对象，则没有任何效果</li>
</ol>
</li>
<li>
<ol start="2">
<li>非对象的展开</li>
</ol>
</li>
</ul>
<blockquote>
<p>如果展开的不是对象，则会自动将其转为对象，再将其属性罗列出来<br>
如果展开运算符后面是字符串，它会自动转成一个类似数组的对象，因此返回的不是空对象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(&#123; ...<span class="hljs-string">'alex'</span> &#125;);<span class="hljs-comment">//&#123;0: "a", 1: "l", 2: "e", 3: "x"&#125;</span>
<span class="hljs-built_in">console</span>.log([...<span class="hljs-string">'alex'</span>]);<span class="hljs-comment">// ["a", "l", "e", "x"]</span>
<span class="hljs-built_in">console</span>.log(...<span class="hljs-string">'alex'</span>);<span class="hljs-comment">// a l e x</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> arr = [<span class="hljs-string">"cccc"</span>, <span class="hljs-string">"dddd"</span>, <span class="hljs-string">"eeeee"</span>];
<span class="hljs-keyword">let</span> obj = &#123; ...arr &#125;;
<span class="hljs-built_in">console</span>.log(obj);<span class="hljs-comment">//&#123;0: "cccc", 1: "dddd", 2: "eeeee"&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
</blockquote>
<h2 data-id="heading-34">八.Symbol唯一值</h2>
<blockquote>
<p>ES6新规定的Symbol(符号)是原始值，且符号实例唯一、不可变的，它的用途是确保对象属性使用唯一标识符。</p>
<p>需要使用Symbol()函数初始化</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">let</span> name1 = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'liming'</span>);
 <span class="hljs-keyword">let</span> name2 = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'liming'</span>);
 <span class="hljs-built_in">console</span>.log(name1 == name2);  <span class="hljs-comment">//false</span>
 
<span class="hljs-comment">// 希望能够多次使用同一个symbol值</span>
 <span class="hljs-keyword">let</span> name1 = <span class="hljs-built_in">Symbol</span>.for(<span class="hljs-string">'name'</span>); <span class="hljs-comment">//检测到未创建后新建</span>
 <span class="hljs-keyword">let</span> name2 = <span class="hljs-built_in">Symbol</span>.for(<span class="hljs-string">'name'</span>); <span class="hljs-comment">//检测到已创建后返回</span>
 <span class="hljs-built_in">console</span>.log(name1 === name2); <span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>Symbol的另一特点是隐藏性，Symbol 作为属性名，遍历对象的时候，该属性不会出现在for...in、for...of循环中，也不会被Object.keys()、Object.getOwnPropertyNames()、JSON.stringify()返回。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">let</span> id = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">"id"</span>);
 <span class="hljs-keyword">let</span> obj = &#123;
  [id]:<span class="hljs-string">'symbol'</span>
 &#125;;
 <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> option <span class="hljs-keyword">in</span> obj)&#123;
     <span class="hljs-built_in">console</span>.log(obj[option]); <span class="hljs-comment">//空</span>
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>但是也有能够访问的方法：Object.getOwnPropertySymbols.该方法会返回一个数组，成员是当前对象的所有用作属性名的Symbol值。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">let</span> id = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">"id"</span>);
 <span class="hljs-keyword">let</span> obj = &#123;
  [id]:<span class="hljs-string">'symbol'</span>
 &#125;;
<span class="hljs-keyword">let</span> array = <span class="hljs-built_in">Object</span>.getOwnPropertySymbols(obj);
 <span class="hljs-built_in">console</span>.log(array); <span class="hljs-comment">//[Symbol(id)]</span>
 <span class="hljs-built_in">console</span>.log(obj[array[<span class="hljs-number">0</span>]]);  <span class="hljs-comment">//'symbol'</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-35">九.Set 和 Map 数据结构</h2>
<h3 data-id="heading-36">9.1 Set数据结构</h3>
<ul>
<li>ES6 提供了新的数据结构 Set。它类似于数组，但是成员的值都是唯一的，没有重复的值。</li>
<li>要创建一个 Set，需要提供一个 Array 作为输入，或者直接创建一个空 Set：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">var</span> s1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(); 
      <span class="hljs-keyword">var</span> s2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]); 
      <span class="hljs-built_in">console</span>.log(s1, <span class="hljs-keyword">typeof</span> s1);   <span class="hljs-comment">//Set(0) &#123;&#125; "object"</span>
      <span class="hljs-built_in">console</span>.log(s2, <span class="hljs-keyword">typeof</span> s2);   <span class="hljs-comment">//Set(3) &#123;1, 2, 3&#125; "object"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-37">9.1.1 Set 实例的方法和属性</h4>
<ul>
<li>
<ol>
<li>add添加成员（可以连写）</li>
</ol>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">const</span> s = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>();
      s.add(<span class="hljs-number">1</span>).add(<span class="hljs-number">2</span>).add(<span class="hljs-number">2</span>);
      <span class="hljs-built_in">console</span>.log(s);<span class="hljs-comment">//&#123;1，2&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<ol start="2">
<li>has判断是否有某个成员</li>
</ol>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">     <span class="hljs-keyword">const</span> s = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-string">"ccc"</span>, <span class="hljs-string">"ssss"</span>, <span class="hljs-string">"dddd"</span>]);
     <span class="hljs-built_in">console</span>.log(s.has(<span class="hljs-string">"dddd"</span>)); <span class="hljs-comment">//true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>3.delete删除某个成员</li>
</ul>
<blockquote>
<p>使用 delete 删除不存在的成员，什么都不会发生，也不会报错</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">const</span> s = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-string">"ccc"</span>, <span class="hljs-string">"ssss"</span>, <span class="hljs-string">"dddd"</span>]);
      s.delete(<span class="hljs-string">"dddd"</span>);
      <span class="hljs-built_in">console</span>.log(s);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<ol start="4">
<li>clear全部清除</li>
</ol>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">      s.clear();
       <span class="hljs-built_in">console</span>.log(s);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<ol start="5">
<li>forEach()：使用回调函数遍历每个成员</li>
</ol>
<blockquote>
<p>有两个参数，第一个是回调函数，第二个是改变this指向<br>
Set 中 value = key</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">   <span class="hljs-keyword">const</span> s = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>();
   s.add(<span class="hljs-number">1</span>).add(<span class="hljs-number">2</span>).add(<span class="hljs-number">2</span>);
   s.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value, key, set</span>) </span>&#123;
     <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>);
     <span class="hljs-built_in">console</span>.log(value, key, set === s);
  &#125;, <span class="hljs-built_in">document</span>);
 <span class="hljs-comment">// 按照成员添加进集合的顺序遍历</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>6.属性size--用来获取成员个数，相当于length</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">     <span class="hljs-keyword">const</span> s = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-string">"ccc"</span>, <span class="hljs-string">"ssss"</span>, <span class="hljs-string">"dddd"</span>]);
     <span class="hljs-built_in">console</span>.log(s.size); <span class="hljs-comment">//3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>7.遍历操作</li>
</ul>
<blockquote>
<p>Set 结构的实例有四个遍历方法，可以用于遍历成员。</p>
<blockquote>
<ul>
<li>Set.prototype.keys()：返回键名的遍历器</li>
<li>Set.prototype.values()：返回键值的遍历器</li>
<li>Set.prototype.entries()：返回键值对的遍历器</li>
<li>Set.prototype.forEach()：使用回调函数遍历每个成员</li>
</ul>
</blockquote>
</blockquote>
<h4 data-id="heading-38">9.1.2 Set 构造函数的参数</h4>
<blockquote>
<p>可以接受一个数组（或者具有 iterable 接口的其他数据结构）作为参数，用来初始化。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//1.数组</span>
       <span class="hljs-keyword">const</span> s = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">1</span>]);


<span class="hljs-comment">//2.字符串、arguments、NodeList、Set 等</span>
       <span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(<span class="hljs-string">'hi'</span>));
       <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">func</span>(<span class="hljs-params"></span>) </span>&#123;
         <span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(<span class="hljs-built_in">arguments</span>));
       &#125;
       func(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">1</span>);
       <span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(<span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">'p'</span>)));

      <span class="hljs-keyword">const</span> s = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">1</span>]);
      <span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(s) === s);
      <span class="hljs-built_in">console</span>.log(s);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-39">9.1.3.Set 的注意事项</h4>
<blockquote>
<p>1.判断重复的方式</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">const</span> s = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-literal">NaN</span>, <span class="hljs-number">2</span>, <span class="hljs-literal">NaN</span>]);
      <span class="hljs-built_in">console</span>.log(<span class="hljs-literal">NaN</span> === <span class="hljs-literal">NaN</span>);

   <span class="hljs-comment">//  Set 对重复值的判断基本遵循严格相等（===）</span>
   <span class="hljs-comment">//  但是对于 NaN 的判断与 === 不同，Set 中 NaN 等于 NaN</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>2.什么时候使用 Set?</p>
<blockquote>
<p>① 数组或字符串去重时<br>
② 不需要通过下标访问，只需要遍历时<br>
③ 为了使用 Set 提供的方法和属性时（add delete clear has forEach size 等）</p>
</blockquote>
</blockquote>
<h4 data-id="heading-40">9.1.4.Set 应用</h4>
<blockquote>
<p>1.数组去重</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-built_in">console</span>.log([...new <span class="hljs-built_in">Set</span>([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">1</span>])]);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>2.字符串去重 'abbacbd';<br>
把字符串用Set方法变成去重后对象，再把对象转化成数组，用数组的join方法转化成字符串</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">       <span class="hljs-keyword">const</span> s = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(<span class="hljs-string">'abbacbd'</span>);
       <span class="hljs-built_in">console</span>.log(s);<span class="hljs-comment">//&#123;'a','b','c','d'&#125;</span>
       <span class="hljs-built_in">console</span>.log([...s].join(<span class="hljs-string">''</span>));
       <span class="hljs-built_in">console</span>.log(s);

       <span class="hljs-comment">//一行搞定</span>
       <span class="hljs-built_in">console</span>.log([...new <span class="hljs-built_in">Set</span>(<span class="hljs-string">'abbacbd'</span>)].join(<span class="hljs-string">''</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>3.存放 DOM 元素</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"> <p><span class="hljs-number">1111</span></p>
 <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>22222<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
 <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>3333<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
      <span class="hljs-comment">// for()</span>
      <span class="hljs-keyword">const</span> s = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(<span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">'p'</span>));
      <span class="hljs-built_in">console</span>.log(s);
      s.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">elem</span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(elem);
        elem.style.color = <span class="hljs-string">'red'</span>;
        elem.style.backgroundColor = <span class="hljs-string">'yellow'</span>;
      &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-41">9.2 Map数据结构</h3>
<blockquote>
<ul>
<li>Map 对象保存键值对。任何值(对象或者原始值) 都可以作为一个键或一个值。构造函数 Map 可以接受一个数组作为参数。<br></li>
<li>有一个size：返回 Map 对象中所包含的键值对个数；</li>
<li>如果只是需要 key -> value 的结构，或者需要字符串以外的值做键，使用 Map 比对象更合适，Map 有 forEach 遍历，size 判断个数</li>
</ul>
</blockquote>
<h4 data-id="heading-42">9.2.1 Map 和 Object 的区别</h4>
<ul>
<li>一个 Object 的键只能是字符串或者 Symbols，但一个 Map 的键可以是任意值。</li>
<li>Map 中的键值是有序的（FIFO 原则），而添加到对象中的键则不是。</li>
<li>Map 的键值对个数可以从 size 属性获取，而 Object 的键值对个数只能手动计算。</li>
<li>Object 都有自己的原型，原型链上的键名有可能和你自己在对象上的设置的键名产生冲突。</li>
</ul>
<h4 data-id="heading-43">9.2.2 Map 对象的方法</h4>
<blockquote>
<ul>
<li>set(key, val): 向 Map 中<code>添加</code>新元素;</li>
<li>get(key): 通过键值<code>查找</code>特定的数值并返回;</li>
<li>has(key): 判断 Map 对象中<code>是否有</code> Key 所对应的值，有返回 true,否则返回 false;</li>
<li>delete(key): 通过键值从 Map 中<code>移除</code>对应的数据;</li>
<li>使用 delete <code>删除</code>不存在的成员，什么都不会发生，也不会报错;</li>
<li>clear(): 将这个 Map 中的所有元素<code>清空</code>;</li>
<li>forEach遍历</li>
</ul>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">const</span> m = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
      <span class="hljs-comment">// 1.set()增加</span>
      m.set(<span class="hljs-string">"age"</span>, <span class="hljs-number">18</span>).set(<span class="hljs-literal">true</span>, <span class="hljs-string">"true"</span>).set(<span class="hljs-string">"age"</span>, <span class="hljs-number">20</span>);
      <span class="hljs-built_in">console</span>.log(m); <span class="hljs-comment">// &#123;"age" => 20, true => "true"&#125;</span>

      <span class="hljs-comment">// 2.get()查找 , get 获取不存在的成员，返回 undefined</span>
      <span class="hljs-built_in">console</span>.log(m.get(<span class="hljs-string">"age"</span>)); <span class="hljs-comment">//20</span>

      <span class="hljs-comment">// 3.has(key):是否有</span>
      <span class="hljs-built_in">console</span>.log(m.has(<span class="hljs-string">"age"</span>)); <span class="hljs-comment">//true</span>

      <span class="hljs-comment">// 4.delete(key)删除</span>
      m.delete(<span class="hljs-string">"age"</span>);
      <span class="hljs-built_in">console</span>.log(m); <span class="hljs-comment">//&#123;true => "true"&#125;</span>

      <span class="hljs-comment">// 5.clear():清空</span>
      m.clear();
      <span class="hljs-built_in">console</span>.log(m); <span class="hljs-comment">//&#123;&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">const</span> m = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
      m.set(<span class="hljs-string">"age"</span>, <span class="hljs-number">20</span>).set(<span class="hljs-literal">true</span>, <span class="hljs-string">"true"</span>);
      m.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value, key, map</span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(value, key, map === m);
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>);
        <span class="hljs-comment">/*
         第一次:  20 "age" true   document
         第二次： true true true  document
        */</span>
      &#125;, <span class="hljs-built_in">document</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-44">9.2.3 Map 构造函数的参数</h4>
<h5 data-id="heading-45">1.以二维数组传参</h5>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">const</span> arr2 = [[<span class="hljs-string">"key"</span>, <span class="hljs-string">"value"</span>]];
      <span class="hljs-keyword">const</span> m = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>(arr2);
      <span class="hljs-built_in">console</span>.log(m); <span class="hljs-comment">//Map(1) &#123;"key" => "value"&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Map构造函数接受数组作为参数，实际上执行的是下面的算法。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> items = [
  [<span class="hljs-string">'name'</span>, <span class="hljs-string">'张三'</span>],
  [<span class="hljs-string">'title'</span>, <span class="hljs-string">'Author'</span>]
];
<span class="hljs-keyword">const</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
items.forEach(
  <span class="hljs-function">(<span class="hljs-params">[key, value]</span>) =></span> map.set(key, value)
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-46">2.Set和Map作为参数</h5>
<blockquote>
<p>事实上，不仅仅是数组，任何具有 Iterator 接口、且每个成员都是一个双元素的数组的数据结构都可以当作Map构造函数的参数。这就是说，Set和Map都可以用来生成新的 Map。<br>
Set 中也必须体现出键和值</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">const</span> s = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([
        [<span class="hljs-number">20</span>, <span class="hljs-string">"二十"</span>],
        [<span class="hljs-number">30</span>, <span class="hljs-string">"三十"</span>],
      ]);
      <span class="hljs-built_in">console</span>.log(s); <span class="hljs-comment">// &#123;Array(2), Array(2)&#125;</span>
      <span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>(s)); <span class="hljs-comment">//Map(2) &#123;20 => "二十", 30 => "三十"&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>Map------复制了一个新的 Map</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"> 
      <span class="hljs-keyword">const</span> m1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>([
        [<span class="hljs-string">"name"</span>, <span class="hljs-string">"alex"</span>],
        [<span class="hljs-string">"age"</span>, <span class="hljs-number">18</span>],
      ]);
      <span class="hljs-built_in">console</span>.log(m1);
      <span class="hljs-keyword">const</span> m2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>(m1); <span class="hljs-comment">//&#123;"name" => "alex", "age" => 18&#125;复制一个新map</span>
      <span class="hljs-built_in">console</span>.log(m2, m2 === m1); <span class="hljs-comment">//&#123;"name" => "alex", "age" => 18&#125; false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>改变三个 P 标签文字的颜色</li>
</ul>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Map 的应用<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>1<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>2<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>3<span class="hljs-tag"></<span class="hljs-name">p</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
      <span class="hljs-comment">//把三个p标签解构出来</span>
      <span class="hljs-keyword">const</span> [p1, p2, p3] = <span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">"p"</span>);
      <span class="hljs-built_in">console</span>.log(p1, p2, p3);
      <span class="hljs-comment">// const m = new Map();</span>
      <span class="hljs-comment">// m.set(p1, 'red');</span>
      <span class="hljs-comment">// m.set(p2, 'green');</span>
      <span class="hljs-comment">// m.set(p3, 'blue');</span>

      <span class="hljs-keyword">const</span> m = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>([
        [
          p1,
          &#123;
            <span class="hljs-attr">color</span>: <span class="hljs-string">"red"</span>,
            <span class="hljs-attr">backgroundColor</span>: <span class="hljs-string">"yellow"</span>,
            <span class="hljs-attr">fontSize</span>: <span class="hljs-string">"40px"</span>,
          &#125;,
        ],
        [
          p2,
          &#123;
            <span class="hljs-attr">color</span>: <span class="hljs-string">"green"</span>,
            <span class="hljs-attr">backgroundColor</span>: <span class="hljs-string">"pink"</span>,
            <span class="hljs-attr">fontSize</span>: <span class="hljs-string">"40px"</span>,
          &#125;,
        ],
        [
          p3,
          &#123;
            <span class="hljs-attr">color</span>: <span class="hljs-string">"blue"</span>,
            <span class="hljs-attr">backgroundColor</span>: <span class="hljs-string">"orange"</span>,
            <span class="hljs-attr">fontSize</span>: <span class="hljs-string">"40px"</span>,
          &#125;,
        ],
      ]);

      m.forEach(<span class="hljs-function">(<span class="hljs-params">propObj, elem</span>) =></span> &#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> p <span class="hljs-keyword">in</span> propObj) &#123;
          elem.style[p] = propObj[p];
        &#125;
      &#125;);

      <span class="hljs-comment">// m.forEach((color, elem) => &#123;</span>
      <span class="hljs-comment">//   elem.style.color = color;</span>
      <span class="hljs-comment">// &#125;);</span>
      <span class="hljs-built_in">console</span>.log(m);
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-47">十.Iterator 和 for...of 循环</h2>
<h3 data-id="heading-48">10.1 Iterator遍历器（迭代器）</h3>
<blockquote>
<p>Iterator 是 ES6 引入的一种新的遍历机制，迭代器有两个核心概念：</p>
</blockquote>
<ul>
<li>迭代器是一个统一的接口，它的作用是使各种数据结构可被便捷的访问，它是通过一个键为 Symbol.iterator 的方法来实现。</li>
<li>迭代器是用于遍历数据结构元素的指针（如数据库中的游标）。</li>
</ul>
<h4 data-id="heading-49">10.1.1 Iterator 的作用有三个：</h4>
<ul>
<li>一是为各种数据结构，提供一个统一的、简便的访问接口；</li>
<li>二是使得数据结构的成员能够按某种次序排列；</li>
<li>三是 ES6 创造了一种新的遍历命令for...of循环，Iterator 接口主要供for...of消费。</li>
</ul>
<h4 data-id="heading-50">10.1.2 迭代的过程如下：</h4>
<ul>
<li>通过 Symbol.iterator 创建一个迭代器，指向当前数据结*构的起始位置</li>
<li>随后通过 next 方法进行向下迭代指向下一个位置， next 方法会返回当前位置的对象，对象包含了 value 和 done 两个属性， value 是当前属性的值， done 用于判断是否遍历结束。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">const</span> items = [<span class="hljs-string">"zero"</span>, <span class="hljs-string">"one"</span>, <span class="hljs-string">"two"</span>];
      <span class="hljs-keyword">const</span> it = items[<span class="hljs-built_in">Symbol</span>.iterator]();
      <span class="hljs-built_in">console</span>.log(it.next()); <span class="hljs-comment">//&#123;value: "zero", done: false&#125;</span>
      <span class="hljs-built_in">console</span>.log(it.next()); <span class="hljs-comment">//&#123;value: "one", done: false&#125;</span>
      <span class="hljs-built_in">console</span>.log(it.next()); <span class="hljs-comment">//&#123;value: "two", done: false&#125;</span>
      <span class="hljs-built_in">console</span>.log(it.next());<span class="hljs-comment">// &#123;value: undefined, done: true&#125;</span>
      <span class="hljs-built_in">console</span>.log(it.next()); <span class="hljs-comment">//&#123;value: undefined, done: true&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-51">10.1.3 为什么需要 Iterator 遍历器--for..of 来遍历</h4>
<p>我们之前的遍历方法是:</p>
<ul>
<li>遍历数组：for 循环和 forEach 方法</li>
<li>遍历对象：for in 循环</li>
</ul>
<p>而 Iterator 遍历器是一个统一的遍历方式，使用 Iterator 封装好的 for..of 来遍历,不管是数组还是对象都可以遍历</p>
<h3 data-id="heading-52">10.2 for..of 来统一遍历遍历</h3>
<blockquote>
<p>1.什么是可遍历？</p>
<blockquote>
<p>只要有 Symbol.iterator 方法，并且这个方法可以生成可遍历对象，就是可遍历的, 只要可遍历，就可以使用 for...of 循环来统一遍历</p>
</blockquote>
<p>2.原生可遍历的有哪些?</p>
<ul>
<li>数组</li>
<li>字符串</li>
<li>Set</li>
<li>Map</li>
<li>arguments</li>
<li>NodeList</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> elem <span class="hljs-keyword">of</span> <span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">'p'</span>)) &#123;
        <span class="hljs-built_in">console</span>.log(elem);
       elem.style.color = <span class="hljs-string">'red'</span>;
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.非原生可遍历的有哪些?</p>
<blockquote>
<p>一般的对象可以用for ... in遍历，也可以给他添加一个Symbol.iterator然后用for ... of 遍历</p>
</blockquote>
</blockquote>
<h4 data-id="heading-53">10.2.1 for...of 遍历数组</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//keys() 得到的是索引的可遍历对象，可以遍历出索引值</span>
      <span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">of</span> arr.keys()) &#123;
          <span class="hljs-built_in">console</span>.log(key);
       &#125;
<span class="hljs-comment">//values() 得到的是值的可遍历对象，可以遍历出值</span>
       <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> value <span class="hljs-keyword">of</span> arr.values()) &#123;
         <span class="hljs-built_in">console</span>.log(value);
       &#125;
   相当于
       <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> value <span class="hljs-keyword">of</span> arr) &#123;
         <span class="hljs-built_in">console</span>.log(value);
       &#125;

<span class="hljs-comment">//entries() 得到的是索引+值组成的数组的可遍历对象</span>
       <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> entries <span class="hljs-keyword">of</span> arr.entries()) &#123;
         <span class="hljs-built_in">console</span>.log(entries);<span class="hljs-comment">//数组[0,1]</span>
       &#125;
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> [index, value] <span class="hljs-keyword">of</span> arr.entries()) &#123;
        <span class="hljs-built_in">console</span>.log(index, value);值<span class="hljs-number">0</span>  <span class="hljs-number">1</span>
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-54">10.2.2  for...of 遍历普通对象</h4>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">const</span> person = &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">"John Smith"</span>,
        <span class="hljs-attr">job</span>: <span class="hljs-string">"agent"</span>,
      &#125;;

      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> [key, value] <span class="hljs-keyword">of</span> <span class="hljs-built_in">Object</span>.entries(person)) &#123;
        <span class="hljs-built_in">console</span>.log(key, value);
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-55">十一.Es6新增方法</h2>
<h3 data-id="heading-56">11.1 Es6字符串新增方法</h3>
<h4 data-id="heading-57">1. includes()判断字符串中是否含有某些字符</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//判断字符串</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'abc'</span>.includes(<span class="hljs-string">'a'</span>, <span class="hljs-number">0</span>));<span class="hljs-comment">//true</span>
<span class="hljs-number">1.</span>第一个参数------表示是否包含该值
<span class="hljs-number">2.</span>第二个参数----- 表示开始搜索的位置，默认是 <span class="hljs-number">0</span>

<span class="hljs-comment">//判断数组</span>
 arr = [<span class="hljs-string">"name"</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>, <span class="hljs-number">7</span>, <span class="hljs-number">8</span>];
 <span class="hljs-built_in">console</span>.log(arr.includes(<span class="hljs-string">"name"</span>));<span class="hljs-comment">//true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-58">应用：给url添加参数</h5>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-comment">// https://www.imooc.com/course/list</span>
      <span class="hljs-comment">// https://www.imooc.com/course/list?c=fe&sort=pop&name=value</span>
      <span class="hljs-keyword">let</span> url = <span class="hljs-string">"https://www.imooc.com/course/list?"</span>;
      <span class="hljs-keyword">const</span> addURLParam = <span class="hljs-function">(<span class="hljs-params">url, name, value</span>) =></span> &#123;
        <span class="hljs-comment">// 第一步：判断url有没有问号，有的话说明后面接了数据，只需加&拼接就欧克，否则先加问号</span>

        url += url.includes(<span class="hljs-string">"?"</span>) ? <span class="hljs-string">"&"</span> : <span class="hljs-string">"?"</span>;
        <span class="hljs-comment">// 第二步：传入key=value，添加给url</span>
        url += <span class="hljs-string">`<span class="hljs-subst">$&#123;name&#125;</span>=<span class="hljs-subst">$&#123;value&#125;</span>`</span>;

        <span class="hljs-keyword">return</span> url;
      &#125;;
      url = addURLParam(url, <span class="hljs-string">"c"</span>, <span class="hljs-string">"fe"</span>);
      <span class="hljs-built_in">console</span>.log(url);<span class="hljs-comment">//https://www.imooc.com/course/list?&c=fe</span>
      url = addURLParam(url, <span class="hljs-string">"sort"</span>, <span class="hljs-string">"pop"</span>);
      <span class="hljs-built_in">console</span>.log(url);<span class="hljs-comment">//https://www.imooc.com/course/list?&c=fe&sort=pop</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-59">2.padStart() 和 padEnd()补全字符串长度</h4>
<blockquote>
<ul>
<li>用来在字符串本身的头部或尾部补全字符串长度</li>
<li>原字符串的长度，等于或大于最大长度，不会消减原字符串，字符串补全不生效，返回原字符串</li>
<li>用来补全的字符串与原字符串长度之和超过了最大长度，截去超出位数的补全字符串，原字符串不动</li>
</ul>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"abc"</span>.padStart(<span class="hljs-number">10</span>, <span class="hljs-string">"0123456789"</span>)); <span class="hljs-comment">//0123456abc</span>
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"abc"</span>.padEnd(<span class="hljs-number">10</span>, <span class="hljs-string">"0123456789"</span>)); <span class="hljs-comment">//abc0123456</span>
      <span class="hljs-comment">//  第一个参数表示补全后的字符串长度，第二个参数是要用到的元素补全字符串</span>
      <span class="hljs-comment">// 如果省略第二个参数，默认使用空格补全长度</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-60">应用----显示日期格式</h5>
<h4 data-id="heading-61">3.trimStart() 和 trimEnd()清除字符串的首或尾空格</h4>
<pre><code class="hljs language-js copyable" lang="js">       <span class="hljs-keyword">const</span> s = <span class="hljs-string">'  a b c  '</span>;
       <span class="hljs-built_in">console</span>.log(s);
       <span class="hljs-built_in">console</span>.log(s.trimStart());
       <span class="hljs-built_in">console</span>.log(s.trimEnd());
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-62">应用-表单验证提交</h5>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>trimStart() 和 trimEnd()<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"username"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"submit"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"提交"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"btn"</span> /></span>

    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
      <span class="hljs-keyword">const</span> usernameInput = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"username"</span>);
      <span class="hljs-keyword">const</span> btn = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"btn"</span>);

      btn.addEventListener(
        <span class="hljs-string">"click"</span>,
        <span class="hljs-function">() =></span> &#123;
          <span class="hljs-built_in">console</span>.log(usernameInput.value);

          <span class="hljs-comment">// 验证</span>
          <span class="hljs-built_in">console</span>.log(usernameInput.value.trim());
          <span class="hljs-keyword">if</span> (usernameInput.value.trim() !== <span class="hljs-string">""</span>) &#123;
            <span class="hljs-comment">// 可以提交</span>
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"可以提交"</span>);
          &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-comment">// 不能提交</span>
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"不能提交"</span>);
          &#125;

          <span class="hljs-comment">// 手动提交</span>
        &#125;,
        <span class="hljs-literal">false</span>
      );
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-63">11.2 Es6数组新增方法</h3>
<h4 data-id="heading-64">1.includes()</h4>
<ul>
<li>判断数组中是否含有某个成员</li>
<li>第二个参数表示搜索的起始位置，默认值是 0</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-comment">//从索引值为2的地方开始，判断后面是否含有2这个元素</span>
      <span class="hljs-built_in">console</span>.log([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>].includes(<span class="hljs-number">2</span>, <span class="hljs-number">2</span>));
      <span class="hljs-comment">// 基本遵循严格相等（===）,但是对于 NaN 的判断与 === 不同，includes 认为 NaN === NaN</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-65">应用-数组去重</h5>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">const</span> arr = [];
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> item <span class="hljs-keyword">of</span> [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">1</span>]) &#123;
        <span class="hljs-keyword">if</span> (!arr.includes(item)) &#123;
          arr.push(item);
        &#125;
      &#125;
      <span class="hljs-built_in">console</span>.log(arr); <span class="hljs-comment">//[1,2]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-66">2.Array.from()</h4>
<ul>
<li>Array.from()将类数组对象（一个类数组对象必须含有 length 属性，且元素属性名必须是数值或者可转换为数值的字符。）或可迭代对象(数组、字符串、Set、Map、NodeList、arguments)转化为数组。</li>
<li>一般情况下把拥有 length 属性的任意对象转化为数组。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-comment">// 类数组：&#123;number:'value',length:1&#125;</span>
      a = &#123; <span class="hljs-number">0</span>: <span class="hljs-string">"aaa"</span>, <span class="hljs-number">1</span>: <span class="hljs-string">"bbb"</span>, <span class="hljs-number">2</span>: <span class="hljs-string">"cccc"</span>, <span class="hljs-number">3</span>: <span class="hljs-string">"ddd"</span>, <span class="hljs-number">4</span>: <span class="hljs-string">"eeee"</span>, <span class="hljs-attr">length</span>: <span class="hljs-number">5</span> &#125;;
      <span class="hljs-keyword">let</span> array1 = <span class="hljs-built_in">Array</span>.from(a);
      <span class="hljs-built_in">console</span>.log(array1); <span class="hljs-comment">// ["aaa", "bbb", "cccc", "ddd", "eeee"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>元素属性名不为数值且无法转换为数值，返回长度为 length 元素值为 undefined 的数组</li>
<li><strong>第一个参数</strong>---能被转化的数据</li>
<li><strong>第二个参数</strong>---作用类似于数组的 map 方法，用来对每个元素进行处理，将处理后的值放入返回的数组</li>
<li><strong>第三个参数</strong>--第二个参数为一般回调函数时，第三个参数可以改变 this 指向</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">     <span class="hljs-comment">// 类数组：&#123;number:'value',length:1&#125;</span>
      a = &#123; <span class="hljs-number">0</span>: <span class="hljs-string">"aaa"</span>, <span class="hljs-number">1</span>: <span class="hljs-string">"bbb"</span>, <span class="hljs-number">2</span>: <span class="hljs-string">"cccc"</span>, <span class="hljs-number">3</span>: <span class="hljs-string">"ddd"</span>, <span class="hljs-number">4</span>: <span class="hljs-string">"eeee"</span>, <span class="hljs-attr">length</span>: <span class="hljs-number">5</span> &#125;;
      <span class="hljs-keyword">let</span> array1 = <span class="hljs-built_in">Array</span>.from(a, <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> value + <span class="hljs-string">"你真帅"</span>);
      <span class="hljs-built_in">console</span>.log(array1); <span class="hljs-comment">// ["aaa你真帅", "bbb你真帅", "cccc你真帅", "ddd你真帅", "eeee你真帅"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-67">3.find() 和 findIndex()</h4>
<blockquote>
<p>find()：find()返回第一个匹配的元素</p>
<blockquote>
<ul>
<li>1.find()方法对数组中的每一项元素执行一次 callback 函数，直至有一个 callback 返回 true。</li>
<li>2.当找到了这样一个元素后，该方法会立即返回这个元素的值，否则返回 undefined。</li>
<li>3.callback函数带有3个参数：当前元素的值、当前元素的索引，以及数组本身。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">     <span class="hljs-keyword">var</span> num = [<span class="hljs-number">10</span>, <span class="hljs-number">20</span>, <span class="hljs-number">30</span>, <span class="hljs-number">40</span>, <span class="hljs-number">50</span>, <span class="hljs-number">60</span>, <span class="hljs-number">70</span>, <span class="hljs-number">80</span>, <span class="hljs-number">90</span>];
     <span class="hljs-keyword">var</span> newNum1 = num.find(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123;
       <span class="hljs-keyword">return</span> item > <span class="hljs-number">40</span>;
     &#125;);
     <span class="hljs-built_in">console</span>.log(newNum1); <span class="hljs-comment">//50</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<p>findIndex()返回数组中第一个满足条件的索引(从0开始), 不满足返回-1;</p>
<blockquote>
<pre><code class="hljs language-js copyable" lang="js">     <span class="hljs-keyword">var</span> num = [<span class="hljs-number">10</span>, <span class="hljs-number">20</span>, <span class="hljs-number">30</span>, <span class="hljs-number">40</span>, <span class="hljs-number">50</span>, <span class="hljs-number">60</span>, <span class="hljs-number">70</span>, <span class="hljs-number">80</span>, <span class="hljs-number">90</span>];
     <span class="hljs-keyword">var</span> newNum1 = num.findIndex(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123;
       <span class="hljs-keyword">return</span> item > <span class="hljs-number">40</span>;
     &#125;);
     <span class="hljs-built_in">console</span>.log(newNum1); <span class="hljs-comment">//4  index=length-1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
</blockquote>
<h5 data-id="heading-68">应用-筛选数据</h5>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">const</span> students = [
        &#123;
          <span class="hljs-attr">name</span>: <span class="hljs-string">"张三"</span>,
          <span class="hljs-attr">sex</span>: <span class="hljs-string">"男"</span>,
          <span class="hljs-attr">age</span>: <span class="hljs-number">16</span>,
        &#125;,
        &#123;
          <span class="hljs-attr">name</span>: <span class="hljs-string">"李四"</span>,
          <span class="hljs-attr">sex</span>: <span class="hljs-string">"女"</span>,
          <span class="hljs-attr">age</span>: <span class="hljs-number">22</span>,
        &#125;,
        &#123;
          <span class="hljs-attr">name</span>: <span class="hljs-string">"王二麻子"</span>,
          <span class="hljs-attr">sex</span>: <span class="hljs-string">"男"</span>,
          <span class="hljs-attr">age</span>: <span class="hljs-number">32</span>,
        &#125;,
      ];
      <span class="hljs-built_in">console</span>.log(students.find(<span class="hljs-function">(<span class="hljs-params">value</span>) =></span> value.sex === <span class="hljs-string">"男"</span>));
      <span class="hljs-built_in">console</span>.log(students.findIndex(<span class="hljs-function">(<span class="hljs-params">value</span>) =></span> value.sex === <span class="hljs-string">"女"</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-69">11.3 Es6对象新增方法</h3>
<h4 data-id="heading-70">1.Object.assign()合并对象</h4>
<ul>
<li>Object.assign(目标对象, 源对象 1,源对象 2,...): 目标对象</li>
<li>Object.assign 直接合并到了第一个参数中，返回的就是合并后的对象</li>
</ul>
<h5 data-id="heading-71">应用--合并默认参数和用户参数</h5>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">const</span> logUser = <span class="hljs-function">(<span class="hljs-params">userOptions</span>) =></span> &#123;
        <span class="hljs-keyword">const</span> DEFAULTS = &#123;
          <span class="hljs-attr">username</span>: <span class="hljs-string">"ZhangSan"</span>,
          <span class="hljs-attr">age</span>: <span class="hljs-number">0</span>,
          <span class="hljs-attr">sex</span>: <span class="hljs-string">"male"</span>,
        &#125;;
        <span class="hljs-keyword">const</span> options = <span class="hljs-built_in">Object</span>.assign(&#123;&#125;, DEFAULTS, userOptions);
        <span class="hljs-built_in">console</span>.log(options);
      &#125;;
      logUser();
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-72">2.Object.keys()、Object.values() 和 Object.entries()</h4>
<ul>
<li>数组的 keys()、values()、entries() 等方法是实例方法，返回的都是 Iterator</li>
<li>对象的 Object.keys()、Object.values()、Object.entries() 等方法是构造函数方法，返回的是数组</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">const</span> person = &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">"Alex"</span>,
        <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,
      &#125;;

      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.keys(person)); <span class="hljs-comment">//['name',"age"]</span>
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.values(person));<span class="hljs-comment">//["Alex", 18]</span>
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.entries(person)); <span class="hljs-comment">//二维数组  [["name", "Alex"],["age", 18]]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-73">应用-和for...of...一起遍历对象</h5>
<pre><code class="hljs language-js copyable" lang="js">      obj = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"蔡徐坤"</span>, <span class="hljs-attr">age</span>: <span class="hljs-string">"18"</span>, <span class="hljs-attr">hobby</span>: [<span class="hljs-string">"唱歌"</span>, <span class="hljs-string">"写歌"</span>, <span class="hljs-string">"跳舞"</span>] &#125;;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.entries(obj));

      <span class="hljs-keyword">for</span> (key <span class="hljs-keyword">of</span> <span class="hljs-built_in">Object</span>.entries(obj)) &#123;
        <span class="hljs-built_in">console</span>.log(key[<span class="hljs-number">0</span>], key[<span class="hljs-number">1</span>]);
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-74">十二.Promise对象</h2>
<ul>
<li>Promise是ES6中新增的异步编程解决方案, 在代码中的表现是一个对象。</li>
<li>Promise的精髓是“状态”，用维护状态、传递状态的方式来使得回调函数能够及时调用;</li>
<li>企业开发中为了保存异步代码的执行顺序, 那么就会出现回调函数层层嵌套，如果回调函数嵌套的层数太多, 就会导致代码的阅读性, 可维护性大大降低。<code>Promise对象可以将异步操作以同步流程来表示, 避免了回调函数层层嵌套(回调地狱)。</code></li>
</ul>
<h3 data-id="heading-75">12.1 基本使用</h3>
<blockquote>
<p>第一步：创建一个Promise实例对象，并传入<code>执行器函数</code>，执行器函数会同时执行</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//Promise是一个构造函数</span>
<span class="hljs-keyword">let</span> p = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(executor)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>第二步：executor执行器函数接受两个函数参数，resolve和reject,这两个函数是改变Promise状态的;</p>
<blockquote>
<ol>
<li>pending:  默认状态，只要没有告诉Promise任务是成功还是失败就是pending状态</li>
</ol>
</blockquote>
<blockquote>
<ol start="2">
<li>fulfilled(resolved): 只要调用resolve函数, 状态就会变为fulfilled, 表示操作成功</li>
</ol>
</blockquote>
<blockquote>
<ol start="3">
<li>rejected: 只要调用rejected函数, 状态就会变为rejected, 表示操作失败</li>
</ol>
</blockquote>
<p><strong>注意点</strong>:状态一旦改变既不可逆, 既从pending变为fulfilled, 那么永远都是fulfilled , 既从pending变为rejected, 那么永远都是rejected.</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">let</span> p = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"我同步执行"</span>);
        resolve(<span class="hljs-string">"我是resolve携带的数据"</span>);
        <span class="hljs-comment">// reject("我是reject携带的失败信息");</span>
      &#125;).then(
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">result</span>(<span class="hljs-params">res</span>) </span>&#123;
          <span class="hljs-built_in">console</span>.log(res);
        &#125;,<span class="hljs-comment">//期约兑现回调</span>
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reason</span>(<span class="hljs-params">reason</span>) </span>&#123;
          <span class="hljs-built_in">console</span>.log(reason);
        &#125;<span class="hljs-comment">//期约拒绝回调</span>
      );
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> p=<span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>((resolve,reject)=&#123;
  <span class="hljs-comment">/* 
  这里一般存放的都是我们即将要处理的异步任务（比如网络请求成功），任务成功我们执行resolve吧数据传出去,
  任务失败我们执行reject（当然写同步的也可以），之后根据状态就可以调用原型里面的三个方法
  */</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-76">12.2 Promise.prototype.then()方法的使用</h3>
<ul>
<li>
<p>then 方法接收两个函数作为参数，第一个参数是 Promise 执行成功时的回调，第二个参数是 Promise 执行失败时的回调，两个函数只会有一个被调用。</p>
</li>
<li>
<p>then()方法执行后返回的是一个新的 Promise 对象</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">let</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
        resolve(<span class="hljs-string">"111"</span>);
      &#125;);
      p1 = promise.then(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">success</span>(<span class="hljs-params">res</span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(res);

        <span class="hljs-keyword">return</span> <span class="hljs-number">222222</span>;
      &#125;);
      <span class="hljs-built_in">console</span>.log(p1);

      <span class="hljs-comment">/*
      p1是一个新的Promise；
         [[PromiseState]]: "fulfilled"
         [[PromiseResult]]: "222"
      */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>同一个promise对象可以多次调用then方法 .  当该promise对象的状态对应时所有then方法都会被执行。</li>
<li>可以通过上一个promise对象的then方法给下一个promise对象的then方法传递参数,传递的参数通过return返回给下一个promise对象的then方法。</li>
<li>链式调用then返回的的Promise对象状态都与第一个一样，接受的参数(对象的结果)由上个链式调用函数的返回值有关</li>
</ul>
<p>第一次使用resolve函数:</p>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">let</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
        resolve(<span class="hljs-string">"我是resolve函数传过来的参数"</span>);
      &#125;);
      p1 = promise.then(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">success</span>(<span class="hljs-params">res</span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(res);

        <span class="hljs-keyword">return</span> res;
      &#125;);
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"我是第1次链式调用then方法"</span>, p1);
      p2 = p1.then(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">success</span>(<span class="hljs-params">res</span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(res);

        <span class="hljs-keyword">return</span> res;
      &#125;);
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"我是第2次链式调用then方法"</span>, p2);
      p3 = p2.then(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">success</span>(<span class="hljs-params">res</span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(res);

        <span class="hljs-keyword">return</span> res;
      &#125;);
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"我是第3次链式调用then方法"</span>, p3);
      p4 = p3.then(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">success</span>(<span class="hljs-params">res</span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(res);

        <span class="hljs-keyword">return</span> res;
      &#125;);
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"我是第4次链式调用then方法"</span>, p4);
      <span class="hljs-comment">/*
      p1，p2,p3,p4是一个新的Promise；
         [[PromiseState]]: "fulfilled"
         [[PromiseResult]]: "我是resolve函数传过来的参数"
      */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>如果第一次是reject：</p>
</blockquote>
<p>第一步：new Promise()并执行reject</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">let</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
        reject(<span class="hljs-string">"我是reject函数传过来的参数"</span>);
        <span class="hljs-comment">// resolve("我是resolve函数传过来的参数");</span>
      &#125;);
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"我是new出来开的promise"</span>, promise);
      <span class="hljs-comment">/*
      [[PromiseState]]: "rejected"
      [[PromiseResult]]: "我是reject函数传过来的参数"//始终不变

      */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二步：</p>
<ul>
<li>promise.then方法执行（根据拒绝状态他应该调用then的第二个失败回调）；同时使第一次then产生的Promise对象，他的状态是成功的；值是undefined</li>
<li>你一定想改他的状态和结果吧？失败函数里面抛出错误，就能改了。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">      p1 = promise.then(
        <span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
          <span class="hljs-built_in">console</span>.log(res);
        &#125;,
        <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"失败回调函数被调用了"</span>, err);
          <span class="hljs-comment">// throw new Error(err);</span>
        &#125;
      );

      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"我是第1次链式调用then方法返回的promise"</span>, p1);
      <span class="hljs-comment">/*
       [[PromiseState]]: "fulfilled"
       [[PromiseResult]]: undefined

       如果在失败回调里面抛出错误，p1就会发生变化   
        [[PromiseState]]: "rejected"
        [[PromiseResult]]: Error: 我是reject函数传过来的参数 
      */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第三步：</p>
<ul>
<li>then方法执行第2次产生的Promise对象（执行哪个函数根据上一个promise的状态决定），这里假定为成功。</li>
<li>之前有一次状态是失败，这里就算执行成功的回调也传不过来原始数据；</li>
<li>在成功的回调里面写上返回值改写p2的结果</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">      p2 = p1.then(
        <span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'我是第二次执行then'</span>,res); <span class="hljs-comment">// res为undefined，没有数据因为第一次调用的时候是reject，传不过来数据</span>
          <span class="hljs-keyword">return</span> <span class="hljs-number">1111</span>;<span class="hljs-comment">//这里是为了让p2的结果是111</span>
        &#125;,
        <span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"失败回调函数被调用了"</span>, err);
        &#125;
      );
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"我是第2次链式调用then方法"</span>, p2);
      <span class="hljs-comment">/*
        [[PromiseState]]: "fulfilled"
        [[PromiseResult]]: 1111
      
      */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>结论：</li>
</ul>
<blockquote>
<p>执行reject()的后果：</p>
<blockquote>
<p>让当前Promise对象状态变为失败，不影响后面的，后面的都为成功；</p>
</blockquote>
<blockquote>
<p>只要调用过程用到了reject(),就再也不能获取原始的数据了；</p>
</blockquote>
<blockquote>
<p>前面使用reject之后，若果想要后面也跟着状态变为失败，就要在reject（）对应的失败函数里面抛出<code>错误语句: throw new Error(err)</code>;</p>
</blockquote>
<blockquote>
<p>若果你想要改变当前调用then返回的Promise结果，就需要在当前then里面添加return返回想要的结果。</p>
</blockquote>
<blockquote>
<p>无论是在上一个promise对象成功的回调还是失败的回调传递的参数, 都会传递给下一个promise对象成功的回调。</p>
</blockquote>
</blockquote>
<h3 data-id="heading-77">12.2 Promise.prototype.catch()方法的使用</h3>
<blockquote>
<ul>
<li>
<ol>
<li>catch 其实是 then(undefined, () => &#123;&#125;) 的语法糖;</li>
</ol>
</li>
<li>
<ol start="2">
<li>如果需要分开监听, 也就是通过then监听成功通过catch监听失败，那么必须使用链式编程, 否则会报错;</li>
</ol>
</li>
</ul>
<blockquote>
<p>catch方法使用链式编程的原因是:</p>
<blockquote>
<p>a.如果promise的状态是失败, 但是没有对应失败的监听就会报错<br>
b.then方法会返回一个新的promise, 新的promise会继承原有promise的状态,状态改变的话所有的then都会执行<br>
c.如果新的promise状态是失败, 但是没有对应失败的监听也会报错</p>
</blockquote>
</blockquote>
<ol start="3">
<li>如果 catch里面的回调函数 抛出一个错误或返回一个本身失败的 Promise ，  通过 catch() 返回的Promise 被rejected；否则，它将显示为成功（resolved）。</li>
</ol>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">            <span class="hljs-comment">//抛出错误</span>
           <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">"我失败了"</span>)
             
            <span class="hljs-comment">//返回失败的Promise</span>
           <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
            reject();
          &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>和then方法第二个参数的区别在于, catch方法可以捕获上一个promise对象then方法中的异常。</li>
</ul>
<blockquote>
<p>之前这样的做法会报错</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">let</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
        resolve();
      &#125;);

      promise.then(
        <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"成功"</span>);

          xxx; <span class="hljs-comment">// Uncaught (in promise) ReferenceError: xxx is not defined</span>
         
        &#125;,
        <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"失败"</span>);
        &#125;
      );
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>把成功回调里面的异常抛给catch了</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">let</span> promise = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
        resolve();
      &#125;);

      promise
        .then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"成功"</span>);

          xxx;
        &#125;)
        .catch(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"失败"</span>, e); <span class="hljs-comment">//捕获到前面的异常并传递给e了,失败 ReferenceError: xxx is not defined</span>
        &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-78">js异常处理</h4>
<blockquote>
<p>利用try&#123;&#125;catch&#123;&#125;来处理异常可以保证程序不被中断, 也可以记录错误原因以便于后续优化迭代更新。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">try</span> &#123;
  可能遇到的意外的代码
&#125;
<span class="hljs-keyword">catch</span>(e) &#123;
  捕获错误的代码块
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>catch的特点：</p>
<ul>
<li>(1)和then一样, 在修改promise状态时, 可以传递参数给catch方法中的回调函数；</li>
<li>(2)和then一样, 同一个promise对象可以多次调用catch方法, 当该promise对象的状态时所有catch方法都会被执行.</li>
<li>(3)和then一样, catch方法每次执行完毕后会返回一个新的promise对象</li>
<li>(4) 和then方法一样, 上一个promise对象也可以给下一个promise成功的传递参数。<code>但是</code>，无论是在上一个promise对象成功的回调还是失败的回调传递的参数, 都会传递给下一个promise对象成功的回调。</li>
<li>(5).和then一样, catch方法如果返回的是一个Promise对象, 那么会将返回的Promise对象的执行结果中的值传递给下一个catch方法。</li>
<li>(6) .和then方法第二个参数的区别在于, catch方法可以捕获上一个promise对象then方法中的异常。</li>
</ul>
</blockquote>
<h3 data-id="heading-79">12.3 Promise.all()方法的使用</h3>
<blockquote>
<p>参数:</p>
<ul>
<li>
<ol>
<li>all方法接收一个数组.</li>
</ol>
</li>
<li>
<ol start="2">
<li>如果数组中有多个Promise对象,只有都成功才会执行then方法,并且会按照添加的顺序, 将所有成功的结果重新打包到一个数组中返回给我们。</li>
</ol>
</li>
<li>
<ol start="3">
<li>如果数组中不是Promise对象, 那么会直接执行then方法</li>
</ol>
</li>
</ul>
<p>返回：</p>
<ul>
<li>
<p>1.all方法会返回一个新的Promise对象</p>
</li>
<li>
<p>2.会按照传入数组的顺序将所有Promise中成功返回的结果保存到一个新的数组返回</p>
</li>
<li>
<p>3.数组中有一个Promise失败就会失败, 只有所有成功才会成功</p>
</li>
</ul>
</blockquote>
<ul>
<li>应用场景: 批量加载, 要么一起成功, 要么一起失败</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">      arr = [
        <span class="hljs-string">"http://www.it666.com/files/system/block_picture_1555422597.jpg"</span>,
        <span class="hljs-string">"http://www.it666.com/files/system/block_picture_1555422597.jpg"</span>,
        <span class="hljs-string">"http://www.it666.com/files/system/block_picture_1555419713.jpg"</span>,
      ];
      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">loadImage</span>(<span class="hljs-params">url</span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
          <span class="hljs-keyword">let</span> oImg = <span class="hljs-keyword">new</span> Image();
          <span class="hljs-keyword">let</span> time = <span class="hljs-built_in">Math</span>.random() * <span class="hljs-number">1000</span>;
          <span class="hljs-comment">// console.log(time);</span>
          <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            oImg.src = url;
          &#125;, time);
          <span class="hljs-comment">// oImg.src = url;</span>
          oImg.onload = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            resolve(oImg);
          &#125;;
          oImg.onerror = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            reject(<span class="hljs-string">"图片加载失败了"</span>);
          &#125;;
        &#125;);
      &#125;
      <span class="hljs-built_in">Promise</span>.all([loadImage(arr[<span class="hljs-number">0</span>]), loadImage(arr[<span class="hljs-number">1</span>]), loadImage(arr[<span class="hljs-number">2</span>])])
        .then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">result</span>) </span>&#123;
          <span class="hljs-comment">// console.log(result);</span>
          result.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">oImg</span>) </span>&#123;
            <span class="hljs-built_in">document</span>.body.appendChild(oImg);
          &#125;);
        &#125;)
        .catch(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
          <span class="hljs-built_in">console</span>.log(e);
        &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-80">12.4 Promise.race()方法的使用</h3>
<blockquote>
<ul>
<li>1.race方法接收一个数组,</li>
<li>2.如果数组中有多个Promise对象, 谁先返回状态就听谁的, 后返回的会被抛弃</li>
<li>3.如果数组中不是Promise对象, 那么会直接执行then方法</li>
</ul>
</blockquote>
<ul>
<li>应用场景: 接口调试, 超时处理</li>
</ul>
<p>给超时函数和加载函数均包装一个promise对象，然后把这个对象写入race里面，紧接着写处理函数，5s之内没有获取资源，就直接超时处理</p>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">let</span> url =
        <span class="hljs-string">"http://m.360buyimg.com/babel/jfs/t1/159039/13/7927/381213/6030c447Efe10500b/5e852f2dd56c27fd.jpg.webp"</span>;
      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">loadImage</span>(<span class="hljs-params">url</span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
          <span class="hljs-keyword">let</span> oImg = <span class="hljs-keyword">new</span> Image();
          <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            oImg.src = url;
          &#125;, <span class="hljs-number">2000</span>);
          oImg.onload = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            resolve(oImg);
          &#125;;
          oImg.onerror = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            reject(<span class="hljs-string">"图片加载失败了"</span>);
          &#125;;
        &#125;);
      &#125;
      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">timeout</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">resolve, reject</span>) </span>&#123;
          <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
            reject(<span class="hljs-string">"超时了"</span>);
          &#125;, <span class="hljs-number">5000</span>);
        &#125;);
      &#125;
      <span class="hljs-built_in">Promise</span>.race([loadImage(url), timeout()])
        .then(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value</span>) </span>&#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"成功"</span>, value);
        &#125;)
        .catch(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"失败"</span>, e);
        &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-81">12.4 Promise.resolve()和Promise.reject()方法的使用</h3>
<h4 data-id="heading-82">Promise.resolve()返回一个成功的Promise对象</h4>
<pre><code class="hljs language-js copyable" lang="js">      p = <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-string">"success"</span>);
      <span class="hljs-built_in">console</span>.log(p);

      <span class="hljs-comment">/*
      [[PromiseState]]: "fulfilled"
      [[PromiseResult]]: "success"
      */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-83">Promise.reject()返回一个失败的Promise对象</h4>
<pre><code class="hljs language-js copyable" lang="js">      p = <span class="hljs-built_in">Promise</span>.reject(<span class="hljs-string">"failed"</span>);
      p.catch(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> <span class="hljs-built_in">console</span>.log(err));
      <span class="hljs-built_in">console</span>.log(p);

      <span class="hljs-comment">/*
       [[PromiseState]]: "rejected"
       [[PromiseResult]]: "failed"
      */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-84">Promise封装网络请求放到<code>网络</code>那一块</h4>
<blockquote>
<p>总结：Promise如何发挥作用？
相当于告诉你家保姆去做几件事：</p>
<blockquote>
<p>1.你先去超市买菜。<br>
2.用超市买回来的菜做饭。<br>
3.将做好的饭菜送到老婆单位。<br>
4.送到单位后打电话告诉我。<br></p>
</blockquote>
<p>我们知道，上面三步都是需要消耗时间的，我们可以理解为三个异步任务。利用 Promise 的写法来书写这个操作：</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//写好任务计划表</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> 买菜(<span class="hljs-params">resolve，reject</span>) </span>&#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        resolve([<span class="hljs-string">'西红柿'</span>、<span class="hljs-string">'鸡蛋'</span>、<span class="hljs-string">'油菜'</span>]);
    &#125;,<span class="hljs-number">3000</span>)
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> 做饭(<span class="hljs-params">resolve, reject</span>)</span>&#123;
    <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-comment">//对做好的饭进行下一步处理。</span>
        resolve (&#123;
            主食: <span class="hljs-string">'米饭'</span>,
            菜: [<span class="hljs-string">'西红柿炒鸡蛋'</span>、<span class="hljs-string">'清炒油菜'</span>]
        &#125;)
    &#125;,<span class="hljs-number">3000</span>) 
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> 送饭(<span class="hljs-params">resolve，reject</span>)</span>&#123;
    <span class="hljs-comment">//对送饭的结果进行下一步处理</span>
    resolve(<span class="hljs-string">'老婆的么么哒'</span>);
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> 电话通知我(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-comment">//电话通知我后的下一步处理</span>
    给保姆加<span class="hljs-number">100</span>块钱奖金;
&#125;

<span class="hljs-comment">//开始做任务</span>
<span class="hljs-comment">// 告诉保姆帮我做几件连贯的事情，先去超市买菜</span>
<span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(买菜)
<span class="hljs-comment">//用买好的菜做饭</span>
.then(<span class="hljs-function">(<span class="hljs-params">买好的菜</span>)=></span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(做饭);
&#125;)
<span class="hljs-comment">//把做好的饭送到老婆公司</span>
.then(<span class="hljs-function">(<span class="hljs-params">做好的饭</span>)=></span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(送饭);
&#125;)
<span class="hljs-comment">//送完饭后打电话通知我</span>
.then(<span class="hljs-function">(<span class="hljs-params">送饭结果</span>)=></span>&#123;
    电话通知我();
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<ul>
<li>请一定要谨记：如果我们的后续任务是异步任务的话，必须return 一个 新的 promise 对象。</li>
<li>如果后续任务是同步任务，只需 return 一个结果即可。</li>
<li>我们上面举的例子，除了电话通知我是一个同步任务，其余的都是异步任务，异步任务 return 的是 promise对象。</li>
</ul>
</blockquote>
<h2 data-id="heading-85">十三.async 函数</h2>
<blockquote>
<p>async和await是Promise的语法糖 <br>
async是对函数的一个修饰，使一个函数返回Promise实例。<br>
await是等待一个Promise实例成功后执行</p>
</blockquote>
<ul>
<li>1.执行async函数后可以写then</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-comment">//1.返回成功的</span>
        <span class="hljs-comment">//return Promise.resolve();</span>
        <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>;

        <span class="hljs-comment">// 2.返回失败的</span>
        <span class="hljs-comment">// return Promise.reject();</span>
        <span class="hljs-comment">// throw new Error("我错了");</span>
      &#125;
      <span class="hljs-built_in">console</span>.log(foo()); <span class="hljs-comment">//Promise实例</span>
      
      foo().then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
        <span class="hljs-built_in">console</span>.log(res); <span class="hljs-comment">//1</span>
      &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>2.必须在async函数里面使用await</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">      P1 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          resolve(<span class="hljs-string">"ok"</span>);
        &#125;, <span class="hljs-number">2000</span>);
      &#125;);

      <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">func</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-comment">/*
        代码的含义:是等待p1实例状态成功了才去执行await后面的代码，
        相当于then里面的的成功处理语句
        */</span>
        <span class="hljs-keyword">let</span> result = <span class="hljs-keyword">await</span> P1;
        <span class="hljs-built_in">console</span>.log(result);
      &#125;
      func();
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-86">面试题：编写一个 sleep 函数，让其等待 1000ms 后再去做其他事情？</h5>
<ul>
<li>方案一：用定时器</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sleep</span>(<span class="hljs-params">interval, callback</span>) </span>&#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> interval === <span class="hljs-string">"function"</span>) &#123;
          callback = interval;
          interval = <span class="hljs-number">2000</span>;
        &#125;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
          callback();
        &#125;, interval);
      &#125;
      sleep(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"我在2000ms之后执行"</span>);
      &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>方案二：函数返回值为Promise对象</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sleep</span>(<span class="hljs-params">interval = <span class="hljs-number">5000</span></span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
          <span class="hljs-built_in">setTimeout</span>(resolve, interval);
        &#125;);
      &#125;
      sleep(<span class="hljs-number">2000</span>).then(<span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"我在2000ms之后执行"</span>);
      &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>方案三:利用await语句</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sleep</span>(<span class="hljs-params">interval = <span class="hljs-number">1000</span></span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
          <span class="hljs-built_in">setTimeout</span>(resolve, interval);
        &#125;);
      &#125;
      (<span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">await</span> sleep();
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"我在1000ms之后执行"</span>);
        <span class="hljs-keyword">await</span> sleep(<span class="hljs-number">2000</span>);
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"我在2000ms之后执行"</span>);
        <span class="hljs-keyword">await</span> sleep(<span class="hljs-number">5000</span>);
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"我在5000ms之后执行"</span>);
      &#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-87">十四.Module 的语法</h2>
<blockquote>
<ul>
<li>ES6 模块的设计思想是尽量的静态化，使得编译时就能确定模块的依赖关系，以及输入和输出的变量。</li>
<li>模块功能主要由两个命令构成：export 和 import。export 命令用于规定模块的对外接口，import 命令用于输入其他模块提供的功能。</li>
</ul>
</blockquote>
<h3 data-id="heading-88">14.1 export 命令</h3>
<blockquote>
<p>一个模块就是一个独立的文件。该文件内部的所有变量，外部无法获取。如果你希望外部能够读取模块内部的某个变量，就必须使用 export 关键字输出该变量。下面是一个 JS 文件，里面使用 export 命令输出变量。</p>
</blockquote>
<h4 data-id="heading-89">1.输出变量</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// profile.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">var</span> firstName = <span class="hljs-string">'Michael'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">var</span> lastName = <span class="hljs-string">'Jackson'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">var</span> year = <span class="hljs-number">1958</span>

<span class="hljs-comment">//等同于下列代码</span>
<span class="hljs-keyword">var</span> firstName = <span class="hljs-string">'Michael'</span>
<span class="hljs-keyword">var</span> lastName = <span class="hljs-string">'Jackson'</span>
<span class="hljs-keyword">var</span> year = <span class="hljs-number">1958</span>

<span class="hljs-keyword">export</span> &#123; firstName, lastName, year &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码是 profile.js 文件，保存了用户信息。ES6 将其视为一个模块，里面用 export 命令对外部输出了三个变量。</p>
<h4 data-id="heading-90">2.输出函数或类（class）</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">multiply</span>(<span class="hljs-params">x, y</span>) </span>&#123;
  <span class="hljs-keyword">return</span> x * y;
&#125;;

通常情况下，<span class="hljs-keyword">export</span>输出的变量就是本来的名字，但是可以使用<span class="hljs-keyword">as</span>关键字重命名

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">v1</span>(<span class="hljs-params"></span>) </span>&#123; ... &#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">v2</span>(<span class="hljs-params"></span>) </span>&#123; ... &#125;

<span class="hljs-keyword">export</span> &#123;
  v1 <span class="hljs-keyword">as</span> streamV1,
  v2 <span class="hljs-keyword">as</span> streamV2,
  v2 <span class="hljs-keyword">as</span> streamLatestVersion
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另：export 语句输出的接口，与其对应的值是动态绑定关系，即通过该接口，可以取到模块内部实时的值。</p>
<h3 data-id="heading-91">14.2 import 命令</h3>
<blockquote>
<p>使用 export 命令定义了模块的对外接口以后，其他 JS 文件就可以通过 import 命令加载这个模块。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; firstName, lastName, year &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./profile.js'</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setName</span>(<span class="hljs-params">element</span>) </span>&#123;
  element.textContent = firstName + <span class="hljs-string">' '</span> + lastName
&#125;

<span class="hljs-comment">//import命令接受一对大括号，里面指定要从其他模块导入的变量名。大括号里面的变量名，</span>
<span class="hljs-comment">//必须与被导入模块（profile.js）对外接口的名称相同。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>如果想为输入的变量重新取一个名字，import 命令要使用 as 关键字，将输入的变量重命名。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; lastName <span class="hljs-keyword">as</span> surname &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./profile.js'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>import 命令输入的变量都是只读的，不允许在加载模块的脚本里面，改写接口。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; a &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./xxx.js'</span>
a = &#123;&#125; <span class="hljs-comment">// Syntax Error : 'a' is read-only;</span>

<span class="hljs-comment">// 但是如果a是一个对象，改写a的属性是允许的</span>
<span class="hljs-keyword">import</span> &#123; a &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./xxx.js'</span>
a.foo = <span class="hljs-string">'hello'</span> <span class="hljs-comment">// 合法操作</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>import 后面的 from 指定模块文件的位置，可以是相对路径，也可以是绝对路径。如果不带有路径，只是一个模块名，那么必须有配置文件，告诉 JavaScript 引擎该模块的位置。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; myMethod &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'util'</span>
<span class="hljs-comment">//  util是模块文件名，由于不带有路径，必须通过配置，告诉引擎怎么取到这个模块。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>import 命令具有提升效果，会提升到整个模块的头部，首先执行。</p>
</blockquote>
<h4 data-id="heading-92">模块的整体加载</h4>
<blockquote>
<p>除了指定加载某个输出值，还可以使用整体加载，即用星号（*）指定一个对象，所有输出值都加载在这个对象上面。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// circle.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">area</span>(<span class="hljs-params">radius</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.PI * radius * radius
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">circumference</span>(<span class="hljs-params">radius</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-number">2</span> * <span class="hljs-built_in">Math</span>.PI * radius
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> circle <span class="hljs-keyword">from</span> <span class="hljs-string">'./circle'</span>

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'圆面积：'</span> + circle.area(<span class="hljs-number">4</span>))
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'圆周长：'</span> + circle.circumference(<span class="hljs-number">14</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-93">export default 命令</h4>
<blockquote>
<p>为了给用户提供方便，让他们不需要知道所要加载的变量名或函数名，就能加载模块。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// export-default.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'foo'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>上面代码是一个模块文件 export-default.js，它的默认输出是一个函数。其他模块加载该模块时，import 命令可以为该匿名函数指定任意名字。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// import-default.js</span>
<span class="hljs-keyword">import</span> customName <span class="hljs-keyword">from</span> <span class="hljs-string">'./export-default'</span>
customName() <span class="hljs-comment">// 'foo'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>module章节内容参考掘金作者：小和山的菜鸟们，在这表示感谢！<a href="https://juejin.cn/post/6956085741977862152" target="_blank">文章传送门</a></p>
<h2 data-id="heading-94">十五.剩余章节(未完待续)</h2>
<p>Class、Generator 函数、Proxy未完待续.....</p></div>  
</div>
            