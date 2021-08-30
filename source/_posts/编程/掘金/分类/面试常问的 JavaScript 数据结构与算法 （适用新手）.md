
---
title: '面试常问的 JavaScript 数据结构与算法 （适用新手）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7721'
author: 掘金
comments: false
date: Sun, 29 Aug 2021 23:30:31 GMT
thumbnail: 'https://picsum.photos/400/300?random=7721'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1 数组</h1>
<h2 data-id="heading-1">数组去重（三种方法）</h2>
<p>方法一：arr.forEach</p>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">unique</span>(<span class="hljs-params">arr</span>) </span>&#123;
  <span class="hljs-comment">//1 申明一个空数组存放</span>
  <span class="hljs-keyword">const</span> res = []
  <span class="hljs-comment">//2 遍历原始数组</span>
  arr.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span>&#123;
    <span class="hljs-comment">//3 判断 res数组中是否包含这个元素</span>
    <span class="hljs-keyword">if</span> (res.indexOf(item) === -<span class="hljs-number">1</span>)&#123;
      <span class="hljs-comment">//4 若干没有，就插入res中</span>
      res.push(item)
    &#125;
  &#125;)
  <span class="hljs-comment">// 5 返回结果</span>
  <span class="hljs-keyword">return</span> res
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>方法二：arr.forEach+空对象</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">unique2</span>(<span class="hljs-params">arr</span>) </span>&#123;
  <span class="hljs-comment">//1 申明一个空数组存放</span>
  <span class="hljs-keyword">const</span> res = []
  <span class="hljs-comment">//2 申明空对象，</span>
  <span class="hljs-keyword">const</span> obj = &#123;&#125;
  <span class="hljs-comment">//3 遍历原始数组</span>
  arr.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span>&#123;
    <span class="hljs-comment">//5</span>
    <span class="hljs-keyword">if</span> (obj[item] === <span class="hljs-literal">undefined</span>)&#123;
      <span class="hljs-comment">//4 将arr中遍历的item作为下标存在obj&#123;&#125;中，比较会方便</span>
      obj[item] = <span class="hljs-literal">true</span>
      res.push(item)
    &#125;
  &#125;)
  <span class="hljs-comment">//6 返回结果</span>
  <span class="hljs-keyword">return</span> res
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>方法三：集合Set，利用集合Set自身的去重功能</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">unique3</span>(<span class="hljs-params">arr</span>) </span>&#123;
  <span class="hljs-comment">//将数组转化为集合Set，这里利用集合Set自身的去重功能</span>
  <span class="hljs-keyword">let</span> set = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(arr)
  <span class="hljs-comment">//将set展开 创建数组</span>
  <span class="hljs-keyword">let</span> array = [...set]
  <span class="hljs-keyword">return</span> array
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 方法三（精简）：</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">unique4</span>(<span class="hljs-params">arr</span>) </span>&#123;
  <span class="hljs-keyword">return</span> [... <span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(arr)]
&#125;

