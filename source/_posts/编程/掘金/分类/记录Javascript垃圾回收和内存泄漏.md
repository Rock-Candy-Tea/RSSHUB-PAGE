
---
title: '记录Javascript垃圾回收和内存泄漏'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d08e477e999447cb6ad5f126f64216d~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 00:24:23 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d08e477e999447cb6ad5f126f64216d~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">垃圾回收</h4>
<h5 data-id="heading-1">是么是垃圾回收？</h5>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FGlossary%2FGarbage_collection" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Glossary/Garbage_collection" ref="nofollow noopener noreferrer"><strong>垃圾回收</strong>是一个术语，用于描述查找和删除那些不再被其它对象引用的对象的处理过程。换句话说，垃圾回收是删除任何其它对象未使用的对象的过程。垃圾回收通常缩写为'GC'，式javascript中使用的内存管理系统的基本组成部分。</a></p>
<h5 data-id="heading-2">为什么要进行垃圾回收？</h5>
<p>在js中，V8只能使用系统的一部分内存，64位系统下最多能分配1.4G内存，32位系统中0.7G，这样的内存其实并不大，nodejs遇到一个2G的文件,可能就无法进行写入内存进行各种操作了.</p>
<ul>
<li>为什么内存分配有上限?</li>
</ul>
<ol>
<li>js的单线程机制</li>
</ol>
<p>意味着一旦进入垃圾回收，就无法进行其它任务了，造成卡顿。
2. 垃圾回收的限制
垃圾回收是一份十分耗时的操作，V8官方是这样形容的</p>
<pre><code class="copyable">以 1.5GB 的垃圾回收堆内存为例，V8 做一次小的垃圾回收需要50ms 以上，做一次非增量式(ps:后面会解释)的垃圾回收甚至要 1s 以上。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>鉴于这些原因，V8做了一个粗暴的选择，限制内存，1.4 0.7由此而来。当然这个内存是可以调整的，</p>
<pre><code class="copyable">// 这是调整老生代这部分的内存，单位是MB。后面会详细介绍新生代和老生代内存
node --max-old-space-size=2048 xxx.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者</p>
<pre><code class="copyable">// 这是调整新生代这部分的内存，单位是 KB。
node --max-new-space-size=2048 xxx.js
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-3">怎么进行垃圾回收的？</h5>
<p>v8把堆内存分为两部分———新生代内存和老生代内存，新生代内存就是临时分配的内存，存活时间短，老生代内存是常驻内存，存活时间长。
盗个图——</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d08e477e999447cb6ad5f126f64216d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://juejin.cn/post/6844904004007247880" target="_blank" title="https://juejin.cn/post/6844904004007247880">(2.4w字,建议收藏)😇原生JS灵魂之问(下), 冲刺🚀进阶最后一公里(附个人成长经验分享)</a></p>
<p>新生代内存默认为32MB和16MB，分别对用64和32位操作系统，够小了，临时存储用的，也能理解。</p>
<ul>
<li>新生代的垃圾回收怎么做的呢？</li>
</ul>
<p>首先将新生代内存一分为二，</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae6637f558f647edae4025d5e2bf5dff~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>From为使用的内存，To为闲置的内存，首先检查From的内存中的对象是否存活，如果存活，就复制到To内存中，否则直接回收，检查完毕之后，To中为使用的内存，From中的内存被回收，为空闲状态，角色反转，检查To的内存中的对象是否存活，如果存活复制到From中,否则直接回收···，如此循环回收。</p>
<p>会有一个问题，检查到非存活对象，直接回收不就好了吗，为什么还要来回翻转，这是为了解决这样的问题，</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bdc2c1ef35974bce9f5bec53ce7701d6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>深色的代表存活对象，白色的代表未使用的内存，很明显的看出，未使用的内存是不连续的，不利于进行内存的分配，这种零散的空间也叫做内存碎片，刚刚说的新生代垃圾回收算法也叫Scavenge算法。</p>
<p>Scavenge算法主要就是解决内存碎片的问题，在一系列操作之后，to空间就变成了这个样子：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/710aff4fe80c4b3db2f4e362042f3f9c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样就方便了内存的分配，不过缺点也很明显，新生代内存只能使用一半，但是它存放的是周期短的对象，这种对象一般很少，因此时间性能非常优秀。</p>
<ul>
<li>老生代的内存回收</li>
</ul>
<p>新生代内存中变量如果经过多次回收依然存在，就会放到老生代内存当中，这种现象叫做晋升。
发生晋升的原因：</p>
<ol>
<li>已经经历过一次Scavenge回收</li>
<li>To(闲置)空间的内存占比超过25%;</li>
</ol>
<p>老生代内存当中不能再使用Scavenge算法了，老生代积累的内存一般都是很大的，复制大量内存，浪费一半内存空间。</p>
<p>那么老生代怎样进行垃圾回收？</p>
<ol>
<li>标记清除，目前在<code>Javascript引擎</code>这种算法是最常用的，到目前为止的大多数浏览器的<code>Javascript引擎</code>都采用标记清除算法，只是不同的浏览器厂商对此算法做了不同的优化。</li>
</ol>
<p>整个标记清除算法大致过程就像下面这样：</p>
<ul>
<li>垃圾收集器在运行时会给内存中的所有变量都加上一个标记，假设内存中的所有对象都是垃圾，全标记为0</li>
<li>然后从各个根对象开始遍历，把不是垃圾的节点变为1</li>
<li>清理所有标记为0的垃圾，销毁并回收它们所占用的内存空间</li>
<li>最后，把所有内存中的对象标记修改为0，等待下一轮垃圾回收</li>
</ul>
<p>根对象，在浏览器中包括又不止于<code>全局window对象</code>,<code>文档DOM树</code>等；</p>
<ul>
<li>优点</li>
</ul>
<p>标记清除的优点只有一个，那就是实现比较简单，标记无非是打与不打两种，这使得一位二进制位(0和1)就可以为其标记，十分简单。</p>
<ul>
<li>缺点</li>
</ul>
<p>老生代内存同样存在<code>内存碎片</code>的问题，老生代怎么解决呢？</p>
<p>问题产生的原因，是因为垃圾清除之后剩余对象内存位置不变引发的问题。</p>
<p><strong>标记整理（Mark-Compact）算法</strong>就可以有效的解决，他的标记阶段和标记清除算法没什么不同，只是标记结束后，标记整理算法将活着的对象向内存的一端移动，最后清理掉边界的内存。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d785761f2644973842cf706624a42ba~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>增量标记</strong></p>
<p>标记清除算法是一种全停顿的垃圾回收方式，对于老生代大量内存来说，耗时过久，为了减少全停顿时间，在2011年，V8对老生代的标记进行了优化,全停顿变为增量标记。</p>
<p>什么是增量？
增量就是将一次性进行标记的任务，分为很多的小步，每个小步执行完之后，执行一会儿逻辑，这样交替就完成了一轮标记。
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14cd063892eb49fa86d78cfc3ebaf36b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>三色标记法(暂停与回复)</p>
<p>执行一会儿增量后，如果采用非黑即白的标记策略，暂停回复后该从哪开始执行，为了解决这个问题V8团队采用了一种特殊的方式：三色标记法</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ccbfc776adf49cdb3c7049c0194c38c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>白色是指未被标记的对象</li>
<li>灰色是指自身被标记，成员变量未被标记</li>
<li>黑色是指自身和成员变量皆被标记</li>
</ul>
<p>最开始都是白色，从一组根对象开始，先将根对象放入到标记列表中，并改变颜色为灰色，当对象的成员变量被标记后，自身变为黑色，无法到达的节点还是白色。</p>
<p>暂停过后恢复执行，直接找到灰色标记并接着往下执行标记就可以了。</p>
<p>三色标记法不需要每次都扫描整个内存空间，减少了全停顿时间。</p>
<p><strong>写屏障</strong></p>
<p>如果增量标记过程中，引用关系被修改怎么办？</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc6122da836940129537f9c1e06235fa~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>B不再引用C，而引用了D，因为C现在是黑色标记，是不会被清理，不过我们不用考虑这个，引用关系没有之后很快会被清理。D是白色，D将在清理阶段被回收，还有引用关系就被回收这肯定是不对的。</p>
<p>为了解决这个问题，V8增量回收采用<code>写屏障</code>的方法,<code>即出现黑色引用白色，强制把白色改为灰色</code>，从而保证下一次可以正确的标记，这个机制也叫做<code>强三色不变性</code>。</p>
<p><strong>惰性清理</strong></p>
<p>如果可用内存可以使我们流畅的运行代码，其实是没必要立即进行垃圾清理的，可以稍微延迟，也无需一次清理完所有内存，可以按需逐一清理直到所有的非活动对象内存被清理完毕，接着再执行增量标记。</p>
<p><strong>增量标记和惰性清理的优缺</strong></p>
<p>增量标记和惰性清理是主线程一次性停顿的时间大大减少，是程序运行更加流畅，但是总停顿时间并没有减少反而略有增加，三色标记法和写屏障无疑增加了运行成本，降低应用程序的吞吐量。</p>
<p><strong>并发回收</strong></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa17085fc85a4a709e61da1b7217f4b9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>它指的是在垃圾回收过程中，主线程不停顿，辅助线程在后台完成GC过程。这是并发回收的优点，同时这也是实现的难点，在主线程运行的过程中，堆内存的引用地址改变，进而引起一系列的改变，比如说标记，它需要额外实现一些读写锁机制来实现。</p>
<ol start="2">
<li>引用计数法</li>
</ol>
<p>这其实是最早的一种垃圾回收算法，他把<code>对象是否不再需要</code>简化定义为<code>对象有没有其它对象引用到它</code>，如果没有引用指向该对象(零引用),对象将被垃圾回收机制回收，目前很少使用这种算法了，因为它的问题很多，还是需要了解下</p>
<p>它的策略是跟踪记录每个变量值被使用的次数：</p>
<ul>
<li>当声明了一个变量并将一个引用类型赋值给该变量的时候这个值的引用次数就为1</li>
<li>同一个值又被赋给另一个变量，引用数加一</li>
<li>该变量的值被其它值覆盖了，则引用次数减一</li>
<li>当这个值的引用次数为0的时候，就说明这个值不再被需要了，垃圾回收器会在运行的时候回收掉引用次数为0的值占用的内存。</li>
</ul>
<pre><code class="copyable">let A = new Object();  // 对象的引用数为1
let B = A;             // 对象的引用数为2
let A = null;          // 对象的引用数减 1  对象的引用数为 1
let B = null;          // 对象的引用数减 1  对象的引用数为 0
···                    // 被回收
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种引用很容易遇到一个问题循环引用，例如</p>
<pre><code class="copyable">function gcTest()&#123;
    let A = new Object();
    let B = new Object();
    A.b = B;
    B.a = A;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>gcTest这个函数调用之后，A和B是要被清除的，但是按照引计数，引用数都是2，是无法完成清理的。按照标记清除的思路来看下，当函数结束后，gcTest这个函数不再被使用，里边的对象也会成为非活动对象，被清除掉。这也是后来放弃引用计数，使用标记清除的原因之一。</p>
