
---
title: '浅析JS垃圾回收'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4937'
author: 掘金
comments: false
date: Sun, 04 Apr 2021 00:22:08 GMT
thumbnail: 'https://picsum.photos/400/300?random=4937'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>当我们创建对象、函数这些东西的时候，我们都需要一个内存去储存他们，即JS的内存管理其实是自动进行的，但是如果我们不需要这些东西的时候，JS是怎么知道的呢？又是怎么清理它们的呢？</p>
<p>JS中内存管理的主要概念是可达性(reachability)，可达值是指保证那些可以被访问或者使用的值保存在内存中。比如一些固有值(roots)和可以通过引用和引用链从根访问到的值。那么这些可达值就无法被删除，剩下的其他值，就受到JS引擎中垃圾收集器的监视并删除。</p>
<p>举个例子：</p>
<pre><code class="copyable">let user = &#123;
  name: "John"
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时全局变量<code>user</code>引用该对象<code>&#123;name: "John"&#125;</code>。该对象的属性存储一个基元，因此将其绘制在对象内部。可是如果这个<code>user</code>被覆盖<code>user = null;</code>，那么这个引用就丢失了，即John变得不可达，没有对象能够访问他，也没有引用他，因此垃圾收集器就会将这个数据删除。</p>
<p>现在我们将引用从复制<code>user</code>到<code>admin</code>：</p>
<pre><code class="copyable">let user = &#123;
  name: "John"
&#125;;

let admin = user;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我们再次执行<code>user = null;</code>时，该对象虽然值为<code>null</code>，但是我们仍然可以通过<code>admin</code>全局变量访问，因此它还在内存中。可是如果我们也覆盖<code>admin</code>，它就会被删除了。</p>
<p>再来个复杂的例子：</p>
<pre><code class="copyable">function marry(man, woman) &#123;
  woman.husband = man;
  man.wife = woman;

  return &#123;
    father: man,
    mother: woman
  &#125;
&#125;

let family = marry(&#123;
  name: "John"
&#125;, &#123;
  name: "Ann"
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时所有的对象都是可达的，但是我们现在要做的是删除<code>family.father</code>这个引用，此时John还是可达的，那我们删除<code>family.mother.husband</code>这个引用呢？答案还是一样，可是如果我们将它们都删除呢？那么此时John就只有传出的引用，没有传入的引用，说得通俗一些就是你认识你的偶像，可是你的偶像却不认识你，这个时候你只能被无情的删除了。</p>
<p>同样的代码，我们执行<code>family = null;</code>会怎么样呢？此时就要引入一个概念即<strong>可达性概念</strong>，虽然家庭成员之间相互间都有传出和传入的引用，但是此时<code>family</code>对象已经和根断开了，那么John和Ann以及他们之间的相互引用链接，都会被删除。</p>
<h5 data-id="heading-0">说完概念，具体垃圾回收是怎么执行的呢？</h5>
<p>基本的垃圾收集算法称为“<strong>标记清除</strong>”。</p>
<p>它定期执行以下步骤：</p>
<ol>
<li>垃圾收集器收取他们的根并对其进行“标记”。</li>
<li>访问并“标记”所有来自它们的引用。</li>
<li>访问标记的对象以及标记它们的引用。记住所有访问过的对象，以免将来再次访问同一对象。</li>
<li>依此类推，直到访问了所有可到达的引用（从根开始）。</li>
<li>把除了被标记以外的所有对象删除。</li>
</ol>
<p>这就是垃圾收集工作原理的概念。</p>
<h5 data-id="heading-1">注意</h5>
<ul>
<li>垃圾收集是自动执行的。我们不能强迫或阻止它。</li>
<li>当对象可以访问时，它们会保留在内存中。</li>
<li>被引用与可(从根)访问不同：一堆相互链接的对象可能都不可访问。</li>
</ul>
<p><a href="https://javascript.info/garbage-collection" target="_blank" rel="nofollow noopener noreferrer">文章来源在这</a></p>
<h4 data-id="heading-2">感谢观看哟</h4></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            