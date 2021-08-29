
---
title: 'Android 架构师之路5 设计模式之单例模式'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f65c62d3408b4b859dfc46ed2626de30~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 28 Aug 2021 04:54:27 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f65c62d3408b4b859dfc46ed2626de30~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">前言</h4>
<blockquote>
<p>Java中单例(Singleton)模式是一种广泛使用的设计模式。单例模式的主要作用是保证在Java程序中，某个类只有一个实例存在。一些管理器和控制器常被设计成单例模式。<br>
单例模式有很多好处，它能够避免实例对象的重复创建，不仅可以减少每次创建对象的时间开销，还可以节约内存空间；能够避免由于操作多个实例导致的逻辑错误。如果一个对象有可能贯穿整个应用程序，而且起到了全局统一管理控制的作用，那么单例模式也许是一个值得考虑的选择。</p>
</blockquote>
<h4 data-id="heading-1">1、单例模式UML类图</h4>
<div align="center">
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f65c62d3408b4b859dfc46ed2626de30~tplv-k3u1fbpfcp-watermark.image" alt="单例模式UML类图" loading="lazy" referrerpolicy="no-referrer">
</div>
<h4 data-id="heading-2">2、单例模式的八种写法</h4>
<h5 data-id="heading-3">2.1饿汉模式</h5>
<p>顾名思义，饿汉法就是在第一次引用该类的时候就创建对象实例，而不管实际是否需要创建。代码如下：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Singleton</span> </span>&#123;   
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> Singleton = <span class="hljs-keyword">new</span> Singleton();
    <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-title">Singleton</span><span class="hljs-params">()</span> </span>&#123;&#125;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-title">getSignleton</span><span class="hljs-params">()</span></span>&#123;
        <span class="hljs-keyword">return</span> singleton;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样做的好处是编写简单，但是无法做到延迟创建对象。但是我们很多时候都希望对象可以尽可能地延迟加载，从而减小负载，所以就需要下面的懒汉法。</p>
<h5 data-id="heading-4">2.2 饿汉模式变种</h5>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Singleton</span> </span>&#123;  
    <span class="hljs-keyword">private</span> Singleton instance = <span class="hljs-keyword">null</span>;  
     <span class="hljs-keyword">static</span> &#123;  
    instance = <span class="hljs-keyword">new</span> Singleton();  
    &#125;  
    <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-title">Singleton</span> <span class="hljs-params">()</span></span>&#123;&#125;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> Singleton <span class="hljs-title">getInstance</span><span class="hljs-params">()</span> </span>&#123;  
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">this</span>.instance;  
    &#125;  
 &#125;  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>表面上看起来差别挺大，其实上面那种差不多，都是在类初始化即实例化instance。.</p>
<h5 data-id="heading-5">2.3不加锁懒汉模式(线程不安全)</h5>
<p>懒汉模式中单例是在需要的时候才去创建的，如果单例已经创建，再次调用获取接口将不会重新创建新的对象，而是直接返回之前创建的对象。如果某个单例使用的次数少，并且创建单例消耗的资源较多，那么就需要实现单例的按需创建，这个时候使用懒汉模式就是一个不错的选择。但是这里的懒汉模式并没有考虑线程安全问题，在多个线程可能会并发调用它的getInstance()方法，就有很大可能导致重复创建对象。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Singleton</span> </span>&#123;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> Singleton singleton = <span class="hljs-keyword">null</span>;
    <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-title">Singleton</span><span class="hljs-params">()</span></span>&#123;&#125;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> Singleton <span class="hljs-title">getSingleton</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">if</span>(singleton == <span class="hljs-keyword">null</span>) singleton = <span class="hljs-keyword">new</span> Singleton();
        <span class="hljs-keyword">return</span> singleton;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-6">2.4加锁懒汉模式（线程安全，但是耗时）</h5>
