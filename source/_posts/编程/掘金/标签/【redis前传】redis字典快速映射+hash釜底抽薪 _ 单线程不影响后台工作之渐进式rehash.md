
---
title: '【redis前传】redis字典快速映射+hash釜底抽薪 _ 单线程不影响后台工作之渐进式rehash'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7039025c97e2478db47a6569ea5e890d~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 04 Jul 2021 14:52:02 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7039025c97e2478db47a6569ea5e890d~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>「本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战！</a>」</p>
<h1 data-id="heading-0">前言</h1>
<ul>
<li>
<p>相信你一定使用过新华字典吧！小时候不会读的字都是通过字典去查找的。在<code>Redis</code>中也存在相同功能叫做字典又称为符号表！是一种保存键值对的抽象数据结构</p>
</li>
<li>
<p>本篇仍然定位在【redis前传】系列中，因为本篇仍然是在解析redis数据结构！当你尝试去了解redis时才能明白其中原理！才能明白为什么redis被大家吹捧速度快，而不是被告知redis很快！</p>
</li>
</ul>
<h1 data-id="heading-1">应用场景</h1>
<ul>
<li>在Redis中有很多场景都是用了字典作为底层数据结构！我们使用最多的应该是redis的库的设置和五种基本数据类型的Hash结构数据！</li>
<li>在上一篇【redis前传】中我们学习了list数据结构。今天我们继续学习主流数据结构Hash。</li>
<li>在redis内部有字典结构、hash结构但是这里的hash和我们平时熟知的redis基础数据的hash并不是一个意思！我们简单的将字典结构、hash结构理解成redis更加底层的一种抽象结构。平时我们使用的hash基础数据结构理解成hash工具</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7039025c97e2478db47a6569ea5e890d~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210624161020745" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>而今天我们的主角就是五种数据结构的Hash分析。他的底层使用了字典这个结构。字典结构内部使用的是底层的hash结构。有点绕！好好理解你行的</li>
</ul>
<h1 data-id="heading-2">哈希表</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05b8af50b8de4848b6c65394b907fbef~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210624164553947" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>上面这张图诠释了作为redis底层结构的Hash。在内部redis称之为dictht  。 后面我们为什么和之前的hash结构冲突我们都已类名为准叫做dictht类。</li>
<li>在hictht类中有四个属性分别是table 、 size 、 sizemask 、 used  ; 其中table就是一个数组；数组中元素是另外一个类叫做dictEntry类。</li>
<li>dictEntry就是真正存储数据的。内部是key、value存储结构。一个简单的哈希表就如图所示。数据最终会存储在table中的dictEntry对象中。</li>
<li>至于为什么sizemask = size -1 ; 这个是为了在计算hash索引时需要用到的。那为什么不直接使用size-1而是通过一个变量来承接呢？这个吧！！！我也不知道。容我去百度百度。</li>
</ul>
<h1 data-id="heading-3">数组节点</h1>
<ul>
<li>上面的哈希表是不是很熟悉，这不和我们Java中的Map数据结构如出一辙吗。可以说是也可以说不是，两者很相似但也有区别的。</li>
<li>在上面中我们提到数据最终是存储在哈希表里table数组里的元素。该元素叫dictEntry 。 下面我们看看dictEntry结构如何吧！</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f718d9e83e5041e48b1f4bf110fec8c5~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210624165611646" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>通过左侧对dictEntry的定义我们可以看出。dictEntry存储的值可以是指针、正数、浮点数各种数据类型！类似于Java中的Object属性。  对于上述的key没有啥真意的就是一个键。</li>
<li>既然是数组那么索引就是固定长度的，那么在有限的长度中肯定会出现经典问题就是【hash冲突】。在Java中我们是通过链表和红黑树来解决冲突的问题！在redis中是通过链表解决的。在dictEntry中通过next指针将冲突元素连接。</li>
<li>这里我们就可以和Java中的Map结构进行理解。他们内部很是相似!!!</li>
<li>这里需要注意下在hash冲突时redis的确是通过链表进行存储的，但是由于哈希表(dictht)中没有记录每个索引未中链表的尾部节点只有头结点信息所以。而且我们也知道链表在查询上效率不佳，所以当发生哈希冲突时redis是将新加入的节点加入在链表的头部！</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b4450f6500f4db39453715ae00814f4~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210625113012772" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-4">字典</h1>
<h2 data-id="heading-5">多态字典</h2>
<ul>
<li>字典是本文开头提出的结构！也是redis中大量使用的一种底层数据结构。在redis中名叫做dict类。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a6b3729e129e434fb0f3a793074cdc91~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210625110556458" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>通过图示我们明确的看出内部是包含哈希表的。其实从名字上我们也可以看出哈希表为什么叫dictht 。 笔者这里认为是dicthashcodetable 。 意思就是字典表内部的一个hash相关的数组(仅个人理解)</li>
<li>之前也提到过redis内部很多地方会使用到字典！就好比我们上学是用到【新华字典】、【成语词典】、【歇后语词典】等等。虽然名字叫法不一样但是内部结构都是一部字典供我们快速定位。而redis中dict内部就是通过type字段进行区分每个字典的。而privdata是每部字典需要的特定参数。通过type和privdata就可以轻松实现各种功能不同的字典，他有个专有名词叫~~<em>多态字典</em>~~</li>
</ul>
<h2 data-id="heading-6">rehash</h2>
<ul>
<li>除了type 、 privdata以外剩下的就是ht 、 rehashidx了。其中ht是一个长度为2的数组。数组里元素就是我们之前提到了哈希表(dictht) 。 ht为什么长度为2 这就需要我们了解下redis的rehash过程了。而rehashidx就是记录rehash的进度！在没有发生rehash的时候rehashidx=-1;</li>
<li>在实际使用过程中在字典中我们所有的数据都会存储在ht[0]对应的哈希表中。ht[1]永远都是一个空数组。这些都是为什么rehash做准备，在正式开始之前我们先来了解下redis为什么需要rehash这个动作</li>
<li>首先我们在哈希表中是一个定长数组发生冲突时内部是通过链表解决的。理论上一个哈希表可以存储足够的数据，这里的足够就是指空间允许的范围有多少存多少。但是我们知道链表的特点就是新增、删除很快但是查询很慢，尤其是当链表很长的时候就会出现查询效率低下的问题！为了避免链表过长redis就会在一定条件下对哈希表中数组长度的扩展从而解决局部链表过长的问题！</li>
<li>每次数组发生长度变化时，那么之前的hash值就需要重新经历一遍hash然后寻址index的过程。这个过程就叫做<em>rehash</em> 。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf43de6c30284d9aa211435b46ceaa49~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210625133555602" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>关于rehash和Java中Map的resize是一样的功能！Java中resize是直接new 出一片内存进行复制的而且他是每次进行2倍扩展。而redis的rehash稍微不同基本上我们也可以理解成2倍扩展！关于两块内存复制有点类似于JVM中垃圾回收有点类似。有时间我们可以一起研究下JVM章节。</li>
<li>那么啥时候需要进行rehash呢？这里和Java的负载因子一样；但是除了负载因子这个空间考核以外redis还考虑一个性能的问题。因为在单线程的前提下我们还要考虑客户端使用的感知性！单线程的意思就是执行命令是顺序执行的。总不能在我们rehash的过程中全部阻塞客户端的使用这对于操作体验上稳定性来说是不友好的。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/946e6963a36940dbb7f5103c0fb2b502~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210625140300363" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>涉及到上述两个命令的我们称之为后台命令结合负载因子产生如下条件</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0cd386bbde324c6591c43cc5fe16919c~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210625140528097" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62380b2d36d946078b2320c5295b2e98~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210625142224557" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5eab424f54c6401c8a4c662a7027a3d8~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210625142326375" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">渐进式rehash</h2>
<ul>
<li>
<p>一直强调redis是单线程。那么什么叫单线程模型？就是对于redis服务来说执行命令是线性操作！但是每个客户端的命令是无序的，先到的就先进入队列redis服务从队列一次取出命令进行执行。除了客户端的命令还有一些系统生成的命令比如说我们上面提到的rehash操作！</p>
</li>
<li>
<p>①、首先为了避免阻塞客户端或者说尽量控制阻塞的时间在客户端感知范围内，redis内部的rehash并不是一次性操作而是一个循序渐进的过程。一次仅复制一部分</p>
</li>
<li>
<p>②、还记得之前我们提到dict中rehashidx这个属性吗，他是记录rehash的进度。因为哈希表内部是一个数组而rehashidx就是记录这个数组的索引。从而我们也可以知道每次rehash复制的时候是已一个索引完整链表为单元进行复制的。</p>
</li>
<li>
<p>③、除了新增以外的其他操作都会同时影响到ht[0]、ht[1] 因为在rehash过程中两个数组都是在使用状态的</p>
</li>
<li>
<p>④、新增值的时候就只需要新增到ht[1]中。因为最终的目的就是将所有值同步到ht[1]中。而ht[0]的值会慢慢的变少；没必要新增到ht[0]</p>
</li>
<li>
<p>⑤、在rehash过程中查找元素时会查找两个数组中的并集元素。这也就也是了为什么再rehash过程新增元素只需要新增到ht[1]的原因</p>
</li>
</ul>
<h1 data-id="heading-8">总结</h1>
<p>①、字典表在redis被广泛使用，基于字典表优秀的设计解决redis单线程问题</p>
<p>②、字典里包含哈希表，哈希表内部使用节点负责存储key、value</p>
<p>③、字典type实现多态字典用于多场景！</p>
<p>④、渐进式rehash解决服务卡顿问题</p></div>  
</div>
            