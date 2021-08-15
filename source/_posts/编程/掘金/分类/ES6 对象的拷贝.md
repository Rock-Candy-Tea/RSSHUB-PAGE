
---
title: 'ES6 对象的拷贝'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5236'
author: 掘金
comments: false
date: Sat, 14 Aug 2021 04:37:49 GMT
thumbnail: 'https://picsum.photos/400/300?random=5236'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第12天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p><code>JavaScript</code> 中，怎么拷贝对象呢？<code>ES5</code> 中的做法是把对象遍历一下，把数据逐项拷贝到目标对象中去；<code>ES6</code> 则提供了一个新的 <code>API</code>，实现对象数据的拷贝：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> target = &#123;&#125; <span class="hljs-comment">// 目标对象（就是我要把数据拷贝到这个对象上来）</span>
<span class="hljs-keyword">const</span> source = &#123; <span class="hljs-attr">b</span>: <span class="hljs-number">4</span>, <span class="hljs-attr">c</span>: <span class="hljs-number">5</span> &#125; <span class="hljs-comment">// 源对象（就是要把数据拷贝出来的地方）</span>
<span class="hljs-built_in">Object</span>.assign(target, source) <span class="hljs-comment">// 拷贝 source 对象的数据到 target 对象上来</span>
<span class="hljs-built_in">console</span>.log(target) <span class="hljs-comment">// &#123;b: 4, c: 5&#125;</span>
<span class="hljs-built_in">console</span>.log(source) <span class="hljs-comment">// &#123;b: 4, c: 5&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是，这个 <code>API</code> 是有“缺陷”的，比如目标对象和源对象的数据结构如下时，拷贝的结果就会丢失掉“<code>h: 10</code>”：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> target = &#123;
  <span class="hljs-attr">a</span>: &#123;
    <span class="hljs-attr">b</span>: &#123;
      <span class="hljs-attr">c</span>: &#123;
        <span class="hljs-attr">d</span>: <span class="hljs-number">9</span>
      &#125;
    &#125;,
    <span class="hljs-attr">e</span>: <span class="hljs-number">5</span>,
    <span class="hljs-attr">f</span>: <span class="hljs-number">6</span>,
    <span class="hljs-attr">h</span>: <span class="hljs-number">10</span>
  &#125;,
  <span class="hljs-attr">i</span>: <span class="hljs-number">3</span>
&#125;;
<span class="hljs-keyword">const</span> source = &#123;
  <span class="hljs-attr">a</span>: &#123;
    <span class="hljs-attr">b</span>: &#123;
      <span class="hljs-attr">c</span>: &#123;
        <span class="hljs-attr">d</span>: <span class="hljs-number">1</span>
      &#125;
    &#125;,
    <span class="hljs-attr">e</span>: <span class="hljs-number">2</span>,
    <span class="hljs-attr">f</span>: <span class="hljs-number">3</span>
  &#125;
&#125;;
<span class="hljs-built_in">Object</span>.assign(target, source);
<span class="hljs-built_in">console</span>.log(target);
<span class="hljs-comment">/* 运行结果：
&#123;
  a: &#123;
    b: &#123;
      c: &#123;
        d: 1
      &#125;
    &#125;,
    e: 2,
    f: 3
  &#125;,
  i: 3
&#125;
 */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样的结果是不合理的，拷贝可以修改原来的数据，但不应该删除原有的东西（原来的“<code>h: 10</code>”没有了）