<p>这种写法考虑了线程安全，将对singleton的null判断以及new的部分使用synchronized进行加锁。同时，对singleton对象使用volatile关键字进行限制，保证其对所有线程的可见性，并且禁止对其进行指令重排序优化。如此即可从语义上保证这种单例模式写法是线程安全的。但是每次通过getInstance方法得到singleton实例的时候都有一个试图去获取同步锁的过程。而众所周知，加锁是很耗时的，对高并发操作很不友好。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Singleton</span> </span>&#123;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">volatile</span> Singleton singleton = <span class="hljs-keyword">null</span>;
 
    <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-title">Singleton</span><span class="hljs-params">()</span></span>&#123;&#125;
 
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> Singleton <span class="hljs-title">getSingleton</span><span class="hljs-params">()</span></span>&#123;
        <span class="hljs-keyword">synchronized</span> (Singleton.class)&#123;
            <span class="hljs-keyword">if</span>(singleton == <span class="hljs-keyword">null</span>)&#123;
                singleton = <span class="hljs-keyword">new</span> Singleton();
            &#125;
        &#125;
        <span class="hljs-keyword">return</span> singleton;
    &#125;    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-7">2.5双重校验锁( 兼顾线程安全和效率的写法)</h5>
<p>虽然上面这种写法是可以正确运行的，但是其效率低下，还是无法实际应用。因为每次调用getSingleton()方法，都必须在synchronized这里进行排队，而真正遇到需要new的情况是非常少的。所以，就诞生了第三种写法：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Singleton</span> </span>&#123;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">volatile</span> Singleton singleton = <span class="hljs-keyword">null</span>;
 
    <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-title">Singleton</span><span class="hljs-params">()</span></span>&#123;&#125;
 
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> Singleton <span class="hljs-title">getSingleton</span><span class="hljs-params">()</span></span>&#123;
        <span class="hljs-keyword">if</span>(singleton == <span class="hljs-keyword">null</span>)&#123;
            <span class="hljs-keyword">synchronized</span> (Singleton.class)&#123;
                <span class="hljs-keyword">if</span>(singleton == <span class="hljs-keyword">null</span>)&#123;
                    singleton = <span class="hljs-keyword">new</span> Singleton();
                &#125;
            &#125;
        &#125;
        <span class="hljs-keyword">return</span> singleton;
    &#125;    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种写法被称为“双重检查锁”，顾名思义，就是在getSingleton()方法中，进行两次null检查。看似多此一举，但实际上却极大提升了并发度，进而提升了性能。为什么可以提高并发度呢？就像上文说的，在单例中new的情况非常少，绝大多数都是可以并行的读操作。因此在加锁前多进行一次null检查就可以减少绝大多数的加锁操作，执行效率提高的目的也就达到了。</p>
