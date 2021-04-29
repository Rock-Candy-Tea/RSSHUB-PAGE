
---
title: 'Go语言能做什么 _ Go主题月'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=3831'
author: 掘金
comments: false
date: Tue, 27 Apr 2021 17:01:58 GMT
thumbnail: 'https://picsum.photos/400/300?random=3831'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、我们为什么选择Go语言</h2>
<p>选择Go语言的原因可能会有很多，关于Go语言的特性、优势等，我们在之前的文档中也已经介绍了很多了。但是最主要的原因，应该是基于以下两方面的考虑：</p>
<ol>
<li>
<p>执行性能</p>
<p>缩短API的响应时长，解决批量请求访问超时的问题。在Uwork的业务场景下，一次API批量请求，往往会涉及对另外接口服务的多次调用，而在之前的PHP实现模式下，要做到并行调用是非常困难的，串行处理却不能从根本上提高处理性能。而GO语言不一样，通过协程可以方便的实现API的并行处理，达到处理效率的最大化。 依赖Golang的高性能HTTP Server，提升系统吞吐能力，由PHP的数百级别提升到数千里甚至过万级别。</p>
</li>
<li>
<p>开发效率</p>
<p>GO语言使用起来简单、代码描述效率高、编码规范统一、上手快。 通过少量的代码，即可实现框架的标准化，并以统一的规范快速构建API业务逻辑。 能快速的构建各种通用组件和公共类库，进一步提升开发效率，实现特定场景下的功能量产。</p>
</li>
</ol>
<h2 data-id="heading-1">二、Go语言能做什么</h2>
<p>Go 语言从发布 1.0 版本以来备受众多开发者关注并得到广泛使用，Go 语言的简单、高效、并发特性吸引了众多传统语言开发者的加入，而且人数越来越多。</p>
<p>鉴于Go语言的特点和设计的初衷，Go语言作为服务器编程语言，很适合处理日志、数据打包、虚拟机处理、文件系统、分布式系统、数据库代理等；网络编程方面，Go语言广泛应用于Web 应用、API应用、下载应用等；除此之外，Go语言还适用于内存数据库和云平台领域，目前国外很多云平台都是采用Go开发。</p>
<ul>
<li>服务器编程，以前你如果使用C或者C++做的那些事情，用Go来做很合适，例如处理日志、数据打包、虚拟机处理、文件系统等。</li>
<li>分布式系统、数据库代理器、中间件等，例如Etcd。</li>
<li>网络编程，这一块目前应用最广，包括Web应用、API应用、下载应用，而且Go内置的net/http包基本上把我们平常用到的网络功能都实现了。</li>
<li>数据库操作</li>
<li>开发云平台，目前国外很多云平台在采用Go开发</li>
</ul>
<h2 data-id="heading-2">三、国内外有哪些企业或项目使用Go语言</h2>
<p>Go发布之后，很多公司特别是云计算公司开始用Go重构他们的基础架构，很多都是直接采用Go进行了开发，最近热火朝天的Docker就是采用Go开发的。</p>
<p>使用 Go 语言开发的开源项目非常多。早期的 Go 语言开源项目只是通过 Go 语言与传统项目进行C语言库绑定实现，例如 Qt、Sqlite 等；后期的很多项目都使用 Go 语言进行重新原生实现，这个过程相对于其他语言要简单一些，这也促成了大量使用 Go 语言原生开发项目的出现。</p>
<ul>
<li>
<p>云计算基础设施领域</p>
<p>代表项目：docker、kubernetes、etcd、<a href="http://tonybai.com/2015/07/06/implement-distributed-services-registery-and-discovery-by-consul/" target="_blank" rel="nofollow noopener noreferrer">consul</a>、cloudflare CDN、七牛云存储等。</p>
</li>
<li>
<p>基础软件</p>
<p>代表项目：<a href="https://github.com/pingcap/tidb" target="_blank" rel="nofollow noopener noreferrer">tidb</a>、<a href="https://github.com/influxdata/influxdb" target="_blank" rel="nofollow noopener noreferrer">influxdb</a>、<a href="https://github.com/cockroachdb/cockroach" target="_blank" rel="nofollow noopener noreferrer">cockroachdb</a>等。</p>
</li>
<li>
<p>微服务</p>
<p>代表项目：<a href="https://github.com/go-kit/kit" target="_blank" rel="nofollow noopener noreferrer">go-kit</a>、<a href="https://github.com/micro/micro" target="_blank" rel="nofollow noopener noreferrer">micro</a>、monzo bank的<a href="https://github.com/monzo" target="_blank" rel="nofollow noopener noreferrer">typhon</a>、<a href="https://www.bilibili.com/" target="_blank" rel="nofollow noopener noreferrer">bilibili</a>等。</p>
</li>
<li>
<p>互联网基础设施</p>
<p>代表项目：<a href="https://github.com/ethereum/go-ethereum" target="_blank" rel="nofollow noopener noreferrer">以太坊</a>、<a href="https://github.com/hyperledger" target="_blank" rel="nofollow noopener noreferrer">hyperledger</a>等。</p>
</li>
</ul>
<blockquote>
<p>采用Go的一些国外公司，如Google、Docker、Apple、Cloud Foundry、CloudFlare、Couchbase、CoreOS、Dropbox、MongoDB、AWS等公司；</p>
<p>采用Go开发的国内企业：如阿里云CDN、百度、小米、七牛、PingCAP、华为、金山软件、猎豹移动、饿了么等公司。</p>
</blockquote>
<h3 data-id="heading-3">Docker</h3>
<p>Docker 是一种操作系统层面的虚拟化技术，可以在操作系统和应用程序之间进行隔离，也可以称之为容器。Docker 可以在一台物理服务器上快速运行一个或多个实例。基于lxc的一个虚拟打包工具，能够实现PAAS平台的组建。例如，启动一个 CentOS 操作系统，并在其内部命令行执行指令后结束，整个过程就像自己在操作系统一样高效。</p>
<p>项目链接：</p>
<p><a href="https://github.com/docker/docker" target="_blank" rel="nofollow noopener noreferrer">github.com/docker/dock…</a></p>
<h3 data-id="heading-4">go语言</h3>
<p>Go 语言自己的早期源码使用C语言和汇编语言写成。从 Go 1.5 版本后，完全使用 Go 语言自身进行编写。Go 语言的源码对了解 Go 语言的底层调度有极大的参考意义，建议希望对 Go 语言有深入了解的读者读一读。</p>
<p>项目链接：</p>
<p><a href="https://github.com/golang/go" target="_blank" rel="nofollow noopener noreferrer">github.com/golang/go</a></p>
<h3 data-id="heading-5">Kubernetes</h3>
<p>Google 公司开发的构建于 Docker 之上的容器调度服务，用户可以通过 Kubernetes 集群进行云端容器集群管理。</p>
<p>项目链接：</p>
<p><a href="https://github.com/kubernetes/kubernetes" target="_blank" rel="nofollow noopener noreferrer">github.com/kubernetes/…</a></p>
<h3 data-id="heading-6">etcd</h3>
<p>一款分布式、可靠的 KV 存储系统，可以快速进行云配置。</p>
<p>项目链接：</p>
<p><a href="https://github.com/coreos/etcd" target="_blank" rel="nofollow noopener noreferrer">github.com/coreos/etcd</a></p>
<h3 data-id="heading-7">beego</h3>
<p>beego 是一个类似 Python的 Tornado 框架，采用了 RESTFul 的设计思路，使用 Go 语言编写的一个极轻量级、高可伸缩性和高性能的 Web 应用框架。</p>
<p>项目链接：</p>
<p><a href="https://github.com/astaxie/beego" target="_blank" rel="nofollow noopener noreferrer">github.com/astaxie/bee…</a></p>
<h3 data-id="heading-8">martini</h3>
<p>一款快速构建模块化的 Web 应用的 Web 框架。</p>
<p>项目链接：</p>
<p><a href="https://github.com/go-martini/martini" target="_blank" rel="nofollow noopener noreferrer">github.com/go-martini/…</a></p>
<h3 data-id="heading-9">codis</h3>
<p>国产的优秀分布式 Redis 解决方案。</p>
<p>项目链接：</p>
<p><a href="https://github.com/CodisLabs/codis" target="_blank" rel="nofollow noopener noreferrer">github.com/CodisLabs/c…</a></p>
<h3 data-id="heading-10">delve</h3>
<p>Go语言</p>
<p>强大的调试器，被很多集成环境和编辑器整合。</p>
<p>项目链接：</p>
<p><a href="https://github.com/derekparker/delve" target="_blank" rel="nofollow noopener noreferrer">github.com/derekparker…</a></p>
<h3 data-id="heading-11">Facebook</h3>
<p>Facebook也在用，为此他们还专门在Github上建立了一个开源组织facebookgo，大家可以通过<a href="https://github.com/facebookgo%E8%AE%BF%E9%97%AE%E6%9F%A5%E7%9C%8Bfacebook%E5%BC%80%E6%BA%90%E7%9A%84%E9%A1%B9%E7%9B%AE%EF%BC%8C%E6%AF%94%E5%A6%82%E8%91%97%E5%90%8D%E7%9A%84%E6%98%AF%E5%B9%B3%E6%BB%91%E5%8D%87%E7%BA%A7%E7%9A%84grace%E3%80%82" target="_blank" rel="nofollow noopener noreferrer">github.com/facebookgo访…</a></p>
<h3 data-id="heading-12">Uber</h3>
<h3 data-id="heading-13">腾讯</h3>
<p>腾讯作为国内的大公司，还是敢于尝试的，尤其是Docker容器化这一块，他们在15年已经做了docker万台规模的实践，具体可以参考<a href="http://www.infoq.com/cn/articles/tencent-millions-scale-docker-application-practice" target="_blank" rel="nofollow noopener noreferrer">www.infoq.com/cn/articles…</a> 。</p>
<h3 data-id="heading-14">百度</h3>
<p>目前所知的百度的使用是在运维这边，是百度运维的一个BFE项目，负责前端流量的接入。他们的负责人在2016年有分享，大家可以看下这个 <a href="http://www.infoq.com/cn/presentations/application-of-golang-in-baidu-frontend" target="_blank" rel="nofollow noopener noreferrer">www.infoq.com/cn/presenta…</a> 。</p>
<p>其次就是百度的消息系统。负责公司手百消息通讯系统服务器端开发及维护。</p>
<h3 data-id="heading-15">京东</h3>
<p>京东云消息推送系统、云存储，以及京东商城等都有使用Go做开发。</p>
<h3 data-id="heading-16">小米</h3>
<p>小米对Golang的支持，莫过于运维监控系统的开源，也就是 <a href="http://open-falcon.com/" target="_blank" rel="nofollow noopener noreferrer">open-falcon.com/</a> 。</p>
<p>此外，小米互娱、小米商城、小米视频、小米生态链等团队都在使用Golang。</p>
<h3 data-id="heading-17">360</h3>
<p>360对Golang的使用也不少，一个是开源的日志搜索系统Poseidon，托管在Github上，<a href="https://github.com/Qihoo360/poseidon" target="_blank" rel="nofollow noopener noreferrer">github.com/Qihoo360/po…</a>.</p>
<p>还有360的推送团队也在使用，他们还写了篇博文在Golang的官方博客上 <a href="https://blog.golang.org/qihoo" target="_blank" rel="nofollow noopener noreferrer">blog.golang.org/qihoo</a>。</p>
<h3 data-id="heading-18">七牛云</h3>
<p>七牛云用了近50万行代码，来实现整个产品。七牛云存储产品网址：<a href="http://qiniu.com/%E3%80%82%E4%B8%8A%E7%BA%BF%E6%97%B6%E9%97%B4%EF%BC%9A2011-9-1%E3%80%82%E5%BA%94%E7%94%A8%E8%8C%83%E5%9B%B4%EF%BC%9A%E6%95%B4%E4%B8%AA%E4%BA%A7%E5%93%81%EF%BC%88%E5%8C%85%E6%8B%AC%E5%9F%BA%E7%A1%80%E6%9C%8D%E5%8A%A1%E3%80%81Web%E7%AB%AF%E3%80%81%E7%BB%9F%E8%AE%A1%E5%B9%B3%E5%8F%B0%E3%80%81%E5%90%84%E7%B1%BB%E5%B0%8F%E5%B7%A5%E5%85%B7%E7%AD%89%E7%AD%89%EF%BC%89Go%E4%BB%A3%E7%A0%81%E8%A1%8C%E6%95%B0%E5%8D%A0%E6%AF%94%EF%BC%9A99.9%25%E6%97%A5" target="_blank" rel="nofollow noopener noreferrer">qiniu.com/。上线时间：2011-…</a> PV：保密</p>
<h3 data-id="heading-19">美团</h3>
<p>美团后台流量支撑程序。应用范围：支撑主站后台流量（排序，推荐，搜索等），提供负载均衡，cache，容错，按条件分流，统计运行指标（qps，latency）等功能。</p>
<h3 data-id="heading-20">滴滴</h3>
<p>基础服务平台。</p>
<h3 data-id="heading-21">金山微看</h3>
<p>应用范围：服务接口，后台流程服务，消息系统，图片系统</p>
<h3 data-id="heading-22">搜狗</h3>
<p>搜狗推送系统。Push系统中用于维持与客户端连接的部分。</p>
<h3 data-id="heading-23">QOR – 模块化的电商系统</h3>
<ul>
<li>QOR官网: <a href="https://link.zhihu.com/?target=http%3A//getqor.com" target="_blank" rel="nofollow noopener noreferrer">QOR: E-commerce & CMS SDK written in Go</a></li>
<li>github地址: qor/qor · GitHub</li>
<li>应用范围: 整个产品</li>
</ul>
<h3 data-id="heading-24">weico</h3>
<p>产品名：weico 3.0， 服务端所有代码都是用Go实现。</p>
<h3 data-id="heading-25">仙侠道</h3>
<ul>
<li>产品网址：[仙侠道官网 – 心动游戏](仙侠道官网 – 心动游戏)</li>
<li>应用范围： 游戏服务端（通讯、逻辑、数据存储）</li>
</ul>
<h3 data-id="heading-26">快玩游戏</h3>
<ul>
<li>网址：<a href="https://www.qfgolang.com/%E5%BF%AB%E7%8E%A9%E5%B0%8F%E6%B8%B8%E6%88%8F,%E5%8D%95%E6%9C%BA%E6%B8%B8%E6%88%8F,%E7%BD%91%E9%A1%B5%E6%B8%B8%E6%88%8F,%E5%BF%AB%E7%8E%A9%E6%B8%B8%E6%88%8F,%E5%BF%AB%E7%8E%A9%E6%B8%B8%E6%88%8F%E7%9B%92" target="_blank" rel="nofollow noopener noreferrer">快玩小游戏,单机游戏,网页游戏,快玩游戏,快玩游戏盒</a></li>
<li>应用范围：实时消息系统、用户认证、用户会话、统一统计接口</li>
</ul>
<h3 data-id="heading-27">盛大云CDN</h3>
<ul>
<li>网址：盛大云计算</li>
<li>应用范围：CDN的调度系统、分发系统、监控系统、短域名服务，CDN内部开放平台、运营报表系统以及其他一些小工具等</li>
</ul>
<h3 data-id="heading-28">Bmob移动后端云服务平台</h3>
<ul>
<li>产品网址：Bmob移动后端云服务平台</li>
<li>应用范围：Restful API(使用Beego)、统计分析平台、常用服务如发邮件、队列异步处理、统计用户空间和接口请求</li>
</ul>
<h3 data-id="heading-29">群策</h3>
<ul>
<li>网址：[群策 – 统一团队沟通，高效完成工作](群策 – 统一团队沟通，高效完成工作)</li>
<li>应用范围：全系统</li>
</ul>
<h3 data-id="heading-30">BiddingX DSP广告投放系统</h3>
<ul>
<li>网址：BiddingX_专业的DSP解决方案供应商</li>
<li>应用范围：竞价投放、曝光统计、点击跳转</li>
</ul>
<h3 data-id="heading-31">街坊四邻</h3>
<ul>
<li>网址：首页 – 街坊四邻</li>
<li>应用范围：后台服务</li>
</ul>
<h3 data-id="heading-32">Leanote</h3>
<ul>
<li>网址：Leanote</li>
</ul>
<h3 data-id="heading-33">Bearychat</h3>
<ul>
<li>网址：BearyChat</li>
</ul>
<h3 data-id="heading-34">宅豆</h3>
<ul>
<li>网址：宅豆网 – 自筑最美家，宅豆随你搭</li>
</ul>
<h3 data-id="heading-35">白板- 设计图讨论工具</h3>
<ul>
<li>网址：白板</li>
</ul>
<h3 data-id="heading-36">实验楼</h3>
<ul>
<li>网址：实验楼 – 第一家以实验为核心的IT在线教育平台</li>
</ul>
<h3 data-id="heading-37">新浪微博</h3>
<p>中间件和弹性调度用 Java 和 Go 编写，微博视频转码及存储服务用 Go 编写。</p>
<h3 data-id="heading-38">爱奇艺</h3>
<p>VR 后台系统中间件，VR 端的 HTTP 接口。</p>
<h3 data-id="heading-39">猎豹移动</h3>
<p>消息推送</p>
<h3 data-id="heading-40">网易</h3>
<p>网易蜂巢容器公有云。</p>
<h3 data-id="heading-41">哔哩哔哩</h3>
<p>弹幕</p>
<h3 data-id="heading-42">巨人网络</h3>
<p>部分手机游戏的服务端。</p>
<h3 data-id="heading-43">今日头条</h3>
<p>Nsq：Nsq 是由Go语言开发的高性能、高可用消息队列系统，性能非常高，每天能处理数十亿条的消息；</p>
<p>Packer:用来生成不同平台的镜像文件，例如VM、vbox、AWS等，作者是vagrant的作者</p>
<p>Skynet：分布式调度框架</p>
<p>Doozer：分布式同步工具，类似ZooKeeper</p>
<p>Heka：mazila开源的日志处理系统</p>
<p>Cbfs：couchbase开源的分布式文件系统</p>
<p>Tsuru：开源的PAAS平台，和SAE实现的功能一模一样</p>
<p>Groupcache：memcahe作者写的用于Google下载系统的缓存系统</p>
<p>God：类似redis的缓存系统，但是支持分布式和扩展性</p>
<p>Gor：网络流量抓包和重放工具</p>
<p>还有很多，比如阿里中间件、聚美优品、高升控股、探探、斗鱼直播、人人车、亚信、Udesk、方付通、招财猫、三一集团、美餐网等。一般的选择，都是选择用于自己公司合适的产品系统来做，比如消息推送的、监控的、容器的等，Golang特别适合做网络并发的服务，这是他的强项，所以也是被优先用于这些项目。Go语言作为一门大型项目开发语言，在很多大公司相继使用，甚至完全转向Go开发。</p>
<h2 data-id="heading-44">四、写在最后</h2>
<p>当然，一个技术能不能发展起来，关键还要看三点。</p>
<ul>
<li><strong>有没有一个比较好的社区。</strong> 像 C、C++、Java、Python 和 JavaScript 的生态圈都是非常丰富和火爆的。尤其是有很多商业机构参与的社区那就更为人气爆棚了，比如 Linux 的社区。</li>
<li><strong>有没有一个工业化的标准。</strong> 像 C、C++、Java 都是有标准化组织的。尤其是 Java，其在架构上还搞出了像 J2EE 这样的企业级标准。</li>
<li><strong>有没有一个或多个杀手级应用。</strong> C、C++ 和 Java 的杀手级应用不用多说了，就算是对于 PHP 这样还不能算是一个好的编程语言来说，因为是 Linux 时代的第一个杀手级解决方案 LAMP 中的关键技术，所以，也发展起来了。</li>
</ul>
<p>上述的这三点是非常关键的，新的技术只需要占到其中一到两点就已经很不错了，何况有的技术，比如 Java，是三点全占到了，所以，Java 的发展是如此好。当然，除了上面这三点重要的，还有一些其它的影响因素，比如：</p>
<ul>
<li>**学习曲线是否低，上手是否快。**这点非常重要，C++ 在这点上越做越不好了。</li>
<li>**有没有一个不错的提高开发效率的开发框架。**如：Java 的 Spring 框架，C++ 的 STL 等。</li>
<li>**是否有一个或多个巨型的技术公司作为后盾。**如：Java 和 Linux 后面的 IBM、Sun……</li>
<li>**有没有解决软件开发中的痛点。**如：Java 解决了 C 和 C++ 的内存管理问题。</li>
</ul>
<p>用这些标尺来量一下 Go 语言，我们可以清楚地看到：</p>
<ul>
<li>Go 语言容易上手；</li>
<li>Go 语言解决了并发编程和写底层应用开发效率的痛点；</li>
<li>Go 语言有 Google 这个世界一流的技术公司在后面；</li>
<li>Go 语言的杀手级应用是 Docker，而 Docker 的生态圈在这几年完全爆棚了。</li>
</ul>
<p>所以，Go 语言的未来是不可限量的。当然，我个人觉得，Go 可能会吞食很多 C、C++、Java 的项目。不过，Go 语言所吞食主要的项目应该是中间层的项目，既不是非常底层也不会是业务层。</p>
<blockquote>
<p>也就是说，Go 语言不会吞食底层到 C 和 C++ 那个级别的，也不会吞食到高层如 Java 业务层的项目。Go 语言能吞食的一定是 PaaS 上的项目，比如一些消息缓存中间件、服务发现、服务代理、控制系统、Agent、日志收集等等，没有复杂的业务场景，也到不了特别底层（如操作系统）的中间平台层的软件项目或工具。而 C 和 C++ 会被打到更底层，Java 会被打到更上层的业务层。</p>
</blockquote>
<p>好了，我们再用上面的标尺来量一下 Go 语言的杀手级应用 Docker，你会发现基本是一样的。</p>
<ul>
<li>Docker 上手很容易。</li>
<li>Docker 解决了运维中的环境问题以及服务调度的痛点。</li>
<li>Docker 的生态圈中有大公司在后面助力。比如 Google。</li>
<li>Docker 产出了工业界标准 OCI。</li>
<li>Docker 的社区和生态圈已经出现像 Java 和 Linux 那样的态势。</li>
<li>……</li>
</ul>
<p>所以，虽然几年前的 Docker ，当时的坑儿还很多，但是，相对于这些大的因素来说，那些小坑儿都不是问题。只是需要一些时间，这些小坑儿在未来 5-10 年就可以完全被填平了。</p>
<p>同样，我们可以看到 Kubernetes 作为服务和容器调度的关键技术一定会是最后的赢家。</p>
<p>最后，我还要说一下，为什么要早一点地进入这些新技术，而不是等待这些技术成熟了后再进入。原因有这么几个。</p>
<p>技术的发展过程非常重要。因为你可以清楚地看到了这种新技术的生态圈发展过程。让我们收获最大的并不是这些技术本身，而是一个技术的变迁和行业的发展。</p>
<p>从中，我们看到了非常具体的各种思潮和思路，这些东西比起 技术本身来说更有价值。因为，这不但让我们重新思考已经掌握的技术以及如何更好地解决已有的问题，而且还让我看到了未来。不但有了技术优势，而且这些知识还让我们的技术生涯多了很多的可能性。</p>
<p>这些关键新技术，可以让你拿到技术的先机。这些对一个需要技术领导力的个人或公司来说都是非常重要的。</p>
<p>一个公司或是个人能够占有技术先机，就会比其它公司或个人有更大的影响力。一旦未来行业需求引爆，那么这个公司或是个人的影响力就会形成一个比较大的护城河，并可以快速地产生经济利益。</p>
<p>Go的应用范围一直在扩大，云计算，微服务，区块链，哪里都有用Go写的重量级项目。docker/kubernetes生态圈，几百/千万行代码，基本统治了云原生应用市场。去年大热的区块链，以太坊的geth，比特币的btcd，闪电网络的lnd，都是Go语言开发。还是那句话，多看看各种语言的生态，或许都并没有你想象的那么不堪。。。Go语言设计上确实不够“先进”，但也是另一种“务实”。其实go不管在国内还是国外已经很受待见了，国外google用的很多，uber也在用，国内有著名的今日头条，每日千亿级的访问妥妥的。多少语言终其一生都没有这么大的应用场景。</p></div>  
</div>
            