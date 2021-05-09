
---
title: 'js之内存机制'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c3588fcc4dd4d7881c6e1af6ad99904~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 08 May 2021 22:52:48 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c3588fcc4dd4d7881c6e1af6ad99904~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>    数据结构是计算机存储，组织数据的方式。数据结构是指相互之间存在一种或多种特定关系的数据元素的集合。数据结构可以分为以下：数组、栈、堆、队列、链表、树、图、散列表类。本文主要讨论栈和堆。</p>
<h2 data-id="heading-0">一、堆栈</h2>
<p>    栈(Stack)又名堆栈，它作为一种数据结构，是一种只能在一端进行插入和删除操作的特殊线性表。它按照先进后出的原则存储数据，先进入的数据被压入栈底，最后的数据在栈顶，需要读取数据时从栈顶取出。它具有记忆作用，对栈的插入与删除操作不需要改变栈底指针。它允许在同一端进行插入和删除，允许进行插入和删除操作的一端称为栈顶(top)，另一端为栈底(bottom)；栈底固定，而栈顶浮动；插入一般称为进栈（PUSH），删除则称为退栈（POP）。栈中元素个数为零时称为空栈。</p>
<p>    堆(Heap)通常是一个可以被看做一棵完全二叉树的数组对象。每个节点有一个值，堆中某个节点的值总是不大于或不小于其父节点的值。常用来实现优先队列，堆的存取方式跟顺序没有关系，无序存取，根据引用直接获取。</p>
<p>    内存(Memory)是计算机中用于存储程序和数据的重要部件。JS内存空间分为栈(stack)、堆(heap)、池(一般也会归类为栈中)。 其中栈存放变量，堆存放复杂对象，池存放常量，所以也叫常量池。</p>
<p>    JavaScript中的基本类型保存在栈内存中，因为这些类型在内存中分别占有固定大小的空间，通过按值来访问。基本类型：Undefined、Null、Boolean、Number 、String（在很多语言中，字符串是使用对象表示的，因此被认为是引用类型，但在ECMAScript中不是）。大致来说栈内存有如下特点：存储基本数据类型，按值访问，存储的值大小固定，系统自动分配和释放空间，主要是用来执行程序，空间小运行效率高，先进后出，后进先出。</p>
<p>    而引用类型如对象，数组，函数它们保存在堆内存中。因为这种值大小不固定，其实说存储于堆中不太准确，因为引用类型的数据的地址指针是存储于栈中的，当我们想要访问引用类型的值，需要先从栈中获得对象的地址指针然后在通过地址指针找到堆中的所需要的数据。堆内存的特点：存储引用数据类型，存储的值大小不定，可动态调整，手动分配和释放空间，主要用来存放对象，空间大，运行效率较低，是一种无序的存储，可根据引用直接获取。　</p>
<p>    既然基本数据类型的值保存在栈内存中，访问方式是按值访问，那从一个变量向一个变量复制时，会在栈中创建一个新值，然后把值复制到为新变量分配的位置上。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//基本数据类型的赋值就是把值复制一下</span>
<span class="hljs-keyword">let</span> n = <span class="hljs-number">2</span>;
<span class="hljs-keyword">let</span> n1 = n;
<span class="hljs-built_in">console</span>.log(n, n1);  <span class="hljs-comment">//2 2</span>

<span class="hljs-comment">//复杂数据类型的赋值，它不光复制了值，还复制了内存中的引用地址</span>
<span class="hljs-keyword">let</span> arr1 = [<span class="hljs-number">10</span>, <span class="hljs-literal">true</span>, <span class="hljs-literal">null</span>];
<span class="hljs-keyword">let</span> arr2 = arr1;
<span class="hljs-keyword">let</span> str1 = arr1[<span class="hljs-number">3</span>];

arr2.push(<span class="hljs-string">'amy'</span>);  <span class="hljs-comment">//arr1与arr2的引用地址是相同,所以不论修改了哪个，两个都会一起改变</span>
<span class="hljs-built_in">console</span>.log(arr2); <span class="hljs-comment">// [10,  true, null, "amy"]</span>
<span class="hljs-built_in">console</span>.log(arr1); <span class="hljs-comment">// [10,  true, null, "amy"]</span>

