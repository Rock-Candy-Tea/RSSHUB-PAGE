
---
title: 'Redis 大数据量（百亿级）Key存储需求及解决方案'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=8571'
author: 掘金
comments: false
date: Wed, 28 Apr 2021 02:06:28 GMT
thumbnail: 'https://picsum.photos/400/300?random=8571'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>最近我在思考实时数仓问题的时候，想到了巨量的redis的存储的问题，然后翻阅到这篇文章，与各位分享</p>
<h1 data-id="heading-0">一 需求背景</h1>
<p>该应用场景为DMP缓存存储需求，DMP需要管理非常多的第三方id数据，其中包括各媒体cookie与自身cookie（以下统称supperid）的mapping关系，还包括了supperid的人口标签、移动端id（主要是idfa和imei）的人口标签，以及一些黑名单id、ip等数据。</p>
<p>在hdfs的帮助下离线存储千亿记录并不困难，然而DMP还需要提供毫秒级的实时查询。由于cookie这种id本身具有不稳定性，<strong>所以很多的真实用户的浏览行为会导致大量的新cookie生成，只有及时同步mapping的数据才能命中DMP的人口标签，无法通过预热来获取较高的命中，这就跟缓存存储带来了极大的挑战</strong>。</p>
<p>经过实际测试，<strong>对于上述数据，常规存储超过五十亿的kv记录就需要1T多的内存，如果需要做高可用多副本那带来的消耗是巨大的，另外kv的长短不齐也会带来很多内存碎片，这就需要超大规模的存储方案来解决上述问题</strong>。</p>
<h1 data-id="heading-1">二 存储何种数据</h1>
<p>人⼝标签主要是cookie、imei、idfa以及其对应的gender（性别）、age（年龄段）、geo（地域）等；mapping关系主要是媒体cookie对supperid的映射。以下是数据存储⽰示例：</p>
<ol>
<li><strong>PC端的ID</strong>：</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">媒体编号-媒体cookie=>supperid

