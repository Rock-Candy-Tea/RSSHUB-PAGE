
---
title: '分布式ID生成方案选型！详细解析雪花算法Snowflake'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a8900c33ad8c4528aa29052adf35bf88~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 10 Jul 2021 06:32:18 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a8900c33ad8c4528aa29052adf35bf88~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战！</a></p>
<h1 data-id="heading-0">分布式唯一ID</h1>
<ul>
<li>使用<strong>RocketMQ</strong>时,需要使用到分布式唯一<strong>ID</strong></li>
<li>消息可能会发生重复,所以要在消费端做幂等性,为了达到业务的幂等性,生产者必须要有一个唯一<strong>ID,</strong> 需要满足以下条件:
<ul>
<li><strong>同一业务场景要全局唯一</strong></li>
<li><strong>该ID必须是在消息的发送方进行生成发送到MQ</strong></li>
<li><strong>消费端根据该ID进行判断是否重复,确保幂等性</strong></li>
</ul>
</li>
<li>在哪里产生以及消费端进行判断做幂等性与该ID无关,此ID需要保证的特性:
<ul>
<li><strong>局部甚至全局唯一</strong></li>
<li><strong>趋势递增</strong></li>
</ul>
</li>
</ul>
<h1 data-id="heading-1">Snowflake算法</h1>
<ul>
<li>Snowflake是Twitter开源的分布式ID生成算法, 结果是一个<strong>Long</strong>型的ID,核心思想是:
<ul>
<li>使用<strong>1</strong>位作为符号位,确定为<strong>0,</strong> 表示<strong>正</strong></li>
<li>使用<strong>41</strong>位作为<strong>毫秒数</strong></li>
<li>使用<strong>10</strong>位作为机器的ID <strong>:</strong> 高<strong>5</strong>位是<strong>数据中心ID,</strong> 低<strong>5</strong>位是<strong>机器ID</strong></li>
<li>使用<strong>12</strong>位作为<strong>毫秒内的序列号,</strong> 意味着每个节点每秒可以产生<strong>4096(2^12^)</strong> 个ID</li>
</ul>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a8900c33ad8c4528aa29052adf35bf88~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
该算法通过二进制的操作进行实现,单机每秒内理论上最多可以生成<strong>1000*(2^12),</strong> 即<strong>409.6</strong>万个ID</p>
<h1 data-id="heading-2">SnowflakeIdWorker</h1>
<ul>
<li><strong>Snowflake算法Java实现SnowflakeIdWorker:</strong></li>
</ul>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">/**
 * Twitter_Snowflake<br>
 * SnowFlake的结构如下(每部分用-分开):<br>
 * 0 - 0000000000 0000000000 0000000000 0000000000 0 - 00000 - 00000 - 000000000000 <br>
 * 1位标识，由于long基本类型在Java中是带符号的，最高位是符号位，正数是0，负数是1，所以id一般是正数，最高位是0<br>
 * 41位时间截(毫秒级)，注意，41位时间截不是存储当前时间的时间截，而是存储时间截的差值（当前时间截 - 开始时间截)
 * 得到的值），这里的的开始时间截，一般是我们的id生成器开始使用的时间，由我们程序来指定的（如下下面程序IdWorker类的startTime属性）。41位的时间截，可以使用69年，年T = (1L << 41) / (1000L * 60 * 60 * 24 * 365) = 69<br>
 * 10位的数据机器位，可以部署在1024个节点，包括5位datacenterId和5位workerId<br>
 * 12位序列，毫秒内的计数，12位的计数顺序号支持每个节点每毫秒(同一机器，同一时间截)产生4096个ID序号<br>
 * 加起来刚好64位，为一个Long型。<br>
 * SnowFlake的优点是，整体上按照时间自增排序，并且整个分布式系统内不会产生ID碰撞(由数据中心ID和机器ID作区分)，并且效率较高，经测试，SnowFlake每秒能够产生26万ID左右。
 */</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SnowflakeIdWorker</span> </span>&#123;

    <span class="hljs-comment">// ==============================Fields===========================================</span>
    <span class="hljs-comment">/** 开始时间截 (2015-01-01) */</span>
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">long</span> twepoch = <span class="hljs-number">1420041600000L</span>;

    <span class="hljs-comment">/** 机器id所占的位数 */</span>
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">long</span> workerIdBits = <span class="hljs-number">5L</span>;

    <span class="hljs-comment">/** 数据标识id所占的位数 */</span>
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">long</span> datacenterIdBits = <span class="hljs-number">5L</span>;

    <span class="hljs-comment">/** 支持的最大机器id，结果是31 (这个移位算法可以很快的计算出几位二进制数所能表示的最大十进制数) */</span>
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">long</span> maxWorkerId = -<span class="hljs-number">1L</span> ^ (-<span class="hljs-number">1L</span> << workerIdBits);

    <span class="hljs-comment">/** 支持的最大数据标识id，结果是31 */</span>
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">long</span> maxDatacenterId = -<span class="hljs-number">1L</span> ^ (-<span class="hljs-number">1L</span> << datacenterIdBits);

    <span class="hljs-comment">/** 序列在id中占的位数 */</span>
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">long</span> sequenceBits = <span class="hljs-number">12L</span>;

    <span class="hljs-comment">/** 机器ID向左移12位 */</span>
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">long</span> workerIdShift = sequenceBits;

    <span class="hljs-comment">/** 数据标识id向左移17位(12+5) */</span>
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">long</span> datacenterIdShift = sequenceBits + workerIdBits;

    <span class="hljs-comment">/** 时间截向左移22位(5+5+12) */</span>
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">long</span> timestampLeftShift = sequenceBits + workerIdBits + datacenterIdBits;

    <span class="hljs-comment">/** 生成序列的掩码，这里为4095 (0b111111111111=0xfff=4095) */</span>
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">final</span> <span class="hljs-keyword">long</span> sequenceMask = -<span class="hljs-number">1L</span> ^ (-<span class="hljs-number">1L</span> << sequenceBits);

    <span class="hljs-comment">/** 工作机器ID(0~31) */</span>
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">long</span> workerId;

    <span class="hljs-comment">/** 数据中心ID(0~31) */</span>
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">long</span> datacenterId;

    <span class="hljs-comment">/** 毫秒内序列(0~4095) */</span>
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">long</span> sequence = <span class="hljs-number">0L</span>;

    <span class="hljs-comment">/** 上次生成ID的时间截 */</span>
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">long</span> lastTimestamp = -<span class="hljs-number">1L</span>;

    <span class="hljs-comment">//==============================Constructors=====================================</span>
    <span class="hljs-comment">/**
     * 构造函数
     * <span class="hljs-doctag">@param</span> workerId 工作ID (0~31)
     * <span class="hljs-doctag">@param</span> datacenterId 数据中心ID (0~31)
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-title">SnowflakeIdWorker</span><span class="hljs-params">(<span class="hljs-keyword">long</span> workerId, <span class="hljs-keyword">long</span> datacenterId)</span> </span>&#123;
        <span class="hljs-keyword">if</span> (workerId > maxWorkerId || workerId < <span class="hljs-number">0</span>) &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> IllegalArgumentException(String.format(<span class="hljs-string">"worker Id can't be greater than %d or less than 0"</span>, maxWorkerId));
        &#125;
        <span class="hljs-keyword">if</span> (datacenterId > maxDatacenterId || datacenterId < <span class="hljs-number">0</span>) &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> IllegalArgumentException(String.format(<span class="hljs-string">"datacenter Id can't be greater than %d or less than 0"</span>, maxDatacenterId));
        &#125;
        <span class="hljs-keyword">this</span>.workerId = workerId;
        <span class="hljs-keyword">this</span>.datacenterId = datacenterId;
    &#125;

    <span class="hljs-comment">// ==============================Methods==========================================</span>
    <span class="hljs-comment">/**
     * 获得下一个ID (该方法是线程安全的)
     * <span class="hljs-doctag">@return</span> SnowflakeId
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">synchronized</span> <span class="hljs-keyword">long</span> <span class="hljs-title">nextId</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">long</span> timestamp = timeGen();

        <span class="hljs-comment">//如果当前时间小于上一次ID生成的时间戳，说明系统时钟回退过这个时候应当抛出异常</span>
        <span class="hljs-keyword">if</span> (timestamp < lastTimestamp) &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> RuntimeException(
                    String.format(<span class="hljs-string">"Clock moved backwards.  Refusing to generate id for %d milliseconds"</span>, lastTimestamp - timestamp));
        &#125;

        <span class="hljs-comment">//如果是同一时间生成的，则进行毫秒内序列</span>
        <span class="hljs-keyword">if</span> (lastTimestamp == timestamp) &#123;
            sequence = (sequence + <span class="hljs-number">1</span>) & sequenceMask;
            <span class="hljs-comment">//毫秒内序列溢出</span>
            <span class="hljs-keyword">if</span> (sequence == <span class="hljs-number">0</span>) &#123;
                <span class="hljs-comment">//阻塞到下一个毫秒,获得新的时间戳</span>
                timestamp = tilNextMillis(lastTimestamp);
            &#125;
        &#125;
        <span class="hljs-comment">//时间戳改变，毫秒内序列重置</span>
        <span class="hljs-keyword">else</span> &#123;
            sequence = <span class="hljs-number">0L</span>;
        &#125;

        <span class="hljs-comment">//上次生成ID的时间截</span>
        lastTimestamp = timestamp;

        <span class="hljs-comment">//移位并通过或运算拼到一起组成64位的ID</span>
        <span class="hljs-keyword">return</span> ((timestamp - twepoch) << timestampLeftShift) <span class="hljs-comment">//</span>
                | (datacenterId << datacenterIdShift) <span class="hljs-comment">//</span>
                | (workerId << workerIdShift) <span class="hljs-comment">//</span>
                | sequence;
    &#125;

    <span class="hljs-comment">/**
     * 阻塞到下一个毫秒，直到获得新的时间戳
     * <span class="hljs-doctag">@param</span> lastTimestamp 上次生成ID的时间截
     * <span class="hljs-doctag">@return</span> 当前时间戳
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">long</span> <span class="hljs-title">tilNextMillis</span><span class="hljs-params">(<span class="hljs-keyword">long</span> lastTimestamp)</span> </span>&#123;
        <span class="hljs-keyword">long</span> timestamp = timeGen();
        <span class="hljs-keyword">while</span> (timestamp <= lastTimestamp) &#123;
            timestamp = timeGen();
        &#125;
        <span class="hljs-keyword">return</span> timestamp;
    &#125;

    <span class="hljs-comment">/**
     * 返回以毫秒为单位的当前时间
     * <span class="hljs-doctag">@return</span> 当前时间(毫秒)
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">long</span> <span class="hljs-title">timeGen</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> System.currentTimeMillis();
    &#125;

    <span class="hljs-comment">//==============================Test=============================================</span>
    <span class="hljs-comment">/** 测试 */</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
        SnowflakeIdWorker idWorker = <span class="hljs-keyword">new</span> SnowflakeIdWorker(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">int</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">1000</span>; i++) &#123;
            <span class="hljs-keyword">long</span> id = idWorker.nextId();
            System.out.println(Long.toBinaryString(id));
            System.out.println(id);
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>优点:</strong>
<ul>
<li>生成速度快</li>
<li>实现简单,没有多余的依赖</li>
<li>可以根据实际情况调整各个位段,方便灵活</li>
</ul>
</li>
<li><strong>缺点:</strong>
<ul>
<li>只能趋势递增</li>
<li>依赖机器时间. 如果发生回拨可能会造成生成的ID重复</li>
</ul>
</li>
</ul>
<blockquote>
<p><strong>SnowFlake算法时间回拨问题:</strong></p>
<ul>
<li><strong>时间回拨产生原因:</strong>
<ul>
<li>由于业务需要,机器需要同步时间服务器</li>
</ul>
</li>
<li><strong>时间回拨问题解决办法:</strong>
<ul>
<li>当回拨时间小于15ms,可以等待时间追上来以后再继续生成</li>
<li>当回拨时间大于15ms时可以通过更换workId来产生之前都没有产生过的Id来解决回拨问题</li>
</ul>
</li>
<li><strong>步骤:</strong>
<ul>
<li>首先将workId的位数进行调整至15位</li>
</ul>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d7915892c064d6da763dbfd43a22b46~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<ul>
<li>然后将<strong>SnowflakeIdWorker</strong>实现调整位段
<ul>
<li>使用<strong>1</strong>位作为<strong>符号位,</strong> 即生成的分布式I唯一d为正数</li>
<li>使用<strong>38</strong>位作为<strong>时间戳,</strong> 表示当前时间相对于初始时间的增量值,单位为毫秒</li>
<li>使用<strong>15</strong>位作为<strong>机器ID,</strong> 最多可支持3.28万个节点</li>
<li>使用<strong>10</strong>位作为<strong>毫秒内的序列号,</strong> 理论上可以生成2^10^个序列号</li>
</ul>
</li>
<li>因为服务的无状态关系,正常情况下<strong>workId</strong>不会配置在具体配置文件中,这里可以选择集中式的<strong>Redis</strong>作为中央存储:
<ul>
<li><strong>将workId调整位数后得到的多余的3万多个workId放置到一个基于Redis的队列中,用来集中管理workId</strong></li>
<li><strong>每次当节点启动的时候,先查看本地是否有workId,如果有那么就作为workId.如果没有,就在队列中取出一个当workId来使用,并从队列中删除</strong></li>
<li><strong>当发现时间回拨太多的时候,就再去队列中去一个来当新的workId使用,将刚刚那个使用回拨的情况的workId存到队列里. 因为队列每次都是从头取出,从尾部插入,这样可以避免刚刚A机器使用的workId又被B机器获取的可能性</strong></li>
<li>如果使用redis又会遇到新的小问题: redis一致性如何保证?redis挂了怎么办?怎么同步?</li>
</ul>
</li>
</ul>
</li>
</ul>
</blockquote>
<ul>
<li>从基础组件的使用角度来说,对于<strong>SnowflakeIdWorker</strong>算法当遇到时间回拨问题,只需要抛出异常即可,这样可以保证算法实现的简单性</li>
<li>也可以参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fbaidu%2Fuid-generator" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/baidu/uid-generator" ref="nofollow noopener noreferrer">uid-generator</a> 方法: 每次取一批<strong>workId,</strong> 集中之后批取,这样可以解决各个节点访问集中机器的性能问题.</li>
</ul></div>  
</div>
            