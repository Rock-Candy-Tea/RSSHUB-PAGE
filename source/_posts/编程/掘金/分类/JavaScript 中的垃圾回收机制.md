
---
title: 'JavaScript 中的垃圾回收机制'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1cab6d0289794c3abd32edb415b01928~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 07 Apr 2021 17:58:20 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1cab6d0289794c3abd32edb415b01928~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><hr color="#000000" size="1"">
<h1 data-id="heading-0">一、内存管理</h1>
<ul>
<li>内存：计算机中所有程序的运行都在内存中进行，由可读写单元组成，表示一片可操作空间</li>
<li>管理： 人为的去操作一片空间的申请，使用，释放</li>
<li>内存管理： 开发者主动去申请空间，使用空间，释放空间</li>
<li>管理流程： 申请 -> 使用 -> 释放</li>
</ul>
<p><strong>JavaScript 不支持开发者进行手动的去对内存进行管理，当JS执行引擎执行代码的时候，遇见变量会自动的在内存中为该变量分配空间</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 申请内存空间</span>
<span class="hljs-keyword">let</span> obj = &#123;&#125;

<span class="hljs-comment">// 使用内存空间</span>
obj.name = <span class="hljs-string">'reborn'</span>

<span class="hljs-comment">// 释放内存空间</span>
obj = <span class="hljs-literal">null</span> 
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">二、JavaScript 中的垃圾回收</h1>
<p>垃圾的定义</p>
<ul>
<li>程序中不被引用（不被需要）的变量就是垃圾</li>
<li>程序中不能再访问到的是垃圾</li>
</ul>
<p>当满足这两点的时候，JS 执行引擎会将内存中的垃圾（空间）进行释放和回收。</p>
<p><strong>可达对象：从根上（全局作用域）出发，可以访问到的对象就是可达对象（作用域，引用）</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 申请内存空间，obj变量引用了这片空间</span>
<span class="hljs-keyword">const</span> obj = &#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'rebornjiang'</span>&#125;

<span class="hljs-comment">// 将 obj 的引用赋值给到 newObj 变量， 目前 newObj 也引用了这片内存空间。</span>
<span class="hljs-keyword">const</span> newObj = obj

<span class="hljs-comment">// 将 obj 的引用给释放掉</span>
obj = <span class="hljs-literal">null</span>

<span class="hljs-comment">// &#123;name: 'rebornjiang'&#125; 这片内存空间还是可达对象，其还有被引用的空间，所以不能够释放掉。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">三、GC算法</h1>
<p>GC的认识与作用
认识： GC是垃圾回收机制的简写
作用：GC可以找到内存中的垃圾，并释放和回收空间。</p>
<p>常见的GC算法</p>
<ul>
<li>引用计数</li>
<li>标记清除</li>
<li>标记整理</li>
<li>分代回收</li>
</ul>
<h2 data-id="heading-3">1. 引用计数算法</h2>
<p>核心思想：</p>
<ul>
<li>有专门的引用计数器用来计算对象（变量）的引用次数</li>
<li>当引用关系发生改变的时候会修改引用数字</li>
<li>判断当前引用数是否为0，如果为0 GC 将其进行作为垃圾进行释放和回收。</li>
</ul>
<p><strong>代码演示</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// case 1</span>
<span class="hljs-keyword">const</span> user1 = &#123; <span class="hljs-attr">age</span>: <span class="hljs-number">18</span> &#125;
<span class="hljs-keyword">const</span> user2 = &#123; <span class="hljs-attr">age</span>: <span class="hljs-number">20</span> &#125;
<span class="hljs-keyword">const</span> user3 = &#123; <span class="hljs-attr">age</span>: <span class="hljs-number">21</span> &#125;

<span class="hljs-keyword">const</span> ageList = [user1.age, user2.age, user3.age]

<span class="hljs-comment">// 当代码执行一轮之后，发现ageList这个数组中仍然还引用了 user1 , user2, user3</span>
<span class="hljs-comment">// 此时这些对象的引用计数就不是0，GC 就不会对其进行释放和回收。</span>


<span class="hljs-comment">// case 2</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> num1 = <span class="hljs-number">1</span>
  <span class="hljs-keyword">const</span> num2 = <span class="hljs-number">2</span>
&#125;

fn()