<span class="hljs-built_in">console</span>.log(unique4([<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">2</span>,<span class="hljs-number">4</span>,<span class="hljs-number">3</span>,<span class="hljs-number">2</span>]))
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">concat 数组合并</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">concat</span>(<span class="hljs-params">arr,...args </span>)</span>&#123;
  <span class="hljs-comment">//1 申明空数组,将arr中数压到res中</span>
  <span class="hljs-keyword">const</span> res =  [...arr]
  <span class="hljs-comment">//2 遍历数组</span>
  args.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span>&#123;
    <span class="hljs-comment">//3判断item是否为数组</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(item)) &#123;
      <span class="hljs-comment">//4 ...item 是解构赋值，逐个将item数组中元素放入res</span>
      res.push(...item)
    &#125; <span class="hljs-keyword">else</span> &#123;
      res.push(item)
    &#125;
  &#125;)
  <span class="hljs-comment">//5 返回结果</span>
  <span class="hljs-keyword">return</span> res
&#125;

<span class="hljs-built_in">console</span>.log(concat(arr,[<span class="hljs-number">4</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>],<span class="hljs-number">7</span>,<span class="hljs-number">8</span>,<span class="hljs-number">9</span>))

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">slice 数组切片</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
* @param &#123;Array&#125; arr
* @param &#123;Number&#125; start
* @param &#123;Number&#125; begin
*
* */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">slice</span>(<span class="hljs-params">arr,start,end</span>)</span>&#123;
  <span class="hljs-comment">//5 加入判断，arr长度是否为0</span>
  <span class="hljs-keyword">if</span> (arr.length === <span class="hljs-number">0</span>) &#123;
    <span class="hljs-keyword">return</span> []
  &#125;
  <span class="hljs-comment">// 6 判断 start,如果传了，就是start，要不就是0</span>
  start = start || <span class="hljs-number">0</span>
  <span class="hljs-comment">//7 如果start 越界，就返回空数组</span>
  <span class="hljs-keyword">if</span> (start >= arr.length)&#123;
    <span class="hljs-keyword">return</span> []
  &#125;
  <span class="hljs-comment">//8 判断end,如果传了，end，要不默认就是数组长度</span>
  end = end || arr.length
  <span class="hljs-comment">//9 如果end小于start就将数组长度给end</span>
  <span class="hljs-keyword">if</span> (end < start)&#123;
    end = arr.length
  &#125;

  <span class="hljs-comment">//1申明一个空数组，slice返回是新数组</span>
  <span class="hljs-keyword">const</span> res = []
  <span class="hljs-comment">//2 遍历对象</span>
  <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < arr.length; i++)&#123;
    <span class="hljs-comment">//3 判断i在数组的位置是否合法</span>
    <span class="hljs-keyword">if</span> (i >= start & i < end) &#123;
      <span class="hljs-comment">//4 将下标对应的元素加入res[]</span>
      res.push(arr[i])
    &#125;
  &#125;
  <span class="hljs-comment">//10 返回结果</span>
  <span class="hljs-keyword">return</span> res
&#125;



<span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>,<span class="hljs-number">7</span>,<span class="hljs-number">8</span>]
<span class="hljs-keyword">const</span> res = slice(arr,<span class="hljs-number">3</span>,<span class="hljs-number">6</span>)
<span class="hljs-built_in">console</span>.log(res)


<span class="hljs-comment">// let res = arr.slice(1,4)//切片数组2-4</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">数组扁平化（两种方法）</h2>
<p>（多维数组>一维数组）</p>
<p>方法一：使用递归（原数组上操作）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">flatten1</span>(<span class="hljs-params">arr</span>)</span>&#123;
<span class="hljs-comment">//  1申明一个空数组</span>
  <span class="hljs-keyword">let</span> res = []
  <span class="hljs-comment">//2 遍历数组</span>
  arr.forEach(<span class="hljs-function"><span class="hljs-params">item</span>=></span>&#123;
    <span class="hljs-comment">//3 判断item是否是数组</span>
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(item)) &#123;
      <span class="hljs-comment">//4 item是数组，递归</span>
      <span class="hljs-comment">//并且与res[]连接</span>
      <span class="hljs-comment">// 重新赋值</span>
      res = res.concat(flatten1(item))
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">//5 如果item不是数组</span>
      <span class="hljs-comment">//重新赋值</span>
      res = res.concat(item)
    &#125;
  &#125;)
<span class="hljs-comment">//6 返回结果</span>
  <span class="hljs-keyword">return</span> res
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>方法二，使用some,新数组上操作</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">flatten2</span>(<span class="hljs-params">arr</span>)</span>&#123;
  <span class="hljs-comment">//1 申明数组</span>
  <span class="hljs-keyword">let</span> res = [...arr]
  <span class="hljs-comment">//2 循环判断</span>
  <span class="hljs-comment">//some用了判断数组中是否有一个满足条件，就返回true</span>
  <span class="hljs-keyword">while</span> (res.some(<span class="hljs-function"><span class="hljs-params">item</span>=></span><span class="hljs-built_in">Array</span>.isArray(item)))&#123;
    <span class="hljs-comment">//res = [].concat([1,2,[3,4,[5,6]],7])</span>
    <span class="hljs-comment">//第一次循环完毕即[1,2,3,4,[5,6],7]</span>
    <span class="hljs-comment">//第二次循环完毕即[1,2,3,4,5,6,7]</span>
    res = [].concat(...res)
  &#125;
  <span class="hljs-comment">//3 返回结果</span>
  <span class="hljs-keyword">return</span> res
&#125;


<span class="hljs-keyword">let</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,[<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,[<span class="hljs-number">5</span>,<span class="hljs-number">6</span>]],<span class="hljs-number">7</span>]
<span class="hljs-built_in">console</span>.log(flatten2(arr))
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">数组分块（一维数组 > 二维数组）</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">chunk</span>(<span class="hljs-params">arr,size=<span class="hljs-number">1</span></span>)</span>&#123;
  <span class="hljs-comment">//7 判断</span>
  <span class="hljs-keyword">if</span> (arr.length === <span class="hljs-number">0</span>)&#123;
    <span class="hljs-keyword">return</span> []
  &#125;
  <span class="hljs-comment">//1 申明两个变量</span>
  <span class="hljs-keyword">let</span> res = []
  <span class="hljs-keyword">let</span> tmp = []<span class="hljs-comment">//先放tmp[]，再放入res[]</span>
  <span class="hljs-comment">//2 遍历</span>
  arr.forEach(<span class="hljs-function"><span class="hljs-params">item</span>=></span>&#123;
    <span class="hljs-comment">//4 判断tmp长度是否为0</span>
    <span class="hljs-keyword">if</span> (tmp.length == <span class="hljs-number">0</span>) &#123;
      <span class="hljs-comment">//5 将tmp压入res[]中</span>
      res.push(tmp)
    &#125;
    <span class="hljs-comment">//3 将元素压入tmp</span>
    tmp.push(item)
    <span class="hljs-comment">// 6 判断tmp数组中长度是否为size，如果是则清空</span>
    <span class="hljs-keyword">if</span> (tmp.length === size)&#123;
      tmp = []
    &#125;
  &#125;)
  <span class="hljs-comment">// 8 返回结果</span>
  <span class="hljs-keyword">return</span> res
&#125;

<span class="hljs-built_in">console</span>.log(chunk([<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>,<span class="hljs-number">7</span>],<span class="hljs-number">4</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">数组差集 ：</h2>
<p>API: filter,遍历，并过滤
对数组1遍历，对比数组2</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">diff</span>(<span class="hljs-params">arr1,arr2=[]</span>)</span>&#123;
  <span class="hljs-comment">//2 判断参数</span>
  <span class="hljs-keyword">if</span> (arr1.length === <span class="hljs-number">0</span>) &#123;
    <span class="hljs-keyword">return</span>  []
  &#125;
  <span class="hljs-comment">//3 判断参数</span>
  <span class="hljs-keyword">if</span> (arr2.length === <span class="hljs-number">0</span>) &#123;
    <span class="hljs-keyword">return</span>  arr1.slice()<span class="hljs-comment">//slice 返回新数组</span>
  &#125;
  <span class="hljs-comment">// 1 filter,遍历，并过滤</span>
  <span class="hljs-keyword">const</span> res = arr1.filter(<span class="hljs-function"><span class="hljs-params">item</span> =></span> !arr2.includes(item))
  <span class="hljs-keyword">return</span> res
&#125;

<span class="hljs-built_in">console</span>.log(diff([<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>],[<span class="hljs-number">5</span>,<span class="hljs-number">6</span>,<span class="hljs-number">8</span>]))
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">删除数组中单个元素（原数组 or 新数组）</h2>
<h3 data-id="heading-8">原数组</h3>
<p>splice改变数组长度，当减掉一个元素后，后面的元素都会前移，因此需要相应减少i的值</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">removeWithoutCopy</span>(<span class="hljs-params">arr, item</span>) </span>&#123;
  <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < arr.length; i++)&#123;
    <span class="hljs-keyword">if</span> (item == arr[i])&#123;
   <span class="hljs-comment">// splice改变数组长度，当减掉一个元素后，后面的元素都会前移，因此需要相应减少i的值</span>
      arr.splice(i,<span class="hljs-number">1</span>)
      i--;
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> arr
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">新数组（两个方法）filter</h3>
<p>方法一:filter</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">remove2</span>(<span class="hljs-params">arr, item</span>) </span>&#123;
  <span class="hljs-keyword">return</span> arr.filter(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">a</span>) </span>&#123;
    <span class="hljs-keyword">return</span> a != item
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>方法二:暴力破解</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">remove1</span>(<span class="hljs-params">arr, item</span>) </span>&#123;
  <span class="hljs-keyword">var</span> arr1 = []
  <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < arr.length; i++)&#123;
    <span class="hljs-keyword">if</span> (arr[i] != item) &#123;
      <span class="hljs-comment">//如果arr[i]不等于item，就加入数组a</span>
      arr1.push(arr[i])
    &#125;
  &#125;
  <span class="hljs-keyword">return</span> arr1
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">删除数组中部分元素</h2>
<p>API：pull（array,...value）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">pull</span>(<span class="hljs-params">arr,...args</span>) </span>&#123;
  <span class="hljs-comment">//1 申明空数组 ，保存删除的元素</span>
  <span class="hljs-keyword">const</span> res = []
  <span class="hljs-comment">// 2 遍历arr</span>
  <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < arr.length; i++)&#123;    <span class="hljs-comment">//3 判断i 元素在不在arg数组中</span>
    <span class="hljs-keyword">if</span>(args.includes(arr[i]))&#123;
      <span class="hljs-comment">//4将arr[i]传入res[]</span>
      res.push(arr[i])
      <span class="hljs-comment">//5 删除arr[i]</span>
      arr.splice(i,<span class="hljs-number">1</span>)<span class="hljs-comment">//splice可以改变原始数组</span>
      <span class="hljs-comment">//6 下标自减</span>
      i--
    &#125;
  &#125;
  <span class="hljs-comment">// 7 返回</span>
  <span class="hljs-keyword">return</span> res

&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">pullAll</span>(<span class="hljs-params">arr,values</span>) </span>&#123;
  <span class="hljs-keyword">return</span> pull(arr,...values)
&#125;

arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>]
<span class="hljs-comment">// console.log(pull(arr ,1,4,5))</span>
<span class="hljs-comment">// console.log(arr)</span>
<span class="hljs-built_in">console</span>.log(pullAll(arr,[<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>]))
<span class="hljs-built_in">console</span>.log(arr)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">得到数组部分元素</h2>
<p>filter 改变原始数组，产生新数组</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">drop</span>(<span class="hljs-params">arr,size</span>) </span>&#123;
  <span class="hljs-comment">//filter 过滤原始数组，产生新数组</span>
  <span class="hljs-keyword">return</span> arr.filter(<span class="hljs-function">(<span class="hljs-params">value ,index</span>)=></span>&#123;
    <span class="hljs-keyword">return</span> index >= size
  &#125;)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">dropRights</span>(<span class="hljs-params">arr,size</span>)</span>&#123;
  <span class="hljs-keyword">return</span> arr.filter(<span class="hljs-function">(<span class="hljs-params">value ,index</span>)=></span>&#123;
    <span class="hljs-keyword">return</span>  index < arr.length-size
  &#125;)
&#125;
<span class="hljs-built_in">console</span>.log(drop([<span class="hljs-number">1</span>,<span class="hljs-number">24</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>],<span class="hljs-number">2</span>))
<span class="hljs-built_in">console</span>.log(dropRights([<span class="hljs-number">1</span>,<span class="hljs-number">24</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>],<span class="hljs-number">2</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-12">2 Array.prototype.XXX</h1>
<h2 data-id="heading-13">map，计算，返回新数组</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>]
<span class="hljs-keyword">const</span> map1 = arr.map(<span class="hljs-function"><span class="hljs-params">x</span>=></span> x*<span class="hljs-number">2</span>)
<span class="hljs-built_in">console</span>.log(map1)<span class="hljs-comment">//[ 2, 4, 6, 8 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>原理：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">map</span>(<span class="hljs-params">arr,callback</span>) </span>&#123;
  <span class="hljs-comment">// 1 申明一个空数组</span>
  <span class="hljs-keyword">let</span> res = []
  <span class="hljs-comment">//2 遍历数组</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i <arr.length ; i++) &#123;
    <span class="hljs-comment">//3 执行回调</span>
    res.push(callback(arr[i],i))
  &#125;
  <span class="hljs-comment">// 4 返回结果</span>
  <span class="hljs-keyword">return</span> res
&#125;


<span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>]

<span class="hljs-comment">// map 函数的调用</span>
<span class="hljs-keyword">const</span> res = map(arr,<span class="hljs-function">(<span class="hljs-params">item,index</span>)=></span> &#123;
  <span class="hljs-keyword">return</span> item * <span class="hljs-number">2</span>
&#125;)

<span class="hljs-built_in">console</span>.log(res)<span class="hljs-comment">//[ 2, 4, 6, 8 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">reduce 回调、暂存器、返回</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>]

<span class="hljs-keyword">let</span> res = arr.reduce(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res,value</span>) </span>&#123;
<span class="hljs-comment">//这里res 是暂存器，默认是0开始</span>
  <span class="hljs-keyword">return</span> res + value
&#125;,<span class="hljs-number">0</span>)

<span class="hljs-built_in">console</span>.log(res)<span class="hljs-comment">//10</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>封装原理：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reduce</span>(<span class="hljs-params">arr,callback,initValue</span>) </span>&#123;
  <span class="hljs-comment">//申明变量</span>
  <span class="hljs-keyword">let</span> res = initValue
  <span class="hljs-comment">//循环遍历</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i <arr.length ; i++) &#123;
    <span class="hljs-comment">//执行回调,赋值给res，即暂存器</span>
    res = callback(res, arr[i])
  &#125;
  <span class="hljs-comment">//返回结果</span>
  <span class="hljs-keyword">return</span> res
&#125;

<span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>]
<span class="hljs-comment">// reduce 函数的调用</span>
<span class="hljs-keyword">let</span> res = reduce(arr, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res,value</span>) </span>&#123;
  <span class="hljs-keyword">return</span> res + value
&#125;,<span class="hljs-number">10</span>)

<span class="hljs-built_in">console</span>.log(res)<span class="hljs-comment">//20</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">filter 过滤，返回新数组</h2>
<pre><code class="copyable">const arr = [1,2,3,4]
// 返回原数组中奇数
const res = arr.filter(item=> item % 2 === 1)

console.log(res)//[ 1, 3 ]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>原理：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">filter</span>(<span class="hljs-params">arr,callback</span>) </span>&#123;
  <span class="hljs-comment">// 1 申明一个空数组</span>
  <span class="hljs-keyword">let</span> res = []
  <span class="hljs-comment">//2 遍历数组</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i <arr.length ; i++) &#123;
    <span class="hljs-comment">//3 执行回调</span>
    <span class="hljs-keyword">let</span> a = (callback(arr[i],i))
    <span class="hljs-comment">//4 判断回调函数是否是真</span>
    <span class="hljs-keyword">if</span> (a) &#123;
      res.push(arr[i])
    &#125;
  &#125;
  <span class="hljs-comment">// 4 返回结果</span>
  <span class="hljs-keyword">return</span> res
&#125;


<span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>]
<span class="hljs-comment">// 返回原数组中奇数</span>
<span class="hljs-keyword">const</span> res = filter(arr,<span class="hljs-function"><span class="hljs-params">item</span>=></span> item % <span class="hljs-number">2</span> === <span class="hljs-number">1</span>)

<span class="hljs-built_in">console</span>.log(res)<span class="hljs-comment">//[ 1, 3 ]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">every 每一个满足则true，否则，false</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>]
<span class="hljs-keyword">const</span> res = arr.every(<span class="hljs-function"><span class="hljs-params">item</span>=></span> item > <span class="hljs-number">2</span>)
<span class="hljs-built_in">console</span>.log(res)<span class="hljs-comment">//false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>原理：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">every</span>(<span class="hljs-params">arr,callback</span>) </span>&#123;
  <span class="hljs-comment">//1 遍历数组</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i <arr.length ; i++) &#123;
    <span class="hljs-comment">//2 执行回调</span>
    <span class="hljs-keyword">let</span> res =callback(arr[i],i)
    <span class="hljs-comment">//3 判断回调条件是否满足（逆向判断）</span>
    <span class="hljs-keyword">if</span> (!res)&#123;
      <span class="hljs-comment">//返回false</span>
      <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>
    &#125;
  &#125;
  <span class="hljs-comment">// 4 满足判断条件，返回true</span>
  <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
&#125;


<span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>]

