
---
title: '真枪实弹！Redis 「冷备」让您睡个安稳觉zZ'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19bea969c10e41a59037bd73f440ab11~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 02:50:32 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19bea969c10e41a59037bd73f440ab11~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第3天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<blockquote>
<p><strong>作者简介</strong>：悟空，8年一线互联网开发和架构经验，用故事讲解分布式、架构设计、Java 核心技术。《JVM性能优化实战》专栏作者，开源了《Spring Cloud 实战 PassJava》项目，公众号：<code>悟空聊架构</code>。本文已收录至 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.passjava.cn" title="https://link.juejin.cn?target=http%3A%2F%2Fwww.passjava.cn" target="_blank">www.passjava.cn</a></p>
</blockquote>
<p>Redis 的 RDB 持久化方案，相信大家都有所了解，但是对于企业来说，如果只是持久化了一个 RDB 文件，不足以应付生产级别的事故。通常的方案就是对 RDB 进行多个备份，今天带大家来真枪实弹操作下 RDB 的冷备，以及通过 RDB 进行数据恢复。</p>
<h2 data-id="heading-0">企业级冷备方案</h2>
<p>Redis RDB 持久化是非常适合做企业级的冷备方案的，这里的冷备可以理解为将已生成的文件拷贝到其他机器或者云服务器上。</p>
<p>RDB 适合做冷备的原因如下：</p>
<ul>
<li>RDB 文件生成后，改变的频率低，除非频繁触发检查点导致重新生成。</li>
<li>RDB 是 Redis 内存快照，比 AOF 日志恢复速度快。</li>
<li>RDB 的生成策略可以自行配置，而且可以配置多项，可以根据系统的使用场景和实际情况进行设置。</li>
</ul>
<h3 data-id="heading-1">备份方案</h3>
<p>1.用 Linux 自带的 crontab 命令执行定时任务，调用数据备份脚本。</p>
<p>2.每小时备份一份一次当前最新的 RDB 快照文件到指定目录，只保留最近 48 小时的备份。</p>
<p>3.每天备份一份当前最新的 RDB 快照文件到指定目录，只保留最近一个月的 备份。</p>
<p>4.每天晚上将备份文件都发送远程的云服务器上。</p>
<p>流程图如下所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19bea969c10e41a59037bd73f440ab11~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">每小时备份</h3>
<p>首先需要编写一个脚本，专门用来做数据备份，创建脚本的命令如下：</p>
<pre><code class="hljs language-SH copyable" lang="SH">mkdir /usr/<span class="hljs-built_in">local</span>/redis
mkdir /usr/<span class="hljs-built_in">local</span>/redis/copy
vi /usr/<span class="hljs-built_in">local</span>/redis/copy/redis_rdb_copy_hourly.sh
mkdir /usr/<span class="hljs-built_in">local</span>/redis/snapshotting
chmod 777 /usr/<span class="hljs-built_in">local</span>/redis
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后编写这个脚本文件：</p>
<pre><code class="hljs language-SH copyable" lang="SH"><span class="hljs-meta">#!/bin/sh </span>

cur_date=`date +%Y%m%d%H`
rm -rf /usr/<span class="hljs-built_in">local</span>/redis/snapshotting/<span class="hljs-variable">$cur_date</span>
mkdir /usr/<span class="hljs-built_in">local</span>/redis/snapshotting/<span class="hljs-variable">$cur_date</span>
cp /var/redis/6379/dump.rdb /usr/<span class="hljs-built_in">local</span>/redis/snapshotting/<span class="hljs-variable">$cur_date</span>

