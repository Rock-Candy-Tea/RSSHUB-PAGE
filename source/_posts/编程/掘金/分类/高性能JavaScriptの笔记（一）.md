
---
title: '高性能JavaScriptの笔记（一）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8a774378364406aa1a4f817e90892ad~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 19 May 2021 00:36:49 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8a774378364406aa1a4f817e90892ad~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">学习来源</h3>
<p><a href="https://gitee.com/wzckongchengji/high_performance_javascript" target="_blank" rel="nofollow noopener noreferrer">《高性能JavaScript-中文版》（仅供学习使用）</a></p>
<h1 data-id="heading-1">数据存取</h1>
<h2 data-id="heading-2">数据位置</h2>
<p>计算机科学中有一个经典问题是通过<strong>改变数据的存储位置来获得最佳的读写性能</strong>，数据存储的位置关系到代码执行过程中数据的检索速度。在JavaScript 中，这个问题相对简单，因为只有几种存储方案可供选择。不过，和其他编程语言一样，<em>数据的存储位置会很大程度上影响其读取速度</em>。JavaScript中有下面四种基本的数据存取位置。</p>
<ol>
<li>字面量
字面量只代表自身，不存储在特定位置。JavaScript中的字面量有:字符串、数字、布尔值、对象、数组、函数、正则表达式，以及特殊的null和undefined值。</li>
<li>本地变量
开发人员使用关键字var定义的数据存储单元。</li>
<li>数组元素
存储在JavaScript数组对象内部,以数字作为索引。</li>
<li>对象成员
存储在JavaScript对象内部，以字符串作为索引。</li>
</ol>
<p>在不同浏览器中，访问不同存储位置的数据需要消耗的时间也是不同的。由下图<code>每200000次读取变量存储位置所消耗的时间</code>可以知道，<strong>读取字面量和本地变量消耗的时间最少，性能最高</strong>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8a774378364406aa1a4f817e90892ad~tplv-k3u1fbpfcp-zoom-1.image" alt="每200000次读取变量存储位置所消耗的时间" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">标识符解析</h2>
<p>标识符解析是有代价的，事实上没有哪种计算机操作可以不产生性能开销。在执行环境的作用域链中，一个标识符所在的位置越深，它的读写速度也就越慢。因此，函数中<strong>读写局部变量总是最快的，而读写全局变量通常是最慢的</strong>（优化JavaScript 引擎在某些情况下能有所改善)。</p>
<p>全局变量总是存在于执行环境作用域链的最末端，因此它也是最远的。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4740261c5ad645e18550b463f2150540~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<br>
<p>JavaScript 中对象是基于原型的，原型是其他对象的基础</p>
<ul>
<li>访问字面量和局部变量的速度最快,相反,访问数组元素和对象成员相对较慢。由于局部变量存在于作用域链的起始位置,因此访问局部变量比访问跨作用域变量更快。变量在作用域链中的位置越深，访问所需时间就越长。由于全局变量总处在作用域链的最末端，因此访问速度也是最慢的。</li>
<li>避免使用with语句,因为它会改变执行环境作用域链。同样，try-catch语句中的catch子句也有同样的影响,因此也要小心使用。</li>
<li>嵌套的对象成员会明显影响性能，尽量少用。</li>
<li>属性或方法在原型链中的位置越深,访问它的速度也越慢。</li>
<li>通常来说，你可以通过把常用的对象成员、数组元素、跨域变量保存在局部变量中来改善JavaScript性能,因为局部变量访问速度更快。</li>
</ul>
<h2 data-id="heading-4">集合对象</h2>
<p>访问集合的效率比访问数组更低
可以考虑将集合变为数组</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">toArray</span>(<span class="hljs-params"></span>) </span>&#123;
<span class="hljs-keyword">var</span> len = coll.length, a = [];
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < len; i++) &#123;
a[i] = coll[i]
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">原型</h1>
<ul>
<li>
<p>JavaScript对象是基于原型的</p>
</li>
<li>
<p>原型是其他对象的基础</p>
</li>
</ul>
<p><strong>对象可以有两种成员类型：</strong></p>
<pre><code class="copyable">1. 实例成员（也称为own成员） 
2.原型成员
<span class="copy-code-btn">复制代码</span></code></pre>
<p>例子：</p>
<pre><code class="copyable">var book = &#123;
   title: 'hello',
   na: 'world'
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>book 是一个对象，在book当中存在<strong>book.title</strong>和<strong>book.toString()</strong></p>
<ul>
<li>book.title属于实例对象</li>
<li>book.toString() 属于继承的原型对象</li>
</ul>
<p>对象成员解析时会先从实例对象中找，如果没有找到会从继承的原型对象寻找</p>
<p>hasOwnProperty()方法可以判断对象是否包含特定的实例对象</p>
<pre><code class="copyable">book.hasOwnProperty('title')   // true
book.hasOwnProperty('toString')   //false
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果要确定对象是否包含特定的属性，可以使用in操作符，in操作符既可以搜索实例也可以搜索原型：</p>
<pre><code class="copyable">console.log('title' in book)  // true
console.log('toString' in book)  // true
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h2 data-id="heading-6">原型链</h2>
<p>默认情况下，所有的对象都是Object的实例</p>
<p><code>instanceof</code>: instanceof 运算符用于检测构造函数的 prototype 属性是否出现在某个实例对象的原型链上</p>
<p>例子：</p>
<pre><code class="copyable">function books(title, na)&#123;
    this.title = title;
    this.na = na;
