
---
title: '深入剖析 JavaScript 的深浅拷贝'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0234702e819c4f1c94fce6869e0d88c6~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 18 Jul 2021 18:04:47 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0234702e819c4f1c94fce6869e0d88c6~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0234702e819c4f1c94fce6869e0d88c6~tplv-k3u1fbpfcp-zoom-1.image" alt="file" loading="lazy" referrerpolicy="no-referrer"></p>
<p>本文首发于：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fbigo-frontend%2Fblog%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/bigo-frontend/blog/" ref="nofollow noopener noreferrer">github.com/bigo-fronte…</a> 欢迎关注、转载。</p>
<h2 data-id="heading-0">前言</h2>
<ul>
<li>放之四海皆准的方法是不存在的，不同的深浅拷贝实现方法和实现粒度有各自的优劣以及各自适合的应用场景。</li>
<li>本文会从实现原理进行分析，并将在 JavaScript 中实现深浅拷贝所需要考虑的问题呈现给大家。让大家对深浅拷贝有个更深刻的认识，以便大家可以更好的选择适合自己的拷贝方法。</li>
</ul>
<h2 data-id="heading-1">什么是浅拷贝/深拷贝</h2>
<ul>
<li>浅拷贝：</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed45d6ddfbe34088b0a446ea5d074162~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>创建一个新对象，这个对象有着原始对象属性值的一份精确拷贝。如果属性是基本类型，拷贝的就是基本类型的值，如果属性是引用类型，拷贝的就是内存地址 ，所以如果其中一个对象改变了这个地址，就会影响到另一个对象。</p>
</blockquote>
<ul>
<li>深拷贝：</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c14694650aa42cb80e680f888c64df0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>将一个对象从内存中完整的拷贝一份出来,从堆内存中开辟一个新的区域存放新对象,且修改新对象不会影响原对象</p>
</blockquote>
<h2 data-id="heading-2">如何实现浅拷贝</h2>
<h3 data-id="heading-3">方法一 Object.assign</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Object.assign() 实现 shallowClone</span>
<span class="hljs-keyword">let</span> student = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"小明"</span>,
  <span class="hljs-attr">score</span>: &#123;
    <span class="hljs-attr">english</span>: <span class="hljs-number">88</span>,
    <span class="hljs-attr">chinese</span>: <span class="hljs-number">77</span>,
    <span class="hljs-attr">math</span>: <span class="hljs-number">99</span>,
  &#125;,
&#125;;

<span class="hljs-keyword">let</span> shallowStudent = <span class="hljs-built_in">Object</span>.assign(&#123;&#125;, student);
shallowStudent.name = <span class="hljs-string">"李雷"</span>;
shallowStudent.score.english = <span class="hljs-number">98</span>; <span class="hljs-comment">// score 是 object, 共用内存地址, 都会被改成98</span>

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"shallowStudent: "</span>, shallowStudent);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"student: "</span>, student);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>缺陷：没能处理数组，不够通用</li>
</ul>
<h3 data-id="heading-4">浅拷贝更为通用的做法：遍历赋值</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> simpleClone = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">target</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> target === <span class="hljs-string">"object"</span>) &#123;
    <span class="hljs-keyword">let</span> cloneTarget = <span class="hljs-built_in">Array</span>.isArray(target) ? [] : &#123;&#125;;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> target) &#123;
      cloneTarget[key] = target[key];
    &#125;
    <span class="hljs-keyword">return</span> cloneTarget;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">return</span> target;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">如何实现 深拷贝</h2>
<h3 data-id="heading-6">方法一 JSON.parse(JSON.stringify())</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> student = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"小明"</span>,
  <span class="hljs-attr">score</span>: &#123;
    <span class="hljs-attr">english</span>: <span class="hljs-number">88</span>,
    <span class="hljs-attr">chinese</span>: <span class="hljs-number">77</span>,
    <span class="hljs-attr">math</span>: <span class="hljs-number">99</span>,
  &#125;,
