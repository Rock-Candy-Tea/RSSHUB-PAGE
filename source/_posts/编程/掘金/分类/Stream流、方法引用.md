
---
title: 'Stream流、方法引用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8540ff5cd304b11b9e0c9542ba5da5c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 26 Aug 2021 01:27:56 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8540ff5cd304b11b9e0c9542ba5da5c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第5天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h1 data-id="heading-0">内容预览</h1>
<ul>
<li>Stream流</li>
<li>方法引用</li>
</ul>
<hr>
<h1 data-id="heading-1">Stream流</h1>
<p>说到Stream便容易想到I/O Stream，而实际上，谁规定“流”就一定是“IO流”呢？在Java 8中，得益于Lambda所带 来的函数式编程，引入了一个<strong>全新的Stream概念</strong>，用于解决已有集合类库既有的弊端。</p>
<h2 data-id="heading-2">1.1 引言</h2>
<h3 data-id="heading-3">传统集合的多步遍历代码</h3>
<p>几乎所有的集合（如<code>Collection</code>接口或<code>Map</code>接口等）都支持直接或间接的遍历操作。而当我们需要对集合中的元 素进行操作的时候，除了必需的添加、删除、获取外，典型的就是集合遍历。例如：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">import</span> java.util.ArrayList; 
<span class="hljs-keyword">import</span> java.util.List;   

<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo01ForEach</span> </span>&#123;
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
         List<String> list = <span class="hljs-keyword">new</span> ArrayList<>();
         list.add(<span class="hljs-string">"张无忌"</span>);
         list.add(<span class="hljs-string">"周芷若"</span>);
         list.add(<span class="hljs-string">"赵敏"</span>);
         list.add(<span class="hljs-string">"张强"</span>);
         list.add(<span class="hljs-string">"张三丰"</span>);
         <span class="hljs-keyword">for</span> (String name : list) &#123;
            System.out.println(name);
            &#125;
     &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是一段非常简单的集合遍历操作：对集合中的每一个字符串都进行打印输出操作。</p>
<h3 data-id="heading-4">循环遍历的弊端</h3>
<p>Java 8的Lambda让我们可以更加专注于<strong>做什么</strong>（What），而不是<strong>怎么做</strong>（How），这点此前已经结合内部类进行 了对比说明。现在，我们仔细体会一下上例代码，可以发现：</p>
<ul>
<li>for循环的语法就是“<strong>怎么做</strong>”</li>
<li>for循环的循环体才是“<strong>做什么</strong>”</li>
</ul>
<p>为什么使用循环？因为要进行遍历。但循环是遍历的唯一方式吗？遍历是指每一个元素逐一进行处理，<strong>而并不是从第一个到最后一个顺次处理的循环</strong>。前者是目的，后者是方式。
试想一下，如果希望对集合中的元素进行筛选过滤：</p>
<ol>
<li>将集合A根据条件一过滤为<strong>子集B</strong>；</li>
<li>然后再根据条件二过滤为<strong>子集C</strong>。</li>
</ol>
<p>那怎么办？在Java 8之前的做法可能为：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">import</span> java.util.ArrayList; 
<span class="hljs-keyword">import</span> java.util.List;   

<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo02NormalFilter</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
            List<String> list = <span class="hljs-keyword">new</span> ArrayList<>();
            list.add(<span class="hljs-string">"张无忌"</span>);
            list.add(<span class="hljs-string">"周芷若"</span>);
            list.add(<span class="hljs-string">"赵敏"</span>);
            list.add(<span class="hljs-string">"张强"</span>);
            list.add(<span class="hljs-string">"张三丰"</span>);
  
         List<String> zhangList = <span class="hljs-keyword">new</span> ArrayList<>();
         <span class="hljs-keyword">for</span> (String name : list) &#123;
             <span class="hljs-keyword">if</span> (name.startsWith(<span class="hljs-string">"张"</span>)) &#123;
                zhangList.add(name);
                &#125;
         &#125;
  
         List<String> shortList = <span class="hljs-keyword">new</span> ArrayList<>();
         <span class="hljs-keyword">for</span> (String name : zhangList) &#123;
             <span class="hljs-keyword">if</span> (name.length() == <span class="hljs-number">3</span>) &#123;
                shortList.add(name);
                &#125;
         &#125;
  
         <span class="hljs-keyword">for</span> (String name : shortList) &#123;
            System.out.println(name);
            &#125;
     &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码中含有三个循环，每一个作用不同：</p>
<ol>
<li>首先筛选所有姓张的人；</li>
<li>然后筛选名字有三个字的人；</li>
<li>后进行对结果进行打印输出。</li>
</ol>
<p>每当我们需要对集合中的元素进行操作的时候，总是需要进行循环、循环、再循环。这是理所当然的么？<strong>不是</strong>。循 环是做事情的方式，而不是目的。另一方面，使用线性循环就意味着只能遍历一次。如果希望再次遍历，只能再使 用另一个循环从头开始。
那，Lambda的衍生物Stream能给我们带来怎样更加优雅的写法呢？</p>
<h3 data-id="heading-5">Stream的更优写法</h3>
<p>下面来看一下借助Java 8的Stream API，什么才叫优雅：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">import</span> java.util.ArrayList; 
<span class="hljs-keyword">import</span> java.util.List;   

