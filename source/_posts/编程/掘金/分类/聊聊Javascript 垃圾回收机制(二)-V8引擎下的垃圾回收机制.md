
---
title: '聊聊Javascript 垃圾回收机制(二)-V8引擎下的垃圾回收机制'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9754'
author: 掘金
comments: false
date: Sat, 20 Mar 2021 07:14:09 GMT
thumbnail: 'https://picsum.photos/400/300?random=9754'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">引子 从修真故事说起</h1>
<p>上文大概介绍了垃圾回收的机制和标记清除法的核心思路， 接下来准备深入介绍下v8引擎里的垃圾回收算法。 既然是算法类的介绍，那自然是比较枯燥的，如果想完全弄懂，可以收藏下来，多看几遍（!·_·!）。</p>
<p>为了缓解一下讲解的枯燥，我觉得可以先从一个比较有意思的话题来引入。 相信大家都看过一些修真玄幻的小说， 渡劫和飞升就是里面常见的桥段，现在来给大家讲个故事：</p>
<p><strong>初始大陆</strong>上有很多普通的修真者在修仙，随着时间推移，人数越来越多，最终到达了这个大陆的承受极限，此时天道必然要出手掌握平衡， 从中选拔留下一下能通过考验的优秀之人，清除掉剩下的修为低下之人，从而腾出大陆空间； 天道选拔的方式是：</p>
<ul>
<li>将这些人挪移到渡劫空间里， 然后开始一场<strong>小天劫</strong>，等到小天劫结束后，再把活下来的人送回大陆空间，没有渡过的人就会被清除，身死道消；</li>
<li>循环往复，只要每次人数达到大陆空间上限，都会进行一次小天劫，</li>
</ul>
<p>那么这之中就会有度过数次天劫的佼佼者， 天道会奖励他<strong>飞升</strong>到更高级、更广阔的<strong>远古大陆</strong>去，踏上更高一级的修炼路程，但是我们知道，修仙之路是逆天之路，<strong>更高级的地方自然也有更高级的劫数</strong>，远古大陆虽然更加辽阔，远胜于初始大陆，但是每隔一定的时间，也会触发一次更大级别的<strong>大天劫</strong>， 清理这个大陆上的修真者。</p>
<p>大部分的修真者生命是短暂的，熬不过一两次<strong>小天劫</strong>，只有少数的修真者能够脱颖而出，飞升到远古大陆。</p>
<p>故事暂时就讲到这里，接下来就是正题。</p>
<h2 data-id="heading-1">堆结构的划分</h2>
<p>在聊垃圾回收之前，要先了解下v8引擎对于堆结构的划分：</p>
<ol>
<li>新空间(New-space)：大多数对象都分配在这里。 新空间很小，并且被设计为可以非常快速地进行垃圾回收，而与其他空间无关。其实这个新生空间对应的，就是前文的<strong>初始大陆</strong></li>
<li>旧指针空间（Old-pointer-space）：包含大多数对象，这些对象可能具有指向其他对象的指针。 在新空间中生存了一段时间后，大多数对象都移到了这里。（特例也可以先不管）</li>
<li>旧数据空间（Old-data-space）：包含仅包含原始数据的对象（没有指向其他对象的指针）。 在新空间中存活了一段时间后，字符串，装箱的数字和未装箱的双精度数组会移到此处。<strong>旧指针空间和旧数据空间合起来就称为旧空间，就对应前文的远古大陆。</strong></li>
<li>大对象空间：此空间包含的对象大于其他空间的大小限制。 大对象永远不会被垃圾收集器移动。（可以先不管）</li>
<li>代码空间：此处分配了包含JIT指令的代码对象。 这是唯一具有可执行内存的空间（尽管可以在大对象空间中分配代码，并且这些代码也是可执行的。（可以先不管）</li>
</ol>
<p>介绍到这里，相信有些同学已经可以对应出一部分内容了，接着往下看（主要先记住前面3个空间就好，后面会一直用到）：</p>
<h2 data-id="heading-2">分代回收机制(Generational collection)</h2>
<p>在大部分小说设定里，普通修真者的生命总是短暂的，能脱颖而出的万中无一。 在大部分程序里，对象数据的生命也是短暂的，只有少部分数据对象会长期存活。所以根据这种情况，v8引擎设计了分代回收的方式 -- 也就是前面提到的：<strong>天劫分一大一小两类，小天劫发生频繁，清扫新生和普通的修真者，只在初始大陆发生；大天劫间隔更久，清理远古大陆的修真者，他们分别发生在不同的空间，共同完成垃圾回收任务。</strong></p>
<p>整体配合机制如下：</p>
<ol>
<li>在<strong>新空间</strong>分配新对象，直到空间充满，就触发<strong>小型回收机制</strong>；</li>
<li>在小型回收机制中存活下2次的对象，就会被移动到旧空间去（根据数据特点分配到旧指针空间或者旧数据空间）；</li>
<li>旧数据空间内存达到一定值的时候（这个阈值具体的参数先不用关注），触发<strong>大型回收机制</strong>（major garbage collection）；</li>
</ol>
<p>（可以再去回头读读前面的故事  是不是基本全对上了！）</p>
<p>接下来我们来分别介绍这两种机制。</p>
<h3 data-id="heading-3">小型回收机制 scavenge</h3>
<p>小型回收机制，官方名称是scavenge， 它发生概率频繁，所以要求速度要比较快。基本算法思路源于著名的<a href="https://en.wikipedia.org/wiki/Cheney's_algorithm?fileGuid=6HypxjRPDVxvcCHg" target="_blank" rel="nofollow noopener noreferrer">Cheney算法</a>，思路如下:</p>
<ol>
<li>把新空间<code>(new-space)</code>均分为两部分，命名为from空间和to空间；（这两个空间不会同时使用）</li>
<li>前面说的新对象的分配 是在to空间进行的，直到填满to空间为止；</li>
<li>此时交换<code>from</code>空间和<code>to</code>空间，也就是把to空间的所有对象都移动到<code>from</code>空间，这一步执行完后，<code>to</code>空间变成空的，<code>from</code>是满的；</li>
<li>在<code>from</code>空间，从<code>root</code>开始寻找所有可访问对象（这是上一篇的内容了，忘记了可以去回顾一下），然后把这些对象都移动到<code>to</code>空间或者<code>old</code>空间（某些已经挨过两次的就应该飞升了），这一步其实<code>v8</code>引擎还会顺便做一下压实（compacted）,也就是把存活的对象位置稍微集中一下，增加一下缓存的局部性，保持分配快速而简单；</li>
<li>清空<code>from</code>空间（筛选剩下的都是可回收的了）；</li>
</ol>
<p>第一次接触这个算法的读者可能稍微有点绕，也会疑惑为什么不直接在<code>to</code>空间满了的时候就直接清理垃圾，保留<code>live</code>对象(也就是可访问对象)，反而要移来移去的；其实多看两遍就很好理解了，这样设计的好处在于<code>to</code>空间永远作为实际的内存分配空间，<code>from</code>充当的只是一个临时容器，也就是<strong>渡劫的空间</strong>，两者不需要同时使用，这样非常清晰。官方还贴了一份伪代码:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">def scavenge():
  swap(fromSpace, toSpace)
  allocationPtr = toSpace.bottom
  scanPtr = toSpace.bottom
  <span class="hljs-keyword">for</span> i = <span class="hljs-number">0.</span>.len(roots):
    root = roots[i]
    <span class="hljs-keyword">if</span> inFromSpace(root):
      rootCopy = copyObject(&allocationPtr, root)
      setForwardingAddress(root, rootCopy)
      roots[i] = rootCopy
  <span class="hljs-keyword">while</span> scanPtr < allocationPtr:
    obj = object at scanPtr
    scanPtr += size(obj)
    n = sizeInWords(obj)
    <span class="hljs-keyword">for</span> i = <span class="hljs-number">0.</span>.n:
      <span class="hljs-keyword">if</span> isPointer(obj[i]) and not inOldSpace(obj[i]):
        fromNeighbor = obj[i]
        <span class="hljs-keyword">if</span> hasForwardingAddress(fromNeighbor):
          toNeighbor = getForwardingAddress(fromNeighbor)
        <span class="hljs-attr">else</span>:
          toNeighbor = copyObject(&allocationPtr, fromNeighbor)
          setForwardingAddress(fromNeighbor, toNeighbor)
        obj[i] = toNeighbor