&#125;;

<span class="hljs-keyword">let</span> deepStudent = <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">JSON</span>.stringify(student));
deepStudent.name = <span class="hljs-string">"李雷"</span>;
deepStudent.score.english = <span class="hljs-number">98</span>;

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"deepStudent: "</span>, deepStudent);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"student: "</span>, student);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>存在问题：JSON.stringify 对于拷贝其他引用类型、拷贝函数、循环引用等情况无法很好处理，只能运用于简单 JSON。</p>
</blockquote>
<h3 data-id="heading-7">深拷贝更为通用的做法：递归遍历赋值</h3>
<ul>
<li>
<p>如果是深拷贝的话，考虑到我们要拷贝的对象是不知道有多少层深度的，我们可以用递归来解决问题：</p>
<ul>
<li>如果是原始类型，无需继续拷贝，直接返回</li>
<li>如果是引用类型，创建一个新的对象，遍历需要克隆的对象，将需要克隆对象的属性执行深拷贝后依次添加到新对象上。</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> deepClone = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">target</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> target === <span class="hljs-string">"object"</span>) &#123;
    <span class="hljs-keyword">let</span> cloneTarget = <span class="hljs-built_in">Array</span>.isArray(target) ? [] : &#123;&#125;;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> target) &#123;
      cloneTarget[key] = deepClone(target[key]);
    &#125;
    <span class="hljs-keyword">return</span> cloneTarget;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">return</span> target;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">考虑循环引用</h3>
<ul>
<li>考虑以下 case:</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> target = &#123;
  <span class="hljs-attr">field1</span>: <span class="hljs-number">1</span>,
  <span class="hljs-attr">field2</span>: <span class="hljs-literal">undefined</span>,
  <span class="hljs-attr">field3</span>: &#123;
    <span class="hljs-attr">child</span>: <span class="hljs-string">"child"</span>,
  &#125;,
  <span class="hljs-attr">field4</span>: [<span class="hljs-number">2</span>, <span class="hljs-number">4</span>, <span class="hljs-number">8</span>],
&#125;;
target.target = target;
<span class="hljs-comment">// 这个case如果还用以上递归代码的话，会导致死循环、栈内存溢出。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>解决循环引用问题，我们可以额外用一个存储空间，来存储当前对象和拷贝对象的对应关系，当需要拷贝当前对象时，先去存储空间中找，有没有拷贝过这个对象，如果有的话直接返回，如果没有的话继续拷贝，这样就可以解决的循环引用的问题。</li>
<li>这个存储空间，需要可以存储 key-value 形式的数据，且 key 可以是一个引用类型，我们可以选择 Map 这种数据结构：检查 map 中有无克隆过的对象,如果有则直接返回，如果没有则将当前对象作为 key，克隆对象作为 value 进行存储，继续克隆</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> deepClone = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">target, map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>()</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> target === <span class="hljs-string">"object"</span>) &#123;
    <span class="hljs-keyword">let</span> cloneTarget = <span class="hljs-built_in">Array</span>.isArray(target) ? [] : &#123;&#125;;
    <span class="hljs-keyword">if</span> (map.get(target)) &#123;
      <span class="hljs-keyword">return</span> map.get(target);
    &#125;
    map.set(target, cloneTarget);
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> key <span class="hljs-keyword">in</span> target) &#123;
      cloneTarget[key] = deepClone(target[key], map);
    &#125;
    <span class="hljs-keyword">return</span> cloneTarget;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">return</span> target;
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">WeakMap 优化</h3>
<ul>
<li>可以使用 WeakMap 进一步优化。WeakMap 对象是一组键/值对的集合，其中的键是弱引用的。其键必须是对象，而值可以是任意的。</li>
<li>我们默认创建一个对象：const obj = &#123;&#125;，就默认创建了一个强引用的对象，我们只有手动将 obj = null，它才会被垃圾回收机制进行回收，如果是弱引用对象，垃圾回收机制会自动帮我们回收。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> obj = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"ConardLi"</span> &#125;;
<span class="hljs-keyword">const</span> target = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
target.set(obj, <span class="hljs-string">"code秘密花园"</span>);
obj = <span class="hljs-literal">null</span>;
<span class="hljs-built_in">console</span>.log(target); <span class="hljs-comment">// Map(1) &#123; &#123; name: 'ConardLi' &#125; => 'code秘密花园' &#125; 即时obj释放了，Map还存留</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> obj = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"ConardLi"</span> &#125;;
<span class="hljs-keyword">const</span> target = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>();
target.set(obj, <span class="hljs-string">"code秘密花园"</span>);
obj = <span class="hljs-literal">null</span>;
<span class="hljs-built_in">console</span>.log(target); <span class="hljs-comment">// WeakMap &#123; <items unknown> &#125; 不再存留obj</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">考虑其他数据类型</h3>
<ul>
<li>上面的代码只考虑了普通的 object 和 array 两种数据类型，实际上所有的引用类型远远不止这两个。下面的代码，在上述深拷贝的基础上，通过类型判断与处理，解决了绝大部分其他类型的拷贝问题。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> mapTag = <span class="hljs-string">"[object Map]"</span>;
<span class="hljs-keyword">const</span> setTag = <span class="hljs-string">"[object Set]"</span>;
<span class="hljs-keyword">const</span> arrayTag = <span class="hljs-string">"[object Array]"</span>;
<span class="hljs-keyword">const</span> objectTag = <span class="hljs-string">"[object Object]"</span>;
<span class="hljs-keyword">const</span> argsTag = <span class="hljs-string">"[object Arguments]"</span>;

