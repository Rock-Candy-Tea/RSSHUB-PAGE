
---
title: 'js面试三之ES6'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3505'
author: 掘金
comments: false
date: Fri, 02 Jul 2021 05:56:10 GMT
thumbnail: 'https://picsum.photos/400/300?random=3505'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><h2 data-id="heading-0">一、变量相关（let、var、const、function）</h2>
<blockquote>
<ul>
<li>let和const都能够声明<code>块级作用域</code>，用法和var是类似的，let的特点是不会变量提升，而是被锁在当前块中。</li>
<li>const 声明的就是常量，保证<code>指针是固定</code>的;<code>声明并赋值</code></li>
</ul>
</blockquote>
<p><strong>let、const 与 var 的区别（五个）:</strong></p>
<blockquote>
<p>1.<code>重复声明</code>--- var 允许重复声明，let、const 不允许</p>
<blockquote>
</blockquote>
<p>2.<code>变量提升</code>---把当前作用域中所有带var、function关键字的进行提前的声明和定义 【预解析】</p>
<ul>
<li>var 会提升变量的声明到当前作用域的顶部; let、const 不存在变量提升.</li>
</ul>
<p>3.<code>块级作用域</code></p>
<blockquote>
<p>var 没有块级作用域，let/const 有块级作用域。若果在独立的&#123;&#125;（不含函数的花括号）内用let/const声明变量会形成块级作用域，不让外界访问。</p>
</blockquote>
<p>4.<code>暂时性死区</code></p>
<ul>
<li>只要作用域内存在 let、const，它们所声明的变量或常量就自动“绑定”这个区域，不再受到外部作用域的影响,let、const 存在暂时性死区</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> name=<span class="hljs-string">'jack'</span>;
&#123;
 name=<span class="hljs-string">'bob'</span>;
 <span class="hljs-keyword">let</span> name;    <span class="hljs-comment">//Uncaught ReferenceError: Cannot access 'name' before initialization</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>5.<code>window 对象的属性和方法</code>:</p>
<blockquote>
<p>全局作用域中，var 声明的变量，以及通过 function 声明的函数，会自动变成 window 对象的属性或方法,let、const 不会。</p>
</blockquote>
</blockquote>
<h2 data-id="heading-1">二.模板字符串</h2>
<ul>
<li>模板字符串用反引号表示，可以在里面直接使用字符串，还可以使用变量、表达式通过<code>$&#123;&#125;</code>注入</li>
<li>模板字符串中，所有的空格、换行或缩进都会被保留在输出之中</li>
</ul>
<h2 data-id="heading-2">三.箭头函数</h2>
<h3 data-id="heading-3">1.箭头函数的结构</h3>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">const</span>/<span class="hljs-keyword">let</span> 函数名 = 参数 => 函数体
      <span class="hljs-keyword">const</span> add = <span class="hljs-function">() =></span> &#123;&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">2.箭头函数简化---- 单个参数可以省略圆括号,单行函数体可省略花括号及return</h3>
<h3 data-id="heading-5">3.this 指向</h3>
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
    箭头函数没有自己的 <span class="hljs-built_in">this</span>，所以会从上级上下文一层一层的往外找<span class="hljs-built_in">this</span>，最后找到<span class="hljs-built_in">window</span>，他的<span class="hljs-built_in">this</span>指向<span class="hljs-built_in">window</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">4.不适用箭头函数的场景</h3>
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
<li>3.需要使用 arguments 的时候，不能用箭头函数，箭头函数中没有 arguments</li>
</ul>
<h2 data-id="heading-7">四.解构赋值</h2>
<blockquote>
<p>解构赋值是指解析某一数据的结构，将我们想要的东西提取出来，赋值给变量或常量；</p>
</blockquote>
<h3 data-id="heading-8">4.1 数组解构赋值(索引值相等和模式匹配)</h3>
<blockquote>
<p>数组解构赋值非常简单，遵循模式匹配原则和索引值相同的进行赋值就可以了，如果不需要结构的用逗号跳过即可。</p>
</blockquote>
<h4 data-id="heading-9">4.1.1 默认值，没有解构出来，就用默认值(惰性求值)</h4>
<blockquote>
<p>只有当一个数组成员严格等于（===）undefined 时，对应的默认值才会生效</p>
<pre><code class="hljs language-js copyable" lang="js">[a = <span class="hljs-number">1</span>, b = <span class="hljs-number">2</span>] = [<span class="hljs-number">3</span>, <span class="hljs-literal">undefined</span>];
<span class="hljs-comment">//a=3,b=2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<h4 data-id="heading-10">4.1.2 数组解构赋值应用</h4>
<ul>
<li>
<p>1.常见的类数组的解构赋值</p>
</li>
<li>
<p>2.函数参数的解构赋值</p>
</li>
<li>
<p>3.交换变量的值</p>
</li>
</ul>
<h3 data-id="heading-11">4.2 对象解构赋值（模式匹配和属性名相同）</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//属性名相同的完成赋值，可以取别名</span>
      <span class="hljs-keyword">const</span> &#123; age, <span class="hljs-attr">username</span>: uname &#125; = &#123; <span class="hljs-attr">username</span>: <span class="hljs-string">'Alex'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">18</span> &#125;;
      <span class="hljs-built_in">console</span>.log(age, uname);<span class="hljs-comment">//解构赋值之后再赋值给uname</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>默认值和数组的一样</p>
