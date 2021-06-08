
---
title: 'JS中this的应用场景，再了解下apply、call和bind！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6066'
author: 掘金
comments: false
date: Sun, 06 Jun 2021 16:29:42 GMT
thumbnail: 'https://picsum.photos/400/300?random=6066'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h1 data-id="heading-0">this的应用场景，再了解下apply、call和bind</h1>
<p>这是我参与更文挑战的第7天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p>在写程序时，我们都知道 <code>this</code> 很好用，但是却很容易导致乱用。就像我刚开始学习箭头函数时，我知道这个箭头指代的是this，但是却不知道它往哪里指，所以在写程序时，就会想当然的乱写，导致有时候因为一个数据获取不到而疯狂找错，这无形之中要增加很大的时间成本，不懂原理胡来总是很容易事后两行泪(T_T)</p>
<p>在下面的这边文章中，将讲解关于this的几大应用场景以及了解在面试中经常会被问到的apply、bind和call究竟是什么，接下来开始进入本文的讲解。</p>
<h1 data-id="heading-1">一、谈谈对this对象的理解</h1>
<ul>
<li>
<p><code>this</code> ，函数执行的上下文，总是指向函数的<strong>直接调用者</strong>（而非间接调用者），可以通过 <code>apply</code> ， <code>call</code> ， <code>bind</code> 改变 <code>this</code> 的指向。</p>
</li>
<li>
<p>如果有 <code>new</code> 关键字，<code>this</code> 指向 <code>new</code> 出来的那个对象。</p>
</li>
<li>
<p>在事件中，<code>this</code> 指向触发这个事件的对象，特殊的是，<code>IE</code> 中的 <code>attachEvent</code> 中的 <code>this</code> 总是指向全局对象 <code>window</code> 。</p>
</li>
<li>
<p>对于匿名函数或者直接调用的函数来说，<code>this</code> 指向全局上下文（浏览器为 <code>window</code> ，<code>NodeJS</code> 为 <code>global</code>），剩下的函数调用，那就是谁调用它， <code>this</code> 就指向谁。</p>
</li>
<li>
<p>对于 <code>es6</code> 的箭头函数，箭头函数的指向取决于该箭头函数声明的位置，在哪里声明， this 就指向哪里。</p>
</li>
</ul>
<h1 data-id="heading-2">二、this的应用场景</h1>
<p><strong>在程序中，this主要有以下5种应用场景：</strong></p>
<ul>
<li>作为普通函数被调用</li>
<li>使用 <code>call</code> 、 <code>apply</code> 和 <code>bind</code> 被调用</li>
<li>作为对象方法被调用</li>
<li>在 <code>class</code> 方法中被调用</li>
<li>箭头函数中被调用</li>
</ul>
<h2 data-id="heading-3">1、作为普通函数被调用</h2>
<p>当 <code>this</code> 作为普通函数被调用时，指向 <code>window</code> 全局。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn1</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>);
&#125;

fn1(); <span class="hljs-comment">//window</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">2、使用call、apply和bind被调用</h2>
<p>当 <code>this</code> 使用 <code>call</code> 、 <code>apply</code> 和 <code>bind</code> 被调用时，直接指向作用域内的内容。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn1</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>);
&#125;

fn1(); <span class="hljs-comment">//window</span>

