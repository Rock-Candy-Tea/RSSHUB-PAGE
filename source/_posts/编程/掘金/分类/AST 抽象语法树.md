
---
title: 'AST 抽象语法树'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34012f9f8b374cfba299da1e591e8ff7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 19 Jun 2021 00:15:04 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34012f9f8b374cfba299da1e591e8ff7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第7天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557?utm_campaign=30day&utm_medium=Ccenter&utm_source=20210528" target="_blank">更文挑战</a></p>
<blockquote>
<p>本文是关于 AST 抽象语法树的学习笔记，这里做个总结与分享，有不足之处还望斧正~</p>
</blockquote>
<h1 data-id="heading-0">简介</h1>
<p>抽象语法树（Abstract Syntax Tree）本质上是一个 js 对象<br>
抽象语法树和虚拟节点的关系，如下图：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34012f9f8b374cfba299da1e591e8ff7~tplv-k3u1fbpfcp-watermark.image" alt="WPS图片-修改尺寸.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">相关算法储备</h1>
<h2 data-id="heading-2">指针思想</h2>
<p>指针就是下标位置<br>
相关练习题：寻找字符串中连续重复次数最多的字符</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 寻找字符串中连续重复次数最多的字符</span>
<span class="hljs-keyword">const</span> str = <span class="hljs-string">'aaaaaaaabbbbbbbbbbbbbbbbbcccccccccdddddd'</span>
<span class="hljs-comment">// start 和 end: 指针</span>
<span class="hljs-keyword">let</span> start = <span class="hljs-number">0</span>, end = <span class="hljs-number">1</span>, maxChar = str[<span class="hljs-number">0</span>], maxCharLength = <span class="hljs-number">0</span>
<span class="hljs-comment">// 当 start 指针在 str 长度范围内时进行循环</span>
<span class="hljs-keyword">while</span> (start < str.length)&#123;
  <span class="hljs-comment">// 如果两个指针指向的字符不一样了，说明不是连续重复的字符了</span>
  <span class="hljs-keyword">if</span> (str[start] !== str[end]) &#123;
    <span class="hljs-comment">// 如果指针之差大于之前存储的最大的连续数</span>
    <span class="hljs-keyword">if</span> (end - start > maxCharLength) &#123;
      maxCharLength = end - start
      maxChar = str[start]
    &#125;
    <span class="hljs-comment">// 让 start 指针直接追上 end 指针</span>
    start = end
  &#125;
  <span class="hljs-comment">// 每次循环 end 指针都向后移动一位</span>
  end++
&#125;
<span class="hljs-built_in">console</span>.log(maxChar, maxCharLength) <span class="hljs-comment">// b 17</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">递归</h2>
<p>凡是遇到“规则重复”，就要想到递归</p>
<h3 data-id="heading-4">斐波那契数列</h3>
<p>相关练习题：用递归的方法输出斐波那契数列前 10 项</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params">n</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.count(n)
  <span class="hljs-keyword">return</span> n === <span class="hljs-number">0</span> || n === <span class="hljs-number">1</span> ? <span class="hljs-number">1</span> : fn(n-<span class="hljs-number">1</span>) + fn(n-<span class="hljs-number">2</span>)
&#125;

<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10</span>; i++) &#123;
  <span class="hljs-built_in">console</span>.log(fn(i))
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>像上面这种解法，会有大量的重复执行，比如 <code>fn(9)</code> 的时候，会去执行 <code>fn(8)</code> 和 <code>fn(7)</code>，而执行 <code>fn(8)</code> 就会再执行一遍 <code>fn(7)</code>。为了避免这种重复的计算，我们可以用一个对象来缓存（cache）已经执行过的函数计算。如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 设置一个缓存对象，用于存储 fn(n) 的值</span>
<span class="hljs-keyword">let</span> cache = &#123;&#125;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params">n</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.count(n)
  <span class="hljs-comment">// 如果 cache 有 n 属性</span>
  <span class="hljs-keyword">if</span> (cache.hasOwnProperty(n)) &#123;
    <span class="hljs-keyword">return</span> cache[n]
  &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-comment">// cache 没有 n 属性，说明是第一次计算</span>
    <span class="hljs-keyword">const</span> v = n === <span class="hljs-number">0</span> || n === <span class="hljs-number">1</span> ? <span class="hljs-number">1</span> : fn(n-<span class="hljs-number">1</span>) + fn(n-<span class="hljs-number">2</span>)
    cache[n] = v
    <span class="hljs-keyword">return</span> v
  &#125;
