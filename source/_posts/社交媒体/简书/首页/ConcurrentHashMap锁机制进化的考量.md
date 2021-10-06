
---
title: 'ConcurrentHashMap锁机制进化的考量'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/195230-746521de13cce97c.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/195230-746521de13cce97c.png'
---

<div>   
<h3>前言</h3>
<p>又是有一段时间没写过Java相关的东西了。本来是想返璞归真一把，聊聊HashMap的，但HashMap的内容太多，写它的大佬也实在太多，并且不乏好文章。就算只读其他大作（如美团技术团队的<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F21673805" target="_blank">《Java 8系列之重新认识HashMap》</a>），配合自己研究代码，相信所有人都能理解，所以作罢。</p>
<p>我们知道，HashMap是无法保证线程安全性的，如果在并发环境下插入一个HashMap，哈希桶数组扩容时，有可能会造成链表出现环（美团技术的文章有详解）。若要保证线程安全性，就得使用ConcurrentHashMap。而ConcurrentHashMap在JDK 7和JDK 8中的锁机制设计有相当大的区别，本文来简单谈谈（其实也是老生常谈了</p>
<h3>CHM in JDK 7</h3>
<p>JDK 7版CHM使用Segment与HashEntry两种数据结构，示意图如下。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1358" data-height="942"><img data-original-src="//upload-images.jianshu.io/upload_images/195230-746521de13cce97c.png" data-original-width="1358" data-original-height="942" data-original-format="image/png" data-original-filesize="102480" src="https://upload-images.jianshu.io/upload_images/195230-746521de13cce97c.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>可见，整个CHM存储空间被划分成16个Segment，每个Segment内又包含0到多个HashEntry的单链表（有一个HashEntry数组存储链表头节点），每个链表就是一个哈希桶。HashEntry内存储具体的键值及哈希码。</p>
<p>Segment内部类继承自ReentrantLock，因此习惯将JDK 7 CHM的这种思路称作“锁分段技术”——在CHM内数据分布均匀的情况下，每一把Segment锁只会负责1/16部分数据的同步。当多线程同时写入CHM时（读取不用加锁），如果数据落到不同的Segment上，就不会造成锁的竞争，提升了并发访问的效率。</p>
<p>以下是Segment.put()方法的源码。</p>
<pre><code class="java">final V put(K key, int hash, V value, boolean onlyIfAbsent) &#123;
    HashEntry<K,V> node = tryLock() ? null :
        scanAndLockForPut(key, hash, value);
    V oldValue;
    try &#123;
        HashEntry<K,V>[] tab = table;
        int index = (tab.length - 1) & hash;
        HashEntry<K,V> first = entryAt(tab, index);
        for (HashEntry<K,V> e = first;;) &#123;
            if (e != null) &#123;
                K k;
                if ((k = e.key) == key ||
                    (e.hash == hash && key.equals(k))) &#123;
                    oldValue = e.value;
                    if (!onlyIfAbsent) &#123;
                        e.value = value;
                        ++modCount;
                    &#125;
                    break;
                &#125;
                e = e.next;
            &#125;
            else &#123;
                if (node != null)
                    node.setNext(first);
                else
                    node = new HashEntry<K,V>(hash, key, value, first);
                int c = count + 1;
                if (c > threshold && tab.length < MAXIMUM_CAPACITY)
                    rehash(node);
                else
                    setEntryAt(tab, index, node);
                ++modCount;
                count = c;
                oldValue = null;
                break;
            &#125;
        &#125;
    &#125; finally &#123;
        unlock();
    &#125;
    return oldValue;
&#125;
</code></pre>
<p>具体的插入过程就不提了，注意区分插入的桶位置存在与不存在HashEntry（即是否发生了哈希冲突）的两种情况，以及头插法、扩容操作就行，下面看看与锁相关的部分。</p>
<p>线程进入put()方法时，会首先调用ReentrantLock.tryLock()方法试图获取锁。如果未能获取到锁（被其他线程持有中），就调用scanAndLockForPut()方法，其源码如下。</p>
<pre><code class="java">private HashEntry<K,V> scanAndLockForPut(K key, int hash, V value) &#123;
    HashEntry<K,V> first = entryForHash(this, hash);
    HashEntry<K,V> e = first;
    HashEntry<K,V> node = null;
    int retries = -1; // negative while locating node
    while (!tryLock()) &#123;
        HashEntry<K,V> f; // to recheck first below
        if (retries < 0) &#123;
            if (e == null) &#123;
                if (node == null) // speculatively create node
                    node = new HashEntry<K,V>(hash, key, value, null);
                retries = 0;
            &#125;
            else if (key.equals(e.key))
                retries = 0;
            else
                e = e.next;
        &#125;
        else if (++retries > MAX_SCAN_RETRIES) &#123;
            lock();
            break;
        &#125;
        else if ((retries & 1) == 0 &&
                 (f = entryForHash(this, hash)) != first) &#123;
            e = first = f; // re-traverse if entry changed
            retries = -1;
        &#125;
    &#125;
    return node;
