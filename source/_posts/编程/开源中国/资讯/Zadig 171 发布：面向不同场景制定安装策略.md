
---
title: 'Zadig 1.7.1 发布：面向不同场景制定安装策略'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-73f391e976a6786dcb3b0e39e48de11a500.png'
author: 开源中国
comments: false
date: Wed, 29 Dec 2021 18:00:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-73f391e976a6786dcb3b0e39e48de11a500.png'
---

<div>   
<div class="content">
                                                                                            <h1 style="margin-left:0; margin-right:0; text-align:left"><u><strong>有秀必应</strong></u></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">众所周知，Zadig V1.7.0 重磅推出了权限管理和统一用户接入功能，优化了系统架构，对于企业场景极其适用，但与此同时也在安装层面带来了一定的复杂度，如 STORAGE_CLASS 配置复杂、初始化任务失败、MySQL startupProbe 报出 warning 等问题，使得 Zadig V1.7.0 的一次安装升级成功率较低，影响了用户对 Zadig 的信心。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">研发团队全面复盘了社区小伙伴们反馈的问题，针对每个问题进行改善，并开了一场线上会议倾听社区小伙伴们的吐槽，现场解决问题。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在此基础上，我们对安装策略重新做了系统的思考，<span style="color:#ff7faa">在 V1.7.1 推出了面向场景的安装策略</span>，降低 Zadig 安装复杂度，期待能够给用户带来更好的体验。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:center"><img alt="图片" src="https://oscimg.oschina.net/oscnet/up-73f391e976a6786dcb3b0e39e48de11a500.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:center"> </p> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><u><strong>2 个 版本，3 个场景，对应 3 种安装方式</strong></u></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>Zadig 采用 </span><strong>主干开发</strong><span>、</span><strong>分支发布</strong><span> 的模式，所有的开发基于 main 分支，在 main 分支达到发布条件后，会从 main 分支拉取 release 分支进行打版发布，推出包含经过全面测试的 正式版本。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="color:#ff7faa">Nightly 版本：</span></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>为了便于开发者和用户尝鲜</strong>，Zadig 从 V1.7.1 版本开始推出了 Nightly 版本，会在每周二、周四定期对 main 分支进行打版。Nightly 版本仅通过了 smoke test，可能会存在 bug，选择 Nightly 尝鲜时请先了解风险。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="color:#ff7faa">正式版本：</span></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Zadig 业务组件运行过程中，还需要 MongoDB / MySQL / 对象存储 (如 Minio) 等依赖组件，这些组件本不属于 Zadig 维护的范畴，但为了给用户带来极致体验，我们在安装包中包含了 <strong>业务组件</strong> 和 <strong>依赖组件</strong>。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在之前的版本中，Zadig 依赖组件默认采用持久化存储，需要用户理解 StorageClass、PV、PVC 等 K8s 概念，并在 K8s 集群中进行正确配置，然后才能成功安装 Zadig。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">使用持久化存储的同时也会增大依赖组件的启动耗时，会导致 Zadig 业务组件启动过程中异常重试或重建。这个过程中的 warning 或 error 信息虽然是预期内，不影响 Zadig 最终安装成功，但会带来用户对 Zadig 安装可靠性的担忧。为了降低快速体验场景中持久化存储带来的复杂度，我们使用 K8s 的 EmptyDir 提供依赖组件需要的存储，提升启动 MongoDB / MySQL / 对象存储 的成功率和效率。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>对于生产使用</strong>，我们依然推荐使用外置高可用的 MongoDB / MySQL / 对象存储，保障数据的可靠性。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="color:#ff7faa">面向场景制定安装策略：</span></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">基于上述分析，我们推出两种版本 ，并针对<span style="color:#ff7faa">快速体验</span>和<span style="color:#ff7faa">生产使用</span>场景，提供不同的安装策略，进一步提升安装体验：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="图片" src="https://oscimg.oschina.net/oscnet/up-5f9cbd04331bad257ba4cf3ce3c39686d6c.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><u><strong>新安装策略</strong></u></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>1. Nightly 版本</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">部署包可以通过 link 获取，在虚拟机上使用如下几条命令就可以快速安装：</p> </li> 
