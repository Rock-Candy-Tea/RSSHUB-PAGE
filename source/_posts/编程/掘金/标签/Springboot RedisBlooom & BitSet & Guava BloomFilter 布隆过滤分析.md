
---
title: 'Springboot RedisBlooom & BitSet & Guava BloomFilter 布隆过滤分析'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1604fa63e5d4e5984122726227ae358~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 06:29:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1604fa63e5d4e5984122726227ae358~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>「本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战！</a>」</p>
<h1 data-id="heading-0">1:使用 BloomFilter 背景</h1>
<p>BloomFilter在项目开发过程中经常使用，比如缓存穿透、爬虫过滤、猜你喜欢多路召回过滤等，判断一个或多个元素是否在一个集合内。它的空间效率和查询时间都远远超过一般的算法，当然它的缺点是有一定的误识别率和删除困难。基于性能和内存使用上考虑，最终选择BloomFilter。接下来重点梳理一下bloomfilter如何使用以及实现原理。</p>
<h1 data-id="heading-1">2:BloomFilter 单机使用</h1>
<h4 data-id="heading-2">1:guava BloomFilter</h4>
<p>其核心是hash 函数的选取以及 bit 数组的大小，主要使用：MURMUR128_MITZ_32 和 MURMUR128_MITZ_64，两者使用的都是MurmurHash3算法。详细的实现见guava的实现类：BloomFilterStrategies ，详细底层算法实现见：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FBloom_filter" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/Bloom_filter" ref="nofollow noopener noreferrer">Bloom_filter算法分析</a></p>
<pre><code class="hljs language-js copyable" lang="js">## 引入guava  maven 库
<dependency>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>com.google.guava<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>guava<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span></span>
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">version</span>></span>30.1.1-jre<span class="hljs-tag"></<span class="hljs-name">version</span>></span></span>
</dependency>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>guava 使用 bloomFilter 比较简单。引入maven包，几行代码搞定。详细如下：</p>
<pre><code class="hljs language-js copyable" lang="js">BloomFilter<CharSequence> bloomFilter  = BloomFilter.create(Funnels.stringFunnel(Charset.defaultCharset()),<span class="hljs-number">1000</span>,<span class="hljs-number">0.0000001</span>);
bloomFilter.put(<span class="hljs-string">"abc"</span>);
boolean  isContains = bloomFilter.mightContain(<span class="hljs-string">"abc"</span>);
System.out.println(isContains );
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">2:基于JVM的 BitSet  BloomFilter</h4>
<p>BitSet只面向数字比较，并且必须是正数。其他类型需要先转换成int类型，转换过程中难免会出现重复，BitSet的准确性就会降低。详细如下：</p>
<pre><code class="hljs language-js copyable" lang="js">public <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">BloomFilter</span> </span>&#123;
    private BitSet bits;
    private int size;
    private AtomicInteger realSize = <span class="hljs-keyword">new</span> AtomicInteger(<span class="hljs-number">0</span>);
    private int addedElements;
    private int hashFunctionNumber;

    <span class="hljs-comment">/**
     * 构造一个布隆过滤器，过滤器的容量为c * n 个bit.
     *
     * <span class="hljs-doctag">@param </span>c 当前过滤器预先开辟的最大包含记录,通常要比预计存入的记录多一倍.
     * <span class="hljs-doctag">@param </span>n 当前过滤器预计所要包含的记录.
     * <span class="hljs-doctag">@param </span>k 哈希函数的个数，等同每条记录要占用的bit数.
     */</span>
    public <span class="hljs-function"><span class="hljs-title">BloomFilter</span>(<span class="hljs-params">int c, int n, int k</span>)</span> &#123;
        <span class="hljs-keyword">if</span> (k > <span class="hljs-number">8</span>) &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> IllegalArgumentException(<span class="hljs-string">"Illegal k(maximum is 8): "</span> + k);
        &#125;
        <span class="hljs-built_in">this</span>.hashFunctionNumber = k;
        <span class="hljs-built_in">this</span>.size = (int) <span class="hljs-built_in">Math</span>.ceil(c * k);
        <span class="hljs-built_in">this</span>.addedElements = n;
        <span class="hljs-built_in">this</span>.bits = <span class="hljs-keyword">new</span> BitSet(size);
    &#125;

    <span class="hljs-comment">/**
     * 写入Bloom过滤器
     *
     * <span class="hljs-doctag">@param </span>str 缓存字符串
     */</span>
    public <span class="hljs-keyword">void</span> <span class="hljs-function"><span class="hljs-title">put</span>(<span class="hljs-params"><span class="hljs-built_in">String</span> str</span>)</span> &#123;
        realSize.incrementAndGet();
        byte[] bytes = str.getBytes();
        int[] positions = createHashes(bytes, hashFunctionNumber);
        <span class="hljs-keyword">for</span> (int i : positions) &#123;
            int position = <span class="hljs-built_in">Math</span>.abs(i % size);
            bits.set(position, <span class="hljs-literal">true</span>);
        &#125;
    &#125;

    <span class="hljs-comment">/**
     * Bloom过滤器是否包含对应的字符串
     *
     * <span class="hljs-doctag">@param </span>str 字符串对象
     * <span class="hljs-doctag">@return </span>true表示包含
     */</span>
    public boolean <span class="hljs-function"><span class="hljs-title">contains</span>(<span class="hljs-params"><span class="hljs-built_in">String</span> str</span>)</span> &#123;
        byte[] bytes = str.getBytes();
        int[] positions = createHashes(bytes, hashFunctionNumber);
        <span class="hljs-keyword">for</span> (int i : positions) &#123;
            int position = <span class="hljs-built_in">Math</span>.abs(i % size);
            <span class="hljs-keyword">if</span> (!bits.get(position)) &#123;
                <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
            &#125;
        &#125;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
    &#125;

    <span class="hljs-comment">/**
     * 得到当前过滤器的错误率.
     *
     * <span class="hljs-doctag">@return </span>错误率
     */</span>
    public double <span class="hljs-function"><span class="hljs-title">getFalsePositiveProbability</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Math</span>.pow((<span class="hljs-number">1</span> - <span class="hljs-built_in">Math</span>.exp(-hashFunctionNumber * (double) addedElements / size)), hashFunctionNumber);
    &#125;

    public int <span class="hljs-function"><span class="hljs-title">getSize</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> size;
    &#125;

    public int <span class="hljs-function"><span class="hljs-title">getRealSize</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> realSize.get();
    &#125;

    private int[] <span class="hljs-function"><span class="hljs-title">createHashes</span>(<span class="hljs-params">byte[] bytes, int hashFunctionNumber</span>)</span> &#123;
        int[] result = <span class="hljs-keyword">new</span> int[hashFunctionNumber];
        <span class="hljs-keyword">for</span> (int i = <span class="hljs-number">0</span>; i < hashFunctionNumber; i++) &#123;
            result[i] = HashFunctions.hash(bytes, i);
        &#125;
        <span class="hljs-keyword">return</span> result;
    &#125;

    <span class="hljs-keyword">static</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HashFunctions</span> </span>&#123;
        <span class="hljs-keyword">static</span> int <span class="hljs-function"><span class="hljs-title">hash</span>(<span class="hljs-params">byte[] bytes, int index</span>)</span> &#123;
            <span class="hljs-keyword">switch</span> (index) &#123;
                <span class="hljs-keyword">case</span> <span class="hljs-number">0</span>:
                    <span class="hljs-keyword">return</span> RSHash(bytes);
                <span class="hljs-keyword">case</span> <span class="hljs-number">1</span>:
                    <span class="hljs-keyword">return</span> JSHash(bytes);
                <span class="hljs-keyword">case</span> <span class="hljs-number">2</span>:
                    <span class="hljs-keyword">return</span> ELFHash(bytes);
                <span class="hljs-keyword">case</span> <span class="hljs-number">3</span>:
                    <span class="hljs-keyword">return</span> BKDRHash(bytes);
                <span class="hljs-keyword">case</span> <span class="hljs-number">4</span>:
                    <span class="hljs-keyword">return</span> APHash(bytes);
                <span class="hljs-keyword">case</span> <span class="hljs-number">5</span>:
                    <span class="hljs-keyword">return</span> DJBHash(bytes);
                <span class="hljs-keyword">case</span> <span class="hljs-number">6</span>:
                    <span class="hljs-keyword">return</span> SDBMHash(bytes);
                <span class="hljs-keyword">case</span> <span class="hljs-number">7</span>:
                    <span class="hljs-keyword">return</span> PJWHash(bytes);
            &#125;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> IllegalArgumentException(<span class="hljs-string">"Invalid index: "</span> + index);
        &#125;

        <span class="hljs-keyword">static</span> int <span class="hljs-function"><span class="hljs-title">RSHash</span>(<span class="hljs-params">byte[] bytes</span>)</span> &#123;
            int hash = <span class="hljs-number">0</span>;
            int magic = <span class="hljs-number">63689</span>;
            <span class="hljs-keyword">for</span> (byte b : bytes) &#123;
                hash = hash * magic + b;
                magic = magic * <span class="hljs-number">378551</span>;
            &#125;
            <span class="hljs-keyword">return</span> hash;
        &#125;

        <span class="hljs-keyword">static</span> int <span class="hljs-function"><span class="hljs-title">JSHash</span>(<span class="hljs-params">byte[] bytes</span>)</span> &#123;
            int hash = <span class="hljs-number">1315423911</span>;
            <span class="hljs-keyword">for</span> (byte b : bytes) &#123;
                hash ^= ((hash << <span class="hljs-number">5</span>) + b + (hash >> <span class="hljs-number">2</span>));
            &#125;
            <span class="hljs-keyword">return</span> hash;
        &#125;

        <span class="hljs-keyword">static</span> int <span class="hljs-function"><span class="hljs-title">ELFHash</span>(<span class="hljs-params">byte[] bytes</span>)</span> &#123;
            int hash = <span class="hljs-number">0</span>;
            int x;
            <span class="hljs-keyword">for</span> (byte b : bytes) &#123;
                hash = (hash << <span class="hljs-number">4</span>) + b;
                <span class="hljs-keyword">if</span> ((x = hash & <span class="hljs-number">0xF0000000</span>) != <span class="hljs-number">0</span>) &#123;
                    hash ^= (x >> <span class="hljs-number">24</span>);
                    hash &= ~x;
                &#125;
            &#125;
            <span class="hljs-keyword">return</span> hash;
        &#125;

        <span class="hljs-keyword">static</span> int <span class="hljs-function"><span class="hljs-title">BKDRHash</span>(<span class="hljs-params">byte[] bytes</span>)</span> &#123;
            int seed = <span class="hljs-number">131</span>;
            int hash = <span class="hljs-number">0</span>;
            <span class="hljs-keyword">for</span> (byte b : bytes) &#123;
                hash = (hash * seed) + b;
            &#125;
            <span class="hljs-keyword">return</span> hash;
        &#125;

        <span class="hljs-keyword">static</span> int <span class="hljs-function"><span class="hljs-title">APHash</span>(<span class="hljs-params">byte[] bytes</span>)</span> &#123;
            int hash = <span class="hljs-number">0</span>;
            int len = bytes.length;
            <span class="hljs-keyword">for</span> (int i = <span class="hljs-number">0</span>; i < len; i++) &#123;
                <span class="hljs-keyword">if</span> ((i & <span class="hljs-number">1</span>) == <span class="hljs-number">0</span>) &#123;
                    hash ^= ((hash << <span class="hljs-number">7</span>) ^ bytes[i] ^ (hash >> <span class="hljs-number">3</span>));
                &#125; <span class="hljs-keyword">else</span> &#123;
                    hash ^= (~((hash << <span class="hljs-number">11</span>) ^ bytes[i] ^ (hash >> <span class="hljs-number">5</span>)));
                &#125;
            &#125;
            <span class="hljs-keyword">return</span> hash;
        &#125;

        <span class="hljs-keyword">static</span> int <span class="hljs-function"><span class="hljs-title">DJBHash</span>(<span class="hljs-params">byte[] bytes</span>)</span> &#123;
            int hash = <span class="hljs-number">5381</span>;
            <span class="hljs-keyword">for</span> (byte b : bytes) &#123;
                hash = ((hash << <span class="hljs-number">5</span>) + hash) + b;
            &#125;
            <span class="hljs-keyword">return</span> hash;
        &#125;

        <span class="hljs-keyword">static</span> int <span class="hljs-function"><span class="hljs-title">SDBMHash</span>(<span class="hljs-params">byte[] bytes</span>)</span> &#123;
            int hash = <span class="hljs-number">0</span>;
            <span class="hljs-keyword">for</span> (byte b : bytes) &#123;
                hash = b + (hash << <span class="hljs-number">6</span>) + (hash << <span class="hljs-number">16</span>) - hash;
            &#125;
            <span class="hljs-keyword">return</span> hash;
        &#125;

        <span class="hljs-keyword">static</span> int <span class="hljs-function"><span class="hljs-title">PJWHash</span>(<span class="hljs-params">byte[] bytes</span>)</span> &#123;
            long bitsInUnsignedInt = (<span class="hljs-number">4</span> << <span class="hljs-number">3</span>);
            long threeQuarters = ((bitsInUnsignedInt * <span class="hljs-number">3</span>) >> <span class="hljs-number">2</span>);
            long oneEighth = (bitsInUnsignedInt >> <span class="hljs-number">3</span>);
            long highBits = (long) (<span class="hljs-number">0xFFFFFFFF</span>) << (bitsInUnsignedInt - oneEighth);
            int hash = <span class="hljs-number">0</span>;
            long test;
            <span class="hljs-keyword">for</span> (byte b : bytes) &#123;
                hash = (hash << oneEighth) + b;
                <span class="hljs-keyword">if</span> ((test = hash & highBits) != <span class="hljs-number">0</span>) &#123;
                    hash = (int) ((hash ^ (test >> threeQuarters)) & (~highBits));
                &#125;
            &#125;
            <span class="hljs-keyword">return</span> hash;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">3:BloomFilter 集群使用</h1>