<ul>
<li>优点</li>
</ul>
<p>对比标记清除算法可以看出来，当引用为0的时候，就可以立即回收。</p>
<p>标记清除算法需要每隔一段时间清理一次，这时候必须要暂停去执行，还要遍历根对象，而引用计数只需要在引用的时候计数就可以了。</p>
<ul>
<li>缺点</li>
</ul>
<p>首先需要一个计数器，这个计数器需要占用很大的位置，因为我们并不清楚引用数量的上限，还有就是循环应用无法回收的问题，这也是最严重的。</p>
<p>垃圾回收就说到这里了，基本上理解了垃圾的回收的方法以及为什么要进行垃圾回收，我想这才是最重要的。</p>
<h4 data-id="heading-4">内存泄漏</h4>
<h5 data-id="heading-5">什么是内存泄漏？</h5>
<p>当不再被使用的对象内存，没有被及时回收，这就是内存泄漏。</p>
<h5 data-id="heading-6">常见的内存泄漏</h5>
<h6 data-id="heading-7">1. 不正当的闭包</h6>
<pre><code class="copyable">function func1(params) &#123;
    let arr1 = new  Array(100).fill('张三');
    return function func2() &#123;

    &#125;
&#125;;
let resFunc1 = func1();

function func2(params) &#123;
    let arr2 = new  Array(100).fill('张三');
    return function func2() &#123;
        let name = arr2;
    &#125;
