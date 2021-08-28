
---
title: '比较RDS for SqlServer、Aurora for MySQL、Auro for postgreSQL的性能'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/336725a725ba41b59953863b77fb887a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 28 Aug 2021 03:08:13 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/336725a725ba41b59953863b77fb887a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第28天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<blockquote>
<ul>
<li>📢欢迎点赞 ：👍 收藏 ⭐留言 📝 如有错误敬请指正，赐人玫瑰，手留余香！</li>
<li>📢本文作者：由webmote 原创，首发于 【掘金】</li>
<li>📢作者格言： 生活在于折腾，当你不折腾生活时，生活就开始折腾你，让我们一起加油！💪💪💪</li>
</ul>
</blockquote>
<h1 data-id="heading-0">1. 比较数据库性能</h1>
<p>数据库的性能BenchaMark测试，在很久以前，各大公司热衷于做各种读写测试，好像最好都测不过Oracle的性能，然后慢慢的大家都沉寂下来，特别是最近几年，鲜有人直接做数据库的性能测试了。</p>
<p>也许随着分布式应用的普及，可能大家都对单机的数据库性能测试不感兴趣了。</p>
<p>据搜索，在2010年之前，有个老外做过SqlServer和MySQL的性能测试，据测试报告说，SQL Server的性能是MySQL的10倍以上，不过这样的性能差，并不影响MySQL成为全球最流行的数据库之一。</p>
<p>看看DB流行度，MySQL排在第二名，SQL server排在第三名，其他的数据库都在下面。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/336725a725ba41b59953863b77fb887a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>因此，可以得出一个简答的结论，单独的看数据库的性能，没有意义。</p>
<h1 data-id="heading-1">2. 怎么测试数据库性能</h1>
<p>不管数据库的性能是不是能决定架构选型，那既然公司比较看重性能的比对，那我们还是需要在一定的基准下测试下数据库的性能。</p>
<p>对于Aurora，AWS生成其比同类型的MySQL快5倍，比PosgreSQL快3倍，AWS怎么测试，都是为了卖它的Aurora，因此其实并不是很科学。当然业界也没有更科学的方案，因此SysBench在此方面就是唯一的选择。</p>
<p>那么我们就使用SysBench来测试各个数据库的性能吧。</p>
<p>对于SqlServer，我并没有看到支撑SqlServer测试的脚本，而对于MySQL和PostgreSQL都有写好的lua脚本，因此我们就不用再考虑脚本的问题了。</p>
<h1 data-id="heading-2">3.准备环境</h1>
<p>我们需要一个标准的测试环境，从硬件配置上应该各个数据库基本保持一致。</p>
<ul>
<li>3台EC2 测试环境，作为客户端发起读写操作</li>
<li>3台服务器，每个数据库一台服务器，配置均为4核32G，SSD硬盘标配。</li>
</ul>
<p>每台EC2虚拟机安装 sysbench测试环境。</p>
<p>连接到各个数据库，开始灌入测试数据。</p>
<pre><code class="hljs language-shell copyable" lang="shell">sudo sysbench --db-driver=mysql --oltp-table-size=100000 --oltp-tables-count=24 --threads=1 --mysql-host=aaa.amazonaws.com --net=host --mysql-port=3306 --mysql-user=admin --mysql-password=12345678  --mysql-db=db1 /usr/share/sysbench/tests/include/oltp_legacy/parallel_prepare.lua prepare

<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后进行读写操作测试，并记录TPS和QPS，就这样，测试完成了，仅仅做单表的测试应该是不够的，不过又有什么关系呢，这仅仅是个粗略的测试，各个数据库的优势不同，非要拿一个尺子丈量，估计是各有优缺吧，因此我们笃定一个标准。</p>
<pre><code class="hljs language-shell copyable" lang="shell">
sysbench /usr/share/sysbench/tests/include/oltp_legacy/oltp.lua --mysql-host=aaa.amazonaws.com  --mysql-user=admin --mysql-password="12345678" --mysql-port=3306  --mysql-db=db1 --max-requests=0 --oltp-simple-ranges=0 --oltp-distxinct-ranges=0 --oltp-sum-ranges=0 --oltp-order-ranges=0 --time=300 --oltp-read-only=on --threads=1000 --report-interval=10 run

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">4.比较测试结果</h1>
<p>为了测试的公正性，我们需要保持每个数据库服务器的cpu利用均达到一个高负载的情况。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/912b92b3c6e5444b91a095c9eccda072~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里晒下AWS的测试结果：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4fda8525b65a43bbaee8123cafd04138~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>嗯，就是这个味道。</p>
<p>一切环境都已就绪，本想今天区公司加班呢，结果睡到了11：00，算了，工作日继续测试吧，我就先总结下，mysql和postgreSQL可预见的顺利，而SQLserver可能需要编写lua测试脚本了。</p>
<p>不过没关系，脚本难不倒小小架构师，就期待我的测试结果吧！</p>
<h1 data-id="heading-4">5. 小结</h1>
<p>postgreSQL具有丰富的功能，但应用并不广，很多三方组件并没有postgreSQL的支持；因此我还是比较侧重于选项MySQL的，掘友们教教我，怎么说服公司放弃postgreSQL，而选用MySQL？</p>
<p>例行小结，理性看待！</p>
<p>结的是啥啊，结的是我想你点赞而不可得的寂寞。😳😳😳</p>
<p>👓都看到这了，还在乎点个赞吗？</p>
<p>👓都点赞了，还在乎一个收藏吗？</p>
<p>👓都收藏了，还在乎一个评论吗？</p></div>  
</div>
            