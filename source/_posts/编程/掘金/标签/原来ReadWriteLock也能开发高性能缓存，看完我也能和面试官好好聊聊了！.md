
---
title: '原来ReadWriteLock也能开发高性能缓存，看完我也能和面试官好好聊聊了！'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca25c024e2984966970031231d1f0c94~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 27 Jul 2021 04:19:58 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca25c024e2984966970031231d1f0c94~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>大家好，我是冰河~~</strong></p>
<p>在实际工作中，有一种非常普遍的并发场景：那就是读多写少的场景。在这种场景下，为了优化程序的性能，我们经常使用缓存来提高应用的访问性能。因为缓存非常适合使用在读多写少的场景中。而在并发场景中，Java SDK中提供了ReadWriteLock来满足读多写少的场景。本文我们就来说说使用ReadWriteLock如何实现一个通用的缓存中心。</p>
<p>本文涉及的知识点有：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca25c024e2984966970031231d1f0c94~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>文章已收录到：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsunshinelyz%2Ftechnology-binghe" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sunshinelyz/technology-binghe" ref="nofollow noopener noreferrer">github.com/sunshinelyz…</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fbinghe001%2Ftechnology-binghe" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/binghe001/technology-binghe" ref="nofollow noopener noreferrer">gitee.com/binghe001/t…</a></p>
<h2 data-id="heading-0">读写锁</h2>
<p>说起读写锁，相信小伙伴们并不陌生。总体来说，读写锁需要遵循以下原则：</p>
<ul>
<li>一个共享变量允许同时被多个读线程读取到。</li>
<li>一个共享变量在同一时刻只能被一个写线程进行写操作。</li>
<li>一个共享变量在被写线程执行写操作时，此时这个共享变量不能被读线程执行读操作。</li>
</ul>
<p><strong>这里，需要小伙伴们注意的是：读写锁和互斥锁的一个重要的区别就是：读写锁允许多个线程同时读共享变量，而互斥锁不允许。所以，在高并发场景下，读写锁的性能要高于互斥锁。但是，读写锁的写操作是互斥的，也就是说，使用读写锁时，一个共享变量在被写线程执行写操作时，此时这个共享变量不能被读线程执行读操作。</strong></p>
<p>读写锁支持公平模式和非公平模式，具体是在<code>ReentrantReadWriteLock</code>的构造方法中传递一个boolean类型的变量来控制。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">ReentrantReadWriteLock</span><span class="hljs-params">(<span class="hljs-keyword">boolean</span> fair)</span> </span>&#123;
    sync = fair ? <span class="hljs-keyword">new</span> FairSync() : <span class="hljs-keyword">new</span> NonfairSync();
    readerLock = <span class="hljs-keyword">new</span> ReadLock(<span class="hljs-keyword">this</span>);
    writerLock = <span class="hljs-keyword">new</span> WriteLock(<span class="hljs-keyword">this</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>另外，需要注意的一点是：在读写锁中，读锁调用newCondition()会抛出UnsupportedOperationException异常，也就是说：读锁不支持条件变量。</strong></p>
<h2 data-id="heading-1">缓存实现</h2>
<p>这里，我们使用ReadWriteLock快速实现一个缓存的通用工具类，总体代码如下所示。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ReadWriteLockCache</span><<span class="hljs-title">K</span>,<span class="hljs-title">V</span>> </span>&#123;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> Map<K, V> m = <span class="hljs-keyword">new</span> HashMap<>();
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> ReadWriteLock rwl = <span class="hljs-keyword">new</span> ReentrantReadWriteLock();
    <span class="hljs-comment">// 读锁</span>
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> Lock r = rwl.readLock();
    <span class="hljs-comment">// 写锁</span>
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> Lock w = rwl.writeLock();
    <span class="hljs-comment">// 读缓存</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> V <span class="hljs-title">get</span><span class="hljs-params">(K key)</span> </span>&#123;
        r.lock();
        <span class="hljs-keyword">try</span> &#123; <span class="hljs-keyword">return</span> m.get(key); &#125;
        <span class="hljs-keyword">finally</span> &#123; r.unlock(); &#125;
    &#125;
    <span class="hljs-comment">// 写缓存</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> V <span class="hljs-title">put</span><span class="hljs-params">(K key, V value)</span> </span>&#123;
        w.lock();
        <span class="hljs-keyword">try</span> &#123; <span class="hljs-keyword">return</span> m.put(key, value); &#125;
        <span class="hljs-keyword">finally</span> &#123; w.unlock(); &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到，在ReadWriteLockCache中，我们定义了两个泛型类型，K代表缓存的Key，V代表缓存的value。在ReadWriteLockCache类的内部，我们使用Map来缓存相应的数据，小伙伴都都知道HashMap并不是线程安全的类，所以，这里使用了读写锁来保证线程的安全性，例如，我们在get()方法中使用了读锁，get()方法可以被多个线程同时执行读操作；put()方法内部使用写锁，也就是说，put()方法在同一时刻只能有一个线程对缓存进行写操作。</p>
<p><strong>这里需要注意的是：无论是读锁还是写锁，锁的释放操作都需要放到<code>finally&#123;&#125;</code>代码块中。</strong></p>
<p>在以往的经验中，有两种向缓存中加载数据的方式，<strong>一种是：项目启动时，将数据全量加载到缓存中，一种是在项目运行期间，按需加载所需要的缓存数据。</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3383ac7932014a73bc788106668217dc~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来，我们就分别来看看全量加载缓存和按需加载缓存的方式。</p>
<h2 data-id="heading-2">全量加载缓存</h2>
<p>全量加载缓存相对来说比较简单，就是在项目启动的时候，将数据一次性加载到缓存中，这种情况适用于缓存数据量不大，数据变动不频繁的场景，例如：可以缓存一些系统中的数据字典等信息。整个缓存加载的大体流程如下所示。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7329c85ef7c49af98c09aba1a92296f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>将数据全量加载到缓存后，后续就可以直接从缓存中读取相应的数据了。</p>
<p>全量加载缓存的代码实现比较简单，这里，我就直接使用如下代码进行演示。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ReadWriteLockCache</span><<span class="hljs-title">K</span>,<span class="hljs-title">V</span>> </span>&#123;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> Map<K, V> m = <span class="hljs-keyword">new</span> HashMap<>();
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> ReadWriteLock rwl = <span class="hljs-keyword">new</span> ReentrantReadWriteLock();
    <span class="hljs-comment">// 读锁</span>
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> Lock r = rwl.readLock();
    <span class="hljs-comment">// 写锁</span>
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> Lock w = rwl.writeLock();
    
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">ReadWriteLockCache</span><span class="hljs-params">()</span></span>&#123;
        <span class="hljs-comment">//查询数据库</span>
        List<Field<K, V>> list = .....;
        <span class="hljs-keyword">if</span>(!CollectionUtils.isEmpty(list))&#123;
            list.parallelStream().forEach((f) ->&#123;
m.put(f.getK(), f.getV);
&#125;);
        &#125;
    &#125;
    <span class="hljs-comment">// 读缓存</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> V <span class="hljs-title">get</span><span class="hljs-params">(K key)</span> </span>&#123;
        r.lock();
        <span class="hljs-keyword">try</span> &#123; <span class="hljs-keyword">return</span> m.get(key); &#125;
        <span class="hljs-keyword">finally</span> &#123; r.unlock(); &#125;
    &#125;
    <span class="hljs-comment">// 写缓存</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> V <span class="hljs-title">put</span><span class="hljs-params">(K key, V value)</span> </span>&#123;
        w.lock();
        <span class="hljs-keyword">try</span> &#123; <span class="hljs-keyword">return</span> m.put(key, value); &#125;
        <span class="hljs-keyword">finally</span> &#123; w.unlock(); &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">按需加载缓存</h2>
<p>按需加载缓存也可以叫作懒加载，就是说：需要加载的时候才会将数据加载到缓存。具体来说：就是程序启动的时候，不会将数据加载到缓存，当运行时，需要查询某些数据，首先检测缓存中是否存在需要的数据，如果存在，则直接读取缓存中的数据，如果不存在，则到数据库中查询数据，并将数据写入缓存。后续的读取操作，因为缓存中已经存在了相应的数据，直接返回缓存的数据即可。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd6f26cff745416c85f136d5571fa5b7~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这种查询缓存的方式适用于大多数缓存数据的场景。</p>
<p>我们可以使用如下代码来表示按需查询缓存的业务。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ReadWriteLockCache</span><<span class="hljs-title">K</span>,<span class="hljs-title">V</span>> </span>&#123;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> Map<K, V> m = <span class="hljs-keyword">new</span> HashMap<>();
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> ReadWriteLock rwl =  <span class="hljs-keyword">new</span> ReentrantReadWriteLock();
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> Lock r = rwl.readLock();
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> Lock w = rwl.writeLock();
    <span class="hljs-function">V <span class="hljs-title">get</span><span class="hljs-params">(K key)</span> </span>&#123;
        V v = <span class="hljs-keyword">null</span>;
        <span class="hljs-comment">//读缓存</span>
        r.lock();        
        <span class="hljs-keyword">try</span> &#123;
            v = m.get(key);
        &#125; <span class="hljs-keyword">finally</span>&#123;
            r.unlock();    
        &#125;
        <span class="hljs-comment">//缓存中存在，返回</span>
        <span class="hljs-keyword">if</span>(v != <span class="hljs-keyword">null</span>) &#123;  
            <span class="hljs-keyword">return</span> v;
        &#125;  
        <span class="hljs-comment">//缓存中不存在，查询数据库</span>
        w.lock();     
        <span class="hljs-keyword">try</span> &#123;
   <span class="hljs-comment">//再次验证缓存中是否存在数据</span>
            v = m.get(key);
            <span class="hljs-keyword">if</span>(v == <span class="hljs-keyword">null</span>)&#123; 
                <span class="hljs-comment">//查询数据库</span>
                v=从数据库中查询出来的数据
                m.put(key, v);
            &#125;
        &#125; <span class="hljs-keyword">finally</span>&#123;
            w.unlock();
        &#125;
        <span class="hljs-keyword">return</span> v; 
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里，在get()方法中，首先从缓存中读取数据，此时，我们对查询缓存的操作添加了读锁，查询返回后，进行解锁操作。判断缓存中返回的数据是否为空，不为空，则直接返回数据；如果为空，则获取写锁，之后再次从缓存中读取数据，如果缓存中不存在数据，则查询数据库，将结果数据写入缓存，释放写锁。最终返回结果数据。</p>
<p><strong>这里，有小伙伴可能会问：为啥程序都已经添加写锁了，在写锁内部为啥还要查询一次缓存呢？</strong></p>
<p>这是因为在高并发的场景下，可能会存在多个线程来竞争写锁的现象。例如：第一次执行get()方法时，缓存中的数据为空。如果此时有三个线程同时调用get()方法，同时运行到 <code>w.lock()</code>代码处，由于写锁的排他性。此时只有一个线程会获取到写锁，其他两个线程则阻塞在<code>w.lock()</code>处。获取到写锁的线程继续往下执行查询数据库，将数据写入缓存，之后释放写锁。</p>
<p>此时，另外两个线程竞争写锁，某个线程会获取到锁，继续往下执行，如果在<code>w.lock()</code>后没有<code> v = m.get(key);</code> 再次查询缓存的数据，则这个线程会直接查询数据库，将数据写入缓存后释放写锁。最后一个线程同样会按照这个流程执行。</p>
<p>这里，实际上第一个线程已经查询过数据库，并且将数据写入缓存了，其他两个线程就没必要再次查询数据库了，直接从缓存中查询出相应的数据即可。所以，在<code>w.lock()</code>后添加<code> v = m.get(key);</code> 再次查询缓存的数据，能够有效的减少高并发场景下重复查询数据库的问题，提升系统的性能。</p>
<h2 data-id="heading-4">读写锁的升降级</h2>
<p><strong>关于锁的升降级，小伙伴们需要注意的是：在ReadWriteLock中，锁是不支持升级的，因为读锁还未释放时，此时获取写锁，就会导致写锁永久等待，相应的线程也会被阻塞而无法唤醒。</strong></p>
<p>虽然不支持锁升级，但是ReadWriteLock支持锁降级，例如，我们来看看官方的ReentrantReadWriteLock示例，如下所示。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CachedData</span> </span>&#123;
    Object data;
    <span class="hljs-keyword">volatile</span> <span class="hljs-keyword">boolean</span> cacheValid;
    <span class="hljs-keyword">final</span> ReentrantReadWriteLock rwl = <span class="hljs-keyword">new</span> ReentrantReadWriteLock();

    <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">processCachedData</span><span class="hljs-params">()</span> </span>&#123;
        rwl.readLock().lock();
        <span class="hljs-keyword">if</span> (!cacheValid) &#123;
            <span class="hljs-comment">// Must release read lock before acquiring write lock</span>
            rwl.readLock().unlock();
            rwl.writeLock().lock();
            <span class="hljs-keyword">try</span> &#123;
                <span class="hljs-comment">// Recheck state because another thread might have</span>
                <span class="hljs-comment">// acquired write lock and changed state before we did.</span>
                <span class="hljs-keyword">if</span> (!cacheValid) &#123;
                    data = ...
                    cacheValid = <span class="hljs-keyword">true</span>;
                &#125;
                <span class="hljs-comment">// Downgrade by acquiring read lock before releasing write lock</span>
                rwl.readLock().lock();
            &#125; <span class="hljs-keyword">finally</span> &#123;
                rwl.writeLock().unlock(); <span class="hljs-comment">// Unlock write, still hold read</span>
            &#125;
        &#125;

        <span class="hljs-keyword">try</span> &#123;
            use(data);
        &#125; <span class="hljs-keyword">finally</span> &#123;
            rwl.readLock().unlock();
        &#125;
    &#125;
&#125;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">数据同步问题</h2>
<p>首先，这里说的数据同步指的是数据源和数据缓存之间的数据同步，说的再直接一点，就是数据库和缓存之间的数据同步。</p>
<p>这里，我们可以采取三种方案来解决数据同步的问题，如下图所示
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8544ba175cd3412da486a4a98214699c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">超时机制</h3>
<p>这个比较好理解，就是在向缓存写入数据的时候，给一个超时时间，当缓存超时后，缓存的数据会自动从缓存中移除，此时程序再次访问缓存时，由于缓存中不存在相应的数据，查询数据库得到数据后，再将数据写入缓存。</p>
<h3 data-id="heading-7">定时更新缓存</h3>
<p>这种方案是超时机制的增强版，在向缓存中写入数据的时候，同样给一个超时时间。与超时机制不同的是，在程序后台单独启动一个线程，定时查询数据库中的数据，然后将数据写入缓存中，这样能够在一定程度上避免缓存的穿透问题。</p>
<h3 data-id="heading-8">实时更新缓存</h3>
<p>这种方案能够做到数据库中的数据与缓存的数据是实时同步的，可以使用阿里开源的Canal框架实现MySQL数据库与缓存数据的实时同步。<strong>也可以使用我个人开源的mykit-data框架哦（推荐使用）~~</strong></p>
<p><strong>mykit-data开源地址：</strong></p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsunshinelyz%2Fmykit-data" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/sunshinelyz/mykit-data" ref="nofollow noopener noreferrer">github.com/sunshinelyz…</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fbinghe001%2Fmykit-data" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/binghe001/mykit-data" ref="nofollow noopener noreferrer">gitee.com/binghe001/m…</a></li>
</ul>
<p><strong>好了，今天就到这儿吧，我是冰河，我们下期见~~</strong></p></div>  
</div>
            