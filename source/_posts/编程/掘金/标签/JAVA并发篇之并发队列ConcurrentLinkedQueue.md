
---
title: 'JAVA并发篇之并发队列ConcurrentLinkedQueue'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45c818ee97534c8c9604b53e819cb7ac~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 06 Jun 2021 23:45:22 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45c818ee97534c8c9604b53e819cb7ac~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文开始介绍并发队列，为后面介绍<strong>线程池</strong>打下基础。并发队列莫非也是<strong>出队</strong>、<strong>入队</strong>操作，还有一个比较重要的点就是如何保证其<strong>线程安全性</strong>，有些并发队列保证<strong>线程安全</strong>是通过<strong>lock</strong>，有些是通过<strong>CAS</strong>。
我们从<strong>ConcurrentLinkedQueue</strong>开始吧。</p>
<h1 data-id="heading-0">1. 介绍</h1>
<p><strong>ConcurrentLinkedQueue</strong>是<strong>集合框架</strong>的一员，是一个无界限且线程安全，基于<strong>单向链表</strong>的队列。该队列的顺序是<strong>FIFO</strong>。当<strong>多线程访问公共集合</strong>时，使用这个类是一个不错的选择。<strong>不允许null元素</strong>。是一个非阻塞的队列。</p>
<p>它的迭代器是<strong>弱一致性</strong>的，不会抛出 <strong>java.util.ConcurrentModificationException</strong>，也可能在迭代期间，其他操作也正在进行。**size()**方法，不能保证是正确的，因为在迭代时，其他线程也可以操作该队列。</p>
<h1 data-id="heading-1">1.1 类图</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45c818ee97534c8c9604b53e819cb7ac~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7eb7be0df5f0409cbb6fa7b74fc14bc0~tplv-k3u1fbpfcp-zoom-1.image" alt="c91451d56a20b4bc9250eea9028aa25d_9c2a7b6dea814eeda0da8ec6e95a409b_from=pc.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>(<em><strong>显示的方法都是公有方法</strong></em>)</p>
<pre><code class="copyable">public class ConcurrentLinkedQueue<E> extends AbstractQueue<E>
        implements Queue<E>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>继承至<strong>AbstractQueue</strong>，他提供了队列操作的一个框架，有基本的方法，<strong>add</strong>、<strong>remove</strong>，<strong>element</strong>等等，这些方法基于<strong>offer</strong>，<strong>poll</strong>，<strong>peek</strong>(最主要看这几个方法)。</p>
<h1 data-id="heading-2">2. 源码分析</h1>
<h1 data-id="heading-3">2.1 类的整体结构</h1>
<p>队列中的元素<strong>Node</strong></p>
<pre><code class="copyable">private static class Node<E> &#123;
        // 保证两个字段的可见性
        volatile E item;
        volatile Node<E> next;

        /**
         * Constructs a new node.  Uses relaxed write because item can
         * only be seen after publication via casNext.
         */
        Node(E item) &#123;
            UNSAFE.putObject(this, itemOffset, item);
        &#125;

        boolean casItem(E cmp, E val) &#123;
            return UNSAFE.compareAndSwapObject(this, itemOffset, cmp, val);
        &#125;

        void lazySetNext(Node<E> val) &#123;
            // putOrderedXXX是putXXXVolatile的延迟版本，设置某个值不会被其他线程立即看到(可见性)
            // putOrderedXXX设置的值的修饰应该是volatile，这样该方法才有用

            // 关于为什么使用这个方法，主要目的肯定是提高效率，但是具体原理，我只能告诉大家跟内存屏障有关(我也不太清楚这一块，待我研究后，再写一篇文章)
            UNSAFE.putOrderedObject(this, nextOffset, val);
        &#125;

        boolean casNext(Node<E> cmp, Node<E> val) &#123;
            return UNSAFE.compareAndSwapObject(this, nextOffset, cmp, val);
        &#125;

        // Unsafe类中的东西，可以去了解一下

        private static final sun.misc.Unsafe UNSAFE;
        private static final long itemOffset;
        private static final long nextOffset;

        static &#123;
            try &#123;
                UNSAFE = sun.misc.Unsafe.getUnsafe();
                Class<?> k = Node.class;
                itemOffset = UNSAFE.objectFieldOffset
                    (k.getDeclaredField("item"));
                nextOffset = UNSAFE.objectFieldOffset
                    (k.getDeclaredField("next"));
            &#125; catch (Exception e) &#123;
                throw new Error(e);
            &#125;
        &#125;
    &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>构造器1:</p>
<pre><code class="copyable">    // private transient volatile Node<E> head;
    // private transient volatile Node<E> tail;
    public ConcurrentLinkedQueue() &#123;
        head = tail = new Node<E>(null);
    &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>构造器2:</p>