fn1.call(&#123; <span class="hljs-attr">x</span> : <span class="hljs-number">100</span> &#125;); <span class="hljs-comment">//&#123;x : 100&#125;</span>
fn1.apply(&#123;<span class="hljs-attr">x</span> : <span class="hljs-number">200</span>&#125;); <span class="hljs-comment">//&#123;x : 200&#125;</span>

<span class="hljs-keyword">const</span> fn2 = fn1.bind(&#123; <span class="hljs-attr">x</span> : <span class="hljs-number">200</span> &#125;);
fn2(); <span class="hljs-comment">//&#123; x : 200 &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">3、作为对象方法被调用</h2>
<p>从下面代码中可以得出，当 <code>this</code> 放在 <code>sayHi()</code> 方法里面时，此时作为 <code>zhangsan</code> 对象的方法被调用，指向的是当前的对象。而放在 <code>wait()</code> 方法时，里面还有一个定时器，定时器里面还有一个函数，所以第二个 <code>this</code> 是作为普通函数被调用，指向 <code>window</code> 全局。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> zhangsan = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'张三'</span>,
    <span class="hljs-function"><span class="hljs-title">sayHi</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-comment">//this 即当前对象</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>);
    &#125;,
    <span class="hljs-function"><span class="hljs-title">wait</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-comment">//this === window</span>
            <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>);
        &#125;);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">4、在class方法中被调用</h2>
<p>从以下代码中可以看出，当 <code>this</code> 在 <code>class</code> 中被调用时，指向的是整个对象。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">People</span></span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name</span>)</span>&#123;
        <span class="hljs-built_in">this</span>.name = name;
        <span class="hljs-built_in">this</span>.age = <span class="hljs-number">20</span>;
    &#125;
    <span class="hljs-function"><span class="hljs-title">sayHi</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>);
    &#125;
&#125;

<span class="hljs-keyword">const</span> zhangsan = <span class="hljs-keyword">new</span> People(<span class="hljs-string">'张三'</span>);
zhangsan.sayHi(); <span class="hljs-comment">//zhangsan 对象</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">5、箭头函数中被调用</h2>
<p>看到以下代码，细心的小伙伴不难发现，跟我们上面第3点看到的似乎有点类似，主要区别在于定时器中的函数改为了箭头函数。当改为箭头函数时，此时的this指向的是zhangsan这一个整个对象，而不再是指向全局。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> zhangsan = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'张三'</span>,
    <span class="hljs-function"><span class="hljs-title">sayHi</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-comment">//this 即当前对象</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>);
    &#125;,
    <span class="hljs-function"><span class="hljs-title">waitAgain</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-comment">//this 即当前对象</span>
            <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>);
        &#125;);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>讲完箭头函数，我们来梳理下箭头函数和普通函数的区别，以及箭头函数是否能当做是构造函数的问题。</p>
<p><strong>（1）箭头函数和普通函数定义</strong></p>
<p><strong>普通函数</strong>通过 <code>function</code> 关键字定义， <code>this</code> 无法结合<strong>词法作用域</strong>使用，在运行时绑定，只取决于函数的调用方式，在哪里被调用，调用位置。（取决于调用者，和是否独立运行）</p>
<p><strong>箭头函数</strong>使用被称为 “胖箭头” 的操作 => 定义，箭头函数不应用普通函数 <code>this</code> 绑定的<strong>四种规则</strong>，而是根据外层（函数或全局）的作用域来决定 <code>this</code> ，且箭头函数的绑定无法被修改（ <code>new</code> 也不行）。</p>
<p><strong>（2）箭头函数和普通函数的区别</strong></p>
<ul>
<li>箭头函数常用于回调函数中，包括事件处理器或定时器。</li>
<li>箭头函数和 <code>var self = this</code> ，都试图取代传统的 this 运行机制，将 this 的绑定拉回到词法作用域。</li>
<li>箭头函数没有原型、没有 <code>this</code> 、没有 <code>super</code>，没有 <code>arguments</code> ，没有 <code>new.target</code>。</li>
<li>箭头函数不能通过 <code>new</code> 关键字调用。
<ul>
<li>一个函数内部有两个方法：<code>[[Call]]</code> 和 <code>[[Construct]]</code>，在通过 <code>new</code> 进行函数调用时，会执行 <code>[[construct]]</code>  方法，创建一个实例对象，然后再执行这个函数体，将函数的 <code>this</code> 绑定在这个实例对象上。</li>
<li>当直接调用时，执行 <code>[[Call]]</code> 方法，直接执行函数体。</li>
<li>箭头函数没有 <code>[[Construct]]</code> 方法，不能被用作构造函数调用，当使用 <code>new</code> 进行函数调用时会报错。</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123; 
<span class="hljs-keyword">return</span> <span class="hljs-function">(<span class="hljs-params">a</span>) =></span> &#123; 
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.a); 
&#125; 
&#125;

<span class="hljs-keyword">var</span> obj1 = &#123; 
<span class="hljs-attr">a</span>: <span class="hljs-number">2</span> 
&#125;

<span class="hljs-keyword">var</span> obj2 = &#123; 
<span class="hljs-attr">a</span>: <span class="hljs-number">3</span> 
&#125;