<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo03StreamFilter</span> </span>&#123;
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
         List<String> list = <span class="hljs-keyword">new</span> ArrayList<>();
         list.add(<span class="hljs-string">"张无忌"</span>);
         list.add(<span class="hljs-string">"周芷若"</span>);
         list.add(<span class="hljs-string">"赵敏"</span>);
         list.add(<span class="hljs-string">"张强"</span>);
         list.add(<span class="hljs-string">"张三丰"</span>);
  
         list.stream()
             .filter(s ‐> s.startsWith(<span class="hljs-string">"张"</span>))
             .filter(s ‐> s.length() == <span class="hljs-number">3</span>)
             .forEach(System.out::println);
     &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>直接阅读代码的字面意思即可完美展示无关逻辑方式的语义：<strong>获取流、过滤姓张、过滤长度为3、逐一打印</strong>。代码 中并没有体现使用线性循环或是其他任何算法进行遍历，我们真正要做的事情内容被更好地体现在代码中。</p>
<h2 data-id="heading-6">1.2 流式思想概述</h2>
<p><strong>注意：请暂时忘记对传统IO流的固有印象！</strong>
整体来看，流式思想类似于工厂车间的“<strong>生产流水线</strong>”。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8540ff5cd304b11b9e0c9542ba5da5c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>当需要对多个元素进行操作（特别是多步操作）的时候，考虑到性能及便利性，我们应该首先拼好一个“模型”步骤方案，然后再按照方案去执行它。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de65d9af8be84a14a96300e38e3b7ba4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
这张图中展示了过滤、映射、跳过、计数等多步操作，这是一种集合元素的处理方案，而方案就是一种“函数模 型”。图中的每一个方框都是一个“流”，调用指定的方法，可以从一个流模型转换为另一个流模型。而右侧的数字 3是终结果。</p>
<p>这里的<code> filter</code> 、<code>map</code>、<code>skip</code>都是在对函数模型进行操作，集合元素并没有真正被处理。只有当终结方法 count 执行的时候，整个模型才会按照指定策略执行操作。而这得益于Lambda的延迟执行特性。</p>
<blockquote>
<p>备注：“Stream流”其实是一个集合元素的函数模型，它并不是集合，也不是数据结构，其本身并不存储任何 元素（或其地址值）。</p>
</blockquote>
<p>Stream（流）是一个来自数据源的元素队列</p>
<ul>
<li>元素是特定类型的对象，形成一个队列。 Java中的Stream并不会存储元素，而是按需计算。</li>
<li><strong>数据源</strong>流的来源。 可以是集合，数组 等。</li>
</ul>
<p>和以前的Collection操作不同， Stream操作还有两个基础的特征：</p>
<ul>
<li><strong>Pipelining</strong>: 中间操作都会返回流对象本身。 这样多个操作可以串联成一个管道， 如同流式风格（ﬂuent style）。 这样做可以对操作进行优化， 比如延迟执行(laziness)和短路( short-circuiting)。</li>
<li><strong>内部迭代</strong>： 以前对集合遍历都是通过Iterator或者增强for的方式, 显式的在集合外部进行迭代， 这叫做外部迭 代。 Stream提供了内部迭代的方式，流可以直接调用遍历方法。</li>
</ul>
<p>当使用一个流的时候，通常包括三个基本步骤：获取一个数据源（source）→ 数据转换→执行操作获取想要的结 果，每次转换原有 Stream 对象不改变，返回一个新的 Stream 对象（可以有多次转换），这就允许对其操作可以 像链条一样排列，变成一个管道。</p>
<h2 data-id="heading-7">1.3 获取流</h2>
<p><code>java.util.stream.Stream<T> </code>是Java 8新加入的常用的流接口。（这并不是一个函数式接口。）
获取一个流非常简单，有以下几种常用的方式：</p>
<ul>
<li>所有的<code>Collection</code>集合都可以通过<code>stream</code>默认方法获取流；</li>
<li><code>Stream </code>接口的静态方法<code>of</code>可以获取数组对应的流。</li>
</ul>
<h3 data-id="heading-8">根据Collection获取流</h3>
<p>首先，<code>java.util.Collection</code>接口中加入了default方法 stream 用来获取流，所以其所有实现类均可获取流。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">import</span> java.util.*; 
<span class="hljs-keyword">import</span> java.util.stream.Stream;   

<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo04GetStream</span> </span>&#123;
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
         List<String> list = <span class="hljs-keyword">new</span> ArrayList<>();
         <span class="hljs-comment">// ...</span>
         Stream<String> stream1 = list.stream();
     
         Set<String> set = <span class="hljs-keyword">new</span> HashSet<>();
         <span class="hljs-comment">// ...</span>
         Stream<String> stream2 = set.stream();
  
         Vector<String> vector = <span class="hljs-keyword">new</span> Vector<>();
        <span class="hljs-comment">// ...</span>
        Stream<String> stream3 = vector.stream();
     &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">根据Map获取流</h3>
<p><code>java.util.Map</code> 接口不是<code>Collection</code>的子接口，且其K-V数据结构不符合流元素的单一特征，所以获取对应的流 需要分key、value或entry等情况：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">import</span> java.util.HashMap; 
<span class="hljs-keyword">import</span> java.util.Map; 
<span class="hljs-keyword">import</span> java.util.stream.Stream;   

<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo05GetStream</span> </span>&#123;
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
         Map<String, String> map = <span class="hljs-keyword">new</span> HashMap<>();
         <span class="hljs-comment">// ...</span>
         Stream<String> keyStream = map.keySet().stream();
         Stream<String> valueStream = map.values().stream();
         Stream<Map.Entry<String, String>> entryStream = map.entrySet().stream();
     &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">根据数组获取流</h3>
<p>如果使用的不是集合或映射而是数组，由于数组对象不可能添加默认方法，所以 <code>Stream </code>接口中提供了静态方法 <code>of </code>，使用很简单：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">import</span> java.util.stream.Stream;   

