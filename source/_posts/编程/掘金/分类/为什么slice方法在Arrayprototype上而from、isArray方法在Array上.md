
---
title: '为什么slice方法在Array.prototype上而from、isArray方法在Array上'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c1db8a0de524bbb8eec6ce725116a66~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 20 Jul 2021 20:33:38 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c1db8a0de524bbb8eec6ce725116a66~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>和这个问题相似的一个问题是：为什么<code>isArray</code>在<code>Array</code>上而不在<code>Array.prototype</code>上。即通常调用<code>isArray</code>方法是使用<code>Array.isArray()</code>，而不是<code>Array.prototype.isArray()</code>。</p>
<p>方法放在原型对象上（即<code>Array.prototype</code>上）大家可以理解，以前在实现继承的时候，就使用过：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">this</span>.name = <span class="hljs-string">'fan'</span>;
&#125;
<span class="hljs-comment">// 方法放在原型对象上，达到共享方法、节省存储空间的效果</span>
Person.prototype.sayHello = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'hello'</span>);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-0">先说明为什么方法可以放在构造函数上</h3>
<p>把方法放在构造函数上很少使用，这就是问题的关键，实际上构造函数也是一个对象，它是<code>Function</code>构造函数的一个实例，<strong>既然是对象，那就可以有自己的属性和方法</strong>，当然就可以把方法放在构造函数上了，比如<code>sayHello</code>这个方法，可以把它放在<code>Person</code>构造函数（也是<code>Person</code>对象）上，当作Person的一个成员。每个JavaScript函数实际上都是一个<code>Function</code>实例。</p>
<p><code>Function</code>构造函数自己也是一个对象，但它没有自己的属性和方法，它也有自己的原型对象，用来放一些属性和方法，比如常用的<code>call</code>、<code>bind</code>、<code>apply</code>方法实际上就是放在<code>Function.prototype</code>上的，所以，只要是函数，就能通过原型链访问到这些方法，因为JS函数是<code>Function</code>实例对象，会指向<code>Function.prototype</code>。
通过以下代码就可以看到一个JS函数是Function实例，并且上面有自己定义的方法：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c1db8a0de524bbb8eec6ce725116a66~tplv-k3u1fbpfcp-watermark.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">接下来说明把方法放在原型对象上和放在构造函数上有什么区别</h3>
<p>由于原型链的关系，凡是放在原型对象上的方法，都可以通过实例直接调用该方法。通俗地讲，就是一个实例只能访问到原型链上（各级原型对象上）的属性和方法，比如一个数组：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>, <span class="hljs-number">5</span>];
<span class="hljs-comment">// 可以直接用arr调用slice方法</span>
<span class="hljs-keyword">let</span> arrCopy1 = arr.slice();
<span class="hljs-comment">// 也可以用Array.prototype.slice.call调用</span>
<span class="hljs-keyword">let</span> arrCopy2 = <span class="hljs-built_in">Array</span>.prototype.slice.call(arr);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是，只要这个方法放在构造函数上，比如<code>from</code>方法，它就不能被实例直接调用，实例访问不到它，如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>];
<span class="hljs-comment">// 错误的调用</span>
<span class="hljs-keyword">let</span> arrCopy = arr.from();    <span class="hljs-comment">// TypeError: arr.from is not a function</span>
<span class="hljs-comment">// 正确的调用</span>
<span class="hljs-keyword">let</span> arrCopy = <span class="hljs-built_in">Array</span>.from(arr);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">最后是为什么要把方法放在不同的地方</h3>
<p>比如<code>Array.isArray</code>，它是判断一个变量是否是一个数组，如果把它放在Array.prototype上，根据前面讲的特性，那么只有当一个变量已经是数组的情况下，才能调用<code>isArray</code>，也就是说，一个变量<code>arr</code>，如果是数组，调用<code>arr.isArray()</code>就是<code>true</code>，如果不是数组，那它根本就没办法调用<code>isArray</code>。况且，变量可能是各种各样的值，比如基本类型的<code>number</code>、<code>string</code>、<code>undefined</code>、<code>null</code>。<code>null</code>是没有办法调用任何函数的。所以，<code>isArray</code>方法必须放在Array构造函数上，每次调用它都用<code>Array.isArray()</code>。</p>
<p>不过，如果使用<code>call</code>强行用实例直接调用原型对象上的方法，也可以实现，但不提倡：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params"></span>) </span>&#123;&#125;
Person.prototype.myIsArray = <span class="hljs-built_in">Array</span>.isArray;

<span class="hljs-keyword">let</span> person = <span class="hljs-keyword">new</span> Person();
<span class="hljs-comment">// 第一个参数是null，因为call是把函数内的this绑定为第一个参数，Array.isArray方法是判断参数是否为数组</span>
<span class="hljs-built_in">console</span>.log(person.myIsArray.call(<span class="hljs-literal">null</span>, [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>]));
<span class="hljs-comment">// 经过测试，可以得到正确的结果，判断一个东西是否是数组</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过<code>Array.isArray()</code>，可以知道其他内置对象的方法放在原型对象上还是在构造函数上，原因都大同小异。</p>
<p>我个人认为<code>from</code>方法之所以放在Array构造函数上是因为不是所有数据类型都能转成数组的，所以在其函数体中，一定有对类型的判断，比如<code>Array.from(null)</code>就会报<code>TypeError: Cannot convert undefined or null to object</code>，显然，放在原型对象上就不合适了（null没法调用任何方法，而<code>from</code>方法必须对不合适的数据类型进行处理）。</p>
<p>对于<code>slice</code>，它可以切割数组，也可以切割字符串，还可以把类数组对象转成数组。对于其他数据类型的变量，是不允许切的，所以根本就不允许其他数据类型的变量调用<code>slice</code>。</p></div>  
</div>
            