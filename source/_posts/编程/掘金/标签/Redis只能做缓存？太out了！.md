
---
title: 'Redis只能做缓存？太out了！'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c093a0e26eb044a091442a9dae2e75d2~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 21:51:15 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c093a0e26eb044a091442a9dae2e75d2~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>⚠️本文为掘金社区首发签约文章，未获授权禁止转载</p>
</blockquote>
<p>大多数数据库，由于经常和磁盘打交道，在高并发场景下，响应会非常的慢。为了解决这种速度差异，大多数系统都习惯性的加入一个缓存层，来加速数据的读取。redis由于它优秀的处理能力和丰富的数据结构，已经成为了事实上的分布式缓存标准。</p>
<p>但是，如果你以为redis只能做缓存的话，那就太小看它了。</p>
<p>redis丰富的数据结构，使得它的业务使用场景非常广泛，加上rdb的持久化特性，它甚至能够被当作落地的数据库使用。在这种情况下，redis能够撑起大多数互联网公司，尤其是社交、游戏、直播类公司的半壁江山。</p>
<h2 data-id="heading-0"><strong>1. Redis能够胜任存储工作</strong></h2>
<p>redis提供了非常丰富的集群模式：<code>主从</code>、<code>哨兵</code>、<code>cluster</code>，满足服务高可用的需求。同时，redis提供了两种持久化方式：<code>aof</code>和<code>rdb</code>，常用的是rdb。</p>
<p>通过<code>bgsave</code>指令，主进程会fork出新的进程，回写磁盘。bgsave相当于做了一个快照，由于它并没有WAL日志和checkpoint机制，是无法做到实时备份的。如果机器突然断电，那就很容易丢失数据。</p>
<p>幸运的是，redis是内存型的数据库，主丛同步的速度是非常快的。如果你的集群维护的好，内存分配的合理，那么除非机房断电，否则redis的SLA，会一直保持在非常高的水平。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c093a0e26eb044a091442a9dae2e75d2~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<p>听起来不是绝对可靠啊，有丢失数据的可能！这在一般CRUD的业务中，是无法忍受的。但为什么redis能够满足大多数互联网公司的需求？这也是由业务属性所决定的。</p>
<p>在决定最大限度拥抱redis之前，你需要确认你的业务是否有以下特点：</p>
<p>除了核心业务，是否大多数业务对于数据的可靠性要求较低，丢失一两条数据是可以忍受的？</p>
<ol>
<li>面对的是C端用户，可根据用户ID快速定位到一类数据，数据集合普遍较小？无大量范围查询需求？</li>
<li>是否能忍受内存型数据的成本需求？</li>
<li>是否业务几乎不需要事务操作？</li>
</ol>
<p>很幸运的是，这类业务需求特别的多。比如常见的社交，游戏、直播、运营类业务，都是可以完全依赖Redis的。</p>
<h2 data-id="heading-1"><strong>2. Reids应用场景</strong></h2>
<p>Redis具有松散的文档结构，丰富的数据类型，能够适应千变万化的scheme变更需求，接下来我将介绍Redis除缓存外的大量的应用场景。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c9e6117846a4683a8179d4d9fc9f646~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2"><strong>2.1 基本用户数据存储</strong></h3>
<p>在传统的数据库设计中，用户表是非常难以设计的，变更的时候会伤筋动骨。使用Redis的<code>hash</code>结构，可以实现松散的数据模型设计。某些不固定，验证型的功能属性，可以以JSON接口直接存储在hash的value中。使用hash结构，可以采用HGET和HMGET等指令，只获取自己所需要的数据，在使用上也是非常便捷的。</p>
<pre><code class="copyable">>HSET user:199929 sex m
>HSET user:199929 age 22
>HGETALL user:199929
1) "sex"
2) "m"
3) "age"
4) "22"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种非统计型的、读多写少的场景，是非常适合使用KV结构进行存储的。Redis的hash结构提供了非常丰富的指令，某个属性也可以使用<code>HINCRBY</code>进行递增递减，非常的方便。</p>
<h3 data-id="heading-3"><strong>2.2 实现计数器</strong></h3>
<p>上面稍微提了一下HINCRBY指令，而对于Redis的Key本身来说，也有<code>INCRBY</code>指令，实现<code>某个值</code>的递增递减。</p>
<p>比如以下场景：统计某个帖子的点赞数；存放某个话题的关注数；存放某个标签的粉丝数；存储一个大体的评论数；某个帖子热度；红点消息数；点赞、喜欢、收藏数等。</p>
<pre><code class="copyable">> INCRBY feed:e3kk38j4kl:like 1
> INCRBY feed:e3kk38j4kl:like 1
> GET feed:e3kk38j4kl:like
"2"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>像微博这样容易出现热点的业务，传统的数据库，肯定是撑不住的，就要借助于内存数据库。由于Redis的速度非常快，就不用再采用传统DB非常慢的<code>count</code>操作，所有这种递增操作都是毫秒级别的，而且效果都是实时的。</p>
<h3 data-id="heading-4"><strong>2.3 排行榜</strong></h3>
<p>排行榜能提高参与者的积极性，所以这项业务非常常见，它本质上是一个topn的问题。</p>
<p>Redis中有一个叫做zset的数据结构，使用跳表实现的有序列表，可以很容易实现排行榜一类的问题。当存入zset中的数据，达到千万甚至是亿的级别，依然能够保持非常高的并发读写，且拥有非常棒的平均响应时间（5ms以内）。</p>
<p>使用<code>zadd</code> 可以添加新的记录，我们会使用排行相关的分数，作为记录的score值，然后使用<code>zrevrange</code>指令即可获取实时的排行榜数据，而<code>zrevrank</code>则可以非常容易的获取用户的实时排名。</p>
<pre><code class="copyable">>ZADD sorted:xjjdog:2021-07  55 dog0
>ZADD sorted:xjjdog:2021-07  89 dog1
>ZADD sorted:xjjdog:2021-07  32 dog2
>ZCARD sorted:xjjdog:2021-07
>3
> ZREVRANGE  sorted:xjjdog:2021-07  0 -10 WITHSCORES # top10排行榜
1) "dog1"
2) "89"
3) "dog0"
4) "55"
5) "dog2"
6) "32"
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5"><strong>2.4 好友关系</strong></h3>
<p><code>set</code>结构，是一个没有重复数据的集合，你可以将某个用户的关注列表、粉丝列表、双向关注列表、黑名单、点赞列表等，使用独立的zset进行存储。</p>
<p>使用<code>ZADD</code>、<code>ZRANK</code>等，将用户的黑名单使用ZADD添加，ZRANK使用返回的sorce值判断是否存在黑名单中。使用<code>sinter</code>指令，可以获取A和B的共同好友。</p>
<p>除了好友关系，有着明确黑名单、白名单业务场景的数据，都可以使用set结构进行存储。这种业务场景还有很多，比如某个用户上传的通讯录，计算通讯录的好友关系等等。</p>
<p>在实际使用中，使用zset存储这类关系的更多一些。zset同set一样，都不允许有重复值，但zset多了一个score字段，我们可以存储一个时间戳，用来标明关系建立所发生的时间，有更明确的业务含义。</p>
<h3 data-id="heading-6"><strong>2.5 统计活跃用户数</strong></h3>
<p>类似统计每天的活跃用户、用户签到、用户在线状态，这种零散的需求，实在是太多了。如果为每一个用户存储一个bool变量，那占用的空间就太多了。这种情况下，我们可以使用<code>bitmap</code>结构，来节省大量的存储空间。</p>
<pre><code class="copyable">>SETBIT online:2021-07-23 3876520333 1
>SETBIT online:2021-07-24 3876520333 1
>GETBIT online:2021-07-23 3876520333
1
>BITOP AND active online:2021-07-23 online:2021-07-24
>GETBIT active 3876520333
1
>DEBUG OBJECT online:2021-07-23
Value at:0x7fdfde438bf0 refcount:1 encoding:raw serializedlength:5506446 lru:16410558 lru_seconds_idle:5
(0.96s)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意，如果你的id很大，你需要先进行一次预处理，否则它会占用非常多的内存。</p>
<p>bitmap包含一串连续的2进制数字，使用1bit来表示真假问题。在bitmap上，可以使用and、or、xor等位操作(<code>bitop</code>)。</p>
<h3 data-id="heading-7"><strong>2.6 分布式锁</strong></h3>
<p>Redis的分布式锁，是一种轻量级的解决方案。虽然它的可靠性比不上Zookeeper之类的系统，但Redis分布式锁有着极高的吞吐量。</p>
<p>一个最简陋的加锁动作，可以使用redis带nx和px参数的set指令去完成。下面是一小段简单的分布式样例代码。</p>
<pre><code class="copyable">public String lock(String key, int timeOutSecond) &#123;
    for (; ; ) &#123;
        String stamp = String.valueOf(System.nanoTime());
        boolean exist = redisTemplate.opsForValue().setIfAbsent(key, stamp, timeOutSecond, TimeUnit.SECONDS);
        if (exist) &#123;
            return stamp;
        &#125;
    &#125;