&#125;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">10</span>; i++) &#123;
  <span class="hljs-built_in">console</span>.log(fn(i))
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">形式转换</h3>
<p>练习题：将数组 [1, 2, 3, [4, 5, [6, 7]], 8] 转为下图所示的对象格式</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/844a6ba11aae497fbe5a4dd7d640a1aa~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
此题有 2 种解法<br>
<strong>1. 递归数组</strong><br>
这种方法只有在遇到传给 convert 的参数为数组时，才递归</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, [<span class="hljs-number">4</span>, <span class="hljs-number">5</span>]]
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">convert</span>(<span class="hljs-params">arr</span>) </span>&#123;
  <span class="hljs-keyword">let</span> convertArr = []
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < arr.length; i++) &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> arr[i] === <span class="hljs-string">'number'</span>) &#123;
      convertArr.push(&#123; <span class="hljs-string">'value'</span>: arr[i] &#125;)
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(arr[i])) &#123;
      convertArr.push(&#123; <span class="hljs-string">'children'</span>: convert(arr[i]) &#125;)
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> convertArr
&#125;
<span class="hljs-keyword">const</span> res = convert(arr)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2. 递归数组的子元素</strong><br>
这里巧妙的运用了 map 方法的特点，从而传递给 convert2 的参数无论是数组还是数字，都递归</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, [<span class="hljs-number">4</span>, <span class="hljs-number">5</span>]]
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">convert2</span>(<span class="hljs-params">item</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> item === <span class="hljs-string">'number'</span>) &#123;
    <span class="hljs-keyword">return</span> &#123; <span class="hljs-string">'value'</span>: item &#125;
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(item)) &#123;
    <span class="hljs-keyword">return</span> &#123; <span class="hljs-string">'children'</span>: item.map(<span class="hljs-function"><span class="hljs-params">_item</span> =></span> convert2(_item)) &#125;
  &#125;
&#125;

<span class="hljs-keyword">const</span> res = convert2(arr)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">栈</h2>
<p>练习题：将字符串 3[1[a]2[b]] 转换成 abbabbabb<br>
这里就用到栈的思想，准备两个栈，一个存放数字，一个存放临时字符串，用一个指针遍历 3[1[a]2[b]]，</p>
<ul>
<li>当指针指向的为数字时，就把数字压入数字栈中</li>
<li>当指针指向的为<code>[</code>时，就把一个空字符串压入字符串栈中</li>
<li>当指针指向的为字母时，就把字符串栈中栈顶的这一项改为这个字母</li>
<li>当指针指向的为<code>]</code>时，就把数字弹栈，字符串中栈顶的这项重复刚刚这个弹出的数字次数，弹栈，然后拼接到新栈顶</li>
</ul>
<p>图示如下（这里没考虑数字或字母重复的情况，代码里会考虑进去）</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9217d9b350ef4aacac113e26e025ac37~tplv-k3u1fbpfcp-watermark.image" alt="gif5新文件.gif" loading="lazy" referrerpolicy="no-referrer"><br>
代码实现</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> str = <span class="hljs-string">'3[2[9abc]11[d]]'</span>