<pre><code class="copyable">public ConcurrentLinkedQueue(Collection<? extends E> c) &#123;
        Node<E> h = null, t = null;
        for (E e : c) &#123;
            checkNotNull(e);
            Node<E> newNode = new Node<E>(e);
            if (h == null)
                h = t = newNode;
            else &#123;
                t.lazySetNext(newNode);
                t = newNode;
            &#125;
        &#125;
        if (h == null)
            h = t = new Node<E>(null);
        head = h;
        tail = t;
    &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面开始讲方法，从<strong>offer</strong>，<strong>poll</strong>，<strong>peek</strong>从这几个方法入手</p>
<h1 data-id="heading-4">2.2 offer</h1>
<blockquote>
<p>添加元素到队尾。因为队列是无界的，这个方法永远不会返回false</p>
</blockquote>
<p>分为三种情况进行分析(<strong>一定自己跟着代码debug，一步步地走</strong>)</p>
<ol>
<li>单线程时（<strong>使用IDEA debug一直进入的是 else if把我搞迷茫了，我会写一个博客来解释原因</strong>）</li>
</ol>
<pre><code class="copyable">        ConcurrentLinkedQueue<String> queue = new ConcurrentLinkedQueue<>();
        queue.offer("A");
        queue.offer("B");

<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上面的代码，分析每一个步骤。 <strong>执行构造函数后:</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73e96f64e081483887dbbbc09bc279e9~tplv-k3u1fbpfcp-zoom-1.image" alt="JAVA并发篇之并发队列ConcurrentLinkedQueue" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时链表的head与tail指向<strong>哨兵节点</strong></p>
<p><strong>插入"A",</strong> <strong>此时没有设置tail</strong>('两跳机制'，这里的原因后面详见)</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bcbca764623e49fd8cf1a57ca7cfd6da~tplv-k3u1fbpfcp-zoom-1.image" alt="JAVA并发篇之并发队列ConcurrentLinkedQueue" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>插入"B",</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c9332751c9348409922e0f8c6324604~tplv-k3u1fbpfcp-zoom-1.image" alt="JAVA并发篇之并发队列ConcurrentLinkedQueue" loading="lazy" referrerpolicy="no-referrer"></p>
<p>单线程情况比较简单</p>
<ol start="2">
<li>多线程offer时</li>
</ol>
<pre><code class="copyable"> public boolean offer(E e) &#123;
        checkNotNull(e);
        final Node<E> newNode = new Node<E>(e);

        for (Node<E> t = tail, p = t;;) &#123;
            Node<E> q = p.next;
            if (q == null) &#123;
                // p is last node
                // 只有一个线程能够CAS成功，其余的都重试
                if (p.casNext(null, newNode)) &#123;

                    // 延迟设置tail，第一个node入队不会设置tail，第二个node入队才会设置tail
                    //以此类推, '两跳机制'
                    if (p != t) // hop two nodes at a time
                        casTail(t, newNode);  // Failure is OK.
                    return true;
                &#125;
                // Lost CAS race to another thread; re-read next
            &#125;
            // 这里是有其他线程正在poll操作才会进入，此时只考虑多线程offer的情况，暂不分析
            else if (p == q)
                // We have fallen off list.  If tail is unchanged, it
                // will also be off-list, in which case we need to
                // jump to head, from which all live nodes are always
                // reachable.  Else the new tail is a better bet.
                p = (t != (t = tail)) ? t : head;
            else
                // Check for tail updates after two hops.
                // 存在tail被更改前，和更改后的两种情况
                p = (p != t && t != (t = tail)) ? t : q;
        &#125;
    &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>结合上面的代码</strong>，看图</p>