<span class="hljs-keyword">let</span> bar1 = foo.call(obj1); <span class="hljs-comment">//2</span>
<span class="hljs-keyword">let</span> bar2 = bar.call(obj2); 
<span class="hljs-built_in">console</span>.log(bar2); <span class="hljs-comment">//undefind</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>（3）this绑定的四大规则</strong></p>
<p>this绑定四大规则<strong>遵循以下顺序：</strong></p>
<p><strong>New 绑定 > 显示绑定 > 隐式绑定 > 默认绑定</strong></p>
<p>下面一一介绍四大规则。</p>
<ul>
<li><strong>默认绑定</strong>：没有其他修饰（ <code>bind</code> 、 <code>apply</code> 、 <code>call</code> ），在非严格模式下定义指向全局对象，在严格模式下定义指向 <code>undefined</code> 。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123; 
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.a); 
&#125;
<span class="hljs-keyword">var</span> a = <span class="hljs-number">2</span>; 
foo(); <span class="hljs-comment">//undefined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>隐式绑定</strong>：调用位置是否有<strong>上下文对象</strong>，或者是否被某个对象拥有或者包含，那么隐式绑定规则会把函数调用中的 <code>this</code> 绑定到这个上下文对象。而且，对象属性链只有<strong>上一层或者最后一层</strong>在调用位置中起作用。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123; 
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.a); 
&#125;
<span class="hljs-keyword">var</span> obj = &#123; 
    <span class="hljs-attr">a</span>: <span class="hljs-number">2</span>, 
    <span class="hljs-attr">foo</span>: foo, 
&#125;
obj.foo(); <span class="hljs-comment">// 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>显式绑定</strong>：通过在函数上运行 <code>call</code> 和 <code>apply</code> ，来显式的绑定 <code>this</code> 。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params"></span>) </span>&#123; 
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.a); 
&#125;
<span class="hljs-keyword">var</span> obj = &#123; 
    <span class="hljs-attr">a</span>: <span class="hljs-number">2</span> 
&#125;;
foo.call(obj); <span class="hljs-comment">//2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>显示绑定之<strong>硬绑定</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params">something</span>) </span>&#123; 
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.a, something); 
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.a + something; 
&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bind</span>(<span class="hljs-params">fn, obj</span>) </span>&#123; 
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">return</span> fn.apply(obj, <span class="hljs-built_in">arguments</span>); 
    &#125;; 
&#125;
<span class="hljs-keyword">var</span> obj = &#123; 
    <span class="hljs-attr">a</span>: <span class="hljs-number">2</span> 
&#125;
<span class="hljs-keyword">var</span> bar = bind(foo, obj);
<span class="hljs-built_in">console</span>.log(bar); <span class="hljs-comment">//f()</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>New 绑定</strong>：<code>new</code> 调用函数会创建一个全新的对象，并将这个对象绑定到函数调用的 <code>this</code>。<code>New</code> 绑定时，如果是 <code>new</code> 一个硬绑定函数，那么会用 <code>new</code> 新建的对象替换这个硬绑定 <code>this </code> 。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">foo</span>(<span class="hljs-params">a</span>) </span>&#123; 
    <span class="hljs-built_in">this</span>.a = a; 
&#125;
<span class="hljs-keyword">var</span> bar = <span class="hljs-keyword">new</span> foo(<span class="hljs-number">2</span>); 
<span class="hljs-built_in">console</span>.log(bar.a); <span class="hljs-comment">//2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8"></h3>
<h1 data-id="heading-9">三、apply、call和bind</h1>
<h2 data-id="heading-10">1、apply、call和bind的共同用法</h2>
<p>先说下三者的共同用法，三者的共同用法就是可以改变<strong>函数</strong>的this指向，并将函数绑定到上下文中。接下来讲述一个应用场景加深理解：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> obj1 = &#123;
    <span class="hljs-attr">hobby</span>: <span class="hljs-string">'running'</span>,
    <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params">favorite</span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`在我的业余时间里，我喜欢<span class="hljs-subst">$&#123;favorite&#125;</span>，但同时我也喜欢<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.hobby&#125;</span>`</span>);
    &#125;
&#125;

<span class="hljs-keyword">let</span> obj2 = &#123;
    <span class="hljs-attr">hobby</span>: <span class="hljs-string">'learning'</span>
&#125;

