
---
title: '从安全的角度谈谈etcd'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210630/d2daf78e11b6016a49271b01206026c9.png'
author: Dockone
comments: false
date: 2021-07-03 11:05:52
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210630/d2daf78e11b6016a49271b01206026c9.png'
---

<div>   
<br><h3>背景</h3>随着CoreOS 、Kubernetes 、CoreDNS、Vulcand等项目在开源社区日益火热，它们所用到KV存储中间件etcd，渐渐为开发人员所关注，etcd采用Go语言开发，作为一个高可用强一致性的服务发现存储仓库，深受Gopher的喜爱。越来越多的团队使用etcd进行配置管理以及服务发现，随之而来的是安全问题，etcd中敏感配置信息，如数据库密码、PrivateKey、SecretKey、Kubernetes集群数据等，如果被攻击者窃取会造成严重影响。<br>
<br>本篇文章起源于一次公司内网渗透，探测到某部门的服务器开启了etcd服务，使用etcd作为应用的配置中心，随即利用etcd配置不当的未授权安全问题，获取到库中某关系数据库地址、帐号密码，进而入侵到该关系型数据库。为什么安全漏洞、安全事件频出由此足见端倪，一小部分的开发或者运维同学，还停留在“能用”的想法，只关注可用、可运维，并没有进一步了解其安全问题，甚至官方文档中安全部分的介绍可能也都是跳过。本篇文章前半部分会以“安全开发”的视角，详细描述etcd的安全实践。后半部分会切换到“安全工程师”的视角，探究etcd安全风险检测。<br><br>
<h3>etcd简介</h3>etcd诞生于CoreOS公司，它最初是用于解决集群管理系统中OS升级的分布式并发控制以及配置文件的存储与分发等问题。基于此，etcd被设计为提供高可用、强一致的小型key value数据存储服务。项目当前隶属于CNCF基金会，被AWS、Google、Microsoft、Alibaba等大型互联网公司广泛使用。<br>
<br>etcd项目地址：<a href="https://github.com/etcd-io/etcd" rel="nofollow" target="_blank">https://github.com/etcd-io/etcd</a><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210630/d2daf78e11b6016a49271b01206026c9.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210630/d2daf78e11b6016a49271b01206026c9.png" class="img-polaroid" title="1.png" alt="1.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图1 etcd架构解析</em><br>
<br>项目历程：<br>
<br>2015年2月份，etcd发布了第一个正式的稳定版本2.0。在2.0版本中，etcd重新设计了Raft一致性算法，并为用户提供了一个简单的树形数据视图，在2.0版本中etcd支持每秒超过1000次的写入性能，满足了当时绝大多数的应用场景需求。2.0版本发布之后，经过不断的迭代与改进，其原有的数据存储方案逐渐成为了新时期的性能瓶颈，之后etcd启动了v3版本的方案设计。<br>
<br>2017年1月份的时候，etcd发布了3.1版本，v3版本方案基本上标志着etcd技术上全面成熟。在v3版本中etcd提供了一套全新的API，重新实现了更高效的一致性读取方法，并且提供了一个gRPC的proxy用于扩展etcd的读取性能。同时，在v3版本的方案中包含了大量的GC优化，在性能优化方面取得了长足的进步，在该版本中etcd可以支持每秒超过10000次的写入。<br>
<br>2018年，CNCF基金会下的众多项目都使用了etcd作为其核心的数据存储。据不完全统计，使用etcd的项目超过了30个，在同年11月份，etcd项目自身也成为了CNCF旗下的孵化项目。进入CNCF基金会后，etcd拥有了超过400个贡献组，其中包含了来自AWS、Google、Alibaba等8个公司的9个项目维护者。<br>
<br>2019年，发布的3.4版本，由Google、Alibaba等公司联合打造，将进一步改进etcd的性能及稳定性，以满足在超大型公司使用中苛刻的场景要求。<br>
<br>2020年，专为云原生软件构建可持续生态系统的云原生计算基金会（CNCF）宣布，etcd项目正式毕业。云原生计算基金会CTO Chris Aniszczyk表示，“etcd项目是Kubernetes内部的一大关键组件，目前有多种其他项目依赖于etcd进行可靠的分布式数据存储。etcd不断扩大的项目规模、以及在最近安全审计当中带来的成熟表现，都给我们留下了深刻的印象。我们期待etcd及其社区在毕业后能够迎来更迅猛的发展。”<br>
<br>在简单了解etcd发展历程后，我们开始进入正题，以安全开发视角浅谈etcd安全实践。<br>
<h3>安全开发视角</h3>某日RKO项目组开发负责人z工，评估需要在项目中使用分布式的KV存储中间件-etcd，以满足业务发展需求，由于涉及到存储敏感数据，需要先充分了解etcd安全性。开发负责人将该任务交代给了安全开发小y，随即小y开始了对etcd安全方面的了解学习。<br><br>
<h4>etcd安全实践</h4><strong>第一步：选择较安全的中间件</strong>  <br>
<br>小y作为一名安全开发，在选择开源项目时，首先要了解有没有安全层面的设计，如果从文档到代码都看不到安全设计那就要慎用了（在采用新的开源项目、中间件时，不妨先联系公司信息安全部门，沟通下安全问题）。根据etcd官方资料，有部分篇幅是介绍其安全性及安全配置的。<br>
<br>具备的安全特性有以下几点：<br>
<ul><li>认证，身份验证，可以配置用户名密码认证、证书认证</li><li>基于角色的访问控制，每一种角色对应一组相应的权限。一旦用户被分配了适当的角色后，该用户就拥有此角色的所有操作权限。权限可细化到指定路径，可给角色授权只读、只写、可读写权限</li><li>传输安全，保障数据在传输过程中的安全，不被劫持，嗅探</li><li>存储加密，默认没有存储加密，但官方文档中也提供了存储加密的思路</li></ul><br>
<br>官方文档反应了etcd是一个相对重视安全的项目，不会因为安全原因被pass掉。<br>
<br><strong>第二步：选择安全版本</strong><br>
<br>即使etcd有很多安全层面的设计，也不代表etcd所有版本都是安全的，在确认好使用etcd后，我们来选择etcd的安全版本。从etcd的发展历程中，可以看到etcd存在两个大版本v2、v3，其中v3版本对性能及稳定性进行了大量的优化，v3这个大版本中又有很多小版本，作为使用者，如何选择较安全的etcd版本？我们不妨探究下。<br>
<br>etcd是在CNCF刚毕业的项目，作为CNCF的项目，安全是其必不可少的属性，可以在CNCF博客中看到毕业前有对etcd v3.4版本进行安全审计，审计团队是第三方安全团队Trail of Bits，安全审计内容：审计是由手动和自动审查混合执行的，自动评审包括运行各种静态分析工具，如errcheck、ineffassign和go-sec、google/gofuzz和dvyukov/go-fuzz测试工具是为了测试etcd提前写日志（Write Ahead Log，WAL）实现。结果随后被审查和必要的分流。手工审查的重点是熟悉etcd在各个领域的实施细节，如配置选项、默认设置、服务发现、WAL操作、Raft共识和领导选举、代理和网关。评估的各种安全领域包括数据验证、访问控制、加密、日志记录、身份验证、数据公开、拒绝服务和配置。<br>
<br>在去年8月份etcd开源项目中就上传了该次安全审计报告，审计报告地址：<a href="https://github.com/etcd-io/etcd/blob/master/security/SECURITY_AUDIT.pdf" rel="nofollow" target="_blank">https://github.com/etcd-io/etc ... T.pdf</a>，报告中的安全问题也录入到了GitHub项目中的安全公告中：<a href="https://github.com/etcd-io/etcd/security/advisories?page=1" rel="nofollow" target="_blank">https://github.com/etcd-io/etc ... e%3D1</a>。这份报告安全审计出etcd存在17处安全问题（见图2），仅存在一处高危风险：“etcd网关，可以将自身包含为端点，从而导致资源耗尽”，该漏洞利用难度较高，需要劫持DNS达到最终拒绝服务的目的。从报告结果可以看出，总体etcd的安全性还是可以的，仅有非默认开启的etcd网关存在一处高危漏洞，作为开发运维人员，建议使用修复了这些漏洞的v3.3.23、v3.4.10及以上版本。<br>
<br><strong>PS</strong>：信息系统没有绝对的安全，在项目发展的过程中，etcd仍然可能被爆出安全漏洞，请务必关注etcd官方的安全公告。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210630/40dbdd004f13b1262cea67b14c88255d.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210630/40dbdd004f13b1262cea67b14c88255d.jpg" class="img-polaroid" title="2.jpg" alt="2.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图2 安全审计报告中的17个安全风险</em><br>
<br><strong>第三步：安全配置</strong><br>
<br>至此小y评估下来etcd是重视安全的项目，并选择了一个安全版本。那么是不是选择了较为安全的版本就完全解决了安全问题呢？回顾安全审计报告，如图3在报告中提出etcd密码强度不足的问题，允许用户使用短密码、弱密码、不安全的密码，如：密码为1，对比修复的代码：<a href="https://github.com/etcd-io/etcd/compare/v3.3.22...v3.3.23" rel="nofollow" target="_blank">https://github.com/etcd-io/etc ... .3.23</a>，发现仅是增加了安全提醒（见图4），请注意，默认情况下，etcd不会在传输层中启用[基于RBAC的身份验证] [auth]或[身份验证功能]，以减少用户入门数据库的麻烦。此外，对于自2013年以来建立的项目而言，更改此默认设置将是一项重大更改。未启用安全功能的etcd群集可以将其数据公开给任何客户端。如果没有注意到这一点，那么etcd数据将会裸奔在内网或互联网中，这体现出安全配置的重要性，在使用的项目本身不存在安全漏洞时，如何正确的安全配置成为非常重要的环节。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210630/0c9885be892da77349a82478fb78d349.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210630/0c9885be892da77349a82478fb78d349.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图3 安全审计报告中提出密码没有长度限制</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210630/26c787b15a5e710441adc5b90a0b1a20.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210630/26c787b15a5e710441adc5b90a0b1a20.jpg" class="img-polaroid" title="4.jpg" alt="4.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图4 仅更改了安全提醒</em><br>
<br>安全配置以etcd v3举例，etcd v3在性能、安全性等方面均有提升。这里简单分享在etcd v2遇到的一个坑，即使在etcd v2版本中开启认证后，guest角色如果未进行限制，仍能以读写权限操作存储的数据。<br>
<pre class="prettyprint">//默认按照etcd启动后，是没有认证的<br>
$./etcd<br>
<br>
//查询角色列表，只有root角色<br>
$ etcdctl role list<br>
root<br>
<br>
//开启认证<br>
$ etcdctl auth enable<br>
<br>
//展示角色列表,注意开启认证后多出一个guest角色<br>
$ etcdctl --username root:********* role list<br>
guest<br>
root<br>
<br>
//开启认证后，匿名访问 http://127.0.0.1:2379/v2/keys/ 仍能访问配置数据<br>
$ curl http://127.0.0.1:2379/v2/keys/<br>
&#123;"action":"get","node":&#123;"dir":true,"nodes":[&#123;"key":"/test","value":"test123","modifiedIndex":11,"createdIndex":11&#125;]&#125;&#125;<br>
<br>
//原因在于guest角色拥有所有目录的读写权限<br>
$ etcdctl -u root:*********  role get guest<br>
Role: guest<br>
KV Read:<br>
/*<br>
KV Write:<br>
/*<br>
<br>
//官方文档不建议直接删除gust角色，建议限制guest角色的读写权限<br>
$ curl http://127.0.0.1:2379/v2/keys/<br>
&#123;"errorCode":110,"message":"The request requires user authentication","cause":"Insufficient credentials","index":0&#125; <br>
</pre><br>
1、开启认证<br>
<br>默认安装好etcd后，无论v3还是v2版本都没有开启认证，任意客户端都可以操作数据库中的数据。需要注意etcd即使没开放在外网，也同样需要开启认证，内网并不是绝对安全的，尤其是etcd这类中间件中可能存储了k8s adm token等重要凭证。所以安全配置第一步是开启etcd认证，认证的方式有基于帐号密码认证和证书认证，这里先讲下帐号密码认证（证书认证下面会提及）。<br>
<br>开启帐号密码认证：<br>
<pre class="prettyprint">$ etcdctl user add root  #添加root用户，注意设置一个强密码<br>
<br>
$ etcdctl auth enable  #开启认证<br>
<br>
$ etcdctl --user="root:*********" role list<br>
root<br>
<br>
$ etcdctl --user="root:*********" user list<br>
root<br>
<br>
$ etcdctl get /test test123<br>
Error: etcdserver: user name is empty<br>
<br>
$ etcdctl --user="root:*********" get /test test123  #确认认证是有效的<br>
/test<br>
test123<br>
</pre><br>
小y在实践过程中学习到了etcd安全认证逻辑，etcdv3中的帐号密码认证使用Go的 bcrypt包，相对v2优化了认证逻辑，不会每个请求都做认证，代替的是每次连接进行认证 , 即发起一次认证请求通过帐号密码获取到token，然后再使用token向etcd服务端建立连接。由于使用了这种认证模式，存在潜在time-of-check/time-of-use (TOCTOU)的风险，然后在认证信息中增加了Revision字段，通过判断修订号一致性来避免这种可以使用老凭证的安全风险,考虑的相当周到了。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210630/65649c443be2f3e11695799e0190ccd9.jpg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210630/65649c443be2f3e11695799e0190ccd9.jpg" class="img-polaroid" title="5.jpg" alt="5.jpg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图5 核心的Authenticate()认证逻辑</em><br>
<br>2、使用基于角色的访问控制<br>
<br>开启认证后，为了进行精细化的访问控制，不建议直接使用root账号，可以添加角色、帐号并按需配置权限。在小y的公司有一套<a href="https://mp.weixin.qq.com/s/pxnrQNE5O9rXTRrzGKn_Sw">帐号与权限系统</a>，etcd服务可进行二次开发或基于etcd proxy接入帐号与权限系统中，实现对应用访问控制的配置管理。<br>
<br>创建角色限制访问控制：<br>
<pre class="prettyprint">#创建角色<br>
$ etcdctl role add testrole<br>
<br>
# 赋予testrole角色只读/foo的权限<br>
$ etcdctl role grant-permission testrole read /foo<br>
<br>
# 赋予testrole角色只读/foo前缀的权限，这个前缀的范围是 [/foo/, /foo0)<br>
$ etcdctl role grant-permission testrole --prefix=true read /foo/<br>
<br>
# 赋予testrole角色只写/foo/bar的权限<br>
$ etcdctl role grant-permission testrole write /foo/bar<br>
<br>
# 赋予testrole角色读取 [key1, key5)范围内的权限<br>
$ etcdctl role grant-permission testrole readwrite key1 key5<br>
<h1>将abc这个用户授予或添加到角色中</h1>etcdctl user grant-role test testrole<br>
etcdctl user revoke-role test testrole<br>
</pre><br>
3、传输加密&证书认证<br>
<br>相关证书可使用cfssl工具生成，请注意证书有效期，默认为一年，需要在到期前更新，否则会影响正常使用。<br>
<br>使用HTTPS的客户端到服务器的传输安全性，该配置可解决客户端到服务器的传输为安全，请准备好CA证书（ca.crt）和签名密钥对（server.crt，server.key）：<br>
<pre class="prettyprint">$ etcd  \<br>
--cert-file=/path/to/server.crt --key-file=/path/to/server.key \<br>
--advertise-client-urls=https://127.0.0.1:2379 --listen-client-urls=https://127.0.0.1:2379<br>
<br>
$ curl --cacert /path/to/ca.crt  -L https://localhost:2379/v3/kv/put \<br>
-X POST  -d '&#123;"key": "Zm9v", "value": "YmFy"&#125;'<br>
</pre><br>
使用HTTPS客户端证书的客户端到服务器身份验证，该配置可解决认证及传输问题，使用客户端证书来防止对etcd的未经授权的访问，客户端会向服务器端提供它们的证书并且服务器会检查该证书是否由指定 CA 颁发，然后决定是否接收该请求。  <br>
<br>在第一点中提到的相同的文件需要用于此，以及一个密钥对客户端（client.crt，client.key）由相同的认证机构签名。<br><br>
<pre class="prettyprint">$ etcd --name infra0 --data-dir infra0<br>
--client-cert-auth --trusted-ca-file=/path/to/ca.crt --cert-file=/path/to/server.crt --key-file=/path/to/server.key \<br>
--advertise-client-urls https://127.0.0.1:2379 --listen-client-urls https://127.0.0.1:2379<br>
<br>
curl --cacert /path/to/ca.crt --cert /path/to/client.crt --key /path/to/client.key \<br>
-L https://127.0.0.1:2379/v2/keys/foo -XPUT -d value=bar -v<br>
</pre><br>
集群中的传输安全性和客户端证书，该配置是解决集群间通信安全及身份验证的。<br>
<br>假定我们和我们的ca.crt两个成员具有由此CA签名的自己的密钥对（member1.crt＆member1.key，member2.crt＆member2.key），则按以下方式启动etcd：<br>
<pre class="prettyprint">DISCOVERY_URL=... # from https://discovery.etcd.io/new 这里可以使用公网发现服务<br>
<br>
$ etcd --name infra1 --data-dir infra1 \<br>
--peer-client-cert-auth --peer-trusted-ca-file=/path/to/ca.crt --peer-cert-file=/path/to/member1.crt --peer-key-file=/path/to/member1.key \<br>
--initial-advertise-peer-urls=https://10.0.1.10:2380 --listen-peer-urls=https://10.0.1.10:2380 \<br>
--discovery $&#123;DISCOVERY_URL&#125;<br>
<br>
# member2<br>
$ etcd --name infra2 --data-dir infra2 \<br>
--peer-client-cert-auth --peer-trusted-ca-file=/path/to/ca.crt --peer-cert-file=/path/to/member2.crt --peer-key-file=/path/to/member2.key \<br>
--initial-advertise-peer-urls=https://10.0.1.11:2380 --listen-peer-urls=https://10.0.1.11:2380 \<br>
--discovery $&#123;DISCOVERY_URL&#125; <br>
</pre><br>
etcd成员将形成一个集群，并且集群中成员之间的所有通信都将使用客户端证书进行加密和身份验证。<br>
<br>自动签名，对于那些只需要加密通信却不需要认证的场景，etcd支持使用自动生成的自签名证书加密通信。因为不需要管理etcd之外的证书和秘钥，故此大大简化了etcd的部署。使用自签发证书配置etcd服务器和客户端之间的通信要用到“--auto-ls”和“--peer-auto-tls”参数。这样，etcd就可以配置成自动生成key，即在初始化的时候，每个member都根据advertised IP地址和主机名创建需要的key。etcd启动参数具体如下：<br>
<pre class="prettyprint">DISCOVERY_URL=... # from https://discovery.etcd.io/new 这里使用公共的发现服务<br>
<br>
# member1<br>
$ etcd --name infra1 --data-dir infra1 \<br>
--auto-tls --peer-auto-tls \<br>
--initial-advertise-peer-urls=https://10.0.1.10:2380 --listen-peer-urls=https://10.0.1.10:2380 \<br>
--discovery $&#123;DISCOVERY_URL&#125;<br>
<br>
# member2<br>
$ etcd --name infra2 --data-dir infra2 \<br>
--auto-tls --peer-auto-tls \<br>
--initial-advertise-peer-urls=https://10.0.1.11:2380 --listen-peer-urls=https://10.0.1.11:2380 \<br>
--discovery $&#123;DISCOVERY_URL&#125; <br>
</pre><br>
4、etcd数据加密存储<br>
<br>etcd数据库中的数据默认未进行加密存储，如需加密存储有两种方案：<br>
<ul><li>应用程序对数据进行加密和解密（如果公司有加解密系统，可通过安全部提供的加解密接口，对敏感数据加密写入，读取后进行解密）</li><li>使用基础存储系统的功能来加密存储的数据，例如dm-crypt</li></ul><br>
<br>5、其他安全参数<br>
<br>--cipher-suites '' //服务器、客户端与对等方之间受支持的TLS密码套件，逗号分隔列表。指定密码套件可以阻止 弱TLS密码套件。  <br>
<br>--cors '*' //cors跨域资源访问设置 ，允许哪些域访问跨域访问该域资源  <br>
<br>--host-whitelist '*' // 如果客户端连接不安全未使用https且“HostWhitelist”不为空，则仅允许其Host字段列在白名单中的HTTP请求。该设置可以阻止DNS重绑定的安全问题  <br>
<br>--auth-token 'simple' //设置token 类型是简单类型，还是jwt类型。生产建议使用jwt类型  <br>
<br>--bcrypt-cost 10 //etcd 认证使用go的bcrypt包。默认cost是2的10次方去hash，这个值设置越高的越高加密次数会越多，最大32，理论上是根据机器性能尽可能选取最高值。但如果设置过高，密码验证会耗时较长，会出现用户名枚举的安全问题。<br>
<pre class="prettyprint">当--bcrypt-cost设为15时，密码hash为：$2a$15$stn0xJ7ieO/ikHpNd0PHP.ZpLarRJZ7ZHLUJrc3ZByq/6mqIh4H46<br>
<br>
$etcdctl --endpoints=127.0.0.1:2379 --user root:root user list  --dial-timeout=5s --debug<br>
.....<br>
INFO: 2021/03/01 13:44:31 parsed scheme: "endpoint"<br>
INFO: 2021/03/01 13:44:31 ccResolverWrapper: sending new addresses to cc: [&#123;127.0.0.1:2379  <nil> 0 <nil>&#125;]<br>
....(密码匹配了两秒后，才会返回)<br>
INFO: 2021/03/01 13:44:33 parsed scheme: "endpoint"<br>
INFO: 2021/03/01 13:44:33 transport: loopyWriter.run returning. connection error: desc = "transport is closing"<br>
INFO: 2021/03/01 13:44:33 ccResolverWrapper: sending new addresses to cc: [&#123;127.0.0.1:2379  <nil> 0 <nil>&#125;]<br>
root<br>
<br>
$etcdctl --endpoints=127.0.0.1:2379 --user rootOO9:**** user list  --dial-timeout=5s --debug<br>
....(直接返回帐号或密码不正确)<br>
<br>
Error: etcdserver: authentication failed, invalid user ID or password<br>
</pre><br>
通过对etcd官方文档、部分开源代码分析后，小y完成了etcd的安全实践。随即将结果同步至RKO项目组开发负责人z工，z工思索了片刻，决定交给小y第二个任务，“由于其他项目组也使用了etcd，大多数是直接拿来用的，安全性肯定没有考虑，将公司不安全的etcd都扫描检测出来，并进修复吧”。只见小y打开了burpsuite，开启了安全工程师视角……<br>
<h3>安全工程师视角</h3><h4>etcd风险检测</h4>小y在安全视角下，首先开始寻找etcd暴露面。etcd默认开放2379、2380端口，etcd使用了CMux包，在一个端口上注册了很多matcher，包括gRPC、v2api、v3api、Metrics、Trace等，所以一个端口下暴露了很多服务。经过对etcd的进一步学习，整理出以下暴露面：<br>
<br><strong>2379端口</strong><br>
<br>基础接口 HandleBasic(）：<br>
<ul><li>/config/local/log //设置etcd全局日志级别，暂时未发现未授权更改该设置会带来的安全影响</li><li>/debug/vars //启动命令等信息，可做信息收集进一步攻击</li><li>/version //etcd版本信息</li></ul><br>
<br>监控指标接口 HandleMetricsHealth()：<br>
<ul><li>/metrics</li><li>/health</li></ul><br>
<br>Trace接口，使用Go官方net trace包。<br>
<br>请注意设置debug参数会注册trace接口，会泄露etcd认证帐号密码。如请求：<a href="http://127.0.0.1:2379/debug/requests?fam=grpc.Recv.Auth&b=0&exp=1" rel="nofollow" target="_blank">http://127.0.0.1:2379/debug/re ... p%3D1</a>，可以看到etcd认证的帐号密码，通过fofa平台对暴露在公网的etcd服务进行扫描，检测出有在公网开启了etcd debug，导致密码泄露的情况。<br>
<ul><li>/debug/requests</li><li>/debug/events</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210630/6226cdac547687496c1d9ddf1f1697aa.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210630/6226cdac547687496c1d9ddf1f1697aa.png" class="img-polaroid" title="6.png" alt="6.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图6 本地开启debug泄露etcd认证的帐号密码</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210630/63d2d66213dc6be1b0f2ce810b44cfbf.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210630/63d2d66213dc6be1b0f2ce810b44cfbf.png" class="img-polaroid" title="7.png" alt="7.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图7 etcd注册Trace接口sensitive设置为true会展示敏感信息，导致帐号密码泄露</em><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210630/4685f567e15fd039c6ab63c81ab7089b.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210630/4685f567e15fd039c6ab63c81ab7089b.png" class="img-polaroid" title="8.png" alt="8.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图8 案例—etcd暴露在互联网并开启debug，泄露帐号密码</em><br>
<br>PProf分析接口：<br>
<ul><li>/debug/pprof</li><li>/debug/pprof/profile</li><li>/debug/pprof/symbol</li><li>/debug/pprof/cmdline</li><li>/debug/pprof/trace</li><li>/debug/pprof/heap</li><li>/debug/pprof/goroutine</li><li>/debug/pprof/threadcreate</li><li>/debug/pprof/block</li><li>/debug/pprof/mutex</li></ul><br>
<br>/v2 /v3 操作etcd的接口。<br>
<br><strong>2380端口</strong><br>
<br>peers：<br>
<ul><li>/members //成员信息接口</li><li>/members/promote/ //将成员提升为选举成员的接口</li></ul><br>
<br><div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210630/90cbf6aa3c18c0f6d8ec4853a4779821.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210630/90cbf6aa3c18c0f6d8ec4853a4779821.png" class="img-polaroid" title="9.png" alt="9.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图9 /members/promote/接口逻辑</em><br>
<br><strong>gRPC代理</strong><br>
<br>etcd grpc-proxy start xx，运行着无状态etcd grpc反向代理，只暴露http metrics，以及转发gRPC请求。<br>
<br>通过对etcd暴露面的分析，我们可以整理出需要检测的etcd安全风险。<br>
<br>不安全的版本：<br>
<br>如安全部门要求强制使用3.4.10及以上安全版本可请求version接口收集版本信息，扫描内网中的etcd服务进行版本比对（可以定时扫描内网中的etcd服务，探测etcd的版本上报安全中心，安全中心可统计公司使用etcd版本的比例）：<br>
<pre class="prettyprint">$ curl http://xxxxx:2377/version  <br>
&#123;"etcdserver":"3.3.11","etcdcluster":"3.3.0"&#125; //判断版本<br>
</pre><br>
v2 HttpAPI、v3 HttpAPI、gRPC未授权访问及弱密码：<br>
<br>编写脚本识别etcd服务，进行未授权访问、弱密码的检测。如某次内网扫描中发现存在etcdv2未授权访问，导致数据库密码等敏感信息可以随便查看<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210630/8332cee460390497b8232301c9ede130.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210630/8332cee460390497b8232301c9ede130.png" class="img-polaroid" title="10.png" alt="10.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图10 内网中etcd未开启认证但可查看数据库等敏感数据</em><br>
<br>开启debug导致帐号密码泄露：<br>
<br>通过扫描/debug/requests目录检测是否开启etcd debug。<br>
<br>小y在整理完etcd安全风险后，在中通心轮安全扫描系统中创建了漏洞，编写并pull了对应的扫描插件。随即又创建了该漏洞的应急扫描任务，扫描结束后漏洞同步至<a href="https://mp.weixin.qq.com/s/kWK9PL_C2IW_T9i_A1Mlsw">中通同安漏洞管理系统</a>中，进行漏洞的闭环处理。<br><br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210630/b49808704112b0f5aa4c7e5a5af2e940.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210630/b49808704112b0f5aa4c7e5a5af2e940.png" class="img-polaroid" title="11.png" alt="11.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>图11 中通心轮安全扫描器漏洞管理界面</em><br>
<h3>总结</h3>本篇文章讲述了如何安全的使用etcd，其一是介绍安全的思维逻辑，如何选择安全的项目，并进行安全配置，其二是站在安全工程视角如何发现、检测、闭环处理安全风险。etcd项目是一个成功的开源项目，虽然13年为了用户快速使用，没有完全考虑安全的问题，但在后面的版本中融入了大量的安全特性，值得借鉴学习。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/5RorSaxl3HwBtKbmc4lctQ" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/5RorSaxl3HwBtKbmc4lctQ</a>
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            </ul>
                                                              
</div>
            