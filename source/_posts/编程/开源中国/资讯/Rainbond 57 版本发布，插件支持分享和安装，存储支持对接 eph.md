
---
title: 'Rainbond 5.7 版本发布，插件支持分享和安装，存储支持对接 eph'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://grstatic.oss-cn-shanghai.aliyuncs.com/wechat/5.7/5.7.png'
author: 开源中国
comments: false
date: Mon, 13 Jun 2022 16:56:00 GMT
thumbnail: 'https://grstatic.oss-cn-shanghai.aliyuncs.com/wechat/5.7/5.7.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt src="https://grstatic.oss-cn-shanghai.aliyuncs.com/wechat/5.7/5.7.png" referrerpolicy="no-referrer"></p> 
<h1>Rainbond 5.7 版本发布，插件支持分享和安装，存储支持对接Ceph</h1> 
<p>当前版本主要的变化有：</p> 
<p><strong>插件支持分享和一键安装</strong></p> 
<p><strong>扩展插件配置能力</strong></p> 
<p><strong>支持对接Ceph</strong></p> 
<p><strong>生产场景的性能优化等</strong></p> 
<h2>主要功能点解读：</h2> 
<h3>1. 插件分享和一键安装</h3> 
<p>为了业务容器的运维和管理能力，Rainbond 通过pod中的sidecar实现了插件机制。开发者可以自己开发插件，并根据业务需要按需开启和配置插件，当前插件已经可以实现：</p> 
<ul> 
 <li>在不更改现有业务代码的情况下扩展组件的功能</li> 
 <li>在业务运行前完成一些数据初始化的操作</li> 
 <li>将业务的日志发送到外部服务器用于分析处理</li> 
 <li>拦截清洗业务的流量，用作防火墙</li> 
 <li>监控业务的性能指标等</li> 
</ul> 
<p>但是，在之前的版本中，用户在某个团队下创建出插件后，需要给另一个团队使用时，还需要再次手动创建，设置对应的配置项。这在一定程度上增加了用户使用的门槛。</p> 
<p>现在和应用一样，我们在支持<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.rainbond.com%2Fdocs%2Fuse-manual%2Fapp-store-manage%2Fshare-app" target="_blank">应用的分享和一键安装</a>后，也可以支持插件的分享和一键安装。当你在某个团队下制作好了可用的插件，你可以通过 Rainbond 的本地组件库或开源应用商店分享出去。其他用户可以通过组件库和开源应用商店安装使用。这样的好处是插件也可以像应用一样积累和复用，社区用户开发的插件也可以分享给其他用户使用。</p> 
<p><img alt src="https://files.mdnice.com/user/23816/668573a2-32c4-4a6e-b5e5-529bb0a34588.png" referrerpolicy="no-referrer"></p> 
<h3>2. 扩展插件的配置能力</h3> 
<p>当插件本身运行时需要相应配置文件或存储时，用户需要手动去组件里添加存储。这是因为插件与组件之间共享存储，但是当一个插件用于多个组件时，那么需要去每个组件下配置存储，这造成了配置的复杂性。</p> 
<p>现在用户可以直接在插件里配置插件运行时所需的存储和配置文件。如下图所示：</p> 
<p><img alt src="https://files.mdnice.com/user/23816/92fafe4a-2638-4f64-b19b-e2a0b559faab.png" referrerpolicy="no-referrer"></p> 
<p>这样当用户为组件开通插件以后，就可以自动为组件创建出对应的存储和配置文件。减少了配置的复杂性。</p> 
<h3>3. 支持对接 Ceph</h3> 
<p>稳定可靠的存储是在生产环境中使用 Kubernetes 最重要的一环。Kubernetes 默认提供了主流的存储卷接入方案（In-Tree），同时也提供了插件机制（Out-Of-Tree），允许接入实现了 CSI 接口的第三方存储，当前版本中，通过扩展CSI能力可以完美对接Ceph。</p> 
<h2>详细变更点</h2> 
<h3>新增功能</h3> 
<ul> 
 <li>【插件管理】支持插件分享和安装</li> 
 <li>【插件管理】支持插件单独定义存储和配置文件</li> 
 <li>【组件管理】源码构建支持 nodejs16 版本；</li> 
 <li>【应用管理】支持应用按更新时间和运行状态排序；</li> 
 <li>【存储】支持通过 CSI 对接 ceph 存储</li> 
</ul> 
<h3>优化功能</h3> 
<ul> 
 <li>【组件管理】优化 web 终端默认容器为组件容器</li> 
 <li>【安装】优化 dind 版本安装时环境检测和提示</li> 
 <li>【安装】优化 helm 安装时环境检查与提示</li> 
 <li>【团队视图】优化团队视图响应速度</li> 
 <li>【组件管理】优化组件日志过大时导致占用磁盘过大的问题</li> 
 <li>【企业管理】企业视图下增加团队资源展示</li> 
 <li>【组件管理】优化内置 mesh 插件资源限制导致的性能问题</li> 
</ul> 
<h3>BUG 修复</h3> 
<ul> 
 <li>【网关】修复网关策略过多时，新增策略不生效的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoodrain%2Frainbond%2Fissues%2F1122" target="_blank">#1122</a></li> 
 <li>【组件管理】修复组件资源监控不生效的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoodrain%2Frainbond%2Fissues%2F1129" target="_blank">#1129</a></li> 
 <li>【组件管理】修复网关路径策略导致的服务端异常问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoodrain%2Frainbond%2Fissues%2F1169" target="_blank">#1169</a></li> 
 <li>【团队管理】修复团队创建者被删除导致团队列表无法展示的问题</li> 
 <li>【企业管理】修复Oauth授权自动过期的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoodrain%2Frainbond%2Fissues%2F1147" target="_blank">#1147</a></li> 
 <li>【组件管理】修复第三方组件出现空实例的问题</li> 
 <li>【应用管理】修复发布应用不展示日志的问题</li> 
 <li>【插件管理】修复初始化类型插件卸载后，组件更新后插件不会被清除的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoodrain%2Frainbond%2Fissues%2F1182" target="_blank">#1182</a></li> 
 <li>【插件管理】修复插件的启动命令中配置环境变量不生效问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoodrain%2Frainbond%2Fissues%2F1185" target="_blank">#1185</a></li> 
</ul> 
<h2>感谢</h2> 
<p><strong>感谢以下开源用户的参与和反馈</strong><br> @pescox<br> @briannadev<br> @wjn1992<br> @gobaiy<br> @hcxjava<br> @AlfredMiss<br> @pytomtoto<br> @wison1001<br> @haohao722<br> @huihui-hb<br> @superjackwong<br> @meijianxin110<br> @lokywang<br> @vicemiami<br> @yeshusheng1234</p>
                                        </div>
                                      
</div>
            