obj1.add(<span class="hljs-string">'reading'</span>); <span class="hljs-comment">//在我的业余时间里，我喜欢reading，但同时我也喜欢running</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到在最后一行代码中，我们调用了 <code>obj1</code> 中的 <code>add</code> 函数，并传入了一个参数 <code>reading</code> 。 <code>add</code> 函数中的 <code>this</code> 指的是他所在的对象 <code>obj1</code> ，所以 <code>this.hobby</code> 就是 <code>running</code> ， 但是我们如果想获得 <code>obj2</code> 中的<code>hobby</code>， 又该怎么处理呢？这就涉及到我们平常所听到的 <code>apply</code> 、 <code>call</code> 和 <code>bind</code> 。</p>
<p>接下来开始讲解 <code>apply</code> 、 <code>call</code> 和 <code>bind</code> 。</p>
<h2 data-id="heading-11">2、apply</h2>
<p><strong>（1）语法：</strong> <code> Array.prototype.apply(this, [args1, args2])</code> 。</p>
<p><strong>（2）传入参数：</strong></p>
<p><strong>第一个参数</strong>：传入 <code>this</code> 需要指向的对象，即函数中的 <code>this</code> 指向谁，就传谁进来；</p>
<p><strong>第二个参数</strong>：传入一个数组，数组中包含了函数需要的实参。</p>
<p><strong>（3）apply的作用：①</strong>调用函数；<strong>②</strong>指定函数中 <code>this</code> 的指向。</p>
<p><strong>（4）代码演示：</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 
 * <span class="hljs-doctag">@description </span>实现apply函数，在函数原型上封装myApply函数, 实现和原生apply函数一样的效果
 */</span>

<span class="hljs-built_in">Function</span>.prototype.myApply = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">context</span>)</span>&#123;

    <span class="hljs-comment">// 存储要转移的目标对象</span>
    _this = context ? <span class="hljs-built_in">Object</span>(context) : <span class="hljs-built_in">window</span>;

    <span class="hljs-comment">// 在转移this的对象上设定一个独一无二的属性，并将函数赋值给它</span>
    <span class="hljs-keyword">let</span> key = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'key'</span>);
    _this[key] = <span class="hljs-built_in">this</span>;

    <span class="hljs-comment">// 将数组里存储的参数拆分开，作为参数调用函数</span>
    <span class="hljs-keyword">let</span> res = <span class="hljs-built_in">arguments</span>[<span class="hljs-number">1</span>] ? _this[key](...arguments[<span class="hljs-number">1</span>]) : _this[key]();

    <span class="hljs-comment">// 删除</span>
    <span class="hljs-keyword">delete</span> _this[key];

    <span class="hljs-comment">// 返回函数返回值</span>
    <span class="hljs-keyword">return</span> res;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>（5）前情回顾</strong></p>
<p>实现了 <code>myApply</code> 之后，我们继续引用刚开始关于爱好的那个例子，来修改 <code>this</code> 的指向。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> obj1 = &#123;
    <span class="hljs-attr">hobby</span>: <span class="hljs-string">'running'</span>,
    <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params">...favorite</span>)</span>&#123; <span class="hljs-comment">//...favorite意味着可以接收多个参数</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`在我的业余时间里，我喜欢<span class="hljs-subst">$&#123;favorite&#125;</span>，但同时我也喜欢<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.hobby&#125;</span>`</span>);
    &#125;
&#125;

<span class="hljs-keyword">let</span> obj2 = &#123;
    <span class="hljs-attr">hobby</span>: <span class="hljs-string">'learning'</span>
&#125;

obj1.add.myApply(obj2, [<span class="hljs-string">'reading'</span>, <span class="hljs-string">'working'</span>]); 

<span class="hljs-comment">// 输出结果：在我的业余时间里，我喜欢reading,working，但同时我也喜欢learning</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>obj1.add.myApply(obj2, ['reading', 'working'])</code> 这一行代码， 第一个参数将 <code>obj1</code> 中的 <code>add</code> 函数的 <code>this</code> 指向了 <code>obj2</code> ， 第二个参数以数组形式<strong>传入多个参数</strong>，作为 <code>obj1</code> 中的 <code>add</code> 函数传入的参数， 所以最后能将 <code>reading</code> 和 <code>working</code> 都输出。</p>
<h2 data-id="heading-12">3、call</h2>
<p><strong>（1）语法：</strong> <code>Array.prototype.call(this, args1, args2)</code></p>
<p><strong>（2）传入参数：</strong></p>
<p><strong>第一个参数</strong>：传入 <code>this</code> 需要指向的对象，即函数中的 <code>this</code> 指向谁，就传谁进来；</p>
<p><strong>其余参数</strong>： 除了第一个参数，其他的参数需要传入几个，就一个一个传递进来即可。</p>
<p><strong>（3）call的作用：①</strong>调用函数；<strong>②</strong>指定函数中 <code>this</code> 的指向。</p>
<p><strong>（4）代码演示：</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * 
 * <span class="hljs-doctag">@description </span>实现apply函数，在函数原型上封装myApply函数, 实现和原生apply函数一样的效果
 */</span>

