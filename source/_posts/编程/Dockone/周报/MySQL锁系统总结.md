
---
title: 'MySQL锁系统总结'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210711/efa6256ef2cbdc5a4adb18495f068f82.jpg'
author: Dockone
comments: false
date: 2021-07-11 13:11:23
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210711/efa6256ef2cbdc5a4adb18495f068f82.jpg'
---

<div>   
<br><h3>InnoDB锁简介</h3>InnoDB支持多种粒度的锁，按照粒度来分，可分为<code class="prettyprint">表锁（LOCK_TABLE）</code>和<code class="prettyprint">行锁（LOCK_REC）</code>。<br>
<br>一般的锁系统都会有<code class="prettyprint">共享锁</code>和<code class="prettyprint">排他锁</code>的分类，<code class="prettyprint">共享锁</code>也叫<code class="prettyprint">读锁</code>，<code class="prettyprint">排他锁</code>也叫<code class="prettyprint">写锁</code>。加在同一个资源上，写锁会阻塞另外一把写锁或读锁的获取，读锁则允许另外一把读锁的获取，也就是读读之间允许并发，读写或者写写会阻塞，InnoDB中表锁和行锁都支持<code class="prettyprint">共享锁（简写S）</code>和<code class="prettyprint">排他锁（简写X）</code>。<br>
<br>因为InnoDB支持多粒度的锁，允许表锁和行锁的并存，为了方便多粒度锁冲突的判断，InnoDB中还存在一种名叫<code class="prettyprint">意向锁（Intention Locks）</code>的锁。<br>
<br>除此之外，还有一种特殊的表锁，自增锁，主要用来并发安全的生成自增id，一种特殊的意向锁，插入意向锁，用来防止幻读问题。<br>
<h3>表锁</h3>表锁，锁定的粒度是整个表，也分共享锁和排他锁。不同于行锁，表锁MySQL Server层就有实现（所以MyISAM支持表锁，也只支持表锁），InnoDB则在存储引擎层面也实现了一遍表锁（后面会介绍具体结构）。  哪些时候会触发表锁呢？在执行某些ddl时，比如<code class="prettyprint">alter table</code>等操作，会对整个表加锁，也可以手动执行锁表语句：<code class="prettyprint">LOCK TALBES table_name [READ | WRITE]</code>，READ为共享锁，WRITE为排他锁，手动解锁的语句为：<code class="prettyprint">UNLOCK TABLES</code>，会直接释放当前会话持有的所有表锁<br>
<br>有一些需要注意的地方：<br>
<ul><li>因为MySQL Server层和InnoDB都实现了表锁，仅当<code class="prettyprint">autocommit=0</code>、<code class="prettyprint">innodb_table_lock=1</code>（默认设置）时，InnoDB层才能知道MySQL加的表锁，ＭySQL Server才能感知InnoDB加的行锁，这种情况下，InnoDB才能自动识别涉及表级锁的死锁，否则，InnoDB将无法自动检测并处理这种死锁。</li><li>在用<code class="prettyprint">LOCK TALBES</code>显式获取锁后，只能访问加锁的这些表，并且如果加的是共享锁，那么只能执行查询操作，而不能执行更新操作，如果获得的是排他锁，则可以进行更新操作。</li><li>开始事务时会自动UNLOCK之前的表锁，COMMIT或ROLLBACK都不能释放用<code class="prettyprint">LOCK TABLES</code>加的表级锁。<code class="prettyprint">LOCK TALBES</code>时会先隐式提交事务，再锁表，<code class="prettyprint">UNLOCK TALBES</code>也会隐式提交事务。所以，事务中需要的表锁必须在事务开头一次性获取，无法再事务中间获取，因为不管是<code class="prettyprint">LOCK TALBES</code>还是<code class="prettyprint">UNLOCK TALBES</code>都会提交事务。</li></ul><br>
<br>官网上建议的表锁的使用方法：<br>
<pre class="prettyprint">SET autocommit=0;  <br>
LOCK TABLES t1 WRITE, t2 READ, ...;  <br>
... do something with tables t1 and t2 here ...  <br>
COMMIT;  <br>
UNLOCK TABLES;<br>
</pre><br>
实际业务中，没有特殊理由，不建议使用表锁，因为锁的粒度太大了，极大的影响并发。<br>
<h3>意向锁</h3>意向锁是一种特殊的表级锁，意向锁是为了让InnoDB多粒度的锁能共存而设计的。取得行的共享锁和排他锁之前需要先取得表的意向共享锁（IS）和意向排他锁（IX），意向共享锁和意向排他锁都是系统自动添加和自动释放的，整个过程无需人工干预。 主要是用来辅助表级和行级锁的冲突判断，因为Innodb支持行级锁，如果没有意向锁，则判断表锁和行锁冲突的时候需要遍历表上所有行锁，有了意向锁，则只要判断表是否存在意向锁就可以知道是否有行锁了。表级别锁的兼容性如下表：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210711/efa6256ef2cbdc5a4adb18495f068f82.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210711/efa6256ef2cbdc5a4adb18495f068f82.jpg" class="img-polaroid" title="1.jpg" alt="1.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
可以看到，意向锁与意向锁兼容，IX、IS自身以及相互都兼容，不互斥，因为意向锁仅表示下一层级加什么类型的锁，不代表当前层加什么类型的锁；IX和表级X、S互斥；IS和表级X锁互斥。其兼容性正好体现了其作用<br>
<h3>自增锁</h3>自增锁是一种特殊的表级别锁，如果一个表的某个行具有<code class="prettyprint">AUTO_INCREMENT</code>的列，则一个事务在插入记录到这个表的时候，会先获取自增锁。如果一个事务持有自增锁，会阻塞其他事物对该表的插入操作，保证自增连续。<code class="prettyprint">innodb_autoinc_lock_mode</code>变量定义了不同的自增算法，在MySQL 8.0之前默认值是1，MySQL 8.0之后默认值是2，具体区别参考<a href="https://dev.mysql.com/doc/refman/8.0/en/innodb-auto-increment-handling.html">官方文档</a>。<br>
<h3>行锁</h3>InnoDB中的行锁种类繁多，可以分为：记录锁（record locks）、间隙锁（gap locks）、临键锁（next-key locks），插入意向锁（insert intention locks）。行锁在逻辑上都可以看作作用于索引或者索引间隙之上，索引分为主键索引和非主键索引两种，如果一条SQL语句操作了主键索引，MySQL就会锁定这条主键索引；如果一条语句操作了非主键索引，MySQL会先锁定该非主键索引，再锁定相关的主键索引。<br>
<br>很多语句都会加行锁，比如Update、Delete、Insert等操作，或者使用SELECT ... FOR SHARE | UPDATE [NOWAIT |SKIP LOCKED]来进行当前读（Locking Reads），其中<code class="prettyprint">SHARE</code>表示加共享锁，<code class="prettyprint">UPDATE</code>表示加排他锁。当要加的锁与当前行已有锁互斥时，会一直阻塞等待一段时间（<code class="prettyprint">innodb_lock_wait_timeout</code>定义了等待时间）。加上<code class="prettyprint">NOWAIT</code>参数则不会阻塞，会立即返回，并显示一个错误，加上<code class="prettyprint">SKIP LOCKED</code>则会在结果集中跳过这些冲突的记录（慎用）。<br>
<br>在不同的语句，不同的事务隔离级别下，甚至不同的索引类型下，行锁会表现成不同的形式，下面介绍这些形式：<br>
<h4>记录锁（record locks）</h4>在逻辑上，记录锁可以理解为锁定的是某个具体的索引，当SQL执行按照唯一性（Primary key、Unique key）索引进行数据的检索时，查询条件等值匹配且查询的数据是存在，这时SQL语句加上的锁即为记录锁。<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210711/0f64a587e8897594e37a7f3ba3f84d81.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210711/0f64a587e8897594e37a7f3ba3f84d81.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<h4>间隙锁（gap locks）</h4>在逻辑上，间隙锁可以理解为锁住的是索引之间的间隙，是一个左开右开的区间。当SQL执行按照索引进行数据的检索时，查询条件的数据不存在，这时SQL语句加上的锁即为间隙锁。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210711/9d2b0cd1d006b7bedb8ff46b14012f86.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210711/9d2b0cd1d006b7bedb8ff46b14012f86.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
如上图，因为这些语句查询的值都不存在，所以锁住的都是间隙。并且在InnoDB存储引擎里，每个数据页中都会有两个虚拟的行记录，用来限定记录的边界，分别是：<code class="prettyprint">Infimum Record</code>和<code class="prettyprint">Supremum Record</code>，<code class="prettyprint">Infimum</code>是比该页中任何记录都要小的值，而<code class="prettyprint">Supremum</code>比该页中最大的记录值还要大，这两条记录在创建页的时候就有了，并且不会删除。所以当查询的值比当前已有记录最大值还大时候，锁住的会是最大值到<code class="prettyprint">Supremum</code>之间的间隙。比如第一条语句，查询的时候就算是等值匹配，只要这个不存在的数据落在两个索引节点之间，就算不是一个范围，也会锁住索引节点间的所有数据即gap3，范围（7，11）。<br>
<br>间隙锁是可以共存的，共享间隙锁与独占间隙锁之间是没有区别的，两者之间并不冲突。其存在的目的都是防止其他事务往间隙中插入新的纪录，故而一个事务所采取的间隙锁是不会去阻止另外一个事务在同一个间隙中加锁的<br>
<br>间隙锁是设计用来防止幻读的，当锁定一个gap时，其他事务没有办法再往这个gap中插入数据，PostgreSQL没有这种机制，所以PostgreSQl没有办法锁住不存在的行，无法防止幻读<br>
<h4>临键锁（next-key locks）</h4>在逻辑上，临键锁可以理解为锁住的是索引本身以及索引之前的间隙，是一个左开右闭的区间。当SQL执行按照非唯一索引进行数据的检索时，会给匹配到行上加上临键锁。<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210711/3d1cef7e0ff0649783a654342c5461a6.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210711/3d1cef7e0ff0649783a654342c5461a6.png" class="img-polaroid" title="4.png" alt="4.png" referrerpolicy="no-referrer"></a>
</div>
<br>
如上图，当执行<code class="prettyprint">select * from table_name where id = 3 for update</code>时会锁定（-∞，3）区间，因为按照这个SQL的语义，即是为了锁住<code class="prettyprint">id=3</code>的数据，不允许其他操作，如果只是锁住记录本身，肯定是没有办法保证的，因为这是非唯一索引，还有可能插入其他<code class="prettyprint">id=3</code>的数据，如果把间隙都给锁住，则其他对这个间隙的插入操作都会被阻塞，从而保证了一致性，这也是临键锁的用意。<br>
<br>如果加锁时，查询条件没有命中索引（非ICP的查询），则InnoDB会尝试给全表每一条记录都加上临键锁，效果相当于锁表了<br>
<h4>插入意向锁（insert intention locks）</h4>插入意向锁是一种间隙锁形式的意向锁，在真正执行INSERT操作之前设置。当执行插入操作时，总会检查当前插入操作的下一条记录（已存在的主索引节点）上是否存在锁对象，判断是否锁住了gap，如果锁住了，则判定和插入意向锁冲突，当前插入操作就需要等待，也就是配合上面的间隙锁或者临键锁一起防止了幻读操作。  因为插入意向锁是一种意向锁，意向锁只是表示一种意象，所以插入意向锁之间不会互相冲突，多个插入操作同时插入同一个gap时，无需互相等待，比如当前索引上有记录4和8，两个并发session同时插入记录6，7。他们会分别为（4，8）加上GAP锁，但相互之间并不冲突。  INSERT语句在执行插入之前，会先在gap中加入插入意向锁，如果是唯一索引，还会进行Duplicate Key判断，如果存在相同Key且该Key被加了互持锁，则还会加共享锁，然后等待（因为这个相同的Key之后有可能会回滚删除，这里非常容易死锁）。等到成功插入后，会在这条记录上加排他记录锁。<br>
<h4>行锁小结</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210711/40a1b9475a62ab90fa84da56adde89e2.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210711/40a1b9475a62ab90fa84da56adde89e2.jpg" class="img-polaroid" title="5.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
行锁在不同的语句中和环境条件下可以表现成：记录锁（record locks）、 间隙锁（gap locks）、临键锁（next-key locks）和插入意向锁（insert intention locks）。记录锁锁住具体的记录，间隙锁锁住记录之间的间隙，临键锁锁住记录和记录前面的间隙，插入意向锁则是特殊的间隙锁，在插入前判断行将要插入的间隙是否会有冲突。<br>
<br>以上说的各种行锁的加锁情况都是在<code class="prettyprint">可重复读（REPEATABLE READ）</code>隔离级别下，这个级别也是InnoDB默认的事务隔离级别，是最常用的隔离级别，但是其实不同语句在不同隔离级别下加锁的情况会有非常大的区别，以下会简单说明。<br>
<h3>不同语句和隔离级别对加锁的影响</h3>这里先排除<code class="prettyprint">读未提交（READ UNCOMMITTED）</code>这种隔离级别的情况，这种级别在生产上几乎无法使用，会出现脏读的情况，不一致读，无法保证事务的ACID。然后先看下<code class="prettyprint">串行化（SERIALIZABLE）</code>隔离级别。<br>
<br><code class="prettyprint">串行化</code>隔离级别和<code class="prettyprint">可重复读</code>隔离级别最大的区别应该是，InnoDB会隐式的转换所有的SELECT语句，给其加共享锁，变成<code class="prettyprint">SELECT ... FOR SHARE</code>，这样读操作会阻塞其他写操作，使得读写无法并发，只能串行，从而保证严格的一致性。不过这种行为也受到<code class="prettyprint">autocommit</code>变量的影响：<br>
<ul><li>如果禁用了<code class="prettyprint">autocommit</code>，如上所述，则InnoDB会隐式的转换所有的SELECT语句，给其加共享锁</li><li>如果开启了<code class="prettyprint">autocommit</code>，不会进行隐式转换，因为每条语句构成一个事务，所有快照读语句（也就是没有FOR UPDATE|SHARE的SELECT语句）可以被认为是只读的事务，是可以安全并发，不需要阻塞其他事务</li></ul><br>
<br><code class="prettyprint">不可重复读（READ COMMITTED）</code>隔离级别下，和<code class="prettyprint">可重复读</code>隔离级别在行锁方面主要的区别是：<br>
<ul><li><code class="prettyprint">不可重复读</code>隔离级别下取消了间隙锁，临键锁也退化成了记录锁。间隙锁定和临键锁仅用于外键约束检查和重复键检查，也就是说加锁时，如果没有符号条件的查询并不加锁，有符合条件的查询也只会给记录加上记录锁。因为没有了间隙锁，所以会出现幻读问题。</li><li>在<code class="prettyprint">可重复读</code>隔离级别下，加锁时如果查询条件没有命中索引（非ICP的查询），则会给表中每条记录都加上临键锁。而<code class="prettyprint">不可重复读</code>隔离级别下因为没有间隙锁，则会退化成给表中每条数据加上记录锁，并且还会把没有匹配的行上的锁给释放掉，而不是把全表所有记录不管有没有匹配都给锁上。</li></ul><br>
<br><h3>死锁</h3>因为使用表锁时，需要一次性申请所有所需表的锁，所以在只使用表锁的情况下不会出现死锁，一般出现死锁的情况都是行锁。InnoDB有死锁探测机制，在申请锁的时候，都会先进行死锁判断，采用的算法深度优先搜索，并且如果在搜索过程中发现有环，就说明发生了死锁，为了避免死锁检测开销过大，如果搜索深度超过了 200（<code class="prettyprint">LOCK_MAX_DEPTH_IN_DEADLOCK_CHECK</code>）也同样认为发生了死锁。出现死锁时，InnoDB会选择一个回滚代价比较小的事务进行回滚。以下会举几个比较典型的死锁例子（均在可重复度隔离级别下），首先会先建一张测试的表：<br>
<pre class="prettyprint">CREATE TABLE `student` (  <br>
`id` int NOT NULL,  <br>
`uuid` varchar(64) NOT NULL,  <br>
`name` varchar(64) NOT NULL,  <br>
`age` int NOT NULL,  <br>
PRIMARY KEY (`id`),  <br>
UNIQUE KEY `uuid_index` (`uuid`),  <br>
KEY `name_index` (`name`)  <br>
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci<br>
</pre><br>
<h4>死锁例一</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210711/237efcf8f24c116a2b884edd64b87a5c.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210711/237efcf8f24c116a2b884edd64b87a5c.jpg" class="img-polaroid" title="6.jpg" alt="6.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
这是最简单最典型的死锁的情况了，两个事务互相锁定持有资源，并且等待对方的资源，最后形成一个环，死锁出现。最后某个事务回滚，写业务代码的时候，应该对并发条件可能出现这种情况的语句有所警觉。<br>
<h4>死锁例二</h4>前提：事务开始时，<code class="prettyprint">student</code>表里有<code class="prettyprint">id=1</code>的记录。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210711/1ab253bb83c2f065b89e039613f65b3b.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210711/1ab253bb83c2f065b89e039613f65b3b.jpg" class="img-polaroid" title="7.jpg" alt="7.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
两个事务分别对某个记录申请共享锁，因为共享锁性质，两个事务都能获取到。然后又都对这条记录申请排他锁，T3中事务一申请排他锁，等待事务二的共享锁释放，加入锁等待队列，T4中事务二又申请排他锁，于是形成环，死锁条件达成。所以在事务开始时就要想到后面可能会做的操作，提前获取足够强度的锁，而不是中途升级。<br>
<h4>死锁例三</h4>前提：事务开始时，<code class="prettyprint">student</code>表里没有<code class="prettyprint">id=100</code>的记录。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210711/01095ec70e691ad1ff24e6c5082370ac.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210711/01095ec70e691ad1ff24e6c5082370ac.jpg" class="img-polaroid" title="8.jpg" alt="8.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
如上，在可重复读隔离级别下，如果两个事务同时对某个间隙用<code class="prettyprint">SELECT...FOR UPDATE</code>加排他锁，在没有符合该条件记录情况下，两个线程都会加锁成功。程序发现记录尚不存在，就试图插入一条新记录，如果两个线程都这么做，就会出现死锁。因为在记录真正插入之前会加插入意向锁，插入意向锁和间隙锁互斥，所以在T3时，事务一阻塞了，申请插入意向锁排队等待事务二的间隙锁释放，T4时，事务二又申请插入意向锁，需要等待事务一的间隙锁释放，形成环，死锁条件达成。<br>
<br>这种情况一般发生在，某些业务需要提前锁住间隙，防止并发插入同一数据（关键属性相同的数据），也就会先<code class="prettyprint">SELECT...FOR UPDATE</code>再<code class="prettyprint">INSERT</code>，但是这样很容易死锁，可以直接对关键属性建立唯一索引，防止并发插入。<br>
<h4>死锁例四</h4>前提：事务开始时，<code class="prettyprint">student</code>表里没有<code class="prettyprint">uuid=uuid100</code>的记录。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210711/5a73673b930a9e189028162131e286bd.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210711/5a73673b930a9e189028162131e286bd.jpg" class="img-polaroid" title="9.jpg" alt="9.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
这也是MySQL官方文档给出的一个例子。三个事务同时插入一条某个唯一索引属性（上面的uuid）相同的数据，其中某个事务先一步插入，其他两个事务会阻塞等待，然后先一步插入的事务回滚，其他两个事务出现死锁，其中某个事务会被回滚。官方文档还提到了另外一种类似的情况，具体可以参考Locks Set by Different SQL Statements in InnoDB，这种死锁的原因是，<code class="prettyprint">INSERT</code>的时候，会对唯一索引进行Duplicate Key判断，如果唯一键冲突，则会加共享锁等待，也就是T3时候的事务二和事务三，都会获得共享锁。T4时，事务一回滚，事务二和事务三都会申请升级排他锁，这样就造成类似死锁案例二的情况，形成死锁了。<br>
<h4>死锁例五</h4><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210711/fcc84167a001c39f2573a5b1ba013aab.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210711/fcc84167a001c39f2573a5b1ba013aab.jpg" class="img-polaroid" title="10.jpg" alt="10.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
这个例子引用自淘宝数据库内核月报-InnoDB 事务锁系统简介，这个地方的死锁我没有试出来，需要在高并发环境才可能出现，理论上可能会出现。虽然只是两个很简单的更新语句，但是事务一的加锁顺序是，先锁二级索引<code class="prettyprint">name_index</code>，再锁聚集索引，事务二的加锁顺序是，先锁聚集索引，再锁二级索引<code class="prettyprint">name_index</code>，不同的加锁顺序在并发时可能导致死锁。<br>
<h4>死锁小结</h4>使用<code class="prettyprint">SHOW ENGINE INNODB STATUS</code>语句可以看到最近一次的死锁信息，在调试的时候很有帮助。  出现死锁后某个事务会回滚，其他事务成功，上层业务会捕获到死锁错误，再重试一般会成功，如果出现大量锁重试，则说明哪里出了问题，写代码的时候可以注意以下几点可以减少死锁出现的概率：<br>
<ul><li>类似的业务逻辑尽量以固定的顺序访问表和行</li><li>如果业务允许，大事务拆小，大事务持有锁的时间更长，更容易出现死锁</li><li>为表添加合理的索引，可以看到可重复读级别下，如果不走索引（非ICP的查询）将会为表的每一行记录加锁</li><li>尽量少用for share或者for update语句，虽然看起来只是在一行记录上加锁，但是由于间隙锁和临键锁的存在，锁住的可能不止是一行记录</li><li>提前申请足够强度的锁，不要先用for share锁住行，后面再update，很容易死锁。</li></ul><br>
<br><h3>锁的内部表示</h3>在<code class="prettyprint">InnoDB</code>内部中，用<code class="prettyprint">unsigned long</code>类型表示锁的类型，其中不同的位代表锁不同的信息，最低的4位表示lock_mode，中间的4位表示lock_type，其余高位表示record_lock_type，内部使用位操作来设置和判断是否设置了对应的值 ：<br>
<br>| record_lock_type | lock_type | lock_mode | --- | --- | ---<br>
<br><code class="prettyprint">lock_mode</code>：描述了锁的基本类型，分为以下几种：<br>
<ul><li>LOCK_IS：意向共享锁</li><li>LOCK_IX：意向排他锁</li><li>LOCK_S：共享锁</li><li>LOCK_X：排他锁</li><li>LOCK_AUTO_INC：自增锁</li></ul><br>
<br>在源码中有一个lock_mode的枚举类型，除了以上还有几个值：LOCK_NONE，用来表示一致性读，LOCK_NUM用来表示lock_mode的数量，LOCK_NONE_UNSET用来复位低8位。<br>
<br><code class="prettyprint">lock_type</code>：占用中间的4位，目前只用到了5位和6位，分别表示表锁（LOCK_TABLE）和 行锁（LOCK_REC）。<br>
<br><code class="prettyprint">record_lock_type</code>：对于表锁类型来说都是空的，对于行锁目前值有：<br>
<ul><li>LOCK_WAIT：表示正在等待锁</li><li>LOCK_ORDINARY：表示临键锁</li><li>LOCK_GAP：表示间隙锁</li><li>LOCK_REC_NOT_GAP：表示记录锁</li><li>LOCK_INSERT_INTENTION：表示插入意向锁</li><li>LOCK_CONV_BY_OTHER：表示锁是由其它事务创建的（比如隐式锁转换）</li></ul><br>
<br>以上说的是锁的类型的表示，行锁、表锁类型相关信息都统一到一个字段了。同类型字段一样，行锁、表锁本身在<code class="prettyprint">InnoDB</code>中也统一用一个结构体来表示<code class="prettyprint">lock_t</code>，大体如下：<br>
<pre class="prettyprint">struct lock_t &#123;  <br>
trx_t* trx; // 锁所属的事务  <br>
UT_LIST_NODE_T(lock_t) trx_locks; // 事务所持锁的列表  <br>
ulint type_mode; // 锁类型  <br>
hash_node_t hash; // 全局锁哈希表对应的节点  <br>
dict_index_t* index; // 行锁的行记录索引  <br>
union &#123;  <br>
lock_table_t; // 表锁   <br>
lock_rec_t rec_lock; // 行锁  <br>
&#125; un_member; // 锁详情  <br>
&#125;;<br>
</pre><br>
行锁和表锁都用一个<code class="prettyprint">lock_t</code>结构来表示，差异部分在一个union结构中表示，里面的type_mode即是上面介绍的锁类型，行锁的结构如下：<br>
<pre class="prettyprint">struct lock_rec_t &#123;  <br>
ulint space; // 锁的space id  <br>
ulint page_no; // 锁的page number  <br>
ulint n_bits; // 锁住位置的bitmap  <br>
&#125;; <br>
</pre><br>
通过（<code class="prettyprint">space</code>,<code class="prettyprint">page_no</code>）可以确定锁所在的页，<code class="prettyprint">InnoDB</code>内部还会有个字段<code class="prettyprint">heap_no</code>来表示记录在页上的偏移，也就是说三元组（<code class="prettyprint">space</code>，<code class="prettyprint">page_no</code>，<code class="prettyprint">heap_no</code>）可以唯一的确定一行的位置。在分配<code class="prettyprint">lock_rec_t</code>结构的时候，还会为其在最后分配一个大小为n_bits的bitmap，而记录偏移的bit即为<code class="prettyprint">heap_no</code>，用来快速判断这页哪些记录加了锁。<br>
<br><code class="prettyprint">InnoDB</code>所有的行锁会插入到一个全局hash表（<code class="prettyprint">lock_sys</code>-><code class="prettyprint">rec_hash</code>）中，相同（<code class="prettyprint">space</code>,<code class="prettyprint">page_no</code>）也就是同一页的锁会被Hash到同一个bucket里，通过<code class="prettyprint">lock_t</code>-><code class="prettyprint">hash</code>串成链表。<br>
<br>总结一下，就是同一事务，同一类型的行锁在同一页上会复用同一个锁结构<code class="prettyprint">lock_t</code>，用后面的bitmap来具体表示锁哪些行，大大节约了空间。同一页上不同的事物或类型的锁通过链表串起来放在<code class="prettyprint">rec_hash</code>的同一个bucket里，利用hash的结构先定位到页，然后遍历同一页上不同的<code class="prettyprint">lock_t</code>，就可以得到哪些事物的哪些锁锁住了哪些行，这种设计平衡了时间和空间的效率。<br>
<h3>总结</h3>InnoDB锁系统配合MVCC机制一起实现了事务的<code class="prettyprint">一致性</code>和<code class="prettyprint">隔离性</code>，InnoDB中的锁总类繁多，并且和事务隔离级别关系密切，不同语句在不同隔离级别下的加锁情况大有不同，细节尤其多，而了解这些对排查死锁会有很大的帮助。行锁在InnoDB中的实现也颇为巧妙，值得学习。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/8KfGmK14gOxByJ6ASaGWcQ" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/8KfGmK14gOxByJ6ASaGWcQ</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            