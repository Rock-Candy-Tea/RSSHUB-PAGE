
---
title: '深入浅出讲解MSE Nacos 2.0新特性'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://intranetproxy.alipay.com/skylark/lark/0/2021/png/53357/1625132946000-f0903d26-5672-4ebc-9f98-667fe450659b.png'
author: 掘金
comments: false
date: Tue, 06 Jul 2021 23:39:08 GMT
thumbnail: 'https://intranetproxy.alipay.com/skylark/lark/0/2021/png/53357/1625132946000-f0903d26-5672-4ebc-9f98-667fe450659b.png'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>简介：</strong> 随着云原生时代的到来，微服务已经成为应用架构的主流，Nacos也凭借简单易用、稳定可靠、性能卓越的核心竞争力成为国内微服务领域首选的注册中心和配置中心；Nacos2.0更是把性能做到极致，让业务快速发展的用户再也不用担心性能问题；同时阿里云MSE也提供Nacos2.0托管服务，一键开通享受阿里十年沉淀微服务所有能力！</p>
<p>作者|风卿</p>
<h3 data-id="heading-0">前言</h3>
<p>MSE从2020年1月发布Nacos1.1.3版本引擎，支持在公有云环境全托管的方式使用Nacos作为注册中心。2020年7月发布Nacos1.2.1版本支持元配置数据管理，支持微服务应用在运行时动态修改配置信息和路由规则等。随着用户的深入使用，Nacos1.X版本的性能问题也渐渐暴露出来。通过对1.X版本的内核改造，Nacos2.0专业版性能提升10倍，基本能满足用户对微服务场景的性能要求。</p>
<p><img src="https://intranetproxy.alipay.com/skylark/lark/0/2021/png/53357/1625132946000-f0903d26-5672-4ebc-9f98-667fe450659b.png" alt="image" title="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>除了性能的提升，专业版具有更高的SLA保障，并且在配置数据上具有更高的安全性，同时通过MCP协议与Istio生态打通，作为Istio的注册中心。</p>
<h3 data-id="heading-1">MSE Nacos1.X基础版架构</h3>
<p>整体1.X架构可以粗略分为五层，分别是接入层、通信层、功能层、同步层和持久化层。</p>
<ul>
<li>用户通过接入层访问Nacos，比如SDK、SCA、Dubbo、Console，Nacos也提供了HTTP协议的open API访问方式。</li>
<li>通信层包含HTTP和UDP，Nacos主要通过HTTP进行通信，少部分服务推送功能会用到UDP。</li>
<li>功能层目前有Naming和Config两大部分，分别提供服务发现和配置管理能力。</li>
<li>同步层包含AP模式的Distro协议（服务注册）和CP模式的Raft协议（服务元信息），以及配置通知的Notify同步方式</li>
<li>Nacos的数据持久化有用到Mysql、Derby和本地文件，配置数据、用户信息、权限数据存储在Mysql或者Derby中，持久化的服务数据则存放在本地文件</li>
</ul>
<p><img src="https://intranetproxy.alipay.com/skylark/lark/0/2021/png/53357/1625139267211-d4a0544f-51a6-4a23-83d3-7cda978237c7.png?x-oss-process=image%2Fresize%2Cw_2222" alt="image" title="image" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">MSE Nacos1.X基础版架构问题</h3>
<p>目前1.X的架构存在几个问题：</p>
<ul>
<li>每个服务实例都通过心跳续约，在Dubbo场景每个接口对应一个服务，当Dubbo的应用接口数较多时需要心跳续约TPS会很高。</li>
<li>心跳续约感知时延长，需要达到续约超时时间才能删除实例，一般需要15S，时效性较差</li>
<li>通过UDP推送变更数据不可靠，需要客户端定时进行数据全量对账保证数据的正确性，大量无效查询，整体服务的QPS很高</li>
<li>通信方式基于HTTP短链接的方式，Nacos侧释放连接会进入TIME_WAIT状态，当QPS较高时会有连接耗尽导致报错的风险，当然这里通过SDK引入HTTP连接池能缓解，但不能根治</li>
<li>配置的长轮询方式会导致相关数据进入JVM Old区申请和释放内存，引起频繁的CMS GC</li>
</ul>
<p><img src="https://intranetproxy.alipay.com/skylark/lark/0/2021/png/53357/1625128546805-f77c5486-d1b9-4649-b599-63d596cac3ca.png?x-oss-process=image%2Fresize%2Cw_2222" alt="image" title="image" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">MSE Nacos2.0专业版架构及新模型</h3>
<p>1.X架构的问题核心点在于连接模型上，2.0架构升级为长连接模型，在通信层通过gRPC和RSocket实现长连接数据传输和推送能力，在连接层新增加请求处理器、流控和负载均衡等功能</p>
<p><img src="https://intranetproxy.alipay.com/skylark/lark/0/2021/png/53357/1625127600000-7a3d3513-009f-44ef-a845-4d998aade86d.png?x-oss-process=image%2Fresize%2Cw_2222" alt="image" title="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>2.0架构解决的问题：</p>
<ul>
<li>
<p>应用POD按照长连接维度进行心跳续约，不需要按照实例级，大大降低重复请求</p>
</li>
<li>
<p>长连接断开时可以快速感知到，不用等待续约超时时长就可以移除实例</p>
</li>
<li>
<p>NIO流式推送机制相对于UDP更可靠，并且可以降低应用对账数据频率</p>
</li>
<li>
<p>没有连接反复创建的开销，大幅降低TIME_WAIT连接多问题</p>
</li>
<li>
<p>长连接也解决了配置模块长轮询CMS GC问题</p>
</li>
</ul>
<p>2.0架构带来的问题：</p>
<ul>
<li>相对于Tomcat HTTP短连接模型，长连接模型需要自己管理连接状态，增加了复杂性</li>
<li>长连接gRPC基于HTTP2.0 Stream，相对于HTTP的open API可观测性和易用性降低了</li>
</ul>
<p><img src="https://intranetproxy.alipay.com/skylark/lark/0/2021/png/53357/1625139218793-fe02ea1c-4d74-4d8a-a0ee-507de9f81dcf.png?x-oss-process=image%2Fresize%2Cw_2222" alt="image" title="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>2.0架构整体来说降低了资源开销，提高了系统吞吐量，在性能上有大幅提升，但同时也增加了复杂度</p>
<h3 data-id="heading-4">MSE Nacos2.0专业版性能</h3>
<p>Nacos分为服务发现模块和配置管理模块，这里先对服务发现场景进行性能测试。</p>
<p>使用200台施压机，每个施压机模拟500个客户端，每个客户端注册5个服务，订阅5个服务，最高可以提供10W个长连接、50W个服务实例和订阅者压测场景</p>
<p><img src="https://intranetproxy.alipay.com/skylark/lark/0/2021/png/53357/1625127802765-b56e1685-d00a-4909-ae0d-e6ed4ee84511.png" alt="image" title="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>服务发现压测主要压变更态和稳定态两种场景：</p>
<ul>
<li>变更态：施压机施压阶段会大量连接Nacos注册和订阅服务，这个阶段服务端的压力相对会比较大，需要看整体注册和订阅是否最终完全成功。</li>
<li>稳定态：当施压机请求都成功之后就会进入稳定状态，客户端和服务端之间只需要维持长连接心跳即可，这个阶段服务端的压力会比较小。如果在变更态服务端的压力过大会发生请求超时、连接断开等问题，不能进入稳定态</li>
</ul>
<p>服务发现也会在MSE上对低版本做升级，对比升级前后的性能变化曲线，这样的性能对比更直观</p>
<p>配置管理模块在实际使用中是写少读多的场景，主要瓶颈点在单台机器性能上，压测场景主要基于单台机器的读性能和连接支撑数<br>
使用200台施压机，每台施压机可以模拟200个客户端，每个客户端订阅200个配置，发起配置订阅和读配置请求</p>
<p><img src="https://intranetproxy.alipay.com/skylark/lark/0/2021/png/53357/1625127741463-b364e9a2-c65b-4b9c-8e91-eca8d81e5a7a.png?x-oss-process=image%2Fresize%2Cw_2222" alt="image" title="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在服务发现场景对比基础版和专业版在2C4G、4C8G和8C16G规格下的性能数据情况。</p>
<p>这里最大的TPS和实例数都是服务能保证高可用稳定运行的数据，大概会是最大值的一半或者三分之二，也就是说挂一台机器也可以正常运行。</p>
<p><img src="https://intranetproxy.alipay.com/skylark/lark/0/2021/png/53357/1625133082664-497e25a3-c808-43cd-be70-f335687eea11.png" alt="image" title="image" loading="lazy" referrerpolicy="no-referrer"> 稳定运行时支持规模提升7倍，实际上最大支持规模提升7-10倍</p>
<p>还有一个场景是对3节点2C4G MSE Nacos升级前后的对比，主要分为三个阶段：</p>
<ul>
<li>第一个阶段客户端使用1.X版本，MSE Nacos使用基础版，实例数从0->6000->10000，最后到14000最大值无法继续增大，Server CPU达到80-90%，客户端不断报错，接着降低实例数到6000</li>
<li>第二阶段升级MSE Nacos基础版到专业版，实例数到达14000无法继续增大，性能压测性能曲线差异不大</li>
<li>第三阶段在保持实例数为14000的状态下，分批升级客户端到2.0版本，CPU指标曲线不断下降至20%左右，并且整体处于稳定态无报错</li>
</ul>
<p><img src="https://intranetproxy.alipay.com/skylark/lark/0/2021/png/53357/1625127863381-6f0be422-1e30-438b-a48e-8dc7057bd993.png" alt="image" title="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>从升级前后的性能曲线感受MSE Nacos2.0专业版性能有提升较大。最后整体的压测情况，相较于基础版，专业版服务发现性能提升10倍，配置管理提升7倍</p>
<p><img src="https://intranetproxy.alipay.com/skylark/lark/0/2021/png/53357/1625127959457-933b7a61-f5c6-4757-8fad-a10c1fe416bb.png" alt="image" title="image" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">MSE Nacos平滑升级专业版</h3>
<p>对于新用户可以直接创建专业版实例，老用户则可以通过MSE"实例变更"一键升级。MSE会在后台对POD升级，由于V1V2数据结构不一样，在一开始的时候Nacos数据默认是双写的，在升级过程中数据会从V1同步到V2，升级完成后数据会从V2同步V1，最后MSE会关闭双写逻辑，整体流程都是自动。</p>
<p><img src="https://intranetproxy.alipay.com/skylark/lark/0/2021/png/53357/1625138814236-c2c8e9a8-8c5d-4a65-ab10-8829e68abc14.png" alt="image" title="image" loading="lazy" referrerpolicy="no-referrer"> SLB的服务端口最后也会增加GRPC 9848端口，此时应用SDK可以从1.X版本升级到2.0版本，整体客户端服务端升级到2.0架构</p>
<p><img src="https://intranetproxy.alipay.com/skylark/lark/0/2021/png/53357/1625128163262-26552ec3-c290-44a0-b772-89f7f8caa711.png" alt="image" title="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>版本之间的兼容性情况，整体的兼容原则是高版本的服务端兼容低版本客户端，但是高版本客户端不一定能访问低版本服务端：</p>
<ul>
<li>1.X客户端可以访问基础版，也可以访问专业版</li>
<li>2.0客户端可以访问专业版，但是不能访问基础版</li>
</ul>
<p><img src="https://intranetproxy.alipay.com/skylark/lark/0/2021/png/53357/1625133014847-add54948-2fec-40fa-bc3f-b06d6288c924.png" alt="image" title="image" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">Nacos配置安全管理</h3>
<p>上一期岛风同学讲解了配置权限控制，整体MSE Nacos通过阿里云RAM主子账号体系来做权限控制，这期我主要讲一下Nacos的配置加密功能。</p>
<p>用户在使用配置数据时可能会将用户信息、数据库密码等敏感信息存放到Nacos中，而Nacos存储配置数据都是明文传输、明文存储的，在数据库内容泄漏或者传输层抓包时会导致敏感配置数据项泄漏，整体安全风险非常高。</p>
<p><img src="https://intranetproxy.alipay.com/skylark/lark/0/2021/png/53357/1625128189522-0d10a43f-5179-4e35-8f89-d165f32cbd52.png" alt="image" title="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>常用的HTTPS协议能解决传输安全，但解决不了存储安全，这里直接在客户端进行加密，这样在传输和存储的过程中数据都是加密的。</p>
<p>这里使用第三方加密系统（如阿里云KMS）加强加密的安全性，为了加密速度快使用对称加密（AES算法），由于密钥要随着密文传输，同时对密钥进行加密，整体采用二级加密的方式。</p>
<p><img src="https://intranetproxy.alipay.com/skylark/lark/0/2021/png/53357/1625480587887-fc0878e2-e502-40a5-8555-040459ee127e.png" alt="image" title="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>SDK在发布数据时会先从KMS中拿到密钥和加密后的密钥，然后使用密钥对数据进行加密，接着将加密数据和加密后的密钥传输到Nacos存储。SDK会从Nacos获取加密数据和加密后的密钥，然后通过加密后的密钥从KMS获取明文密钥，接着通过明文密钥对加密数据进行解密获取明文数据，解决了整体传输和存储中的数据安全问题。</p>
<p>为了兼容老逻辑，并且只有敏感数据需要加密，Nacos只对固定前缀DataId的数据进行加密，并且在开源侧通过SPI插件化实现，让用户自己能扩展</p>
<p>用户可以通过SDK和MSE控制台对敏感数据进行加解密，整体SDK和MSE控制台都会先访问KMS再加密存储配置数据，然后解密之后再展示明文，使用流程和之前明文存储一致</p>
<p><img src="https://intranetproxy.alipay.com/skylark/lark/0/2021/png/53357/1625480623839-d67b7d67-bab2-4fd8-b8a0-c5c0f2b71a20.png" alt="image" title="image" loading="lazy" referrerpolicy="no-referrer"></p>
<p>用户使用SDK接入开启加解密功能需要SDK在1.4.2版本及以上，同时需要引入MSE内部实现的nacos-client-mse-extension加解密插件。</p>
<p>com.alibaba.nacos</p>
<p>nacos-client</p>
<p>1.4.2</p>
<p>com.alibaba.nacos</p>
<p>nacos-client-mse-extension</p>
<p>1.0.1</p>
<p>初始化SDK时需要填入子账号AK/SK，并授权KMS加解密权限，具体细节可以参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fhelp.aliyun.com%2Fdocument_detail%2F254762.html%3Fspm%3Da2c4g.11186623.6.613.177a3a5fnWqzEJ" target="_blank" rel="nofollow noopener noreferrer" title="https://help.aliyun.com/document_detail/254762.html?spm=a2c4g.11186623.6.613.177a3a5fnWqzEJ" ref="nofollow noopener noreferrer">创建和使用配置加密</a></p>
<p>Properties properties = new Properties();</p>
<p>properties.put("serverAddr", "mse-xxxxxx-p.nacos-ans.mse.aliyuncs.com");</p>
<p>properties.put("accessKey", "xxxxxxxxxxxxxx");</p>
<p>properties.put("secretKey", "xxxxxxxxxxxxxx");</p>
<p>properties.put("keyId", "alias/acs/mse");</p>
<p>properties.put("regionId", "cn-hangzhou");</p>
<p>ConfigService configService = NacosFactory.createConfigService(properties);</p>
<p>String content = configService.getConfig("cipher-kms-aes-256-dataid", "group", 6000);</p>
<h3 data-id="heading-7">总结</h3>
<p>MSE Nacos2.0专业版相较于基础版在性能、可用性和安全性上都有较大提升，基础版建议用于测试环境，对于生产环境建议使用专业版。对于用户身份、密码等配置敏感信息建议都开启权限控制能力并且加密保存加强数据安全。</p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fclick.aliyun.com%2Fm%2F1000282372%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://click.aliyun.com/m/1000282372/" ref="nofollow noopener noreferrer">原文链接</a></p>
<p>本文为阿里云原创内容，未经允许不得转载。</p></div>  
</div>
            