<p>BloomFilter的单机使用的类库已足够的方便，实际开发过程中始终会面临集群的问题。因为rest或rpc 服务基本都是无状态的，不会将某一个请求固定在某台机器上。接下来我们需要引入redis的插件RedisBloom。</p>
<h4 data-id="heading-5">1:下载git 仓库,make编译。</h4>
<pre><code class="hljs language-js copyable" lang="js">wget https:<span class="hljs-comment">//github.com/RedisBloom/RedisBloom/archive/refs/tags/v2.2.5.tar.gz --no-check-certificate</span>

## 下载完毕以后解压，然后make 编译
make 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1604fa63e5d4e5984122726227ae358~tplv-k3u1fbpfcp-watermark.image" alt="Snip20210712_73.png" loading="lazy" referrerpolicy="no-referrer">
当时在mac 环境下编译，执行一直失败。没有找到相关的解决方案，随后我在阿里云上找了一个按量付费的机器。安装完毕以后释放，也就几毛钱。 如下图 ，编译完成以后会生成redisbloom.so。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c12d10b098544ae1acc880c3786432ad~tplv-k3u1fbpfcp-watermark.image" alt="Snip20210711_67.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-6">2:centos7.6 安装redis。</h4>
<p>详细安装步骤如下：</p>
<pre><code class="hljs language-js copyable" lang="js">## 先安排依赖
yum install -y cpp binutils glibc glibc-kernheaders glibc-common glibc-devel gcc make tcl