</li>
<li>
<p>如果将一个已经声明的变量用于对象的解构赋值，整个赋值需在圆括号中进行，防止被当成块级作用域</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">let</span> x = <span class="hljs-number">2</span>;
(&#123; x &#125; = &#123; <span class="hljs-attr">x</span>: <span class="hljs-number">1</span> &#125;);
<span class="hljs-built_in">console</span>.log(x);    <span class="hljs-comment">//1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-12">对象解构赋值的应用</h4>
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
<h3 data-id="heading-13">4.3 字符串的解构赋值</h3>
<ul>
<li>字符串可以按照数组形式的解构赋值</li>
<li>字符串可以按照类数组对象形式的解构赋值（可以按照索引值和length）</li>
</ul>
<h2 data-id="heading-14">五.对象字面量增强</h2>
<h3 data-id="heading-15">5.1 属性和方法简写</h3>
<p>在对象中属性名和值相等可以简写；方法可以直接写，也不用function声明</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> age=<span class="hljs-number">18</span>
<span class="hljs-keyword">const</span> obj=&#123;
            age,
            <span class="hljs-function"><span class="hljs-title">fn</span>(<span class="hljs-params"></span>)</span>&#123;&#125;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">5.2.方括号语法增强--属性名可以写变量啦</h3>
<blockquote>
<p>1.方括号语法可以写在对象字面量中</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">const</span> name = <span class="hljs-number">123</span>;
      <span class="hljs-keyword">const</span> obj = &#123;
        [<span class="hljs-string">"age"</span>]: <span class="hljs-number">18</span>,
        [name]: <span class="hljs-string">"蔡徐坤"</span>,
      &#125;;
      <span class="hljs-built_in">console</span>.log(obj);<span class="hljs-comment">//&#123;123: "蔡徐坤", age: 18&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">六、函数参数默认值-可以给形参设置默认值，不传参则使用默认值</h2>
<h2 data-id="heading-18">七.剩余参数与展开运算符</h2>
<p>剩余/扩展运算符同样也是ES6一个非常重要的语法，使用3个点（...），后面跟着一个含有iterator接口的数据结构</p>
<h3 data-id="heading-19">7.1 剩余参数--参数变数组</h3>
<p>剩余参数可以将多余的实参组成一个数组，可以在函数形参的最后一个位置通过<code>...args</code>设置，</p>
<h4 data-id="heading-20">7.1.1 箭头函数的剩余参数</h4>
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
<h4 data-id="heading-21">7.1.2  剩余参数的应用</h4>
<ul>
<li>1.完成 add 函数</li>
<li>2.与解构赋值结合使用</li>
</ul>
<h3 data-id="heading-22">7.2 数组展开运算符---将一个数组转为用逗号分隔的参数序列，主要用于函数调用。</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Math</span>.min(...[<span class="hljs-number">3</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>]));
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-23">7.2.1 替代函数的 apply 方法</h4>
<p>由于扩展运算符可以展开数组，所以不再需要apply方法，将数组转为函数的参数了，apply方法第二个参数是数组实参。</p>
<h4 data-id="heading-24">7.2.2 数组展开运算符的应用</h4>
<ul>
<li>1.复制数组（深拷贝）</li>
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
<h3 data-id="heading-25">7.3 对象展开运算符的基本用法</h3>
<p>对象的扩展运算符（...）用于取出参数对象的所有可遍历属性，拷贝到当前对象之中。</p>
<h4 data-id="heading-26">1. 展开对象(深拷贝对象)</h4>
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
<h4 data-id="heading-27">2.合并对象，后面的同属姓名会覆盖前面的</h4>
<h4 data-id="heading-28">3. 用户参数和默认参数合并，默认参数写前面，用户参数写后面</h4>
<h4 data-id="heading-29">4.注意事项---如果展开的不是对象，则会自动将其转为对象，再将其属性罗列出来，类数组对象<br></h4>
<h2 data-id="heading-30">八.Symbol唯一值</h2>
<blockquote>
<p>ES6新规定的Symbol(符号)是原始值，且符号实例唯一、不可变的，它的用途是确保对象属性使用唯一标识符。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//1.需要使用Symbol()函数初始化</span>
 <span class="hljs-keyword">let</span> name1 = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'liming'</span>);
 <span class="hljs-keyword">let</span> name2 = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'liming'</span>);
 <span class="hljs-built_in">console</span>.log(name1 == name2);  <span class="hljs-comment">//false</span>
 