<ul>
<li><strong>步骤一</strong>，<strong>线程A</strong>、<strong>线程B</strong>都执行到</li>
</ul>
<pre><code class="copyable">   if (p.casNext(null, newNode))

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78f9d388067d40e395a959f68a98aea5~tplv-k3u1fbpfcp-zoom-1.image" alt="JAVA并发篇之并发队列ConcurrentLinkedQueue" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>步骤二</strong>，只有一个线程执行成功，假设<strong>线程A</strong>成功，<strong>线程B</strong>失败
因为<strong>p(a) == t(a)</strong>, 此时不执行<em>casTail</em>，<strong>tail</strong>不变。<em>q = p.next</em>, 所以此时<strong>q(b) = Node2</strong> ，那么 <em>p(b) != q(b)</em>, <strong>线程B</strong>执行<em>p = (p != t && t != (t = tail)) ? t : q;</em></li>
</ul>
<p><strong>线程B</strong>即将执行</p>
<pre><code class="copyable">   p = (p != t && t != (t = tail)) ? t : q;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>步骤三</strong> 此时线程C进入。
此时，<em>p(c) != q(c)</em>, <strong>线程C</strong>执行</li>
</ul>
<pre><code class="copyable">   p = (p != t && t != (t = tail)) ? t : q;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行完后，<strong>q(c)<strong>赋值给</strong>p(c)</strong>. 再次循环，此时，<em>q(c) == null</em>, 设置p(c)的next，<strong>线程C</strong>将值入队</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf407b4c5f2343878287d513c4a28b18~tplv-k3u1fbpfcp-zoom-1.image" alt="d068d7a20fb765fac7b41cb45376a96a_75b5bd8e77824ac2a6e484590e6d1714_from=pc.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>步骤四</strong> <em>p(c) != t(c)</em>, <strong>线程C</strong>执行<em>casTail(t, newNode)</em>, <strong>线程C</strong>设置尾结点</li>
<li>此时线程B执行</li>
</ul>
<pre><code class="copyable">   p = (p != t && t != (t = tail)) ? t : q;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为p(b) == t(b)，所以 q(b) 赋值给 p(b)。继续循环，最后得到</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/74fb945c274642d0bce50d5dc223eb94~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ae708a3476f4ce3a170de0ec928f548~tplv-k3u1fbpfcp-zoom-1.image" alt="c5c8d5f5a458b674a3ca2a081886c242_6f2e5a70346847f49c76b6cd52494bcf_from=pc.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li><strong>多线程的另一种情况</strong>，回到<strong>步骤三</strong>，此时<strong>线程C</strong>把值入队了，但是还没有设置<strong>tail</strong></li>
</ol>
<ul>
<li><strong>线程B</strong>，将值入队成功
在<strong>步骤三</strong>的基础上，<strong>线程B</strong>入队成功后，目前的状况如下:</li>
</ul>
<p>此时，<strong>线程C</strong>执行<strong>casTail(t, newNode)</strong>，但是现在的tail != t(c), CAS失败, 直接返回。</p>
<h1 data-id="heading-5">2.2.1 小结</h1>
<p>上面不管是多线程还是单线程，都是努力地去寻找<strong>next为null</strong>的节点，若为<strong>next节点</strong>为null，再判断是否满足设置<strong>tail</strong>的条件。</p>
<p>多线程<strong>offer</strong>的第一种情况存在<strong>设置tail</strong>滞后的问题，我把它称之为**"两跳机制"<strong>，后面讲使用这种机制的原因。
我们看到上面的情况一直没有进入</strong>else if (p == q)<strong>分支，进入</strong>else if<strong>分支只会发生在有其他线程在</strong>poll<strong>时，我们先讲讲</strong>poll**，再讲讲何时进入<strong>else if</strong>分支。</p>
<h1 data-id="heading-6">2.3 poll</h1>
<blockquote>
<p>删除并返回头结点的值</p>
</blockquote>
<p>简单提一下<strong>单线程</strong>与<strong>多线程</strong>的<strong>poll</strong>，着重分析一下<strong>poll</strong>与<strong>offer</strong>共存的情况</p>
<ol>
<li>单线程时
单线程比较简单，就不画图了，按照上面的<strong>queue</strong>，进行<strong>一步一步的debug</strong>就行了</li>
<li>多线程，只有<strong>poll</strong>时</li>
</ol>
<pre><code class="copyable"> public E poll() &#123;
        restartFromHead:
        for (;;) &#123;
            for (Node<E> h = head, p = h, q;;) &#123;
                E item = p.item;

                // casItem这里只有一个线程能够成功，其余的继续下面的代码
                if (item != null && p.casItem(item, null)) &#123;
                    // Successful CAS is the linearization point
                    // for item to be removed from this queue.
                    if (p != h) // hop two nodes at a time
                        updateHead(h, ((q = p.next) != null) ? q : p);
                    return item;
                &#125;
                else if ((q = p.next) == null) &#123;
                    updateHead(h, p);
                    return null;
                &#125;
                else if (p == q)
                    continue restartFromHead;
                else
                    p = q;
            &#125;
        &#125;
    &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">    final void updateHead(Node<E> h, Node<E> p) &#123;
        if (h != p && casHead(h, p))
            // 将之前的头节点，自己指向自己，等待被GC
            h.lazySetNext(h);
    &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>从上面代码可以看出，修改<strong>item</strong>与<strong>head</strong>都会使用CAS，这些变量都是被<strong>volatile</strong>修饰，所以保证了这些变量的<strong>线程安全性</strong>。不管是单线程还是多线程的<strong>poll</strong>，它们都是去寻找一个<strong>有效的头节点</strong>，删除并返回该值，若不是有效的就继续找，若队列为空了，就返回<strong>null</strong>。</p>