##centos7 默认的 gcc 版本小于 <span class="hljs-number">5.3</span> 无法编译
sudo yum -y install centos-release-scl
sudo yum -y install devtoolset-<span class="hljs-number">9</span>-gcc devtoolset-<span class="hljs-number">9</span>-gcc-c++ devtoolset-<span class="hljs-number">9</span>-binutils

##临时生效，退出 shell 或重启会恢复原 gcc 版本
sudo scl enable devtoolset-<span class="hljs-number">9</span> bash

##永久生效
sudo echo <span class="hljs-string">"source /opt/rh/devtoolset-9/enable"</span> >><span class="hljs-regexp">/etc/</span>profile

## https 下载要上加上  --no-check-certificate
wget https:<span class="hljs-comment">//download.redis.io/releases/redis-6.2.4.tar.gz   --no-check-certificate</span>


## 解压安装
tar -zxvf redis-<span class="hljs-number">6.2</span><span class="hljs-number">.4</span>.tar.gz
cd redis-<span class="hljs-number">6.2</span><span class="hljs-number">.4</span>
make
make test
make install


创建根目录下的 redis 配置
sudo mkdir /etc/redis
## cp redis-<span class="hljs-number">6.2</span><span class="hljs-number">.4</span> 下面的redis conf 到 /etc/redis/
sudo cp redis.conf /etc/redis/

