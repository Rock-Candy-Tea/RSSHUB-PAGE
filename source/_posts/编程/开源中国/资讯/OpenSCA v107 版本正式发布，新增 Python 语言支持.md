
---
title: 'OpenSCA v1.0.7 版本正式发布，新增 Python 语言支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-13e386b39703c478c10eb687e0de1a5c864.png'
author: 开源中国
comments: false
date: Fri, 01 Jul 2022 15:41:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-13e386b39703c478c10eb687e0de1a5c864.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>2022 年 6 月 29 日，OpenSCA 新版本 v1.0.7 正式发布，重磅功能持续更新，满足用户更多需求。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span><strong>1. </strong><strong>v1.0.7 更新内容</strong></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">新增支持 Python 语言的开源组件检测</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">新增 Gradle 包管理工具的静态解析</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">优化同一组件在不同路径检出时的展示效果</p> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span><strong>2. 更新说明</strong></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>（1）新增支持 Python 语言的开源组件检测</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">本版本中，我们新增一个重要功能，支持 Python 语言 pip 包管理工具的<strong><span style="color:#a417a1"><span> </span>pipfile、pipfile.lock 和 setup.py</span></strong><span> </span>特征文件的开源组件检测。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:center"><img alt height="406" src="https://oscimg.oschina.net/oscnet/up-13e386b39703c478c10eb687e0de1a5c864.png" width="1094" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>（2）新增 Gradle 包管理工具的静态解析</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">本版本新增支持 Gradle 的静态解析，在无法使用 Gradle 动态解析时会采用静态解析方法，此方法可以不依赖 Gradle 包管理工具。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>（3）优化同一组件在不同路径检出时的展示效果</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">针对同一组件在多个路径均检出时的情况，在检测结果中会展示一个组件，在该组件的 “检出路径” 功能模块内会列举展示多个路径。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:center"><img alt height="252" src="https://oscimg.oschina.net/oscnet/up-1dfda0359cb02394f843c85ee31811ba60a.png" width="1043" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span>3. 检测能力</span></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">目前 OpenSCA 已支持以下编程语言对应的包管理器及相关配置文件的解析：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:center"><img alt height="586" src="https://oscimg.oschina.net/oscnet/up-c2e17fc20dcbccf789a015aa63204771dfe.png" width="722" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:center"><strong><span style="color:#a417a1">参与和贡献，共建开源项目</span></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">感谢每一位开源社区成员对 OpenSCA 的支持和贡献。我们鼓励更多伙伴参与到 OpenSCA 开源项目的建设中来，成为开源贡献者，有任何建议都可以发在评论区或者 Gitee、GitHub 上 OpenSCA 项目的 Issues 中。让我们一起拥抱开源，共筑开源安全生态，促进开源产业健康发展。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>OpenSCA</strong><span> </span>是悬镜安全旗下<strong>源鉴 OSS</strong><span> </span>开源威胁管控产品的开源版本，继承了<strong>源鉴 OSS</strong><span> </span>的多源<span> </span><strong>SCA</strong><span> </span>开源应用安全缺陷检测等核心能力。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>OpenSCA</strong><span> </span>用开源的方式做开源风险治理，致力于做软件供应链安全的护航者，守护中国软件供应链安全。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>OpenSCA</strong><span> </span>的代码会在<span> </span><strong>GitHub</strong><span> </span>和<span> </span><strong>Gitee</strong><span> </span>持续迭代，欢迎<span> </span><strong>Star 和 PR</strong>，成为我们的开源贡献者，也可提交问题或建议至<span> </span><strong>Issues</strong>。我们会参考大家的建议不断完善<span> </span><strong>OpenSCA</strong><span> </span>开源项目，敬请期待更多功能的支持。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">GitHub：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:rgba(208, 192, 217, 0.41)">https://github.com/XmirrorSecurity/OpenSCA-cli/</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Gitee：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:rgba(208, 192, 217, 0.41)">https://gitee.com/XmirrorSecurity/OpenSCA-cli/</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">OpenSCA 官网：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:rgba(208, 192, 217, 0.41)">https://opensca.xmirror.cn/</span></p> 
<p> </p>
                                        </div>
                                      
</div>
            