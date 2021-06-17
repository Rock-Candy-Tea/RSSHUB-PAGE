
---
title: '原来JavaScript是这样实现模块区分的！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1755'
author: 掘金
comments: false
date: Wed, 16 Jun 2021 01:34:05 GMT
thumbnail: 'https://picsum.photos/400/300?random=1755'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>这是我参与更文挑战的第<code>9</code>天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h2 data-id="heading-0">前言</h2>
<p>我们都知道代码模块化带来的好处有很多很多，但是在ES6以前的JavaScript中时没有代码<code>import</code>的概念的，那么他们又是怎么组合起来的呢？</p>
<h2 data-id="heading-1">立即执行函数</h2>
<p>看过<code>JQuery</code>源码的小伙伴都知道，<code>JQuery</code>是用一个<strong>立即执行函数</strong>包裹住代码，对外暴露部分变量供其他模块调用的，举个例子:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">window</span></span>) </span>&#123;
        <span class="hljs-keyword">const</span> Jq = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">target</span>) </span>&#123;
            <span class="hljs-built_in">this</span>.element = <span class="hljs-built_in">document</span>.querySelector(target);
        &#125;
        
        Jq.prototype.setBackground = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">color</span>) </span>&#123;
            <span class="hljs-built_in">this</span>.element.style.background = color;
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>;
        &#125;
        
        <span class="hljs-comment">// 对外抛出 $ 方法</span>
        <span class="hljs-built_in">window</span>.$ = <span class="hljs-function">(<span class="hljs-params">target</span>) =></span> <span class="hljs-keyword">new</span> Jq(target)
        
    &#125;)(<span class="hljs-built_in">window</span>)
    
    $(<span class="hljs-string">'body'</span>).setBackground(<span class="hljs-string">'red'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码的意思是声明了一个函数并<strong>立即调用</strong>，通过传入的<code>window</code>对象向外部暴露我们想要暴露的变量或方法。这就是一个简单的模块化的体现。<br>
这样的好处就是可以将一些变量和方法私有化。但它的坏处也很明显：不提供依<strong>赖管理机制</strong>；对外暴露方法只能通过全局对象实现。<br>
这样的简单模块化工具显然不能满足我们复杂的系统设计的需求。</p>
<h2 data-id="heading-2">显式模块声明</h2>
<p>从上面立即执行函数对外暴露的方法可以看出，对外暴露方法只能通过传入的全局对象才能向外部暴露方法或变量。如果我们可以将想要暴露的数据<strong>集合起来统一返回</strong>，那就最好了。而且这样的实现貌似也不难，继续来写一个简单的方法：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">const</span> <span class="hljs-built_in">module</span> = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sum</span>(<span class="hljs-params">a, b</span>) </span>&#123; <span class="hljs-keyword">return</span> a + b &#125;;
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">multiply</span>(<span class="hljs-params">a, b</span>) </span>&#123; <span class="hljs-keyword">return</span> a * b &#125;;
        
        <span class="hljs-keyword">return</span> &#123;
            sum,
            multiply,
        &#125;
    &#125;()
    
    <span class="hljs-built_in">module</span>.sum(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>); <span class="hljs-comment">// 3</span>
    <span class="hljs-built_in">module</span>.sum(<span class="hljs-number">2</span>, <span class="hljs-number">3</span>); <span class="hljs-comment">// 6</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们用一个变量来装函数的返回值。这样我们就可以访问这个声明的变量去调用返回的方法。达到<strong>代码复用</strong>和<strong>代码封装</strong>的功能。<br>
但是与立即执行函数一样，它也不提供<strong>模块管理机制</strong>。</p>
<h2 data-id="heading-3">什么是模块管理机制</h2>
<p>上面有两次都提到了<strong>模块管理机制</strong>，现在来简单了解一下。<br>
在以前写JavaScript的时候，如果需要引用其他JS文件，是需要在HTML文件中添加<code><script src="..."></script></code>标签引入的，在JS文件没有找到很好的办法去引入。当我们需要用到很多的模块文件时，那么管理模块时也必然会乱。<br>
所以需要引入一种<strong>约定</strong>，在JS文件中也能实现<strong>模块的引用</strong>，就比如说<code>import</code>和<code>export</code>提供引入和输出，<code>require</code>和<code>module.export</code>也是一样，这就是<code>模块管理机制</code>。</p>
<h2 data-id="heading-4">异步模块定义(AMD)</h2>
<p>了解完模块管理机制的概念，下面来看一种引入了模块管理机制的模块化方案。<br>
<code>异步模块定义(Asynchronous Module Definition)</code>，从名字可以看到，它是用异步去加载模块的。而且他是基于<a href="https://requirejs.org/" target="_blank" rel="nofollow noopener noreferrer">RequireJS</a>的，来看下面的代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-comment">// moduleA.js</span>
    define(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">TEST</span>: <span class="hljs-string">'test moduleA'</span>
        &#125;
    &#125;)
    
    <span class="hljs-comment">// main.js</span>
    <span class="hljs-built_in">require</span>.config(&#123;
      <span class="hljs-attr">baseUrl</span>: <span class="hljs-string">'js'</span>,
      <span class="hljs-attr">paths</span>: &#123;
        <span class="hljs-string">"testModule"</span>: <span class="hljs-string">"./moduleA"</span>,
      &#125;
    &#125;)
    <span class="hljs-built_in">require</span>([<span class="hljs-string">'testModule'</span>], <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">moduleA</span>) </span>&#123;
        <span class="hljs-keyword">const</span> test = moduleA();
        <span class="hljs-built_in">console</span>.log(test.TEST); <span class="hljs-comment">// test moduleA</span>
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码声明了两个js文件，<code>moduleA.js</code>是定义的模块文件，使用<code>define</code>方法定义模块。<br>
<strong>main.js</strong>中使用<code>require</code>方法引入定义的模块。<code>require.config</code>定义引入的配置。<br>
<code>require</code>方法接收两个参数：<code>模块数组</code>和<code>引入成功后的回调函数</code>，当定义的模块加载完成后，调用回调函数。<br>
从上面例子可以看到，它提供一种<code>模块管理机制</code>，允许我们在js文件中<strong>引入其他的js文件</strong>，而不再是从HTML的<code><script></code>标签引入。除此之外，AMD还有如下优点：</p>
<ul>
<li>采用异步方式加载模块，模块的加载不影响它后面语句的运行。</li>
<li>所有依赖这个模块的语句，都定义在一个回调函数中，等到加载完成之后，这个回调函数才会运行。</li>
</ul>
<p>AMD虽然可以做到异步加载，但是它也是会有缺点的：</p>
<ul>
<li>它<strong>不能做到按需加载</strong>，而是必须提前加载所有的依赖。</li>
</ul>
<h2 data-id="heading-5">共同模块定义(CMD)</h2>
<p><code>共同模块定义(Common Module Definition)</code>也是一种异步模块定义规范。<br>
CMD定义模块的方法是<code>define(factory)</code>，如果 factory 是一个函数，回调函数中会指定三个参数 <strong>require</strong>，<strong>exports</strong>，<strong>module</strong><br>
<code>require</code>是一个函数，这个函数接收一个模块标识符（模块 id），返回的是导出模块的API。
<code>exports</code>提供在模块执行时添加模块 API 的对象。
<code>module</code>是一个对象，提供<code>exports</code>，<code>dependencies</code>，<code>uri</code>方法，具体了解可以点击<a href="https://www.cnblogs.com/mybilibili/p/10411159.html#31-%E6%A8%A1%E5%9D%97%E5%AE%9A%E4%B9%89" target="_blank" rel="nofollow noopener noreferrer">这里</a>。<br>
下面是使用cmd定义模块的伪代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    define(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">require</span>, <span class="hljs-keyword">export</span>, <span class="hljs-built_in">module</span></span>) </span>&#123;
        <span class="hljs-keyword">const</span> md = <span class="hljs-built_in">require</span>(<span class="hljs-string">'modulePath'</span>);
        <span class="hljs-keyword">const</span> result = md[ moduleFunction ].get();
        <span class="hljs-built_in">module</span>.exports = &#123;
            result
        &#125;
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>CMD是<a href="https://seajs.github.io/seajs/docs/" target="_blank" rel="nofollow noopener noreferrer">SeaJS</a>在推广过程中对模块定义的规范化产出，具体例子可以看到SeaJs的<a href="https://seajs.github.io/seajs/docs/#quick-start" target="_blank" rel="nofollow noopener noreferrer">使用文档</a>。</p>
<h3 data-id="heading-6">与AMD的区别</h3>
<p>AMD与CMD都是异步模块定义规范，但是他们也会存在一些区别：</p>
<ul>
<li>对于模块的依赖，AMD是提前执行，CMD是延时执行。</li>
<li>AMD推崇<strong>依赖前置</strong>，CMD推崇<strong>就近依赖</strong>。</li>
</ul>
<p><strong>依赖前置</strong>：在定义模块的时候要先声明其依赖的模块，就像这样：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-built_in">require</span>([<span class="hljs-string">'module'</span>], <span class="hljs-function">() =></span> &#123;...&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>就近依赖</strong>：可以在在使用时引入依赖的模块</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    define(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"><span class="hljs-built_in">require</span>, <span class="hljs-keyword">export</span>, <span class="hljs-built_in">module</span></span>) </span>&#123;
        ...
        <span class="hljs-keyword">const</span> md = <span class="hljs-built_in">require</span>(<span class="hljs-string">'modulePath'</span>);
        ...
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">CommonJs</h2>
<p><a href="http://wiki.commonjs.org/wiki/Modules/1.1" target="_blank" rel="nofollow noopener noreferrer">CommonJs</a>也是一种模块定义规范，node的模块系统就是基于<code>CommonJs</code>的。</p>
<ul>
<li>在<code>CommonJs</code>中每一个文件就是一个模块，拥<strong>有自己独立的作用域，变量，以及方法</strong>等，对其他的模块都不可见。</li>
<li><code>CommonJS</code>规范规定，每个模块内部，<code>module</code>变量代表当前模块。这个变量是一个对象，它的<code>module.exports</code>属性是对外的接口。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-comment">// module.js</span>
    <span class="hljs-built_in">module</span>.exports = &#123;
        ...
        ...
    &#125;
    
    <span class="hljs-comment">// main.js</span>
    <span class="hljs-keyword">const</span> md = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./module.js'</span>);
    ...
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>加载某个模块，其实是加载该模块的<code>module.exports</code>属性。<code>require</code>方法用于加载模块。</li>
</ul>
<p>需要注意的是，CommonJs是<strong>同步加载</strong>，而上面提到的<code>AMD</code>,<code>UMD</code>是异步加载。</p>
<h2 data-id="heading-8">通用模块定义(UMD)</h2>
<p><code>通用模块定义(Universal Module Definition)</code>把前端和后端的模块加载融合在一起了，他提供了一个前后端统一的解决方案。支持<strong>AMD</strong>和<strong>CommonJS</strong>模式。UMD的实现其实很简单，前面我们已经了解了<code>AMD</code>还是<code>CommonJs</code>，那么UMD就是提供了一个方法判断是前端加载还是后端加载，主要的判断步骤是:</p>
<ul>
<li>先判断是否支持Node.js模块格式（exports是否存在），存在则使用Node.js模块格式。</li>
<li>再判断是否支持AMD（define是否存在），存在则使用AMD方式加载模块。</li>
<li>前两个都不存在，则将模块公开到全局（window或global）。</li>
</ul>
<h2 data-id="heading-9">ES6中的模块</h2>
<p>ES6中使用了<code>import</code>，<code>export</code>来实现模块的引入和导出代码，模块加载分为<strong>静态加载</strong>和<strong>动态加载</strong>。<br>
静态加载时，ES6规定<code>import</code><strong>必须放在代码顶层</strong>，因为import命令会被 JavaScript 引擎静态分析，先于模块内的其他模块执行。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">import</span> &#123;&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'modulePath'</span>;
    ...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的import语法显然是不能实现动态加载的动态加载，如果在某一些场景需要用到动态加载(例如动态路由)，那么应该怎么做呢？<br>
ES6提供一个<code>import()</code>函数，它可以在代码<strong>运行时动态引入模块</strong>，加载完成后会返回一个<code>Promise</code>。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">import</span>(<span class="hljs-string">'modulePath'</span>).then(<span class="hljs-function"><span class="hljs-params">module</span> =></span> &#123;
        ...
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">小结</h2>
<p>本文主要介绍了JavaScript是如何实现模块化的。<br>
前端使用模块化的定义有：<code>立即执行函数</code>，<code>显式模块声明</code>，<code>AMD</code>，<code>CMD</code>，<code>UMD</code><br>
node使用<strong>CommonJs</strong>进行模块化<br>
若文章中有不严谨或出错的地方请在评论区域指出。</p>
<h2 data-id="heading-11">参考</h2>
<ol>
<li>了不起的JavaScript工程师</li>
<li>JavaScript高级程序设计</li>
<li><a href="https://requirejs.org/" target="_blank" rel="nofollow noopener noreferrer">RequireJS</a></li>
<li><a href="https://seajs.github.io/seajs/docs/#quick-start" target="_blank" rel="nofollow noopener noreferrer">SeaJS</a></li>
</ol></div>  
</div>
            