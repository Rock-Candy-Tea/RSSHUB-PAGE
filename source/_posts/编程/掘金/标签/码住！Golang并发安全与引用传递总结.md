
---
title: '码住！Golang并发安全与引用传递总结'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=4533'
author: 掘金
comments: false
date: Thu, 08 Sep 2022 17:52:39 GMT
thumbnail: 'https://picsum.photos/400/300?random=4533'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>因为现在服务上云的趋势，业务代码都纷纷转向golang的技术栈。在迁移或使用的过程中，由于对golang特性的生疏经常会遇到一些问题，本文总结了golang并发安全和参数引用传值时的一些知识。</p>
<p>一、Map类型并发读写引发Fatal Error</p>
<p>先看一个在Go中关于Map类型并发读写的经典例子：</p>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-keyword">var</span> testMap  = <span class="hljs-keyword">map</span>[<span class="hljs-type">string</span>]<span class="hljs-type">string</span>&#123;&#125;
<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">main</span><span class="hljs-params">()</span></span> &#123;
   <span class="hljs-keyword">go</span> <span class="hljs-function"><span class="hljs-keyword">func</span><span class="hljs-params">()</span></span> &#123;
      <span class="hljs-keyword">for</span>&#123;
         _ = testMap[<span class="hljs-string">"bar"</span>]
      &#125;
   &#125;()
   <span class="hljs-keyword">go</span> <span class="hljs-function"><span class="hljs-keyword">func</span><span class="hljs-params">()</span></span> &#123;
      <span class="hljs-keyword">for</span>  &#123;
         testMap[<span class="hljs-string">"bar"</span>] = <span class="hljs-string">"foo"</span>
      &#125;
   &#125;()
   <span class="hljs-keyword">select</span>&#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上例子会引发一个Fatal error：</p>
<p>fatal error: concurrent map read and map write</p>
<p>产生这个错误的原因就是在Go中Map类型并不是并发安全的，出于安全的考虑，此时会引发一个致命错误以保证程序不出现数据的混乱。</p>
<p>二、Go如何检测Map并发异常</p>
<p>在Go源码map.go中，可以看到以下flags：</p>
<pre><code class="hljs language-vbnet copyable" lang="vbnet">// flags
<span class="hljs-keyword">iterator</span>     = <span class="hljs-number">1</span> // there may be an <span class="hljs-keyword">iterator</span> <span class="hljs-keyword">using</span> buckets
oldIterator  = <span class="hljs-number">2</span> // there may be an <span class="hljs-keyword">iterator</span> <span class="hljs-keyword">using</span> oldbuckets
hashWriting  = <span class="hljs-number">4</span> // a goroutine <span class="hljs-built_in">is</span> writing <span class="hljs-keyword">to</span> the map
sameSizeGrow = <span class="hljs-number">8</span> // the current map growth <span class="hljs-built_in">is</span> <span class="hljs-keyword">to</span> a <span class="hljs-built_in">new</span> map <span class="hljs-keyword">of</span> the same size
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在源码中mapaccess1、mapaccess2都用于查询mapassign和mapdelete用于修改。</p>
<p>对于查询操作，大致检查并发错误的流程如下：在查询前检查并发flag是否存在，如果存在就抛出异常。</p>
<pre><code class="hljs language-csharp copyable" lang="csharp"><span class="hljs-keyword">if</span> h.flags&hashWriting != <span class="hljs-number">0</span> &#123;
    <span class="hljs-keyword">throw</span>(<span class="hljs-string">"concurrent map read and map write"</span>)
&#125;
对于修改操作则如下：

写入前检查一次标记位，通过后打上标记。