<span class="hljs-built_in">Function</span>.prototype.myCall = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">context</span>)</span>&#123;

    <span class="hljs-comment">// 存储要转移的目标对象</span>
    <span class="hljs-keyword">let</span> _this = context ? <span class="hljs-built_in">Object</span>(context) : <span class="hljs-built_in">window</span>;

    <span class="hljs-comment">// 在转移this的对象上设定一个独一无二的属性，并将函数赋值给它</span>
    <span class="hljs-keyword">let</span>  key = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'key'</span>);
    _this[key] = <span class="hljs-built_in">this</span>;

    <span class="hljs-comment">// 创建空数组，存储多个传入参数</span>
    <span class="hljs-keyword">let</span> args = [];

    <span class="hljs-comment">// 将所有传入的参数添加到新数组中</span>
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i =<span class="hljs-number">1</span>; i < <span class="hljs-built_in">arguments</span>.length; i++)&#123;
        args.push(<span class="hljs-built_in">arguments</span>[i]);
    &#125;

    <span class="hljs-comment">// 将新数组拆开作为多个参数传入，并调用函数</span>
    <span class="hljs-keyword">let</span> res = _this[key](...args);

    <span class="hljs-comment">// 删除</span>
    <span class="hljs-keyword">delete</span> _this[key];

    <span class="hljs-comment">// 返回函数返回值</span>
    <span class="hljs-keyword">return</span> res;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>（5）前情回顾</strong></p>
<p>实现了 <code>myCall</code> 之后，我们继续引用刚开始关于爱好的那个例子，来修改 <code>this</code> 的指向。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> obj1 = &#123;
    <span class="hljs-attr">hobby</span>: <span class="hljs-string">'running'</span>,
    <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params">...favorite</span>)</span>&#123; <span class="hljs-comment">//...favorite意味着可以接收多个参数</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`在我的业余时间里，我喜欢<span class="hljs-subst">$&#123;favorite&#125;</span>，但同时我也喜欢<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.hobby&#125;</span>`</span>);
    &#125;
&#125;

<span class="hljs-keyword">let</span> obj2 = &#123;
    <span class="hljs-attr">hobby</span>: <span class="hljs-string">'learning'</span>
&#125;

obj1.add.myCall(obj2, <span class="hljs-string">'reading'</span>, <span class="hljs-string">'working'</span>);

<span class="hljs-comment">// 输出结果：在我的业余时间里，我喜欢reading,working，但同时我也喜欢learning</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>obj1.add.myCall(obj2, 'reading', 'working')</code> 这一行代码， 第一个参数将 <code>obj1</code> 中的 <code>add</code> 函数的 <code>this</code> 指向了 <code>obj2</code> ， 第二个参数通过依次<strong>传入多个参数</strong>的形式，作为 <code>obj1</code> 中的 <code>add</code> 函数传入的参数， 所以最后能将 <code>reading</code> 和 <code>working</code> 都输出。</p>
<p>讲到这里，我们来梳理下 <code>call</code> 和 <code>apply</code> 的区别：</p>
<p><code>call</code> 和 <code>apply</code> 唯一的区别就是在于<strong>给函数传入参数的形式不同</strong>， <code>call</code> 是将多个参数逐个传入， 而<code>apply</code> 是 将多个参数放在一个数组中，一起传入。</p>
<h2 data-id="heading-13">4、bind</h2>
<p><strong>（1）语法：</strong> <code> Array.prototype.bind(this, args1, args2)</code> 。</p>
<p><strong>（2）传入参数：</strong></p>
<p><strong>第一个参数</strong>：传入 <code>this</code> 需要指向的对象，即函数中的 <code>this</code> 指向谁，就传谁进来；</p>
<p><strong>其余参数</strong>： 除了第一个参数，其他参数的传递可以像 <code>apply</code> 一样的数组类型，也可以像 <code>call</code> 一样的逐个传入；但需注意的是后面需要<strong>加个小括号</strong>进行其余参数的传递。</p>
<p><strong>（3）call的作用：①</strong>克隆当前函数，返回克隆出来的新函数；<strong>②</strong>新克隆出来的函数，该函数的this被指定了。</p>
<p><strong>（4）代码演示：</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@description </span>实现Bind函数，在函数原型上封装myBind函数 , 实现和原生bind函数一样的效果
 * 
 */</span>