<span class="hljs-keyword">const</span> res = every(arr,<span class="hljs-function">(<span class="hljs-params">item,index</span>)=></span> &#123;
  <span class="hljs-keyword">return</span> item > <span class="hljs-number">2</span>
&#125;)
<span class="hljs-built_in">console</span>.log(res)<span class="hljs-comment">//false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-17">some 有一个满足则true，否则，false</h2>
<pre><code class="copyable">const arr = [1,2,3,4]
const res = arr.some(item=> item > 2)
console.log(res)//true
<span class="copy-code-btn">复制代码</span></code></pre>
<p>原理：</p>
<pre><code class="copyable">function some(arr,callback) &#123;
  //1 遍历数组
  for (let i = 0; i <arr.length ; i++) &#123;
    //2 执行回调
    let res =callback(arr[i],i)
    //3 判断回调条件是否有一个满足
    if (res)&#123;
      //返回true
      return true
    &#125;
  &#125;
  // 4 一个都满足判断条件，返回 false
  return false
&#125;


const arr = [1,2,3,4]

const res = some(arr,(item,index)=> &#123;
  return item > 2
&#125;)
console.log(res)//true
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-18">find 找到数组中第一个true的值，否则undefined</h2>
<pre><code class="copyable">const arr = [1,2,3,4]
const res = arr.find( item=> item > 2)
console.log(res)//3
<span class="copy-code-btn">复制代码</span></code></pre>
<p>原理</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">find</span>(<span class="hljs-params">arr,callback</span>) </span>&#123;
  <span class="hljs-comment">//1 遍历数组</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i <arr.length ; i++) &#123;
    <span class="hljs-comment">//2 执行回调</span>
    <span class="hljs-keyword">let</span> res =callback(arr[i],i)
    <span class="hljs-comment">//3 判断</span>
    <span class="hljs-keyword">if</span> (res)&#123;
      <span class="hljs-comment">//返回当前正在遍历的元素</span>
      <span class="hljs-keyword">return</span> arr[i]
    &#125;
  &#125;
  <span class="hljs-comment">// 4 没有满足判断条件，返回undefined</span>
  <span class="hljs-keyword">return</span> <span class="hljs-literal">undefined</span>
&#125;


<span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>]

<span class="hljs-keyword">const</span> res = find(arr,<span class="hljs-function">(<span class="hljs-params">item,index</span>)=></span> &#123;
  <span class="hljs-keyword">return</span> item > <span class="hljs-number">2</span>
&#125;)
<span class="hljs-built_in">console</span>.log(res)<span class="hljs-comment">//3</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-19">findIndex 与find类似，返回为true的索引，否则返回-1</h2>
<pre><code class="copyable">const arr = [1,7,2,9,4]
const res = arr.findIndex(item=> item > 6)
console.log(res)//1
<span class="copy-code-btn">复制代码</span></code></pre>
<p>原理：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">findIndex</span>(<span class="hljs-params">arr,callback</span>) </span>&#123;
  <span class="hljs-comment">//1 遍历数组</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i <arr.length ; i++) &#123;
    <span class="hljs-comment">//2 执行回调</span>
    <span class="hljs-keyword">let</span> res =callback(arr[i],i)
    <span class="hljs-comment">//3 判断</span>
    <span class="hljs-keyword">if</span> (res)&#123;
      <span class="hljs-comment">//返回当前正在遍历的元素下标</span>
      <span class="hljs-keyword">return</span> i
    &#125;
  &#125;
  <span class="hljs-comment">// 4 没有满足判断条件，返回-1</span>
  <span class="hljs-keyword">return</span> -<span class="hljs-number">1</span>
&#125;


<span class="hljs-keyword">const</span> arr = [<span class="hljs-number">1</span>,<span class="hljs-number">7</span>,<span class="hljs-number">2</span>,<span class="hljs-number">9</span>,<span class="hljs-number">4</span>]

<span class="hljs-keyword">const</span> res = findIndex(arr,<span class="hljs-function">(<span class="hljs-params">item,index</span>)=></span> &#123;
  <span class="hljs-keyword">return</span> item > <span class="hljs-number">2</span>
&#125;)
<span class="hljs-built_in">console</span>.log(res)<span class="hljs-comment">//1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-20">3 函数相关</h1>
<h2 data-id="heading-21">call ，改变this的指向</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">call</span>(<span class="hljs-params">Fn,obj,...args</span>) </span>&#123;
  <span class="hljs-comment">//4 判断</span>
  <span class="hljs-keyword">if</span> (obj === <span class="hljs-literal">undefined</span> || obj === <span class="hljs-literal">null</span>)&#123;
    obj = globalThis<span class="hljs-comment">//全局对象</span>
  &#125;
  <span class="hljs-comment">//1 为obj 添加临时方法</span>
  obj.temp = Fn<span class="hljs-comment">//this 指向都是一样的</span>
  <span class="hljs-comment">// 2 调用temp方法</span>
  <span class="hljs-keyword">let</span> res = obj.temp(...args)
  <span class="hljs-comment">//3 删除temp方法</span>
  <span class="hljs-keyword">delete</span> obj.temp
  <span class="hljs-comment">// 返回执行结果</span>
  <span class="hljs-keyword">return</span> res
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-comment">//申明一个函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">a,b</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>)
  <span class="hljs-keyword">return</span> a + b + <span class="hljs-built_in">this</span>.c
&#125;
<span class="hljs-comment">//申明一个对象</span>
<span class="hljs-keyword">let</span> obj = &#123;
  <span class="hljs-attr">c</span>:<span class="hljs-number">200</span>
&#125;
<span class="hljs-comment">//添加全局属性</span>
<span class="hljs-comment">// window.c = 123</span>

<span class="hljs-comment">//执行call函数</span>
<span class="hljs-built_in">console</span>.log(call(add,obj,<span class="hljs-number">10</span>,<span class="hljs-number">20</span>))
<span class="hljs-comment">// console.log(call(add,null,1,2))</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-22">apply，改变this的指向,传入参数是数组</h2>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">apply</span>(<span class="hljs-params">Fn,obj,args</span>) </span>&#123;
  <span class="hljs-comment">//4 判断</span>
  <span class="hljs-keyword">if</span> (obj === <span class="hljs-literal">undefined</span> || obj === <span class="hljs-literal">null</span>)&#123;
    obj = globalThis<span class="hljs-comment">//全局对象</span>
  &#125;
  <span class="hljs-comment">//1 为obj 添加临时方法</span>
  obj.temp = Fn
  <span class="hljs-comment">// 2 调用temp方法</span>
  <span class="hljs-keyword">let</span> res = obj.temp(...args)
  <span class="hljs-comment">//3 删除temp方法</span>
  <span class="hljs-keyword">delete</span> obj.temp
  <span class="hljs-comment">// 返回执行结果</span>
  <span class="hljs-keyword">return</span> res
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//申明一个函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">a,b</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>)
  <span class="hljs-keyword">return</span> a + b + <span class="hljs-built_in">this</span>.c
&#125;
<span class="hljs-comment">//申明一个对象</span>
<span class="hljs-keyword">let</span> obj = &#123;
  <span class="hljs-attr">c</span>:<span class="hljs-number">200</span>
&#125;
<span class="hljs-comment">//添加全局属性</span>
<span class="hljs-comment">// window.c = 123</span>

<span class="hljs-comment">//执行函数</span>
<span class="hljs-built_in">console</span>.log(apply(add,obj,[<span class="hljs-number">10</span>,<span class="hljs-number">20</span>]))
<span class="hljs-comment">// console.log(apply(add,null,[1,2]))</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-23">bind</h2>
<p>类似call，
bind不执行函数，创建新函数</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bind</span>(<span class="hljs-params">Fn,obj,...args</span>) </span>&#123;
  <span class="hljs-comment">// 返回新函数</span>
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">...args2</span>) </span>&#123;
    <span class="hljs-comment">//执行call 函数</span>
    <span class="hljs-keyword">return</span> call(Fn, obj,...args,...args2)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">
<span class="hljs-comment">//申明一个函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">a,b</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>)
  <span class="hljs-keyword">return</span> a + b + <span class="hljs-built_in">this</span>.c
&#125;
<span class="hljs-comment">//申明一个对象</span>
<span class="hljs-keyword">let</span> obj = &#123;
  <span class="hljs-attr">c</span>:<span class="hljs-number">200</span>
&#125;
<span class="hljs-comment">//添加全局属性</span>
<span class="hljs-comment">// window.c = 123</span>

<span class="hljs-comment">//执行函数</span>

<span class="hljs-keyword">let</span> fn = bind(add,obj,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>)
<span class="hljs-built_in">console</span>.log(fn(<span class="hljs-number">1</span>,<span class="hljs-number">2</span>))
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            