<span class="hljs-comment">// 指针</span>
<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>
<span class="hljs-comment">// 字符串从指针位置开始直至结束的部分</span>
<span class="hljs-keyword">let</span> restStr = str
<span class="hljs-comment">// 存放数字的栈</span>
<span class="hljs-keyword">const</span> stackNum = []
<span class="hljs-comment">// 存放字符串的栈</span>
<span class="hljs-keyword">const</span> stackStr = []

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">smartRepeat</span>(<span class="hljs-params">templateStr</span>) </span>&#123;
  <span class="hljs-comment">// 这里用 while 而不用 for 循环，因为 i 不一定每次都是 +1</span>
  <span class="hljs-keyword">while</span> (i < str.length - <span class="hljs-number">1</span>) &#123; 
    <span class="hljs-comment">/* 
    -1 是因为 str 最后一个必为 ]，如果不 -1，那么本例中当指针指到最后一个 ] 时，
    将对数字栈的栈顶，也是最后一个元素 3 进行出栈，
    然后是字符串栈的栈顶，也是最后一个元素 abcabcddddddddddd 进行出栈，然后重复 3 遍拼接到字符串栈的新栈顶，
    可是此时字符串栈已经没有元素了，新栈顶将是 undefined 
    */</span>
    restStr = str.substring(i)
    <span class="hljs-comment">// 如果是 数字 后面紧跟 [ 开头的字符串</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-regexp">/^(\d+)\[/</span>.test(restStr)) &#123;
      <span class="hljs-comment">// 捕获数字部分</span>
      <span class="hljs-keyword">const</span> nums = restStr.match(<span class="hljs-regexp">/^(\d+)\[/</span>)[<span class="hljs-number">1</span>]
      <span class="hljs-comment">// 把数字压入数字栈</span>
      stackNum.push(nums)
      <span class="hljs-comment">// 把空字符串压入字符串栈</span>
      stackStr.push(<span class="hljs-string">''</span>)
      <span class="hljs-comment">// 指针跳过相应的长度，+1 是因为把 ] 一起跳过了  </span>
      i += nums.length + <span class="hljs-number">1</span>
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-regexp">/^(\w+)\]/</span>.test(restStr)) &#123; <span class="hljs-comment">// 如果是 字母 后面紧跟 ] 开头的字符串</span>
      <span class="hljs-comment">// 捕获字母部分</span>
      <span class="hljs-keyword">const</span> str = restStr.match(<span class="hljs-regexp">/^(\w+)\]/</span>)[<span class="hljs-number">1</span>]
      <span class="hljs-comment">// 将字符串栈的栈顶的那一项赋值为捕获的字母</span>
      stackStr[stackStr.length - <span class="hljs-number">1</span>] = str
      <span class="hljs-comment">// 直接跳过字母的长度</span>
      i += str.length
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (restStr[<span class="hljs-number">0</span>] === <span class="hljs-string">']'</span>) &#123;
      <span class="hljs-comment">// 对数字栈进行出栈操作</span>
      <span class="hljs-keyword">const</span> popNum = stackNum.pop()
      <span class="hljs-comment">// 对字符串栈进行出栈</span>
      <span class="hljs-keyword">const</span> popStr = stackStr.pop()
      <span class="hljs-comment">// 字符串拼接</span>
      stackStr[stackStr.length - <span class="hljs-number">1</span>] += popStr.repeat(popNum)
      i++ 
    &#125;
  &#125;
  <span class="hljs-comment">// while 循环结束，此时数字栈和字符串栈各自剩下最后一个元素，将 字符串 重复 数字 遍返回</span>
  <span class="hljs-keyword">return</span> stackStr[<span class="hljs-number">0</span>].repeat(stackNum[<span class="hljs-number">0</span>])
