
---
title: '【redis前传】集思广益之quicklist，取其精华去其糟粕'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1bb8a11ba8d042b2aef4a426100295f1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 16:58:35 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1bb8a11ba8d042b2aef4a426100295f1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第2天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h1 data-id="heading-0">前言</h1>
<ul>
<li>在之前我们已经学习了redis五大数据结构中的list结构。其内部是linkedList和zipList两种结构。这是我们已经学习的内容。之前我没有结合操作具体查看。事实上在两者中还存在一种结合体quickList</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1bb8a11ba8d042b2aef4a426100295f1~tplv-k3u1fbpfcp-watermark.image" alt="image-20210715191310177" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">结构演变</h1>
<ul>
<li>在上面我们添加了一个key为zlist的数据。通过object encoding zlist查看底层就是通过quicklist来构建的。之前在ziplist章节汇总我们了解到在redis中hash和list基本数据结构都使用了ziplist存储数据的。在list中我们确实quicklist。这里我们提前说明下quicklist内部就是基于ziplist来实现的。</li>
</ul>
<h2 data-id="heading-2">linkedList</h2>
<ul>
<li>在开场quicklist之前我们简单梳理下之前学过的linkedList ，他是一种常见的<a href="https://link.juejin.cn/?target=%25E5%25BE%2585%25E8%25A1%25A5%25E5%2585%2585" target="_blank" title="%E5%BE%85%E8%A1%A5%E5%85%85" ref="nofollow noopener noreferrer">双线链表</a>。通过两个指针完成我们链表的构建。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22d9ee5372f6455992e98ce9a53fe467~tplv-k3u1fbpfcp-watermark.image" alt="image-20210723133046693" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">C++指针</h2>
<ul>
<li>redis是基于内存运行的，而内存有十分的宝贵所以redis在设计了双线链表后觉得有点耗内存。因为指针本身也是需要开辟空间的。根据系统的不同指针占位不同。这里我总结了一下一个指针占位就是一个系统操作的基本位</li>
<li>这里基本位是什么意思呢？加入你是64位系统那么一个指针就是64位即8个字节。如果你是32位系统那么一个指针就是32位即4个字节</li>
<li>也就是说如果我在redis中向双向链表中存储N个英文字母，我们又知道一个应为字母占1个字节。那么这N个元素就是N的listNode  . 那么维持着N个listNode中间就需要2*(N-1)个指针。在64位系统中也就是我们需要开辟将近129倍的空间来存储内容。上述情况我们只有N个字节的内容，却需要<code>2*(N-1)*8+N</code>个字节来构建listNode。</li>
<li>随着节点的递增我们浪费程度越离谱。所以redis在双向链表的基础上结合了ziplist进行改良。</li>
</ul>
<h2 data-id="heading-4">过渡原因</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/436f2c0c0efa4599b10bfe3e590a0c9c~tplv-k3u1fbpfcp-watermark.image" alt="image-20210723133853290" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">ziplist</h2>
<ul>
<li>在ziplist章节中我们知道ziplist是一块连续内存，是redis对内存的一种改良结构。ziplist实现了内存的高使用率！</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5cab76642b3f4818a140450c38f750f0~tplv-k3u1fbpfcp-watermark.image" alt="image-20210723134013816" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">linkedlist+ziplist好处</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e3958b7c29c44528409fea2c648dc61~tplv-k3u1fbpfcp-watermark.image" alt="image-20210723134105776" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-7">quicklist引入</h1>
<ul>
<li>quicklist是在redis3.2之后引入的，笔者这里使用的是redis6.4方便源码好像并没有quicklist源码。</li>
<li>后来翻阅了之后redis6.4好像取消了quicklist . 结构。所以我又特别下了一个3.2的版本。这里具体的是redis3.2.4版本！！！</li>
</ul>
<h1 data-id="heading-8">庐山真面目</h1>
<h2 data-id="heading-9">quicklist</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ccff14e6dc8546ba8ca034db3599ce3f~tplv-k3u1fbpfcp-watermark.image" alt="image-20210723134438938" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>通过他的源码我们很清晰的看出他的内部数据结构！这个大家应该很熟悉了。quicklist可以说就是我们之前的linkedList 结构。内部就是双向链表只不过里面的属性稍微多了点</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2043b72823b34ce6b5460b61299acefe~tplv-k3u1fbpfcp-watermark.image" alt="image-20210723134617683" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>通过图示是不是感觉和linkedList一样。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b69281f26c8341b283ca395dce605745~tplv-k3u1fbpfcp-watermark.image" alt="image-20210723134817146" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>接下来我们看看quicklist中各个属性的含义吧</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/748f9978afff4a0a887fb61d300a9c38~tplv-k3u1fbpfcp-watermark.image" alt="image-20210723134859582" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">quicklistNode</h2>
<ul>
<li>quicklist只是一个抽象的概念，真正负责数据的存储的是组成quicklist的成员quicklistNode 。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/060fad3370a844a49b0acabe9a429e7f~tplv-k3u1fbpfcp-watermark.image" alt="image-20210723135204092" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>各个属性的作用</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5aada038309e4fc9971d69561cbc2867~tplv-k3u1fbpfcp-watermark.image" alt="image-20210723135327554" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>通过上面的属性介绍，我们也可以了解了解到node节点中的数据结构就是ziplist 。在ziplist基础上会在进行压缩达到内存更高的使用效率！</p>
</li>
<li>
<p>关于压缩这里我们不用太去了解！主要目的就是一种编码，这种编码是无法真正使用的在使用期间redis会进行解码操作。在解码操作期间就是通过recompress属性来标记的。</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b42fc52c91441c1bf844e1c6b70e382~tplv-k3u1fbpfcp-watermark.image" alt="image-20210723135734482" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-11">insert</h1>
<ul>
<li>在了解quicklist基本结构之后我们在看看insert时结构会发生哪些变化！上面我们也提到了在redis.conf配置文件中<code>list-max-ziplist-size</code>属性是用来设置quicklist中每个节点中的ziplist存储的大小设置的。</li>
</ul>

































