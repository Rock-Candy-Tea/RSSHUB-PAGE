
---
title: 'Gitee：高并发大存储下的架构演进之路'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/efb80877244448b1a8295524282caf49~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 06 Apr 2021 18:56:10 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/efb80877244448b1a8295524282caf49~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>Gitee 自2013年推出以来，每年的数据量都是倍增的，截止到2021年3月份，Gitee 上已经有了600万+的开发者，超1500万的仓库，成为了国内首屈一指的研发协作平台。在数据日益增长的过程中，Gitee 的架构也是经过了数个迭代，才能支撑起目前的数据量级。我曾在不少的大会上分享过 Gitee 的架构，也和很多有类似场景的同学一起讨论过，偶然被问起有没有专门的文章来介绍 Gitee 架构的，所以难得假期有时间，将此主题整理成文，以供大家参阅。</p>
</blockquote>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/efb80877244448b1a8295524282caf49~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>作为国内发展最快的代码托管平台，Gitee 每天数据都在飞速的增长中，而且随着 DevOps 概念的普及，持续构建也给平台带来更多的请求和更大的并发量，每天需要处理上千万的 Git 操作，Gitee 架构也是在这个过程中逐步迭代发展起来的，回望 Gitee 架构的发展，主要分为5个阶段：</p>
<ul>
<li>
<p>单机架构</p>
</li>
<li>
<p>分布式存储架构</p>
</li>
<li>
<p>NFS 架构</p>
</li>
<li>
<p>自研分片架构</p>
</li>
<li>
<p>Rime 读写分离架构</p>
</li>
</ul>
<p>接下来就分享下 Gitee 整个架构的演进史。</p>
<h3 data-id="heading-0"></h3>
<h3 data-id="heading-1"><strong>单机架构</strong></h3>
<p>Gitee 上线于2013年5月份，上线之初就是一个单纯的单体 Rails 应用，所有的请求都是通过这个 Rails 应用进行负载的。</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64ad8636212640f487a719d5624ccf40~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>除了把 Mysql 和 Redis 单独一台机器进行部署之外，跟绝大多数 Web 应用不一样的是 Gitee 需要存储大量的 Git 仓库，无论是 Web 读写仓库还是通过 Git 的方式操作仓库，都是需要应用直接操作服务器上的裸仓库的。这种单体架构在访问量不大的时候还算可以，比如团队或者企业内部使用，但是如果把他作为一个公有云的 SaaS 服务提供出去的话，随着访问量和使用量的增长，压力也会越来越明显，主要就是以下两个：</p>
<ol>
<li>
<p>存储空间的压力</p>
</li>
<li>
<p>计算资源的压力</p>
</li>
</ol>
<p>由于开源中国社区的影响力，Gitee 在刚上线之处就涌入了大部分用户，完全不需要担心种子用户的来源。相反，随着社区用户越来越多的使用，首先遭遇的问题就是存储的压力，由于当时使用的是阿里云的云主机，最大的磁盘只能选择2T，虽然后面通过一些渠道实现了扩容，但是云主机后的物理机器也只是一个1U的机器，最多只能有4块硬盘，所以当存储达到接近8T之后，除了外挂存储设备，没有什么更好的直接扩容的方式了。</p>
<p>而且随着使用量的增加，每到工作日的高峰期，比如早上9点左右，下午5点左右，是推拉代码的高峰期，机器的IO几乎是满负载的，所以每到这个时候整个系统都会非常缓慢，所以系统扩容的事情刻不容缓。经过讨论，团队决定选择使用分布式存储系统 Ceph，在经过了一系列不算特别严谨的「验证」后（这也是后面出问题的根本原因），我们就采购机器开始进行系统的扩容了。</p>
<h3 data-id="heading-2"><strong>分布式存储架构</strong></h3>
<p>Ceph 是一个分布式文件系统，它的主要目标是设计成基于POSIX的没有单点故障的分布式文件系统，能够轻松的扩展到数PB级别的容量，所以当时的想法是借助于 Ceph 的横向扩容能力以及高可靠性，实现对存储系统的扩容，并且在存储系统上层提供多组无状态的应用，使这些应用共享 Ceph 存储，从而进一步实现了计算资源扩容的目的。</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2249802140c64b3183bfa44b2f41736a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>于是在2014年7月份的时候我们采购了一批机器，开始进行系统的搭建和验证，然后挑选了一个周末开始进行系统的迁移与上线。迁移完成后的功能验证一切正常，但是到了工作日，随着访问量的增加，一切开始往不好的方向发展了，整个系统开始变得非常缓慢，经过排查，发现系统的瓶颈在 Ceph 的 IO 上，于是紧急调用了一台 ISCSI 存储设备，将数据进行迁移进行压力的分担。本以为一切稳定了下来，但是更可怕的事情发生了，Ceph RBD 设备突然间被卸载，所有的仓库数据都没了，瞬间整个群和社区都炸开了锅，经过14个小时的分析和研究，终于把设备重新挂载上，然后全速将数据迁往 ISCSI 存储设备，才逐步平息了这场风波。</p>
<ul>
<li>
<p>海量小文件的读写性能瓶颈</p>
</li>
<li>
<p>RBD 块设备意外卸载</p>
</li>
</ul>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0104a22816054100b1b16c9b5d4d988b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>后来经过研究，才发现分布式存储系统并不适合用在 Git 这种海量小文件的场景下，因为 Git 每一次的操作都需要遍历大量的引用和对象，导致每一次操作整体耗时非常多，Github 之前发过一篇博客，也有提到分布式存储系统不适用于 Git 这种场景。而且在块设备被卸载掉的时候，我们花费了长达14个小时的时间去进行恢复，这也是对工具没有一个深入了解就去贸然使用的后果。经过这次血与泪的教训，我们更加谨慎，更加细心的去做后续所有的调整。</p>
<h3 data-id="heading-3">NFS 架构</h3>
<p>不过，存储压力和计算压力依旧在，是迫在眉睫需要解决的问题，怎么办呢？于是为了临时解决问题，我们采用了相对原始的方案，也就是2014年 Gitlab 官方提供的方案</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/926252197e414b3b9255ead739a21c0d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这个方案主要就是使用 NFS 来进行磁盘的共享，在上游搭建多台应用实例来实现计算资源的扩展，但是由于存储都是走网络，必然会带来性能的损耗，而且在实际应用的过程中，由于 Git 操作的场景比较复杂，会带来一系列的问题</p>
<ul>
<li>
<p>内网带宽瓶颈</p>
</li>
<li>
<p>NFS 性能问题导致雪崩效应</p>
</li>
<li>
<p>NFS缓冲文件导致删除不彻底</p>
</li>
<li>
<p>无法方便的横向扩展存储，毫无维护性</p>
</li>
</ul>
<h4 data-id="heading-4"></h4>
<h4 data-id="heading-5"><strong>内网带宽瓶颈</strong></h4>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ff5f490312342b6be1c450927a6a6c3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>因为存储都是经过 NFS 进行挂载的，如果有比较大的比如超过 1G 的仓库，它在执行 Clone 的时候将会消耗大量的内网带宽，一般情况下我们的服务器的网口都是 1Gbps 的，所以很容易就会把网卡占满，占满导致的情况就是其它仓库的操作速度被拖慢，进而导致大量的请求阻塞。这还不是最严重的，最严重的情况是内部服务网口被占满，导致 Mysql、Redis 等服务严重丢包，整个系统会非常缓慢，这种情况当时的解决方式就是把核心服务的调用走其它网口来解决，但是 NFS 网口的问题仍然没法解决。</p>
<h4 data-id="heading-6"><strong>NFS 性能问题导致雪崩效应</strong></h4>
<p>这个就比较好理解了，如果某台 NFS 存储机器的 IO 性能过慢，同时所有的应用机器都有这个存储机器的读写请求，那整个系统就会出问题，所以这个架构下的系统是非常脆弱的，经不起考验。</p>
<h4 data-id="heading-7"><strong>NFS缓冲文件导致删除不彻底</strong></h4>
<p>这个问题是非常头疼的问题，问题的原因是因为为了提升文件的读写性能，开启了 NFS 内存缓存，所以会出现有些机器删除了 NFS 存储上的一些文件，但是在另外的机器上还存在于内存中，导致应用的一些逻辑判定出问题。</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab432bd29ccd480fb44432b5a4b3253f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>举个例子，Git 在推送的过程中会产生<code>.lock</code>文件，为的是防止在分支推送的过程中其它客户端同时推送造成的问题，所以如果我们往<code>master</code>分支推送代码的时候，服务端会产生<code>master.lock</code>文件，这样其它客户端就没有办法同时往<code>master</code>分支上推送代码了。在推送完代码后，Git 会自动的清除掉<code>master.lock</code>文件，但由于上面我们说的原因，有一些情况下我们在一台应用机处理完推送请求后，明明已经删除掉这个<code>master.lock</code>文件了，但是在另外一台应用机器的内存里还存在，就会导致无法推送。解决这个问题的方法就是关闭 NFS 内存级别的缓存，但是性能就会受损，还真是难以抉择，好在出现这种问题的情况极少，所以为了性能，只能忍受了。</p>
<h4 data-id="heading-8"><strong>维护性差</strong></h4>
<p>还是那句老话，由于历史原因，应用的存储目录结构是固定的，所以我们不得不通过软连接的方式对整个目录进行扩容，而扩容的前提是要把 NFS 存储的设备挂载在目录呀，所以当时整个系统每个应用机器的挂载情况是非常复杂的</p>
<pre><code class="copyable">git@gitee-app1:~$ df -h
Filesystem                Size  Used Avail Use% Mounted on
/dev/sda1                184G   15G  160G   9% /
/dev/sda2                307G   47G  245G  16% /home
172.16.3.66:/data    10T     50G  9.9T     1%  /data
172.16.30.1:/disk1   10T     50G  9.9T     1%  /disk1
172.16.30.2:/disk2   10T     50G  9.9T     1%  /disk2
172.16.30.3:/disk3   10T     50G  9.9T     1%  /disk3
172.16.30.4:/disk4   10T     50G  9.9T     1%  /disk4
172.16.30.5:/disk5   10T     50G  9.9T     1%  /disk5
172.16.30.6:/disk6   10T     50G  9.9T     1%  /disk6
172.16.30.7:/disk7   10T     50G  9.9T     1%  /disk7
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>哇，看到这样的目录结构，运维要哭了，维护起来极其困难，如此下去，失控是早晚的事。</p>
<h3 data-id="heading-9"><strong>自研分片架构</strong></h3>
<p>NFS 这样的方式可以抵挡一阵子，但是并不是长久之计，所以必须寻求改变，在架构上做改进。理想的方式当然是 Github 那种分片架构，通过 RPC 的方式将应用和仓库调用拆离开来，这样无论是扩展和维护都会比较方便</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7ba37be9c284abf8fbd3b7a64bf9542~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>但是这种改造需要对应用进行改造，成本大，周期长，而且鉴于当时的情况，基本没有太多的研发资源投入在架构上，那怎么办呢？当时在做这个架构讨论的时候，我们有一位前端同事（昵称：一只大熊猫）提了一个想法，既然应用无法拆离，那为什么不再网上一层做分片路由呢？</p>
<blockquote>
<p>题外话：团队内部的「提问」是非常有必要的，而且激发了团队讨论的氛围，我们能够更好的做一些有价值的东西，所以每一个团队成员，尤其是作为一个开发者，永远不要怕说，你的一个小小的想法，对于团队可能是一次非常长远的影响。比如这位熊猫先生的一句话，就直接决定了后续 Gitee 架构的发展方向，有空希望能够再一起吃竹子 ;D</p>
</blockquote>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/138ecac4599545d29cd31f24238cfce6~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>于是，第一版本的架构应运而生，我们不改变应用原有的结构，并允许应用是有状态的，也就是应用与仓库捆绑，一组应用对应一批仓库，只要能够在请求上进行辨识，并将其分发到对应的应用上进行处理即可。</p>
<p>从业务角度来讲，Gitee 上的请求分为3类：</p>
<ol>
<li>
<p>http(s) 请求，浏览仓库以及 Git 的 http(s) 方式操作代码</p>
</li>
<li>
<p>SSH 请求，Git 的 SSH 方式操作代码</p>
</li>
<li>
<p>SVN 请求，Gitee 特性，使用 SVN 的方式操作 Git 仓库</p>
</li>
</ol>
<p>所以我们只需要对这三类请求进行分片路由，从请求中截取仓库信息，根据仓库信息找到对应的机器，然后进行请求的转发即可。由此我们开发了3个组件，分别为这三种请求做路由代理</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f0b9ce728884e34b4e2a210a99969da~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-10"><strong>Miracle http(s) 动态分发代理</strong></h4>
<p>组件基于 Nginx 进行二次开发，主要的功能就是通过对 URL 进行截取，获取到仓库的命名空间，然后根据这个命名空间进行 Proxy。比如上图中我们请求了<code>https://gitee.com/zoker/taskover</code>这个仓库，Miracle 或通过 URL 得知这个请求是请求<code>zoker</code>的仓库，所以 Miracle 会先去路由 Redis 查找<code>User.zoker</code>的路由，如果不存在则去数据库进行查找，并在路由 Redis 进行缓存，用来提升获取路由 IP 地址的速度。拿到 IP 之后，Miracle 就会动态的将这个请求 Proxy 对应的后端 App1 上，那么用户就会正确的看到这个仓库的内容。</p>
<p>对于路由的分发一定是要保证准确的，如果<code>User.zoker</code>取到的是一个错误的 IP，那么用户看到的现象就是空仓库，这不是我们所期望的。另外，对于非仓库的请求，也就是跟仓库资源无关的请求，比如登陆，动态等，将会随机分发到任一台后端机器，因为与仓库无关，所以任意一台后端机器均可处理。</p>
<h4 data-id="heading-11"><strong>SSH & SVN 动态分发代理</strong></h4>
<p>SSHD 组件主要是用来对 Git 的 SSH 请求进行分发代理，使用 LibSSH 进行二开；SVNSBZ 是针对 SVN 请求的动态分发代理。两者实现的逻辑与 Miracle 类似，这里不再赘述。</p>
<h4 data-id="heading-12"><strong>遗留问题</strong></h4>
<p>这种架构上线后，无论是从架构负载上，还是从运维维护成本上，都有了极大的改进。但是架构的演进总是无尽头的，没有万金油，当前的架构还是存在一些问题：</p>
<ul>
<li>
<p>以用户为原子单位的分片过大</p>
</li>
<li>
<p>Git via https 请求由 GiteeWeb 处理，相互会影响</p>
</li>
<li>
<p>Git via SSH、SVN 相关操作的 Api 仍旧由 GiteeWeb 处理</p>
</li>
<li>
<p>未解决单仓负载过大的问题</p>
</li>
</ul>
<p>因为是以用户或者组织为原子单位进行分片，所以如果一个用户下的仓库过多，体积过大，可能一台机器也处理不完，虽然我们在应用上限制了单个用户可创建的仓库数量以及体积，但是这种场景必定会出现，所以需要提前考虑。而且如果单仓库访问量过大，比如某些热门的开源项目，极端情况下一台机器也可能无法承受住这些请求，依旧是有缺陷的。</p>
<p>此外，Git 请求涉及到鉴权，所有的鉴权还是走的 GiteeWeb 的接口，并且 Git 的 https 操作依旧由 GiteeWeb 处理，并没有像 SSH 那样有单独的组件进行处理，所以耦合性还是太强。</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/315dbcea77dd4a31940ede8083280ce2~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>基于以上的一些问题，我们进一步对架构进行了改进，主要做了以下改动：</p>
<ul>
<li>
<p>以仓库为原子单位分片</p>
</li>
<li>
<p>Git via https 服务拆离</p>
</li>
<li>
<p>SSH、SVN 相关操作的 Api 拆离</p>
</li>
</ul>
<p>以仓库分片使路由的原子单位更小，更容易进行管理和扩容，仓库路由主要是以<code>所属空间/仓库地址</code>为键，类似于<code>zoker/taskover</code>这种键进行路由</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93ae7435b05a415dbfbcb82909d8eafa~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>把 Git 的 http(s) 操作拆离出来的主要目的就是为了不让它影响到 Web 的访问，因为 Git 的操作是非常耗时的，场景不一样，放在一起容易出现影响。而鉴权相关的 Api 的独立也是为了减少 GiteeWeb 的压力，因为推拉这种操作是非常非常多的，所以 Api 的访问也会非常大，把它跟常规的用户 Web 请求混在一起也是非常容易相互影响的。</p>
<p>在做完这些拆离之后，GiteeWeb 的稳定性提升了不少，由于 Api 和 Git 操作带来的不稳定下降了 95% 左右。整个架构组件的构成类似于这样</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be7c89be655349409785aa2a598e48e3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-13"><strong>遗留问题</strong></h4>
<p>虽然提升了系统整体的稳定性，但是我们还是需要考虑一些极端的情况，比如如果单仓库过大怎么办？单仓库访问量过大怎么办？好在系统能够对单仓库的容量进行限制，但是如果是一个非常热非常火的仓库呢？如果出现那种突然间大并发的访问，该如何适应呢？</p>
<h3 data-id="heading-14"><strong>Rime 读写分离架构</strong></h3>
<p>Gitee 作为国内最大的研发协作平台，也作为首屈一指的代码托管平台，众多的开源项目在 Gitee 上建立了生态，其中不乏热度非常高的仓库，并且在高校、培训机构、黑客马拉松等场景也是作为代码托管平台的首选，经常都可以遇到大并发的访问。但是目前架构主要的问题是机器的备份都是冷备，没有办法有效的利用起来，并且单仓请求负载过大的问题也没有解决。</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d8b7c199ecc438e809b27e7fb59616f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-15"><strong>为什么要做 Rime 架构？</strong></h4>
<p>自从华为入驻 Gitee 之后，我们才开始真正的重视这个问题。2020年开始，华为陆续在 Gitee 平台上开源了 MindSpore、openEuler 等框架，单仓库的压力才逐渐显现出来，为了迎接2020年9月份举世瞩目的鸿蒙操作系统开源，我们在2020上半年继续优化了我们的架构，使其能够多机负载同一个仓库的 IO 操作，这就是我们现在的 Rime 读写分离架构。</p>
<h4 data-id="heading-16"></h4>
<h4 data-id="heading-17"><strong>实现原理</strong></h4>
<p>想要实现机器的多读的效果，就必须考虑到仓库同步一致性的问题。试想，如果一个请求被分发到一台备机，刚好主机又刚推送过代码，那么用户在网页上看到的仓库将会是推送前的，这就是一个非常严重的问题，那么该如何保证用户访问备机也是最新的代码呢？或者说如何保证同步的及时性？这里我们采用的如下的逻辑来进行保证</p>
<ol>
<li>
<p>写操作写往主机</p>
</li>
<li>
<p>由主机主动发起同步到备机</p>
</li>
<li>
<p>主动维护同步状态，根据同步状态决定路由分发</p>
</li>
</ol>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b3f75aefceb540be8bc28377d1099bfd~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>如上图所示，我们把仓库的操作分为读和写两种，一般情况下，读可以均等分发到各个的备机，这样一来如果我们有一台主机，两台备机，那么在不考虑其它因素的情况下，理论上仓库的读取能力是增加了3倍的。但是考虑到仓库会有写的情况，那就会涉及到备机的同步，刚刚我们也说过，如果同步不及时，就会导致访问到了老的代码，这显然是一个极大的缺陷。</p>
<p>为了解决这个问题，我们利用 Git 的钩子，在仓库被写入之后，同步触发一个同步的队列，这个队列的主要任务有如下几个：</p>
<ol>
<li>
<p>同步仓库到备机</p>
</li>
<li>
<p>验证同步后的仓库的一致性</p>
</li>
<li>
<p>管理变更同步状态</p>
</li>
</ol>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/310975edc3bd475293d58ac2dd0bfcc3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>当一个仓库有推送之后，会由 Git 钩子触发一个同步任务，这个任务会主动的将增量同步到配置的备机，在同步完成后，会进行引用的一致性校验，这个一致性校验使用的是<code>blake3</code>哈希算法，通过对<code>refs/</code>中的内容进行编码，来确认同步后的仓库是否版本完全一致。</p>
<p>对于状态管理，当触发任务之后，会第一之间将两台备机的这个仓库状态设置为未同步，我们的分发组件对于读操作，只会分发到主机或者设置为已同步状态的备机，当同步完成并且完成一致性校验之后，会将相关备机的同步状态设置为已同步，那么读操作就又会分发到备机上来了。但是如果同步失败，比如上图中同步到 App1bakA 的是成功的，那么读操作是可以正常的分发到备机的，但是 App1bakB 却是失败的，那么读操作就不会分发到未同步的机器，避免访问上出现不一致的问题。</p>
<h4 data-id="heading-18"><strong>架构成果</strong></h4>
<p>通过对架构的读写分离的改造，系统对于单仓库访问过大的这种情况也能够轻松应对了。2020年9月10号，华为鸿蒙操作系统正式在 Gitee 上开源，这个备受瞩目的项目一经开放就给 Gitee 带来了巨大的流量以及大量的仓库下载操作，由于前期工作准备充分，并且读写分离架构极大提升了单仓库负载的性能，所以算是完美的为鸿蒙操作系统成功的保驾护航了。</p>
<p><img alt="图片" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/737f6a27d17a4bd0b7b452daf8b288fb~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-19"></h4>
<h4 data-id="heading-20"><strong>后续优化</strong></h4>
<p>可能有细心的同学已经想到了，如果一个仓库不同的在写，并且同时伴随着巨大的访问量，那么是不是就变成了单机器要去处理这些所有的请求？答案是 Yes，但是这种场景正常情况下是没有的，一般情况下写操作的频率是远远低于读操作的，如果真的出现了这种情况，只能说明被攻击了，那么我们在组件上也进行了单仓库最大并发的限制，这也是我们维护 Gitee 以来得出的合理的限制条件，完全不会影响到正常用户的使用。</p>
<p>但是架构的优化是无止境的，对于上面提到的情况，我们依旧是需要进行改良的，目前主要的做法主要是提交的时候同步更新，备机同步成功或者部分备机同步成功才算本次推送成功，这种方式缺点是会加长用户推送的时间，但是能够很好的解决主机单读的问题。目前的架构是多读单写，如果后面这个领域内出现了一些频繁写入的场景，可以考虑变更为多读多写，做好状态和冲突的维护即可。</p>
<h3 data-id="heading-21"><strong>未来展望</strong></h3>
<p>目前的架构最大的问题就是应用和仓库的操作未拆离，这对于架构的扩展性是极为不利的，所以目前或者后续我们正在做的就是对服务进行拆离和其他方面的优化：</p>
<ol>
<li>
<p>仓库的操作拆离，单独以 RPC 的方式进行调用</p>
</li>
<li>
<p>应用的前后端分离</p>
</li>
<li>
<p>队列、通知等服务的拆离</p>
</li>
<li>
<p>热点仓库的自动按需扩容</p>
</li>
<li>
<p>根据机器的指标进行新仓库的分配</p>
</li>
<li>
<p>...</p>
</li>
</ol>
<h3 data-id="heading-22"></h3>
<h3 data-id="heading-23"><strong>最后</strong></h3>
<p>Gitee 自2013年上线以来，直到2017年自研架构上线才真正解决了内忧外患，「内」是因为架构无法撑起访问量导致的各种不稳定，「外」是外部的一些 DDOS、CC 攻击等难以招架，好在架构这项内功修炼得当，这些一直以来的问题才能够轻松自如的应对。</p>
<p>有句老话说得好，脱离了一切场景谈技术的行为都是耍流氓，架构亦如是，脱离了背景去谈架构是毫无意义的，很多时候我们做了非常多的工作，可能只是能够解决当前或者未来几年的问题，但是我们需要高瞻远瞩，对后续产品的发展、数据的增长、功能的增强做预估，这样才能更好的改变架构来适应这个高速发展的领域，进而更好的去服务企业和赋能开发者。</p>
<blockquote>
<p>原文作者为 Gitee 负责人周凯，发表于公众号「Zoker随笔」</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            