<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo06GetStream</span> </span>&#123;
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
         String[] array = &#123; <span class="hljs-string">"张无忌"</span>, <span class="hljs-string">"张翠山"</span>, <span class="hljs-string">"张三丰"</span>, <span class="hljs-string">"张一元"</span> &#125;;
         Stream<String> stream = Stream.of(array);
     &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>备注： of 方法的参数其实是一个可变参数，所以支持数组。</p>
</blockquote>
<h3 data-id="heading-11">1.4 常用方法</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bbeab8368c0244c79b93d7d7204c7b30~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>流模型的操作很丰富，这里介绍一些常用的API。这些方法可以被分成两种：</p>
<ul>
<li><strong>延迟方法</strong>：返回值类型仍然是<code>Stream</code>接口自身类型的方法，因此支持链式调用。（除了终结方法外，其余方 法均为延迟方法。）</li>
<li><strong>终结方法</strong>：返回值类型不再是<code>Stream</code>接口自身类型的方法，因此不再支持类似<code>StringBuilder</code>那样的链式调用。本小节中，终结方法包括<code>count</code>和 <code>forEach </code>方法。</li>
</ul>
<blockquote>
<p>备注：本小节之外的更多方法，请自行参考API文档。</p>
</blockquote>
<h3 data-id="heading-12">逐一处理：forEach</h3>
<p>虽然方法名字叫<code>forEach</code>，但是与for循环中的“for-each”昵称不同。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">forEach</span><span class="hljs-params">(Consumer<? <span class="hljs-keyword">super</span> T> action)</span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该方法接收一个 Consumer 接口函数，会将每一个流元素交给该函数进行处理。 #### 复习Consumer接口</p>
<pre><code class="hljs language-java copyable" lang="java">java.util.function.Consumer<T>接口是一个消费型接口。 
Consumer接口中包含抽象方法<span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">accept</span><span class="hljs-params">(T t)</span>，意为消费一个指定泛型的数据。
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">基本使用：</h4>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">import</span> java.util.stream.Stream;   

<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo12StreamForEach</span> </span>&#123;
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
         Stream<String> stream = Stream.of(<span class="hljs-string">"张无忌"</span>, <span class="hljs-string">"张三丰"</span>, <span class="hljs-string">"周芷若"</span>);
         stream.forEach(name‐> System.out.println(name));
     &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">过滤：ﬁlter</h3>
<p>可以通过<code>filter</code>方法将一个流转换成另一个子集流。方法签名:</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function">Stream<T> <span class="hljs-title">filter</span><span class="hljs-params">(Predicate<? <span class="hljs-keyword">super</span> T> predicate)</span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该接口接收一个<code>Predicate</code>函数式接口参数（可以是一个Lambda或方法引用）作为筛选条件。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c68b2f2124c447eb76bff87ddaa87a6~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-15">复习Predicate接口</h4>
<p>此前我们已经学习过<code>java.util.stream.Predicate</code>函数式接口，其中唯一的抽象方法为：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">boolean</span> <span class="hljs-title">test</span><span class="hljs-params">(T t)</span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该方法将会产生一个boolean值结果，代表指定的条件是否满足。如果结果为true，那么Stream流的 filter 方法 将会留用元素；如果结果为false，那么<code>filter</code>方法将会舍弃元素。</p>
<h4 data-id="heading-16">基本使用</h4>
<p>Stream流中的<code>filter</code>方法基本使用的代码如：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">import</span> java.util.stream.Stream;   

<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo07StreamFilter</span> </span>&#123;
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
         Stream<String> original = Stream.of(<span class="hljs-string">"张无忌"</span>, <span class="hljs-string">"张三丰"</span>, <span class="hljs-string">"周芷若"</span>);
         Stream<String> result = original.filter(s ‐> s.startsWith(<span class="hljs-string">"张"</span>));
     &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这里通过Lambda表达式来指定了筛选的条件：必须姓张。</p>
<h3 data-id="heading-17">映射：map</h3>
<p>如果需要将流中的元素映射到另一个流中，可以使用<code>map</code>方法。方法签名：</p>
<pre><code class="hljs language-java copyable" lang="java"><R> <span class="hljs-function">Stream<R> <span class="hljs-title">map</span><span class="hljs-params">(Function<? <span class="hljs-keyword">super</span> T, ? extends R> mapper)</span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该接口需要一个<code>Function</code>函数式接口参数，可以将当前流中的T类型数据转换为另一种R类型的流。</p>
<p><img src="https://upload-images.jianshu.io/upload_images/23400280-9fd341e1b7b9aed2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-18">复习Function接口</h4>
<p>此前我们已经学习过<code>java.util.stream.Function</code>函数式接口，其中唯一的抽象方法为：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function">R <span class="hljs-title">apply</span><span class="hljs-params">(T t)</span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这可以将一种T类型转换成为R类型，而这种转换的动作，就称为“映射”。</p>
<h4 data-id="heading-19">基本使用</h4>
<p>Stream流中的<code>map</code>方法基本使用的代码如：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">import</span> java.util.stream.Stream;   

<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo08StreamMap</span> </span>&#123;
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
         Stream<String> original = Stream.of(<span class="hljs-string">"10"</span>, <span class="hljs-string">"12"</span>, <span class="hljs-string">"18"</span>);
         Stream<Integer> result = original.map(str‐>Integer.parseInt(str));
     &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码中，<code>map</code>方法的参数通过方法引用，将字符串类型转换成为了int类型（并自动装箱为<code>Integer</code>类对 象）。</p>
