
---
title: 'Nacos 2.1.0 发布，支持鉴权及加解密插件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9704'
author: 开源中国
comments: false
date: Tue, 10 May 2022 12:34:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9704'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Nacos 2.1.0<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnacos.io%2Fzh-cn%2Fblog%2F2.1.0-release.html" target="_blank"> 已正式发布</a>。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">新版本内容</h3> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">2.1.0版本主要增加了认证插件和配置加密插件能力。 并关闭默认支持服务端从 1.X 版本升级的能力，若需要使用平滑升级能力，需要在配置文件中开启此功能。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">对于客户端，此版本重构了类扫描逻辑并删除了 org.reflections 依赖，以解决 org.reflections 冲突时的不兼容问题。 最后，这个版本做了一些控制台优化并修复了 2.0.4 中发现的一些问题。 详细变更日志如下：</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code>## Features

[#5695] Add a plugin SPI for configuration encryption and decryption for Nacos 2.0
[#5696] Add a plugin SPI for authentication for Nacos 2.0.
[#7930] Default close support upgrade from 1.X feature.
[#7992] Support cluster grpc client to set thread pool size.
[#8220] Add reset raft cluster operation.

## Enhancement & Refactor

[#7487] Add generics for the CacheBuilder.
[#7879] Refactor destroy method of AbstractMemberLookup.
[#7924][#8214] Add ldap auth plugin.
[#7952] Ignore read request for raft follower's state machine to enhance raft stability.
[#7966] Add more information in Auth/Distro/Curcuit-Filter when cause some server error.
[#7971] Stop version judge Task and release thread after upgrade completely.
[#8072] Enhance memory cost in DistroProtocol initialization.
[#8107] Enhance console change password operation.
[#8156] Support js and css of console auto-upgrade. 


## BugFix

[#1717][#7359] Fix XSS vulnerabilities.
[#6273] Fix loop request for offline server nodes API.
[#6999] Fix Nacos client does not support logback overload log configuration.
[#7757] Fix jraft read request deserialize to write request problem. 
[#7780] Fix config a-b-a problem.
[#7941] Fix version comparison error in Config Detail page.
[#8087] Fix text out of box in configuration manager.
[#8108] Fix throw NPR for health check for v2.
[#8050] Fix configuration about Distro changes could not take effect.
[#8161] Fix console can't use relative path problem.
[#8163] Fix multi-instance share the same local snapshot.
[#8196] Fix subscriber api without count when the query number is more than subscriber count.

## Dependency

[#7758] Update module nacos-consistency protobuf-maven-plugin version to 0.6.1.
[#7886] Enhance package scan logic and remove org.reflections dependency.

## Tests

[#4981] Add much unit test.
[#8009] Fix NPE of unit test. 
</code></pre> 
<h3 style="margin-left:0; margin-right:0; text-align:start">插件化</h3> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">支持插件化是2.1.0版本的主要改动之一。Nacos通过<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.oracle.com%2Fjavase%2Ftutorial%2Fsound%2FSPI-intro.html" target="_blank">SPI</a><span> </span>的方式，允许用户和开发者实现自己的对应功能插件使用；目前Nacos已经支持鉴权和加解密的插件化能力。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:start">鉴权</h4> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">自从Nacos 1.2 版本加入鉴权功能后，社区对鉴权功能的讨论一直持续。原因是Nacos目前的鉴权系统设计为防止错用及用户隔离。但社区中对鉴权能力的要求不局限于此，为了满足不同的用户对鉴权程度的不同要求。Nacos社区希望设计一套用于鉴权的API，并将其注入到网络请求的流程中。 Nacos目前的鉴权实现也已经重构成默认的鉴权插件，社区所贡献的LADP也已改造完成，使用方式和以前一致；如果需要开发自定义的鉴权插件，可以参考文档<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnacos.io%2Fzh-cn%2Fdocs%2Fauth-plugin.html" target="_blank">鉴权插件</a>实现。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:start">加解密</h4> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">在Nacos社区中，许多用户关注配置中某些敏感信息的安全性问题。除了通过鉴权，社区也希望能对配置内容中的敏感信息进行加密。由于用户和开发者所使用或对接的算法和加解密系统可能不同，因此Nacos社区设计了一套用于加解密的API，并将其注入到发布和查询配置的工作流程中。 更多加解密插件的细节可以参考文档<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnacos.io%2Fzh-cn%2Fdocs%2Fconfig-encryption.html" target="_blank">配置加密插件</a>。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">默认关闭兼容1.X服务端升级</h3> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">默认关闭支持服务端从 1.X 版本升级的能力是Nacos2.1.0版本的另一个重要改动。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">在2.0.X版本中，数据结构进行了一些重新设计，导致和1.X的数据无法直接兼容，为了方便社区用户从1.X平滑升级到Nacos2.0版本，Nacos2.0版本除了兼容1.X的openAPI外，还新增了双写数据等逻辑；但这部分逻辑对系统资源有较大的损耗，并且由于机制较为复杂，导致部分直接使用2.0版本的用户可能会遇到一些版本切换的疑问。因此在Nacos2.1版本中，我们默认关闭了兼容1.X服务端平滑升级能功能，关闭该功能后直接部署2.1版本将不会再从1.X模式进行检测和升级，而是直接运行在2.X的数据模式下，同时也支持2.0版本直接升级2.1版本。</p> 
<p style="color:#24292e; margin-left:0; margin-right:0; text-align:start">若是希望从Nacos1.X直接升级到Nacos2.1.0版本，则需要在application.properties文件中设置配置<code>nacos.core.support.upgrade.from.1x=true</code>，此时Nacos2.1版本会和Nacos2.0版本一样，以1.X的数据模式启动，并开始自动升级检测，待全集群数据一致，且准备完毕后，切换至2.0数据模式，更多升级相关的内容，请参考文档<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnacos.io%2Fzh-cn%2Fdocs%2F2.0.0-upgrading.html" target="_blank">升级文档</a>。</p> 
<p>发布公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnacos.io%2Fzh-cn%2Fblog%2F2.1.0-release.html" target="_blank">https://nacos.io/zh-cn/blog/2.1.0-release.html</a><br> Release：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fnacos%2Freleases%2Ftag%2F2.1.0" target="_blank">https://github.com/alibaba/nacos/releases/tag/2.1.0</a></p>
                                        </div>
                                      
</div>
            