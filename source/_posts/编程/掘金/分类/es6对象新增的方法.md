
---
title: 'es6对象新增的方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2855'
author: 掘金
comments: false
date: Thu, 26 Aug 2021 01:58:21 GMT
thumbnail: 'https://picsum.photos/400/300?random=2855'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第26天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>es6与之前相比，对于Object来说增加了一些新的属性。这篇文章针对几个属性来进行说明</p>
<hr>
<h3 data-id="heading-0">Object.assign()</h3>
<h4 data-id="heading-1">基本用法 </h4>
<p><code>Object.assign()</code>方法用于对象的合并，将源对象（source）的所有可枚举属性，复制到目标对象（target）。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> target = &#123; <span class="hljs-attr">a</span>: <span class="hljs-number">1</span> &#125;;

<span class="hljs-keyword">const</span> source1 = &#123; <span class="hljs-attr">b</span>: <span class="hljs-number">2</span> &#125;;
<span class="hljs-keyword">const</span> source2 = &#123; <span class="hljs-attr">c</span>: <span class="hljs-number">3</span> &#125;;

<span class="hljs-built_in">Object</span>.assign(target, source1, source2);
target <span class="hljs-comment">// &#123;a:1, b:2, c:3&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><code>Object.assign()</code>方法的第一个参数是目标对象，后面的参数都是源对象。</p>
<p>注意，如果目标对象与源对象有同名属性，或多个源对象有同名属性，则后面的属性会覆盖前面的属性。</p>
<p>如果只有一个参数，<code>Object.assign()</code>会直接返回该参数。</p>
<p>如果该参数不是对象，则会先转成对象，然后返回。</p>
<p>由于<code>undefined</code>和<code>null</code>无法转成对象，所以如果它们作为参数，就会报错。</p>
<p>如果非对象参数出现在源对象的位置（即非首参数），那么处理规则有所不同。首先，这些参数都会转成对象，如果无法转成对象，就会跳过。这意味着，如果<code>undefined</code>和<code>null</code>不在首参数，就不会报错。</p>
</blockquote>
<hr>
<h3 data-id="heading-2">Object.is()</h3>
<p>ES5 比较两个值是否相等，只有两个运算符：相等运算符（<code>==</code>）和严格相等运算符（<code>===</code>）。它们都有缺点，前者会自动转换数据类型，后者的<code>NaN</code>不等于自身，以及<code>+0</code>等于<code>-0</code>。JavaScript 缺乏一种运算，在所有环境中，只要两个值是一样的，它们就应该相等。</p>
<p>ES6 提出“Same-value equality”（同值相等）算法，用来解决这个问题。<code>Object.is</code>就是部署这个算法的新方法。它用来比较两个值是否严格相等，与严格比较运算符（===）的行为基本一致。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">Object</span>.is(<span class="hljs-string">'foo'</span>, <span class="hljs-string">'foo'</span>)
<span class="hljs-comment">// true</span>
<span class="hljs-built_in">Object</span>.is(&#123;&#125;, &#123;&#125;)
<span class="hljs-comment">// false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-3">Object.getOwnPropertyDescriptors()</h3>
<p>ES5 的<code>Object.getOwnPropertyDescriptor()</code>方法会返回某个对象属性的描述对象（descriptor）。ES2017 引入了<code>Object.getOwnPropertyDescriptors()</code>方法，返回指定对象所有自身属性（非继承属性）的描述对象。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> obj = &#123;
  <span class="hljs-attr">foo</span>: <span class="hljs-number">123</span>,
  <span class="hljs-keyword">get</span> <span class="hljs-title">bar</span>() &#123; <span class="hljs-keyword">return</span> <span class="hljs-string">'abc'</span> &#125;
&#125;;

<span class="hljs-built_in">Object</span>.getOwnPropertyDescriptors(obj)
<span class="hljs-comment">// &#123; foo:</span>
<span class="hljs-comment">//    &#123; value: 123,</span>
<span class="hljs-comment">//      writable: true,</span>
<span class="hljs-comment">//      enumerable: true,</span>
<span class="hljs-comment">//      configurable: true &#125;,</span>
<span class="hljs-comment">//   bar:</span>
<span class="hljs-comment">//    &#123; get: [Function: get bar],</span>
<span class="hljs-comment">//      set: undefined,</span>
<span class="hljs-comment">//      enumerable: true,</span>
<span class="hljs-comment">//      configurable: true &#125; &#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，<code>Object.getOwnPropertyDescriptors()</code>方法返回一个对象，所有原对象的属性名都是该对象的属性名，对应的属性值就是该属性的描述对象。</p>
<hr>
<h3 data-id="heading-4">__proto__属性</h3>
<p>JavaScript 语言的对象继承是通过原型链实现的。ES6 提供了更多原型对象的操作方法。</p>
<h4 data-id="heading-5">__proto__属性</h4>
<p><code>__proto__</code>属性（前后各两个下划线），用来读取或设置当前对象的原型对象（prototype）。目前，所有浏览器（包括 IE11）都部署了这个属性。</p>
<pre><code class="copyable">// es5 的写法
const obj = &#123;
  method: function() &#123; ... &#125;
&#125;;
obj.__proto__ = someOtherObj;

// es6 的写法
var obj = Object.create(someOtherObj);
obj.method = function() &#123; ... &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该属性没有写入 ES6 的正文，而是写入了附录，原因是<code>__proto__</code>前后的双下划线，说明它本质上是一个内部属性，而不是一个正式的对外的 API，只是由于浏览器广泛支持，才被加入了 ES6。标准明确规定，只有浏览器必须部署这个属性，其他运行环境不一定需要部署，而且新的代码最好认为这个属性是不存在的。因此，无论从语义的角度，还是从兼容性的角度，都不要使用这个属性，而是使用下面的<code>Object.setPrototypeOf()</code>（写操作）、<code>Object.getPrototypeOf()</code>（读操作）、<code>Object.create()</code>（生成操作）代替。</p>
<hr>
<h3 data-id="heading-6">Object.values()</h3>
<p><code>Object.values</code>方法返回一个数组，成员是参数对象自身的（不含继承的）所有可遍历（enumerable）属性的键值。</p>
<pre><code class="copyable">const obj = &#123; foo: 'bar', baz: 42 &#125;;
Object.values(obj)
// ["bar", 42]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>返回数组的成员顺序，与本章的《属性的遍历》部分介绍的排列规则一致。</p>
<pre><code class="copyable">const obj = &#123; 100: 'a', 2: 'b', 7: 'c' &#125;;
Object.values(obj)
// ["b", "c", "a"]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，属性名为数值的属性，是按照数值大小，从小到大遍历的，因此返回的顺序是<code>b</code>、<code>c</code>、<code>a</code>。
<code>Object.values</code>只返回对象自身的可遍历属性。</p></div>  
</div>
            