</ul> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span><span style="color:#ca7d37"><span>export</span></span> IP=<NODE PUBLIC IP></span></code><code><span><span style="color:#ca7d37"><span>export</span></span> PORT=<<span style="color:#0e9ce5">30000</span>~<span style="color:#0e9ce5">32767</span> 任一端口></span></code><code><span>curl -sL <span style="color:#dd1144"><span style="color:#032f62">"https://download.koderover.com/install?type=nightly"</span></span> | bash</span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:center">3 行命令，成功安装！</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:center"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>2. 正式版</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span><strong><span><span>1）面向</span><span style="color:#ff7faa">快速体验场景</span><span>的安装模式：</span></span></strong></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>其目的是方便以最小心智安装，用户不用深入了解和配置 K8s 存储</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>虚拟机环境的操作同上述 Nightly 版本，下述以 K8s 场景为例说明：</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">参见 link 获取面向快速体验场景的安装包，针对 K8s 集群执行如下操作便可快速安装：</p> </li> 
</ul> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span><span style="color:#ca7d37"><span>export</span></span> IP=<任一 NODE PUBLIC IP></span></code><code><span><span style="color:#ca7d37"><span>export</span></span> PORT=<30000~32767 任一端口></span></code><code><span>curl -sL <span style="color:#dd1144"><span style="color:#032f62">"https://download.koderover.com/install?type=quickstart"</span></span> | bash</span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:center">3 行命令，成功安装！</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>2）面向<span style="color:#ff7faa">生产环境</span>的安装模式：</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">推荐用户使用外置高可用的 MongoDB / MySQL / 对象存储 (如 Minio) ，或使用 Zadig 安装包中容器化的 MongoDB / MySQL / Minio，并为三者提供持久化存储</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>下述以外置高可用的 MongoDB / MySQL 为例说明：</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">参见 link 获取面向快速体验场景的安装包，针对 K8s 集群执行如下操作便可快速安装：</p> </li> 
</ul> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span><span style="color:#ca7d37"><span style="color:#d73a49">export</span></span> IP=<IP></span></code><code><span><span style="color:#ca7d37"><span style="color:#d73a49">export</span></span> PORT=<<span>30000</span>~<span>32767</span> 任一端口></span></code><code><span><span style="color:#ca7d37"><span style="color:#d73a49">export</span></span> EMAIL=example@koderover.com</span></code><code><span><span style="color:#ca7d37">export</span> PASSWORD=zadig</span></code><code><span><em><span style="color:#6a737d"># 配置高可用的 MySQL。</span></em></span></code><code><span><em><span style="color:#6a737d"># 安装前需要手动在该 MySQL 实例中创建名为 dex 的 database</span></em></span></code><code><span><span style="color:#ca7d37"><span style="color:#6a737d">export</span></span><span style="color:#6a737d"> MYSQL_HOST=<span><MYSQL_HOST></span></span></span></code><code><span><span style="color:#ca7d37"><span style="color:#6a737d">export</span></span><span style="color:#6a737d"> MYSQL_PORT=<span><MYSQL_PORT></span></span></span></code><code><span><span style="color:#ca7d37"><span style="color:#6a737d">export</span></span><span style="color:#6a737d"> MYSQL_USERNAME=<span><MYSQL_USERNAME></span></span></span></code><code><span><span style="color:#ca7d37"><span style="color:#6a737d">export</span></span><span style="color:#6a737d"> MYSQL_PASSWORD=<span><MYSQL_PASSWORD></span></span></span></code><code><span><em><span style="color:#6a737d"># 配置高可用的 MongoDB</span></em></span></code><code><span><span style="color:#ca7d37"><span style="color:#6a737d">export</span></span><span style="color:#6a737d"> MONGO_URI=<span><MONGO_URI></span></span></span></code><code><span><span style="color:#ca7d37"><span style="color:#6a737d">export</span></span><span style="color:#6a737d"> MONGO_DB=<span><MONGO_DB></span></span></span></code>
<code><span>curl -sL <span style="color:#dd1144"><span style="color:#032f62">"https://download.koderover.com/install?type=standard | bash</span></span></span></code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:center">数行命令，成功安装！</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><u><strong>进一步优化</strong></u></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>不论是脚本方式还是 Helm 方式，Zadig 的安装本质上是如下形态：</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="图片" src="https://oscimg.oschina.net/oscnet/up-97fbdbecb708f280264144582906e8e42e2.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#888888"><em><span style="color:#888888">Zadig Chart 作为代码包封装了 Zadig 所有服务，对外提供了脚本 和 Helm CLI 两类使用方法，不同的安装方式区别在于使用方法中参数的不同。</span></em></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#ff7faa"><strong>Zadig Chart 的局限性</strong></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">脚本方式虽然灵活，但对于故障自查等场景，会有比较高的实现成本和维护成本。Helm CLI 虽然是社区管理 Chart 的标准工具，但缺少面向业务场景的故障自查等能力，需要二次封装，且在业务有自身 CLI 的情况下，Helm CLI 会带来额外的工具学习、使用成本。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#ff7faa"><strong>关于优化的思考</strong></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">为此，我们在思考提供更为便利强大的安装工具，降低 Zadig 整体的使用负担，如在 Zadig 已有的 CLI 工具 kodespace 中集成安装、升级、初始化、故障自查等服务。同时我们也在考虑进一步发挥 CLI 工具的能力，提供插件机制，方便社区小伙伴们针对自身的环境做集成。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="图片" src="https://oscimg.oschina.net/oscnet/up-dd600b4120a9f2336c0821990061e02407a.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<h1 style="margin-left:0; margin-right:0; text-align:left"><u><strong>Zadig 线上安装会</strong></u></h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>安装是使用 Zadig 的第一步，我们很重视每个用户的反馈。为了给 Zadig 用户提供更好的触达渠道，我们计划分别从 12.30 号开始每周四下午 4 点举行一次线上讨论会，倾听用户的吐槽、问题和建议，现场答疑，针对问题制定改善计划。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>会议主题</strong>：Zadig 线上倾听会</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>会议时间：</strong>每周四 16:00-17:00 北京时间 （2021/12/30 起）</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>扫码入会</strong>：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt height="300" src="https://oscimg.oschina.net/oscnet/up-cb6dcfc45e337baa3d6b805d2f0ff0aadb4.png" width="300" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            