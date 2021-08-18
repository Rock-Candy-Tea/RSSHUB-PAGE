
---
title: 'Typescript 类型的本质是什么'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1873'
author: 掘金
comments: false
date: Tue, 17 Aug 2021 11:07:43 GMT
thumbnail: 'https://picsum.photos/400/300?random=1873'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">类型</h2>
<p><code>类型</code>指的是变量的类型，而变量是一块内存空间，不同类型的变量会占用不同的字节数，而且可以做的操作也不同。number、boolean、string 等类型的变量会占用不同的内存大小。</p>
<p>类型分为基础类型和引用类型，基础类型分配在栈上，而引用类型分配在堆上，之所以有引用类型是因为这种类型是复合出来的，比如对象，它可能有任意多个属性，这种就放在可动态分配内存的堆上，然后在栈上记录下该地址，这就是引用类型。</p>
<p>类型是运行时的变量的内存空间大小和可以做的操作的标识，但是代码中不一定包含，根据代码中是否有类型的标识，语言分为了静态类型语言和动态类型语言。</p>
<h2 data-id="heading-1">静态类型、动态类型、类型安全</h2>
<p><code>动态类型</code>语言的代码中没有记录变量的类型，对什么变量赋什么值做什么操作都是可以的，这样写代码时不用考虑类型的问题，比较简单，但是也有隐患，就是运行时变量赋值时发现类型不一致，或者调用了没有的方法等，这是动态类型语言的缺点。</p>
<p><code>静态类型</code>语言则是把类型的标识保存在了代码里，也就是有静态类型系统。声明的变量的类型在运行时会分配相应的内存空间，就会赋相同类型的值，就会调用该类型有的方法，如果不是，在编译时就能检查出来。</p>
<p>这种同样类型的变量只赋值同类型的值，只做该类型允许的操作就叫做<code>类型安全</code>，显然，动态类型是类型不安全的，会在运行时有各种类型相关问题，而静态类型则通过类型系统在编译期间就把类型不安全的操作检查了出来进行报错，所以是类型安全的。</p>
<p>typescript 就是给动态类型的 javascript 添加了一套静态类型系统，是 javascript 的超集。</p>
<h2 data-id="heading-2">静态类型系统的 3 个层次</h2>
<p>其实静态类型系统分为 3 个层次：</p>
<h3 data-id="heading-3">纯静态的类型系统</h3>
<p>第一种就是纯静态的类型系统，变量的类型都是定义时声明的，但有一个问题就是遇到参数的类型可能是多种类型的时候会比较麻烦。一些古老的语言是这种。</p>
<p>比如：</p>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">add</span><span class="hljs-params">(<span class="hljs-keyword">int</span> a, <span class="hljs-keyword">int</span> b)</span> </span>&#123;
    <span class="hljs-keyword">return</span> a + b;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-c copyable" lang="c"><span class="hljs-function"><span class="hljs-keyword">double</span> <span class="hljs-title">add</span><span class="hljs-params">(<span class="hljs-keyword">double</span> a, <span class="hljs-keyword">double</span> b)</span> </span>&#123;
    <span class="hljs-keyword">return</span> a + b;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">带泛型的静态类型系统</h3>
<p>第二种是带泛型的静态类型系统，泛型也叫类型参数，具体的类型可以通过泛型参数来动态确定，多了一定的灵活性。java 是这种。</p>
<p>比如：</p>
<pre><code class="hljs language-java copyable" lang="java">T add<T>(T a, T b) &#123;
    <span class="hljs-keyword">return</span> a + b;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">支持高级类型的静态类型系统</h3>
