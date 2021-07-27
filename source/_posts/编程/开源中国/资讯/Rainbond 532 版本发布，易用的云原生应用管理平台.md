
---
title: 'Rainbond 5.3.2 版本发布，易用的云原生应用管理平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://ucc.alicdn.com/pic/developer-ecology/f487b5e9a87041b1963ae8ce1cd0891e.png'
author: 开源中国
comments: false
date: Tue, 27 Jul 2021 09:36:00 GMT
thumbnail: 'https://ucc.alicdn.com/pic/developer-ecology/f487b5e9a87041b1963ae8ce1cd0891e.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h1>Rainbond 5.3.2 版本发布，易用的云原生应用管理平台</h1> 
<blockquote> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgoodrain%2Frainbond" target="_blank">Rainbond</a> 是云原生且易用的应用管理平台。云原生应用交付的最佳实践。专注于以应用为中心的理念。赋能企业搭建云原生开发云、云原生交付云。</p> 
 <p><strong>对于企业：</strong> Rainbond 是开箱即用的云原生平台，借助 Rainbond 可以快速完成企业研发和交付体系的云原生转型。</p> 
 <p><strong>对于开发者：</strong> 基于 Rainbond 开发、测试和运维企业业务应用，开箱即用的获得全方位的云原生技术能力。包括但不仅限于持续集成、服务治理、架构支撑、多维度应用观测、流量管理。</p> 
 <p><strong>对于项目交付：</strong> 基于 Rainbond 搭建产品版本化管理体系，搭建标准化客户交付环境，使传统的交付流程可以自动化、简单化和可管理。</p> 
</blockquote> 
<h3>优化功能</h3> 
<p>- 【交付】应用发布记录信息完善，本地记录发布应用商店名称和应用模版名称；</p> 
<p>- 【交付】升级过程中增加了组件健康检测属性的变更展示。</p> 
<p>- 【交付】DockerCompose 导出的应用模版正确处理连接信息变量。</p> 
<p>- 【性能】优化企业视图统计数据 API 性能，加快组件数量较多时的页面价值速度；</p> 
<p>- 【管理】优化了离线环境下组件库列表加载速度问题。</p> 
<p>- 【安装】增加了对 Kubernetes 版本的检测和不合规提示。</p> 
<p>- 【安装】增加了集群安装出错后提示用户查询详细日志。</p> 
<p>- 【安装】突出了集群安装时对用户必要环境的提示。</p> 
<h3>BUG 修复</h3> 
<p>- 【交付】修复应用升级导致无变更组件进行了滚动更新的缺陷；</p> 
<p>- 【管理】修复应用列表页面与应用详情页对应用占用资源统计不一致的缺陷；</p> 
<p>- 【管理】修复团队资源限额后的提示错误缺陷；</p> 
<p>- 【管理】修复了 Helm 应用配置参数不生效的缺陷；</p> 
<p>- 【管理】修复了 Helm 应用升级页面加载不了数据的缺陷；</p> 
<p>- 【管理】修复了安装应用市场应用连接信息变量初始化错误的缺陷；</p> 
<p>- 【管理】修复了安装部分应用市场应用失败的缺陷；</p> 
<p>- 【管理】修复了网关策略设置为 websocket 不生效的缺陷；</p> 
<p>- 【管理】修复了应用切换治理模式后分配内存错误的缺陷；</p> 
<p>- 【安装】修复了集群初始化进度与实际状态不一致的缺陷；</p> 
<p>- 【用户】修复了单点登录模式下无法单点退出的缺陷；</p> 
<p>- 【CI】修复了对接 Gitee 私有化版本代码仓库无法列出项目列表的缺陷;</p> 
<p>- 【稳定性】修复了 rbd-worker 在进行主从切换时异常退出的缺陷；</p> 
<h3>升级方式</h3> 
<p>支持从 5.3.1 版本升级到5.3.2，参考 <a href="https://www.oschina.net/docs/upgrade/5.3.2-upgrade/">升级参考文档</a></p> 
<p>其他版本用户需要依次版本升级，参考以下文档升级到 5.3.1。</p> 
<p>支持从 5.3.0 版本升级到 5.3.1 <a href="https://www.oschina.net/docs/upgrade/5.3.1-upgrade/">升级参考文档</a></p> 
<p>支持从 5.2.X 版本升级到 5.3.1 <a href="https://www.oschina.net/docs/upgrade/5.2.2-5.3.1/">升级参考文档</a></p> 
<h3>社区</h3> 
<p>如果您对Rainbond项目感兴趣，如果您有一些疑问，如果您对云原生、Kubernetes等技术感兴趣，欢迎加入Rainbond 社区钉钉群（群号：31096419）</p> 
<p><img alt="dingding-group.png" src="https://ucc.alicdn.com/pic/developer-ecology/f487b5e9a87041b1963ae8ce1cd0891e.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            