supperid => &#123; <span class="hljs-function"><span class="hljs-params">age</span>=></span>年龄段编码，gender=>性别编码，geo=>地理位置编码 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li><strong>Device端的ID</strong>：</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">imei or idfa => &#123; <span class="hljs-function"><span class="hljs-params">age</span>=></span>年龄段编码，gender=>性别编码，geo=>地理位置编码 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>显然PC数据需要存储两种key=>value还有key=>hashmap，⽽而Device数据需要存储⼀一种</p>
<p>key=>hashmap即可。</p>
<h1 data-id="heading-2">三 数据特点</h1>
<ul>
<li>短key短value：</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">其中superid为<span class="hljs-number">21</span>位数字：比如<span class="hljs-number">1605242015141689522</span>；
imei为小写md5：比如2d131005dc0f37d362a5d97094103633；
idfa为大写带”-”md5：比如：51DFFC83-<span class="hljs-number">9541</span>-<span class="hljs-number">4411</span>-FA4F-356927E39D04；
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>媒体自身的cookie长短不一；</li>
<li>需要为全量数据提供服务，supperid是百亿级、媒体映射是千亿级、移动id是几十亿级；</li>
<li><strong>每天有十亿级别的mapping关系产生；</strong></li>
<li><strong>对于较大时间窗口内可以预判热数据（有一些存留的稳定cookie）；</strong></li>
<li><strong>对于当前mapping数据无法预判热数据，有很多是新生成的cookie；</strong></li>
</ul>
<h1 data-id="heading-3">4 存在的技术挑战</h1>
<p>1）<strong>长短不一容易造成内存碎片</strong>；</p>
<p>2）<strong>由于指针大量存在，内存膨胀率比较高，一般在7倍，纯内存存储通病</strong>；</p>
<p>3）<strong>虽然可以通过cookie的行为预判其热度，但每天新生成的id依然很多（百分比比较敏感，暂不透露）</strong>；</p>
<p>4）<strong>由于服务要求在公网环境（国内公网延迟60ms以下）下100ms以内，所以原则上当天新更新的mapping和人口标签需要全部in memory，而不会让请求落到后端的冷数据</strong>；</p>
<p>5）<strong>业务方面，所有数据原则上至少保留35天甚至更久</strong>；</p>
<p>6）<strong>内存至今也比较昂贵，百亿级Key乃至千亿级存储方案势在必行</strong>！</p>
<h1 data-id="heading-4">5 解决方案</h1>
<h2 data-id="heading-5">5.1 淘汰策略</h2>
<p>存储吃紧的一个重要原因在于每天会有很多新数据入库，所以及时清理数据尤为重要。主要方法就是发现和保留热数据淘汰冷数据。</p>
<p>网民的量级远远达不到几十亿的规模，id有一定的生命周期，会不断的变化。所以很大程度上我们存储的id实际上是无效的。而查询其实前端的逻辑就是广告曝光，跟人的行为有关，所以一个id在某个时间窗口的（可能是一个campaign，半个月、几个月）访问行为上会有一定的重复性。</p>
<p><strong>数据初始化之前，我们先利用hbase将日志的id聚合去重，划定TTL的范围，一般是35天，这样可以砍掉近35天未出现的id。另外在Redis中设置过期时间是35天，当有访问并命中时，对key进行续命，延长过期时间，未在35天出现的自然淘汰。这样可以针对稳定cookie或id有效，实际证明，续命的方法对idfa和imei比较实用，长期积累可达到非常理想的命中</strong>。</p>
<h2 data-id="heading-6">5.2 减少膨胀</h2>
<p>Hash表空间大小和Key的个数决定了冲突率（或者用负载因子衡量），再合理的范围内，key越多自然hash表空间越大，消耗的内存自然也会很大。<strong>再加上大量指针本身是长整型，所以内存存储的膨胀十分可观</strong>。先来谈谈如何把key的个数减少。</p>
<p>大家先来了解一种存储结构。我们期望将key1=>value1存储在redis中，那么可以按照如下过程去存储。<strong>先用固定长度的随机散列md5(key)值作为redis的key，我们称之为BucketId</strong>，而将key1=>value1存储在hashmap结构中，这样在查询的时候就可以让client按照上面的过程计算出散列，从而查询到value1。</p>
<p><strong>过程变化简单描述为：get(key1) -> hget(md5(key1), key1) 从而得到value1</strong>。</p>
<p>如果我们通过预先计算，<strong>让很多key可以在BucketId空间里碰撞，那么可以认为一个BucketId下面挂了多个key。比如平均每个BucketId下面挂10个key，那么理论上我们将会减少超过90%的redis key的个数</strong>。</p>
<p>具体实现起来有一些麻烦，而且用这个方法之前你要想好容量规模。<strong>我们通常使用的md5是32位的hexString（16进制字符），它的空间是128bit，这个量级太大了，我们需要存储的是百亿级，大约是33bit（2的33次方），所以我们需要有一种机制计算出合适位数的散列，而且为了节约内存，我们需要利用全部字符类型（ASCII码在0~127之间）来填充，而不用HexString，这样Key的长度可以缩短到一半</strong>。</p>
<p>下面是具体的实现方式</p>
<pre><code class="hljs language-js copyable" lang="js">
public <span class="hljs-keyword">static</span> byte [] <span class="hljs-function"><span class="hljs-title">getBucketId</span>(<span class="hljs-params">byte [] key, Integer bit</span>)</span> &#123;

    MessageDigest mdInst = MessageDigest.getInstance(<span class="hljs-string">"MD5"</span>);

    mdInst.update(key);

    byte [] md = mdInst.digest();

    byte [] r = <span class="hljs-keyword">new</span> byte[(bit-<span class="hljs-number">1</span>)/<span class="hljs-number">7</span> + <span class="hljs-number">1</span>];<span class="hljs-comment">// 因为一个字节中只有7位能够表示成单字符，ascii码是7位</span>

    int a = (int) <span class="hljs-built_in">Math</span>.pow(<span class="hljs-number">2</span>, bit%<span class="hljs-number">7</span>)-<span class="hljs-number">2</span>;

    md[r.length-<span class="hljs-number">1</span>] = (byte) (md[r.length-<span class="hljs-number">1</span>] & a);

    System.arraycopy(md, <span class="hljs-number">0</span>, r, <span class="hljs-number">0</span>, r.length);

    <span class="hljs-keyword">for</span>(int i=<span class="hljs-number">0</span>;i<r.length;i++) &#123;

    <span class="hljs-keyword">if</span>(r[i]<<span class="hljs-number">0</span>) r[i] &= <span class="hljs-number">127</span>;

    &#125;

    <span class="hljs-keyword">return</span> r;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参数bit决定了最终BucketId空间的大小，空间大小集合是2的整数幂次的离散值。这里解释一下为何一个字节中只有7位可用，是因为redis存储key时需要是ASCII（0~127），而不是byte array。<strong>如果规划百亿级存储，计划每个桶分担10个kv，那么我们只需2^30=1073741824的桶个数即可，也就是最终key的个数</strong>。</p>
<h3 data-id="heading-7">5.3 减少碎片</h3>
<p>碎片主要原因在于内存无法对齐、过期删除后，内存无法重新分配。<strong>通过上文描述的方式，我们可以将人口标签和mapping数据按照上面的方式去存储，这样的好处就是redis key是等长的</strong>。另外对于hashmap中的key我们也做了相关优化，截取cookie或者deviceid的后六位作为key，这样也可以保证内存对齐，理论上会有冲突的可能性，但在同一个桶内后缀相同的概率极低(试想id几乎是随机的字符串，随意10个由较长字符组成的id后缀相同的概率*桶样本数=发生冲突的期望值<<0.05,也就是说出现一个冲突样本则是极小概率事件，而且这个概率可以通过调整后缀保留长度控制期望值)。而value只存储age、gender、geo的编码，用三个字节去存储。</p>
<p>另外提一下，减少碎片还有个很low但是有效的方法，将slave重启，然后强制的failover切换主从，这样相当于给master整理的内存的碎片。</p>
<p><strong>推荐Google-tcmalloc， facebook-jemalloc内存分配，可以在value不大时减少内存碎片和内存消耗。有人测过大value情况下反而libc更节约</strong>。</p></div>  
</div>
            