arr2 = [<span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>];  <span class="hljs-comment">//因为arr2又重新赋值开辟了一块内存，引用地址不一样了</span>
<span class="hljs-built_in">console</span>.log(arr2); <span class="hljs-comment">// [2, 3, 4]</span>
<span class="hljs-built_in">console</span>.log(arr1); <span class="hljs-comment">// [10,  true, null, "amy"]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面代码可以看出，当改变arr2时，arr1中的数据也发生变化。这是因为arr1是数组属于引用类型，当它赋值给arr2时，传的是栈中的地址（相当于新建了一个不同名“指针”），而不是堆内存中对象的值。arr1和arr2都指向同一块堆内存，arr2修改堆内存时，也会影响到arr1。当arr2重新赋值时，又开辟了一块内存，arr2的引用指向这块新的内存，但arr1的指向并没有发生改变，所以这时arr2和arr1又不一样了。</p>
<h2 data-id="heading-1">二、浏览器中js代码运行</h2>
<p>    浏览器想要代码执行就要提供一个供代码执行的环境。我们把这个环境叫做<strong>执行环境栈ECStack</strong>。浏览器还会把内置的一些属性和方法放到一个单独的堆内存中，这个堆内存叫做<strong>全局对象(Global Object)</strong> 简称GO，供以后我们调用。浏览器会让window指向GO，所以在浏览器端window代表的就是全局对象。</p>
<p>    浏览器环境提供后，我们开始让代码执行，代码执行会有一个自己的执行上下文，那什么是执行上下文呢？</p>
<p><strong>执行上下文(Execution Context)简称EC</strong>。变量或者函数的上下文决定了他们有权访问的其它数据以及行为。简单来说EC指的是当前代码的执行环境。</p>
<p>    它可以分为全局执行上下文,我们在此简称为EC(G)、函数环境中的私有上下文和块级上下文。每一个上下文都有一个与之关联的变量对象，这个上下文中定义的所有变量和函数都保存在这个对象中， 这个变量对象称之为<strong>VO(Variable Object)</strong>。函数私有上下文中叫做<strong>AO(Activation Object)活动对象</strong>，但它也是变量对象，它是VO的一个分支。</p>
<p>    形成的全局执行上下文要进入到栈内存中执行，这个过程称为‘进栈’。执行完代码后它有可能会有一个出栈释放步骤，遵循先进后出原则。在全局执行上下文中会创建一些全局变量，这些全局变量还有全局变量存放的值放在变量对象VO(G)中。　</p>
<p>如下所示，代码自上而下执行：</p>
<ul>
<li>先创建一个值。在创建时，如果是基本数据类型值，它可以直接存在栈内存中，如果是引用数据类型值要重新开辟一个堆内存，把内容存入，最后把这个堆内存16进制地址放入栈内存中，供变量关联使用。</li>
<li>然后创建相应的变量</li>
<li>最后把值和变量进行关联（所有的指针赋值都是指针关联指向）</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> a = <span class="hljs-number">12</span>;
<span class="hljs-keyword">let</span> b = a;
b = <span class="hljs-number">13</span>;
<span class="hljs-built_in">console</span>.log(a);
<span class="hljs-keyword">let</span> n = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'davina'</span>
&#125;
<span class="hljs-keyword">let</span> m = n;
m.name = <span class="hljs-string">'lisa'</span>;
<span class="hljs-built_in">console</span>.log(n.name);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> a = &#123;<span class="hljs-attr">n</span>:<span class="hljs-number">12</span>&#125;;
<span class="hljs-keyword">var</span> b = a;
a.x = a = &#123;<span class="hljs-attr">n</span>:<span class="hljs-number">13</span>&#125;;
<span class="hljs-built_in">console</span>.log(a.x);
<span class="hljs-built_in">console</span>.log(a);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c3588fcc4dd4d7881c6e1af6ad99904~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">三、生命周期</h2>
<p>    不管什么程序，内存生命周期分为以下三步：1、分配所需内存  2、使用分配到的内存  3、不需要时将其释放(归放)。</p>
<p>JavaScript环境中分配的内存有如下生命周期：</p>
<ul>
<li>a.  内存分配：声明变量、函数、对象时，系统会自动为他们分配内存</li>
<li>b.  内存使用： 即读写内存。也就是使用变量、函数</li>
<li>c.  内存回收： 由垃圾回收机制自动回收不再使用的内存　</li>
</ul>
<p>JavaScript内存分配：在js中数据类型分为基本数据类型和复杂数据类型，对于基本数据类型它是存在于栈中，它由操作系统自动分配和自动释放，而复杂数据类型它是放在堆中，大小不固定，系统无法进行自动释放，需要js引擎来释放这些内存。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> n = <span class="hljs-number">2</span>;          <span class="hljs-comment">//给数值变量分配内存</span>
<span class="hljs-keyword">var</span> o = &#123;           <span class="hljs-comment">//给对象及其包含的值分配内存</span>
       <span class="hljs-attr">a</span>: <span class="hljs-number">1</span>,
       <span class="hljs-attr">b</span>: <span class="hljs-number">2</span>
   &#125;                  
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params">c</span>) </span>&#123;
     <span class="hljs-keyword">return</span> c;     <span class="hljs-comment">//给函数分配内存</span>