写入完成再次检查标记位，通过后还原标记。

   <span class="hljs-comment">//各类前置操作</span>
   ....
   <span class="hljs-keyword">if</span> h.flags&hashWriting != <span class="hljs-number">0</span> &#123;
      <span class="hljs-comment">//检查是否存在并发</span>
      <span class="hljs-keyword">throw</span>(<span class="hljs-string">"concurrent map writes"</span>)
   &#125;


   <span class="hljs-comment">//赋值标记位</span>
   h.flags ^= hashWriting
   ....
   <span class="hljs-comment">//后续操作</span>
  done:
   <span class="hljs-comment">//完成修改后，再次检查标记位</span>
   <span class="hljs-keyword">if</span> h.flags&hashWriting == <span class="hljs-number">0</span> &#123;
      <span class="hljs-keyword">throw</span>(<span class="hljs-string">"concurrent map writes"</span>)
   &#125;
   <span class="hljs-comment">//还原标记位取消hashWriting标记</span>
   h.flags &^= hashWriting
<span class="copy-code-btn">复制代码</span></code></pre>
<p>三、如何避免Map的并发问题</p>
<p>go官方认为因为Map并发的问题在实际开发中并不常见，如果把Map原生设计成并发安全的会带来巨大的性能开销。因此需要使用额外方式来实现。</p>
<p>（一）自行使用锁和map来解决并发问题</p>
<p>参考如下：</p>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-keyword">type</span> cocurrentMap = <span class="hljs-keyword">struct</span> &#123;
   sync.RWMutex
   m <span class="hljs-keyword">map</span>[<span class="hljs-type">string</span>]<span class="hljs-type">string</span>
&#125;


