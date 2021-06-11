
---
title: 'js数组对象深拷贝'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b01b74c2008240549c7dcc4a482456ef~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 00:50:10 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b01b74c2008240549c7dcc4a482456ef~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第11天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p>大家好，我是前端队长Daotin，想要获取更多前端精彩内容，关注我，解锁前端成长新姿势。</p>
<p>以下正文：</p>
<h2 data-id="heading-0">背景</h2>
<p>踩过的坑如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b01b74c2008240549c7dcc4a482456ef~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>formData本来是父组件传过来的，但是我不想直接用，于是我直接赋值给一个formDataCopy的对象。</p>
<p>但是诡异的事情发生了，就是在我填写自己的表单组件的时候，一旦表单的数据发生的变化时，本来是formDataCopy的值发生变化，但是‘formDataDefault值’ 这个字符串却被打印出来，也就是说formData改变了。</p>
<p>奇怪，formData是父组件传过来的值怎么会改变呢？</p>
<p>经过一番挣扎，才发现formDataCopy使用的是简单的赋值，导致formDataCopy和formData指向相同的对象。</p>
<p>formDataCopy一改变，formData就会跟着变。</p>
<p>以上是背景，所以我就对浅拷贝和深拷贝进行了总结：</p>
<h2 data-id="heading-1">浅拷贝</h2>
<p>什么是浅拷贝：两者是指向一个对象。</p>
<h3 data-id="heading-2">对象的浅拷贝</h3>
<p>1、对象的直接遍历赋值。</p>
<p>2、ES6中的 <code>var copyObj = Object.assign(&#123;&#125;, obj);</code></p>
<p>3、ES7扩展运算符 <code>var copyObj = &#123; ...obj &#125;</code></p>
<p>4、Jquery浅拷贝 <code>var copiedObject = jQuery.extend(&#123;&#125;, originalObject)</code>   如果改变了originalObject，copiedObject 也会变。</p>
<h3 data-id="heading-3">数组的浅拷贝</h3>
<p>（两者指向不同的对象，但是只能拷贝一层）</p>
<ul>
<li>array.concat();</li>
<li>array.slice(0);</li>
</ul>
<p>如果该元素是个对象引用 （不是实际的对象），slice 会拷贝这个对象引用到新的数组里。两个对象引用都引用了同一个对象。如果被引用的对象发生改变，则新的和原来的数组中的这个元素也会发生改变，所以是浅拷贝。</p>
<p>对于字符串、数字及布尔值来说（不是 String、Number 或者 Boolean 对象），slice 会拷贝这些值到新的数组里。在别的数组里修改这些字符串或数字或是布尔值，将不会影响另一个数组。</p>
<blockquote>
<p>也就是说，如果原数组改变的是基本数据类型，比如String，Boolean，Number的数据，不会影响到新数组；
但是如果改变的是对象或者数组中的数据，是会影响到新数组的，也也就是对于对象或者数组，新旧数组指向的是一个对象。</p>
</blockquote>
<h2 data-id="heading-4">深拷贝</h2>
<p>（下面说的深拷贝是基本对象的深拷贝，不考虑对象的复杂属性，比如set，get，Function等）</p>
<p>1、最简单的方式 <code>JSON.parse(JSON.stringify(Obj))</code> 这种方法使用较为简单，可以满足基本的深拷贝需求，而且能够处理JSON格式能表示的所有数据类型，但是对于正则表达式类型、函数类型等无法进行深拷贝(而且会直接丢失相应的值)。</p>
<p>2、jQuery深拷贝 <code>var copiedObject = $.extend(true, &#123;&#125;, originalObject)</code></p>
<p>3、手动写递归方式</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> array = [
   &#123; <span class="hljs-attr">number</span>: <span class="hljs-number">1</span> &#125;,
   &#123; <span class="hljs-attr">number</span>: <span class="hljs-number">2</span> &#125;,
   &#123; <span class="hljs-attr">number</span>: <span class="hljs-number">3</span> &#125;
];
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">copy</span> (<span class="hljs-params">obj</span>) </span>&#123;
        <span class="hljs-keyword">var</span> newobj = obj.constructor === <span class="hljs-built_in">Array</span> ? [] : &#123;&#125;;
        <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span> obj !== <span class="hljs-string">'object'</span>)&#123;
            <span class="hljs-keyword">return</span>;
        &#125;
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i <span class="hljs-keyword">in</span> obj)&#123;
           newobj[i] = <span class="hljs-keyword">typeof</span> obj[i] === <span class="hljs-string">'object'</span> ? copy(obj[i]) : obj[i];
        &#125;
        <span class="hljs-keyword">return</span> newobj
&#125;
<span class="hljs-keyword">var</span> copyArray = copy(array)
copyArray[<span class="hljs-number">0</span>].number = <span class="hljs-number">100</span>;
<span class="hljs-built_in">console</span>.log(array); <span class="hljs-comment">//  [&#123;number: 1&#125;, &#123; number: 2 &#125;, &#123; number: 3 &#125;]</span>
<span class="hljs-built_in">console</span>.log(copyArray); <span class="hljs-comment">// [&#123;number: 100&#125;, &#123; number: 2 &#125;, &#123; number: 3 &#125;]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">参考文档</h2>
<p><a href="https://www.cnblogs.com/penghuwan/p/7359026.html" target="_blank" rel="nofollow noopener noreferrer">www.cnblogs.com/penghuwan/p…</a></p>
<p><a href="https://github.com/wengjq/Blog/issues/3" target="_blank" rel="nofollow noopener noreferrer">github.com/wengjq/Blog…</a></p>
<hr>
<blockquote>
<p><strong>最近热门文章</strong>：</p>
<ul>
<li><a href="https://juejin.cn/post/6963071339108237319" target="_blank">图片瀑布流，就是如此简单（so easy）</a></li>
<li><a href="https://juejin.cn/post/6961968236837470216" target="_blank">梳理ajax跨域常用4种解决方案（简单易懂）</a></li>
<li><a href="https://juejin.cn/post/6961226664869101605" target="_blank">Vue.js命名风格指南（易记版）</a></li>
</ul>
</blockquote>
<p><em><strong>以上，如果你看了觉得对你有所帮助，就点个赞叭，这样Daotin也有更新下去的动力，跪谢各位父老乡亲啦~~~ 听说喜欢点赞的人，一个月内都会有好运降临哦 ~~</strong></em></p></div>  
</div>
            