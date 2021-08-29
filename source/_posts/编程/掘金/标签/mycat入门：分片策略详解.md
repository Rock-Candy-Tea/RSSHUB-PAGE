
---
title: 'mycat入门：分片策略详解'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=4977'
author: 掘金
comments: false
date: Sat, 28 Aug 2021 18:17:52 GMT
thumbnail: 'https://picsum.photos/400/300?random=4977'
---

<div>   
<div class="markdown-body html cache"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>这是我参与8月更文挑战的第29天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
</blockquote>
<p>分片策略为数据表的拆分原则，了解即可。</p>
<h3 data-id="heading-0">1.分片枚举</h3>
<p>通过在配置文件中配置可能的枚举 id，自己配置分片，本规则适用于特定的场景，比如有些业务需要按照省 份或区县来做保存，而全国省份区县固定的，这类业务使用本条规则，配置如下：</p>
<pre><code class="copyable"><tableRule name="sharding-by-intfile">
<rule>
<columns>user_id</columns>
<algorithm>hash-int</algorithm>
</rule>
</tableRule>
<function name="hash-int" class="io.mycat.route.function.PartitionByFileMap">
<property name="mapFile">partition-hash-int.txt</property>
<property name="type">0</property>
<property name="defaultNode">0</property>
</function>
partition-hash-int.txt 配置：
10000=0
10010=1
DEFAULT_NODE=1
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">上面 columns 标识将要分片的表字段，algorithm 分片函数，
其中分片函数配置中，mapFile 标识配置文件名称，type 默认值为 0，0 表示 Integer，非零表示 String，
所有的节点配置都是从 0 开始，及 0 代表节点 1
/**
* defaultNode 默认节点:小于 0 表示不设置默认节点，大于等于 0 表示设置默认节点
* 默认节点的作用：枚举分片时，如果碰到不识别的枚举值，就让它路由到默认节点
* 如果不配置默认节点（defaultNode 值小于 0 表示不配置默认节点），碰到
* 不识别的枚举值就会报错，
* like this：can’t find datanode for sharding column:column_nameval:ffffffff
*/
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">2.固定分片 hash 算法</h3>
<p>本条规则类似于十进制的求模运算，区别在于是二进制的操作,是取 id 的二进制低 10 位，即 id 二进制 &1111111111。 此算法的优点在于如果按照 10 进制取模运算，在连续插入 1-10 时候 1-10 会被分到 1-10 个分片，增 大了插入的事务控制难度，而此算法根据二进制则可能会分到连续的分片，减少插入事务事务控制难度。</p>
<pre><code class="copyable"><tableRule name="rule1">
<rule>
<columns>user_id</columns>
<algorithm>func1</algorithm>
</rule>
</tableRule>
<function name="func1" class="io.mycat.route.function.PartitionByLong">
<property name="partitionCount">2,1</property>
<property name="partitionLength">256,512</property>
</function>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">配置说明：
上面 columns 标识将要分片的表字段，algorithm 分片函数，
partitionCount 分片个数列表，partitionLength 分片范围列表
分区长度:默认为最大 2^n=1024 ,即最大支持 1024 分区
约 束 :
count,length 两个数组的长度必须是一致的。
1024 = sum((count[i]*length[i])). count 和 length 两个向量的点积恒等于 1024
用法例子：
本例的分区策略：希望将数据水平分成 3 份，前两份各占 25%，第三份占 50%。（故本例非均匀分区）
// |<———————1024———————————>|
// |<—-256—>|<—-256—>|<———-512————->|
// | partition0 | partition1 | partition2 |
// | 共 2 份,故 count[0]=2 | 共 1 份，故 count[1]=1 |
int[] count = new int[] &#123; 2, 1 &#125;;
int[] length = new int[] &#123; 256, 512 &#125;;
PartitionUtil pu = new PartitionUtil(count, length);
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">// 下面代码演示分别以 offerId 字段或 memberId 字段根据上述分区策略拆分的分配结果
int DEFAULT_STR_HEAD_LEN = 8; // cobar 默认会配置为此值
long offerId = 12345;
String memberId = "qiushuo";
// 若根据 offerId 分配，partNo1 将等于 0，即按照上述分区策略，offerId 为 12345 时将会被分配
到 partition0 中
int partNo1 = pu.partition(offerId);
// 若根据 memberId 分配，partNo2 将等于 2，即按照上述分区策略，memberId 为 qiushuo 时将会被
分到 partition2 中
int partNo2 = pu.partition(memberId, 0, DEFAULT_STR_HEAD_LEN);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果需要平均分配设置：平均分为 4 分片，partitionCount*partitionLength=1024</p>
<pre><code class="copyable"><function name="func1" class="io.mycat.route.function.PartitionByLong">
<property name="partitionCount">4</property>
<property name="partitionLength">256</property>
</function>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">3.范围约定</h3>
<p>此分片适用于，提前规划好分片字段某个范围属于哪个分片， start <= range <= end. range start-end ,data node index K=1000,M=10000.</p>
<pre><code class="copyable"><tableRule name="auto-sharding-long">
<rule>
<columns>user_id</columns>
<algorithm>rang-long</algorithm>
</rule>
</tableRule>
<function name="rang-long" class="io.mycat.route.function.AutoPartitionByLong">
<property name="mapFile">autopartition-long.txt</property>
<property name="defaultNode">0</property>
</function>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">配置说明：
上面 columns 标识将要分片的表字段，algorithm 分片函数，
rang-long 函数中 mapFile 代表配置文件路径
defaultNode 超过范围后的默认节点。
所有的节点配置都是从 0 开始，及 0 代表节点 1，此配置非常简单，即预先制定可能的 id 范围到某个分片
0-500M=0
500M-1000M=1
1000M-1500M=2
或
0-10000000=0
10000001-20000000=1
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">4.取模</h3>
<p>此规则为对分片字段求摸运算</p>
<pre><code class="copyable"><tableRule name="mod-long">
<rule>
<columns>user_id</columns>
<algorithm>mod-long</algorithm>
</rule>
</tableRule>
<function name="mod-long" class="io.mycat.route.function.PartitionByMod">
<!-- how many data nodes -->
<property name="count">3</property>
</function>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">配置说明：
上面 columns 标识将要分片的表字段，algorithm 分片函数，
此种配置非常明确即根据 id 进行十进制求模预算，相比固定分片 hash，此种在批量插入时可能存在批量插入单
事务插入多数据分片，增大事务一致性难度。
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">5.按日期（天）分片</h3>
<p>此规则为按天分片。</p>
<pre><code class="copyable"><tableRule name="sharding-by-date">
<rule>
<columns>create_time</columns>
<algorithm>sharding-by-date</algorithm>
</rule>
</tableRule>
<function name="sharding-by-date" class="io.mycat.route.function.PartitionByDate">
<property name="dateFormat">yyyy-MM-dd</property>
<property name="sBeginDate">2014-01-01</property>
<property name="sEndDate">2014-01-02</property>
<property name="sPartionDay">10</property>
</function>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">配置说明：
columns ：标识将要分片的表字段
algorithm ：分片函数
dateFormat ：日期格式
sBeginDate ：开始日期
sEndDate：结束日期
sPartionDay ：分区天数，即默认从开始日期算起，分隔 10 天一个分区
如果配置了 sEndDate 则代表数据达到了这个日期的分片后后循环从开始分片插入。
Assert.assertEquals(true, 0 == partition.calculate(“2014-01-01”));
Assert.assertEquals(true, 0 == partition.calculate(“2014-01-10”));
Assert.assertEquals(true, 1 == partition.calculate(“2014-01-11”));
Assert.assertEquals(true, 12 == partition.calculate(“2014-05-01”));
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">6.取模范围约束</h3>
<p>此种规则是取模运算与范围约束的结合，主要为了后续数据迁移做准备，即可以自主决定取模后数据的节点 分布。</p>
<pre><code class="copyable"><tableRule name="sharding-by-pattern">
<rule>
<columns>user_id</columns>
<algorithm>sharding-by-pattern</algorithm>
</rule>
</tableRule>
<function name="sharding-by-pattern" class="io.mycat.route.function.PartitionByPattern"
<property name="patternValue">256</property>
<property name="defaultNode">2</property>
<property name="mapFile">partition-pattern.txt</property>
</function>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>partition-pattern.txt</p>
<pre><code class="copyable">partition-pattern.txt
# id partition range start-end ,data node index
###### first host configuration
1-32=0
33-64=1
65-96=2
97-128=3
######## second host configuration
129-160=4
161-192=5
193-224=6
225-256=7
0-0=7
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">配置说明：
上面 columns 标识将要分片的表字段，algorithm 分片函数，patternValue 即求模基数，defaoultNode
默认节点，如果配置了默认，则不会按照求模运算
mapFile 配置文件路径
配置文件中，1-32 即代表 id%256 后分布的范围，如果在 1-32 则在分区 1，其他类推，如果 id 非数据，则
会分配在 defaoultNode 默认节点
String idVal = “0”;
Assert.assertEquals(true, 7 == autoPartition.calculate(idVal));
idVal = “45a”;
Assert.assertEquals(true, 2 == autoPartition.calculate(idVal));
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">7.截取数字做 hash 求模范围约束</h3>
<p>此种规则类似于取模范围约束，此规则支持数据符号字母取模。</p>
<pre><code class="copyable"><tableRule name="sharding-by-prefixpattern">
<rule>
<columns>user_id</columns>
<algorithm>sharding-by-prefixpattern</algorithm>
</rule>
</tableRule>
<function name="sharding-by-pattern"
class="io.mycat.route.function.PartitionByPrefixPattern">
<property name="patternValue">256</property>
<property name="prefixLength">5</property>
<property name="mapFile">partition-pattern.txt</property>
</function>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>partition-pattern.txt</p>
<pre><code class="copyable">partition-pattern.txt
# range start-end ,data node index
# ASCII
# 8-57=0-9 阿拉伯数字
# 64、65-90=@、A-Z
# 97-122=a-z
###### first host configuration
1-4=0
5-8=1
9-12=2
13-16=3
###### second host configuration
17-20=4
21-24=5
25-28=6
29-32=7
0-0=7
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">配置说明：
上面 columns 标识将要分片的表字段，algorithm 分片函数，patternValue 即求模基数，prefixLength
ASCII 截取的位数
mapFile 配置文件路径
配置文件中，1-32 即代表 id%256 后分布的范围，如果在 1-32 则在分区 1，其他类推
此种方式类似方式 6 只不过采取的是将列种获取前 prefixLength 位列所有 ASCII 码的和进行求模
sum%patternValue ,获取的值，在范围内的分片数，
String idVal=“gf89f9a”;
Assert.assertEquals(true, 0==autoPartition.calculate(idVal));
idVal=“8df99a”;
Assert.assertEquals(true, 4==autoPartition.calculate(idVal));
idVal=“8dhdf99a”;
Assert.assertEquals(true, 3==autoPartition.calculate(idVal));
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">8.应用指定</h3>
<p>此规则是在运行阶段有应用自主决定路由到那个分片。</p>
<pre><code class="copyable"><tableRule name="sharding-by-substring">
<rule>
<columns>user_id</columns>
<algorithm>sharding-by-substring</algorithm>
</rule>
</tableRule>
<function name="sharding-by-substring"
class="io.mycat.route.function.PartitionDirectBySubString">
<property name="startIndex">0</property><!-- zero-based -->
<property name="size">2</property>
<property name="partitionCount">8</property>
<property name="defaultPartition">0</property>
</function>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">配置说明：
上面 columns 标识将要分片的表字段，algorithm 分片函数
此方法为直接根据字符子串（必须是数字）计算分区号（由应用传递参数，显式指定分区号）。
例如 id=05-100000002
在此配置中代表根据 id 中从 startIndex=0，开始，截取 siz=2 位数字即 05，05 就是获取的分区，如果没传
默认分配到 defaultPartition
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">9.截取数字 hash 解析</h3>
<p>此规则是截取字符串中的 int 数值 hash 分片。</p>
<pre><code class="copyable"><tableRule name="sharding-by-stringhash">
<rule>
<columns>user_id</columns>
<algorithm>sharding-by-stringhash</algorithm>
</rule>
</tableRule>
<function name="sharding-by-stringhash"
class="io.mycat.route.function.PartitionByString">
<property name="partitionLength">512</property><!-- zero-based -->
<property name="partitionCount">2</property>
<property name="hashSlice">0:2</property>
</function>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">配置说明：
上面 columns 标识将要分片的表字段，algorithm 分片函数
函数中 partitionLength 代表字符串 hash 求模基数，
partitionCount 分区数，
hashSlice hash 预算位，即根据子字符串中 int 值 hash 运算
hashSlice ： 0 means str.length(), -1 means str.length()-1
/**
* “2” -> (0,2)
* “1:2” -> (1,2)
* “1:” -> (1,0)
* “-1:” -> (-1,0)
* “:-1” -> (0,-1)
* “:” -> (0,0)
*/
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">例子：
String idVal=null;
rule.setPartitionLength("512");
rule.setPartitionCount("2");
rule.init();
rule.setHashSlice("0:2");
// idVal = "0";
// Assert.assertEquals(true, 0 == rule.calculate(idVal));
// idVal = "45a";
// Assert.assertEquals(true, 1 == rule.calculate(idVal));
//last 4
rule = new PartitionByString();
rule.setPartitionLength("512");
rule.setPartitionCount("2");
rule.init();
//last 4 characters
rule.setHashSlice("-4:0");
idVal = "aaaabbb0000";
Assert.assertEquals(true, 0 == rule.calculate(idVal));
idVal = "aaaabbb2359";
Assert.assertEquals(true, 0 == rule.calculate(idVal));
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">10.一致性 hash</h3>
<p>一致性hash有效解决了分布式数据的扩容问题。</p>
<pre><code class="copyable"><tableRule name="sharding-by-murmur">
<rule>
<columns>user_id</columns>
<algorithm>murmur</algorithm>
</rule>
</tableRule>
<function name="murmur" class="io.mycat.route.function.PartitionByMurmurHash">
<property name="seed">0</property><!-- 默认是 0-->
<property name="count">2</property><!-- 要分片的数据库节点数量，必须指定，否则没法分片-->
<property name="virtualBucketTimes">160</property><!-- 一个实际的数据库节点被映射为这么多虚拟节点，默认是 160 倍，也就是虚拟节点数是物理节点数的 160 倍-->
<!--
<property name="weightMapFile">weightMapFile</property>
节点的权重，没有指定权重的节点默认是 1。以 properties 文件的格式填写，以从 0 开始到 count-1 的整数值也就
是节点索引为 key，以节点权重值为值。所有权重值必须是正整数，否则以 1 代替 -->
<!--
<property name="bucketMapPath">/etc/mycat/bucketMapPath</property>
用于测试时观察各物理节点与虚拟节点的分布情况，如果指定了这个属性，会把虚拟节点的 murmur hash 值与物理节
点的映射按行输出到这个文件，没有默认值，如果不指定，就不会输出任何东西 -->
</function>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">11.按单月小时拆分</h3>
<p>此规则是单月内按照小时拆分，最小粒度是小时，可以一天最多 24 个分片，最少 1 个分片，一个月完后下月 从头开始循环。 每个月月尾，需要手工清理数据。</p>
<pre><code class="copyable"><tableRule name="sharding-by-hour">
<rule>
<columns>create_time</columns>
<algorithm>sharding-by-hour</algorithm>
</rule>
</tableRule>
<function name="sharding-by-hour" class="io.mycat.route.function.LatestMonthPartion">
<property name="splitOneDay">24</property>
</function>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置说明： columns： 拆分字段，字符串类型（yyyymmddHH） splitOneDay ： 一天切分的分片数</p>
<pre><code class="copyable">LatestMonthPartion partion = new LatestMonthPartion();
partion.setSplitOneDay(24);
Integer val = partion.calculate("2015020100");
assertTrue(val == 0);
val = partion.calculate("2015020216");
assertTrue(val == 40);
val = partion.calculate("2015022823");
assertTrue(val == 27 * 24 + 23);
Integer[] span = partion.calculateRange("2015020100", "2015022823");
assertTrue(span.length == 27 * 24 + 23 + 1);
assertTrue(span[0] == 0 && span[span.length - 1] == 27 * 24 + 23);
span = partion.calculateRange("2015020100", "2015020123");
assertTrue(span.length == 24);
assertTrue(span[0] == 0 && span[span.length - 1] == 23);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">12.范围求模分片</h3>
<p>先进行范围分片计算出分片组，组内再求模 优点可以避免扩容时的数据迁移，又可以一定程度上避免范围分片的热点问题 综合了范围分片和求模分片的优点，分片组内使用求模可以保证组内数据比较均匀，分片组之间是范围分片可以 兼顾范围查询。 最好事先规划好分片的数量，数据扩容时按分片组扩容，则原有分片组的数据不需要迁移。由于分片组内数据比 较均匀，所以分片组内可以避免热点数据问题。</p>
<pre><code class="copyable"><tableRule name="auto-sharding-rang-mod">
<rule>
<columns>id</columns>
<algorithm>rang-mod</algorithm>
</rule>
</tableRule>
<function name="rang-mod"
class="io.mycat.route.function.PartitionByRangeMod">
<property name="mapFile">partition-range-mod.txt</property>
<property name="defaultNode">21</property>
</function>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">配置说明：
上面 columns 标识将要分片的表字段，algorithm 分片函数，
rang-mod 函数中 mapFile 代表配置文件路径
defaultNode 超过范围后的默认节点顺序号，节点从 0 开始。
partition-range-mod.txt
range start-end ,data node group size
以下配置一个范围代表一个分片组，=号后面的数字代表该分片组所拥有的分片的数量。
0-200M=5 //代表有 5 个分片节点
200M1-400M=1
400M1-600M=4
600M1-800M=4
800M1-1000M=6
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">13.日期范围 hash 分片</h3>
<p>思想与范围求模一致，当由于日期在取模会有数据集中问题，所以改成 hash 方法。 先根据日期分组，再根据时间 hash 使得短期内数据分布的更均匀 优点可以避免扩容时的数据迁移，又可以一定程度上避免范围分片的热点问题 要求日期格式尽量精确些，不然达不到局部均匀的目的</p>
<pre><code class="copyable"><tableRule name="rangeDateHash">
<rule>
<columns>col_date</columns>
<algorithm>range-date-hash</algorithm>
</rule>
</tableRule>
<function name="range-date-hash"
class="io.mycat.route.function.PartitionByRangeDateHash">
<property name="sBeginDate">2014-01-01 00:00:00</property>
<property name="sPartionDay">3</property>
<property name="dateFormat">yyyy-MM-dd HH:mm:ss</property>
<property name="groupPartionSize">6</property>
</function>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>sPartionDay 代表多少天分一个分片
groupPartionSize 代表分片组的大小</p>
<h3 data-id="heading-13">14.冷热数据分片</h3>
<p>根据日期查询日志数据 冷热数据分布 ，最近 n 个月的到实时交易库查询，超过 n 个月的按照 m 天分片。</p>
<pre><code class="copyable"><tableRule name="sharding-by-date">
<rule>
<columns>create_time</columns>
<algorithm>sharding-by-hotdate</algorithm>
</rule>
</tableRule>
<function name="sharding-by-hotdate" class="io.mycat.route.function.PartitionByHotDate">
<property name="dateFormat">yyyy-MM-dd</property>
<property name="sLastDay">10</property>
<property name="sPartionDay">30</property>
</function>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">15.自然月分片</h3>
<p>按月份列分区 ，每个自然月一个分片，格式 between 操作解析的范例。</p>
<pre><code class="copyable"><tableRule name="sharding-by-month">
<rule>
<columns>create_time</columns>
<algorithm>sharding-by-month</algorithm>
</rule>
</tableRule>
<function name="sharding-by-month" class="io.mycat.route.function.PartitionByMonth">
<property name="dateFormat">yyyy-MM-dd</property>
<property name="sBeginDate">2014-01-01</property>
</function>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置说明：</p>
<ul>
<li>columns： 分片字段，字符串类型</li>
<li>dateFormat ： 日期字符串格式</li>
<li>sBeginDate ： 开始日期</li>
</ul>
<pre><code class="copyable">PartitionByMonth partition = new PartitionByMonth();
partition.setDateFormat("yyyy-MM-dd");
partition.setsBeginDate("2014-01-01");
partition.init();
Assert.assertEquals(true, 0 == partition.calculate("2014-01-01"));
Assert.assertEquals(true, 0 == partition.calculate("2014-01-10"));
Assert.assertEquals(true, 0 == partition.calculate("2014-01-31"));
Assert.assertEquals(true, 1 == partition.calculate("2014-02-01"));
Assert.assertEquals(true, 1 == partition.calculate("2014-02-28"));
Assert.assertEquals(true, 2 == partition.calculate("2014-03-1"));
Assert.assertEquals(true, 11 == partition.calculate("2014-12-31"));
Assert.assertEquals(true, 12 == partition.calculate("2015-01-31"));
Assert.assertEquals(true, 23 == partition.calculate("2015-12-31"));
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">16.有状态分片算法</h3>
<p>有状态分片算法与之前的分片算法不同,它是为数据自动迁移而设计的. 直至 2018 年 7 月 24 日为止,现支持有状态算法的分片策略只有 crc32slot 欢迎大家提供更多有状态分片算法.</p>
<p>一个有状态分片算法在使用过程中暂时存在两个操作</p>
<p>一种是初始化,使用 mycat 创建配置带有有状态分片算法的 table 时(推介)或者第一次配置有状态分片算法的 table 并启动 mycat 时,有状态分片算法会根据表的 dataNode 的数量划分分片范围并生成 ruledata 下的文件, 这个分片范围规则就是’状态’,一个表对应一个状态,对应一个有状态分片算法实例,以及对应一个满足以下命 名规则的文件:</p>
<p>算法名字_schema 名字_table 名字.properties 文件里内容一般具有以下特征：</p>
<pre><code class="copyable">8=91016-102399
7=79639-91015
6=68262-79638
5=56885-68261
4=45508-56884
3=34131-45507
2=22754-34130
1=11377-22753
0=0-11376
<span class="copy-code-btn">复制代码</span></code></pre>
<p>行数就是 table 的分片节点数量,每行的’数字-数字’就是分片算法生成的范围,这个范围与具体算法实现有关, 一个分片节点可能存在多个范围,这些范围以逗号,分隔.一般来说,不要手动更改这个文件,应该使用算法生成范围, 而且需要注意的是,物理库上的数据的分片字段的值一定要落在对应范围里. 一种是添加操作,即数据扩容,具体参考第六章的 6.8 与 6.9 添加节点,有状态分片算法根据节点的变化,重新分配范围规则,之后执行数据自动迁移任务.</p>
<h3 data-id="heading-16">17.crc32slot 分片算法</h3>
<p>crc32solt 是有状态分片算法的实现之一,具体参考第六章 数据自动迁移方案设计 crc32(key)%102400=slot</p>
<p>slot 按照范围均匀分布在 dataNode 上,针对每张表进行实例化，通过一个文件记录 slot 和节点 映射关系，迁移过程中通过 zk 协调 其中需要在分片表中增加 slot 字段，用以避免迁移时重新计算，只需要迁移对应 slot 数据即可 分片最大个数为 102400 个，短期内应该够用，每分片一千万，总共可以支持一万亿数据 配置说明:</p>
<pre><code class="copyable"><table name="travelrecord" dataNode="dn1,dn2" rule="crc32slot" />
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">18.使用 mycat 配置完表后使用 mycat 创建表</h3>
<pre><code class="copyable">USE TESTDB;
CREATE TABLE `travelrecord`
( id xxxx
xxxxxxx
) ENGINE=INNODB DEFAULT CHARSET=utf8;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            