<span class="hljs-keyword">const</span> boolTag = <span class="hljs-string">"[object Boolean]"</span>;
<span class="hljs-keyword">const</span> dateTag = <span class="hljs-string">"[object Date]"</span>;
<span class="hljs-keyword">const</span> numberTag = <span class="hljs-string">"[object Number]"</span>;
<span class="hljs-keyword">const</span> stringTag = <span class="hljs-string">"[object String]"</span>;
<span class="hljs-keyword">const</span> symbolTag = <span class="hljs-string">"[object Symbol]"</span>;
<span class="hljs-keyword">const</span> errorTag = <span class="hljs-string">"[object Error]"</span>;
<span class="hljs-keyword">const</span> regexpTag = <span class="hljs-string">"[object RegExp]"</span>;
<span class="hljs-keyword">const</span> funcTag = <span class="hljs-string">"[object Function]"</span>;

<span class="hljs-keyword">const</span> deepTag = [mapTag, setTag, arrayTag, objectTag, argsTag];

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">forEach</span>(<span class="hljs-params">array, iteratee</span>) </span>&#123;
  <span class="hljs-keyword">let</span> index = -<span class="hljs-number">1</span>;
  <span class="hljs-keyword">const</span> length = array.length;
  <span class="hljs-keyword">while</span> (++index < length) &#123;
    iteratee(array[index], index);
  &#125;
  <span class="hljs-keyword">return</span> array;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isObject</span>(<span class="hljs-params">target</span>) </span>&#123;
  <span class="hljs-keyword">const</span> type = <span class="hljs-keyword">typeof</span> target;
  <span class="hljs-keyword">return</span> target !== <span class="hljs-literal">null</span> && (type === <span class="hljs-string">"object"</span> || type === <span class="hljs-string">"function"</span>);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getType</span>(<span class="hljs-params">target</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.prototype.toString.call(target);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getInit</span>(<span class="hljs-params">target</span>) </span>&#123;
  <span class="hljs-keyword">const</span> Ctor = target.constructor;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Ctor();
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">cloneSymbol</span>(<span class="hljs-params">targe</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>(<span class="hljs-built_in">Symbol</span>.prototype.valueOf.call(targe));
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">cloneReg</span>(<span class="hljs-params">targe</span>) </span>&#123;
  <span class="hljs-keyword">const</span> reFlags = <span class="hljs-regexp">/\w*$/</span>;
  <span class="hljs-keyword">const</span> result = <span class="hljs-keyword">new</span> targe.constructor(targe.source, reFlags.exec(targe));
  result.lastIndex = targe.lastIndex;
  <span class="hljs-keyword">return</span> result;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">cloneFunction</span>(<span class="hljs-params">func</span>) </span>&#123;
  <span class="hljs-keyword">const</span> bodyReg = <span class="hljs-regexp">/(?<=&#123;)(.|\n)+(?=&#125;)/m</span>;
  <span class="hljs-keyword">const</span> paramReg = <span class="hljs-regexp">/(?<=\().+(?=\)\s+&#123;)/</span>;
  <span class="hljs-keyword">const</span> funcString = func.toString();
  <span class="hljs-keyword">if</span> (func.prototype) &#123;
    <span class="hljs-keyword">const</span> param = paramReg.exec(funcString);
    <span class="hljs-keyword">const</span> body = bodyReg.exec(funcString);
    <span class="hljs-keyword">if</span> (body) &#123;
      <span class="hljs-keyword">if</span> (param) &#123;
        <span class="hljs-keyword">const</span> paramArr = param[<span class="hljs-number">0</span>].split(<span class="hljs-string">","</span>);
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Function</span>(...paramArr, body[<span class="hljs-number">0</span>]);
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Function</span>(body[<span class="hljs-number">0</span>]);
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">eval</span>(funcString);
  &#125;
&#125;

<span class="hljs-comment">// 处理 不可继续遍历的类型</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">cloneOtherType</span>(<span class="hljs-params">targe, type</span>) </span>&#123;
  <span class="hljs-keyword">const</span> Ctor = targe.constructor;
  <span class="hljs-keyword">switch</span> (type) &#123;
    <span class="hljs-keyword">case</span> boolTag:
    <span class="hljs-keyword">case</span> numberTag:
    <span class="hljs-keyword">case</span> stringTag:
    <span class="hljs-keyword">case</span> errorTag:
    <span class="hljs-keyword">case</span> dateTag:
      <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Ctor(targe);
    <span class="hljs-keyword">case</span> regexpTag:
      <span class="hljs-keyword">return</span> cloneReg(targe);
    <span class="hljs-keyword">case</span> symbolTag:
      <span class="hljs-keyword">return</span> cloneSymbol(targe);
    <span class="hljs-keyword">case</span> funcTag:
      <span class="hljs-keyword">return</span> cloneFunction(targe);
    <span class="hljs-keyword">default</span>:
      <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
  &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">clone</span>(<span class="hljs-params">target, map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>()</span>) </span>&#123;
  <span class="hljs-comment">// 克隆原始类型</span>
  <span class="hljs-keyword">if</span> (!isObject(target)) &#123;
    <span class="hljs-keyword">return</span> target;
  &#125;

  <span class="hljs-comment">// 初始化</span>
  <span class="hljs-keyword">const</span> type = getType(target);
  <span class="hljs-keyword">let</span> cloneTarget;
  <span class="hljs-keyword">if</span> (deepTag.includes(type)) &#123;
    cloneTarget = getInit(target, type);
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">return</span> cloneOtherType(target, type);
  &#125;

  <span class="hljs-comment">// 防止循环引用</span>
  <span class="hljs-keyword">if</span> (map.get(target)) &#123;
    <span class="hljs-keyword">return</span> map.get(target);
  &#125;
  map.set(target, cloneTarget);

  <span class="hljs-comment">// 克隆set</span>
  <span class="hljs-keyword">if</span> (type === setTag) &#123;
    target.forEach(<span class="hljs-function">(<span class="hljs-params">value</span>) =></span> &#123;
      cloneTarget.add(clone(value, map));
    &#125;);
    <span class="hljs-keyword">return</span> cloneTarget;
  &#125;

  <span class="hljs-comment">// 克隆map</span>
  <span class="hljs-keyword">if</span> (type === mapTag) &#123;
    target.forEach(<span class="hljs-function">(<span class="hljs-params">value, key</span>) =></span> &#123;
      cloneTarget.set(key, clone(value, map));
    &#125;);
    <span class="hljs-keyword">return</span> cloneTarget;
  &#125;

  <span class="hljs-comment">// 克隆对象和数组</span>
  <span class="hljs-keyword">const</span> keys = type === arrayTag ? <span class="hljs-literal">undefined</span> : <span class="hljs-built_in">Object</span>.keys(target);
  forEach(keys || target, <span class="hljs-function">(<span class="hljs-params">value, key</span>) =></span> &#123;
    <span class="hljs-keyword">if</span> (keys) &#123;
      key = value;
    &#125;
    cloneTarget[key] = clone(target[key], map);
  &#125;);

  <span class="hljs-keyword">return</span> cloneTarget;
&#125;

<span class="hljs-built_in">module</span>.exports = &#123;
  clone,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">第三方库的实现</h2>
<h3 data-id="heading-12">Underscore —— _.clone()</h3>
<ul>
<li>在 Underscore 中有这样一个方法：_.clone()，这个方法实际上是一种浅复制 (shallow-copy)，所有嵌套的对象和数组都是直接复制引用而并没有进行深复制。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 源码地址 https://github.com/jashkenas/underscore/blob/master/modules/clone.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">clone</span>(<span class="hljs-params">obj</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (!isObject(obj)) <span class="hljs-keyword">return</span> obj;
  <span class="hljs-keyword">return</span> isArray(obj) ? obj.slice() : extend(&#123;&#125;, obj);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">jQuery —— <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi mathvariant="normal">.</mi><mi>c</mi><mi>l</mi><mi>o</mi><mi>n</mi><mi>e</mi><mo stretchy="false">(</mo><mo stretchy="false">)</mo><mi mathvariant="normal">/</mi></mrow><annotation encoding="application/x-tex">.clone() / </annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord">.</span><span class="mord mathnormal">c</span><span class="mord mathnormal" style="margin-right:0.01968em;">l</span><span class="mord mathnormal">o</span><span class="mord mathnormal">n</span><span class="mord mathnormal">e</span><span class="mopen">(</span><span class="mclose">)</span><span class="mord">/</span></span></span></span></span>.extend()</h3>
<ul>
<li>在 jQuery 中也有这么一个叫 <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi mathvariant="normal">.</mi><mi>c</mi><mi>l</mi><mi>o</mi><mi>n</mi><mi>e</mi><mo stretchy="false">(</mo><mo stretchy="false">)</mo><mtext>的方法，可是它并不是用于一般的</mtext><mi>J</mi><mi>S</mi><mtext>对象的深复制，而是用于</mtext><mi>D</mi><mi>O</mi><mi>M</mi><mtext>对象。与</mtext><mi>U</mi><mi>n</mi><mi>d</mi><mi>e</mi><mi>r</mi><mi>s</mi><mi>c</mi><mi>o</mi><mi>r</mi><mi>e</mi><mtext>类似，我们也是可以通过</mtext></mrow><annotation encoding="application/x-tex">.clone() 的方法，可是它并不是用于一般的 JS 对象的深复制，而是用于 DOM 对象。与 Underscore 类似，我们也是可以通过 </annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord">.</span><span class="mord mathnormal">c</span><span class="mord mathnormal" style="margin-right:0.01968em;">l</span><span class="mord mathnormal">o</span><span class="mord mathnormal">n</span><span class="mord mathnormal">e</span><span class="mopen">(</span><span class="mclose">)</span><span class="mord cjk_fallback">的</span><span class="mord cjk_fallback">方</span><span class="mord cjk_fallback">法</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">可</span><span class="mord cjk_fallback">是</span><span class="mord cjk_fallback">它</span><span class="mord cjk_fallback">并</span><span class="mord cjk_fallback">不</span><span class="mord cjk_fallback">是</span><span class="mord cjk_fallback">用</span><span class="mord cjk_fallback">于</span><span class="mord cjk_fallback">一</span><span class="mord cjk_fallback">般</span><span class="mord cjk_fallback">的</span><span class="mord mathnormal" style="margin-right:0.09618em;">J</span><span class="mord mathnormal" style="margin-right:0.05764em;">S</span><span class="mord cjk_fallback">对</span><span class="mord cjk_fallback">象</span><span class="mord cjk_fallback">的</span><span class="mord cjk_fallback">深</span><span class="mord cjk_fallback">复</span><span class="mord cjk_fallback">制</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">而</span><span class="mord cjk_fallback">是</span><span class="mord cjk_fallback">用</span><span class="mord cjk_fallback">于</span><span class="mord mathnormal" style="margin-right:0.02778em;">D</span><span class="mord mathnormal" style="margin-right:0.02778em;">O</span><span class="mord mathnormal" style="margin-right:0.10903em;">M</span><span class="mord cjk_fallback">对</span><span class="mord cjk_fallback">象</span><span class="mord cjk_fallback">。</span><span class="mord cjk_fallback">与</span><span class="mord mathnormal" style="margin-right:0.10903em;">U</span><span class="mord mathnormal">n</span><span class="mord mathnormal">d</span><span class="mord mathnormal">e</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">s</span><span class="mord mathnormal">c</span><span class="mord mathnormal">o</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">e</span><span class="mord cjk_fallback">类</span><span class="mord cjk_fallback">似</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">我</span><span class="mord cjk_fallback">们</span><span class="mord cjk_fallback">也</span><span class="mord cjk_fallback">是</span><span class="mord cjk_fallback">可</span><span class="mord cjk_fallback">以</span><span class="mord cjk_fallback">通</span><span class="mord cjk_fallback">过</span></span></span></span></span>.extend() 方法来完成深复制。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjquery%2Fjquery%2Fblob%2Fmain%2Fsrc%2Fcore.js%23L116" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/jquery/jquery/blob/main/src/core.js#L116" ref="nofollow noopener noreferrer">源码</a></li>
</ul>
<h3 data-id="heading-14">lodash —— <em>.clone() /</em>.cloneDeep()</h3>
<ul>
<li>
<p>在 lodash 中关于复制的方法有两个，分别是*.clone()和*.cloneDeep()。其中*.clone(obj, true)等价于*.cloneDeep(obj)。使用上，lodash 和前两者并没有太大的区别，但看了源码会发现，Underscore 的实现只有 30 行左右，而 jQuery 也不过 60 多行。可 lodash 中与深复制相关的代码却有上百行，为什么呢？</p>
</li>
<li>
<p>因为 jQuery 无法正确深复制 JSON 对象以外的对象，而 lodash 花了大量的代码来实现 ES6 引入的大量新的标准对象。而且，lodash 针对存在环的对象的处理也是非常出色的。因此相较而言，lodash 在深复制上的行为反馈比前两个库好很多，是更拥抱未来的一个第三方库。</p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Flodash%2Flodash%2Fblob%2Fmaster%2FcloneDeep.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/lodash/lodash/blob/master/cloneDeep.js" ref="nofollow noopener noreferrer">源码</a></p>
</li>
</ul>
<h2 data-id="heading-15">总结</h2>
<ul>
<li>本文由浅入深地介绍了深浅拷贝的定义，实现深拷贝中需要考虑的问题与要点，一步步地完善了一个深拷贝，最后对比了一下市面上的常用库的深拷贝实现。</li>
<li>希望看完本篇文章能让大家对深浅拷贝有个更深刻的认识。能自行实现一个基本的深拷贝函数。</li>
</ul>
<p>欢迎大家留言讨论，祝工作顺利、生活愉快！</p>
<p>我是bigo前端，下期见。</p></div>  
</div>
            