&#125;

<span class="hljs-comment">//有些函数调用结果是分配对象内存</span>
<span class="hljs-keyword">var</span> d = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>() <span class="hljs-comment">//  分配一个Date对象</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">四、垃圾回收机制</h2>
<h3 data-id="heading-4">4.1 概念</h3>
<p>    JavaScript它是通过自动内存管理实现内存分配和闲置资源回收。它的基本思路很简单，确定某个变量不会再使用然后释放它占用的内存，这个过程是周期性的，<strong>垃圾回收（Garbage Collection,简称GC）</strong> 程序每隔一定时间就会自动运行。简单来说，当一个数据使用完后，垃圾回收机制会检测这个数据有没有在其它地方被引用，或者说是在其它地方有没有在使用，如果没有使用那么它就被回收并释放所占用的内存，如果在其它地方依然有使用，那就不会被回收。但某块内存是否还有用或者是还在使用是一个“不可判定”的问题，垃圾回收过程是一个近似但不完美方案。需要注意一点不是所有的语言都有GC，c语言就需要手动管理内存。</p>
<h3 data-id="heading-5">4.2 回收策略</h3>
<h4 data-id="heading-6">4.2.1 标记清除</h4>
<p>    JavaScript最常用的垃圾回收策略是<strong>标记清理 （mark-and-sweep）</strong>。垃圾回收程序运行时，会标记内存中存储的所有变量，然后它会将所有在上下文中的变量，以及被在上下文中的变量引用的变量的标记去掉。随后再给剩下的变量进行另外标记（任何在上下文中的变量都访问不到它们）。最后垃圾回收程序做内存清理，销毁带标记的所有值并收回它们的内存。</p>
<p>    在v8引擎浏览器环境下我们可以简单的理解标记清除就是从根对象(可以简单理解为全局上下文)出发定时扫描内存中的对象，所有roots被检查标记，所有的子对象也会被检查标记，从根开始的所有对象如果可以到达则它不会被当成垃圾会保留，从根部出发无法触及到的对象被标记为不在使用，后面进行回收。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;
     <span class="hljs-keyword">var</span> a = <span class="hljs-number">10</span>; <span class="hljs-comment">//进行标记</span>
     a++;
     a = <span class="hljs-literal">null</span>;   <span class="hljs-comment">//标记清除</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e82033f5c7ad4904b87cd6d6e93d075c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7">4.2.2 引用计数</h4>
<p>    对每个值都记录它引用的次数。当声明一个变量并给它赋一个引用值这个值的引用次数为1，如果同一个值又赋值给另外一个变量，那么引用就加1。如果保存对该值引用的变量被其它值覆盖了，那引用数减1。当一个值的引用数为0时，就说明没办法再访问到这个值了，因此可以安全地收回其内存。垃圾回收程序下次运行的时候就会释放引用数为0的值的内存。</p>
<p>    低版本IE浏览器就是用引用计数策略来进行垃圾回收。在真实的项目中，某些情况会导致计数规则出现一些问题，造成很多内存不能被释放掉，产生“内存泄漏”。</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">//引用计数</span>
<span class="hljs-keyword">var</span> person = &#123;
    <span class="hljs-attr">age</span>: <span class="hljs-number">18</span>,        <span class="hljs-comment">//标记1次</span>
    <span class="hljs-attr">name</span>: <span class="hljs-string">'amy'</span>
    &#125;;
person.age = <span class="hljs-literal">null</span>; <span class="hljs-comment">//虽然age设置了null,但是person对象还有指向name的引用，所以name不会被回收</span>

 <span class="hljs-keyword">var</span> p = person;
 person = <span class="hljs-number">2</span>;    <span class="hljs-comment">//原来的person对象被赋值为2，但因为有新引用p指向person对象，所以它不会被回收</span>

p = <span class="hljs-literal">null</span>       <span class="hljs-comment">//person对象已经没有引用了，所以会被回收</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>引用计数有一个很大的问题那就是循环引用，所谓的循环引用就是两个对象相互引用，即对象A有一个指针指向对象B，而对象B也引用了对象A。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;
     <span class="hljs-keyword">var</span> a = &#123;&#125;;  
     <span class="hljs-keyword">var</span> b = &#123;&#125;;
     a.age = b;
     b.age = a;
