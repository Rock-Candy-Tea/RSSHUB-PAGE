
---
title: '由JS在对象数组循环过程中修改对象属性所导致的问题谈到对象的浅拷贝和深拷贝'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5331'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 17:23:33 GMT
thumbnail: 'https://picsum.photos/400/300?random=5331'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>最近在工作中用React.js写前端，接触了很多JS的东东，在做数组嵌套循环的时候发现一个问题：</p>
<p>我的需求是想把arr1和arr2添加到resultArr 中，并且给arr2分别添加index属性为arr1的idnex值。代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> arr1 = [&#123; <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'a'</span>, <span class="hljs-attr">index</span>: <span class="hljs-number">0</span> &#125;, &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'b'</span>, <span class="hljs-attr">index</span>: <span class="hljs-number">1</span> &#125;];
<span class="hljs-keyword">const</span> arr2 = [&#123; <span class="hljs-attr">id</span>: <span class="hljs-number">3</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'c'</span> &#125;, &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">4</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'d'</span> &#125;];

<span class="hljs-keyword">const</span> resultArr = [];
arr1.forEach(<span class="hljs-function">(<span class="hljs-params">itemA, index</span>) =></span> &#123;
resultArr.push(itemA);
arr2.forEach(<span class="hljs-function">(<span class="hljs-params">itemB</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> item = itemB;
    item.index = index;
    resultArr.push(item);
  &#125;);
&#125;);

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'resultArr: '</span>,resultArr );
    <span class="hljs-comment">/*期望结果：
    0: &#123;id: 1, name: "a", index: 0&#125;
    1: &#123;id: 3, name: "c", index: 0&#125;
    2: &#123;id: 4, name: "d", index: 0&#125;
    3: &#123;id: 2, name: "b", index: 1&#125;
    4: &#123;id: 3, name: "c", index: 1&#125;
    5: &#123;id: 4, name: "d", index: 1&#125;
    */</span>
    <span class="hljs-comment">/*实际结果：
     0: &#123;id: 1, name: "a", index: 0&#125;
    1: &#123;id: 3, name: "c", index: 1&#125;
    2: &#123;id: 4, name: "d", index: 1&#125;
    3: &#123;id: 2, name: "b", index: 1&#125;
    4: &#123;id: 3, name: "c", index: 1&#125;
    5: &#123;id: 4, name: "d", index: 1&#125;
    */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>刚开始看到这个确实比较懵逼，在网上冲浪（划水）的间隙查了一下，应该是在arr2循环中改变了arr1数组对象的属性导致的。</p>
<p>改为以下代码就没有这个问题了。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> arr1 = [&#123; <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'a'</span>, <span class="hljs-attr">index</span>: <span class="hljs-number">0</span> &#125;, &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">2</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'b'</span>, <span class="hljs-attr">index</span>: <span class="hljs-number">1</span> &#125;];
<span class="hljs-keyword">const</span> arr2 = [&#123; <span class="hljs-attr">id</span>: <span class="hljs-number">3</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'c'</span> &#125;, &#123; <span class="hljs-attr">id</span>: <span class="hljs-number">4</span>, <span class="hljs-attr">name</span>: <span class="hljs-string">'d'</span> &#125;];

<span class="hljs-keyword">const</span> resultArr = [];
arr1.forEach(<span class="hljs-function">(<span class="hljs-params">itemA, index</span>) =></span> &#123;
resultArr.push(itemA);
    arr2.forEach(<span class="hljs-function">(<span class="hljs-params">itemB</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> item = &#123;
        <span class="hljs-attr">id</span>: itemB.id,
        <span class="hljs-attr">name</span>: itemB.name,
        <span class="hljs-attr">index</span>: index
        &#125;;
        resultArr.push(item);
    &#125;);
&#125;);

<span class="hljs-built_in">console</span>.log(resultArr);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>知其然，更应知其所以然（这样才有利于更好的装逼），很明显这里两个写法唯一的不同就是数组的浅拷贝和深拷贝了，那么接下来就说说js的浅拷贝和深拷贝吧！</p>
<p>浅拷贝是拷贝一层，深层次的对象就拷贝其引用；深拷贝是拷贝多层，每一级别的数据都会拷贝出来；</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">   <span class="hljs-keyword">const</span> obj1 = &#123;
      <span class="hljs-attr">a</span>: <span class="hljs-string">'hello'</span>,
      <span class="hljs-attr">b</span>: <span class="hljs-number">18</span>,
      <span class="hljs-attr">c</span>: &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'如花'</span>,
        <span class="hljs-attr">weight</span>: <span class="hljs-number">200</span>
      &#125;
    &#125;;
    <span class="hljs-keyword">const</span> obj2 = <span class="hljs-built_in">Object</span>.assign(&#123;&#125;, obj1);
    obj2.b = <span class="hljs-number">30</span>;
    obj2.c.name = <span class="hljs-string">'凤姐'</span>;
<span class="hljs-comment">//结果如下：</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'obj1'</span>, obj1);<span class="hljs-comment">//a:'hello',b:18,c:&#123;name:'凤姐',weight:200&#125;</span>
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'obj2'</span>, obj2);<span class="hljs-comment">//a:'hello',b:30,c:&#123;name:'凤姐',weight:200&#125;</span>
    
    <span class="hljs-comment">//在copy这个对象的时候，属性a和属性b是直接copy它的值，而属性c也是一个对象，所以copy的是其引用地址</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>常用的assign()，concat()等方法都是浅拷贝，另外需要注意以下写法：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-keyword">const</span> obj1 = &#123;
      <span class="hljs-attr">a</span>: <span class="hljs-string">'hello'</span>,
      <span class="hljs-attr">b</span>: <span class="hljs-number">18</span>,
      <span class="hljs-attr">c</span>: &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'如花'</span>,
        <span class="hljs-attr">weight</span>: <span class="hljs-number">200</span>
      &#125;
 &#125;;
 <span class="hljs-keyword">const</span> obj2 = obj1;
 obj2.b = <span class="hljs-number">30</span>;
 obj2.c.name = <span class="hljs-string">'凤姐'</span>;
 <span class="hljs-comment">//此时是直接进行的地址引用，对obj2的修改都将影响到arr1</span>
 <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'obj1'</span>, obj1);<span class="hljs-comment">//a:'hello',b:30,c:&#123;name:'凤姐',weight:200&#125;</span>
 <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'obj2'</span>, obj2);<span class="hljs-comment">//a:'hello',b:30,c:&#123;name:'凤姐',weight:200&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么如何实现深拷贝呢？
最直接的办法就是挨个属性赋值：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> obj1 = &#123;
      <span class="hljs-attr">a</span>: <span class="hljs-string">'hello'</span>,
      <span class="hljs-attr">b</span>: <span class="hljs-number">18</span>,
      <span class="hljs-attr">c</span>: &#123;
        <span class="hljs-attr">name</span>: <span class="hljs-string">'如花'</span>,
      &#125;
&#125;;
<span class="hljs-keyword">const</span> obj2 = &#123;
<span class="hljs-attr">a</span>: obj1.a,
    <span class="hljs-attr">b</span>: obj1.b,
    <span class="hljs-attr">c</span>: &#123;
    <span class="hljs-attr">name</span>: obj1.c.name,
    &#125;
&#125;;
obj2.b = <span class="hljs-number">30</span>;
obj2.c.name = <span class="hljs-string">'凤姐'</span>;

<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'obj1'</span>, obj1);<span class="hljs-comment">//a:'hello',b:18,c:&#123;name:'如花',weight:200&#125;</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'obj2'</span>, obj2);<span class="hljs-comment">//a:'hello',b:30,c:&#123;name:'凤姐',weight:200&#125;</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此外还可以先将a对象转为json，再将json赋值给b对象，不过这两种方法总归没那么优雅，其实用ES6语法写起来倒也不算复杂。</p>
<p>作为一名后端工程师，暂时就了解到这里了，最后用后端习惯的表达方式来总结一下浅拷贝和深拷贝：</p>
<p><strong>在对一个对象进行拷贝时，如果其属性是基本类型（即 Boolean，null，undefined，String 和 Number），则是进行的值拷贝，而如果其属性是Array，Function或Object，则拷贝的是其引用地址，在改变拷贝后的对象中的该属性时，会直接修改该引用所实际指向的地址的值，即会改变原对象该属性的值。</strong></p></div>  
</div>
            