在 /etc/systemd/system新建service文件
sudo vi /etc/systemd/system/redis.service 

[Unit]
Description=Redis
After=network.target

[Service]
#Type=forking
ExecStart=<span class="hljs-regexp">/usr/</span>local/bin/redis-server /etc/redis/redis.conf
ExecReload=<span class="hljs-regexp">/usr/</span>local/bin/redis-server -s reload
ExecStop=<span class="hljs-regexp">/usr/</span>local/bin/redis-server -s stop
PrivateTmp=<span class="hljs-literal">true</span>

[Install]
WantedBy=multi-user.target

加入开启启动
sudo systemctl daemon-reload
sudo systemctl enable redis


启动服务：
sudo systemctl restart redis
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">3:redis加载redisbloom.so。</h4>
<p>注意redisbloom.so 我直接配置在 redis.conf ,这样启动的时候就默认加载。redis的其他配置比如bind 127.0.0.1 , requirepass 123456 其他的根据自己的需求在redis.conf中设置。
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9938ba77f16f4d9196287fad48bbd998~tplv-k3u1fbpfcp-watermark.image" alt="Snip20210711_69.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">4:redis bloom 测试，详细如下。</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5dfd9e3ef64a45bd821ab924724e5d1f~tplv-k3u1fbpfcp-watermark.image" alt="Snip20210711_68.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-9">5:JRedisBloom 依赖包。</h4>
<p>RedisBloom 提供了丰富的client ,详细见：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FRedisBloom%2FRedisBloom" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/RedisBloom/RedisBloom" ref="nofollow noopener noreferrer">RedisBloom</a> 。 针对于Python、Java、Go、Php、.Net都有实现。
注意：如果你引入的是redis client 是redis.clients，只需引入jrebloom maven即可实现RedisBloom。 如果你使用的是spring-data-redis，请继续往下看。</p>
<pre><code class="hljs language-js copyable" lang="js"> <dependency>
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>redis.clients<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span></span>
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>jedis<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span></span>
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">version</span>></span>3.6.1<span class="hljs-tag"></<span class="hljs-name">version</span>></span></span>
 </dependency>
 <span class="xml"><span class="hljs-tag"><<span class="hljs-name">dependency</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">groupId</span>></span>com.redislabs<span class="hljs-tag"></<span class="hljs-name">groupId</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">artifactId</span>></span>jrebloom<span class="hljs-tag"></<span class="hljs-name">artifactId</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">version</span>></span>2.1.0<span class="hljs-tag"></<span class="hljs-name">version</span>></span>
