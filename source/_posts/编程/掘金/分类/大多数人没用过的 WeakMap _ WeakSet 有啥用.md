
---
title: '大多数人没用过的 WeakMap _ WeakSet 有啥用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3300'
author: 掘金
comments: false
date: Wed, 07 Apr 2021 21:44:11 GMT
thumbnail: 'https://picsum.photos/400/300?random=3300'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>下一篇，打算聊聊绝大多数人都没在代码里写过的 WeakMap WeakSet</p>
</blockquote>
<p>上一篇文章 <a href="https://juejin.cn/post/6947881997033275406" target="_blank">《JavaScript 面试题外的【this】》</a>中的承诺如期而至。</p>
<hr>
<p>在聊 <code>WeakSet</code> 之前，我们还是先温习一下 <code>Set</code> 这个相对简单的数据结构。</p>
<blockquote>
<p>Set对象是值的集合，你可以按照插入的顺序迭代它的元素。 Set中的元素只会出现一次，即 Set 中的元素是唯一的。</p>
</blockquote>
<p>它提供了如下的接口：</p>
<ul>
<li><code>Set.prototype.add</code>      在集合中增加一个元素</li>
<li><code>Set.prototype.delete</code> 在集合中删除一个元素</li>
<li><code>Set.prototype.has</code>  判断一个元素是否存在于集合中</li>
<li><code>Set.prototype.clear</code>  清空集合</li>
<li><code>Set.prototype.entries/forEach/values</code> 以各种不同的方式遍历这个集合</li>
</ul>
<p>再拎出来 WeakSet 对比一下</p>
<blockquote>
<p>WeakSet 对象允许你将弱保持对象存储在一个集合中。</p>
</blockquote>
<p>首先，WeakSet 里面的引用是弱引用。对于这点，mdn 内也有详尽的描述。</p>
<blockquote>
<p>WeakSet持弱引用：集合中对象的引用为弱引用。 如果没有其他的对WeakSet中对象的引用，那么这些对象会被当成垃圾回收掉。 这也意味着WeakSet中没有存储当前对象的列表。 正因为这样，WeakSet 是不可枚举的。</p>
</blockquote>
<p>也正由于不可枚举，所以在 <code>Set</code> 中涉及到遍历的方法在 <code>WeakSet</code> 均不存在。于是， WeakSet 的接口也就设下这么几个</p>
<ul>
<li><code>WeakSet.prototype.add</code>      在集合中增加一个元素</li>
<li><code>WeakSet.prototype.delete</code> 在集合中删除一个元素</li>
<li><code>WeakSet.prototype.has</code>  判断一个元素是否存在于集合中</li>
</ul>
<p><code>add</code> 和 <code>delete</code> 都是对 <code>WeakSet</code> 内部进行修改的接口，真正有用的接口实质上就只有判断元素是否存在于集合中 —— <code>has</code> 这一个。</p>
<p>这就让 <code>WeakSet</code> 显得很鸡肋。 其实我们用集合类型的数据结构，其实最多的操作还是用来遍历，无论是 <code>Array</code> 还是 <code>Set</code>。</p>
<p>我们用 <code>Set</code> 而不用 <code>Array</code>，是因为场景需要一个<strong>无序且值唯一</strong>的<strong>集合</strong>。而我们本以为 <code>WeakSet</code> 可以用在解决需要一个<strong>无序、值为一且弱引用</strong>的<strong>集合</strong>的场景。然而结果却大相径庭，这货根本无法遍历，怎么能当作<strong>集合</strong>来用呢。</p>
<hr>
<p>如果有心翻 mdn 的话，其实能够看到一个小插曲 —— 一个被废弃的接口 <code>WeakSet.prototype.clear</code></p>
<p>很明显类似于 <code>Set.prototype.clear</code> 这是一个用来清空的接口，没什么特别的。被废弃了也没啥影响，因为所有你可以用到 <code>clear</code> 的情况，都可以通过 <code>new WeakSet()</code> 以创建一个新的实例的方式进行代替。</p>
<p>但是有意思的是这句</p>
<blockquote>
<p>没有规范或草案。该方法原本计划包括在 ECMAScript 6，但是在草案 revision 28 (October 14, 2014) 被抛弃了。浏览器原先的实现不久后也被移除了，它从来不是标准的一分子。</p>
</blockquote>
<p>没错，这个接口原本包含在 ES6 中，并且也已经被实现了，却还是被遗弃了。至于原因，其实上面对弱引用的描述已经初现端倪了。</p>
<blockquote>
<p>这也意味着WeakSet中没有存储当前对象的列表。</p>
</blockquote>
<p>连存储当前对象的列表都没有当然也就没有办法“清空”了。同时也印证了我们之前的判断 —— <strong>这个东西被设计出来根本不是如同 Set 一样，它并不是被当作一个特殊场景下的集合来用的</strong>。</p>
<hr>
<p>在继续讨论 WeakSet 到底是用来做啥之前，再讨论一个挺有意思的事情。</p>
<p>有些人看到弱引用，就想到垃圾回收，进而开始研究起 js 引擎来，想到要实现这么厉害的功能，必定是改了很多底层的架构啥的……</p>
<p>然而有趣的是，在 WeakSet 刚出的时候就已经有 polyfill 能够模拟这个功能了。</p>
<p>写几行代码表示一下原理……</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">WeakSet</span> </span>&#123;
    #id = <span class="hljs-string">''</span>

    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.#id = <span class="hljs-built_in">Symbol</span>()
    &#125;

    <span class="hljs-function"><span class="hljs-title">add</span>(<span class="hljs-params">obj</span>)</span> &#123;
        <span class="hljs-built_in">Object</span>.defineProperty(obj, <span class="hljs-built_in">this</span>.#id, &#123;
            <span class="hljs-attr">enumable</span>: <span class="hljs-literal">false</span>,
            <span class="hljs-attr">configurable</span>: <span class="hljs-literal">true</span>,
        &#125;)
    &#125;

    <span class="hljs-function"><span class="hljs-title">delete</span>(<span class="hljs-params">obj</span>)</span> &#123;
        <span class="hljs-keyword">if</span> (obj.hasOwnProperty(<span class="hljs-built_in">this</span>.#id)) &#123;
            <span class="hljs-keyword">delete</span> obj[<span class="hljs-built_in">this</span>.#id]
        &#125;
    &#125;

    <span class="hljs-function"><span class="hljs-title">has</span>(<span class="hljs-params">obj</span>)</span> &#123;
        <span class="hljs-keyword">return</span> obj.hasOwnProperty(<span class="hljs-built_in">this</span>.#id)
    &#125;
    
    <span class="hljs-function"><span class="hljs-title">clear</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">this</span>.#id = <span class="hljs-built_in">Symbol</span>()
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>简而言之，就直接在对象上创建一个无法枚举的属性表示这个元素是否存在于当前 <code>WeakSet</code> 内。</p>
<p>如果是 <code>WeakMap</code> 的话，就直接把对应的值写入到这个属性内就可以了。</p>
<hr>
<p>这个 polyfill 让事情变得更有意思了。它意味着 <code>WeakMap</code> <code>WeakSet</code> 拥有一个等价的写法。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 很简单的一个类，拥有一个 val 的私有属性，和对应的 set/get</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Foo</span> </span>&#123;
    #val = <span class="hljs-literal">null</span>
    
    <span class="hljs-function"><span class="hljs-title">setVal</span>(<span class="hljs-params">v</span>)</span> &#123; <span class="hljs-built_in">this</span>.#val = v &#125;
    <span class="hljs-function"><span class="hljs-title">getVal</span>(<span class="hljs-params">v</span>)</span> &#123; <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.#val &#125;
&#125;

<span class="hljs-comment">// 通过 WeakMap,讲 val 从对象内部拆分出来，对应的 set/get 也变成了静态方法</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Bar</span> </span>&#123;
    <span class="hljs-keyword">static</span> map = <span class="hljs-keyword">new</span> <span class="hljs-built_in">WeakMap</span>()

    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">getVal</span>(<span class="hljs-params">obj</span>)</span> &#123;
       <span class="hljs-keyword">if</span>( Bar.map.has(obj))&#123;
           <span class="hljs-keyword">return</span> Bar.map.get(obj)
       &#125;<span class="hljs-keyword">else</span>&#123;
           <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>
       &#125;
    &#125;

    <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">setVal</span>(<span class="hljs-params">obj,v</span>)</span>&#123;
        Bar.map.set(obj,v)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个等价写法说明我们用到某个 <code>WeakMap</code> 的地方，可以直接把其当作一个属性写到这个对象上面去，反之也意味着对于一个对象上的某个属性，都可以通过 <code>WeakMap</code> 拆分到外部。</p>
<p>而这就是 <code>WeakMap</code> <code>WeakSet</code> 的用途。</p>
<hr>
<p>值写在对象上，代码又不是不能跑，何必费力气拆分到外部，还要专门整一个特殊的数据结构实现这种写法？</p>
<p><strong>能跑不代表写得好！！！</strong></p>
<p>写业务的时候或许遇到的比较少，其实如果写一些架构模块不难发现这种场景：</p>
<p>我需要对一些对象进行一些拓展，譬如记录一些 log 信息，你可以在原来封装好的类里面加属性，加接口。但带来的麻烦是，类会变得越来越臃肿，你也没法保证其他模块以后不会用到这些东西，影响你这个功能的重构。更何况有些对象来自于第三方库，也没法改。</p>
<p>当然,不去修改类，直接加字段也不是不行，但这种破坏封装性的代码有时候会带来意想不到的情况，比如传来一个被 freeze 的对象。</p>
<p>使用 <code>WeakMap</code> <code>WeakSet</code>，既能不破坏原有代码的封装，又能控制这些数据的可见性，何乐而不为呢？</p>
<hr>
<p><a href="https://juejin.cn/post/6947881997033275406" target="_blank">上一篇文章</a>讨论的广为人知的 <code>this</code>，这一篇文章讨论的鲜为人知的 <code>WeakMap</code> <code>WeakSet</code></p>
<p>两文讨论的东西大相径庭，其实想表达的意思却是一致的。对于一些语言特性亦或者第三方库，死背接口、甚至于一句一句地去扒源码，并不能让人用好它，理解这些接口背后的设计意图才是关键。</p>
<p>下一篇，打算整点写代码的东西，如果大家觉得本文还有点内容，还请高抬贵手点个赞哈。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            