<span class="hljs-comment">// 希望能够多次使用同一个symbol值</span>
 <span class="hljs-keyword">let</span> name1 = <span class="hljs-built_in">Symbol</span>.for(<span class="hljs-string">'name'</span>); <span class="hljs-comment">//检测到未创建后新建</span>
 <span class="hljs-keyword">let</span> name2 = <span class="hljs-built_in">Symbol</span>.for(<span class="hljs-string">'name'</span>); <span class="hljs-comment">//检测到已创建后返回</span>
 <span class="hljs-built_in">console</span>.log(name1 === name2); <span class="hljs-comment">// true</span>
 
<span class="hljs-comment">//能够访问的方法：Object.getOwnPropertySymbols.该方法会返回一个数组，成员是当前对象的所有用作属性名的Symbol值。</span>

 <span class="hljs-keyword">let</span> id = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">"id"</span>);
 <span class="hljs-keyword">let</span> obj = &#123;
  [id]:<span class="hljs-string">'symbol'</span>
 &#125;;
<span class="hljs-keyword">let</span> array = <span class="hljs-built_in">Object</span>.getOwnPropertySymbols(obj);
 <span class="hljs-built_in">console</span>.log(array); <span class="hljs-comment">//[Symbol(id)]</span>
 <span class="hljs-built_in">console</span>.log(obj[array[<span class="hljs-number">0</span>]]);  <span class="hljs-comment">//'symbol'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-31">九.Set 和 Map 数据结构</h2>
<h3 data-id="heading-32">9.1 Set数据结构---类似于数组（ value = key），但没有重复的值。</h3>
<p>Set 构造函数的参数--可以接受一个数组（或者具有 iterable 接口的其他数据结构如字符串、arguments、NodeList、Set）作为参数，用来初始化。</p>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">var</span> s2 = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]); 
      <span class="hljs-built_in">console</span>.log(s2, <span class="hljs-keyword">typeof</span> s2);   <span class="hljs-comment">//Set(3) &#123;1, 2, 3&#125; "object"</span>

<span class="hljs-comment">// 1. add添加成员（可以连写）</span>
      <span class="hljs-keyword">const</span> s = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>();
      s.add(<span class="hljs-number">1</span>).add(<span class="hljs-number">2</span>).add(<span class="hljs-number">2</span>);
      <span class="hljs-built_in">console</span>.log(s);<span class="hljs-comment">//&#123;1，2&#125;</span>
      
<span class="hljs-comment">// 2. has判断是否有某个成员</span>
      <span class="hljs-keyword">const</span> s = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-string">"ccc"</span>, <span class="hljs-string">"ssss"</span>, <span class="hljs-string">"dddd"</span>]);
      <span class="hljs-built_in">console</span>.log(s.has(<span class="hljs-string">"dddd"</span>)); <span class="hljs-comment">//true</span>
      
