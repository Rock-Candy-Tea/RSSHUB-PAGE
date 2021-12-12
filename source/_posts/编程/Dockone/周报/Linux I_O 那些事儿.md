
---
title: 'Linux I_O 那些事儿'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211207/c1f09b9c0a285d81e94d227fc54bf977.png'
author: Dockone
comments: false
date: 2021-12-12 09:08:17
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211207/c1f09b9c0a285d81e94d227fc54bf977.png'
---

<div>   
<br>【编者的话】本文主要以一张图为基础，向大家介绍Linux在I/O上做了哪些事情，即Linux中直接I/O原理，希望本文的经验和思路能为读者提供一些帮助和思考。<br>
<h3>引言</h3>我们先看一张图，这张图大体上描述了Linux系统上，应用程序对磁盘上的文件进行读写时，从上到下经历了哪些事情。这篇文章就以这张图为基础，介绍Linux在I/O上做了哪些事情。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211207/c1f09b9c0a285d81e94d227fc54bf977.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211207/c1f09b9c0a285d81e94d227fc54bf977.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h3>文件系统</h3><h4>什么是文件系统</h4>文件系统，本身是对存储设备上的文件，进行组织管理的机制。组织方式不同，就会形成不同的文件系统。比如常见的Ext4、XFS、ZFS以及网络文件系统NFS等等。<br>
<br>但是<strong>不同类型的文件系统标准和接口可能各有差异，我们在做应用开发的时候却很少关心系统调用以下的具体实现</strong>，大部分时候都是直接系统调用Open，Read，Write，Close来实现应用程序的功能，不会再去关注我们具体用了什么文件系统（UFS、XFS、Ext4、ZFS），磁盘是什么接口（IDE、SCSI，SAS，SATA等），磁盘是什么存储介质（HDD、SSD）应用开发者之所以这么爽，各种复杂细节都不用管直接调接口，是因为内核为我们做了大量的有技术含量的脏活累活。<br>
<br>开始的那张图看到Linux在各种不同的文件系统之上，虚拟了一个VFS，目的就是统一各种不同文件系统的标准和接口，让开发者可以使用相同的系统调用来使用不同的文件系统。<br>
<h4>文件系统如何工作（VFS）</h4><strong>Linux系统下的文件</strong><br>
<br>在Linux中一切皆文件。不仅普通的文件和目录，就连块设备、套接字、管道等，也都要通过统一的文件系统来管理。<br>
<pre class="prettyprint">用 ls -l 命令看最前面的字符可以看到这个文件是什么类型<br>
<br>
brw-r--r-- 1 root    root    1, 2 4月  25 11:03 bnod // 块设备文件<br>
crw-r--r-- 1 root    root    1, 2 4月  25 11:04 cnod // 符号设备文件<br>
drwxr-xr-x 2 wrn3552 wrn3552    6 4月  25 11:01 dir // 目录<br>
-rw-r--r-- 1 wrn3552 wrn3552    0 4月  25 11:01 file // 普通文件<br>
prw-r--r-- 1 root    root       0 4月  25 11:04 pipeline // 有名管道<br>
srwxr-xr-x 1 root    root       0 4月  25 11:06 socket.sock // socket文件<br>
lrwxrwxrwx 1 root    root       4 4月  25 11:04 softlink -> file // 软连接<br>
-rw-r--r-- 2 wrn3552 wrn3552 0 4月  25 11:07 hardlink // 硬链接（本质也是普通文件）<br>
</pre><br>
Linux文件系统设计了<strong>两个</strong>数据结构来管理这些不同种类的文件：<br>
<ul><li>inode（index node）：索引节点</li><li>dentry（directory entry）：目录项</li></ul><br>
<br><strong>inode</strong><br>
<br>inode是用来记录文件的metadata，所谓metadata在Wikipedia上的描述是data of data，其实指的就是文件的各种属性，比如inode编号、文件大小、访问权限、修改日期、数据的位置等。<br>
<pre class="prettyprint">wrn3552@novadev:~/playground$ stat file<br>
文件：file<br>
大小：0               块：0          IO块：4096   普通空文件<br>
设备：fe21h/65057d      Inode：32828       硬链接：2<br>
权限：(0644/-rw-r--r--)  Uid：( 3041/ wrn3552)   Gid：( 3041/ wrn3552)<br>
最近访问：2021-04-25 11:07:59.603745534 +0800<br>
最近更改：2021-04-25 11:07:59.603745534 +0800<br>
最近改动：2021-04-25 11:08:04.739848692 +0800<br>
创建时间：-<br>
</pre><br>
inode和文件一一对应，它跟文件内容一样，都会被持久化存储到磁盘中。所以，inode同样占用磁盘空间，只不过相对于文件来说它大小固定且大小不算大。<br>
<br><strong>dentry</strong><br>
<br>dentry用来记录文件的名字、inode指针以及与其他dentry的关联关系。<br>
<pre class="prettyprint">wrn3552@novadev:~/playground$ tree<br>
.<br>
├── dir<br>
│   └── file_in_dir<br>
├── file<br>
└── hardlink<br>
</pre><br>
<ul><li>文件的名字：像dir、file、hardlink、file_in_dir这些名字是记录在dentry里的。</li><li>inode指针：就是指向这个文件的inode。</li><li>与其他dentry的关联关系：其实就是每个文件的层级关系，哪个文件在哪个文件下面，构成了文件系统的目录结构。</li></ul><br>
<br>不同于inode，dentry是由内核维护的一个内存数据结构，所以通常也被叫做dentry cache。<br>
<h4>件是如何存储在磁盘上的</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211207/942800f3945420354287aff8201626fb.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211207/942800f3945420354287aff8201626fb.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这里有张图解释了文件是如何存储在磁盘上的：<br>
<br>首先，磁盘再进行文件系统格式化的时候，会分出来<strong>3个区</strong>：Superblock、inode blocks、data blocks。（其实还有boot block，可能会包含一些Bootstrap代码，在机器启动的时候被读到，这里忽略）<br>
<br>其中inode blocks放的都是每个文件的inode，data blocks里放的是每个文件的内容数据。<br>
<br>这里关注一下<strong>Superblock，它包含了整个文件系统的metadata</strong>，具体有：<br>
<ul><li>inode/data block 总量、使用量、剩余量。</li><li>文件系统的格式，属主等等各种属性。</li></ul><br>
<br>Superblock对于文件系统来说非常重要，如果Superblock损坏了，文件系统就挂载不了了，相应的文件也没办法读写。<br>
<br>既然Superblock这么重要，那肯定不能只有一份，坏了就没了，它在系统中是有很多副本的，在Superblock损坏的时候，可以使用fsck（File System Check and repair）来恢复。<br>
<br>回到上面的那张图，可以很清晰地看到文件的各种属性和文件的数据是如何存储在磁盘上的：<br>
<ul><li>dentry里包含了文件的名字、目录结构、inode指针。</li><li>inode指针指向文件特定的inode（存在inode blocks里）</li><li>每个inode又指向data blocks里具体的logical block，这里的logical block存的就是文件具体的数据。</li></ul><br>
<br>这里解释一下什么是logical block：<br>
<ul><li>对于不同存储介质的磁盘，都有最小的读写单元 /sys/block/sda/queue/physical_block_size。</li><li>HDD叫做sector（扇区），SSD叫做page（页面）</li><li>对于HDD来说，每个sector大小512Bytes。</li><li>对于SSD来说每个page大小不等（和cell类型有关），经典的大小是4KB。</li><li>但是Linux觉得按照存储介质的最小读写单元来进行读写可能会有效率问题，所以支持在文件系统格式化的时候指定block size的大小，一般是把几个physical_block拼起来就成了一个logical block /sys/block/sda/queue/logical_block_size。</li><li>理论上应该是logical_block_size>=physical_block_size，但是有时候我们会看到physical_block_size=4K，logical_block_size=512B情况，其实这是因为磁盘上做了一层512B的仿真（emulation）（详情可参考512e和4Kn）</li></ul><br>
<br><h3>ZFS</h3>这里简单介绍一个广泛应用的文件系统ZFS，一些数据库应用也会用到 ZFS。<br>
<br>先看一张ZFS的层级结构图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211207/31ac17fab074c3bff7e7a580210c7bbb.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211207/31ac17fab074c3bff7e7a580210c7bbb.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
这是一张从底向上的图：<br>
<ul><li>将若干物理设备disk组成一个虚拟设备vdev（同时，disk 也是一种vdev）</li><li>再将若干个虚拟设备vdev加到一个zpool里。</li><li>在zpool的基础上创建zfs并挂载（zvol可以先不看，我们没有用到）</li></ul><br>
<br><h4>ZFS的一些操作</h4><strong>创建zpool</strong><br>
<pre class="prettyprint">root@:~ # zpool create tank raidz /dev/ada1 /dev/ada2 /dev/ada3 raidz /dev/ada4 /dev/ada5 /dev/ada6<br>
root@:~ # zpool list tank<br>
NAME    SIZE  ALLOC   FREE  CKPOINT  EXPANDSZ   FRAG    CAP  DEDUP  HEALTH  ALTROOT<br>
tank     11G   824K  11.0G        -         -     0%     0%  1.00x  ONLINE  -<br>
root@:~ # zpool status tank<br>
pool: tank<br>
state: ONLINE<br>
scan: none requested<br>
config:<br>
<br>
    NAME        STATE     READ WRITE CKSUM<br>
    tank        ONLINE       0     0     0<br>
      raidz1-0  ONLINE       0     0     0<br>
        ada1    ONLINE       0     0     0<br>
        ada2    ONLINE       0     0     0<br>
        ada3    ONLINE       0     0     0<br>
      raidz1-1  ONLINE       0     0     0<br>
        ada4    ONLINE       0     0     0<br>
        ada5    ONLINE       0     0     0<br>
        ada6    ONLINE       0     0     0<br>