<span class="hljs-comment">// 当fn()执行结束之后，num1 与 num2 不在被使用，其引用计数器为0， GC 就会对其进行回收。 </span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>优点:</strong></p>
<ul>
<li>发现可以立即回收，当监听到内存中空间的引用为0时可以立即释放回收。</li>
<li>可最大程度减少程序暂停的可能。操作系统给每个程序分配的内存空间是有限的，当内存空间快达到最大值的时候，采用引用计数算法的回收机制会立即运行，找到引用计数为0的垃圾进行释放与回收。</li>
</ul>
<p><strong>缺点：</strong></p>
<ul>
<li>无法将循环引用的对象进行回收释放。参考下面代码示例</li>
<li>相对于其他的GC算法时间开销大。这是因为引用计数算法需要对内存空间对象维护一个引用计数，并监听引用的变化，当引用发生变化后，引用计数也要发生相应的改变。可内存中会有许多的空间对象要被维护和监听其引用计数，这样就会导致引用计数算法的时间开销大。</li>
<li>资源消耗大。因为其维护了一个引用计数器，当对象的引用发生变化之后需要更改引用计数器就会有消耗。</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 对象的循环引用</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> obj1 = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'rebornjiang'</span> &#125;
  <span class="hljs-keyword">const</span> obj2 = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'molly'</span> &#125;

  obj1.name = obj2
  obj2.name = obj1
  <span class="hljs-keyword">return</span> <span class="hljs-string">''</span>
&#125;
fn()

<span class="hljs-comment">// 即使fn执行结束之后，肯定会涉及垃圾回收，obj1 与 obj2 在全局也不会再有引用他们，但是此时obj1 与 obj2 的name属性相互引用了obj1 与 obj2这两个对象</span>
<span class="hljs-comment">// 其引用计数就不是0， 所以 采用 引用计数垃圾回收机制就不能将其进行释放与回收。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">2. 标记清除算法</h2>
<p>标记清除算法核心思想：</p>
<ul>
<li>分为标记和清除两个阶段</li>
<li>遍历所有的对象，然后将其活动对象(可达对象)进行标记</li>
<li>遍历所有的对象，然后将非标记的对象进行清除，释放回收相应的空间，将回收的空间加入空闲链表中，等待申请使用。</li>
<li>同时将标记对象进行取消其标记。</li>
</ul>
<p><strong>优点</strong></p>
<ul>
<li>相对引用计数算法 它可以清除循环引用对象</li>
</ul>
<p><img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1cab6d0289794c3abd32edb415b01928~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 将上面图示转换为代码</span>
<span class="hljs-keyword">const</span> A = &#123;
  <span class="hljs-attr">D</span>: &#123;&#125;
&#125;

<span class="hljs-keyword">const</span> B = &#123;&#125;

<span class="hljs-keyword">const</span> C = &#123;
  <span class="hljs-attr">E</span>: &#123;&#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> a1 = &#123;&#125;
  <span class="hljs-keyword">const</span> b1 = &#123;&#125;
  a1.obj1 = b1
  b1.obj2 = a1

  <span class="hljs-keyword">return</span> <span class="hljs-string">''</span>
&#125;

fn()