<p>第三种是支持高级类型的静态类型系统，高级类型就是生成类型的类型，它除了可以传泛型参数外还可以支持分支、递归、取属性等操作，可以通过复杂的逻辑来生成类型。 typescript 是这种。</p>
<p>比如下面的高级类型：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> RepeatN<Item, N <span class="hljs-keyword">extends</span> <span class="hljs-built_in">number</span>, Tuple <span class="hljs-keyword">extends</span> <span class="hljs-built_in">any</span>[] = []> = Tuple[<span class="hljs-string">'length'</span>] <span class="hljs-keyword">extends</span> N ? Tuple : RepeatN<Item, N, [...Tuple, Item]>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>它的作用是当传入泛型参数时，返回该参数重复 n 次的元组：</p>
<pre><code class="copyable">type res = RepeactN<'a', 3>;
// res 为 ['a', 'a', 'a']
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>高级类型</code>支持类型编程，甚至是图灵完备的，<code>图灵完备</code>的意思就是说提供的语言特性可以描述所有可计算的逻辑。也就是所有用 javascript 写的逻辑在 typescript 中用类型都可以实现，只不过具体语法有不同。</p>
<h4 data-id="heading-6">高级类型示例</h4>
<p>就拿上面这个把参数重复 n 次的代码来说，如果用 javascript 我们会这样写：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">repeactN</span>(<span class="hljs-params">item, n</span>) </span>&#123;
    <span class="hljs-keyword">const</span> res = [];
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i< n; i++) &#123;
        res[i] = item;
    &#125;
    <span class="hljs-keyword">return</span> res;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用 typescript 的类型系统怎么写呢？</p>
<p>图灵完备意味着两者都能实现同样的逻辑，只不过实现方式不同。我们只要把逻辑想清楚，然后用类型支持的语法实现即可。</p>
<p>首先，函数参数在 ts 类型里就是泛型参数，变量在 ts 类型里也用泛型参数来存储，循环在 ts 类型利用递归来实现，所以就是这样的：</p>
<p>首先定义类型，Item 是重复的目标， n 是个数，然后第三个参数 Tuple 用来存储结果</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> RepeatN<Item, N <span class="hljs-keyword">extends</span> <span class="hljs-built_in">number</span>, Tuple <span class="hljs-keyword">extends</span> <span class="hljs-built_in">any</span>[] = []>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后具体的实现就是要不断的往 Tuple 里放 Item，递归构造</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">RepeatN<Item, N, [...Tuple, Item]>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>直到 Tuple 的 length 到了 N</p>
<pre><code class="copyable">Tuple['length'] extends N ? Tuple : RepeatN<Item, N, [...Tuple, Item]>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以，完整的类型就是这样的：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">type</span> RepeatN<Item, N <span class="hljs-keyword">extends</span> <span class="hljs-built_in">number</span>, Tuple <span class="hljs-keyword">extends</span> <span class="hljs-built_in">any</span>[] = []> = Tuple[<span class="hljs-string">'length'</span>] <span class="hljs-keyword">extends</span> N ? Tuple : RepeatN<Item, N, [...Tuple, Item]>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过这个高级类型我们可以感受到，typescript 的静态类型系统就是第三种，可以支持类型编程，可以实现各种复杂逻辑，最终生成目标类型。</p>
<h2 data-id="heading-7">tyepscript 类型系统复杂度的原因</h2>
<p>为什么 tyepscript 要设计这么复杂的类型系统呢？</p>
<p>静态类型的目的就是把运行时的行为在编译时就检查出来，那么就要在编译期间就要确定最终类型，而 javascript 逻辑又很灵活，所以想还没运行就确定类型就需要各种类型的推导来生成最终类型，所以也就设计出了带高级类型的静态类型系统。</p>
<p>tyepscript 静态类型系统的复杂度主要是因为 javascript 比较灵活导致的，是不可避免的。</p>
<h2 data-id="heading-8">总结</h2>
<p><code>类型</code>本质上是运行时变量的内存大小和可对它进行的操作，变量只赋值同类型的值就是<code>类型安全</code>，<code>动态类型</code>在源码中没有类型信息，没法保证类型安全，而<code>静态类型</code>则是在源码中有类型信息，可以在编译期间检查出类型的错误，保证类型安全。</p>
<p>javascript 就是动态类型语言，虽然写代码比较简单，但是运行时很容易出类型安全问题，typescript 就是解决了 javascript 没有静态类型系统的问题而做的扩展。ts 的类型系统是支持<code>泛型</code>、支持<code>高级类型</code>的静态类型系统，而且类型的语法是<code>图灵完备</code>的，也就是各种逻辑都可以表达，只不过和 js 中的语法会有不同。这也是 ts 给 js 扩展的这套类型系统中最复杂的部分，被大家戏称为类型体操，但是这种复杂度是为了让 javascript 变得类型安全不可避免的。</p>
<p>其实高级类型的所谓类型体操也没有那么难，只要想清楚要表达的逻辑，然后一步步用相应的语法实现即可，只不过语法会有一些别扭，比如变量用泛型参数实现、循环用递归实现等，但只要理清逻辑，实现起来还是不难的。</p></div>  
</div>
            