<h3 data-id="heading-20">统计个数：count</h3>
<p>正如旧集合<code>Collection</code>当中的<code>size</code>方法一样，流提供<code>count</code>方法来数一数其中的元素个数：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">long</span> <span class="hljs-title">count</span><span class="hljs-params">()</span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该方法返回一个long值代表元素个数（不再像旧集合那样是int值）。基本使用：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">import</span> java.util.stream.Stream;   

<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo09StreamCount</span> </span>&#123;
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
         Stream<String> original = Stream.of(<span class="hljs-string">"张无忌"</span>, <span class="hljs-string">"张三丰"</span>, <span class="hljs-string">"周芷若"</span>);
         Stream<String> result = original.filter(s ‐> s.startsWith(<span class="hljs-string">"张"</span>));
         System.out.println(result.count()); <span class="hljs-comment">// 2</span>
     &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-21">取用前几个：limit</h3>
<p><code>limit </code>方法可以对流进行截取，只取用前n个。方法签名：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function">Stream<T> <span class="hljs-title">limit</span><span class="hljs-params">(<span class="hljs-keyword">long</span> maxSize)</span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参数是一个long型，如果集合当前长度大于参数则进行截取；否则不进行操作。基本使用：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c241999b5f2437c83442a0139db64d6~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">import</span> java.util.stream.Stream;   

<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo10StreamLimit</span> </span>&#123;
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
         Stream<String> original = Stream.of(<span class="hljs-string">"张无忌"</span>, <span class="hljs-string">"张三丰"</span>, <span class="hljs-string">"周芷若"</span>);
         Stream<String> result = original.limit(<span class="hljs-number">2</span>);
         System.out.println(result.count()); <span class="hljs-comment">// 2</span>
     &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-22">跳过前几个：skip</h3>
<p>如果希望跳过前几个元素，可以使用<code>skip</code>方法获取一个截取之后的新流：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function">Stream<T> <span class="hljs-title">skip</span><span class="hljs-params">(<span class="hljs-keyword">long</span> n)</span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果流的当前长度大于n，则跳过前n个；否则将会得到一个长度为0的空流。基本使用：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/503ba7e6c02e41efbeda66f240e31eea~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">import</span> java.util.stream.Stream;   
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo11StreamSkip</span> </span>&#123;
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
         Stream<String> original = Stream.of(<span class="hljs-string">"张无忌"</span>, <span class="hljs-string">"张三丰"</span>, <span class="hljs-string">"周芷若"</span>);
         Stream<String> result = original.skip(<span class="hljs-number">2</span>);
         System.out.println(result.count()); <span class="hljs-comment">// 1</span>
     &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">组合：concat</h3>
<p>如果有两个流，希望合并成为一个流，那么可以使用<code>Stream</code>接口的静态方法 <code>concat </code>：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">static</span> <T> <span class="hljs-function">Stream<T> <span class="hljs-title">concat</span><span class="hljs-params">(Stream<? extends T> a, Stream<? extends T> b)</span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>备注：这是一个静态方法，与 java.lang.String 当中的 concat 方法是不同的。</p>
</blockquote>
<p>该方法的基本使用代码如：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">import</span> java.util.stream.Stream;   

<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo12StreamConcat</span> </span>&#123;
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
         Stream<String> streamA = Stream.of(<span class="hljs-string">"张无忌"</span>);
         Stream<String> streamB = Stream.of(<span class="hljs-string">"张翠山"</span>);
         Stream<String> result = Stream.concat(streamA, streamB);
     &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-24">1.5 练习：集合元素处理（传统方式）</h2>
<h3 data-id="heading-25">题目</h3>
<p>现在有两个<code>ArrayList</code>集合存储队伍当中的多个成员姓名，要求使用传统的for循环（或增强for循环）<strong>依次</strong>进行以 下若干操作步骤：</p>
<ol>
<li>第一个队伍只要名字为3个字的成员姓名；存储到一个新集合中。</li>
<li>第一个队伍筛选之后只要前3个人；存储到一个新集合中。</li>
<li>第二个队伍只要姓张的成员姓名；存储到一个新集合中。</li>
<li>第二个队伍筛选之后不要前2个人；存储到一个新集合中。</li>
<li>将两个队伍合并为一个队伍；存储到一个新集合中。</li>
<li>根据姓名创建<code>Person</code>对象；存储到一个新集合中。</li>
<li>打印整个队伍的Person对象信息。</li>
</ol>
<p>两个队伍（集合）的代码如下：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">import</span> java.util.ArrayList; 
<span class="hljs-keyword">import</span> java.util.List;
   
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">DemoArrayListNames</span> </span>&#123;
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
        <span class="hljs-comment">//第一支队伍</span>
         ArrayList<String> one = <span class="hljs-keyword">new</span> ArrayList<>();
  
         one.add(<span class="hljs-string">"迪丽热巴"</span>);
         one.add(<span class="hljs-string">"宋远桥"</span>);
         one.add(<span class="hljs-string">"苏星河"</span>);
         one.add(<span class="hljs-string">"石破天"</span>);
         one.add(<span class="hljs-string">"石中玉"</span>);
         one.add(<span class="hljs-string">"老子"</span>);
         one.add(<span class="hljs-string">"庄子"</span>);
         one.add(<span class="hljs-string">"洪七公"</span>);
  
         <span class="hljs-comment">//第二支队伍</span>
         ArrayList<String> two = <span class="hljs-keyword">new</span> ArrayList<>();
         two.add(<span class="hljs-string">"古力娜扎"</span>);
         two.add(<span class="hljs-string">"张无忌"</span>);
         two.add(<span class="hljs-string">"赵丽颖"</span>);
         two.add(<span class="hljs-string">"张三丰"</span>);
         two.add(<span class="hljs-string">"尼古拉斯赵四"</span>);
         two.add(<span class="hljs-string">"张天爱"</span>);
         two.add(<span class="hljs-string">"张二狗"</span>);
         <span class="hljs-comment">// ....</span>
              &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而<code>Person</code>类的代码为：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
   
       <span class="hljs-keyword">private</span> String name;

       <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">Person</span><span class="hljs-params">()</span> </span>&#123;&#125;

       <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">Person</span><span class="hljs-params">(String name)</span> </span>&#123;
         <span class="hljs-keyword">this</span>.name = name;
        &#125;
  
     <span class="hljs-meta">@Override</span>
     <span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">toString</span><span class="hljs-params">()</span> </span>&#123;
         <span class="hljs-keyword">return</span> <span class="hljs-string">"Person&#123;name='"</span> + name + <span class="hljs-string">"'&#125;"</span>;
     &#125;
  
     <span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">getName</span><span class="hljs-params">()</span> </span>&#123;
         <span class="hljs-keyword">return</span> name;
     &#125;
  
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">setName</span><span class="hljs-params">(String name)</span> </span>&#123;
         <span class="hljs-keyword">this</span>.name = name;
     &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-26">解答</h3>