<span class="hljs-tag"></<span class="hljs-name">dependency</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-10">4:Spring Data Redis 如何引入BloomFilter</h1>
<p>我们的推荐系统工程是基于的spingboot,redis引入的是spring-data-redis。当时RedisBloom没有spring-data-redis实现，已经准备再通过redis.clients 初始化。后面发现<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fredooper%2Fspring-data-redis-bloom-filter" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/redooper/spring-data-redis-bloom-filter" ref="nofollow noopener noreferrer"> https://github.com/redooper/spring-data-redis-bloom-filter </a>基于 RedisTemplate execute 实现。下载到本地打包完成，上传到本地私服即可。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f993fcabf0a488fb4eee87790e64683~tplv-k3u1fbpfcp-watermark.image" alt="Snip20210712_74.png" loading="lazy" referrerpolicy="no-referrer">
注意：源码里面在创建bloomfilter的时候，没有给bloomfilter key过期时间。我们的场景在创建bloomfilter的时候，需默认给一个过期时间（finally加过期处理）。为了避免同一个时间点key大面积失效，在过期时间的基础上加一个随机时间。避免redis同一时间点，失效过多引起不必要的问题。</p>
<h1 data-id="heading-11">5:总结</h1>
<p>BloomFilter之所以能做到在时间和空间上的效率比较高，是因为牺牲了判断的准确率、删除的便利性。所以我们在使用BloomFilter的场景中，要允许出现一定的准确性。我们在推荐系统多路召回需要把用户最近展示过的内容剔除，所以引入RedisBloom。我们也是边踩坑，边找解决方案。我始终相信，所有的问题都可以解决，无非在业务或技术方案去突破。文中如果有不准确的地方，所以大家一起指正交流。git上也有人提供布谷鸟的概念，可以针对布隆过滤器进行删除，有兴趣的同学可以了解一下。详细见<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fkristoff-it%2Fredis-cuckoofilter" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/kristoff-it/redis-cuckoofilter" ref="nofollow noopener noreferrer">redis-cuckoofilter</a></p></div>  
</div>
            