del_date=`date -d -48hour +%Y%m%d`
rm -rf /usr/<span class="hljs-built_in">local</span>/redis/snapshotting/<span class="hljs-variable">$del_date</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>脚本解释：</p>
<ul>
<li>cur_data 代表当前时间，精确到小时，比如 2021080616。</li>
<li>删除当前小时的快照文件。</li>
<li>创建当前小时的备份文件，文件为空的。</li>
<li>拷贝当前的快照文件到上一步创建的空的备份文件中。</li>
<li>del_date 代表 48 小时以前的时间，精确到小时，比如 2021080416。</li>
<li>删除 48 小时以前的备份文件。</li>
</ul>
<p>设置定时任务，每个小时的 0 分跑一次脚本：</p>
<pre><code class="hljs language-SH copyable" lang="SH">crontab -e
0 * * * * sh /usr/local.redis/copy/redis_rdb_copy_hourly.sh
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为要等到下一个小时的 0 点，所以就手动运行脚本来测试：</p>
<pre><code class="hljs language-sh copyable" lang="sh"><span class="hljs-built_in">cd</span> /usr/<span class="hljs-built_in">local</span>/redis/copy
./redis_rdb_copy_hourly.sh 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>会在 snapshotting 文件夹创建一个目录：2021080809，表示这是 2021-08-08 09 时的备份文件夹（注意这个时间是 UTC 时间）。这个目录里面还会有一个 dump.rdb 文件。如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e5c9524baf347d6b8f7a7719dffc542~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">每天备份</h3>
<p>和每小时备份类似，先创建一个每天备份一次的脚本：</p>
<pre><code class="hljs language-sh copyable" lang="sh">vi /usr/<span class="hljs-built_in">local</span>/redis/copy/redis_rdb_copy_daily.sh
chomd 777 *
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编写脚本：</p>
<pre><code class="hljs language-sh copyable" lang="sh"><span class="hljs-meta">#!/bin/sh </span>

cur_date=`date +%Y%m%d`
rm -rf /usr/<span class="hljs-built_in">local</span>/redis/snapshotting/<span class="hljs-variable">$cur_date</span>
mkdir /usr/<span class="hljs-built_in">local</span>/redis/snapshotting/<span class="hljs-variable">$cur_date</span>
cp /var/redis/6379/dump.rdb /usr/<span class="hljs-built_in">local</span>/redis/snapshotting/<span class="hljs-variable">$cur_date</span>

del_date=`date -d -1month +%Y%m%d`
rm -rf /usr/<span class="hljs-built_in">local</span>/redis/snapshotting/<span class="hljs-variable">$del_date</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建每天备份一次的定时任务：</p>
<pre><code class="hljs language-SH copyable" lang="SH">crontab -e

0 0 * * * sh /usr/<span class="hljs-built_in">local</span>/redis/copy/redis_rdb_copy_daily.sh
<span class="copy-code-btn">复制代码</span></code></pre>
<p>手动执行备份脚本：</p>
<pre><code class="hljs language-SH copyable" lang="SH"><span class="hljs-built_in">cd</span> /usr/<span class="hljs-built_in">local</span>/redis/copy
./redis_rdb_copy_daily.sh 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>会在 snapshotting 文件夹创建一个目录：20210808，表示这是今天 2021-08-08 的备份文件夹（注意这个时间是 UTC 时间）。这个目录里面还会有一个 dump.rdb 文件。如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7335cdf56b3e4b049e1322e5ef8982fa~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>另外这些备份建议都上传到云服务器上。</p>
<h2 data-id="heading-4">从备份文件中恢复</h2>
<p>假设一种场景：几个小时前上线的程序把 Redis 的数据都污染了，数据错了，该怎么办？</p>
<p>可以选择某个更早的时间点的备份文件进行恢复。</p>
<h4 data-id="heading-5">恢复的流程</h4>
<ul>
<li>停止 Redis，暂时关闭 AOF 的持久化配置。</li>
<li>删除 AOF 日志文件和 RDB 快照文件。</li>
<li>拷贝 RDB 快照文件到 Redis 的 RDB 文件加载目录。</li>
<li>重启 Redis，确认数据恢复成功。</li>
<li>热修改 Redis 的 AOF 持久化配置，Redis 会将内存中的数据写入到 AOF 文件中。</li>
<li>再次停止 Redis，手动修改配置文件，打开 AOF 持久化，防止热修改不生效。</li>
<li>再次重启 Redis。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e253825726747649c915943e450b9fc~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>参考资料：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.runoob.com%2Flinux%2Flinux-comm-date.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.runoob.com/linux/linux-comm-date.html" ref="nofollow noopener noreferrer">www.runoob.com/linux/linux…</a></p></div>  
</div>
            