<span class="hljs-comment">// 当fn执行完成之后，a1与b1就与全局没有什么关系了，a1 b1就编程了不可达对象。</span>
<span class="hljs-comment">// 在标记清除算法的第一个阶段，就不会对 a1 b1 进行标记，等待标记清除算法的第二个</span>
<span class="hljs-comment">// 阶段会对 a1 b1 进行清除，同时会回收空间，将回收空间添加到空闲链表中，等待申请使用。</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>缺点</strong></p>
<ul>
<li>回收空间会是碎片化的空间，不能够使空间得到最大利用率。</li>
<li>标记清除是不可以立即清除垃圾的</li>
<li>
<ul>
<li>当标记清除和标记整理GC运行时，程序会暂停执行</li>
</ul>
</li>
</ul>
<p>模拟内存存储请看</p>
<p><strong>任何一个内存空间对象都会有两部分组成: 头 + 域
头: 存储空间源信息的，如空间的大小，空间的地址信息。
域： 专门用来存放数据的</strong>
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/826aa6a31c3c4307a1c3147f9817ecae~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
示例图说明：</p>
<ul>
<li>标记清除算法在第一轮标记的阶段会将 A 标记为可达对象，BC不进行标记。</li>
<li>标记清除算法的第二阶段会将未标记的BC不可达对象进行清除和回收其空间添加到空闲链表中，等待申请使用。</li>
<li>B 空间对象会有两个域存储空间，C空间对象会有 一个域存储空间。B C 加起来好像是释放了三个域存储空间，但是由于 B C 内存空间中多了一个 A空间，这就造成所回收的空间BC的空间地址不连续，这就造成内存空间的碎片化。</li>
<li>碎片化空间不能够组合使用，这就导致申请使用的空间大小需要跟释放空间大小相匹配才能够达到空间的最大利用率。</li>
</ul>
<h2 data-id="heading-5">3. 标记整理算法实现原理</h2>
<p>核心思想：</p>
<ul>
<li>标记整理算法是标记清除算法的增强操作，解决标记清除算法带来的空间碎片化的问题。</li>
<li>标记阶段的操作与 标记清除算法GC的标记阶段是一样的</li>
<li>标记整理会在清除阶段之前会执行整理，将标记的可达对象与未标记的不可达对象进行分类分开，使即将要被回收的空间地址产生连续。</li>
</ul>
<p>请查看下图：
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d2762c0f70f4fb4b3c18e11d0e1eefb~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b3c20b97a8264d048142bca965d1f9c5~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<strong>优点</strong></p>
<ul>
<li>与标记清除的优点相同</li>
<li>弥补了标记清除所带来的空间碎片化的缺点</li>
</ul>
<p><strong>缺点</strong></p>
<ul>
<li>当标记清除和标记整理GC运行时，程序会暂停执行</li>
<li>不能够立即回收垃圾</li>
</ul>
<h2 data-id="heading-6">4. 分代回收算法</h2>
<p>V8 垃圾回收策略就是采取分代回收，参考下一节。</p>
<h1 data-id="heading-7">四、V8 JS执行引擎的认识</h1>
<p><strong>V8的认识</strong></p>
<ul>
<li>V8 是 JS执行引擎</li>
<li>V8 速度快 是因为采用即时编译。不像其他 JS 执行引擎需要将代码编译成字节码，并解释成机器码。V8引擎在执行 JS 代码的时候可以直接翻译成机器码进行执行。</li>
<li>V8 内存设有上限。</li>
</ul>
<p><strong>V8 垃圾回收策略</strong>
采用分代回收思想, 这个代分为新生代对象与老生代对象，对不同代对象采取不同的GC算法进行垃圾回收。</p>
<ul>
<li>V8 执行引擎将内存存储空间一分为二，分为新生代存储空间与老生代存储空间</li>
<li>针对不同代对象采用不同的GC算法，使垃圾回收效率达到最高。</li>
</ul>
<p><img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01b00bfafe834d9d968eb90aeeecee8d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>新生代老生代对象的概念</strong></p>
<ul>
<li>新生代对象：存活时间较短的对象，如函数内的局部作用域的成员，执行完成之后就会进行回收。</li>
<li>老生代对象：存活时间长的对象，如全局作用域中的成员，闭包成员</li>
</ul>
<p>V8常用的GC算法</p>
<ul>
<li>分代回收</li>
<li>空间复制</li>
<li>标记清除</li>
<li>标记整理</li>
<li>标记增量</li>
</ul>
<h2 data-id="heading-8">1. V8 回收新生代对象</h2>
<p>新生代对象被存储在新生代存储空间，在不同操作系统的存储空间大小不一样，在 OSx64 为32M，OSx32 为16M。</p>
<p><img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7154d224f85748238b43d8228c59697c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>新生代对象回收实现的原理</p>
<ul>
<li>对新生代对象采用复制算法 + 标记整理算法进行垃圾回收</li>
<li>将新生代内存空间分为两个相等的大小的空间，如上图的 From  与 To模块</li>
<li>使用空间为From，空闲空间为To</li>
<li>代码执行的时候需要申请空间进行使用，会将所有的活动对象都分配到到 From 空间内</li>
<li>当From空间容量到达一定的程度之后会触发标记整理GC操作，将标记整理的活动对象拷贝到空闲空间To内</li>
<li>最后将 From空间内的变量进行完全的释放掉,并将From空间与 To空间进行交换。</li>
</ul>
<p>回收细节说明:</p>
<ul>
<li>拷贝过程可能会出现晋升</li>
<li>晋升就是将新生代对象移动至老生代</li>
<li>是否晋升取决于以下两个标准</li>
<li>一轮GC还存货的新生代需要晋升</li>
<li>To 空间的使用率超过25%</li>
</ul>
<h2 data-id="heading-9">2. V8 回收老生代对象</h2>
<p>老生代对象被存储在老生代存储空间，在不同操作系统的存储空间大小不一样，在 OSx64 为1.4G，OSx32 为700M。
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e7597b7e1ac4c2f833d89f19da56a96~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>老生代对象回收实现原理</p>
<ul>
<li>主要采用标记清除，标记整理，增量标记算法</li>
<li>首先使用标记清除完成垃圾空间的回收。对于碎片化存储空间等待标记整理算法进行处理。</li>
<li>当新生代对象要往老生代对象中移动的时候，并且老生代对象的内存空间又不足以分配给移动过来的对象，此时会采用标记整理对碎片化空间进行优化。</li>
<li>采用增量标记进行效率优化</li>
</ul>
<p><strong>增量标记算法</strong>
增量标记算法如图就可以知道，在对可达对象进行标记的时候不一次性标记完，乃是分段标记，提供垃圾回收的效率。
<img alt="在这里插入图片描述" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b8ed59c3bcc4dfbb2a8c29ceaab063d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            