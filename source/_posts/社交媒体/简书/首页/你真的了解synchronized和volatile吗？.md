
---
title: '你真的了解synchronized和volatile吗？'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://www.jianshu.com/p/undefined'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://www.jianshu.com/p/undefined'
---

<div>   
<p><a href="https://links.jianshu.com/go?to=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2F-7iXIm3PABNEzPjx0QUIZw" target="_blank">原文来自于公众号：三不猴子</a>欢迎关注我的公众号，公众号内回复666获取面试资料，回复电子书获取200本PDF电子书</p>
<h3>什么是cas？</h3>
<p>cas：compare and swap 比较然后交换，它在没有锁的状态下可以保证多线程的对值得更新。我们可以看一下在jdk中对cas的应用：</p>
<pre><code class="Java">/**
 * Atomically increments by one the current value.
 *
 * @return the updated value
 */
public final int incrementAndGet() &#123;
    return unsafe.getAndAddInt(this, valueOffset, 1) + 1;
&#125;


public final int getAndAddInt(Object var1, long var2, int var4) &#123;
        int var5;
        do &#123;
            var5 = this.getIntVolatile(var1, var2);
        &#125; while(!this.compareAndSwapInt(var1, var2, var5, var5 + var4));

        return var5;
&#125;
</code></pre>
<p>在Atomic原子类中的自增操作中就使用到了compareAndSwapInt，这里的cas的实现使用的native方法。用一张流程图来理解什么是cas。</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1504" data-height="1140"><img data-original-src="//upload-images.jianshu.io/upload_images/1449291-55e6433f3bde24d2" data-original-width="1504" data-original-height="1140" data-original-format="image/png" data-original-filesize="192001" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div><br>
<p>我们先会存一下要修改的值，再修改之后再去看一下要修改的值是不是还是我们存的值如果是一致的则修改，我们在更新数据常用的乐观锁就是用的cas的机制。</p>

<blockquote>
<p>在这里面有个ABA的问题：所谓ABA就是在线程A存了值之后，有个线程B对这个值进行修改，B修改了多次最后结果还是原来那个值，这就是ABA问题，此时需要根据业务场景判断这个值得修改是否需要感知。如果需要感知就可以给这个值再加上一个版本号。</p>
</blockquote>
<p>我们用一段代码演示一下cas中ABA的问题吧</p>
<pre><code class="Java">import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicInteger;

/**
 * create by yanghongxing on 2020/5/8 11:03 下午
 */