&#125;
<span class="hljs-keyword">const</span> result = smartRepeat(str)
<span class="hljs-built_in">console</span>.log(result) <span class="hljs-comment">// 9abc9abcddddddddddd9abc9abcddddddddddd9abc9abcddddddddddd</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Tips：repeat是es6的字符串方法，构造并返回一个新字符串，该字符串包含被连接在一起的指定数量的字符串的副本。如果repeat的参数是字符串，则会先转换成数字。</p>
<h1 data-id="heading-7">手写实现 AST</h1>
<h2 data-id="heading-8">原理</h2>
<p>首先注意一点，平时在 .vue 文件里写在 template 里的看似 dom 的内容，事实上会经由 vue-loader 的解析，作为字符串提取处理。实现 AST 的原理根本上就是把一段字符串通过指针逐个遍历，根据不同情况进行不同的处理，进行一些栈操作，类似上文中栈里练习题。<br>
比如，想要将如下代码转成 AST</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>范特西<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>七里香<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">ul</span>></span> 
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>转换目标（AST）</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  tag: <span class="hljs-string">"div"</span>, 
  children: [
    &#123;
      tag: <span class="hljs-string">"h3"</span>, 
      children: [ &#123; text: <span class="hljs-string">"范特西"</span>, type: <span class="hljs-number">3</span> &#125;], 
      type: <span class="hljs-number">1</span>,
    &#125;,
    &#123;
      tag: <span class="hljs-string">"ul"</span>, 
      children: [
        &#123;
          tag: <span class="hljs-string">"li"</span>, 
          children: [&#123; text: <span class="hljs-string">"七里香"</span>, type: <span class="hljs-number">3</span> &#125;], 
          type: <span class="hljs-number">1</span>,
        &#125;
      ], 
      type: <span class="hljs-number">1</span>,
    &#125;
  ], 
  type: <span class="hljs-number">1</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以准备两个栈和一个用于遍历模板字符串的指针：</p>
<ul>
<li>指针遇到标签则往一个栈（标签栈）中加入该标签名，另一个栈（数组栈）中加入一个空数组（代码里为了方便事实上是加入一个对象 <code>&#123; tag: startTag, children: [] &#125;）</code></li>
<li>指针遇到文字则将数组栈中的栈顶的数组内容改为文字</li>
<li>指针遇到闭合标签则将标签栈和数组栈都进行出栈操作（数组栈出栈的内容就是标签栈出栈的标签的内容），然后将出栈的这两个元素组合下，拼接到数组栈的新栈顶的那个数组里。</li>
</ul>
<p>动图示意如下
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee4d80b0acd54eeba58346e5fde39032~tplv-k3u1fbpfcp-watermark.image" alt="gif5新文件 (1).gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">代码</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// index.js</span>
<span class="hljs-keyword">import</span> parse <span class="hljs-keyword">from</span> <span class="hljs-string">'./parse.js'</span>
<span class="hljs-keyword">const</span> templateStr = <span class="hljs-string">`<div>
  <h3 id="legend" class="jay song">范特西</h3>
  <ul>
    <li>七里香</li>
  </ul> 
</div>`</span>

<span class="hljs-keyword">const</span> ast = parse(templateStr)
<span class="hljs-built_in">console</span>.log(ast)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// parse.js</span>
<span class="hljs-keyword">import</span> parseAttrs <span class="hljs-keyword">from</span> <span class="hljs-string">'./parseAttrs.js'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">templateStr</span>) </span>&#123;
  <span class="hljs-comment">// 准备一个指针</span>
  <span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>
  <span class="hljs-comment">// 准备两个栈</span>
  <span class="hljs-comment">// 初始添加元素 &#123; children: [] &#125; 是因为如果不加， stackContent 在遇到最后一个封闭标签进行弹栈后，stackContent 里就没有元素了，也没有 .children 可以去 push 了</span>
  <span class="hljs-keyword">const</span> stackTag = [], stackContent = [&#123; <span class="hljs-attr">children</span>: [] &#125;] 
  <span class="hljs-comment">// 指针所指位置为开头的剩余字符串</span>
  <span class="hljs-keyword">let</span> restTemplateStr = templateStr
  <span class="hljs-comment">// 识别开始标签的正则</span>
  <span class="hljs-keyword">const</span> regExpStart = <span class="hljs-regexp">/^<([a-z]+[1-6]?)(\s?[^>]*)>/</span>

 <span class="hljs-keyword">while</span> (i < templateStr.length - <span class="hljs-number">1</span>) &#123;
  restTemplateStr = templateStr.substring(i)
  <span class="hljs-comment">// 遇到开始标签</span>
  <span class="hljs-keyword">if</span> (regExpStart.test(restTemplateStr)) &#123;
    <span class="hljs-keyword">const</span> startTag = restTemplateStr.match(regExpStart)[<span class="hljs-number">1</span>] <span class="hljs-comment">// 标签</span>
    <span class="hljs-keyword">const</span> attrsStr = restTemplateStr.match(regExpStart)[<span class="hljs-number">2</span>] <span class="hljs-comment">// 属性</span>
    <span class="hljs-comment">// 标签栈进行压栈</span>
    stackTag.push(startTag)
    <span class="hljs-comment">// 内容栈进行压栈</span>
    stackContent.push(&#123;
      <span class="hljs-attr">tag</span>: startTag,
      <span class="hljs-attr">attrs</span>: parseAttrs(attrsStr),
      <span class="hljs-attr">type</span>: <span class="hljs-number">1</span>,
      <span class="hljs-attr">children</span>: []
    &#125;)
    i += startTag.length + attrsStr.length  + <span class="hljs-number">2</span> <span class="hljs-comment">// +2 是因为还要算上 < 和 ></span>
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-regexp">/^<\/[a-z]+[1-6]?>/</span>.test(restTemplateStr)) &#123; <span class="hljs-comment">// 遇到结束标签</span>
    <span class="hljs-keyword">const</span> endTag = restTemplateStr.match(<span class="hljs-regexp">/^<\/([a-z]+[1-6]?)>/</span>)[<span class="hljs-number">1</span>]
    <span class="hljs-comment">// 结束标签应该与标签栈的栈顶标签一致</span>
    <span class="hljs-keyword">if</span> (endTag === stackTag[stackTag.length -<span class="hljs-number">1</span>]) &#123;
      <span class="hljs-comment">// 两个栈都进行弹栈</span>
      stackTag.pop()
      <span class="hljs-keyword">const</span> popContent = stackContent.pop()
      stackContent[stackContent.length - <span class="hljs-number">1</span>].children.push(popContent)
      i += endTag.length + <span class="hljs-number">3</span> <span class="hljs-comment">// +3 是因为还要算上 </ 和 ></span>
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">throw</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'标签'</span> + stackTag[stackTag.length -<span class="hljs-number">1</span>] + <span class="hljs-string">'没有闭合'</span>)
    &#125;
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-regexp">/^[^<]+<\/[a-z]+[1-6]?>/</span>.test(restTemplateStr)) &#123; <span class="hljs-comment">// 遇到内容</span>
    <span class="hljs-keyword">const</span> wordStr = restTemplateStr.match(<span class="hljs-regexp">/^([^<]+)<\/[a-z]+[1-6]?>/</span>)[<span class="hljs-number">1</span>] <span class="hljs-comment">// 捕获结束标签 </> 之前的内容，并且不能包括开始标签 <></span>
    <span class="hljs-keyword">if</span> (!<span class="hljs-regexp">/^\s+$/</span>.test(wordStr)) &#123; <span class="hljs-comment">// 如果捕获的内容不为空</span>
      <span class="hljs-comment">// 将内容栈栈顶元素进行赋值</span>
      stackContent[stackContent.length - <span class="hljs-number">1</span>].children.push(&#123;
        <span class="hljs-attr">text</span>: wordStr,
        <span class="hljs-attr">type</span>: <span class="hljs-number">3</span>
      &#125;)
    &#125;
    i += wordStr.length
  &#125; <span class="hljs-keyword">else</span> &#123;
    i++
  &#125;
 &#125;
 <span class="hljs-comment">// 因为定义 stackContent 的时候就默认添加了一项元素 &#123; children: [] &#125;，现在只要返回 children 的第一项就行 </span>
 <span class="hljs-keyword">return</span> stackContent[<span class="hljs-number">0</span>].children[<span class="hljs-number">0</span>]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了处理标签内可能的属性，注意，我们截取每个属性的标准不是简单的判断空格，因为属性里可能有多个值，他们之间可能有空格，所以判断依据是不在双引号内的空格</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// parseAttrs.js</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">attrsStr</span>) </span>&#123;
  <span class="hljs-keyword">const</span> attrsStrTrim = attrsStr.trim() <span class="hljs-comment">// 去空格</span>
  <span class="hljs-keyword">if</span> (attrsStrTrim) &#123;
    <span class="hljs-keyword">let</span> point = <span class="hljs-number">0</span> <span class="hljs-comment">// 断点</span>
    <span class="hljs-keyword">let</span> isYinhao = <span class="hljs-literal">false</span> <span class="hljs-comment">// 是否是引号</span>
    <span class="hljs-keyword">let</span> result = [] <span class="hljs-comment">// 结果数组</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>; index < attrsStrTrim.length; index++) &#123;
      <span class="hljs-keyword">if</span> (attrsStrTrim[index] === <span class="hljs-string">'"'</span>) isYinhao = !isYinhao
      <span class="hljs-comment">// 遇到空格且不在双引号内，就截取从 point 到此的字符串</span>
      <span class="hljs-keyword">if</span> (!isYinhao && <span class="hljs-regexp">/\s/</span>.test(attrsStrTrim[index])) &#123;
        <span class="hljs-keyword">const</span> attrs = attrsStrTrim.substring(point, index)
        result.push(attrs)
        point = index
      &#125;
    &#125;
    result.push(attrsStrTrim.substring(point + <span class="hljs-number">1</span>)) <span class="hljs-comment">// 最后一个属性是没有通过 for 循环得到的，所以要专门加上，+1 是为了去除开始的空格</span>
    <span class="hljs-comment">// ["id="legend"", "class="jay song""]</span>
    result = result.map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
      <span class="hljs-comment">// 根据等号拆分</span>
      <span class="hljs-keyword">const</span> itemMatch = item.match(<span class="hljs-regexp">/(.+)="(.+)"/</span>)
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">name</span>: itemMatch[<span class="hljs-number">1</span>],
        <span class="hljs-attr">value</span>: itemMatch[<span class="hljs-number">2</span>]
      &#125;
    &#125;)
    <span class="hljs-keyword">return</span> result
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">return</span> []
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此，本次分享的主要内容已经结束~</p>
<h1 data-id="heading-10">One More Thing</h1>
<p>这里对上文代码中用到的 <code>console.count()</code> 和 <code>hasOwnProperty()</code> 做点补充说明</p>
<h2 data-id="heading-11">console.count()</h2>
<p>首先，该特性是非标准的，请尽量不要在生产环境中使用它！<br>
输出 count() 被调用的次数，接受一个可选参数 label，每次调用，如果标签一样，则对应的计数数字会增加 1，如果不一样则重新开始计数</p>
<h2 data-id="heading-12">hasOwnProperty()</h2>
<p>用来检测一个对象是否含有特定的自身属性；<br>
和 <code>in</code> 运算符不同，<code>hasOwnProperty</code> 会忽略掉那些从原型链上继承到的属性，<br>
也就是上面的代码 <code>if (cache.hasOwnProperty(n))</code> 其实也可以写成 <code>if (n in cache)</code></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d160e26986d1447e8ef2dfe783fc6eb6~tplv-k3u1fbpfcp-watermark.image" alt="感谢.gif" loading="lazy" referrerpolicy="no-referrer"><br>
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a7fbbcaca1c480c942b7735a7228e9f~tplv-k3u1fbpfcp-watermark.image" alt="点赞.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            