实际上，<code>Object.assign()</code> 实现的是浅复制（对于不是引用类型的值，会进行数据的替换，
对于引用类型的值，则不再遍历，只是将引用的对象的地址进行了替换），而不是深复制，
所以才会出现上面的问题（<code>a</code> 是个对象，属于引用类型的值，所以在拷贝时拷贝的是地址值，
也就是用源对象中 <code>a</code> 的地址值替换掉了目标对象中 <code>a</code> 的地址值，<code>a</code> 里面的数据也就完全被替换掉了）
所以呢，使用 <code>Object.assign(target, source)</code> 时，<code>source</code> 到 <code>target</code> 的拷贝过程中，
可能会出现数据丢失的情况，就是它不能实现深拷贝，只能实现浅拷贝。
如果在使用 <code>Object.assign()</code> 时想要实现深拷贝，则还需要进行递归。</p>
<p>如果目标对象传入的是 <code>undefined</code> 和 <code>null</code> 将会怎么样呢？</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> tar1 = <span class="hljs-literal">undefined</span>
<span class="hljs-keyword">const</span> tar2 = <span class="hljs-literal">null</span>
<span class="hljs-keyword">const</span> sou = &#123;
  <span class="hljs-attr">a</span>: <span class="hljs-number">2</span>,
  <span class="hljs-attr">b</span>: <span class="hljs-number">3</span>,
  <span class="hljs-attr">c</span>: <span class="hljs-number">4</span>
&#125;
<span class="hljs-built_in">Object</span>.assign(tar1, sou) <span class="hljs-comment">// Uncaught TypeError: Cannot convert undefined or null to object</span>
<span class="hljs-built_in">Object</span>.assign(tar2, sou) <span class="hljs-comment">// Uncaught TypeError: Cannot convert undefined or null to object</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可见，目标对象传入的是 <code>undefined</code> 或 <code>null</code> 时，会报错，“不能将 <code>undefined</code> 或 <code>null</code> 转换为对象”。</p>
<p>如果源对象传入的是 <code>undefined</code> 和 <code>null</code> 将会怎么样呢？</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> tar = &#123;
  <span class="hljs-attr">a</span>: &#123;
    <span class="hljs-attr">b</span>: &#123;
      <span class="hljs-attr">c</span>: &#123;
        <span class="hljs-attr">d</span>: <span class="hljs-number">9</span>
      &#125;
    &#125;,
    <span class="hljs-attr">e</span>: <span class="hljs-number">5</span>,
    <span class="hljs-attr">f</span>: <span class="hljs-number">6</span>,
    <span class="hljs-attr">h</span>: <span class="hljs-number">10</span>
  &#125;,
  <span class="hljs-attr">i</span>: <span class="hljs-number">3</span>
&#125;
<span class="hljs-keyword">const</span> sou1 = <span class="hljs-literal">undefined</span>
<span class="hljs-keyword">const</span> sou2 = <span class="hljs-literal">null</span>
<span class="hljs-built_in">Object</span>.assign(tar, sou1)
<span class="hljs-built_in">console</span>.log(tar)
<span class="hljs-comment">/* 运行结果：
&#123;
  a: &#123;
    b: &#123;
      c: &#123;
        d: 9
      &#125;
    &#125;,
    e: 5,
    f: 6,
    h: 10
  &#125;,
  i: 3
&#125;
*/</span>
tar = &#123;
  <span class="hljs-attr">a</span>: &#123;
    <span class="hljs-attr">b</span>: &#123;
      <span class="hljs-attr">c</span>: &#123;
        <span class="hljs-attr">d</span>: <span class="hljs-number">9</span>
      &#125;
    &#125;,
    <span class="hljs-attr">e</span>: <span class="hljs-number">5</span>,
    <span class="hljs-attr">f</span>: <span class="hljs-number">6</span>,
    <span class="hljs-attr">h</span>: <span class="hljs-number">10</span>
  &#125;,
  <span class="hljs-attr">i</span>: <span class="hljs-number">3</span>