<p>既然使用传统的for循环写法，那么：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">DemoArrayListNames</span> </span>&#123;
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
         List<String> one = <span class="hljs-keyword">new</span> ArrayList<>();
         <span class="hljs-comment">// ...</span>
  
         List<String> two = <span class="hljs-keyword">new</span> ArrayList<>();
         <span class="hljs-comment">// ...</span>
  
         <span class="hljs-comment">// 第一个队伍只要名字为3个字的成员姓名；</span>
         List<String> oneA = <span class="hljs-keyword">new</span> ArrayList<>();
         <span class="hljs-keyword">for</span> (String name : one) &#123;
             <span class="hljs-keyword">if</span> (name.length() == <span class="hljs-number">3</span>) &#123;
                 oneA.add(name);
             &#125;
         &#125;
  
         <span class="hljs-comment">// 第一个队伍筛选之后只要前3个人；</span>
         List<String> oneB = <span class="hljs-keyword">new</span> ArrayList<>();
         <span class="hljs-keyword">for</span> (<span class="hljs-keyword">int</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">3</span>; i++) &#123;
             oneB.add(oneA.get(i));
         &#125;
  
         <span class="hljs-comment">// 第二个队伍只要姓张的成员姓名；</span>
         List<String> twoA = <span class="hljs-keyword">new</span> ArrayList<>();
         <span class="hljs-keyword">for</span> (String name : two) &#123;
             <span class="hljs-keyword">if</span> (name.startsWith(<span class="hljs-string">"张"</span>)) &#123;
                 twoA.add(name);
             &#125;
         &#125;
  
         <span class="hljs-comment">// 第二个队伍筛选之后不要前2个人；</span>
         List<String> twoB = <span class="hljs-keyword">new</span> ArrayList<>();
         <span class="hljs-keyword">for</span> (<span class="hljs-keyword">int</span> i = <span class="hljs-number">2</span>; i < twoA.size(); i++) &#123;
             twoB.add(twoA.get(i));
         &#125;
  
         <span class="hljs-comment">// 将两个队伍合并为一个队伍；</span>
         List<String> totalNames = <span class="hljs-keyword">new</span> ArrayList<>();
         totalNames.addAll(oneB);
         totalNames.addAll(twoB);
  
         <span class="hljs-comment">// 根据姓名创建Person对象；</span>
         List<Person> totalPersonList = <span class="hljs-keyword">new</span> ArrayList<>();
         <span class="hljs-keyword">for</span> (String name : totalNames) &#123;
             totalPersonList.add(<span class="hljs-keyword">new</span> Person(name));
         &#125;
 
        <span class="hljs-comment">// 打印整个队伍的Person对象信息。</span>
         <span class="hljs-keyword">for</span> (Person person : totalPersonList) &#123;
             System.out.println(person);
         &#125;
     &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行结果为：</p>
<pre><code class="copyable">Person&#123;name='宋远桥'&#125; 
Person&#123;name='苏星河'&#125; 
Person&#123;name='石破天'&#125; 
Person&#123;name='张天爱'&#125; 
Person&#123;name='张二狗'&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-27">1.6 练习：集合元素处理（Stream方式）</h2>
<h3 data-id="heading-28">题目</h3>
<p>将上一题当中的传统for循环写法更换为Stream流式处理方式。两个集合的初始内容不变，<code>Person</code>类的定义也不 变。</p>
<h3 data-id="heading-29">解答</h3>
<p>等效的Stream流式处理代码为：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">import</span> java.util.ArrayList; 
<span class="hljs-keyword">import</span> java.util.List; 
<span class="hljs-keyword">import</span> java.util.stream.Stream;   

<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">DemoStreamNames</span> </span>&#123;
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
         List<String> one = <span class="hljs-keyword">new</span> ArrayList<>();
         <span class="hljs-comment">// ...</span>
  
         List<String> two = <span class="hljs-keyword">new</span> ArrayList<>();
         <span class="hljs-comment">// ...</span>
  
         <span class="hljs-comment">// 第一个队伍只要名字为3个字的成员姓名；</span>
         <span class="hljs-comment">// 第一个队伍筛选之后只要前3个人；</span>
         Stream<String> streamOne = one.stream().filter(s ‐> s.length() == <span class="hljs-number">3</span>).limit(<span class="hljs-number">3</span>);
  
         <span class="hljs-comment">// 第二个队伍只要姓张的成员姓名；</span>
         <span class="hljs-comment">// 第二个队伍筛选之后不要前2个人；</span>
         Stream<String> streamTwo = two.stream().filter(s ‐> s.startsWith(<span class="hljs-string">"张"</span>)).skip(<span class="hljs-number">2</span>);
  
         <span class="hljs-comment">// 将两个队伍合并为一个队伍；</span>
         <span class="hljs-comment">// 根据姓名创建Person对象；</span>
         <span class="hljs-comment">// 打印整个队伍的Person对象信息。         Stream.concat(streamOne, streamTwo).map(Person::new).forEach(System.out::println);</span>

    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行效果完全一样：</p>
<pre><code class="copyable">Person&#123;name='宋远桥'&#125; 
Person&#123;name='苏星河'&#125; 
Person&#123;name='石破天'&#125; 
Person&#123;name='张天爱'&#125; 
Person&#123;name='张二狗'&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h1 data-id="heading-30">方法引用</h1>
<p>在使用Lambda表达式的时候，我们实际上传递进去的代码就是一种解决方案：拿什么参数做什么操作。那么考虑 一种情况：如果我们在Lambda中所指定的操作方案，已经有地方存在相同方案，那是否还有必要再写重复逻辑？</p>
<h2 data-id="heading-31">2.1 冗余的Lambda场景</h2>
<p>来看一个简单的函数式接口以应用Lambda表达式：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@FunctionalInterface</span> 
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">Printable</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">print</span><span class="hljs-params">(String str)</span></span>;    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>Printable</code>接口当中唯一的抽象方法<code>print</code>接收一个字符串参数，目的就是为了打印显示它。那么通过Lambda 来使用它的代码很简单：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo01PrintSimple</span> </span>&#123;
     <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">printString</span><span class="hljs-params">(Printable data)</span> </span>&#123;
        data.print(<span class="hljs-string">"Hello, World!"</span>);
     &#125;
  
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
        printString(s ‐> System.out.println(s));
     &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中<code>printString</code>方法只管调用<code>Printable</code>接口的<code>print</code>方法，而并不管 print 方法的具体实现逻辑会将字符串 打印到什么地方去。而<code>main</code>方法通过Lambda表达式指定了函数式接口<code>Printable</code>的具体操作方案为：<strong>拿到 String（类型可推导，所以可省略）数据后，在控制台中输出它</strong>。</p>
<h2 data-id="heading-32">2.2 问题分析</h2>
<p>这段代码的问题在于，对字符串进行控制台打印输出的操作方案，明明已经有了现成的实现，那就是<code>System.out</code>对象中的<code>println(String)</code>方法。既然Lambda希望做的事情就是调用<code>println(String)</code>方法，那何必自己手动调用呢？</p>
<h2 data-id="heading-33">2.3 用方法引用改进代码</h2>
<p>能否省去Lambda的语法格式（尽管它已经相当简洁）呢？只要“引用”过去就好了：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo02PrintRef</span> </span>&#123;
     <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">printString</span><span class="hljs-params">(Printable data)</span> </span>&#123;
         data.print(<span class="hljs-string">"Hello, World!"</span>);
     &#125;
  
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
        printString(System.out::println);
        &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>请注意其中的双冒号<code>::</code>写法，这被称为“方法引用”，而双冒号是一种新的语法。 ## 2.4 方法引用符
双冒号<code>::</code>为引用运算符，而它所在的表达式被称为<strong>方法引用</strong>。如果Lambda要表达的函数方案已经存在于某个方 法的实现中，那么则可以通过双冒号来引用该方法作为Lambda的替代者。</p>
<h3 data-id="heading-34">语义分析</h3>
<p>例如上例中，<code>System.out</code>对象中有一个重载的<code>println(String)</code>方法恰好就是我们所需要的。那么对于<code>printString</code>方法的函数式接口参数，对比下面两种写法，完全等效：</p>
<ul>
<li>Lambda表达式写法：<code> s -> System.out.println(s)</code>;</li>
<li>方法引用写法： <code>System.out::println</code></li>
</ul>
<p>第一种语义是指：拿到参数之后经Lambda之手，继而传递给<code>System.out.println</code>方法去处理。
第二种等效写法的语义是指：直接让<code>System.out</code>中的<code>println</code>方法来取代Lambda。两种写法的执行效果完全一 样，而第二种方法引用的写法复用了已有方案，更加简洁。</p>
<blockquote>
<p>注:Lambda 中 传递的参数 一定是方法引用中 的那个方法可以接收的类型,否则会抛出异常</p>
</blockquote>
<h3 data-id="heading-35">推导与省略</h3>
<p>如果使用Lambda，那么根据“<strong>可推导就是可省略</strong>”的原则，无需指定参数类型，也无需指定的重载形式——它们都 将被自动推导。而如果使用方法引用，也是同样可以根据上下文进行推导。
函数式接口是Lambda的基础，而方法引用是Lambda的孪生兄弟。
下面这段代码将会调用<code>println</code>方法的不同重载形式，将函数式接口改为int类型的参数：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@FunctionalInterface</span> 
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">PrintableInteger</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">print</span><span class="hljs-params">(<span class="hljs-keyword">int</span> str)</span></span>;    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于上下文变了之后可以自动推导出唯一对应的匹配重载，所以方法引用没有任何变化：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo03PrintOverload</span> </span>&#123;
     <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">printInteger</span><span class="hljs-params">(PrintableInteger data)</span> </span>&#123;
        data.print(<span class="hljs-number">1024</span>);
        &#125;
  
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
        printInteger(System.out::println);
        &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这次方法引用将会自动匹配到<code>println(int)</code>的重载形式。</p>
<h2 data-id="heading-36">2.5 通过对象名引用成员方法</h2>
<p>这是常见的一种用法，与上例相同。如果一个类中已经存在了一个成员方法：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MethodRefObject</span> </span>&#123;
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">printUpperCase</span><span class="hljs-params">(String str)</span> </span>&#123;
        System.out.println(str.toUpperCase());
        &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数式接口仍然定义为：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@FunctionalInterface</span> 
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">Printable</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">print</span><span class="hljs-params">(String str)</span></span>;    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么当需要使用这个<code>printUpperCase</code>成员方法来替代<code>Printable</code>接口的Lambda的时候，已经具有了<code>MethodRefObject</code>类的对象实例，则可以通过对象名引用成员方法，代码为：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo04MethodRef</span> </span>&#123;
     <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">printString</span><span class="hljs-params">(Printable lambda)</span> </span>&#123;
        lambda.print(<span class="hljs-string">"Hello"</span>);
      &#125;
  
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
         MethodRefObject obj = <span class="hljs-keyword">new</span> MethodRefObject();
         printString(obj::printUpperCase);
     &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-37">2.6 通过类名称引用静态方法</h2>
<p>由于在<code>java.lang.Math</code>类中已经存在了静态方法<code>abs</code>，所以当我们需要通过Lambda来调用该方法时，有两种写 法。首先是函数式接口：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@FunctionalInterface</span> 
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">Calcable</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">int</span> <span class="hljs-title">calc</span><span class="hljs-params">(<span class="hljs-keyword">int</span> num)</span></span>;    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第一种写法是使用Lambda表达式：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo05Lambda</span> </span>&#123;
     <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">method</span><span class="hljs-params">(<span class="hljs-keyword">int</span> num, Calcable lambda)</span> </span>&#123;
        System.out.println(lambda.calc(num));
      &#125;
  
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
        method(‐<span class="hljs-number">10</span>, n ‐> Math.abs(n));
      &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是使用方法引用的更好写法是：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo06MethodRef</span> </span>&#123;
     <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">method</span><span class="hljs-params">(<span class="hljs-keyword">int</span> num, Calcable lambda)</span> </span>&#123;
        System.out.println(lambda.calc(num));
      &#125;
  
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
        method(‐<span class="hljs-number">10</span>, Math::abs);
      &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个例子中，下面两种写法是等效的：</p>
<ul>
<li>Lambda表达式：<code>n -> Math.abs(n)</code></li>
<li>方法引用：<code>Math::abs</code></li>
</ul>
<h2 data-id="heading-38">2.7 通过super引用成员方法</h2>
<p>如果存在继承关系，当Lambda中需要出现super调用时，也可以使用方法引用进行替代。首先是函数式接口：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@FunctionalInterface</span> 
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">Greetable</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">greet</span><span class="hljs-params">()</span></span>;    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后是父类<code>Human</code>的内容：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Human</span> </span>&#123;
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">sayHello</span><span class="hljs-params">()</span> </span>&#123;
        System.out.println(<span class="hljs-string">"Hello!"</span>);
        &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>后是子类<code>Man</code>的内容，其中使用了Lambda的写法：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Man</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Human</span> </span>&#123;
     <span class="hljs-meta">@Override</span>
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">sayHello</span><span class="hljs-params">()</span> </span>&#123;
         System.out.println(<span class="hljs-string">"大家好,我是Man!"</span>);
     &#125;
  
     <span class="hljs-comment">//定义方法method,参数传递Greetable接口</span>
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">method</span><span class="hljs-params">(Greetable g)</span></span>&#123;
         g.greet();
     &#125;
  
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">show</span><span class="hljs-params">()</span></span>&#123;
         <span class="hljs-comment">//调用method方法,使用Lambda表达式</span>
         method(()‐>&#123;
             <span class="hljs-comment">//创建Human对象,调用sayHello方法</span>
             <span class="hljs-keyword">new</span> Human().sayHello();
         &#125;);
         <span class="hljs-comment">//简化Lambda</span>
         method(()‐><span class="hljs-keyword">new</span> Human().sayHello());
         <span class="hljs-comment">//使用super关键字代替父类对象</span>
         method(()‐><span class="hljs-keyword">super</span>.sayHello());
     &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是如果使用方法引用来调用父类中的<code>sayHello</code>方法会更好，例如另一个子类 <code>Woman</code> ：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Man</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Human</span> </span>&#123;
     <span class="hljs-meta">@Override</span>
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">sayHello</span><span class="hljs-params">()</span> </span>&#123;
         System.out.println(<span class="hljs-string">"大家好,我是Man!"</span>);
     &#125;
  
     <span class="hljs-comment">//定义方法method,参数传递Greetable接口</span>
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">method</span><span class="hljs-params">(Greetable g)</span></span>&#123;
         g.greet();
     &#125;
  
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">show</span><span class="hljs-params">()</span></span>&#123;
         method(<span class="hljs-keyword">super</span>::sayHello);
     &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个例子中，下面两种写法是等效的：</p>
<ul>
<li>Lambda表达式：<code>() -> super.sayHello()</code></li>
<li>方法引用：<code>super::sayHello</code></li>
</ul>
<h2 data-id="heading-39">2.8 通过this引用成员方法</h2>
<p>this代表当前对象，如果需要引用的方法就是当前类中的成员方法，那么可以使用“<strong>this::成员方法</strong>”的格式来使用方法引用。首先是简单的函数式接口：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@FunctionalInterface</span> 
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">Richable</span> </span>&#123;
     <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">buy</span><span class="hljs-params">()</span></span>;   
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面是一个丈夫<code>Husband</code>类：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Husband</span> </span>&#123;
     <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span> <span class="hljs-title">marry</span><span class="hljs-params">(Richable lambda)</span> </span>&#123;
        lambda.buy();
      &#125;
  
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">beHappy</span><span class="hljs-params">()</span> </span>&#123;
        marry(() ‐> System.out.println(<span class="hljs-string">"买套房子"</span>));
      &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>开心方法<code>beHappy</code>调用了结婚方法<code>marry</code>，后者的参数为函数式接口<code>Richable</code>，所以需要一个Lambda表达式。 但是如果这个Lambda表达式的内容已经在本类当中存在了，则可以对<code>Husband</code>丈夫类进行修改：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Husband</span> </span>&#123;
     <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span> <span class="hljs-title">buyHouse</span><span class="hljs-params">()</span> </span>&#123;
        System.out.println(<span class="hljs-string">"买套房子"</span>);
      &#125;
  
     <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span> <span class="hljs-title">marry</span><span class="hljs-params">(Richable lambda)</span> </span>&#123;
        lambda.buy();
      &#125;
  
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">beHappy</span><span class="hljs-params">()</span> </span>&#123;
        marry(() ‐> <span class="hljs-keyword">this</span>.buyHouse());
      &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果希望取消掉Lambda表达式，用方法引用进行替换，则更好的写法为：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Husband</span> </span>&#123;
     <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span> <span class="hljs-title">buyHouse</span><span class="hljs-params">()</span> </span>&#123;
        System.out.println(<span class="hljs-string">"买套房子"</span>);
      &#125;
  
     <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span> <span class="hljs-title">marry</span><span class="hljs-params">(Richable lambda)</span> </span>&#123;
        lambda.buy();
      &#125;
  
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">beHappy</span><span class="hljs-params">()</span> </span>&#123;
        marry(<span class="hljs-keyword">this</span>::buyHouse);
      &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个例子中，下面两种写法是等效的：</p>
<ul>
<li>Lambda表达式：<code>() -> this.buyHouse()</code></li>
<li>方法引用：<code>this::buyHouse</code></li>
</ul>
<h2 data-id="heading-40">2.9 类的构造器引用</h2>
<p>由于构造器的名称与类名完全一样，并不固定。所以构造器引用使用 类名称<code>::new </code>的格式表示。首先是一个简单的<code>Person</code>类：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Person</span> </span>&#123;
     <span class="hljs-keyword">private</span> String name;
  
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">Person</span><span class="hljs-params">(String name)</span> </span>&#123;
         <span class="hljs-keyword">this</span>.name = name;
     &#125;
  
     <span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">getName</span><span class="hljs-params">()</span> </span>&#123;
         <span class="hljs-keyword">return</span> name;
     &#125;
  
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">setName</span><span class="hljs-params">(String name)</span> </span>&#123;
         <span class="hljs-keyword">this</span>.name = name;
     &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后是用来创建<code>Person</code>对象的函数式接口：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">PersonBuilder</span> </span>&#123;
     <span class="hljs-function">Person <span class="hljs-title">buildPerson</span><span class="hljs-params">(String name)</span></span>; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>要使用这个函数式接口，可以通过Lambda表达式：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo09Lambda</span> </span>&#123;
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">printName</span><span class="hljs-params">(String name, PersonBuilder builder)</span> </span>&#123;
        System.out.println(builder.buildPerson(name).getName());
      &#125;
  
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
        printName(<span class="hljs-string">"赵丽颖"</span>, name ‐> <span class="hljs-keyword">new</span> Person(name));
      &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是通过构造器引用，有更好的写法：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo10ConstructorRef</span> </span>&#123;
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">printName</span><span class="hljs-params">(String name, PersonBuilder builder)</span> </span>&#123;
        System.out.println(builder.buildPerson(name).getName());
      &#125;
  
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
        printName(<span class="hljs-string">"赵丽颖"</span>, Person::<span class="hljs-keyword">new</span>);
      &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个例子中，下面两种写法是等效的：</p>
<ul>
<li>Lambda表达式：<code>name -> new Person(name)</code></li>
<li>方法引用：<code>Person::new</code></li>
</ul>
<h2 data-id="heading-41">2.10 数组的构造器引用</h2>
<p>数组也是<code>Object</code>的子类对象，所以同样具有构造器，只是语法稍有不同。如果对应到Lambda的使用场景中时， 需要一个函数式接口：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@FunctionalInterface</span> 
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">ArrayBuilder</span> </span>&#123;
    <span class="hljs-keyword">int</span>[] buildArray(<span class="hljs-keyword">int</span> length);    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在应用该接口的时候，可以通过Lambda表达式：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo11ArrayInitRef</span> </span>&#123;
     <span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">int</span>[] initArray(<span class="hljs-keyword">int</span> length, ArrayBuilder builder) &#123;
        <span class="hljs-keyword">return</span> builder.buildArray(length);
     &#125;
      
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
        <span class="hljs-keyword">int</span>[] array = initArray(<span class="hljs-number">10</span>, length ‐> <span class="hljs-keyword">new</span> <span class="hljs-keyword">int</span>[length]);
     &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是更好的写法是使用数组的构造器引用：</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo12ArrayInitRef</span> </span>&#123;
     <span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">int</span>[] initArray(<span class="hljs-keyword">int</span> length, ArrayBuilder builder) &#123;
        <span class="hljs-keyword">return</span> builder.buildArray(length);
     &#125;
  
     <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
        <span class="hljs-keyword">int</span>[] array = initArray(<span class="hljs-number">10</span>, <span class="hljs-keyword">int</span>[]::<span class="hljs-keyword">new</span>);
     &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个例子中，下面两种写法是等效的：</p>
<ul>
<li>Lambda表达式：<code>length -> new int[length]</code></li>
<li>方法引用：<code>int[]::new</code></li>
</ul></div>  
</div>
            