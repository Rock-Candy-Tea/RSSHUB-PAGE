
---
title: '必须了解的MySQL三大日志：binlog、redo log和undo log'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211209/7df9a0f2aede2b01a2831133e90d6bfc.png'
author: Dockone
comments: false
date: 2021-12-12 10:08:46
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211209/7df9a0f2aede2b01a2831133e90d6bfc.png'
---

<div>   
<br>日志是<code class="prettyprint">MySQL</code>数据库的重要组成部分，记录着数据库运行期间各种状态信息。<code class="prettyprint">MySQL</code>日志主要包括错误日志、查询日志、慢查询日志、事务日志、二进制日志几大类。作为开发，我们重点需要关注的是二进制日志（<code class="prettyprint">binlog</code>）和事务日志（包括<code class="prettyprint">redo log</code>和<code class="prettyprint">undo log</code>），本文接下来会详细介绍这三种日志。<br>
<h3>binlog</h3><code class="prettyprint">binlog</code>用于记录数据库执行的写入性操作（不包括查询）信息，以二进制的形式保存在磁盘中。<code class="prettyprint">binlog</code>是<code class="prettyprint">MySQL</code>的逻辑日志，并且由<code class="prettyprint">Server</code>层进行记录，使用任何存储引擎的<code class="prettyprint">MySQL</code>数据库都会记录<code class="prettyprint">binlog</code>日志。<br>
<ul><li>逻辑日志：可以简单理解为记录的就是SQL语句。</li><li>物理日志：因为<code class="prettyprint">MySQL</code>数据最终是保存在数据页中的，物理日志记录的就是数据页变更。</li></ul><br>
<br><code class="prettyprint">binlog</code>是通过追加的方式进行写入的，可以通过<code class="prettyprint">max_binlog_size</code>参数设置每个<code class="prettyprint">binlog</code>文件的大小，当文件大小达到给定值之后，会生成新的文件来保存日志。<br>
<h4>binlog使用场景</h4>在实际应用中，<code class="prettyprint">binlog</code>的主要使用场景有两个，分别是<strong>主从复制</strong>和<strong>数据恢复</strong>。<br>
<ul><li><strong>主从复制</strong>：在<code class="prettyprint">Master</code>端开启<code class="prettyprint">binlog</code>，然后将<code class="prettyprint">binlog</code>发送到各个<code class="prettyprint">Slave</code>端，<code class="prettyprint">Slave</code>端重放<code class="prettyprint">binlog</code>从而达到主从数据一致。</li><li><strong>数据恢复</strong>：通过使用<code class="prettyprint">mysqlbinlog</code>工具来恢复数据。</li></ul><br>
<br><h4>binlog刷盘时机</h4>对于<code class="prettyprint">InnoDB</code>存储引擎而言，只有在事务提交时才会记录<code class="prettyprint">biglog</code>，此时记录还在内存中，那么<code class="prettyprint">biglog</code>是什么时候刷到磁盘中的呢？<code class="prettyprint">MySQL</code>通过<code class="prettyprint">sync_binlog</code>参数控制<code class="prettyprint">biglog</code>的刷盘时机，取值范围是<code class="prettyprint">0-N</code>：<br>
<ul><li>0：不去强制要求，由系统自行判断何时写入磁盘；</li><li>1：每次<code class="prettyprint">commit</code>的时候都要将<code class="prettyprint">binlog</code>写入磁盘；</li><li>N：每N个事务，才会将<code class="prettyprint">binlog</code>写入磁盘。</li></ul><br>
<br>从上面可以看出，<code class="prettyprint">sync_binlog</code>最安全的是设置是<code class="prettyprint">1</code>，这也是<code class="prettyprint">MySQL 5.7.7</code>之后版本的默认值。但是设置一个大一些的值可以提升数据库性能，因此实际情况下也可以将值适当调大，牺牲一定的一致性来获取更好的性能。<br>
<h4>binlog日志格式</h4><code class="prettyprint">binlog</code>日志有三种格式，分别为<code class="prettyprint">STATMENT</code>、<code class="prettyprint">ROW</code>和<code class="prettyprint">MIXED</code>。<br>
<br>在<code class="prettyprint">MySQL 5.7.7</code>之前，默认的格式是<code class="prettyprint">STATEMENT</code>，<code class="prettyprint">MySQL 5.7.7</code>之后，默认值是<code class="prettyprint">ROW</code>。日志格式通过<code class="prettyprint">binlog-format</code>指定。<br>
<ul><li><code class="prettyprint">STATMENT</code>：基于<code class="prettyprint">SQL</code>语句的复制（<code class="prettyprint">statement-based replication, SBR</code>），每一条会修改数据的SQL语句会记录到<code class="prettyprint">binlog</code>中。优点：不需要记录每一行的变化，减少了<code class="prettyprint">binlog</code>日志量，节约了<code class="prettyprint">IO</code>，从而提高了性能；缺点：在某些情况下会导致主从数据不一致，比如执行<code class="prettyprint">sysdate()</code>、<code class="prettyprint">slepp()</code>等。</li><li><code class="prettyprint">ROW</code>：基于行的复制（<code class="prettyprint">row-based replication，RBR</code>），不记录每条SQL语句的上下文信息，仅需记录哪条数据被修改了。优点：不会出现某些特定情况下的存储过程、或function、或trigger的调用和触发无法被正确复制的问题；缺点：会产生大量的日志，尤其是<code class="prettyprint">alter table</code>的时候会让日志暴涨。</li><li><code class="prettyprint">MIXED</code>：基于<code class="prettyprint">STATMENT</code>和<code class="prettyprint">ROW</code>两种模式的混合复制（<code class="prettyprint">mixed-based replication，MBR</code>），一般的复制使用<code class="prettyprint">STATEMENT</code>模式保存<code class="prettyprint">binlog</code>，对于<code class="prettyprint">STATEMENT</code>模式无法复制的操作使用<code class="prettyprint">ROW</code>模式保存<code class="prettyprint">binlog</code>。</li></ul><br>
<br><h3>redo log</h3><h4>为什么需要redo log</h4>我们都知道，事务的四大特性里面有一个是<strong>持久性</strong>，具体来说就是<strong>只要事务提交成功，那么对数据库做的修改就被永久保存下来了，不可能因为任何原因再回到原来的状态</strong>。那么<code class="prettyprint">MySQL</code>是如何保证持久性的呢？最简单的做法是在每次事务提交的时候，将该事务涉及修改的数据页全部刷新到磁盘中。但是这么做会有严重的性能问题，主要体现在两个方面：<br>
<ol><li>因为<code class="prettyprint">Innodb</code>是以<code class="prettyprint">页</code>为单位进行磁盘交互的，而一个事务很可能只修改一个数据页里面的几个字节，这个时候将完整的数据页刷到磁盘的话，太浪费资源了！</li><li>一个事务可能涉及修改多个数据页，并且这些数据页在物理上并不连续，使用随机IO写入性能太差！</li></ol><br>
<br>因此<code class="prettyprint">MySQL</code>设计了<code class="prettyprint">redo log</code>，<strong>具体来说就是只记录事务对数据页做了哪些修改</strong>，这样就能完美地解决性能问题了（相对而言文件更小并且是顺序IO）。<br>
<h4>redo log基本概念</h4><code class="prettyprint">redo log</code>包括两部分：一个是内存中的日志缓冲（<code class="prettyprint">redo log buffer</code>），另一个是磁盘上的日志文件（<code class="prettyprint">redo log file</code>）。<code class="prettyprint">MySQL</code>每执行一条<code class="prettyprint">DML</code>语句，先将记录写入<code class="prettyprint">redo log buffer</code>，后续某个时间点再一次性将多个操作记录写到<code class="prettyprint">redo log file</code>。这种<strong>先写日志，再写磁盘</strong>的技术就是<code class="prettyprint">MySQL</code>里经常说到的<code class="prettyprint">WAL（Write-Ahead Logging）</code>技术。<br>
<br>在计算机操作系统中，用户空间（<code class="prettyprint">user space</code>）下的缓冲区数据一般情况下是无法直接写入磁盘的，中间必须经过操作系统内核空间（<code class="prettyprint">kernel space</code>）缓冲区（<code class="prettyprint">OS Buffer</code>）。因此，<code class="prettyprint">redo log buffer</code>写入<code class="prettyprint">redo log file</code>实际上是先写入<code class="prettyprint">OS Buffer</code>，然后再通过系统调用<code class="prettyprint">fsync()</code>将其刷到<code class="prettyprint">redo log file</code>中，过程如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211209/7df9a0f2aede2b01a2831133e90d6bfc.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211209/7df9a0f2aede2b01a2831133e90d6bfc.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<code class="prettyprint">MySQL</code>支持三种将<code class="prettyprint">redo log buffer</code>写入<code class="prettyprint">redo log file</code>的时机，可以通过<code class="prettyprint">innodb_flush_log_at_trx_commit</code>参数配置，各参数值含义如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211209/def90c5f0f421650a91d3c923744c7e7.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211209/def90c5f0f421650a91d3c923744c7e7.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211209/8d3530ed5986ec2d0de2113d5a058683.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211209/8d3530ed5986ec2d0de2113d5a058683.jpg" class="img-polaroid" title="3.jpg" alt="3.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>redo log记录形式</h4>前面说过，<code class="prettyprint">redo log</code>实际上记录数据页的变更，而这种变更记录是没必要全部保存，因此<code class="prettyprint">redo log</code>实现上采用了大小固定，循环写入的方式，当写到结尾时，会回到开头循环写日志。如下图：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211209/886cfcaf1e9aa6580bed63230f614a75.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211209/886cfcaf1e9aa6580bed63230f614a75.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
同时我们很容易得知，在InnoDB中，既有<code class="prettyprint">redo log</code>需要刷盘，还有<code class="prettyprint">数据页</code>也需要刷盘，<code class="prettyprint">redo log</code>存在的意义主要就是降低对<code class="prettyprint">数据页</code>刷盘的要求。在上图中，<code class="prettyprint">write pos</code>表示<code class="prettyprint">redo log</code>当前记录的<code class="prettyprint">LSN</code>（逻辑序列号）位置，<code class="prettyprint">check point</code>表示数据页更改记录刷盘后对应<code class="prettyprint">redo log</code>所处的<code class="prettyprint">LSN</code>（逻辑序列号）位置。<code class="prettyprint">write pos</code>到<code class="prettyprint">check point</code>之间的部分是<code class="prettyprint">redo log</code>空着的部分，用于记录新的记录；<code class="prettyprint">check point</code>到<code class="prettyprint">write pos</code>之间是<code class="prettyprint">redo log</code>待落盘的数据页更改记录。当<code class="prettyprint">write pos</code>追上<code class="prettyprint">check point</code>时，会先推动<code class="prettyprint">check point</code>向前移动，空出位置再记录新的日志。<br>
<br>启动<code class="prettyprint">InnoDB</code>的时候，不管上次是正常关闭还是异常关闭，总是会进行恢复操作。因为<code class="prettyprint">redo log</code>记录的是数据页的物理变化，因此恢复的时候速度比逻辑日志（如<code class="prettyprint">binlog</code>）要快很多。重启<code class="prettyprint">InnoDB</code>时，首先会检查磁盘中数据页的<code class="prettyprint">LSN</code>，如果数据页的<code class="prettyprint">LSN</code>小于日志中的<code class="prettyprint">LSN</code>，则会从<code class="prettyprint">checkpoint</code>开始恢复。还有一种情况，在宕机前正处于<code class="prettyprint">checkpoint</code>的刷盘过程，且数据页的刷盘进度超过了日志页的刷盘进度，此时会出现数据页中记录的<code class="prettyprint">LSN</code>大于日志中的<code class="prettyprint">LSN</code>，这时超出日志进度的部分将不会重做，因为这本身就表示已经做过的事情，无需再重做。<br>
<h4>redo log与binlog区别</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20211209/f8ed0ee85105df0326283ba7cee45692.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20211209/f8ed0ee85105df0326283ba7cee45692.png" class="img-polaroid" title="5.png" alt="5.png" referrerpolicy="no-referrer"></a>
</div>
<br>
由<code class="prettyprint">binlog</code>和<code class="prettyprint">redo log</code>的区别可知：<code class="prettyprint">binlog</code>日志只用于归档，只依靠<code class="prettyprint">binlog</code>是没有<code class="prettyprint">crash-safe</code>能力的。但只有<code class="prettyprint">redo log</code>也不行，因为<code class="prettyprint">redo log</code>是<code class="prettyprint">InnoDB</code>特有的，且日志上的记录落盘后会被覆盖掉。因此需要<code class="prettyprint">binlog</code>和<code class="prettyprint">redo log</code>二者同时记录，才能保证当数据库发生宕机重启时，数据不会丢失。<br>
<h3>undo log</h3>数据库事务四大特性中有一个是<strong>原子性</strong>，具体来说就是<strong>原子性是指对数据库的一系列操作，要么全部成功，要么全部失败，不可能出现部分成功的情况</strong>。实际上，<strong>原子性</strong>底层就是通过<code class="prettyprint">undo log</code>实现的。<code class="prettyprint">undo log</code>主要记录了数据的逻辑变化，比如一条<code class="prettyprint">INSERT</code>语句，对应一条<code class="prettyprint">DELETE</code>的<code class="prettyprint">undo log</code>，对于每个<code class="prettyprint">UPDATE</code>语句，对应一条相反的<code class="prettyprint">UPDATE</code>的<code class="prettyprint">undo log</code>，这样在发生错误时，就能回滚到事务之前的数据状态。同时，<code class="prettyprint">undo log</code>也是<code class="prettyprint">MVCC</code>（多版本并发控制）实现的关键，这部分内容在<a href="https://juejin.cn/post/6855129007336521741" rel="nofollow" target="_blank">https://juejin.cn/post/6855129007336521741</a>中有介绍，不再赘述。<br>
<br>参考链接：<br>
<ol><li><a href="https://juejin.cn/post/6844903794073960455" rel="nofollow" target="_blank">https://juejin.cn/post/6844903794073960455</a></li><li><a href="https://www.cnblogs.com/f-ck-need-u/archive/2018/05/08/9010872.html" rel="nofollow" target="_blank">https://www.cnblogs.com/f-ck-n ... .html</a></li><li><a href="https://www.cnblogs.com/ivy-zheng/p/11094528.html" rel="nofollow" target="_blank">https://www.cnblogs.com/ivy-zheng/p/11094528.html</a></li><li><a href="https://yq.aliyun.com/articles/592937" rel="nofollow" target="_blank">https://yq.aliyun.com/articles/592937</a></li><li><a href="https://www.jianshu.com/p/5af73b203f2a" rel="nofollow" target="_blank">https://www.jianshu.com/p/5af73b203f2a</a></li><li><a href="https://www.jianshu.com/p/20e10ed721d0" rel="nofollow" target="_blank">https://www.jianshu.com/p/20e10ed721d0</a></li></ol><br>
<br>原文链接：<a href="https://juejin.cn/post/6860252224930070536" rel="nofollow" target="_blank">https://juejin.cn/post/6860252224930070536</a>，作者：夜尽天明_
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            