&#125;
public void unlock(String key, String stamp) &#123;
    redisTemplate.execute(script, Arrays.asList(key), stamp);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>删除操作的lua为。</p>
<pre><code class="copyable">local stamp = ARGV[1]
local key = KEYS[1]
local current = redis.call("GET",key)
if stamp == current then
    redis.call("DEL",key)
    return "OK"
end
<span class="copy-code-btn">复制代码</span></code></pre>
<p>redisson的RedLock，是使用最普遍的分布式锁解决方案，有读写锁的差别，并处理了多redis实例情况下的异常问题。</p>
<h3 data-id="heading-8"><strong>2.7 分布式限流</strong></h3>
<p>使用计数器去实现简单的限流，在Redis中是非常方便的，只需要使用incr配合expire指令即可。</p>
<pre><code class="copyable"> incr key
 expire key 1
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种简单的实现，通常来说不会有问题，但在流量比较大的情况下，在时间跨度上会有流量突然飙升的风险。根本原因，就是这种时间切分方式太固定了，没有类似滑动窗口这种平滑的过度方案。</p>
<p>同样是redisson的RRateLimiter，实现了与<code>guava</code>中类似的分布式限流工具类，使用非常便捷。下面是一个简短的例子：</p>
<pre><code class="copyable"> RRateLimiter limiter = redisson.getRateLimiter("xjjdogLimiter");
 // 只需要初始化一次
 // 每2秒钟5个许可
 limiter.trySetRate(RateType.OVERALL, 5, 2, RateIntervalUnit.SECONDS);
 
 // 没有可用的许可，将一直阻塞    
 limiter.acquire(3);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9"><strong>2.8 消息队列</strong></h3>
