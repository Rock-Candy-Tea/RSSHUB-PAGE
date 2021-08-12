
---
title: 'JS对象的增删改查、遍历以及解构赋值...'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5336'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 18:33:19 GMT
thumbnail: 'https://picsum.photos/400/300?random=5336'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1.对象的增删改查</h1>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> obj = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>()
<span class="hljs-comment">// 增</span>
        obj.name = <span class="hljs-string">'sss'</span>
        obj[<span class="hljs-string">'age'</span>] = <span class="hljs-number">16</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'obj'</span>, obj);
        <span class="hljs-comment">// 删</span>
        <span class="hljs-keyword">delete</span> obj.name
        <span class="hljs-keyword">delete</span> obj[<span class="hljs-string">'age'</span>]
        <span class="hljs-built_in">console</span>.log(obj);
        <span class="hljs-comment">// 改</span>
        obj.name = <span class="hljs-string">'lll'</span>
        obj[<span class="hljs-string">'age'</span>] = <span class="hljs-number">19</span>
        <span class="hljs-comment">// 查</span>
        <span class="hljs-built_in">console</span>.log(obj.name);
        <span class="hljs-built_in">console</span>.log(obj[<span class="hljs-string">'age'</span>]);
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">2.对象的遍历</h1>
<h2 data-id="heading-2">1.在JavaScript中对象和数组一样是可以遍历的</h2>
<h2 data-id="heading-3">2.什么是对象的遍历?</h2>
<blockquote>
<p>对象的遍历就是依次取出对象中所有的属性和方法</p>
</blockquote>
<h2 data-id="heading-4">3.如何遍历一个对象?</h2>
<blockquote>
<p>在JS中可以通过<strong>高级for循环</strong>来遍历对象</p>
</blockquote>
<p>以下代码的含义: 将指定对象中所有的属性和方法的名称取出来了依次的赋值给key这个变量
for(let key in obj)&#123;&#125;</p>
<blockquote>
<p>for...in...无法遍历原型对象中的属性和方法</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript">        <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span></span>&#123;
            <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">myName, myAge</span>)</span>&#123;
                <span class="hljs-built_in">this</span>.name = myName;
                <span class="hljs-built_in">this</span>.age = myAge;
            &#125;
            <span class="hljs-comment">// 注意点: ES6定义类的格式, 会将方法默认放到原型对象中</span>
            <span class="hljs-function"><span class="hljs-title">say</span>(<span class="hljs-params"></span>)</span>&#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name, <span class="hljs-built_in">this</span>.age);
            &#125;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript">         <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params">myName, myAge</span>)</span>&#123;
            <span class="hljs-built_in">this</span>.name = myName;
            <span class="hljs-built_in">this</span>.age = myAge;
            <span class="hljs-built_in">this</span>.say = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name, <span class="hljs-built_in">this</span>.age);
            &#125;
        &#125;
        <span class="hljs-keyword">let</span> p = <span class="hljs-keyword">new</span> Person(<span class="hljs-string">"LNJ"</span>, <span class="hljs-number">34</span>);
        <span class="hljs-built_in">console</span>.log(p);
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> key <span class="hljs-keyword">in</span> p)&#123;
            <span class="hljs-keyword">if</span>(p[key] <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Function</span>)&#123;
                <span class="hljs-comment">// 不输出函数</span>
                <span class="hljs-keyword">continue</span>;
            &#125;
            <span class="hljs-comment">// console.log(key); // name / age / say</span>
            <span class="hljs-comment">// 注意点: 以下代码的含义取出p对象中名称叫做当前遍历到的名称的属性或者方法的取值</span>
            <span class="hljs-built_in">console</span>.log(p[key]); <span class="hljs-comment">// p["name"] / p["age"] / p["say"]</span>
            <span class="hljs-comment">// 注意点: 以下代码的含义取出p对象中名称叫做key的属性的取值</span>
            <span class="hljs-comment">// console.log(p.key); // undefined</span>
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">3.对象的解构赋值</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2FME_GIRL%2Farticle%2Fdetails%2F119538668" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/ME_GIRL/article/details/119538668" ref="nofollow noopener noreferrer">数组的解构赋值</a></p>
<h2 data-id="heading-6">1.在对象的解构赋值中, 等号左边的格式必须和等号右边的格式一模一样, 才能完全解构</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> obj = &#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">"lnj"</span>,
            <span class="hljs-attr">age</span>: <span class="hljs-number">34</span>
        &#125;
        <span class="hljs-keyword">let</span> &#123;name, age&#125; = obj <span class="hljs-comment">// name = 'lnj';age = 34</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">2.在对象的解构赋值中, 两边的个数可以不一样</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> obj = &#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">"lnj"</span>,
            <span class="hljs-attr">age</span>: <span class="hljs-number">34</span>
        &#125;
        <span class="hljs-keyword">let</span> &#123;name&#125; = obj <span class="hljs-comment">// name = 'lnj'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">3.在对象的解构赋值中,如果右边少于左边, 我们可以给左边指定默认值</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> obj = &#123;
            <span class="hljs-attr">name</span>: <span class="hljs-string">"lnj"</span>,
            <span class="hljs-attr">age</span>: <span class="hljs-number">34</span>
        &#125;
        <span class="hljs-keyword">let</span> &#123;name, age, height = <span class="hljs-number">1.8</span>&#125; = obj
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>注意点:</code></p>
<blockquote>
<p>在对象<code>解构赋值</code>中, <code>左边的变量名称</code>必须和<code>对象的属性名称一致</code>, 才能解构出数据
顺序可以不一致，因为它会去匹配相同的属性名称</p>
</blockquote></div>  
</div>
            