<p>最后分析一下，<strong>offer</strong>与<strong>poll</strong>共存的情况</p>
<ul>
<li><strong>线程A</strong>做<strong>offer</strong>操作，<strong>线程B</strong>做<strong>poll</strong>操作，初始的状态如下：</li>
<li><strong>线程A</strong>进入。</li>
<li><strong>线程A</strong>将要执行</li>
</ul>
<pre><code class="copyable">Node<E> q = p.next;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>线程B</strong>进入，进行<strong>poll</strong>操作
此时，<strong>线程B</strong>执行了一次内循环，将q(b)赋值给了p(b)；</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5eabd24b70ab4370a445e872013f0623~tplv-k3u1fbpfcp-zoom-1.image" alt="JAVA并发篇之并发队列ConcurrentLinkedQueue" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>线程B</strong>再次执行内循环，此时将<strong>p(b).item</strong>置空，将<strong>p(b)<strong>赋值给</strong>head</strong>，之前的<strong>h(b)<strong>的</strong>next</strong>指向自己，<strong>线程B</strong>退出</li>
<li><strong>线程A</strong>执行</li>
</ul>
<pre><code class="copyable">  Node<E> q = p.next;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e645c170d5e4de1aba783cf1db7b3fa~tplv-k3u1fbpfcp-zoom-1.image" alt="JAVA并发篇之并发队列ConcurrentLinkedQueue" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时，<strong>p(a).next</strong> 指向自己(等待被<em>GC</em>), 进入**else if (p == q)**分支，<strong>线程A</strong>退出，经过一番执行后，最后得到的状态，如下:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b6cc15e26924a859f6db17a7ce8753e~tplv-k3u1fbpfcp-zoom-1.image" alt="JAVA并发篇之并发队列ConcurrentLinkedQueue" loading="lazy" referrerpolicy="no-referrer"></p>
<p>进入<strong>else if (p == q)<strong>分支的情况，只会发生在</strong>poll</strong>与<strong>offer</strong>共存的情况下。</p>
<h1 data-id="heading-7">2.4 peek</h1>
<blockquote>
<p>获取首个有效的节点，并返回</p>
</blockquote>
<pre><code class="copyable">public E peek() &#123;
        restartFromHead:
        for (;;) &#123;
            for (Node<E> h = head, p = h, q;;) &#123;
                E item = p.item;
                if (item != null || (q = p.next) == null) &#123;
                    updateHead(h, p);
                    return item;
                &#125;
                else if (p == q)
                    continue restartFromHead;
                else
                    p = q;
            &#125;
        &#125;
    &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>peek</strong>与<strong>poll</strong>的操作类似，这里就贴一下代码就是了。</p>
<h1 data-id="heading-8">3. 总结</h1>
<p><strong>ConcurrentLinkedQueue</strong>是使用非阻塞的方式保证线程的安全性，在设置关系到整个<strong>Queue</strong>结构的变量时(这些变量都被<strong>volatile</strong>修饰)，都使用<strong>CAS</strong>的方式对它们进行赋值。</p>
<ul>
<li>size方法是<strong>线程不安全的</strong>，返回的结果可能不准确</li>
</ul>
<p><strong>关于“两跳机制”(自己取得名字)，</strong></p>
<blockquote>
<p>Both head and tail are permitted to lag. In fact, failing to update them every time one could is a significant optimization (fewer CASes). As with LinkedTransferQueue (see the internal documentation for that class), we use a slack threshold of two; that is, we update head/tail when the current pointer appears to be two or more steps away from the first/last node.</p>
</blockquote>
<blockquote>
<p>Since head and tail are updated concurrently and independently, it is possible for tail to lag behind head (why not)? -- ConcurrentLinkedQueue</p>
</blockquote>
<p>大致意思，<strong>head</strong>与<strong>tail</strong>允许被延迟设置。不是每次更新它们是一个重大的优化，这样做就可以<strong>更少的CAS</strong>(这样在很多线程使用时，积少成多，效率更高)。它的延迟阈值是2，设置head/tail时，当前的结点离first/last有两步或更多的距离。 这就是“<em>两跳机制</em>”</p>
<p>我们想不通的地方，可能是这个类或方法的一个优化的地方。向着大佬看齐~</p>
<h1 data-id="heading-9">4. 引用</h1>
<p>Java多线程 39 - ConcurrentLinkedQueue详解，讲得非常好，上面的思路是跟着他来的</p></div>  
</div>
            