&#125;
<span class="hljs-built_in">Object</span>.assign(tar, sou2)
<span class="hljs-built_in">console</span>.log(tar)
<span class="hljs-comment">/* 运行结果：
&#123;
  a: &#123;
    b: &#123;
      c: &#123;
        d: 9
      &#125;
    &#125;,
    e: 5,
    f: 6,
    h: 10
  &#125;,
  i: 3
&#125;
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可见，源对象传入的是 <code>undefined</code> 或 <code>null</code> 时，拷贝后目标对象还是其原来的值。</p>
<p>如果目标对象<strong>是</strong>个嵌套的对象，子对象的属性会被覆盖吗？</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> tg = &#123;
  <span class="hljs-attr">a</span>: &#123;
    <span class="hljs-attr">b</span>: <span class="hljs-number">2</span>,
    <span class="hljs-attr">d</span>: <span class="hljs-number">4</span>
  &#125;
&#125;
<span class="hljs-keyword">const</span> sr1 = &#123;
  <span class="hljs-attr">e</span>: <span class="hljs-number">7</span>
&#125;
<span class="hljs-built_in">Object</span>.assign(tg, sr1)
<span class="hljs-built_in">console</span>.log(tg)
<span class="hljs-comment">/* 运行结果：
&#123;
  a: &#123;
    b: 2,
    d: 4
  &#125;,
  e: 7
&#125;
*/</span>
tg = &#123;
  <span class="hljs-attr">a</span>: &#123;
    <span class="hljs-attr">b</span>: <span class="hljs-number">2</span>,
    <span class="hljs-attr">d</span>: <span class="hljs-number">4</span>
  &#125;
&#125;
<span class="hljs-keyword">const</span> sr2 = &#123;
  <span class="hljs-attr">a</span>: &#123;
    <span class="hljs-attr">b</span>: <span class="hljs-number">2</span>
  &#125;
&#125;
<span class="hljs-built_in">Object</span>.assign(tg, sr2)
<span class="hljs-built_in">console</span>.log(tg)
<span class="hljs-comment">/* 运行结果：
&#123;
  a: &#123;
    b: 2
  &#125;
&#125;
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可见，目标对象是个嵌套的对象时，如果源对象中没有目标对象的子对象名，源对象的数据会拷贝到子对象的后面，子对象的属性不会被覆盖；如果源对象中存在目标对象的子对象名时，子对象的属性会被覆盖。</p>
<p>如果目标对象中<strong>存在</strong>嵌套的对象，子对象的属性会被覆盖吗？</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> tg = &#123;
  <span class="hljs-attr">a</span>: &#123;
    <span class="hljs-attr">b</span>: <span class="hljs-number">2</span>,
    <span class="hljs-attr">d</span>: <span class="hljs-number">4</span>
  &#125;,
  <span class="hljs-attr">c</span>: <span class="hljs-number">3</span>
&#125; <span class="hljs-comment">// 目标对象中嵌套了子对象 a</span>
<span class="hljs-keyword">const</span> sr1 = &#123;
  <span class="hljs-attr">e</span>: <span class="hljs-number">7</span>
&#125;
<span class="hljs-built_in">Object</span>.assign(tg, sr1)
<span class="hljs-built_in">console</span>.log(tg)
<span class="hljs-comment">/* 运行结果：
&#123;
  a: &#123;
    b: 2,
    d: 4
  &#125;,
  c: 3,
  e: 7
&#125;
*/</span>
tg = &#123;
  <span class="hljs-attr">a</span>: &#123;
    <span class="hljs-attr">b</span>: <span class="hljs-number">2</span>,
    <span class="hljs-attr">d</span>: <span class="hljs-number">4</span>
  &#125;,
  <span class="hljs-attr">c</span>: <span class="hljs-number">3</span>
&#125; <span class="hljs-comment">// 目标对象中嵌套了子对象 a</span>
<span class="hljs-keyword">const</span> sr2 = &#123;
  <span class="hljs-attr">a</span>: &#123;
    <span class="hljs-attr">b</span>: <span class="hljs-number">5</span>
  &#125;,
  <span class="hljs-attr">c</span>: <span class="hljs-number">6</span>,
  <span class="hljs-attr">e</span>: <span class="hljs-number">7</span>
&#125;
<span class="hljs-built_in">Object</span>.assign(tg, sr2)
<span class="hljs-built_in">console</span>.log(tg)
<span class="hljs-comment">/* 运行结果：
&#123;
  a: &#123;
    b: 5
  &#125;,
  c: 6,
  e: 7
&#125;
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可见，目标对象中存在嵌套的对象时，如果源对象中没有目标对象的子对象名，源对象的数据会添加到目标对象中，子对象的属性不会被覆盖；如果源对象中存在目标对象的子对象名时，子对象的属性会被覆盖。</p></div>  
</div>
            