<span class="hljs-comment">// 3.delete删除某个成员</span>
      s.delete(<span class="hljs-string">"dddd"</span>);
      
<span class="hljs-comment">// 4. clear全部清除</span>
      s.clear();
      
<span class="hljs-comment">// 5.属性size--用来获取成员个数，相当于length</span>

<span class="hljs-comment">// 6.遍历操作（四个方法），Set 中 value = key</span>
    <span class="hljs-comment">// Set.prototype.keys()：返回键名的遍历器</span>
    <span class="hljs-comment">// Set.prototype.values()：返回键值的遍历器</span>
    <span class="hljs-comment">// Set.prototype.entries()：返回键值对的遍历器</span>
    <span class="hljs-comment">/*  
        Set.prototype.forEach()：使用回调函数遍历每个成员，有两个参数，
        第一个是回调函数，第二个是改变this指向
    */</span>
        <span class="hljs-keyword">const</span> s = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>([<span class="hljs-string">"蔡徐坤"</span>, <span class="hljs-string">"李易峰"</span>, <span class="hljs-string">"易烊千玺"</span>]);
        s.forEach(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">value, key, set</span>) </span>&#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>);<span class="hljs-comment">//document</span>
          <span class="hljs-built_in">console</span>.log(value, key, set === s);<span class="hljs-comment">//蔡徐坤 蔡徐坤 true</span>
       &#125;, <span class="hljs-built_in">document</span>);
      <span class="hljs-comment">// 按照成员添加进集合的顺序遍历</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-33">Set 应用</h4>
<blockquote>
<blockquote>
<p>① 数组或字符串去重时<br>
② 不需要通过下标访问，只需要遍历时<br>
③ 为了使用 Set 提供的方法和属性时（add delete clear has forEach size 等）</p>
</blockquote>
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
<h2 data-id="heading-34">十.Iterator 和 for...of 循环</h2>
<h3 data-id="heading-35">10.1 Iterator遍历器（迭代器）</h3>
<blockquote>
<p>Iterator 是 ES6 引入的一种新的遍历机制，凡是有Iterator接口的数据结构都是可遍历的，可以通过<code>for...of...</code>来遍历.</p>
</blockquote>
<h3 data-id="heading-36">10.2 为什么需要 Iterator 遍历器--for..of 来遍历</h3>
<p>我们之前的遍历方法是:</p>
<ul>
<li>遍历数组：for 循环和 forEach 方法</li>
<li>遍历对象：for in 循环</li>
</ul>
<p>而 Iterator 遍历器是一个统一的遍历方式，使用 Iterator 封装好的 for..of 来遍历,不管是数组还是对象都可以遍历</p>
<h3 data-id="heading-37">10.3 原生可遍历（有Iterator接口）</h3>
<blockquote>
<ul>
<li>数组</li>
<li>字符串</li>
<li>Set</li>
<li>Map</li>
<li>arguments</li>
<li>NodeList（一般用querySelectorAll获得的）</li>
</ul>
</blockquote>
<ul>
<li>一般的对象可以用for ... in遍历，也可以给他添加一个Symbol.iterator然后用for ... of 遍历</li>
</ul>
<h4 data-id="heading-38">10.2.1 for...of 遍历数组</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
<span class="hljs-comment">//1.遍历出索引值arr.keys() 得到的是索引的可遍历对象</span>
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">of</span> arr.keys()) &#123;
          <span class="hljs-built_in">console</span>.log(key);
       &#125;
<span class="hljs-comment">//2.遍历出值arr.values() 可以等价于arr</span>
<span class="hljs-comment">//3遍历出[index,value]用arr.entries() 得到的是索引+值组成的数组的可遍历对象</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-39">10.2.2  for...of 遍历普通对象<code>Object.entries(obj)</code></h4>
<h2 data-id="heading-40">十一.Es6新增方法</h2>
<h3 data-id="heading-41">11.1 Es6字符串新增方法(3个)</h3>
<h4 data-id="heading-42">1. includes()判断字符串中是否含有某些字符</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//判断字符串</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'abc'</span>.includes(<span class="hljs-string">'a'</span>, <span class="hljs-number">0</span>));<span class="hljs-comment">//true</span>
<span class="hljs-number">1.</span>第一个参数------表示是否包含该值
<span class="hljs-number">2.</span>第二个参数----- 表示开始搜索的位置，默认是 <span class="hljs-number">0</span>，index

<span class="hljs-comment">//判断数组</span>
 arr = [<span class="hljs-string">"name"</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>, <span class="hljs-number">7</span>, <span class="hljs-number">8</span>];
 <span class="hljs-built_in">console</span>.log(arr.includes(<span class="hljs-string">"name"</span>));<span class="hljs-comment">//true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-43">应用：给url添加参数，判断url有没有问号，有问号说明有<code>key=value</code>,再添加就直接添加连接符<code>&key=value</code></h5>
<h4 data-id="heading-44">2.padStart() 和 padEnd()在字符串本身的头部或尾部补全字符串长度</h4>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"abc"</span>.padStart(<span class="hljs-number">10</span>, <span class="hljs-string">"0123456789"</span>)); <span class="hljs-comment">//0123456abc</span>
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"abc"</span>.padEnd(<span class="hljs-number">10</span>, <span class="hljs-string">"0123456789"</span>)); <span class="hljs-comment">//abc0123456</span>
      <span class="hljs-comment">//  第一个参数表示补全后的字符串长度(有几个)，第二个参数是要用到的元素补全字符串</span>
      <span class="hljs-comment">// 如果省略第二个参数，默认使用空格补全长度</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-45">应用----显示日期格式</h5>
