
---
title: 'KubeSphere 3.1.1 发布，可以接入集群已有的 Prometheus'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=390'
author: 开源中国
comments: false
date: Tue, 03 Aug 2021 15:37:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=390'
---

<div>   
<div class="content">
                                                                                            <p>KubeSphere 作为一款面向应用的开源容器平台，经过 3 年的发展和 10 个版本的迭代，收获了两百多位开源贡献者，超过十万次下载，并有数千名社区用户用 KubeSphere 作为企业容器平台。</p> 
<p>7 月 7 日，KubeSphere 3.1.1 版本正式发布，<strong>现在部署 KubeSphere 时可以指定 Kubernetes 集群中已有的 Prometheus 啦！！！</strong></p> 
<p>鉴于最近有很多 KubeSphere 社区用户询问 KubeSphere 3.1.1 的发布进度，本文将会详细介绍 KubeSphere 3.1.1 比较重要的新特性。</p> 
<blockquote> 
 <p>KubeSphere 3.1.1 不是大版本更新，只是针对 v3.1.0 的 patch 版本，也就是修修补补的工作。本文只列出优化增强的功能，问题修复请查看完整的 Release Notes。</p> 
</blockquote> 
<h2>安装与升级</h2> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubesphere%2Fkubekey%2Fblob%2Fmaster%2FREADME_zh-CN.md" target="_blank">在 Linux 中安装 KubeSphere 3.1.1</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubesphere%2Fks-installer%2Fblob%2Fmaster%2FREADME_zh.md%23%25E9%2583%25A8%25E7%25BD%25B2-kubesphere" target="_blank">在 Kubernetes 中安装 KubeSphere 3.1.1</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubesphere%2Fks-installer%2Fblob%2Fmaster%2FREADME_zh.md%23%25E5%258D%2587%25E7%25BA%25A7" target="_blank">从 KubeSphere 低版本升级到 3.1.1 版本</a></li> 
</ul> 
<h2>优化增强的功能</h2> 
<h3>用户体验</h3> 
<ul> 
 <li>删除工作负载时支持批量删除关联资源 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubesphere%2Fconsole%2Fpull%2F1933" target="_blank">#1933</a></li> 
 <li>优化页面弹框 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubesphere%2Fconsole%2Fpull%2F2016" target="_blank">#2016</a></li> 
 <li>允许在 system-workspace 下的项目中使用容器终端 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubesphere%2Fconsole%2Fpull%2F1921" target="_blank">#1921</a></li> 
</ul> 
<h3>可观测性</h3> 
<ul> 
 <li>优化了通知设置中端口号的格式限制<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubesphere%2Fconsole%2Fpull%2F1885" target="_blank">#1885</a></li> 
 <li>支持安装时指定使用已有的 Prometheus. <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubesphere%2Fks-installer%2Fpull%2F1528" target="_blank">#1528</a></li> 
</ul> 
<h3>微服务治理</h3> 
<ul> 
 <li>优化 trace 页面增加时间选择器 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubesphere%2Fconsole%2Fpull%2F2022" target="_blank">#2022</a></li> 
</ul> 
<h3>DevOps</h3> 
<ul> 
 <li>支持 GitLab 多分支流水线按分支名筛选过滤 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubesphere%2Fconsole%2Fpull%2F2077" target="_blank">#2077</a></li> 
 <li>更改了 b2i 页面的“重新执行”按钮为“执行”<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubesphere%2Fconsole%2Fpull%2F1981" target="_blank">#1981</a></li> 
</ul> 
<h3>多集群管理</h3> 
<ul> 
 <li>优化了 member 集群配置错误时的提示信息 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubesphere%2Fconsole%2Fpull%2F2084" target="_blank">#2084</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubesphere%2Fconsole%2Fpull%2F1965" target="_blank">#1965</a></li> 
</ul> 
<h3>计量计费</h3> 
<ul> 
 <li>计量计费部分的 UI 调整 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubesphere%2Fconsole%2Fpull%2F1896" target="_blank">#1896</a></li> 
 <li>修改了计量计费按钮的颜色 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubesphere%2Fconsole%2Fpull%2F1934" target="_blank">#1934</a></li> 
</ul> 
<h3>应用商店</h3> 
<ul> 
 <li>优化应用模板创建页面提示文案与页面布局 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubesphere%2Fconsole%2Fpull%2F2012" target="_blank">#2012</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubesphere%2Fconsole%2Fpull%2F2063" target="_blank">#2063</a></li> 
 <li>优化应用导入功能 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubesphere%2Fopenpitrix-jobs%2Fpull%2F18" target="_blank">kubesphere/openpitrix-jobs#18</a></li> 
 <li>应用商店中新增 RadonDB PostgreSQL 应用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubesphere%2Fopenpitrix-jobs%2Fpull%2F17" target="_blank">kubesphere/openpitrix-jobs#17</a></li> 
</ul> 
<h3>安全</h3> 
<ul> 
 <li>切换 jwt-go 的分支，用于修复 CVE-2020-26160 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubesphere%2Fkubesphere%2Fpull%2F3991" target="_blank">#3991</a></li> 
 <li>升级 protobuf 版本至 v1.3.2 用于修复 CVE-2021-3121 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubesphere%2Fkubesphere%2Fpull%2F3944" target="_blank">#3944</a></li> 
 <li>升级 crypto 至最新版用于修复 CVE-2020-29652 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubesphere%2Fkubesphere%2Fpull%2F3997" target="_blank">#3997</a></li> 
 <li>移除了 yarn.lock 文件以避免一些 CVE 漏洞误报 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubesphere%2Fconsole%2Fpull%2F2024" target="_blank">#2024</a></li> 
</ul> 
<h3>存储</h3> 
<ul> 
 <li>提升了 s3 uploader 并发性能 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubesphere%2Fkubesphere%2Fpull%2F4011" target="_blank">#4011</a></li> 
 <li>增加预置的 CSI Provisioner CR 配置 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubesphere%2Fks-installer%2Fpull%2F1536" target="_blank">#1536</a></li> 
</ul> 
<h3>KubeEdge 集成</h3> 
<ul> 
 <li>支持 KubeEdge v1.6.2 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubesphere%2Fks-installer%2Fpull%2F1527" target="_blank">#1527</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubesphere%2Fks-installer%2Fpull%2F1542" target="_blank">#1542</a></li> 
</ul> 
<h2>下载与升级</h2> 
<p>大家可以到 KubeSphere GitHub 主页查看完整的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fkubesphere%2Fkubesphere%2Freleases%2Ftag%2Fv3.1.1" target="_blank">英文版 KubeSphere 3.1.1 Release Notes</a>，了解更多与升级有关的注意事项。国内用户也可以访问下方链接来查看完整的 Release Notes：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkubesphere.com.cn%2Fdocs%2Frelease%2Frelease-v311%2F" target="_blank">https://kubesphere.com.cn/docs/release/release-v311/</a></li> 
</ul>
                                        </div>
                                      
</div>
            