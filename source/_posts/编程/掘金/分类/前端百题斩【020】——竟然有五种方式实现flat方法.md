
---
title: '前端百题斩【020】——竟然有五种方式实现flat方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1858'
author: 掘金
comments: false
date: Sun, 20 Jun 2021 03:26:32 GMT
thumbnail: 'https://picsum.photos/400/300?random=1858'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第6天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<blockquote>
<p>写该系列文章的初衷是“让每位前端工程师掌握高频知识点，为工作助力”。这是前端百题斩的第20斩，希望朋友们关注公众号“执鸢者”，用知识武装自己的头脑。</p>
</blockquote>
<h3 data-id="heading-0">20.1 背景</h3>
<blockquote>
<p>不知道老铁们有没有遇到过一道面试题：如何将一个多维数组展开成一个一维数组？当时我遇到的时候还不了解flat这个神奇的方法，用了最传统的解决方法进行解决。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> flatten = <span class="hljs-function"><span class="hljs-params">arr</span> =></span> arr.toString().split(<span class="hljs-string">','</span>).map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> +item);

<span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, [<span class="hljs-number">3</span>, <span class="hljs-number">4</span>, [<span class="hljs-number">5</span>, <span class="hljs-number">6</span>]]];
<span class="hljs-built_in">console</span>.log(flatten(arr)); <span class="hljs-comment">// [ 1, 2, 3, 4, 5, 6 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>上述方法是不是很神奇，会将多层级的数组展开成为一个层级，但是该方式其实存在很大问题的，下面让我们一起看看这些问题。</p>
</blockquote>
<ol>
<li>不管多少层级都会展开为一个层级；</li>
<li>处理后的结果其实都是字符串，需要后续再转换为原来的类型。</li>
</ol>
<blockquote>
<p>正是基于这个契机，发现了ES6新增了flat函数，这个函数天生就是为数据扁平化处理而生的。</p>
</blockquote>
<h3 data-id="heading-1">20.2 flat基础</h3>
<blockquote>
<p><code>flat()</code> 方法会按照一个可指定的深度递归遍历数组，并将所有元素与遍历到的子数组中的元素合并为一个新数组返回。</p>
</blockquote>
<ol>
<li>flat方法的用法如下所示：</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> newArray = arr.flat([depth])
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>小试牛刀</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, [<span class="hljs-number">3</span>, <span class="hljs-number">4</span>, [<span class="hljs-number">5</span>, <span class="hljs-number">6</span>]]];
<span class="hljs-built_in">console</span>.log(arr.flat(<span class="hljs-number">1</span>)); <span class="hljs-comment">// [ 1, 2, 3, 4, [ 5, 6 ] ]</span>
<span class="hljs-built_in">console</span>.log(arr.flat(<span class="hljs-number">2</span>)); <span class="hljs-comment">// [ 1, 2, 3, 4, 5, 6 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">20.3 实现</h3>
<blockquote>
<p>flat这么香，那么我们是否可以自己实现一个呢？实现该方法的方式有很多，下面就让我们一起看看这五种方式。(注：这五种方式试MDN上给出的替代方案)</p>
</blockquote>
<h4 data-id="heading-3">20.3.1 使用reduce和concat</h4>
<blockquote>
<p>该方式实现起来虽然很简单，但是存在一个很大的缺陷：只能展开一层，对于多层的情况将无能为力。其思想总结起来为以下两个步骤：</p>
</blockquote>
<ol>
<li>利用reduce函数去依次处理每个数组中的元素；</li>
<li>利用concat将当前的数组元素（值或子数组）添加到结果数组中。</li>
</ol>
<pre><code class="copyable">// 使用reduce和concat
Array.prototype.flat1 = function () &#123;
    return this.reduce((acc, val) => acc.concat(val), []);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">20.3.2 使用reduce + concat + isArray + recursivity</h4>
<blockquote>
<p>该方式已经具备展开多层的能力了，其实现思想可总结为以下几点：</p>
</blockquote>
<ol>
<li>利用reduce函数去依次处理每个数组中的元素；</li>
<li>利用concat将当前元素添加到结果数组中；</li>
<li>利用isArray判断当前数组中的元素是不是一个数组；</li>
<li>利用递归思想展开多层级的数组。</li>
</ol>
<pre><code class="copyable">// 使用reduce + concat + isArray +recursivity
Array.prototype.flat2 = function (deep = 1) &#123;
    const flatDeep = (arr, deep = 1) => &#123;
        return deep > 0 ? arr.reduce((acc, val) => acc.concat(Array.isArray(val) ? flatDeep(val, deep - 1) : val), []) : arr.slice();
    &#125;

    return flatDeep(this, deep);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">20.3.3 使用forEach + concat + isArray +recursivity</h4>
<blockquote>
<p>该方式与上述方式很类似，能够设定层级展开，只是遍历数组由reduce转换为forEach。</p>
</blockquote>
<pre><code class="copyable">// 使用forEach + concat + isArray +recursivity
// forEach 遍历数组会自动跳过空元素
Array.prototype.flat3 = function (deep = 1) &#123;
    const result = [];
    (function flat(arr, deep) &#123;
        arr.forEach((item) => &#123;
            if (Array.isArray(item) && deep > 0) &#123;
                flat(item, deep - 1);
            &#125; else &#123;
                result.push(item);
            &#125;
        &#125;)
    &#125;)(this, deep);

    return result;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">20.3.4 使用for of + concat + isArray +recursivity</h4>
<blockquote>
<p>该方式与上述方式很类似，能够设定层级展开，只是遍历数组利用了for of方法</p>
</blockquote>
<pre><code class="copyable">// 使用for of + concat + isArray +recursivity
// for of 遍历数组会自动跳过空元素
Array.prototype.flat4 = function (deep = 1) &#123;
    const result = [];
    (function flat(arr, deep) &#123;
        for(let item of arr) &#123;
            if (Array.isArray(item) && deep > 0) &#123;
                flat(item, deep - 1);
            &#125; else &#123;
                // 去除空元素，因为void 表达式返回的都是undefined，不适用undefined是因为undefined在局部变量会被重写
                item !== void 0 && result.push(item);
            &#125;
        &#125;
    &#125;)(this, deep);

    return result;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">20.3.5 使用堆栈stack</h4>
<blockquote>
<p>该方式主要利用堆栈的思想，将一个多层数组全部展开为一层。其思想可总结为以下几个步骤：</p>
</blockquote>
<ol>
<li>将要处理的数组放到一个栈中处理；</li>
<li>从栈顶取出元素，判断该元素类型，若为数组，则将该数组展开再放回栈顶；若为普通元素则将其放到结果中；</li>
<li>循环遍历，至到栈为空。</li>
</ol>
<pre><code class="copyable">// 使用堆栈stack
Array.prototype.flat5 = function() &#123;
    const stack = [...this];
    const result = [];
    while (stack.length > 0) &#123;
        const next = stack.pop();
        if (Array.isArray(next)) &#123;
            stack.push(...next);
        &#125; else &#123;
            result.push(next);
        &#125;
    &#125;

    // 反转恢复原来顺序
    return result.reverse();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>1.如果觉得这篇文章还不错，来个分享、点赞吧，让更多的人也看到</p>
<p>2.关注公众号执鸢者，与号主一起斩杀前端百题</p></div>  
</div>
            