</pre><br>
<ul><li>创建了一个名为tank的zpool</li><li>这里的raidz同RAID5</li></ul><br>
<br>除了raidz还支持其他方案：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211207/4674ec08fbc063187b1391d07f2ecf9d.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211207/4674ec08fbc063187b1391d07f2ecf9d.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<strong>创建ZFS</strong><br>
<pre class="prettyprint">root@:~ # zfs create -o mountpoint=/mnt/srev tank/srev<br>
root@:~ # df -h tank/srev<br>
Filesystem    Size    Used   Avail Capacity  Mounted on<br>
tank/srev     7.1G    117K    7.1G     0%    /mnt/srev<br>
</pre><br>
<ul><li>创建了一个ZFS，挂载到了/mnt/srev。</li><li>这里没有指定ZFS的quota，创建的ZFS大小即zpool大小。</li></ul><br>
<br><strong>对ZFS设置quota</strong><br>
<pre class="prettyprint">root@:~ # zfs set quota=1G tank/srev<br>
root@:~ # df -h tank/srev<br>
Filesystem    Size    Used   Avail Capacity  Mounted on<br>
tank/srev     1.0G    118K    1.0G     0%    /mnt/srev<br>
</pre><br>
<h4>ZFS特性</h4><strong>Pool存储</strong><br>
<br>上面的层级图和操作步骤可以看到ZFS是基于zpool创建的，zpool可以动态扩容意味着存储空间也可以动态扩容。而且可以创建多个文件系统，文件系统共享完整的zpool空间无需预分配。<br>
<br><strong>事务文件系统</strong><br>
<br>ZFS的写操作是事务的，意味着要么就没写，要么就写成功了，不会像其他文件系统那样，应用打开了文件，写入还没保存的时候断电，导致文件为空。<br>
<br>ZFS保证写操作事务采用的是copy on write的方式：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211207/2c5d3765b0ae15936ce12f19fc7a68e6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211207/2c5d3765b0ae15936ce12f19fc7a68e6.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
当block B有修改变成B1的时候，普通的文件系统会直接在block B原地进行修改变成B1。<br>
<br>ZFS则会再另一个地方写B1，然后再在后面安全的时候对原来的B进行回收。这样结果就不会出现B被打开而写失败的情况，大不了就是B1没写成功。<br>
<br>这个特性让ZFS在断电后不需要执行fsck来检查磁盘中是否存在写操作失败需要恢复的情况，大大提升了应用的可用性。<br>
<br><strong>ARC缓存</strong><br>
<br>ZFS中的ARC（Adjustable Replacement Cache）读缓存淘汰算法，是基于IBM的ARP（Adaptive Replacement Cache）演化而来。<br>
<br>在一些文件系统中实现的标准LRU算法其实是有缺陷的：比如复制大文件之类的线性大量I/O操作，导致缓存失效率猛增（大量文件只读一次，放到内存不会被再读，坐等淘汰）。<br>
<br>另外，缓存可以根据时间来进行优化（LRU，最近最多使用），也可以根据频率进行优化（LFU，最近最常使用），这两种方法各有优劣，但是没办法适应所有场景。<br>
<br>ARC的设计就是尝试在LRU和LFU之间找到一个平衡，根据当前的I/O workload来调整用LRU多一点还是LFU多一点。<br>
<br>ARC定义了4个链表：<br>
<ul><li>LRU list：最近最多使用的页面，存具体数据。</li><li>LFU list：最近最常使用的页面，存具体数据。</li><li>Ghost list for LRU：最近从LRU表淘汰下来的页面信息，不存具体数据，只存页面信息。</li><li>Ghost list for LFU：最近从LFU表淘汰下来的页面信息，不存具体数据，只存页面信息。</li></ul><br>
<br>ARC工作流程大致如下：<br>
<ul><li>LRU list和LFU list填充和淘汰过程和标准算法一样。</li><li>当一个页面从LRU list淘汰下来时，这个页面的信息会放到LRU ghost表中。</li><li>如果这个页面一直没被再次引用到，那么这个页面的信息最终也会在LRU ghost表中被淘汰掉。</li><li>如果这个页面在LRU ghost表中未被淘汰的时候，被再一次访问了，这时候会引起一次幽灵（phantom）命中。</li><li>phantom命中的时候，事实上还是要把数据从磁盘第一次放缓存。</li><li>但是这时候系统知道刚刚被LRU表淘汰的页面又被访问到了，说明LRU list太小了，这时它会把LRU list长度加一，LFU长度减一。</li><li>对于LFU的过程也与上述过程类似。</li></ul><br>
<br><h3>磁盘类型</h3>磁盘根据不同的分类方式，有各种不一样的类型。<br>
<h4>磁盘的存储介质</h4>根据磁盘的存储介质可以分两类（大家都很熟悉）：HDD（机械硬盘）和SSD（固态硬盘）。<br>
<h4>磁盘的接口</h4>根据磁盘接口分类：<br>
<ul><li>IDE（Integrated Drive Electronics）</li><li>SCSI（Small Computer System Interface）</li><li>SAS（Serial Attached SCSI）</li><li>SATA（Serial ATA）</li><li>……</li></ul><br>
<br>不同的接口，往往分配不同的设备名称。比如，IDE设备会分配一个hd前缀的设备名，SCSI和SATA设备会分配一个sd前缀的设备名。如果是多块同类型的磁盘，就会按照a、b、c等的字母顺序来编号。<br>
<h4>Linux对磁盘的管理</h4>其实在Linux中，磁盘实际上是作为一个块设备来管理的，也就是以块为单位读写数据，并且支持随机读写。每个块设备都会被赋予两个设备号，分别是主、次设备号。主设备号用在驱动程序中，用来区分设备类型；而次设备号则是用来给多个同类设备编号。<br>
<pre class="prettyprint">g18-"299" on ~# ls -l /dev/sda*<br>
brw-rw---- 1 root disk 8,  0 Apr 25 15:53 /dev/sda<br>
brw-rw---- 1 root disk 8,  1 Apr 25 15:53 /dev/sda1<br>
brw-rw---- 1 root disk 8, 10 Apr 25 15:53 /dev/sda10<br>
brw-rw---- 1 root disk 8,  2 Apr 25 15:53 /dev/sda2<br>
brw-rw---- 1 root disk 8,  5 Apr 25 15:53 /dev/sda5<br>
brw-rw---- 1 root disk 8,  6 Apr 25 15:53 /dev/sda6<br>
brw-rw---- 1 root disk 8,  7 Apr 25 15:53 /dev/sda7<br>
brw-rw---- 1 root disk 8,  8 Apr 25 15:53 /dev/sda8<br>
brw-rw---- 1 root disk 8,  9 Apr 25 15:53 /dev/sda9<br>
</pre><br>
<ul><li>这些sda磁盘主设备号都是8，表示它是一个sd类型的块设备。</li><li>次设备号0-10表示这些不同sd块设备的编号。</li></ul><br>
<br><h3>Generic Block Layer</h3><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211207/b77bdd8ac99a3fe4c7a7225a861e379a.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211207/b77bdd8ac99a3fe4c7a7225a861e379a.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
可以看到中间的Block Layer其实就是Generic Block Layer。<br>
<br>在图中可以看到Block Layer的I/O调度分为两类，分别表示<strong>单队列和多队列</strong>的调度：<br>
<ul><li>I/O scheduler</li><li>blkmq</li></ul><br>
<br><h4>I/O调度</h4>老版本的内核里只支持单队列的I/O scheduler，在3.16版本的内核开始支持多队列blkmq。<br>
<br>这里介绍几种经典的I/O调度策略：<br>
<br><strong>单队列I/O scheduler</strong><br>
<ul><li>NOOP：事实上是个FIFO的队列，只做基本的请求合并。</li><li>CFQ：Completely Fair Queueing，完全公平调度器，给每个进程维护一个I/O调度队列，按照时间片来均匀分布每个进程I/O请求。</li><li>DeadLine：为读和写请求创建不同的I/O队列，确保达到deadline的请求被优先处理。</li></ul><br>
<br><strong>多队列blkmq</strong><br>
<ul><li>bfq：Budget Fair Queueing，也是公平调度器，不过不是按时间片来分配，而是按请求的扇区数量（带宽）</li><li>kyber：维护两个队列（同步/读、异步/写），同时严格限制发到这两个队列的请求数以保证相应时间。</li><li>mq-deadline：多队列版本的deadline。</li></ul><br>
<br>具体各种I/O调度策略可以参考：<a href="https://wiki.ubuntu.com/Kernel/Reference/IOSchedulers" rel="nofollow" target="_blank">https://wiki.ubuntu.com/Kernel ... ulers</a><br>
<br>关于blkmq可以参考：<a href="https://www.thomas-krenn.com/en/wiki/Linux_Multi-Queue_Block_IO_Queueing_Mechanism_" rel="nofollow" target="_blank">https://www.thomas-krenn.com/e ... nism_</a>(blk-mq)_Details<br>
<br>多队列调度可以参考：<a href="https://lwn.net/Articles/738449/" rel="nofollow" target="_blank">https://lwn.net/Articles/738449/</a><br>
<h3>性能指标</h3>一般来说I/O性能指标有这<strong>5</strong>个：<br>
<ul><li>使用率：ioutil，指的是磁盘处理I/O的时间百分比，ioutil只看有没有I/O请求，不看I/O请求的大小。ioutil越高表示一直都有I/O请求，不代表磁盘无法响应新的I/O请求。</li><li>IOPS：每秒的I/O请求数。</li><li>吞吐量/带宽：每秒的I/O请求大小，通常是MB/s或者GB/s为单位。</li><li>响应时间：I/O请求发出到收到响应的时间。</li><li>饱和度：指的是磁盘处理I/O的繁忙程度。这个指标比较玄学，没有直接的数据可以表示，一般是根据平均队列请求长度或者响应时间跟基准测试的结果进行对比来估算（在做基准测试时，还会分顺序/随机、读/写进行排列组合分别去测IOPS和带宽）</li></ul><br>
<br>上面的指标除了饱和度外，其他都可以在监控系统中看到。<strong>Linux也提供了一些命令来输出不同维度的I/O状态</strong>：<br>
<ul><li>iostat-d-x：看各个设备的I/O状态，数据来源/proc/diskstats。</li><li>pidstat-d：看近处的I/O。</li><li>iotop：类似top，按I/O大小对进程排序。</li></ul><br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/X7_aXicypwogK3vjAVmppw" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/X7_aXicypwogK3vjAVmppw</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            