<span class="hljs-built_in">Function</span>.prototype.myBind = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">context</span>)</span>&#123;

    <span class="hljs-comment">// 存储要转移的目标对象</span>
    <span class="hljs-keyword">let</span> _this = context ? <span class="hljs-built_in">Object</span>(context) : <span class="hljs-built_in">window</span>;

    <span class="hljs-comment">// 在转移this的对象上设定一个独一无二的属性，并将函数赋值给它</span>
    <span class="hljs-keyword">let</span> key = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'key'</span>);
    _this[key] = <span class="hljs-built_in">this</span>;

    <span class="hljs-comment">// 创建函数闭包</span>
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;

        <span class="hljs-comment">// 将所有参数先拆分开，再添加到新数组中，以此来支持多参数传入以及数组参数传入的需求</span>
        <span class="hljs-keyword">let</span> args = [].concat(...arguments);

        <span class="hljs-comment">// 调用函数</span>
        <span class="hljs-keyword">let</span> res = _this[key](...args);

        <span class="hljs-comment">// 删除</span>
        <span class="hljs-keyword">delete</span> _this[key];

        <span class="hljs-comment">// 返回函数返回值</span>
        <span class="hljs-keyword">return</span> res;
    &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>（5）前情回顾</strong></p>
<p>实现了 <code>myBind</code> 之后，我们继续引用刚开始关于爱好的那个例子，来修改 <code>this</code> 的指向。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> obj1 = &#123;
    <span class="hljs-attr">hobby</span>: <span class="hljs-string">'running'</span>,
    <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params">...favorite</span>)</span>&#123; <span class="hljs-comment">//...favorite意味着可以接收多个参数</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`在我的业余时间里，我喜欢<span class="hljs-subst">$&#123;favorite&#125;</span>，但同时我也喜欢<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.hobby&#125;</span>`</span>);
    &#125;
&#125;

<span class="hljs-keyword">let</span> obj2 = &#123;
    <span class="hljs-attr">hobby</span>: <span class="hljs-string">'learning'</span>
&#125;

obj1.add.myBind(obj2)([<span class="hljs-string">'reading'</span>, <span class="hljs-string">'working'</span>]);

<span class="hljs-comment">// 输出结果：在我的业余时间里，我喜欢reading,working，但同时我也喜欢learning</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过以上我们可以看到， <code>bind</code> 有点类似 <code>apply</code> 和 <code>call</code> 的结合，只不过它返回的是一个函数，需要自身再进行一次调用， 而传给这个函数的参数形式有两种方式，可以是像 <code>apply</code> 一样的数组形式， 也可以是像 <code>call</code> 一样的逐个传入的形式。</p>
<p>大家不要觉得这个后面加个小括号太麻烦，这就是 <code>bind</code> 的强大之处，有时候 <code>bind </code>也会经常运用在<strong>函数柯里化</strong>中。</p>
<p>讲到这里，关于this的相关知识就讲完啦！接下来我们来做个总结。</p>
<h2 data-id="heading-14">5、做个小结</h2>
<ul>
<li>
<p><code>this</code> 取什么样的值，是在函数执行时确定的，不是在函数定义的时候确定的。</p>
</li>
<li>
<p><code>apply</code> 、<code>call</code> 、<code>bind</code> 三者都是函数的方法，都可以改变函数的 <code>this</code> 指向。</p>
</li>
<li>
<p><code>apply</code> 和 <code>call</code> 都是改变函数 <code>this</code> 指向，并传入参数后立即调用执行该函数。</p>
</li>
<li>
<p><code>bind</code> 是在改变函数 <code>this</code> 指向后，并传入参数后返回一个新的函数，不会立即调用执行。</p>
</li>
<li>
<p><code>apply</code> 传入的参数是数组形式的，<code>call</code> 传入的参数是按顺序的逐个传入并以逗号隔开， <code>bind</code> 传入的参数既可以是数组形式，也可以是按顺序逐个传入。</p>
</li>
</ul>
<h1 data-id="heading-15">四、结束语</h1>
<p>关于 <code>this</code> 的指向问题在前端的面试中尤为常见，大家可以按照上文中的顺序把 <code>this</code> 的知识点串联起来一起理解！同时，本文内容为本人理解所整理，可能会存在边界歧义等问题。如果有不理解或者有误的地方欢迎评论区评论或私信我交流~</p>
<blockquote>
<ul>
<li>
<p>关注公众号 <strong>星期一研究室</strong> ，不定期分享学习干货</p>
</li>
<li>
<p>如果这篇文章对你有用，记得<strong>点个赞加个关注</strong>再走哦~</p>
</li>
</ul>
</blockquote></div>  
</div>
            