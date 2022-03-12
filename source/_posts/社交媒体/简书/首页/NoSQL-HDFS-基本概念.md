
---
title: 'NoSQL-HDFS-基本概念'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/2636642-752b1f7e77131eee.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/2636642-752b1f7e77131eee.png'
---

<div>   
<p>Hadoop</p>
<ul>
<li>Map-Reduce</li>
<li>HDFS</li>
</ul>
<h1>正文</h1>
<h2>分布式文件系统</h2>
<p>文件系统：文件系统是用来存储和管理文件，并且提供文件的查询、增加、删除等操作。<br>
直观上的体验：在shell窗口输入<code>ls</code>命令，就可以看到当前目录下的文件夹、文件。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="423" data-height="200"><img data-original-src="//upload-images.jianshu.io/upload_images/2636642-752b1f7e77131eee.png" data-original-width="423" data-original-height="200" data-original-format="image/png" data-original-filesize="114488" src="https://upload-images.jianshu.io/upload_images/2636642-752b1f7e77131eee.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<p>文件存储在哪里？硬盘<br>
一台只有250G硬盘的电脑，如果需要存储500G的文件可以怎么办？先将电脑硬盘扩容至少250G，再将文件分割成多块，放到多块硬盘上储存。</p>
<p>通过<code>hdfs dfs -ls</code>命令可以查看分布式文件系统中的文件，就像本地的ls命令一样。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="395" data-height="128"><img data-original-src="//upload-images.jianshu.io/upload_images/2636642-eb920bfd998d3ce0.png" data-original-width="395" data-original-height="128" data-original-format="image/png" data-original-filesize="60392" src="https://upload-images.jianshu.io/upload_images/2636642-eb920bfd998d3ce0.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<p>HDFS在客户端上提供了查询、新增和删除的指令，可以实现将分布在多台机器上的文件系统进行统一的管理。</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="400" data-height="251"><img data-original-src="//upload-images.jianshu.io/upload_images/2636642-afc278e0b4ead83a.png" data-original-width="400" data-original-height="251" data-original-format="image/png" data-original-filesize="96065" src="https://upload-images.jianshu.io/upload_images/2636642-afc278e0b4ead83a.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<h2>文件切块</h2>
<p>在分布式文件系统中，一个大文件会被切分成块，分别存储到几台机器上。结合上文中提到的那个存储500G大文件的那个例子，这500G的文件会按照一定的大小被切分成若干块，然后分别存储在若干台机器上，然后提供统一的操作接口。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="416" data-height="182"><img data-original-src="//upload-images.jianshu.io/upload_images/2636642-206c0e24f3273f4c.png" data-original-width="416" data-original-height="182" data-original-format="image/png" data-original-filesize="45302" src="https://upload-images.jianshu.io/upload_images/2636642-206c0e24f3273f4c.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<p>看到这里，不少人可能会觉得，分布式文件系统不过如此，很简单嘛。事实真的是这样的么？</p>
<p><strong>潜在问题</strong></p>
<blockquote>
<p>如果要查找一个文件，如何快速地知道这个文件在哪台机器上？</p>
</blockquote>
<p>假如我有一个1000台机器组成的分布式系统，一台机器每天出现故障的概率是0.1%，那么整个系统每天出现故障的概率是多大呢？答案是(1-0.1%)^1000=63%，因此需要提供一个容错机制来保证发生差错时文件依然可以读出，这里暂时先不展开介绍。</p>
<p>如果要存储PB级或者EB级的数据，成千上万台机器组成的集群是很常见的，所以说分布式系统比单机系统要复杂得多呀。</p>
<h2>HDFS的架构</h2>
<p>这是一张HDFS的架构简图：</p>
<ul>
<li>DataNode是真正存储数据的地方，</li>
<li>NameNode相当于一个管理者master，它知道每一个DataNode的存储情况，</li>
<li>client其实就是那个对外操作的统一接口。</li>
</ul>
<p>client通过nameNode了解数据在哪些DataNode上，从而发起查询。此外，不仅是查询文件，写入文件的时候也是先去请教NameNode，看看应该往哪个DateNode中去写。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="411" data-height="160"><img data-original-src="//upload-images.jianshu.io/upload_images/2636642-6fd5eb86b7dbf24e.png" data-original-width="411" data-original-height="160" data-original-format="image/png" data-original-filesize="32253" src="https://upload-images.jianshu.io/upload_images/2636642-6fd5eb86b7dbf24e.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<p>为了某一份数据只写入到一个Datanode中，而这个Datanode因为某些原因出错无法读取的问题，需要通过冗余备份的方式来进行容错处理。因此，HDFS在写入一个数据块的时候，不会仅仅写入一个DataNode，而是会写入到多个DataNode中，这样，如果其中一个DataNode坏了，还可以从其余的DataNode中拿到数据，保证了数据不丢失。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="450" data-height="161"><img data-original-src="//upload-images.jianshu.io/upload_images/2636642-fd6a091b02ff96d1.png" data-original-width="450" data-original-height="161" data-original-format="image/png" data-original-filesize="37069" src="https://upload-images.jianshu.io/upload_images/2636642-fd6a091b02ff96d1.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<p>实际上，每个数据块在HDFS上都会保存多份，保存在不同的DataNode上。这种是牺牲一定存储空间换取可靠性的做法。</p>
<h2>HDFS读写流程</h2>
<p>接下来我们来看一下完整的文件写入的流程：</p>
<p>大文件要写入HDFS，client端根据配置将大文件分成固定大小的块，然后再上传到HDFS。</p>
<br>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="386" data-height="239"><img data-original-src="//upload-images.jianshu.io/upload_images/2636642-d66eebfbe4906437.png" data-original-width="386" data-original-height="239" data-original-format="image/png" data-original-filesize="49295" src="https://upload-images.jianshu.io/upload_images/2636642-d66eebfbe4906437.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<p>读取文件的流程：</p>
<p>1、client询问NameNode，我要读取某个路径下的文件，麻烦告诉我这个文件都在哪些DataNode上？<br>
2、NameNode回复client，这个路径下的文件被切成了3块，分别在DataNode1、DataNode3和DataNode4上<br>
3、client去找DataNode1、DataNode3和DataNode4，拿到3个文件块，通过stream读取并且整合起来</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="464" data-height="437"><img data-original-src="//upload-images.jianshu.io/upload_images/2636642-8deaa4261ee5b5ab.png" data-original-width="464" data-original-height="437" data-original-format="image/png" data-original-filesize="134992" src="https://upload-images.jianshu.io/upload_images/2636642-8deaa4261ee5b5ab.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<p>文件写入的流程：<br>
1、client先将文件分块，然后询问NameNode，我要写入一个文件到某个路径下，文件有3块，应该怎么写？<br>
2、NameNode回复client，可以分别写到DataNode1、DataNode2、DataNode3、DataNode4上，记住，每个块重复写3份，总共是9份<br>
3、client找到DataNode1、DataNode2、DataNode3、DataNode4，把数据写到他们上面</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="439" data-height="435"><img data-original-src="//upload-images.jianshu.io/upload_images/2636642-323600f2d3d288de.png" data-original-width="439" data-original-height="435" data-original-format="image/png" data-original-filesize="117951" src="https://upload-images.jianshu.io/upload_images/2636642-323600f2d3d288de.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<p>出于容错的考虑，每个数据块有3个备份，但是3个备份快都直接由client端直接写入势必会带来client端过重的写入压力，这个点是否有更好的解决方案呢？回忆一下mysql主备之间是通过binlog文件进行同步的，HDFS当然也可以借鉴这个思想，数据其实只需要写入到一个datanode上，然后由datanode之间相互进行备份同步，减少了client端的写入压力，那么至于是一个datanode写入成功即成功，还是需要所有的参与备份的datanode返回写入成功才算成功，是可靠性配置的策略，当然这个设置会影响到数据写入的吞吐率，我们可以看到可靠性和效率永远是“鱼和熊掌不可兼得”的。</p>
<p><strong>潜在问题</strong></p>
<blockquote>
<p>如果NameNode运行了很久，文件操作很多的话，操作记录日志文件editlog就会很大吧？那么下次NameNode重启的时候，需要进行大量操作的恢复，启动时间就会非常长。</p>
</blockquote>
<p>NameNode确实会回放editlog，但是不是每次都从头回放，它会先加载一个fsimage，这个文件是之前某一个时刻整个NameNode的文件元数据的内存快照，然后再在这个基础上回放editlog，完成后，会清空editlog，再把当前文件元数据的内存状态写入fsimage，方便下一次加载。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="383" data-height="521"><img data-original-src="//upload-images.jianshu.io/upload_images/2636642-1a9777aaf0abbf3c.png" data-original-width="383" data-original-height="521" data-original-format="image/png" data-original-filesize="126300" src="https://upload-images.jianshu.io/upload_images/2636642-1a9777aaf0abbf3c.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<p>这样，全量回放就变成了增量回放，但是如果NameNode长时间未重启过，editlog依然会比较大，恢复的时间依然比较长，这个问题怎么解呢？</p>
<p>SecondNameNode是一个NameNode内的定时任务线程，它会定期地将editlog写入fsimage，然后情况原来的editlog，从而保证editlog的文件大小维持在一定大小。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="405" data-height="679"><img data-original-src="//upload-images.jianshu.io/upload_images/2636642-f0a7ee1f3fd2bbc2.png" data-original-width="405" data-original-height="679" data-original-format="image/png" data-original-filesize="159260" src="https://upload-images.jianshu.io/upload_images/2636642-f0a7ee1f3fd2bbc2.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<h2>HDFS的高可用保障</h2>
<blockquote>
<p>NameNode对于hdfs来说是非常重要的，假如NameNode挂了，谁来接替它的工作呢？是SecondNameNode吗？</p>
</blockquote>
<p>NameNode挂了， SecondNameNode并不能替代NameNode，所以如果集群中只有一个NameNode，它挂了，整个系统就挂了。hadoop2.x之前，整个集群只能有一个NameNode，是有可能发生单点故障的，所以hadoop1.x有本身的不稳定性。但是hadoop2.x之后，我们可以在集群中配置多个NameNode，就不会有这个问题了，但是配置多个NameNode，需要注意的地方就更多了，系统就更加复杂了。</p>
<p>俗话说“一山不容二虎”，两个NameNode只能有一个是活跃状态active，另一个是备份状态standby，我们看一下两个NameNode的架构图。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="417" data-height="233"><img data-original-src="//upload-images.jianshu.io/upload_images/2636642-d3ad7e2519f3c84e.png" data-original-width="417" data-original-height="233" data-original-format="image/png" data-original-filesize="59889" src="https://upload-images.jianshu.io/upload_images/2636642-d3ad7e2519f3c84e.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<p>两个NameNode通过JournalNode实现同步editlog，保持状态一致可以相互替换。</p>
<p>因为active的NameNode挂了之后，standby的NameNode要马上接替它，所以它们的数据要时刻保持一致，在写入数据的时候，两个NameNode内存中都要记录数据的元信息，并保持一致。这个JournalNode就是用来在两个NameNode中同步数据的，并且standby NameNode实现了SecondNameNode的功能。</p>
<p>进行数据同步操作的过程如下：<br>
active NameNode有操作之后，它的editlog会被记录到JournalNode中，standby NameNode会从JournalNode中读取到变化并进行同步，同时standby NameNode会监听记录的变化。这样做的话就是实时同步了，并且standby NameNode就实现了SecondNameNode的功能。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="403" data-height="155"><img data-original-src="//upload-images.jianshu.io/upload_images/2636642-005d8e8aaceda6ee.png" data-original-width="403" data-original-height="155" data-original-format="image/png" data-original-filesize="26961" src="https://upload-images.jianshu.io/upload_images/2636642-005d8e8aaceda6ee.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<h2>HDFS的优缺点</h2>
<p>优点：</p>
<ul>
<li>hdfs可以存储海量数据：理论上可以任意横向扩容</li>
<li>高可用：任何一台机器挂了都有备份，不会影响整个系统的使用，也不会造成数据丢失。</li>
</ul>
<p>缺点：</p>
<ul>
<li>HDFS不适合存储大批量的小文件：每一个小文件都有元信息，它们都存在NameNode里面，可能造成NameNode的内存不足。</li>
<li>HDFS不提供编辑文件的功能，HDFS文件写入后是不能随机修改的，只能追加：如果要随机写，由于文件被切块，需要先找到内容在哪个块，然后读入内存，修改完成之后再更新所有备份，由于一个块并不小，这个效率会很低。</li>
<li>由于HDFS写入非常复杂，所以它本身不支持并发写入。</li>
<li>查询效率不是特别高，数量级在秒级。</li>
</ul>
<h1>总结</h1>
<ol>
<li>hdfs是一个分布式文件系统，简单理解就是多台机器组成的一个文件系统。</li>
<li>hdfs中有3个重要的模块，client对外提供统一操作接口，DataNode真正存储数据，NameNode协调和管理数据，是一个典型的master-slave架构。</li>
<li>hdfs会对大文件进行切块，并且每个切块会存储备份，保证数据的高可用，适合存储大数据。</li>
<li>NameNode通过fsimage和editlog来实现数据恢复和高可用。</li>
<li>hdfs不适用于大量小文件存储，不支持并发写入，不支持文件随机修改，查询效率大概在秒级。</li>
</ol>
<h1>参考资料</h1>
<ol>
<li><a href="https://links.jianshu.com/go?to=https%3A%2F%2Fwww.pianshen.com%2Farticle%2F44511206799%2F" target="_blank">【生活现场】从生日请客到hdfs工作原理解析</a></li>
</ol>
  
</div>
            