　　<span class="hljs-comment">// 由于a和b互相引用，计数永远不可能为0</span>
   &#125;
 fn();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>    总之，JavaScript是使用垃圾回收的编程语言，我们不需要担心内存的分配与回收，但了解其机制可以更好进行性能优化。一般来说主流浏览器都是使用标记清除即给当前不使用的值加上标记，一定时间后来清理。但也有另外一种引用计数策略，它在老版本IE中使用，也需要简单了解，主要记录值被引用了多少次，当引用为0时就可以进行清理。</p>
<h2 data-id="heading-8">五、内存管理</h2>
<p>    程序运行是需要用到内存的，在日常的工作中我们需要将内存占用量保持在一个比较小的值让页面性能更加友好也需要及时释放内存保证系统正常运行。</p>
<h3 data-id="heading-9">5.1 优化性能</h3>
<p>    我们可以通过<strong>解除引用</strong>来保证代码在执行时只保存必要数据，不再需要的数据将其设置为null，从而释放它的引用。它适用于全局变量和全局对象（局部变量在超出作用域后会被自动解除）。或者<strong>声明时使用let或者const</strong>尽量少用var，因为const或let它们都是以块作为作用域，相对于var来说，这两个关键字会让垃圾回收程序更早介入,这样也可以尽早回收内存。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params">name</span>)</span>&#123;
    <span class="hljs-keyword">let</span> obj = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Object</span>();
    obj.name = name;
    <span class="hljs-keyword">return</span> obj;
&#125;
<span class="hljs-keyword">let</span> person = fn(<span class="hljs-string">'amy'</span>);

person = <span class="hljs-literal">null</span>; <span class="hljs-comment">//解除person对值的引用</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">5.2 内存泄漏</h3>
<p>    本质上来说，内存泄漏是由于疏忽或者是错误造成程序未能释放那些已经不在使用的内存，造成内存浪费。在内存有限的情况下，内存泄漏是一个大问题。</p>
<h4 data-id="heading-11">5.2.1 出现内存泄漏的情况</h4>
<ul>
<li><strong>意外的全局变量</strong></li>
</ul>
<p>意外声明的全局变量是最常见也是最容易修复的内存泄漏问题。如下所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>)</span>&#123;
    name = <span class="hljs-string">'amy'</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时name是window的属性，只要window本身不被清理那么name就不会消失。我们可以在变量声明前加上const,let或者var关键字，这样变量会在函数执行完后离开使用域。</p>
<ul>
<li><strong>闭包</strong></li>
</ul>
<p>使用闭包很容易在不知不觉中就造成了内存泄漏。如下所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">let</span> box = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'xxx'</span>);
    box.onclick=<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-comment">//do something</span>
        <span class="hljs-keyword">return</span> box;
    &#125;
    <span class="hljs-comment">// box = null;//解除引用</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>闭包可以保护函数内部的变量，使其不被释放。在上面的例子中，定义fn函数时，因为它里面还有定义了其它函数即box点击事件，并且点击事件还引用了外面的变量，形成了闭包。这样也导致box很难被回收。如果box不是一个小字符串内容很大，这时就会导致内存占用这种大问题，所以我们要及时解除引用或者是将事件处理函数定义在外面。</p>
<ul>
<li><strong>计时器或者回调函数</strong></li>
</ul>
<p>定时器也会导致内存的泄漏。如下所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> name = <span class="hljs-string">'amy'</span>;
<span class="hljs-built_in">setInterval</span>(<span class="hljs-function">()=></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'*****'</span> + name +<span class="hljs-string">'*******'</span>)
&#125;,<span class="hljs-number">1000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>只要定时器一直运行。回调函数中引用的name就会一直占用内存。所以我们要习惯在用了定时器后及时清除定时器。</p>
<h4 data-id="heading-12">5.2.2 识别方法</h4>
<p>我们可以在chrome中的performance中查看：</p>
<ul>
<li>F12打开开发者工具performance</li>
<li>勾选screenshots和memory</li>
<li>开始录制</li>
<li>停止录制</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d894a503d984840815ceeadb7b1ef9b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
图中heap部分可以看到内存在周期性回落也可以看到垃圾回收的周期，如果垃圾回收的最低值在上涨，那就要内存泄漏问题。</p>
<p>避免内存泄漏的方法，主要是将不需要的引用及时归还：</p>
<ul>
<li>减少不必要的全局变量，尽量用const或者let声明，及时清除无用数据</li>
<li>定时器使用后要及时清除定时器</li>
<li>避免创建过多对象</li>
<li>对闭包这种机制使用时要及时清除引用</li>
</ul></div>  
</div>
            