&#125;
books.prototype.say = function() &#123;
    console.info(this.title, this.na)
&#125;
var b1 = new books('111111', '22');
console.log(b1 instanceof books)  // true
console.log(b1.__proto__)
console.log(books.prototype)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>b1的__proto__与books的prototype是相同的</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d96bbc3f46d842d6a6bbf6a574253f08~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">嵌套成员</h2>
<p>由于对象成员可能包含其他成员，每次遇到点操作符，也就是book.title这类，嵌套成员会导致JavaScript引擎搜索所有对象成员</p>
<p><strong>对象成员嵌套得越深，读取速度就越慢</strong></p>
<p>执行<code>location.href </code>总比 <code>window.location.href</code>要快
<code>window.location.href</code>也比<code>window.location.href.toString()</code>要快</p>
<h2 data-id="heading-8">缓存对象成员值</h2>
<p>由于所有类似的性能问题都与对象成员有关，因此应该尽可能避免使用它们。</p>
<p><strong>在同一个函数中没有必要多此读取同一个对象成员</strong></p>
<p><strong>可以将值保存在局部变量当中减少查找次数</strong></p>
<p>例子：</p>
<pre><code class="copyable">function hasEitherClass(element, className1, className2) &#123;
      for(var i = 0; i < 1000; i++) &#123;
           var k = element.className;
      &#125;
      return element.className == className1 || element.className == className2;
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">function hasEitherClass2(element, className1, className2) &#123;
        var currentClassName = element.className;
        for(var i = 0; i < 1000; i++) &#123;
            var k = currentClassName;
        &#125;                                
        return currentClassName == className1 || currentClassName == className2;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用console.time测试后，hasEitherClass2的运行速度比hasEitherClass更快</p>
<br>
<h1 data-id="heading-9">小节</h1>
<p><em><strong>平时写代码时可以优化的点①：</strong></em></p>
<p>document是个全局对象。搜索该变量的过程必须遍历整个作用域链，直到最后在全局变量对象中找到。</p>
<p>可以通过以下方法减少对性能的影响：</p>
<ul>
<li>先将全局变量的引用存储在一个局部变量中</li>
<li>然后使用这个局部变量代替全局变量。这样访问全局变量的次数就减少了，因为局部变量访问更快。</li>
<li>例子：<code>var doc = document;  var bd = doc.body;  var a = doc.getElementById("a");</code></li>
</ul>
<p><em><strong>平时写代码时可以优化的点②：</strong></em></p>
<p>可以使用<code>location.href</code>来代替<code>window.location.href</code></p></div>  
</div>
            