&#125;;
let resFunc2 = func2();
resFunc2();
resFunc2 = null;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>闭包resFunc1没有造成内存泄漏，resFunc1造成了内存泄漏，resFunc1中存在对arr2的引用，没有被回收，造成了内存泄漏，当resFunc2函数调用完成之后，resFunc2 = null,切断引用手动垃圾回收就可以了。</p>
<h6 data-id="heading-8">2. 隐式全局变量</h6>
<p>对于全局变量，垃圾回收机制很难判断什么时候去回收，通常不会回收它们，所以我们要避免额外全局变量的使用。</p>
<pre><code class="copyable">function func3(params) &#123;
    test = new  Array(100).fill('张三');
    this.test2 = new  Array(100).fill('张三');
&#125;;
func3();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>无意中全局增加了 test和test2两个全局变量，首先避免这种写法，使用</p>
<pre><code class="copyable">"use strict"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者就是及时清理全局变量中不再使用的和额外添加的变量。</p>
<h6 data-id="heading-9">3. 游离DOM引用</h6>
<p>觉得这个不常用，还是解释下，游离DOM，我理解的就是父节点被删除，但是自身还存在引用的节点，无法GC，需要手动把父节点和父节点的子节点全部置为null,才能GC。</p>
<h6 data-id="heading-10">4. 遗忘的定时器</h6>
<pre><code class="copyable">setInterval(() => &#123;
    this.$axios().then();
&#125;, 3000);  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>比如说每隔三秒更新一次数据，没有及时清除的情况下，定时器引用的变量之类会一直存在，不会被回收掉，setTimeout 和 cancelAnimationFrame同样存在这个问题，需要及时用 clearInterval 或者 clearTimeout 或者 cancelAnimationFrame 及时清除掉定时器</p>
<h6 data-id="heading-11">5. 遗忘的事件监听器</h6>
<pre><code class="copyable"><template>
    <div></div>
</template>
<script>
export default &#123;
    created()&#123;
        window.addEventListener('resize',this.func)
    &#125;,
    beforeDestroy()&#123;
        window.removeEventListener("resize", this.func)
    &#125;,
    methods:&#123;
        func()&#123;&#125;
    &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当事件监听器在组建内挂载事件处理函数，组件销毁时不主动将其清除时，其中引用的变量或者函数都被认为是需要的而不会进行回收，如果里边引用了大量的数据，比如说请求返回的数据，可能会引起页面内存占用过高，造成卡顿，甚至崩溃。</p>
<h6 data-id="heading-12">6. 遗忘的监听者模式</h6>
<pre><code class="copyable"><template>
    <div></div>
</template>

<script>
export default &#123;
    created() &#123;
        eventBus.on("listener", this.func)
    &#125;,
    beforeDestroy()&#123;
        eventBus.off("listener", this.func)
    &#125;,
    methods: &#123;
        func() &#123;
        // do something
        &#125;
    &#125;
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>和遗忘的事件监听器相同，在beforeDestroy勾子函数清除掉即可。</p>
<h6 data-id="heading-13">7. 遗忘的Map Sep对象</h6>
<p>当使用<code>Map</code>或者<code>Sep</code>存储对象时，都是对Object的强引用，需要主动清除引用。</p>
<p><code>WeakMap</code>对于键是弱引用，不会干扰GC，<code>WeakSet</code>也是如此。</p>
<pre><code class="copyable">//  obj 对 &#123;a :1&#125; 是强引用
let obj = &#123;a :1&#125;;

//  map 对 obj 是强引用
let map = new Map();
map.set(obj,1)

//  set 对 obj 是强引用
let set = new Set();
set.add(obj);

obj = null;
console.log(map.size); // 1
console.log(set.size); // 1
<span class="copy-code-btn">复制代码</span></code></pre>
<p>改为 <code>WeakSet WeakMap</code></p>
<pre><code class="copyable">    let obj = &#123;a :1&#125;;

    //  map 对 obj 是强引用
    let map = new WeakMap();
    map.set(obj,1)

    //  set 对 obj 是强引用
    let set = new WeakSet();
    set.add(obj);

    obj = null;
    console.log(map.size); // undefined
    console.log(set.size); // undefined
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如上所示，当使用<code>WeakSet WeakMap</code>后，map.size 和 set.size 打印为undefined,已经被清理掉了。</p>
<h6 data-id="heading-14">8. 未清理的console</h6>
<p>觉得这点比较容易理解吧，console.log()也是一个函数，</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83318f625c954f039c2793947c73bbc4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>函数传参都是值传递，对值的引用，会导致内存清除不掉，这应该会造成内存泄漏的。</p>
<h4 data-id="heading-15">总结：</h4>
<p>介绍了垃圾回收和内存泄漏，以后写代码的时候，也可以从容的避免这些坑，这个也算优化吧。</p>
<p>参考文章：</p>
<ul>
<li><a href="https://juejin.cn/post/6984188410659340324#heading-6" target="_blank" title="https://juejin.cn/post/6984188410659340324#heading-6">「硬核JS」你的程序中可能存在内存泄漏</a></li>
<li><a href="https://juejin.cn/post/6844903833387155464" target="_blank" title="https://juejin.cn/post/6844903833387155464">JavaScript中的垃圾回收和内存泄漏</a></li>
<li><a href="https://juejin.cn/post/6844904004007247880" target="_blank" title="https://juejin.cn/post/6844904004007247880">原生JS灵魂之问(下), 冲刺🚀进阶最后一公里(附个人成长经验分享)</a></li>
</ul></div>  
</div>
            