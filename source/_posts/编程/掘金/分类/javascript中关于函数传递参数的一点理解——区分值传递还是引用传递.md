
---
title: 'javascript中关于函数传递参数的一点理解——区分值传递还是引用传递'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d277bc6a8ca547a88b3fb829eac37c17~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 21 May 2021 02:25:14 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d277bc6a8ca547a88b3fb829eac37c17~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">首先，ECMAscript中所有的函数是按照值传递的</h3>
<p>这意味着函数外的值会被复制到函数内部的参数中，就类似于一个变量。如果是原始值，那么就跟原始值变量复制一样，如果是引用值，那么就跟引用值变量的复制是一样。(红包书上的原话)</p>
<h3 data-id="heading-1">一个题目</h3>
<p>如果对这个问题的答案不是很清楚，需要去测试的话，这边文章很值得看下去。我的理解如果有问题，希望大家能够指出来。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params">a</span>) </span>&#123;
  a = a + <span class="hljs-number">10</span>
  <span class="hljs-built_in">console</span>.log(a)
&#125;
<span class="hljs-keyword">var</span> a = <span class="hljs-number">10</span>

test(a)
<span class="hljs-built_in">console</span>.log(a); 
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">对是值传递还是引用传递的分析</h3>
<p>在按值传递时，只会被复制到一个局部变量，就是函数外面的变量，在作为函数实参传递时会在函数内部对实参和形参存在一个赋值操作。在按照引用传递时值在内存中的位置会被保存在一个局部变量，这个局部变量被用在函数内部，也就是内外的实参形参是一个值，所以函数内部的修改会影响到函数的外部。js中函数是按照值传递的。有了这个结论，这时候，上面的问题，就迎刃而解了。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params">a</span>) </span>&#123;
  a = a + <span class="hljs-number">10</span>
  <span class="hljs-built_in">console</span>.log(a) <span class="hljs-comment">// 20</span>
&#125;
<span class="hljs-keyword">var</span> a = <span class="hljs-number">10</span>

test(a)
<span class="hljs-built_in">console</span>.log(a);  <span class="hljs-comment">// 10</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>首先，形参相当于是在函数内部声明的局部变量 var a</li>
<li>值传递，相当于把实参a = 10 给了形参a一份副本,把局部变量a赋值为了10</li>
<li>所以修改是在a这个局部变量上的修改，局部变量值加一变成了20， 打印出20</li>
<li>而对区局变量a没有任何影响</li>
</ul>
<p>对于上面的解释没有什么问题，但是当传递的一个引用类型的值时，就似乎没有那么清楚了</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setName</span>(<span class="hljs-params">obj</span>) </span>&#123;
  obj.name = <span class="hljs-string">'lisi'</span>
&#125;

<span class="hljs-keyword">let</span> person = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'zhangsan'</span>
&#125;

setName(person)
<span class="hljs-built_in">console</span>.log(person.name); <span class="hljs-comment">// lisi</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这次我们把一个对象作为函数的参数进行传递，我们来分析</p>
<ul>
<li>首先我们创建了一个person对象，里面有name属性</li>
<li>把对象传递到函数中，执行了类似于var obj = person的赋值操作。</li>
<li>结果，有点意外的，对于obj的修改，也反映到了person上面</li>
<li>对应的关系如图</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d277bc6a8ca547a88b3fb829eac37c17~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
这个结果是因为js的赋值操作的结果是使得obj和person同时指向了堆内存上的对象，所以函数内部修改了obj会反映到函数外部的person对象上，因为修改的是堆内存上的对象。但是函数内部修改对象的影响到了全局，并不代表着参数是按照引用来传递的。下面我们来证明这个结论</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">setName</span>(<span class="hljs-params">obj</span>) </span>&#123;
  obj.name = <span class="hljs-string">'lisi'</span>
  obj = &#123;&#125;
  obj.name = <span class="hljs-string">'wangwu'</span>
&#125;

<span class="hljs-keyword">let</span> person = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'zhangsan'</span>
&#125;

setName(person)
<span class="hljs-built_in">console</span>.log(person.name); <span class="hljs-comment">// lisi</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述的例子中在函数内部修改了形参为一个空对象，结果仍然是lisi，我们来一步步分析，这个例子是怎么能够说明是值传递的呢，如图</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/646958327d8044d299f5587f2e053ede~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>首先在函数内部，把形参obj修改为了一个空对象，就相当于这样相当于修改了obj指向的堆内存对象，指向了一个空对象，跟person不再指向同一个对象</li>
<li>然后修改其name属性为wangwu，但是这个时候修改name只是修改局部obj指向的新的堆内存，对person没有任何的改变。</li>
<li>因为是值传递，所以只是进行了obj的简单赋值为person，因为js的引用赋值是修改指向的内存，所以obj的变化显示在了person上。而如果是引用赋值的话，就是obj两个是绑定在一块的，obj指向了新的空对象，person必定也只想新的空对象，显然没有，person仍然指向原来的对象。由此可见，是值传递的。</li>
</ul>
<p>总结，</p>
<ul>
<li>js函数传参是值传递的，无论是引用类型还是基本类型</li>
</ul>
<p>参考文献：《javascript高级程序设计》</p></div>  
</div>
            