<h4 data-id="heading-46">3.trimStart() 和 trimEnd()清除字符串的首或尾空格</h4>
<pre><code class="hljs language-js copyable" lang="js">       <span class="hljs-keyword">const</span> s = <span class="hljs-string">'  a b c  '</span>;
       <span class="hljs-built_in">console</span>.log(s);
       <span class="hljs-built_in">console</span>.log(s.trimStart());
       <span class="hljs-built_in">console</span>.log(s.trimEnd());
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-47">应用-表单验证提交</h5>
<h3 data-id="heading-48">11.2 Es6数组新增方法（三个）</h3>
<h4 data-id="heading-49">1.includes()</h4>
<ul>
<li>判断数组中是否含有某个成员</li>
<li>第二个参数表示搜索的起始位置，默认值是 0</li>
</ul>
<h5 data-id="heading-50">应用-数组去重</h5>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">const</span> arr = [];
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> item <span class="hljs-keyword">of</span> [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">1</span>]) &#123;
        <span class="hljs-keyword">if</span> (!arr.includes(item)) &#123;
          arr.push(item);
        &#125;
      &#125;
      <span class="hljs-built_in">console</span>.log(arr); <span class="hljs-comment">//[1,2]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-51">2.Array.from()将类数组对象或可迭代对象转化为数组</h4>
<ul>
<li>
<p>一个类数组对象必须含有 length 属性，且元素属性名必须是数值或者可转换为数值的字符。</p>
</li>
<li>
<p>可迭代对象(数组、字符串、Set、Map、NodeList、arguments)。</p>
</li>
<li>
<p>元素属性名不为数值且无法转换为数值，返回长度为 length 元素值为 undefined 的数组</p>
</li>
<li>
<p><strong>第一个参数</strong>---能被转化的数据对象。</p>
</li>
<li>
<p><strong>第二个参数</strong>---作用类似于数组的 map 方法，用来对每个元素进行处理，将处理后的值放入返回的数组</p>
</li>
<li>
<p><strong>第三个参数</strong>--第二个参数为一般回调函数时，第三个参数可以改变 this 指向</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">let</span> a = &#123; 
          <span class="hljs-number">0</span>: <span class="hljs-string">"aaa"</span>, 
          <span class="hljs-number">1</span>: <span class="hljs-string">"bbb"</span>, 
          <span class="hljs-number">2</span>: <span class="hljs-string">"cccc"</span>, 
          <span class="hljs-number">3</span>: <span class="hljs-string">"ddd"</span>, 
          <span class="hljs-number">4</span>: <span class="hljs-string">"eeee"</span>, 
          <span class="hljs-attr">length</span>: <span class="hljs-number">5</span> 
        &#125;;
      <span class="hljs-keyword">let</span> array1 = <span class="hljs-built_in">Array</span>.from(a, <span class="hljs-function">(<span class="hljs-params">value</span>) =></span> value + <span class="hljs-string">"你真帅"</span>);
      <span class="hljs-built_in">console</span>.log(array1); <span class="hljs-comment">// ["aaa你真帅", "bbb你真帅", "cccc你真帅", "ddd你真帅", "eeee你真帅"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-52">3.find(callback)返回元素 和 findIndex()返回索引</h4>
<blockquote>
<p>find()：find()返回第一个匹配到的元素</p>
<blockquote>
<ul>
<li>1.find()方法依次对数组项中执行回调函数（条件判断语句），直至条件为 true，就返回该项（元素），找不到的话就返回undefined。</li>
<li>2.callback函数带有3个参数：当前元素的值、当前元素的索引，以及数组本身。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">     <span class="hljs-keyword">var</span> num = [<span class="hljs-number">10</span>, <span class="hljs-number">20</span>, <span class="hljs-number">30</span>, <span class="hljs-number">40</span>, <span class="hljs-number">50</span>, <span class="hljs-number">60</span>, <span class="hljs-number">70</span>, <span class="hljs-number">80</span>, <span class="hljs-number">90</span>];
     <span class="hljs-keyword">var</span> newNum1 = num.find(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123;
       <span class="hljs-keyword">return</span> item > <span class="hljs-number">40</span>;
     &#125;);
     <span class="hljs-built_in">console</span>.log(newNum1); <span class="hljs-comment">//50</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</blockquote>
<p>findIndex()用法结构类似，但是，返回数组中第一个满足条件的索引(从0开始), 不满足返回-1;</p>
</blockquote>
<h5 data-id="heading-53">应用-筛选数据</h5>
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
<h3 data-id="heading-54">11.3 Es6对象新增方法（2个）</h3>
<h4 data-id="heading-55">1.Object.assign()合并对象</h4>
<ul>
<li>Object.assign(目标对象, 源对象 1,源对象 2,...): 目标对象</li>
<li>Object.assign 直接合并到了第一个参数中，返回的就是合并后的对象</li>
</ul>
<h5 data-id="heading-56">应用--合并默认参数和用户参数</h5>
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
<h4 data-id="heading-57">2.Object.keys()、Object.values() 和 Object.entries()</h4>
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
<h5 data-id="heading-58">应用-和for...of...一起遍历对象</h5>
<pre><code class="hljs language-js copyable" lang="js">      obj = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"蔡徐坤"</span>, <span class="hljs-attr">age</span>: <span class="hljs-string">"18"</span>, <span class="hljs-attr">hobby</span>: [<span class="hljs-string">"唱歌"</span>, <span class="hljs-string">"写歌"</span>, <span class="hljs-string">"跳舞"</span>] &#125;;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.entries(obj));

      <span class="hljs-keyword">for</span> (key <span class="hljs-keyword">of</span> <span class="hljs-built_in">Object</span>.entries(obj)) &#123;
        <span class="hljs-built_in">console</span>.log(key[<span class="hljs-number">0</span>], key[<span class="hljs-number">1</span>]);
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-59">十二.Promise对象</h2>
<ul>
<li>Promise是ES6中新增的异步编程解决方案, 他是一个构造函数，在代码中通过<code>new Promise()</code>生成一个实例对象。精髓是通过状态调用用对应的回调函数。</li>
<li><code>Promise对象可以将异步操作以同步流程来表示, 避免了回调函数层层嵌套(回调地狱)。</code></li>
</ul>
<h3 data-id="heading-60">12.1 基本使用</h3>
<blockquote>
<p><code>第一步</code>：创建一个Promise实例对象，并传入<code>执行器函数</code>，执行器函数会同时执行</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//Promise是一个构造函数</span>
<span class="hljs-keyword">let</span> p = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(executor)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><code>第二步</code>：executor执行器函数接受<code>两个函数参数</code>，resolve和reject,这两个函数是改变Promise状态的;状态一旦改变既不可逆。</p>
<blockquote>
<ol>
<li>pending:  初始状态。</li>
<li>fulfilled(resolved): 只要调用resolve函数的状态, 表示操作成功。</li>
<li>rejected: 只要调用rejected函数，表示操作失败。</li>
<li>状态成功或失败都会调用对应成功或失败的回调函数。<code>.then(success()&#123;&#125;,failed()&#123;&#125;)</code></li>
</ol>
</blockquote>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> p=<span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>((resolve,reject)=&#123;
  <span class="hljs-comment">/* 
  执行器函数里面，一般存放的都是我们即将要处理的异步任务（比如网络请求），任务成功我们执行resolve吧数据传出去, 任务失败我们执行reject（当然写同步的也可以），之后根据状态就可以调用原型里面的三个方法
  */</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-61">12.2 Promise.prototype.then()方法的使用（可以多次使用）</h3>
<ul>
<li>
<p>then 方法接收两个<code>函数为参数</code>，第一个参数是 Promise 执行成功时的回调，第二个参数是 Promise 执行失败时的回调，两个函数只会有一个被调用。</p>
</li>
<li>
<p>then()方法执行后返回的是一个新的 Promise 对象,这个promise的状态由then里面执行的回调函数的返回值决定，返回值是非promise对象，他的状态就是成功的，返回值是promise对象，状态就由这个对象决定</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Promise对象的结构；</span>
&#123;
 [[PromiseState]]: <span class="hljs-string">"fulfilled"</span>
<span class="hljs-comment">//第一个由resolve或reject决定，后面执行的then返回的对象状态由当前函数返回值决定</span>
         
[[PromiseResult]]: <span class="hljs-string">"222"</span>
<span class="hljs-comment">//结果就是当前Promise对象调用then之后return的值，</span>
&#125;      
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<ul>
<li>可以通过上一个promise对象的then方法给下一个promise对象的then方法传递参数,传递的参数通过return返回给下一个promise对象的then方法。</li>
<li>如果第一次是reject（），会调用失败的回调函数，并且返回一个新的promise状态是成功的，那么我们想要让他状态失败怎么搞，在调用回调函数里面抛出错误<code>throw new Error(err);</code></li>
</ul>
</blockquote>
<blockquote>
<p>结论：
执行reject()的后果：</p>
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
<h3 data-id="heading-62">12.2 Promise.prototype.catch()方法的使用</h3>
<ul>
<li>.catch()专门监听失败的回调</li>
<li>如果需要分开监听,用<code>.then().catch()</code>方法使用链式编程，promise的状态如果是失败, 但是没有对应失败的监听就会报错<br></li>
<li>和then方法第二个参数的区别在于, catch方法可以捕获上一个promise对象then方法(也包括成功的回调的方法)中的异常。</li>
</ul>
<h4 data-id="heading-63">js异常处理</h4>
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
<h3 data-id="heading-64">12.3 Promise.all()方法的使用</h3>
<blockquote>
<p>参数:</p>
<ul>
<li>
<ol>
<li>all方法接收一个<code>数组</code>.</li>
</ol>
</li>
<li>
<ol start="2">
<li>如果数组中有多个Promise对象,只有<code>都成功</code>才会执行then方法,并且会按照添加的顺序, 将所有成功的结果重新打包到一个数组中返回给我们。</li>
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
<h3 data-id="heading-65">12.4 Promise.race()方法的使用</h3>
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
<h3 data-id="heading-66">12.5 Promise.resolve()和Promise.reject()方法的使用</h3>
<h4 data-id="heading-67">Promise.resolve()返回一个成功的Promise对象</h4>
<pre><code class="hljs language-js copyable" lang="js">      p = <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-string">"success"</span>);
      <span class="hljs-built_in">console</span>.log(p);

      <span class="hljs-comment">/*
      [[PromiseState]]: "fulfilled"
      [[PromiseResult]]: "success"
      */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-68">Promise.reject()返回一个失败的Promise对象</h4>
<pre><code class="hljs language-js copyable" lang="js">      p = <span class="hljs-built_in">Promise</span>.reject(<span class="hljs-string">"failed"</span>);
      p.catch(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> <span class="hljs-built_in">console</span>.log(err));
      <span class="hljs-built_in">console</span>.log(p);

      <span class="hljs-comment">/*
       [[PromiseState]]: "rejected"
       [[PromiseResult]]: "failed"
      */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-69">Promise封装网络请求放到<code>网络</code>那一块</h4>
<blockquote>
<p>总结：Promise如何发挥作用？</p>
</blockquote>
<ul>
<li>买菜（20分钟）-->做饭（30分钟）-->送饭（十分钟）-->通知；都是耗时的异步任务</li>
<li>搞很多函数（买菜函数、做饭函数、送饭函数、亲一个函数），均接受resolve函数参数，并在定时器里面执行resolve把做好了的事情发过去。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(买菜).then(<span class="hljs-function">(<span class="hljs-params">买好的菜</span>)=></span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(做饭);
&#125;).then(<span class="hljs-function">(<span class="hljs-params">做好的饭</span>)=></span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(送饭);
&#125;).then(<span class="hljs-function">(<span class="hljs-params">送饭结果</span>)=></span>&#123;
    老婆亲一个();
&#125;).catch(<span class="hljs-function"><span class="hljs-params">err</span>=></span><span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(err))
<span class="copy-code-btn">复制代码</span></code></pre>
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
<h2 data-id="heading-70">十三.async 函数</h2>
<blockquote>
<p>async和await是Promise的语法糖 <br>
async是对函数的一个修饰，使一个函数返回Promise实例。<br>
await是等待一个Promise实例成功后执行</p>
</blockquote>
<ul>
<li>1.给函数加上一个async修饰符之后，函数执行的结果是一个成功的promise对象，我们可以直接在函数执行语句后面用then。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">      <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-comment">//1.返回成功的</span>
        <span class="hljs-comment">//return Promise.resolve();</span>
        <span class="hljs-keyword">return</span> <span class="hljs-number">1</span>;

        <span class="hljs-comment">// 2.返回失败的</span>
        <span class="hljs-comment">// return Promise.reject();</span>
        <span class="hljs-comment">// throw new Error("我错了");</span>
      &#125;
 
      foo().then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
        <span class="hljs-built_in">console</span>.log(res); <span class="hljs-comment">//1</span>
      &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>2.await只能在async函数里面执行，否则会报错，它的含义是等待一个promise实例成功后执行。</li>
</ul>
<h5 data-id="heading-71">面试题：编写一个 sleep 函数，让其等待 1000ms 后再去做其他事情？</h5>
<ul>
<li>方案一：用定时器</li>
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
        <span class="hljs-comment">//买菜需要八秒</span>
        <span class="hljs-keyword">await</span> sleep(<span class="hljs-number">8000</span>);
        <span class="hljs-comment">//菜卖回来了通知我</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"我在1000ms之后执行"</span>);
        <span class="hljs-comment">//做饭需要两秒</span>
        <span class="hljs-keyword">await</span> sleep(<span class="hljs-number">2000</span>);
        <span class="hljs-comment">//饭做好了通知我</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"我在2000ms之后执行"</span>);
        <span class="hljs-comment">//吃饭需要5s</span>
        <span class="hljs-keyword">await</span> sleep(<span class="hljs-number">5000</span>);
        <span class="hljs-comment">//吃完饭了通知我</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"我在5000ms之后执行"</span>);
      &#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-72">十四.Module 的语法</h2>
<blockquote>
<p>一个模块就是一个独立的文件。该文件内部的所有变量，外部无法获取。如果你希望外部能够读取模块内部的某个变量，就必须使用 export 关键字输出该变量。下面是一个 JS 文件，里面使用 export 命令输出变量。</p>
</blockquote>
<h3 data-id="heading-73">变量或函数加载</h3>
<ul>
<li>若果要输出变量或函数，直接在其最前面加上export，而使用其他模块中变量时，则使用import引入</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//1.export 设置对外接口</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">var</span> name=<span class="hljs-string">'蔡徐坤'</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">multiply</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
<span class="hljs-keyword">export</span> &#123; firstName, lastName, year &#125;

<span class="hljs-comment">//import 命令加载这个模块（对外对内接口名相同）。</span>
<span class="hljs-comment">//import 命令输入的变量都是只读的，不允许在加载模块的脚本里面，改写接口。</span>
<span class="hljs-comment">//import 命令具有提升效果，会提升到整个模块的头部，首先执行。</span>
<span class="hljs-keyword">import</span> &#123; firstName, lastName, year &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./profile.js'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-74">模块的整体加载---<code>export default</code> 命令</h3>
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
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            