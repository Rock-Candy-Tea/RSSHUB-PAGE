
---
title: 'JS数组奇淫巧技'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=470'
author: 掘金
comments: false
date: Fri, 06 Aug 2021 06:35:10 GMT
thumbnail: 'https://picsum.photos/400/300?random=470'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第6天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<blockquote>
<p>本文主要记录关于数组操作的“常规操作”，助您工作更顺心，emmm，明天又是要学习一天提升自己的黄金时刻啦~~加油</p>
</blockquote>
<h2 data-id="heading-0">基本操作中常见情况</h2>
<p>主要涉及到数组的一些常用方法，也是开发中使用频率较高的，本文适合对数组的方法有一定理解的朋友阅读🈷</p>
<h3 data-id="heading-1">伪数组转数组</h3>
<ul>
<li>
<p>推荐用法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> ArrLike = &#123;<span class="hljs-number">0</span>: <span class="hljs-string">'hello'</span>, <span class="hljs-number">1</span>: <span class="hljs-string">'world'</span>, <span class="hljs-attr">length</span>: <span class="hljs-number">2</span>&#125;
<span class="hljs-comment">// Array.from(ArrLike) 可以返回一个数组， 参数是：拥有 length 属性的对象或可迭代的对象。</span>
<span class="hljs-built_in">Array</span>.from(ArrLike)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>替代方案</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// [].slice.call(ArrLike, 0, 0)// 0, 0 默认不写也行</span>
[].slice.call(ArrLike)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-2">数组降维</h3>
<ul>
<li>
<p>推荐用法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Arr = [[<span class="hljs-number">111</span>, <span class="hljs-number">2</span>, <span class="hljs-number">33</span>], [<span class="hljs-number">55</span>, <span class="hljs-number">66</span>, <span class="hljs-number">77</span>], &#123;<span class="hljs-attr">key</span>: <span class="hljs-string">'value'</span>&#125; ]
<span class="hljs-comment">// Arr.flat(n) - n 默认为2，为 Infinity 时 可展开任意层</span>
Arr.flat()<span class="hljs-comment">// [222, 333, 444, 55, 66, 77, &#123;…&#125;]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>替代方案</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 先字符串化 再分割，缺点也明显，新数组中对象没有正确的得到</span>
Arr.join().split(<span class="hljs-string">','</span>)<span class="hljs-comment">//  ["111", "2", "33", "55", "66", "77", "[object Object]"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-3">数组去重</h3>
<ul>
<li>
<p>推荐用法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>]
<span class="hljs-comment">// 使用Set()</span>
[...new <span class="hljs-built_in">Set</span>(Arr)]
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-4">数组合并</h3>
<ul>
<li>
<p>推荐用法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Arr1 = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>], Arr2 = [<span class="hljs-number">4</span>, <span class="hljs-number">5</span>, <span class="hljs-number">6</span>];
<span class="hljs-comment">// 扩展运算符合并的数组是浅拷贝</span>
[...Arr1, ...Arr2]<span class="hljs-comment">// [1, 2, 3, 4, 5, 6]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>替代方案</p>
<pre><code class="hljs language-js copyable" lang="js">Arr1.concat(Arr2)
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-5">交换变量</h3>
<ul>
<li>
<p>推荐用法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 不使用第三个变量，就能完成交换赋值</span>
[a, b] = [b, a]
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-6">数组求和</h3>
<ul>
<li>
<p>推荐用法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>]
Arr.reduce(<span class="hljs-function">(<span class="hljs-params">sum, num</span>) =></span> sum += num, <span class="hljs-number">0</span>)<span class="hljs-comment">// 10</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h2 data-id="heading-7">数组循环方法的使用</h2>
<p>用了下面的方法，再也不用想着for循环了，开心😄</p>
<h3 data-id="heading-8">由原数组生成任意想要生成的新数组</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> Users = [&#123;<span class="hljs-attr">id</span>:  <span class="hljs-number">1</span>,<span class="hljs-attr">name</span>: <span class="hljs-string">'aYin'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">26</span>, <span class="hljs-attr">sex</span>: <span class="hljs-string">'male'</span>&#125;, &#123;<span class="hljs-attr">id</span>: <span class="hljs-number">2</span>,<span class="hljs-attr">name</span>: <span class="hljs-string">'zz'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">23</span>, <span class="hljs-attr">sex</span>: <span class="hljs-string">'female'</span>&#125;, &#123;<span class="hljs-attr">id</span>:  <span class="hljs-number">3</span>,<span class="hljs-attr">name</span>: <span class="hljs-string">'aYin'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">26</span>, <span class="hljs-attr">sex</span>: <span class="hljs-string">'male'</span>&#125;]

<span class="hljs-comment">// 生成一个包含名字和id的数组</span>
<span class="hljs-keyword">const</span> newArr = Users.map(<span class="hljs-function"><span class="hljs-params">user</span> =></span> &#123;
    <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-comment">// 这里可以添加任意你想返回的数据 或者 插入你想插入的自定义数据</span>
        <span class="hljs-attr">id</span>: user.id,
        <span class="hljs-attr">name</span>: user.name
    &#125;
&#125;)
newArr<span class="hljs-comment">// [&#123;id:  1,name: 'aYin'&#125;, &#123;id: 2,name: 'zz'&#125;]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">筛选符合条件指定目标</h3>
<h4 data-id="heading-10">寻找第一个符合的子项</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 当然find 方法只会帮你找到第一个</span>
<span class="hljs-keyword">const</span> aYin = Users.find(<span class="hljs-function"><span class="hljs-params">user</span> =></span> user.id  === <span class="hljs-number">1</span>)<span class="hljs-comment">// [&#123;id:  1,name: 'aYin', age: 26, sex: 'male'&#125;]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">寻找所有符合的子项</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// filter</span>
<span class="hljs-keyword">const</span> aYin = Users.filter(<span class="hljs-function"><span class="hljs-params">user</span> =></span> user.name === <span class="hljs-string">'aYin'</span>) 
<span class="hljs-comment">// [&#123;id:  1,name: 'aYin', age: 26, sex: 'male'&#125;, &#123;id:  3,name: 'aYin', age: 26, sex: 'male'&#125;]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">批量改变原数组每一项内容</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// forEach</span>
<span class="hljs-keyword">const</span> customData = [<span class="hljs-string">'帅'</span>, <span class="hljs-string">'漂亮'</span>, <span class="hljs-string">'真帅'</span>]
Users.forEach(<span class="hljs-function">(<span class="hljs-params">user, index</span>) =></span> &#123;
    user.character = customData[index]
&#125;)
Users <span class="hljs-comment">//  [&#123;id:  1,name: 'aYin', age: 26, sex: 'male', character: "帅"&#125;, &#123;id: 2,name: 'zz', age: 23, sex: 'female', character: "漂亮"&#125;, &#123;id:  3,name: 'aYin', age: 26, sex: 'male', character: "真帅"&#125;]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">判断是否是数组</h2>
<ul>
<li>
<p>Array.isArray()</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Array</span>.isArray(Users)<span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>instanceof</p>
<pre><code class="hljs language-js copyable" lang="js">Users <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span><span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>Object.prototype.toString</p>
<pre><code class="hljs language-js copyable" lang="js">toString.call(Users)  === <span class="hljs-string">"[object Array]"</span><span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>constructor</p>
<blockquote>
<p>constructor 可以被重新赋值，不建议使用</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">Users.constructor === <span class="hljs-built_in">Array</span><span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul></div>  
</div>
            