<table><thead><tr><th>属性值</th><th>作用</th></tr></thead><tbody><tr><td>-1</td><td>每个quicklistNode节点的ziplist所占字节数不能超过4kb</td></tr><tr><td>-2</td><td>每个quicklistNode节点的ziplist所占字节数不能超过8kb</td></tr><tr><td>-3</td><td>每个quicklistNode节点的ziplist所占字节数不能超过16kb</td></tr><tr><td>-4</td><td>每个quicklistNode节点的ziplist所占字节数不能超过32kb</td></tr><tr><td>-5</td><td>每个quicklistNode节点的ziplist所占字节数不能超过64kb</td></tr><tr><td>int</td><td>ziplist包含的entry上限</td></tr></tbody></table>
<h3 data-id="heading-12">两端插入</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/362bc2cdd78f40bc8f5bbb9392ec67a2~tplv-k3u1fbpfcp-watermark.image" alt="image-20210723140744723" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>第一种情况就是我们需要插入的数据是在两端的。如上图所示我们在redis.conf配置文件中设置的<code>list-max-ziplist-size: 2</code> 。表示内部节点ziplist中entry个数最大为2  。此时我们head头部节点中已经存储了两个内容，tail尾部节点存储的是1个节点！</li>
<li>这个时候如果我们想头部添加一个元素是obj1 。 可想而知我们是无法加入的，这个时候redis会重新创建一个ziplist结构并包含obj1 ，将新创建的ziplist加入到链表的头部之后</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c558b847cc244162bfec7db5b995f259~tplv-k3u1fbpfcp-watermark.image" alt="image-20210723141323765" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>而obj2加入尾结点时，因为尾结点的节点数是1还未达到峰值2，所以直接就加入了。最终的效果图如下</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3afc9a3e1afb416590428f4f7f26d72a~tplv-k3u1fbpfcp-watermark.image" alt="image-20210723141540152" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">中间插入</h3>
<pre><code class="hljs language-flow copyable" lang="flow">st=>start: Insert
ziplistInsert=>operation: 向ziplist中插入
subziplistInsert=>operation: 将该ziplist拆分两个ziplist， 在对应位置加入
insertNear=>operation: 插入相邻的ziplist中
newZipInsert=>operation: 新建ziplist插入
cond=>condition: ziplist是否可以容纳
headtailCond=>condition: 插入位置在ziplist两端
nearheadtailCond=>condition: 相邻ziplist是否可以容纳
e=>end: 快乐的一天

st->cond
cond(yes)->ziplistInsert
cond(no)->headtailCond(yes)->nearheadtailCond
headtailCond(no)->subziplistInsert
nearheadtailCond(yes)->insertNear
nearheadtailCond(no)->newZipInsert
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-14">总结</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a9a07e0334c4772aa302e2041922c26~tplv-k3u1fbpfcp-watermark.image" alt="image-20210723144626592" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-15">参考文献</h3>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fyitouhan%2Farticle%2Fdetails%2F108035859" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/yitouhan/article/details/108035859" ref="nofollow noopener noreferrer">lzf压缩算法</a></p></div>  
</div>
            