&#125;
</code></pre>
<p>可见是自旋执行tryLock()方法获取锁，最多会重试MAX_SCAN_RETRIES（多核环境下为64）次。如果重试达到上限还未成功，就直接调用lock()方法阻塞，等待锁被其他线程释放。注意在重试的最后会检测对应的HashEntry是否发生了变化，如果变化了，会重新开始自旋。</p>
<p>关于<code>(retries & 1) == 0</code>这句话是怎么来的，可以参见<a href="https://links.jianshu.com/go?to=http%3A%2F%2Faltair.cs.oswego.edu%2Fpipermail%2Fconcurrency-interest%2F2014-August%2F012881.html" target="_blank">Doug Lea本人的解答</a>。</p>
<p>本线程插入完毕之后，调用ReentrantLock.unlock()方法释放锁，同时唤醒AQS队列中阻塞着的下一个线程（如果有的话）进行插入操作，执行完毕。</p>
<h3>CHM in JDK 8</h3>
<p>JDK 8版CHM使用与HashMap相同的数据结构，即哈希桶数组（Node[]）+链表或红黑树，示意图如下。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1390" data-height="794"><img data-original-src="//upload-images.jianshu.io/upload_images/195230-fa4ebdadd77c81f7.png" data-original-width="1390" data-original-height="794" data-original-format="image/png" data-original-filesize="94319" src="https://upload-images.jianshu.io/upload_images/195230-fa4ebdadd77c81f7.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1190" data-height="444"><img data-original-src="//upload-images.jianshu.io/upload_images/195230-e8c3e01e1b25102f.png" data-original-width="1190" data-original-height="444" data-original-format="image/png" data-original-filesize="211782" src="https://upload-images.jianshu.io/upload_images/195230-e8c3e01e1b25102f.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>虽然JDK 8的CHM源码里还保留着Segment的定义，但已经不再使用了。</p>
<p>以下则是插入数据的核心方法putVal()的源码。</p>
<pre><code class="java"> final V putVal(K key, V value, boolean onlyIfAbsent) &#123;
     if (key == null || value == null) throw new NullPointerException();
     int hash = spread(key.hashCode());
     int binCount = 0;
     for (Node<K,V>[] tab = table;;) &#123;
         Node<K,V> f; int n, i, fh;
         if (tab == null || (n = tab.length) == 0)
             tab = initTable();
         else if ((f = tabAt(tab, i = (n - 1) & hash)) == null) &#123;
             if (casTabAt(tab, i, null,
                          new Node<K,V>(hash, key, value, null)))
                 break;                   // no lock when adding to empty bin
         &#125;
         else if ((fh = f.hash) == MOVED)
             tab = helpTransfer(tab, f);
         else &#123;
             V oldVal = null;
             synchronized (f) &#123;
                 if (tabAt(tab, i) == f) &#123;
                     if (fh >= 0) &#123;
                         binCount = 1;
                         for (Node<K,V> e = f;; ++binCount) &#123;
                             K ek;
                             if (e.hash == hash &&
                                 ((ek = e.key) == key ||
                                  (ek != null && key.equals(ek)))) &#123;
                                 oldVal = e.val;
                                 if (!onlyIfAbsent)
                                     e.val = value;
                                 break;
                             &#125;
                             Node<K,V> pred = e;
                             if ((e = e.next) == null) &#123;
                                 pred.next = new Node<K,V>(hash, key,
                                                           value, null);
                                 break;
                             &#125;
                         &#125;
                     &#125;
                     else if (f instanceof TreeBin) &#123;
                         Node<K,V> p;
                         binCount = 2;
                         if ((p = ((TreeBin<K,V>)f).putTreeVal(hash, key,
                                                        value)) != null) &#123;
                             oldVal = p.val;
                             if (!onlyIfAbsent)
                                 p.val = value;
                         &#125;
                     &#125;
                 &#125;
             &#125;
             if (binCount != 0) &#123;
                 if (binCount >= TREEIFY_THRESHOLD)
                     treeifyBin(tab, i);
                 if (oldVal != null)
                     return oldVal;
                 break;
             &#125;
         &#125;
     &#125;
     addCount(1L, binCount);
     return null;
 &#125;
</code></pre>
<p>该方法的步骤简述如下：</p>
<ol>
<li>计算key的哈希码；</li>
<li>检查哈希桶数组是否为空，若为空，调用initTable()方法初始化；</li>
<li>调用tabAt()方法获得哈希码对应到哈希桶数组的下标，并获取该桶的头结点f；</li>
<li>若f为空（即为空桶），调用casTabAt()方法，通过CAS操作（Unsafe.compareAndSwapObject()）将新元素插入为头节点。若CAS失败，说明有并发操作，重试之；</li>
<li>若f不为空，但是其hash值为MOVED（即-1），说明其他线程触发了扩容操作，调用helpTransfer()方法参与扩容；</li>
<li>若均不符合4和5步骤的条件，说明可以正常插入，用synchronized关键字在f上加锁，并在对应桶的链表或红黑树上插入新元素；</li>
<li>最后判断是否要将链表转换为红黑树，如果需要，调用treeifyBin()方法转换之。</li>
</ol>
<p>通过上面的分析，我们可以总结出，JDK 8的CHM用CAS和synchronized替代了JDK 7中的分段ReentrantLock。</p>
<blockquote>
<p><strong>这种“进化”有什么好处呢？</strong></p>
<p>其一，锁分离的<strong>粒度细化</strong>了，从Segment级别细化到了哈希桶级别。也就是说，在插入元素不发生哈希冲突的情况下，就不必加锁。</p>
<p>其二，在插入桶的头结点时使用无锁的<strong>CAS操作</strong>，效率很高。</p>
<p>其三，虽然我们也可以让Node类继承ReentrantLock并执行f.lock()/unlock()操作，但从JDK 6开始，JVM对内置的synchronized关键字做了大量优化，<strong>synchronized不再是重量级锁的代名词</strong>，而是会由无锁状态开始，随着并发程度的提升而膨胀成偏向锁、轻量级锁，再到重量级锁（其中包含适应性自旋过程）。在锁粒度细化的前提下，发生争用的概率降低，synchronized膨胀成重量级锁的机会也不多，故可以省去线程被挂起和唤醒（上下文切换）的大量开销。</p>
</blockquote>
<h3>The End</h3>
<p>明天早起搬砖，民那晚安晚安。</p>
  
</div>
            