
---
title: '简述时序数据库Influxdb：TSM引擎.'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7874b0ea8a184477ab9b451b582f9ef2~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 03:26:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7874b0ea8a184477ab9b451b582f9ef2~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Influxdb .</h1>
<blockquote>
<p>我这里主要针对Influxdb2.0做一些分享.</p>
</blockquote>
<h2 data-id="heading-1">🔖 一、基本概念.</h2>
<blockquote>
<p>一些时序数据库中的基本概念。</p>
</blockquote>
<h3 data-id="heading-2">1.1 基本概念.</h3>
<ul>
<li>
<p>时序数据库的概念.</p>
<ol>
<li>
<p>什么是时序数据库：时序数据库就是随着时间不短产生的一系列数据，简单点来说就是带时间戳的数据。也可以这样理解，时间序列是一连串基于时间的数据点，他们主要以时间为索引，描述了某个被测量主题在每个时间点被测量的值.</p>
<p>时序数据的主要特点就是数据量大，写多读少、几乎不进行更新和删除操作.</p>
</li>
</ol>
</li>
<li>
<p>时序数据的特点：数据量大、写多读少、几乎不进行更新和删除操作.</p>
</li>
<li>
<p>Influxdb 和 MySQL 之间的对比.</p>
</li>
<li>
<p>性能分析.</p>
<ul>
<li>和其他时序数据库性能对比.</li>
<li>和传统数据库之间的对比.</li>
</ul>
</li>
<li>
<p><code>influxdb</code>优点：</p>
<ul>
<li>独立部署.</li>
<li>TSM存储引擎，高写、数据压缩.</li>
<li>灵活支持TAG写入.</li>
<li>Tag索引.</li>
<li>灵活的数据保留.RP.</li>
</ul>
</li>
<li>
<p>基本概念：</p>
<ul>
<li>
<p>influxdb 中的基本概念.</p>





























<table><thead><tr><th>Influxdb</th><th>SQL</th></tr></thead><tbody><tr><td>Bucket</td><td>database</td></tr><tr><td>measurement</td><td>table</td></tr><tr><td>point</td><td>row</td></tr><tr><td>tag</td><td>有索引的列</td></tr><tr><td>field</td><td>没有索引的列</td></tr></tbody></table>
</li>
<li>
<p>series 数据结构：表示的含义是：相同measurement 和 tags 的都属于同一个series. 同一个Block里面一定都是同一个Series，但是一个Series，并不仅仅存在一个Block里面.  <strong>下文经常出现的：SeriesKey=measurement+tags</strong>，这里应该是tagk=tagv,否则是没有意义的. 因为Tag是用来给数据进行打标的。</p>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-keyword">type</span> Series <span class="hljs-keyword">struct</span> &#123;
    mu          sync.RWMutex
    Key         <span class="hljs-keyword">string</span>              <span class="hljs-comment">// series key</span>
    Tags        <span class="hljs-keyword">map</span>[<span class="hljs-keyword">string</span>]<span class="hljs-keyword">string</span>   <span class="hljs-comment">// tags</span>
    id          <span class="hljs-keyword">uint64</span>              <span class="hljs-comment">// id</span>
    measurement *Measurement        <span class="hljs-comment">// measurement</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