<h5 data-id="heading-8">该种写法存在Java低版本中的问题</h5>
<div align="center">
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d38e9b60b1644f309f3458de5f0940da~tplv-k3u1fbpfcp-watermark.image" alt="内存模型" loading="lazy" referrerpolicy="no-referrer">
</div>
<p>那么，这种写法是不是绝对安全呢？前面说了，从语义角度来看，并没有什么问题。但是其实还是有坑。说这个坑之前我们要先来看看volatile这个关键字。其实这个关键字有两层语义。第一层语义相信大家都比较熟悉，就是可见性。可见性指的是在一个线程中对该变量的修改会马上由工作内存（Work Memory）写回主内存（Main Memory），所以会马上反应在其它线程的读取操作中。顺便一提，工作内存和主内存可以近似理解为实际电脑中的高速缓存和主存，工作内存是线程独享的，主存是线程共享的。volatile的第二层语义是禁止指令重排序优化。大家知道我们写的代码（尤其是多线程代码），由于编译器优化，在实际执行的时候可能与我们编写的顺序不同。编译器只保证程序执行结果与源代码相同，却不保证实际指令的顺序与源代码相同。这在单线程看起来没什么问题，然而一旦引入多线程，这种乱序就可能导致严重问题。volatile关键字就可以从语义上解决这个问题。</p>
<p>例如，考虑下面的事件序列：</p>
<ol>
<li>线程<em>A</em>发现变量没有被初始化, 然后它获取锁并开始变量的初始化。</li>
<li>由于某些编程语言的语义，编译器生成的代码允许在线程<em>A</em>执行完变量的初始化之前，更新变量并将其指向部分初始化的对象。</li>
<li>线程<em>B</em>发现共享变量已经被初始化，并返回变量。由于线程<em>B</em>确信变量已被初始化，它没有获取锁。如果在<em>A</em>完成初始化之前共享变量对<em>B</em>可见（这是由于<em>A</em>没有完成初始化或者因为一些初始化的值还没有穿过<em>B</em>使用的内存(<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzh.wikipedia.org%2Fwiki%2F%25E7%25BC%2593%25E5%25AD%2598%25E4%25B8%2580%25E8%2587%25B4%25E6%2580%25A7" target="_blank" rel="nofollow noopener noreferrer" title="https://zh.wikipedia.org/wiki/%E7%BC%93%E5%AD%98%E4%B8%80%E8%87%B4%E6%80%A7" ref="nofollow noopener noreferrer">缓存一致性</a>)），程序很可能会崩溃。</li>
</ol>
<pre><code class="hljs language-xml copyable" lang="xml">Symantec JIT 编译 singletons[i].reference = new Singleton(); 这段代码时，如果不加volatile关键词，会生成如下字节码：

0206106A   mov         eax,0F97E78h
0206106F   call        01F6B210                  ; allocate space for
                                                 ; Singleton, return result in eax
02061074   mov         dword ptr [ebp],eax       ; EBP is &singletons[i].reference 
                                                ; store the unconstructed object here.
02061077   mov         ecx,dword ptr [eax]       ; dereference the handle to
                                                 ; get the raw pointer
02061079   mov         dword ptr [ecx],100h      ; Next 4 lines are
0206107F   mov         dword ptr [ecx+4],200h    ; Singleton's inlined constructor
02061086   mov         dword ptr [ecx+8],400h
0206108D   mov         dword ptr [ecx+0Ch],0F84030h
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-9">可以看到，在执行<code>Singleton</code>的构造函数之前，<code>Singleton</code>的新实例就被赋值给了<code>singletons[i].reference</code>，这在Java内存模型中是完全合法的。</h6>
<p>注意，前面反复提到“从语义上讲是没有问题的”，但是很不幸，禁止指令重排优化这条语义直到jdk1.5以后才能正确工作。此前的JDK中即使将变量声明为volatile也无法完全避免重排序所导致的问题。所以，在jdk1.5版本前，双重检查锁形式的单例模式是无法保证线程安全的。</p>
<h5 data-id="heading-10">2.6 静态内部类法(推荐)</h5>
<p>那么，有没有一种延时加载，并且能保证线程安全的简单写法呢？我们可以把Singleton实例放到一个静态内部类中，这样就避免了静态实例在Singleton类加载的时候就创建对象，并且由于静态内部类只会被加载一次，所以这种写法也是线程安全的：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Singleton</span> </span>&#123;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Holder</span> </span>&#123;
        <span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> Singleton singleton = <span class="hljs-keyword">new</span> Singleton();
    &#125;
 
    <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-title">Singleton</span><span class="hljs-params">()</span></span>&#123;&#125;
 
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> Singleton <span class="hljs-title">getSingleton</span><span class="hljs-params">()</span></span>&#123;
        <span class="hljs-keyword">return</span> Holder.singleton;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是，上面提到的所有实现方式都有两个共同的缺点：</p>
<ul>
<li>都需要额外的工作(Serializable、transient、readResolve())来实现序列化，否则每次反序列化一个序列化的对象实例时都会创建一个新的实例。</li>
<li>可能会有人使用反射强行调用我们的私有构造器（如果要避免这种情况，可以修改构造器，让它在创建第二个实例的时候抛异常）。</li>
</ul>
<h5 data-id="heading-11">2.7 枚举写法</h5>
<p>当然，还有一种更加优雅的方法来实现单例模式，那就是枚举写法：</p>
<pre><code class="hljs language-java copyable" lang="java">    <span class="hljs-keyword">public</span>  <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Resource</span></span>&#123;
    &#125;

    <span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">enum</span> <span class="hljs-title">SomeThing</span> </span>&#123;
        INSTANCE;
        <span class="hljs-keyword">private</span> Resource instance;
        SomeThing() &#123;
            instance = <span class="hljs-keyword">new</span> Resource();
        &#125;
        <span class="hljs-function"><span class="hljs-keyword">public</span> Resource <span class="hljs-title">getInstance</span><span class="hljs-params">()</span> </span>&#123;
            <span class="hljs-keyword">return</span> instance;
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>调用</p>
<pre><code class="hljs language-java copyable" lang="java">    Resource resource = SomeThing.INSTANCE.getInstance();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用枚举除了线程安全和防止反射强行调用构造器之外，还提供了自动序列化机制，防止反序列化的时候创建新的对象。因此，<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.amazon.com%2Fgp%2Fproduct%2FB000WJOUPA%2Fref%3Das_li_qf_sp_asin_il_tl%3Fie%3DUTF8%26camp%3D1789%26creative%3D9325%26creativeASIN%3DB000WJOUPA%26linkCode%3Das2%26tag%3Djob0ae-20" target="_blank" rel="nofollow noopener noreferrer" title="http://www.amazon.com/gp/product/B000WJOUPA/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B000WJOUPA&linkCode=as2&tag=job0ae-20" ref="nofollow noopener noreferrer">Effective Java</a>推荐尽可能地使用枚举来实现单例。</p>
<h5 data-id="heading-12">2.8 容器实现单例模式</h5>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">import</span> java.util.HashMap;
<span class="hljs-keyword">import</span> java.util.Map;

<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Singleton</span> </span>&#123;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> Map<String, Object> objMap = <span class="hljs-keyword">new</span> HashMap<String, Object>();

    <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-title">Singleton</span><span class="hljs-params">()</span> </span>&#123;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">registerService</span><span class="hljs-params">(String key, Object instance)</span> </span>&#123;
        <span class="hljs-keyword">if</span> (!objMap.containsKey(key)) &#123;
            objMap.put(key, instance);
        &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> Object <span class="hljs-title">getService</span><span class="hljs-params">(String key)</span> </span>&#123;
        <span class="hljs-keyword">return</span> objMap.get(key);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种实现方式使得我们可以管理多种类型的单例，并且在使用时可以通过统一接口进行获取操作，降低用户使用成本，也对用户隐藏了具体实现，降低耦合度。</p>
<h4 data-id="heading-13">3 、单例模式在Android源码中应用</h4>
<blockquote>
<p>第三方 ImageLoader（通过源码分析，得到单例模式中双重检测方案）<br>
LayoutInflater 单例模式通过容器进行管理<br>
LayoutInflater 源码分析 WindowManager、ActivityManager、PowerManager都是容器管理</p>
</blockquote>
<h3 data-id="heading-14">总结</h3>
<p>代码没有一劳永逸的写法，只有在特定条件下最合适的写法。在不同的平台、不同的开发环境（尤其是jdk版本）下，自然有不同的最优解（或者说较优解）。<br>
比如枚举，虽然Effective Java中推荐使用，但是在Android平台上却是不被推荐的。在<a href="https://link.juejin.cn/?target=http%3A%2F%2Fdeveloper.android.com%2Ftraining%2Farticles%2Fmemory.html" target="_blank" rel="nofollow noopener noreferrer" title="http://developer.android.com/training/articles/memory.html" ref="nofollow noopener noreferrer">这篇Android Training</a>中明确指出：</p>
<blockquote>
<p>Enums often require more than twice as much memory as static constants. You should strictly avoid using enums on Android.</p>
</blockquote>
<p>再比如双重检查锁法，不能在jdk1.5之前使用，而在<code>Android</code>平台上使用就比较放心了（一般Android都是jdk1.6以上了，不仅修正了volatile的语义问题，还加入了不少锁优化，使得多线程同步的开销降低不少）。</p>
<p>最后，不管采取何种方案，请时刻牢记单例的三大要点：</p>
<ul>
<li>线程安全</li>
<li>延迟加载</li>
<li>序列化与反序列化安全</li>
</ul></div>  
</div>
            