def copyObject(*allocationPtr, object):
  copy = *allocationPtr
  *allocationPtr += size(object)
  memcpy(copy, object, size(object))
  <span class="hljs-keyword">return</span> copy
<span class="copy-code-btn">复制代码</span></code></pre>
<p>代码自然看起来枯燥一些，适合有兴趣的读者后面慢慢研究，第一遍阅读完全可以略过，因为思路都已经讲完了，缺的只是一些具体的实现。</p>
<p>这里有个小细节，我们刚刚说到，回收的起始点是<code>root</code>对象，也就是全局对象以及所有它可以访问到的对象（包括闭包等）。那么<strong>如果某个对象只是被已经飞升到旧空间的数据对象引用了那么办呢？</strong> 按照我们这种清理方式，如果我们不把旧空间扫描一遍来排查这样的特殊情况，就会把这个对象给误清理掉；如果我们真的这么做，那成本就抬高了,因为我们说过小型清理的发生频率非常高，所以不可能每次都还去扫描旧空间。</p>
<p><strong>所以，为了解决这个问题，v8引擎在内存里维护了一个缓冲区，每当新<code>(new-space)</code>空间的对象被旧<code>(old-space)</code>空间的对象引用时， 这个旧空间对象的<code>key</code>将会被记录下来，例如:</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> user1 = &#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'leo'</span>&#125;;
<span class="hljs-comment">// ...这里省略一些代码， 假定经历了一段时间并且user1被移动到old空间之后</span>
use1.friend = &#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'john'</span>&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个例子中，我们假设<code>use1</code>经过一段时间后进入了旧空间，然后<code>&#123;name: 'john'&#125;</code>被新分配到新空间，并且只有<code>user1</code>保留了对它的引用，此时这个<code>key</code>，也就是<code>friend</code>的内存位置会被记录到缓冲区里，后面会专门检测这种情况，防止误杀。
这个虽然需要额外花费一些代价，但是是为了达到回收效果必须要付出的成本，而且实际这种情景的频率并没有想象的高。</p>
<h3 data-id="heading-4">大型回收机制</h3>
<p>小型回收机制<code>Scavenge</code>比较适合小区域的清理，因为它需要交换内存空间，有比较多内存开销，因为新空间比较小，所以这样做是没问题的， 对于要大的多的旧空间，就要用大型回收机制。</p>
<p>大型回收机制指的就是我们前文说的标记-清除法，实际上包含分成<strong>标记-清除</strong>和<strong>标记-压实</strong>（压实的概念前面也说过了）两种。他们都是分2个阶段来运行的：</p>
<ul>
<li><strong>标记</strong>阶段：本质上就是一场深度优先搜索：有三种颜色的标记（白色-初始状态，黑色-已检查状态；灰色-待检查状态）；
<ol>
<li>首先将所有的对象设置为<strong>白色</strong>，然后从root对象出发，将所有可以访问的对象标记为<strong>灰色</strong>。并用一个数组缓存起来；</li>
<li>然后遍历该数组，每次都把要遍历的对象<strong>涂成黑色并移出</strong>，并且把他的相邻节点都涂成<strong>灰色</strong>，并放入队列，直到队列为空</li>
<li>继续检查是否有<strong>灰色对象，如果有继续放入队列然后循环, 直到所有的可访问对象都变成黑色。</strong></li>
</ol>
</li>
</ul>
<p>这一段看起来虽然有点绕，但是实质上就是深度遍历有向图，比较基础，所以就不画流程图了。 经过标记以后，所有的对象就只剩下黑色和白色了，其中白色的就是可清理垃圾对象。</p>
<ul>
<li>**清除（或压实）**阶段：清除算法比较简单，根据上一步的查找结果，把对应白色标记对象内存地址转为自由空间； 压实算法相对复杂一些，核心的思路是把对象从比较分散的内存地址，集体迁移到其他某一块连续的内存地址里面，一般是另外选取一个连续内存块，然后把对象复制过去，并且在源对象上留下一个转发地址，在迁移过程中，记录下相关的指针位置，在完成整个迁移之后，更新指针指向新位置， 如果遇到某一块内存地址由于太多对象都要迁移过去，导致无法全部迁移，那么会等到下一个大回收周期再继续迁移。</li>
</ul>
<p>好了 到这里，核心内容基本就介绍完了，可以稍作休息。</p>
<h2 data-id="heading-5">v8引擎的优化机制-增量标记和延迟清除</h2>
<p>遇到大量的实时数据处理时，标记清除（或压实）法会很耗时，所以Google提出了两项改进方案：增量标记和延迟清除。</p>
<h3 data-id="heading-6"><strong>增量标记</strong>：</h3>
<p>这个其实蛮好理解的，因为前文讲到的标记清除算法可能一次做完需要很长的时间，<strong>这个期间是****需要暂停程序的</strong>，所以v8允许设定一个阈值，例如每次标记一定数量（比如100个）的对象，就先回去执行程序，然后再回来继续标记，也就是<strong>在程序运行过程穿插垃圾回收，从而降低最大暂停时间。</strong></p>
<p>但是这个方法有个问题： 假如我第一次已经把一些对象标记过了，但是返回垃圾回收过程时，<strong>有些对象被修改了！</strong></p>
<p>例如前面标记为黑色的对象，在返回执行程序过程，增加了一个指向已经被标记为白色对象的指针，这就会导致直接继续执行标记会误杀这个白色对象（因为后来它实际上变成可访问的了），怎么办呢？</p>
<p>很简单，还记不记得小回收阶段，<strong>v8引擎在内存里维护了一个缓冲区，解决new空间的对象被old空间的对象引用的方法？ 同样的，他也会记录这种从黑色对象到白色对象的指针，并且之后把这样的黑色对象再变成灰色，重新检查，这样问题就解决了。</strong></p>
<h3 data-id="heading-7"><strong>延迟清除</strong>：</h3>
<p>这个也很简单，在标记之后，引擎清楚直到哪些是可以清除的对象，但是并不代表需要同时清除掉这些垃圾，所以引擎选择<strong>按需清理，优先从需要的页面开始，逐步清理所有的页面垃圾，然后就算就完成了一整个垃圾回收周期。</strong></p>
<h1 data-id="heading-8">总结</h1>
<p>本文在前一节的基础上，深入分析了v8引擎的垃圾回收机制，</p>
<ul>
<li>从大的方面来说，分成小回收周期和大的回收周期</li>
<li>小回收周期发生在新空间，频率高，时间短速度快，运用chenny算法</li>
<li>大回收周期发生在旧空间，频率低，速度慢，用深度优先遍历和三色标记法（黑白灰）</li>
<li>优化方式主要是增量标记和延迟清理，核心思路是碎片化标记阶段和优先按需清理空间</li>
</ul>
<p>好了，关于垃圾回收的内容，大概就说到这里， 本文相对前一篇文章稍微枯燥一些，而且没有画图来说明过程（问就是懒得画-_-），但是多看几遍还是挺好理解的，而且已经去掉了关于内存位图之类更底层的东西方便理解核心思路，想钻研更底层内容的同学可以看后面详细的参考文章。</p>
<p><strong>惯例：如果内容有错误的地方欢迎指出（觉得看着不理解不舒服想吐槽也完全没问题）；如果有帮助，欢迎点赞和收藏，转载请征得同意后著明出处，如果有问题也欢迎私信交流，主页有邮箱地址</strong></p>
<p>顺便再说下，RingCentral目前在杭州也设置了办公点，而且可以申请长期远程办公，告别996，平衡工作生活，有兴趣的同学可以私信或者发邮件给我，可以免费帮忙内推~</p>
<h1 data-id="heading-9">参考文章</h1>
<p><a href="http://jayconrod.com/posts/55/a-tour-of-v8-garbage-collection?fileGuid=6HypxjRPDVxvcCHg" target="_blank" rel="nofollow noopener noreferrer">jayconrod.com/posts/55/a-…</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            