</ul>
<h3 data-id="heading-3">1.2 适用场景分析.</h3>
<p>什么场景下需要使用时序数据库：一切数据和时间序列有关系的都可以使用influxdb来进行存储。下面具体分析分析.</p>
<ul>
<li><strong>数据监控</strong>：后台程序数据收集、分析.</li>
<li>**服务器监控：**服务器CPU、内存监控.</li>
<li><strong>事件跟踪</strong>： 跟踪事件的状态. 一个事件的状态时随时间相关的，比如START扫码买会员.</li>
<li><strong>日志监控</strong>：日志也是和时间序列相关的，所以也可以使用influxdb来进行存储和展示.</li>
<li><strong>用户行为</strong>：跟踪用户的行为. 用户在打开START之后，其所有的行为是在时间线上的.</li>
<li><strong>DevOps</strong>：IT基础设施和应用的运维系统，采集、分析、设备运行和应用服务运行监控指标。<strong>DevOps</strong> 是一系列整合软件开发和软件运维活动的实践。目标是缩短软件开发周期并使用持续交付提供高质量的软件.</li>
</ul>
<h3 data-id="heading-4">1.3 使用方法.</h3>
<ul>
<li>
<p>2.0 之前可以使用<code>InfluxQL</code>来进行操作，和SQL类似.</p>
<pre><code class="copyable">show databases;
show measurements;
insert measurement,tagk1=tagv1,tagk2=tagv2 field1=value1,field2=value2
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>2.0版本需要使用<code>Flux</code>来进行操作.</p>
<p>下面含义表示：查询<code>bucket</code>为<code>mzx</code>中的数据，查询的是距离当前时间1天之内的数据。根据<code>measurement</code>进行过滤.</p>
<pre><code class="hljs language-go copyable" lang="go">from(bucket: <span class="hljs-string">"mzx"</span>)
  |> <span class="hljs-keyword">range</span>(start: <span class="hljs-number">-1</span>d)
  |> filter(fn: (r) => r[<span class="hljs-string">"_measurement"</span>] == <span class="hljs-string">"student"</span>)
  |> sort()
  |> yield(name: <span class="hljs-string">"sort"</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以通过下面的方式快速构建<code>Flux</code>查询语句.</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7874b0ea8a184477ab9b451b582f9ef2~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image-20210805160629687" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<h3 data-id="heading-5">2.3  客户端使用方法.</h3>
<p>目前支持如下客户端： 使用方法也很简单.</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e88ea6290e44f8b925e70f1f8b70e32~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image-20210805161251843" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">🔖 三、TSM 引擎. (技术选型)</h2>
<blockquote>
<p>Influxdb 引擎的技术选型也是很有意思的.</p>
</blockquote>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fjasper-zhang1.gitbooks.io%2Finfluxdb%2Fcontent%2FConcepts%2Fstorage_engine.html" target="_blank" rel="nofollow noopener noreferrer" title="https://jasper-zhang1.gitbooks.io/influxdb/content/Concepts/storage_engine.html" ref="nofollow noopener noreferrer">存储引擎 · InfluxDB中文文档 (gitbooks.io)</a></p>
</blockquote>
<p>**首先，我们先了解下问什么Influxdb选择自研TSM存储引擎：**Influxdb 早期也就是0.8版本中允许多个存储引擎，包括<code>LevelDB</code>、<code>RocksDB</code>、<code>LMDB</code>、<code>HyperLevelDB</code>，而Influxdb0.9版本使用<code>BoltDB</code>作为存储引擎，而0.11+版本支持的TSM存储引擎在0.9.5版本中发布.  其最终实现结果是：比B+Tree实现高达45倍的磁盘空间使用量的减少，甚至比使用LevelDB及其变体有更高的写入吞吐量和压缩率。</p>
<p>当我们首先使用<code>LevelDB</code>（基于LSM树），LevelDB 带来的两大优势是写入吞吐量高、内置压缩，然而如果使用LevelDB，那么就会遇到下面的问题：LevelDB 不支持热备份，如果要对数据库进行安全备份，则必须将其关闭，然后将其复制。</p>
<p><code>RocksDB</code>和<code>HyperLevelDB</code>解决了这个问题，但是还有一个更为紧迫的问题：那就是用户自动管理数据保留的方法，这意味着我们需要大量的删除，在LSM树中，删除（<code>LSM</code>树删除其实也是通过向WAL写入特殊删除来进行删除，其并不会立即删除）与写入同样昂贵，为了避免删除操作，我们将数据分割成<code>Shrad</code>数据，这些数据是连续的时间块，Shard 通常会持有一天或者7天内的数据，每个Shard 映射到底层的LevelDB，同样这个意味着我们需要关闭数据库来删除底层文件到达删除一天的数据的目的。</p>
<p>为了解决上面出现的问题，<code>RockesDB</code>的用户提出一个<code>ColumnFamilies</code>的功能：将时间序列数据放入Rocks时，通常将时间块分成列族，然后在时间到达时删除他们，但是新的问题又来了：当InfluxDB中又大量数据时，LevelDB将数据分解成许多小文件，最终造成了一个问题就是：有一年的数据的用户将用尽文件句柄，将任何数据库推演到极致都会遇到这个问题。</p>
<p>为了解决文件句柄用尽的问题，Influxdb 决定将引擎转移到<code>BoltDB</code>（0.9.0-0.9.2），BoltDB 是一个纯粹的Golang数据库，它具有与LevelDB相同的API语言：<code>keyspace</code>有序的存储. BoltDB对我们来说最大的好出就是使用单个文件作为数据库，这解决了<code>RocksDB</code>文件句柄过多的问题. 但是在运行一段时间之后，发现，在数据库超过几GB之后，IOPS开始成为影响Influxdb的性能瓶颈.  在 <code>0.9.3-0.9.4</code>版本的发布，我们在写之前加一个WAL，这样可以减少随机插入的<code>keyspace</code>的数量. 但是这，高<code>IOPS</code>仍然是一个问题。</p>
<p>于是TSM就出现了.</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17601efc972345618ce1e5e4dd616d23~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image-20210805175948408" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">3.1 存储引擎TSM Tree.</h3>
<blockquote>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fblog.fatedier.com%2F2016%2F08%2F05%2Fdetailed-in-influxdb-tsm-storage-engine-one%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://blog.fatedier.com/2016/08/05/detailed-in-influxdb-tsm-storage-engine-one/" ref="nofollow noopener noreferrer">InfluxDB详解之TSM存储引擎解析（一） (fatedier.com)</a></p>
</blockquote>
<p>每一个Shard中都包含一个TSM引擎.</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f097ef440d74d3d98879fd4f64e96ac~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image-20210803163448681" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>了解各个组件：</strong></p>
<ul>
<li>
<p><code>Cache</code>：相当于是LSM Tree中的 MemTable，在内存中一个简单的<code>map</code>结构，这里的key为<code>serieskey</code>（measurement+所有tags的序列化字符串.） + <code>分隔符</code>+ <code>filedName</code>，map的<code>Value</code>是一个数组.</p>
<p>可以理解Cache为当前WAL在内存中的数据，因为写入数据时，会先向WAL中写入数据，之后会在想Cache中写入数据.Cache中的数据并不是无限增长的，有一个<code>maxSize</code>（默认是<code>25M</code>）参数用于控制当前Cache中的阈值，当到达阈值后，会将当前的Cache进行一次快照，之后会清空当前的Cache中的内容，再创建一个新的WAL文件用于进行新的写入，剩下的WAL文件会被清除，快照中的数据经过时间排序之后写入新的TSM文件中.</p>
</li>
<li>
<p><code>WAL</code>：WAL 中的内容与<code>Cache</code>中的内容是相同，其作用为了持久化当前在内存Cache中的数据，当系统崩溃之后可以通过WAL文件恢复还没有写入到TSM文件中的数据. 这里要说明一下：数据是顺序追加到WAL文件末尾的， 所以其写入效率非常高.</p>
<p>WAL 文件结构：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/51adcc9ac95d43eda28efe8eb4bde524~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image-20210804203921520" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Type：该项目中的Value类型.</p>
<p>Key Len：指明Key的长度.</p>
<p>Key：key的值：measument + tags + fieldName</p>
<p>Count：同一个Key下数据的个数.（从时间戳、Series中考虑）</p>
<p>Time：单个Value的时间戳.</p>
<p>Value：存储Value的具体内容.</p>
</li>
<li>
<p><code>TSM File</code>：TSM File 使用了自己设计的格式，对查询性能以及压缩方面进行了很多优化，具体如下；</p>
<pre><code class="hljs language-go copyable" lang="go">┌────────┬────────────────────────────────────┬
│ Header │               Blocks               │    Index    │    Footer   │
│<span class="hljs-number">5</span> bytes │              N bytes               │   N bytes   │   <span class="hljs-number">4</span> bytes   │
└────────┴────────────────────────────────────┴
<span class="copy-code-btn">复制代码</span></code></pre>
<p>重点说一下<code>Blocks</code>和<code>Index</code></p>
<p>每个block内存储的是某个TimeSeries的一段时间范围内的值，即某个时间段下某个measurement的某组tag set 对应的某个field的所有值，block内部会根据field不同的值类型采取不同的压缩策略。</p>
<p>块是成对的CRC32校验和和数据序列，CRC32用于块级错误检测，块的长度存储在索引中.</p>
<pre><code class="hljs language-go copyable" lang="go">┌────────────────────────────────────────
│                          Blocks                           │
├───────────────────┬───────────────────┬
│      Block <span class="hljs-number">1</span>      │      Block <span class="hljs-number">2</span>      │      Block N      │
├─────────┬─────────┼─────────┬─────────┼
│  CRC    │  Data   │  CRC    │  Data   │  CRC    │  Data   │
│ <span class="hljs-number">4</span> bytes │ N bytes │ <span class="hljs-number">4</span> bytes │ N bytes │ <span class="hljs-number">4</span> bytes │ N bytes │
└─────────┴─────────┴─────────┴─────────┴
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>下面是Index部分</strong>：文件内的索引信息保存了 每个TimeSeries下所有的数据Block的位置信息，索引数据按照TimeSeries的Key（measurement-tagsets-timestamp）的字典序进行排列，在内存中不会吧完整的index数据加载进去（<strong>内存中加载的索引应该是一个类似倒排索引的索引结构</strong>-间接索引），这样会很大，而只是对部分key做索引，称之为<code>indirectindex</code>。该indirectindex会保存一些索引的辅助信息，而仅仅通过一个索引就可以知道该Blocks中是否存在本次要进行索引的信息。若想要定位某个TimeSeries的Index数据，会先根据内存中的部分Key信息找到与其最相近的Index Offset，之后从该起点开始顺序扫描<code>内存Index</code>，再精确定位到该Key在TSM文件中Index数据位置.</p>
<pre><code class="copyable">┌──────────────────────────────────────────────────────
│                                   Index                                    │
├─────────┬─────────┬──────┬───────┬─────────┬─────────
│ Key Len │   Key   │ Type │ Count │Min Time │Max Time │ Offset │  Size  │...│
│ 2 bytes │ N bytes │1 byte│2 bytes│ 8 bytes │ 8 bytes │8 bytes │4 bytes │   │
└─────────┴─────────┴──────┴───────┴─────────┴─────────
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>这里介绍一下Index中每一项的含义.</p>
</blockquote>
<p>Compactor：</p>
<ul>
<li>快照 - 缓存和 WAL 中的值必须转换为 TSM 文件以释放 WAL 段使用的内存和磁盘空间。这些压缩基于缓存内存和时间阈值发生。</li>
<li>级别压缩 - 级别压缩（级别 1-4）随着 TSM 文件的增长而发生。TSM 文件从快照压缩为 1 级文件。多个 1 级文件被压缩以生成 2 级文件。该过程一直持续到文件达到级别 4 和 TSM 文件的最大大小。
除非需要运行删除、索引优化压缩或完全压缩，否则它们不会被进一步压缩。较低级别的压缩使用避免 CPU 密集型活动（如解压缩和组合块）的策略。更高级别（因此频率更低）的压缩将重新组合块以完全压缩它们并提高压缩率。</li>
<li>索引优化 - 当许多 4 级 TSM 文件累积时，内部索引变得更大且访问成本更高。索引优化压缩将<code>Series</code>和索引拆分到一组新的 TSM 文件中，将给定<code>Series</code>的所有点排序到一个 TSM 文件中。在索引优化之前，每个 TSM 文件都包含大多数或所有<code>Series</code>的点，因此每个都包含相同的系列索引。索引优化后，每个 TSM 文件都包含来自最小<code>Series</code>的点，并且文件之间的<code>Series</code>重叠很少。因此，每个 TSM 文件都有一个较小的唯一系列索引，而不是完整<code>Series</code>列表的副本。此外，来自特定<code>Series</code>的所有点在 TSM 文件中都是<code>连续</code>的，而不是分布在多个 TSM 文件中。</li>
</ul>
</li>
</ul>
<h2 data-id="heading-8">🔖 四、索引.</h2>
<blockquote>
<p>TSM 是存储数据的一种结构，所以为了提高查询效率需要建立索引，Influxdb中的索引也被称之为间接索引.</p>
</blockquote>
<p>LSM Tree 通过将大量的随机写转换为顺序写，从而极大提升了数据写入的性能，与此同时牺牲了部分读的能力，TSM 存储引擎基于LSM开发，所以情况类似，通常设计数据库时会采用索引文件的方式，TSM采用的是类倒排索引方式.</p>
<p>**索引数据结构：**插入数据时会更新DatabaseIndex结构中的数据.</p>
<p><strong>先根据<code>DatabaseIndex</code>过滤掉一些<code>SeriesKey</code>，然后根据<code>TimeStamp</code>从TSM File 保留在内存中的索引进行过滤一次.</strong></p>
<pre><code class="copyable">type DatabaseIndex struct &#123;
    measurements map[string]*Measurement // 该数据库下所有 Measurement 对象
    series       map[string]*Series      // 所有 Series 对象，SeriesKey = measurement + tags
    name string // 数据库名
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Influxdb 在启动时会对<code>DatabaseIndex</code>进行初始化，从所有的Shard下的TSM File中加载Index数据，但是这里加载并不是全部加载，而只是加载<code>Block</code>下面的最大时间和最小时间来进行索引，在进行查找的时候只需要根据时间戳就可以知道该数据位于那个<code>Block</code>中.</p>
<p>我们再来看下面的数据结构：</p>
<pre><code class="hljs language-go copyable" lang="go"><span class="hljs-keyword">type</span> Measurement <span class="hljs-keyword">struct</span> &#123;
    Name       <span class="hljs-keyword">string</span> <span class="hljs-string">`json:"name,omitempty"`</span>
    fieldNames <span class="hljs-keyword">map</span>[<span class="hljs-keyword">string</span>]<span class="hljs-keyword">struct</span>&#123;&#125;      <span class="hljs-comment">// 此 measurement 中的所有 filedNames</span>

    <span class="hljs-comment">// 内存中的索引信息</span>
    <span class="hljs-comment">// id 以及其对应的 series 信息，主要是为了在 seriesByTagKeyValue 中存储Id节约内存</span>
    seriesByID          <span class="hljs-keyword">map</span>[<span class="hljs-keyword">uint64</span>]*Series              

    <span class="hljs-comment">// 根据 tagk 和 tagv 的双重索引，保存排好序的 SeriesID 数组</span>
    <span class="hljs-comment">// 这个 map 用于在查询操作时，可以根据 tags 来快速过滤出要查询的所有 SeriesID，之后根据 SeriesKey 以及时间范围从文件中读取相应内容</span>
    seriesByTagKeyValue <span class="hljs-keyword">map</span>[<span class="hljs-keyword">string</span>]<span class="hljs-keyword">map</span>[<span class="hljs-keyword">string</span>]SeriesIDs <span class="hljs-comment">// map from tag key to value to sorted set of series ids</span>

    <span class="hljs-comment">// 此 measurement 中所有 series 的 id，按照 id 排序</span>
    seriesIDs           SeriesIDs                       <span class="hljs-comment">// sorted list of series IDs in this measurement</span>
&#125;

<span class="hljs-keyword">type</span> Series <span class="hljs-keyword">struct</span> &#123;
    Key         <span class="hljs-keyword">string</span>              <span class="hljs-comment">// series key</span>
    Tags        <span class="hljs-keyword">map</span>[<span class="hljs-keyword">string</span>]<span class="hljs-keyword">string</span>   <span class="hljs-comment">// tags</span>
    id          <span class="hljs-keyword">uint64</span>              <span class="hljs-comment">// id</span>
    measurement *Measurement        <span class="hljs-comment">// 所属 measurement</span>
    <span class="hljs-comment">// 在哪些 shard 中存在</span>
    shardIDs    <span class="hljs-keyword">map</span>[<span class="hljs-keyword">uint64</span>]<span class="hljs-keyword">bool</span> <span class="hljs-comment">// shards that have this series defined</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于查询我们首先通过<code>DatabaseIndex.measurements.seriesByTagKeyValue["tagK"]["tagV"]</code>获取到所有匹配的<code>series</code>的ID值，然后通过<code>Measurement.seriesByID</code>获取到指定的<code>Series</code>，然后通过<code>Series</code>结构体来发现该<code>Series</code>在那些<code>Shard</code>中存在.  至此我们在<code>O(1)</code>的时间复杂度内获取到了所有符合要求的<code>Series Key</code>然后我们就需要创建数据迭代器从不同的Shard中获取每一个SeriesKey中指定的数据通过时间，这里就需要使用到 <code>TSM File</code>索引了，</p>
<p><strong>TSM File</strong>内存索引：在内存中，TSM 为每一个TSM File维护了一个内存索引，但是其并不是将所有TSM File中Index部分的数据加载到内存中，而仅仅只是加载每一个<code>Block</code>中保持的数据的最大时间和最下时间，每次通过Series定位到某一个Shard时，只需要根据时间就可以定位到本次要查询的Key的内容位于那个Block中。然后去访问TSM File中的详细索引，通过详细索引，我们可以知道其在TSM File中的偏移量.</p>
<p>定位到具体的Shard之后，仅仅只需要根据TSM FIle在内存中维护的索引的时间范围来进行比较即可知道当前的Key是否存在当前的<code>Block</code>中.</p>
<h2 data-id="heading-9">🔖 五、增加.</h2>
<blockquote>
<p>图形化解释过程.</p>
</blockquote>
<h3 data-id="heading-10">5.1 增加数据过程.</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7c4ff0715b94978af8c51b638adc349~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image-20210805170246255" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>过程说明：</strong></p>
<p>当influxdb接收到HTTP请求要增加数据的时候，influxdb会通过HTTP模块（解析SeriesKey）和RP模块来定位到其所在的ShardGroup.</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5cbeaa1de3ed4b878a541c7bc1fa90d7~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image-20210805171030167" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后在根据RP来定位到本次SeriesKey属于那个Shard. 当找到其属于那个Shard的Series之后，就需要进行写入了. 写入之前需要先构建索引，构建之后在进行写入缓存和WAL中. 当WAL超过25M则会进行写入L1中的tsm file中，其中最重要的就是将本次Sereis保存在<code>seriesByTagKeyValue</code>map中。 这里的map有点倒排索引的意思，通过倒排索引来快速定位到具体的Series. 进而可以快速的进行插入和查询.</p>
<h2 data-id="heading-11">🔖 六、高可用：以结果导向来进行分析.</h2>
<blockquote>
<p>如何实现高可用？<a href="https://link.juejin.cn/?target=https%3A%2F%2Fkm.woa.com%2Fgroup%2F568%2Farticles%2Fshow%2F452251%3Fkmref%3Dsearch%26from_page%3D1%26no%3D5" target="_blank" rel="nofollow noopener noreferrer" title="https://km.woa.com/group/568/articles/show/452251?kmref=search&from_page=1&no=5" ref="nofollow noopener noreferrer">InfluxDB集群方案在海量网络时序数据存储场景的应用 - 网管系统 - KM平台 (woa.com)</a></p>
</blockquote>
<p>哈希一致性代理 + 缓存  +  多节点.</p>
<h3 data-id="heading-12">6.1 总体架构图.</h3>
<p>如果要实现<code>influxdb</code>的高可用，那么就必须搭建集群，但是可惜的是<code>influxdb</code>的集群版本是商业闭源的。那么应该怎么实现呢？</p>
<p>参考KM文章，通过<code>proxy</code>来进行实现. 架构图如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ebcc620174cb42a38f7d88d0fd5145c3~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image-20210804211055122" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>client：各种语言的influxdb的客户端.</li>
<li>lb：负载均衡，将客户端的请求均衡的发布到各个proxy地址.</li>
<li>influx-proxy：代理实例，<code>基于database+measurement</code><strong>作为key使用一致性hash算法将读写请求分发到对应的<code>influxdb</code>实例中</strong>，同时具有全局配置中心管理、数据缓存、故障恢复等集群功能.</li>
<li>circle：一致性哈希环，一个circle包含了若干个<code>influxdb</code>实例，共同存储了一份全量的数据，即每个circle全都是全量数据的一个副本，各个circle的数据互相备份.</li>
<li>influxdb：influxdb单节点的实例，通过url来进行区分，一个实例只存储了一份全量数据的一部分数据.</li>
</ul>
<h3 data-id="heading-13">6.2 集群高可用.</h3>
<p>在集群高可用上，架构上可以部署多个proxy分摊压力，proxy之间无状态，一个挂掉不影响另外一个。如果在写入数据时有Influxdb实例出现故障，proxy会缓存失败的数据，直到Influxdb实例重新运行后，恢复重写。</p>
<p><strong>性能测试对比</strong>：测试结果来自[KM文章](<a href="https://link.juejin.cn/?target=https%3A%2F%2Fkm.woa.com%2Fgroup%2F568%2Farticles%2Fshow%2F452251%3Fkmref%3Dsearch%26from_page%3D1%26no%3D5" target="_blank" rel="nofollow noopener noreferrer" title="https://km.woa.com/group/568/articles/show/452251?kmref=search&from_page=1&no=5" ref="nofollow noopener noreferrer">InfluxDB集群方案在海量网络时序数据存储场景的应用 - 网管系统 - KM平台 (woa.com)</a>)</p>
<p>压测条件：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5da5d109aeff4203b34b721b9528d34e~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image-20210804215607598" loading="lazy" referrerpolicy="no-referrer"></p>
<p>压测结果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/302885e5c77f4ee8acebf39b665b85d8~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="image-20210804220821515" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            