<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">main</span><span class="hljs-params">()</span></span> &#123;
   <span class="hljs-keyword">var</span> testMap = &cocurrentMap&#123;m:<span class="hljs-built_in">make</span>(<span class="hljs-keyword">map</span>[<span class="hljs-type">string</span>]<span class="hljs-type">string</span>)&#125;
   <span class="hljs-comment">//写</span>
   testMap.Lock()
   testMap.m[<span class="hljs-string">"a"</span>] = <span class="hljs-string">"foo"</span>
   testMap.Unlock()
   <span class="hljs-comment">//读</span>
   testMap.RLock()
   fmt.Println(testMap.m[<span class="hljs-string">"a"</span>])
   testMap.RUnlock()
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个方法存在问题就是并发量巨大的时候，锁的竞争也会带来巨量消耗，性能 一般。</p>
<p>（二）使用sync.Map</p>
<p>sync.Map通过巧妙的设计来提高并发安全下Map的性能，其设计思路是通过空间换时间来实现的，同时维护2份数据，read&dirty。read主要用来避免读写冲突。
其数据结构如下：</p>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-keyword">type</span> Map <span class="hljs-keyword">struct</span> &#123;
   mu Mutex <span class="hljs-comment">//锁</span>
   read atomic.Value <span class="hljs-comment">//readOnly</span>
   dirty <span class="hljs-keyword">map</span>[<span class="hljs-keyword">interface</span>&#123;&#125;]*entry <span class="hljs-comment">//*entry</span>
   misses <span class="hljs-type">int</span>
&#125;


<span class="hljs-keyword">type</span> readOnly <span class="hljs-keyword">struct</span> &#123;
   m       <span class="hljs-keyword">map</span>[<span class="hljs-keyword">interface</span>&#123;&#125;]*entry
   amended <span class="hljs-type">bool</span> <span class="hljs-comment">// true if the dirty map contains some key not in m.</span>
&#125;


<span class="hljs-keyword">type</span> entry <span class="hljs-keyword">struct</span> &#123;
   p unsafe.Pointer <span class="hljs-comment">// *interface&#123;&#125;</span>
&#125;
使用示例如下：

<span class="hljs-keyword">var</span> m sync.Map
<span class="hljs-comment">// 写</span>
m.Store(<span class="hljs-string">"test"</span>, <span class="hljs-number">1</span>)
m.Store(<span class="hljs-number">1</span>, <span class="hljs-literal">true</span>)


<span class="hljs-comment">// 读</span>
val1, _ := m.Load(<span class="hljs-string">"test"</span>)
val2, _ := m.Load(<span class="hljs-number">1</span>)
fmt.Println(val1.(<span class="hljs-type">int</span>))
fmt.Println(val2.(<span class="hljs-type">bool</span>))


<span class="hljs-comment">//遍历</span>
m.Range(<span class="hljs-function"><span class="hljs-keyword">func</span><span class="hljs-params">(key, value <span class="hljs-keyword">interface</span>&#123;&#125;)</span></span> <span class="hljs-type">bool</span> &#123;
   <span class="hljs-comment">//....</span>
   <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
&#125;)


<span class="hljs-comment">//删除</span>
m.Delete(<span class="hljs-string">"test"</span>)


<span class="hljs-comment">//读取或写入</span>
m.LoadOrStore(<span class="hljs-string">"test"</span>, <span class="hljs-number">1</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里对sync.Map的原理不做深入展开，只提几点特性：</p>
<p>read和dirty是共享内存的，尽量减少冗余内存的开销。</p>
<p>read是原子性的，可以并发读，写需要加锁。</p>
<p>读的时候先read中取，如果没有则会尝试去dirty中读取（需要有标记位readOnly.amended配合）</p>
<p>dirty就是原生Map类型，需要配合各类锁读写。</p>
<p>当read中miss次数等于dirty长度时，dirty会提升为read，并且清理已经删除的k-v（延迟更新，具体如何清理需要enrty中的p标记位配合）</p>
<p>双检查（在加锁后会再次对值检查一遍是否依然符合条件）</p>
<p>sync.Map适用于读多写少的场景。</p>
<p>sync.Map没有提供获取长度size的方法，需要通过遍历来计算。</p>
<p>四、切片类型Slice是并发安全的吗</p>
<p>与Map一样，Slice也不是并发安全的：</p>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-keyword">var</span> testSlice []<span class="hljs-type">int</span>
<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">main</span><span class="hljs-params">()</span></span> &#123;
   <span class="hljs-keyword">for</span> i:=<span class="hljs-number">0</span>; i<<span class="hljs-number">1000</span>; i++ &#123;
      <span class="hljs-keyword">go</span> <span class="hljs-function"><span class="hljs-keyword">func</span><span class="hljs-params">()</span></span> &#123;
         testSlice = <span class="hljs-built_in">append</span>(testSlice, i)
      &#125;()
   &#125;
   <span class="hljs-keyword">for</span> idx, val := <span class="hljs-keyword">range</span> testSlice &#123;
      fmt.Printf(<span class="hljs-string">"idx:%d val:%d\n"</span>, idx, val)
   &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到输出如下：</p>
<p>........</p>
<p>idx:901 val:999</p>
<p>idx:902 val:999</p>
<p>.........</p>
<p>但是在切片中并不会引发panic，如果程序无意中对切片使用了并发读写，严重的话会导致获取的数据和之后存储的数据错乱，所以这里要格外小心，可以通过加锁来避免。</p>
<p>五、Map、Slice作为参数传递的问题</p>
<p>切片除了并发有问题外，当他作为参数传递的时候，也会导致意料之外的问题，Go官方说明在Go中所有的传递都是值传递，没有引用传递的问题，但是在实际使用时，切片偶尔会引起一些疑惑，例如以下情况：</p>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">changeVal</span><span class="hljs-params">(testSlice []<span class="hljs-type">string</span>, idx <span class="hljs-type">int</span>, val <span class="hljs-type">string</span>)</span></span>&#123;
   testSlice[idx] = val
&#125;


<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">main</span><span class="hljs-params">()</span></span> &#123;
   <span class="hljs-keyword">var</span> testSlice []<span class="hljs-type">string</span>
   testSlice = <span class="hljs-built_in">make</span>([]<span class="hljs-type">string</span>, <span class="hljs-number">5</span>)
   testSlice[<span class="hljs-number">0</span>] = <span class="hljs-string">"foo"</span>
   changeVal(testSlice, <span class="hljs-number">0</span>, <span class="hljs-string">"bar"</span>)
   fmt.Println(testSlice[<span class="hljs-number">0</span>])
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上代码执行后可以看到打印出的值为：</p>
<p>bar</p>
<p>这里就奇怪了，如果按照Go官方说明在该语言中传递都是值传递的话，为什么函数内修改切片会导致原切片也一起修改呢？这里要分2个问题来看：</p>
<p>Go只会对基础值类型在传参中使用深拷贝，实际上对于Slice和Map类型，使用的是浅拷贝，Slice作为传参，其指向的内存地址依然是原数据。</p>
<p>Slice扩容机制的影响：向Slice中添加元素超出容量的时候，我们知道会触发扩容机制，而扩容机制会创建一份新的【原数据】此时，它与浅拷贝获取到的变量是没有任何关联的。</p>
<p>可以通过以下代码验证，我们故意构造触发扩容的场景：</p>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">appendVal</span><span class="hljs-params">(testSlice []<span class="hljs-type">string</span>, val <span class="hljs-type">string</span>)</span></span>&#123;
   fmt.Printf(<span class="hljs-string">"testSlice:%p\n"</span>, testSlice)
   testSlice = <span class="hljs-built_in">append</span>(testSlice, <span class="hljs-string">"addCap"</span>) <span class="hljs-comment">//触发了扩容机制</span>
   fmt.Printf(<span class="hljs-string">"after append testSlice:%p\n"</span>, testSlice)
   testSlice[<span class="hljs-number">0</span>] = val
&#125;


<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">main</span><span class="hljs-params">()</span></span> &#123;
   <span class="hljs-keyword">var</span> testSlice []<span class="hljs-type">string</span>
   testSlice = <span class="hljs-built_in">make</span>([]<span class="hljs-type">string</span>, <span class="hljs-number">5</span>)
   testSlice[<span class="hljs-number">0</span>] = <span class="hljs-string">"foo"</span>
   appendVal(testSlice,<span class="hljs-string">"bar"</span>)
   fmt.Println(testSlice[<span class="hljs-number">0</span>]) <span class="hljs-comment">//此时打印出的值为foo</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到控制台打印如下：</p>
<p>testSlice:0xc00005a050</p>
<p>after append testSlice:0xc0000700a0</p>
<p>foo</p>
<p>此时因为扩容的影响导致原切片和传递后的切片不再有关联，因此打印值回到了最初的原数据foo</p>
<p>除了扩容机制外，我们也可以利用go中的copy函数来强制深拷贝：</p>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-keyword">var</span> newTestSlice []<span class="hljs-type">string</span>
newTestSlice = <span class="hljs-built_in">make</span>([]<span class="hljs-type">string</span>, <span class="hljs-built_in">len</span>(testSlice))
<span class="hljs-built_in">copy</span>(newTestSlice, testSlice)
fmt.Printf(<span class="hljs-string">"testSlice:%p\n"</span>, testSlice)
fmt.Printf(<span class="hljs-string">"newTestSlice:%p\n"</span>, newTestSlice)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>testSlice:0xc0000d6000</p>
<p>newTestSlice:0xc0000d6050</p>
<p>另外对于数组类型，如果无意中转换为切片时，也极容易导致这种不确定性发生。切片作为参数传递时，在函数内对切片进行修改，需要时刻注意。</p>
<p>回过头再来看Map就一目了然了，因为Map的操作对象一直是引用，其即使扩容后，引用的地址不会改变，所以不会出现时而可以修改，时而不能修改的情况：</p>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">changeMap</span><span class="hljs-params">(testMap <span class="hljs-keyword">map</span>[<span class="hljs-type">string</span>]<span class="hljs-type">string</span>, k <span class="hljs-type">string</span>, v <span class="hljs-type">string</span>)</span></span>&#123;
   testMap[k] = v
&#125;


<span class="hljs-function"><span class="hljs-keyword">func</span> <span class="hljs-title">main</span><span class="hljs-params">()</span></span> &#123;
   <span class="hljs-keyword">var</span> testMap <span class="hljs-keyword">map</span>[<span class="hljs-type">string</span>]<span class="hljs-type">string</span>
   testMap = <span class="hljs-built_in">make</span>(<span class="hljs-keyword">map</span>[<span class="hljs-type">string</span>]<span class="hljs-type">string</span>)
   testMap[<span class="hljs-string">"foo"</span>] = <span class="hljs-string">"bar"</span>
   changeMap(testMap, <span class="hljs-string">"foo"</span>, <span class="hljs-string">"rab"</span>)
   fmt.Println(testMap)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出：map[foo:rab]</p>
<p>可以看到函数内修改了原参数的值。</p></div>  
</div>
            