<p>redis可以实现简单的队列。在生产者端，使用LPUSH加入到某个列表中；在消费端，不断的使用RPOP指令取出这些数据，或者使用阻塞的BRPOP指令获取数据，适合小规模的抢购需求。</p>
<p>Redis还有PUB/SUB模式，不过pubsub更适合做消息广播之类的业务。</p>
<p>在Redis5.0中，增加了stream类型的数据结构。它比较类似于Kafka，有主题和消费组的概念，可以实现多播以及持久化，已经能满足大多数业务需求了。</p>
<h3 data-id="heading-10"><strong>2..9 LBS应用</strong></h3>
<p>早早在Redis3.2版本，就推出了GEO功能。通过<code>GEOADD</code>指令追加lat、lng经纬数据，可以实现坐标之间的距离计算、包含关系计算、附近的人等功能。</p>
<p>关于GEO功能，最强大的开源方案是基于PostgreSQL的PostGIS，但对于一般规模的GEO服务，redis已经足够用了。</p>
<h3 data-id="heading-11"><strong>2.10 更多扩展应用场景</strong></h3>
<p>要看redis能干什么，就不得不提以下java的客户端类库redisson。redisson包含丰富的分布式数据结构，全部是基于redis进行设计的。</p>
<p>redisson提供了比如Set、 SetMultimap、 ScoredSortedSet、 SortedSet, Map、 ConcurrentMap、 List、 ListMultimap、 Queue、BlockingQueue等非常多的数据结构，使得基于redis的编程更加的方便。在github上，可以看到有上百个这样的数据结构：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fredisson%2Fredisson%2Ftree%2Fmaster%2Fredisson%2Fsrc%2Fmain%2Fjava%2Forg%2Fredisson%2Fapi%25E3%2580%2582" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/redisson/redisson/tree/master/redisson/src/main/java/org/redisson/api%E3%80%82" ref="nofollow noopener noreferrer">github.com/redisson/re…</a></p>
<p>对于某个语言来说，基本的数组、链表、集合等api，配合起来能够完成大部分业务的开发。Redis也不例外，它拥有这些基本的api操作能力，同样能够组合成分布式的、线程安全的高并发应用。</p>
<p>由于Redis是基于内存的，所以它的速度非常快，我们也会把它当作一个中间数据的存储地去使用。比如一些公用的配置，放到redis中进行分享，它就充当了一个配置中心的作用；比如把JWT的令牌存放到Redis中，就可以突破JWT的一些限制，做到安全登出。</p>
<h2 data-id="heading-12"><strong>3. 一站式Redis面临的挑战</strong></h2>
<p>redis的数据结构丰富，一般不会在功能性上造成困扰。但随着请求量的增加，SLA要求的提高，我们势必会对Redis进行一些改造和定制性开发。</p>
<h3 data-id="heading-13"><strong>3.1 高可用挑战</strong></h3>
<p>redis提供了主从、哨兵、cluster等三种集群模式，其中cluster模式为目前大多数公司所采用的方式。</p>
<p>但是，redis的cluster模式，有不少的硬伤。redis cluster采用虚拟槽的概念，把所有的key映射到 0～16383个整数槽内，属于无中心化的架构。但它的维护成本较高，slave也不能够参与读取操作。</p>
<p>它的主要问题，在于一些批量操作的限制。由于key被hash到多台机器上，所以mget、hmset、sunion等操作就非常的不友好，经常发生性能问题。</p>
<p>redis的主从模式是最简单的模式，但无法做到自动failover，通常在主从切换后，还需要修改业务代码，这是不能忍受的。即使加上haproxy这样的负载均衡组件，复杂性也是非常高的。</p>
<p>哨兵模式在主从数量比较多的时候，能够显著的体现它的价值。一个哨兵集群，能够监控成百上千个集群，但是哨兵集群本身的维护是比较困难的。幸运的是，redis的文本协议非常简单，在netty中，甚至直接提供了redis的codec。自研一套哨兵系统，加强它的功能，是可行的。</p>
<h3 data-id="heading-14"><strong>3.2 冷热数据分离</strong></h3>
<p>redis的特点是，不管什么数据，都一股脑地搞到内存里做计算，这对于有时间序列概念，有冷热数据之分的业务，造成了非常大的成本考验。为什么大多数开发者喜欢把数据存放在MySQL中，而不是Redis中？除了事务性要求以外，很大原因是历史数据的问题。</p>
<p>通常，这种冷热数据的切换，是由中间件完成的。我们上面也谈到了，Redis是一个文本协议，非常简单。做一个中间件，或者做一个协议兼容的Redis模拟存储，是比较容易的。</p>
<p>比如我们Redis中，只保留最近一年的活跃用户。一个好几年不活跃的用户，突然间访问了系统，这时候我们获取数据的时候，就需要中间件进行转换，从容量更大，速度更慢的存储中查找。</p>
<p>这个时候，Redis的作用，更像是一个热库，更像是一个传统cache层做的事情，发生在业务已经上规模的时候。但是注意，直到此时，我们的业务层代码，一直都是操作的redis的api。它们使用这众多的函数指令，并不关心数据到底是真正存储在redis中，还是在ssdb中。</p>
<h3 data-id="heading-15"><strong>3.3 功能性需求</strong></h3>
<p>redis还能玩很多花样。举个例子，全文搜索。很多人都会首选es，但redis生态就提供了一个模块：RediSearch，可以做查询，可以做filter。</p>
<p>但我们通常还会有更多的需求，比如统计类、搜索类、运营效果分析等。这类需求与大数据相关，即使是传统的DB也不能胜任。这时候，我们当然要把redis中的数据，导入到其他平台进行计算啦。</p>
<p>如果你选择的是redis数据库，那么dba打交道的，就是rdb，而不是binlog。有很多的rdb解析工具(比如redis-rdb-tools)，能够定期把rdb解析成记录，导入到hadoop等其他平台。</p>
<p>此时，rdb成为所有团队的中枢，成为基本的数据交换格式。导入到其他db后的业务，该怎么玩怎么玩，完全不会因为业务系统选用了redis就无法运转。</p>
<h2 data-id="heading-16"><strong>4. 总结</strong></h2>
<p>大多数业务系统，跑在redis上，这是很多一直使用MySQL做业务系统的同学所不能想象的。看完了上面的介绍，相信你能够对redis能够实现的存储功能有个大体的了解。打开你的社交app、游戏app、视频app，看一下它们的功能，能够涵盖多少呢？</p>
<p>我这里要强调的是，某些数据，并不是一定要落地到RDBMS才算安全，它们并不是一个强需求。</p>
<p>那既然redis这么厉害，为什么还要有mysql、tidb这样的存储呢？关键还在于业务属性上。</p>
<p>如果一个业务系统，每次交互的数据，都是一个非常大的结果集，并涉及到非常复杂的统计、过滤工作，那么RDBMS是必须的；但如果一个系统，能够通过某个标识，快速定位到一类数据，这一类数据在可以预见的未来，是有限的，那就非常适合Redis<code>存储</code>。</p>
<p>一个电商系统，选用redis做存储就是作死，但一个社交系统就快活的多。在合适的场景选用合适的工具，才是我们应该做的。</p>
<p>但是一个系统，能否在产品验证期，就能快速的响应变化，快速开发上线，才是成功的关键。这也是使用redis做数据库，所能够带来的最大好处。千万别被那概率极低的丢数据场景，给吓怕了。比起产品成功，你的系统即使是牢如钢铁，也一文不值。</p>
<blockquote>
<p>⚠️本文为掘金社区首发签约文章，未获授权禁止转载</p>
</blockquote></div>  
</div>
            