public class ABA &#123;
    private static AtomicInteger atomicInt = new AtomicInteger(100);

    public static void main(String[] args) throws InterruptedException &#123;
        // 对一个AtomicInteger的值该两次，最后结果与之前相同
        Thread intT1 = new Thread(() -> &#123;
            atomicInt.compareAndSet(100, 101);
            atomicInt.compareAndSet(101, 100);
        &#125;);
        
        Thread intT2 = new Thread(() -> &#123;
            try &#123;
                TimeUnit.SECONDS.sleep(1);
            &#125; catch (InterruptedException e) &#123;
            &#125;
            boolean c3 = atomicInt.compareAndSet(100, 101);
            // true，执行成功
            System.out.println(c3);
        &#125;);
        intT1.start();
        intT2.start();
    &#125;
&#125;

</code></pre>
<p>使用jdk中的AtomicStampedReference可以解决这个问题。最后我们看一下cas实现原理，看一下最后native方法的源码 jdk8u: atomic_linux_x86.inline.hpp</p>
<pre><code class="c++">inline jint     Atomic::cmpxchg    (jint     exchange_value, volatile jint*     dest, jint     compare_value) &#123;
  int mp = os::is_MP();
  __asm__ volatile (LOCK_IF_MP(%4) "cmpxchgl %1,(%3)"
                    : "=a" (exchange_value)
                    : "r" (exchange_value), "a" (compare_value), "r" (dest), "r" (mp)
                    : "cc", "memory");
  return exchange_value;
</code></pre>
<p>汇编指令 我们看这一条</p>
<pre><code>__asm__ volatile (LOCK_IF_MP(%4) "cmpxchgl %1,(%3)"
</code></pre>
<p><strong>asm</strong>表示汇编指令，lock表示锁，if如果 mp（%4）表示cpu是多核， cmpxchgl表示 cmp exchange  全称 compare and exchange。<br>
最终实现：</p>
<pre><code class="assembly">lock cmpxchg 指令
</code></pre>
<p>这条汇编指令(硬件指令)表示如果是多核CPU则加上锁。</p>
<h3>Java对象在内存的布局</h3>
<p>我们先了解一下Java对象在内存中的（详细）布局，这个布局与Java锁的实现息息相关。<br>
使用工具：JOL = Java Object Layout</p>
<pre><code class="xml"><dependencies>
    <!-- https://mvnrepository.com/artifact/org.openjdk.jol/jol-core -->
    <dependency>
        <groupId>org.openjdk.jol</groupId>
        <artifactId>jol-core</artifactId>
        <version>0.9</version>
    </dependency>
</dependencies>
</code></pre>
<p>使用示例</p>
<pre><code class="Java">public class ShowJOL &#123;
    public static void main(String[] args) &#123;
        Object o = new Object();
        System.out.println(ClassLayout.parseInstance(o).toPrintable());
    &#125;
&#125;
</code></pre>
<p>输出</p>
<pre><code>java.lang.Object object internals:
 OFFSET  SIZE   TYPE DESCRIPTION                               VALUE
      0     4        (object header)                           01 00 00 00 (00000001 00000000 00000000 00000000) (1)
      4     4        (object header)                           00 00 00 00 (00000000 00000000 00000000 00000000) (0)
      8     4        (object header)                           e5 01 00 f8 (11100101 00000001 00000000 11111000) (-134217243)
     12     4        (loss due to the next object alignment)
Instance size: 16 bytes
Space losses: 0 bytes internal + 4 bytes external = 4 bytes total
</code></pre>
<blockquote>
<p>OFFSET:从第几个位置开始 <br>size:大小，单位字节，</p>
<p>TYPE DESCRIPTION：类型描述，上面的示例就是object header对象头，</p>
<p>VALUE：值</p>
<p>loss due to the next object alignment: 由于下一个对象对齐而造成的损失,我们看下面这张图。</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="308" data-height="672"><img data-original-src="//upload-images.jianshu.io/upload_images/1449291-8820b093e98df11b" data-original-width="308" data-original-height="672" data-original-format="image/png" data-original-filesize="165358" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
</blockquote>
<blockquote>
<p>markword：关于锁的信息。<br><br>
class pointer: 表示对象是属于哪个类的。<br><br>
instance data：字面理解实例数据，比如在在对象中创建了一个int a 就占4个字节，long b就占8个字节。<br><br>
padding data：如果上面的数据所占用的空间不能被8整除，padding则占用空间凑齐使之能被8整除。被8整除在读取数据的时候会比较快。</p>
</blockquote>
<p>对着这张图我们再看看上面JOL打印出来的数据，第一个和第二个都是markword各 4个字节，第三个是class pointer4个字节，本来还有  instance data 用来存成员变量的但是我们写的没有所以为0，这些总共加起来12个字节不能被8整除，所以我们要对齐加4个字节。（注这里的内存占用是默认开启字节压缩XX:+UseCompressedClassPointers -XX:+UseCompressedOops）</p>
<p>看完了这些东西我们再来执行一下下面的代码</p>
<pre><code class="java">/**
 * create by yanghongxing on 2020/5/11 11:52 下午
 */
public class ShowJOL &#123;
    public static void main(String[] args) &#123;
        Object o = new Object();
        System.out.println(ClassLayout.parseInstance(o).toPrintable());
    &#125;
&#125;
</code></pre>
<p>执行结果：</p>
<pre><code>java.lang.Object object internals:
 OFFSET  SIZE   TYPE DESCRIPTION                               VALUE
      0     4        (object header)                           01 00 00 00 (00000001 00000000 00000000 00000000) (1)
      4     4        (object header)                           00 00 00 00 (00000000 00000000 00000000 00000000) (0)
      8     4        (object header)                           e5 01 00 f8 (11100101 00000001 00000000 11111000) (-134217243)
     12     4        (loss due to the next object alignment)
Instance size: 16 bytes
Space losses: 0 bytes internal + 4 bytes external = 4 bytes total

</code></pre>
<p>对比这个的输出和第一次我们打印的输出，我们可以得出结论synchronized锁的信息是记录在markword上。<br>我们做Java开发的经常听到的一句话就是synchronized是个重量级的锁，事实上一定是这样吗？我们可以通过分析markword看看synchronized加锁过程，在早期jdk1.0的时候jdk每次申请的就是重量级的锁，性能比较差，随着后面jdk的升级synchronized的性能有所提升，synchronized并不是一开始就加重量级的锁，而是有个慢慢升级的过程。先来看表格<br>
</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1425" data-height="744"><img data-original-src="//upload-images.jianshu.io/upload_images/1449291-58446fb5b56c9ac9" data-original-width="1425" data-original-height="744" data-original-format="image/png" data-original-filesize="103177" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div><p></p>
<blockquote>
<p>偏向锁Biased Locking：Java6引入的一项多线程优化，偏向锁，顾名思义，它会偏向于第一个访问锁的线程，如果在运行过程中，同步锁只有一个线程访问，不存在多线程争用的情况，则线程是不需要触发同步的，这种情况下，就会给线程加一个偏向锁。<br>
如果在运行过程中，遇到了其他线程抢占锁，则持有偏向锁的线程会被挂起，JVM会消除它身上的偏向锁，将锁恢复到标准的轻量级锁。<br>自旋锁：自旋锁的目的是为了占着CPU的资源不释放，等到获取到锁立即进行处理。一直在自旋也是占用CPU的，如果自旋的线程非常多，自旋次数也非常大CPU可能会跑满，所以需要升级。<br>重量级锁：内核态的锁，资源开销较大。内部会将等待中的线程进行wait处理，防止消耗CPU。</p>
</blockquote>
<p>结合这张表格我们再写一个示例看看synchronized在没有锁竞争的情况下默认是怎么样的。</p>
<pre><code class="java">/**
 * create by yanghongxing on 2020/5/11 11:52 下午
 */
public class ShowJOL &#123;
    public static void main(String[] args) &#123;
        Object o = new Object();
        System.out.println(Integer.toHexString(o.hashCode()));
        System.out.println(ClassLayout.parseInstance(o).toPrintable());

        synchronized (o) &#123;
            System.out.println(Integer.toHexString(o.hashCode()));
            System.out.println(ClassLayout.parseInstance(o).toPrintable());
        &#125;
    &#125;
&#125;
</code></pre>
<p>然后看输出:</p>
<pre><code>5f8ed237

java.lang.Object object internals:
 OFFSET  SIZE   TYPE DESCRIPTION                               VALUE
      0     4        (object header)                           01 37 d2 8e (00000001 00110111 11010010 10001110) (-1898825983)
      4     4        (object header)                           5f 00 00 00 (01011111 00000000 00000000 00000000) (95)
      8     4        (object header)                           e5 01 00 f8 (11100101 00000001 00000000 11111000) (-134217243)
     12     4        (loss due to the next object alignment)
Instance size: 16 bytes
Space losses: 0 bytes internal + 4 bytes external = 4 bytes total

java.lang.Object object internals:
 OFFSET  SIZE   TYPE DESCRIPTION                               VALUE
      0     4        (object header)                           90 29 7d 06 (10010000 00101001 01111101 00000110) (108865936)
      4     4        (object header)                           00 70 00 00 (00000000 01110000 00000000 00000000) (28672)
      8     4        (object header)                           e5 01 00 f8 (11100101 00000001 00000000 11111000) (-134217243)
     12     4        (loss due to the next object alignment)
Instance size: 16 bytes
Space losses: 0 bytes internal + 4 bytes external = 4 bytes total

Disconnected from the target VM, address: '127.0.0.1:62501', transport: 'socket'

Process finished with exit code 0

</code></pre>
<p>我们在第一行打印了这个Object的hashcode的16进制编码，对比没有加锁的输出这hashcode是存在对象的markword中的。我们再看这个未加锁的markword的二级制值：00000001 00110111 11010010 10001110，看前8位的倒数3位也就001（口语描述不知道是不是准确）对比上面的表格也就是无锁状态，我们再看第二个markword的值000，对应表格就是轻量锁、自旋锁。我们再使用一个存在锁竞争的例子看看是怎么样的。</p>
<pre><code class="java">/**
 * create by yanghongxing on 2020/5/12 7:13 下午
 */
public class MarkwordMain &#123;


    private static Object OBJ = new Object();

    private static void printf() &#123;
        System.out.println(ClassLayout.parseInstance(OBJ).toPrintable());
    &#125;

    private static Runnable RUNNABLE = () -> &#123;
        synchronized (OBJ) &#123;
            printf();
        &#125;
    &#125;;

    public static void main(String[] args) throws InterruptedException &#123;
        for (int i = 0; i < 3; i++) &#123;
            new Thread(RUNNABLE).start();
        &#125;
        Thread.sleep(Integer.MAX_VALUE);
    &#125;
&#125;
</code></pre>
<p>这段代码中我们使用了三个线程去竞争打印这个内存分布的操作，看看输出结果，</p>
<pre><code>java.lang.Object object internals:
 OFFSET  SIZE   TYPE DESCRIPTION                               VALUE
      0     4        (object header)                           5a 59 82 ef (01011010 01011001 10000010 11101111) (-276670118)
      4     4        (object header)                           f9 7f 00 00 (11111001 01111111 00000000 00000000) (32761)
      8     4        (object header)                           e5 01 00 f8 (11100101 00000001 00000000 11111000) (-134217243)
     12     4        (loss due to the next object alignment)
Instance size: 16 bytes
Space losses: 0 bytes internal + 4 bytes external = 4 bytes total

java.lang.Object object internals:
 OFFSET  SIZE   TYPE DESCRIPTION                               VALUE
      0     4        (object header)                           5a 59 82 ef (01011010 01011001 10000010 11101111) (-276670118)
      4     4        (object header)                           f9 7f 00 00 (11111001 01111111 00000000 00000000) (32761)
      8     4        (object header)                           e5 01 00 f8 (11100101 00000001 00000000 11111000) (-134217243)
     12     4        (loss due to the next object alignment)
Instance size: 16 bytes
Space losses: 0 bytes internal + 4 bytes external = 4 bytes total

java.lang.Object object internals:
 OFFSET  SIZE   TYPE DESCRIPTION                               VALUE
      0     4        (object header)                           5a 59 82 ef (01011010 01011001 10000010 11101111) (-276670118)
      4     4        (object header)                           f9 7f 00 00 (11111001 01111111 00000000 00000000) (32761)
      8     4        (object header)                           e5 01 00 f8 (11100101 00000001 00000000 11111000) (-134217243)
     12     4        (loss due to the next object alignment)
Instance size: 16 bytes
Space losses: 0 bytes internal + 4 bytes external = 4 bytes total
</code></pre>
<p>我们看到是010，对应表格就是重量级锁。</p>
<p>synchronized 锁升级时按照，new - 偏向锁 - 轻量级锁 （无锁, 自旋锁，自适应自旋）- 重量级锁的过程升级的。偏向锁 - markword 上记录当前线程指针，下次同一个线程加锁的时候，不需要争用，只需要判断线程指针是否同一个，所以，偏向锁，偏向加锁的第一个线程 。</p>
<p>有争用 - 锁升级为轻量级锁 - 每个线程有自己的LockRecord在自己的线程栈上，用CAS去争用markword的LockRecord的指针，指针指向哪个线程的LockRecord，哪个线程就拥有锁</p>
<p>自旋超过10次，升级为重量级锁 - 如果太多线程自旋 CPU消耗过大，不如升级为重量级锁，进入等待队列（不消耗CPU）-XX:PreBlockSpin</p>
<p>自旋锁在 JDK1.4.2 中引入，使用 -XX:+UseSpinning 来开启。JDK 6 中变为默认开启，并且引入了自适应的自旋锁（适应性自旋锁）。</p>
<p>自适应自旋锁意味着自旋的时间（次数）不再固定，而是由前一次在同一个锁上的自旋时间及锁的拥有者的状态来决定。如果在同一个锁对象上，自旋等待刚刚成功获得过锁，并且持有锁的线程正在运行中，那么虚拟机就会认为这次自旋也是很有可能再次成功，进而它将允许自旋等待持续相对更长的时间。如果对于某个锁，自旋很少成功获得过，那在以后尝试获取这个锁时将可能省略掉自旋过程，直接阻塞线程，避免浪费处理器资源。</p>
<h3>synchronized实现原理</h3>
<h4>Java源代码级别</h4>
<p>synchronized(对象)</p>
<h4>字节码层级</h4>
<p>使用idea插件jclasslib插件查看字节码，我们以之前代码为例</p>
<pre><code class="java">public class ShowJOL &#123;
    public static void main(String[] args) &#123;
        Object o = new Object();
        System.out.println(ClassLayout.parseInstance(o).toPrintable());
    &#125;
&#125;
</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="804" data-height="289"><img data-original-src="//upload-images.jianshu.io/upload_images/1449291-e247f204db410c89" data-original-width="804" data-original-height="289" data-original-format="image/png" data-original-filesize="45883" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<pre><code class="java">public class ShowJOL &#123;
    public static void main(String[] args) &#123;
        Object o = new Object();
        synchronized (o) &#123;
            System.out.println(ClassLayout.parseInstance(o).toPrintable());
        &#125;
    &#125;
&#125;
</code></pre>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="822" data-height="469"><img data-original-src="//upload-images.jianshu.io/upload_images/1449291-e15975bbe033098a" data-original-width="822" data-original-height="469" data-original-format="image/png" data-original-filesize="69941" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div><br>
<p>在字节码层面是以monitorenter作为开始锁的开始，以moniterexit作为结束。</p>

<h4>汇编级别</h4>
<p>我们使用hsdis工具对Java源码进行反编译为汇编代码</p>
<pre><code class="java">/**
 * create by yanghongxing on 2020/5/12 11:45 下午
 */
public class SynchronizedTest &#123;

    private static int c;

    public static synchronized void sync() &#123;
    &#125;

    public static void noSynchronized() &#123;
        int a = 1;
        int b = 2;
        c = a + b;
    &#125;

    public static void main(String[] args) &#123;
        for (int j = 0; j < 1000_000; j++) &#123;
            sync();
            noSynchronized();
        &#125;
    &#125;
&#125;
</code></pre>
<pre><code>  0x00000001195d2e4e: lock cmpxchg %r11,(%r10)
  0x00000001195d2e53: je     0x00000001195d2da0
  0x00000001195d2e59: mov    %r13,(%rsp)
  0x00000001195d2e5d: movabs $0x79578d830,%rsi  ;   &#123;oop(a 'java/lang/Class' = 'com/example/demo/SynchronizedTest')&#125;
  0x00000001195d2e67: lea    0x10(%rsp),%rdx
  0x00000001195d2e6c: data32 xchg %ax,%ax
  0x00000001195d2e6f: callq  0x0000000119525860  ; OopMap&#123;off=404&#125;
                                                ;*synchronization entry
                                                ; - com.example.demo.SynchronizedTest::sync@-1 (line 11)
</code></pre>
<p>我们看到了开篇提到的lock cmpxchg这条汇编命令，结论是synchronized底层也是使用cas的方式来实现锁。</p>
<h3>锁消除 lock eliminate</h3>
<pre><code class="java">public void add(String str1,String str2)&#123;
         StringBuffer sb = new StringBuffer();
         sb.append(str1).append(str2);
&#125;
</code></pre>
<p>我们都知道 StringBuffer 是线程安全的，因为它的关键方法都是被 synchronized 修饰过的，但我们看上面这段代码，我们会发现，sb 这个引用只会在 add 方法中使用，不可能被其它线程引用（因为是局部变量，栈私有），因此 sb 是不可能共享的资源，JVM 会自动消除 StringBuffer 对象内部的锁。</p>
<h3>锁粗化 lock coarsening</h3>
<pre><code class="java">public String test(String str)&#123;
       int i = 0;
       StringBuffer sb = new StringBuffer():
       while(i < 100)&#123;
           sb.append(str);
           i++;
       &#125;
       return sb.toString():
&#125;
</code></pre>
<p>JVM 会检测到这样一连串的操作都对同一个对象加锁（while 循环内 100 次执行 append，没有锁粗化的就要进行 100  次加锁/解锁），此时 JVM 就会将加锁的范围粗化到这一连串的操作的外部（比如 while 虚幻体外），使得这一连串操作只需要加一次锁即可。</p>
<h2>volatile实现应用和原理</h2>
<p>首先了解一下volatile的作用：</p>
<ol>
<li><p>禁止指令重拍</p></li>
<li>
<p>保证内存的可见性</p>
<p>先看个看个示例</p>
</li>
</ol>
<pre><code class="Java">public class VolatileExample &#123;
    // 可见性参数
    /*volatile*/ static boolean flag = false;

    public static void main(String[] args) &#123;
        new Thread(() -> &#123;
            try &#123;
                // 暂停 0.5s 执行
                Thread.sleep(500);
            &#125; catch (InterruptedException e) &#123;
                e.printStackTrace();
            &#125;
            flag = true;
            System.out.println("flag 被修改成 true");
        &#125;).start();
        // 一直循环检测 flag=true
        while (true) &#123;
            if (flag) &#123;
                System.out.println("检测到 flag 变为 true");
                break;
            &#125;
        &#125;
    &#125;
&#125;

</code></pre>
<p>在不加volatile的时候，在子线程中修改了flag为true，但是父线程中是不可见的，我们加上volatile修饰时”检测到 flag 变为 true“可以输出。再看一个指令重排的例子。</p>
<pre><code class="Java">public class VolatileExample1 &#123;
    // 指令重排参数
    private static int a = 0, b = 0;
    private static int x = 0, y = 0;

    public static void main(String[] args) throws InterruptedException &#123;
        for (int i = 0; i < Integer.MAX_VALUE; i++) &#123;
            Thread t1 = new Thread(() -> &#123;
                // 有可能发生指令重排，先 x=b 再 a=1
                a = 1;
                x = b;
            &#125;);
            Thread t2 = new Thread(() -> &#123;
                // 有可能发生指令重排，先 y=a 再 b=1
                b = 1;
                y = a;
            &#125;);
            t1.start();
            t2.start();
            t1.join();
            t2.join();
            System.out.println("第 " + i + "次，x=" + x + " | y=" + y);
            if (x == 0 && y == 0) &#123;
                // 发生了指令重排
                break;
            &#125;
            // 初始化变量
            a = 0;
            b = 0;
            x = 0;
            y = 0;
        &#125;
    &#125;
&#125;
</code></pre>
<p>程序停止的时候只有先执行， x = b;然后执行 y = a;最后执行 a = 1和b = 1语句时，即发生了指令重排。我们再说一个禁止指令重排的应用。单例模式中保证多线程环境下的单例我们通常会使用双重校验的机制，实现代码如下：</p>
<pre><code class="Java">public class LazyDoubleCheckSingleton &#123;
    private volatile static LazyDoubleCheckSingleton lazyDoubleCheckSingleton = null;
    private LazyDoubleCheckSingleton() &#123;

    &#125;
    public static LazyDoubleCheckSingleton getInstance() &#123;
        if (lazyDoubleCheckSingleton == null) &#123;
            synchronized (LazyDoubleCheckSingleton.class) &#123;
                if (lazyDoubleCheckSingleton == null) &#123;
                    lazyDoubleCheckSingleton = new LazyDoubleCheckSingleton();
                &#125;
            &#125;
        &#125;
        return lazyDoubleCheckSingleton;
    &#125;
&#125;

</code></pre>
<p>对于要保证线程安全的单例最容易想到的方式就是在getInstance方法上加上synchronized就好啦，但是这种方式锁的力度太大，性能不是很好，所以我们在getInstance方法上先判断一下lazyDoubleCheckSingleton这个变量是否为空，如果为空我们就进行加锁。在再进行一次判断如果为空就创建一个对象。这里进行了两次判断所谓通常被称为双重校验。这里的成员变量为什么要加volatile？不加volatile会怎么样？为弄明白这个问题我们先了解一下创建一个对象的过程。</p>
<p>以lazyDoubleCheckSingleton = new LazyDoubleCheckSingleton()为例，</p>
<ol>
<li><p>分配内存给这个对象</p></li>
<li><p>初始化对象</p></li>
<li>
<p>设置lazyDoubleCheckSingleton 指向刚分配的内存地址</p>
<p>如果我们不使用volatile修饰这个lazyDoubleCheckSingleton的话可能会出现，1-3-2的执行流程，当执行1-3步之后，此时lazyDoubleCheckSingleton变量已经不为空了，他的值是new出对象的内存地址，此时有个线程过来了 到了if (lazyDoubleCheckSingleton == null) 这一步，判断不为空，就直接return出去了，这个线程拿到的就是一个未初始化的线程。所以我们要使用volatile修饰，保证指令按照1-2-3的顺序执行。下面加张图方便直观了解这个过程。</p>
</li>
</ol>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="914" data-height="704"><img data-original-src="//upload-images.jianshu.io/upload_images/1449291-ed36b8698f17c70f" data-original-width="914" data-original-height="704" data-original-format="image/png" data-original-filesize="252735" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p>对于在多线程中的执行就变成下面的方式了。<br>
多线程.png</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1280" data-height="626"><img data-original-src="//upload-images.jianshu.io/upload_images/1449291-3a6ce0e2428c9873" data-original-width="1280" data-original-height="626" data-original-format="image/png" data-original-filesize="288873" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
  
</div>
            