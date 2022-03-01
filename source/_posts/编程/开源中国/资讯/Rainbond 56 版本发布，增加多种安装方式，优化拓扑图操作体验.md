
---
title: 'Rainbond 5.6 版本发布，增加多种安装方式，优化拓扑图操作体验'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.goodrain.com/wechat/upgrade-5.6/1.png'
author: 开源中国
comments: false
date: Tue, 01 Mar 2022 16:49:00 GMT
thumbnail: 'https://static.goodrain.com/wechat/upgrade-5.6/1.png'
---

<div>   
<div class="content">
                                                                                            <blockquote> 
 <p>Rainbond 5.6 版本，主要致力于提升拓扑图操作效率以及快速安装体验，降低用户使用门槛。</p> 
</blockquote> 
<h2>主要功能点解读：</h2> 
<h3>支持单机快速体验</h3> 
<p>为了方便在单机电脑上快速安装体验Rainbond，当前版本支持通过一条命令安装和体验，现在支持的平台包括：</p> 
<ul> 
 <li>Linux</li> 
 <li>Linux（ARM）</li> 
 <li>Mac（Intel）</li> 
 <li>Mac（M1）</li> 
 <li>Windows</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.rainbond.com%2Fdocs%2Fquick-start%2Fquick-install%2F%3Fchannel%3Doschina" target="_blank">快速安装</a></p> 
<h3>支持Helm安装方式</h3> 
<p>Helm 提供了一套简单易用的命令行，借助开发者制作好的 Charts 包完成应用的安装、更新、升级、回滚等操作。当前版本通过 Helm 作为包管理工具适配了市面可见的大多数 Kubernetes 类型，这些类型包括：</p> 
<ul> 
 <li> <p>使用不同安装工具（如kubeadm、sealos）部署的各种版本的标准 Kubernetes 集群；</p> </li> 
 <li> <p>各大云服务商推出的 Kubernetes 即服务的云产品，如阿里云ACK、腾讯云TKE、华为云CCE；</p> </li> 
 <li> <p>基于 Kubernetes 规范实现的其它容器基础设施，如Rancher、 K3s 、Kubedge；</p> </li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.rainbond.com%2Fdocs%2Fuser-operations%2Fdeploy%2Finstall-with-helm%2Fk8s-install-with-helm%2F%3Fchannel%3Doschina" target="_blank">Helm安装</a></p> 
<h3>优化拓扑图操作体验</h3> 
<p>在之前的版本中，由于 Rainbond 展示层级较多，用户操作单个组件时，往往需要切换到组件视图，这使得用户操作层级变多，也无法第一时间获取需要的信息。这次我们针对拓扑图的展示信息做了优化，使其能在应用层级给出更多的信息，并进行操作。降低进入组件视图的操作负担。</p> 
<p>新版本展示信息如下：</p> 
<p><img alt src="https://static.goodrain.com/wechat/upgrade-5.6/1.png" referrerpolicy="no-referrer"></p> 
<p>在新版本中，拓扑图展示信息处给出了一排组件操作按钮，分别是访问组件、进入Web终端、更新组件、关闭组件、删除组件。用户可以根据这些按钮快速操作组件，同时下方展示出了组件内的容器信息。极大的提升了用户的操作效率。</p> 
<h3>增加拓扑图聚合模式</h3> 
<p>在企业实际使用中，一个应用下的组件，往往会依赖其他应用下的组件，此时用户看到的拓扑图信息会大且比较杂乱，无法快速分辨其他组件所属的应用。这时对于用户而言，多个应用之间的依赖关系不明确。为了解决此问题，我们新增了拓扑图聚合模式。在这种情况下，可以更清晰的展示多个应用间的依赖关系。</p> 
<p>在普通模式下，可以看到该应用依赖了多个组件，但是我们对于这些组件之间的关系并不清楚。</p> 
<p><img alt="img" src="https://static.goodrain.com/wechat/upgrade-5.6/2.png" referrerpolicy="no-referrer"></p> 
<p>我们切换到聚合模式，可以看到，组件与其他应用之间的关系清晰明了。</p> 
<p><img alt="img" src="https://static.goodrain.com/wechat/upgrade-5.6/3.png" referrerpolicy="no-referrer"></p> 
<p>点开 Gitlab 这个应用的拓扑图，我们可以知道这个应用的运行状态，以及依赖的组件信息。</p> 
<p><img alt="img" src="https://static.goodrain.com/wechat/upgrade-5.6/4.png" referrerpolicy="no-referrer"></p> 
<h3>支持网关路径重写</h3> 
<p>之前 Rainbond 网关只实现了简单的location代理，并未提供路由重写相关的功能。当有这样的需求：</p> 
<p>要在目标服务<code>http://&#123;upstream&#125;/index.html</code>的path多加一层虚拟目录去访问：<code>http://example/abc/index.html</code>。达到 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fexample%2Fabc%2Findex.html" target="_blank">http://example/abc/index.html</a> => http://&#123;upstream-1&#125;/index.html 的效果。对应的网关配置如下。</p> 
<pre><code class="language-Nginx">location / &#123;

    rewrite /abc(/|$)(.*) /$2 last;

    proxy_pass http://127.0.0.1;

&#125;
</code></pre> 
<p>如今需要实现这种复杂的rewrite配置，只需在UI上填写对应字段即可，如下图所示：</p> 
<p><img alt="img" src="https://static.goodrain.com/wechat/upgrade-5.6/5.png" referrerpolicy="no-referrer"></p> 
<p>###</p> 
<h2>详细变更点</h2> 
<h3>新增功能</h3> 
<ul> 
 <li> <p>【应用管理】提升拓扑图展示信息；</p> </li> 
 <li> <p>【应用管理】支持拓扑图聚合模式；</p> </li> 
 <li> <p>【网关管理】支持网关路径重写；<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpescox" target="_blank">@pescox</a></p> </li> 
</ul> 
<h3>优化功能</h3> 
<ul> 
 <li> <p>【组件管理】优化添加组件流程；</p> </li> 
 <li> <p>【安装】支持arm64版本；</p> </li> 
 <li> <p>【安装】支持helm安装；</p> </li> 
 <li> <p>【安装】支持docker in docker方式启动测试环境；</p> </li> 
</ul> 
<h3>BUG 修复</h3> 
<ul> 
 <li> <p>【组件管理】修复组件构建后网关策略无法访问的问题</p> </li> 
 <li> <p>【组件管理】修复有状态组件(如Mysql集群)无法启动的问题</p> </li> 
 <li> <p>【性能】修复rbd-worker存在的内存泄漏问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpescox" target="_blank">@pescox</a></p> </li> 
 <li> <p>【安装】修复安装时错误信息展示不全的问题</p> </li> 
 <li> <p>【组件管理】修复helm应用关联的第三方组件信息错误的问题</p> </li> 
</ul> 
<p>感谢 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpescox" target="_blank">@pescox</a> 在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoodrain%2Frainbond%2Fissues%2F1125" target="_blank">#1125</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoodrain%2Frainbond%2Fissues%2F1139" target="_blank">#1139</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoodrain%2Frainbond%2Fissues%2F1143" target="_blank">#1143</a> 所做的贡献</p> 
<p>感谢 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxixinlove" target="_blank">@xixinlove</a> 在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoodrain%2Frainbond%2Fissues%2F1141" target="_blank">#1141</a> 所做的贡献</p>
                                        </div>
                                      
</div>
            