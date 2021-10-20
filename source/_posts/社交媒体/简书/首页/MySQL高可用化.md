
---
title: 'MySQL高可用化'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/6464086-6f00f122797a81d9.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/6464086-6f00f122797a81d9.png'
---

<div>   
<p>服务在运行过程中存在很多意外情况，如：如服务器宕机、磁盘损坏、RAID卡损坏等。如何保证数据库在服务发生意外的情况下数据不丢失呢？服务还能继续提供服务呢？</p>
<p>我们一般通过备份的方式来解决数据丢失问题，通过复制来解决MySQL的高可用问题。</p>
<h1>备份</h1>
<p>备份的方法不同可以将备份分为：</p>
<ul>
<li>Hot Backup（热备，在线备份）：在数据运行过程中进行备份，对数据库操作没有影响。</li>
<li>Cold Backup（冷备，离线备份）：在数据停止情况下，直接拷贝数据库物理文件。</li>
<li>Warm Backup（温备）：在数据运行过程中进行，但是会对当前数据库的操作有所影响，如加一个全局读锁以保证备份数据的一致性。</li>
</ul>
<p>按照备份后文件的内容，备份又可以分为：</p>
<ul>
<li>逻辑备份：是指备份出的文件内容是可读的，一般是文本文件。内容一般是由一条条SQL语句，或者是表内实际数据组成。一般适用于数据库的升级、迁移等工作。但其缺点是恢复所需要的时间往往较长。</li>
<li>裸文件备份：是指复制数据库的物理文件，既可以是在数据库运行中的复制（如ibbackup、xtrabackup这类工具），也可以是在数据库停止运行时直接的数据文件复制。这类备份的恢复时间往往较逻辑备份短很多。</li>
</ul>
<p>若按照备份数据库的内容来分，备份又可以分为：</p>
<ul>
<li>完全备份：完全备份是指对数据库进行一个完整的备份。</li>
<li>增量备份：增量备份是指在上次完全备份的基础上，对于更改的数据进行备份。</li>
<li>日志备份：日志备份主要是指对MySQL数据库二进制日志的备份，通过对一个完全备份进行二进制日志的重做（replay）来完成数据库的point-in-time的恢复工作。</li>
</ul>
<h1>复制</h1>
<p>复制（replication）是MySQL数据库提供的一种高可用高性能的解决方案，一般用来建立大型的应用，原理如下：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="944" data-height="542"><img data-original-src="//upload-images.jianshu.io/upload_images/6464086-6f00f122797a81d9.png" data-original-width="944" data-original-height="542" data-original-format="image/png" data-original-filesize="87947" src="https://upload-images.jianshu.io/upload_images/6464086-6f00f122797a81d9.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<ol>
<li>主服务器（master）把数据更改记录到二进制日志（binlog）中，然后通过<code>binary log dump</code>线程将二进制文件推送到从服务器。</li>
<li>从服务器（slave）通过I/O线程，把主服务器的二进制日志复制到自己的中继日志（relay log）中，中继日志通常会位于os缓存中，所以中继日志的开销很小。</li>
<li>从服务器通过SQL线程重做中继日志中的日志，把更改应用到自己的数据库上，以达到数据的最终一致性。</li>
</ol>
<p>从服务器有2个线程，一个是I/O线程，负责读取主服务器的二进制日志，并将其保存为中继日志；另一个是SQL线程，复制执行中继日志。这里需要特别注意的是，<strong>复制是一个异步过程，从服务器数据存在延迟</strong>。</p>
<p>MySQL二进制日志文件Binlog有三种格式，<code>Statement</code>、<code>Row</code>和<code>Mixed</code>，所以MySQL的复制也对应有三种方式。</p>
<h2>异步复制</h2>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1090" data-height="495"><img data-original-src="//upload-images.jianshu.io/upload_images/6464086-fd793a91668fbd4c.png" data-original-width="1090" data-original-height="495" data-original-format="image/png" data-original-filesize="126132" src="https://upload-images.jianshu.io/upload_images/6464086-fd793a91668fbd4c.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<p>主库执行完Commit后，在主库写入Binlog日志后即可成功返回客户端，无需等Binlog日志传送给从库。</p>
<h2>半同步复制</h2>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1193" data-height="513"><img data-original-src="//upload-images.jianshu.io/upload_images/6464086-1c6ac799537a94a8.png" data-original-width="1193" data-original-height="513" data-original-format="image/png" data-original-filesize="63789" src="https://upload-images.jianshu.io/upload_images/6464086-1c6ac799537a94a8.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<p>在 MySQL5.5之前，MySQL的复制是异步操作，主库和从库的数据之间存在一定的延迟，这样存在一个隐患：当在主库上写人一个事务并提交成功，而从库尚未得到主库推送的Binlog日志时，主库宕机了，例如主库可能因磁盘损坏、内存故障等造成主库上该事务 Binlog丢失，此时从库就可能损失这个事务，从而造成主从不一致。</p>
<p>而半同步复制，是等待<strong>其中一个</strong>从库也接收到Binlog事务并成功写入Relay Log之后，才返回Commit操作成功给客户端；如此半同步就保证了事务成功提交后至少有两份日志记录，一份在主库Binlog上，另一份在从库的Relay Log上，从而进一步保证数据完整性；半同步复制很大程度取决于主从网络RTT（往返时延），以插件 semisync_master/semisync_slave 形式存在。</p>
<h1>集群</h1>
<p>使用集群可以提高MySQL服务器的可用性和性能，MySQL服务支持多种集群方案。</p>
<h2>MySQL Cluster</h2>
<p>由Mysql本身提供，优势：可用性非常高，性能非常好。每份数据至少可在不同主机存一份拷贝，且冗余数据拷贝实时同步。但它的维护非常复杂，存在部分Bug，目前还不适合比较核心的线上系统，所以不推荐。</p>
<h2>DRBD磁盘网络镜像</h2>
<p>Distributed Replicated Block Device，其实现方式是通过网络来镜像整个设备(磁盘)。它允许用户在远程机器上建立一个本地块设备的实时镜像，与心跳链接结合使用，也可看做一种网络RAID。</p>
<p>优势：软件功能强大，数据可在底层快设备级别跨物理主机镜像，且可根据性能和可靠性要求配置不同级别的同步。IO操作保持顺序，可满足数据库对数据一致性的苛刻要求。</p>
<p>但非分布式文件系统环境无法支持镜像数据同时可见，性能和可靠性两者相互矛盾，无法适用于性能和可靠性要求都比较苛刻的环境，维护成本高于MySQL Replication。另外，DRBD也是官方推荐的可用于MySQL高可用方案之一，所以这个大家可根据实际环境来考虑是否部署。</p>
<h2>MySQL Replication</h2>
<p>MySQL的复制上在实际应用场景中使用最多的一种方案，主要优势是成本低，实现起来比较简单，缺点是从服务器存在一定的延迟。</p>
<h1>常用架构</h1>
<h2>一主多从，提高系统的读性能</h2>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="244" data-height="264"><img data-original-src="//upload-images.jianshu.io/upload_images/6464086-86330a5b4f1f6d07.png" data-original-width="244" data-original-height="264" data-original-format="image/png" data-original-filesize="44631" src="https://upload-images.jianshu.io/upload_images/6464086-86330a5b4f1f6d07.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<p>一主一从和一主多从是最常见的主从架构，实施起来简单并且有效，主要用来实现读写分离，提升度的性能，降低主库压力，在主库出现异常宕机的情况下，可以把一个从库切换为主库继续提供服务。</p>
<h2>多级复制</h2>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="302" data-height="106"><img data-original-src="//upload-images.jianshu.io/upload_images/6464086-aae553c1a43e419a.png" data-original-width="302" data-original-height="106" data-original-format="image/png" data-original-filesize="26512" src="https://upload-images.jianshu.io/upload_images/6464086-aae553c1a43e419a.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<p>MySQL的复制是主库推送Binlog到从库，在上面一主多从的情况下，主库的I/O和网络压力都会随着从库的增加而增大。多级而使用多级复制可以很好的解决这个问题，但是随着从库的链路的增加从库的数据延迟也会随着增大。</p>
<h2>双主复制/Dual Master</h2>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="678" data-height="407"><img data-original-src="//upload-images.jianshu.io/upload_images/6464086-32d98f5bf98fe913.png" data-original-width="678" data-original-height="407" data-original-format="image/png" data-original-filesize="106860" src="https://upload-images.jianshu.io/upload_images/6464086-32d98f5bf98fe913.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<p>其实就是master1和master2互为主从关系，这样任何一方所做的变更，都会通过复制应用到另外一方的数据库中。client客户端的写请求都访问主库 Master1，而读请求可以选择访问主库Master1或 Master2。</p>
<h2>双主多级复制架构</h2>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="819" data-height="526"><img data-original-src="//upload-images.jianshu.io/upload_images/6464086-0f16bc709a98adee.png" data-original-width="819" data-original-height="526" data-original-format="image/png" data-original-filesize="132780" src="https://upload-images.jianshu.io/upload_images/6464086-0f16bc709a98adee.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image.png</div>
</div>
<p>双主复制还能和主从复制联合起来使用，在 Master2库下配置从库 Slave1、 Slave2等，这样即可通过从库Slave等来分担读取压力。</p>
  
</div>
            