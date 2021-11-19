
---
title: '腾讯云容器安全服务（TCSS）捕获利用 GitLab ExifTool RCE 漏洞在野攻击案例'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/1119/142026_J8YH_5430600.png'
author: 开源中国
comments: false
date: Fri, 19 Nov 2021 14:30:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/1119/142026_J8YH_5430600.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><strong>腾讯云容器安全服务（TCSS）</strong><span>捕获 GitLab ExifTool RCE漏洞（<span>CVE-2021-22205</span>）在公有云的在野攻击案例，漏洞利用导致业务容器内被植入后门程序。攻击者利用漏洞攻击后，企业业务容器会被植入门罗币挖矿程序、后门程序、或其他木马。<br> <br> <strong>漏洞编号：</strong>CVE-2021-22205<br> <br> <strong>漏洞等级：</strong></span><span><span style="color:#ff0000">严重，初始 CVSS 评分：9.9</span><span>。</span></span></p> 
<p><span>之后在 2021 年 9 月 21 日，GitLab 官方将 CVSS 评分修改为最高的 10.0。</span></p> 
<p><span><strong><span>漏洞影响版本<span>：</span></span></strong></span></p> 
<p><span>11.9.0 <= Gitlab CE/EE < 13.8.8</span></p> 
<p><span>13.9.0 <= Gitlab CE/EE < 13.9.6</span></p> 
<p><span>13.10.0 <= Gitlab CE/EE < 13.10.3</span></p> 
<h2><span><strong><span>漏洞在野利用事件描述：</span></strong></span></h2> 
<p><span>GitLab 是美国 GitLab 公司的一款使用 RubyonRails 开发的、自托管的、Git（版本控制系统）项目仓库应用程序。该程序可用于查阅项目的文件内容、提交历史、Bug 列表等，可通过 Web 界面访问公开或私人项目。由于 GitLab 存在未授权的端点，导致该漏洞在无需进行身份验证的情况下即可进行利用。</span></p> 
<h2><strong><span><span>腾讯安全网络空间测绘：</span></span></strong></h2> 
<p><span><span style="color:#000000">腾讯安全网络空间测绘结果显示，</span><span style="color:#000000">GitLab</span><span style="color:#000000">组件在全球应用分布较广，中国占比最高（</span><span style="color:#000000">31.19%</span><span style="color:#000000">）、其次是美国（</span><span style="color:#000000">16.80%</span><span style="color:#000000">）、德国（</span><span style="color:#000000">12.77%</span><span style="color:#000000">）。在中国大陆地区，浙江、北京、广东、上海四省市位居前列，占比超过</span><span style="color:#000000">83%</span><span style="color:#000000">。</span></span></p> 
<p><img alt height="665" src="https://static.oschina.net/uploads/space/2021/1119/142026_J8YH_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<p><span style="color:#333333"><span>腾讯安全 10 月 28 日、29 日分别发布过漏洞风险通告及在野利用通告，后陆续发现黑产组织利用该漏洞大量攻击云主机（参考链接：</span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzI5ODk3OTM1Ng%3D%3D%26mid%3D2247499555%26idx%3D1%26sn%3Dc1fd70b5469ae31e9a7c6d2b1ad8df4f%26scene%3D21%23wechat_redirect" target="_blank"><span style="color:#0052ff"><em>https://mp.weixin.qq.com/s/WQtx1ujwfN-Vybl7DJgBuw</em></span></a><span style="color:#333333"><span>）</span></span></p> 
<p><span><span style="color:#0052ff"><strong>腾讯云容器安全服务（TCSS）</strong></span><span>近期对开发人员常用的容器镜像进行安全检测，结果发现：存在GitLab ExifTool RCE漏洞的风险镜像228个，存在风险的镜像文件曾被广泛下载使用。安全检测数据表明，已有个别客户因使用存在该漏洞的风险镜像而发生入侵事件。</span></span></p> 
<h2><span><strong>漏洞修复建议：</strong></span></h2> 
<p><span><span>腾讯安全专家建议政企机构开发者及时升级Gitlab到最新版本，或使用已修复漏洞的最新Gitlab镜像，配置访问控制策略，避免受影响的Gitlab暴露在公网。</span></span></p> 
<p><span>参考：</span><u><em>https://about.gitlab.com/update/</em></u><br> <br> <span>推荐从可靠可信的云服务厂商官方网站下载安全镜像：</span></p> 
<ul> 
 <li><u><em>https://hub.docker.com/r/gitlab/gitlab-ce</em></u></li> 
 <li><u><em>https://hub.docker.com/r/gitlab/gitlab-ee</em></u></li> 
</ul> 
<p><span>可以使用腾讯容器安全服务（TCSS）对已使用的镜像进行安全扫描，存在风险的过期镜像文件建议弃用。在日常运维工作需要使用容器镜像前，使用文件查杀功能扫描容器内是否存在木马、病毒文件。</span></p> 
<p><span style="background-color:#ffffff; color:#333333">腾讯容器安全服务（TCSS）检测到存在 Gitlab ExifTool RCE 漏洞风险的镜像：</span></p> 
<p><img alt height="380" src="https://static.oschina.net/uploads/space/2021/1119/142419_FmLo_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#333333">漏洞利用后，会导致这个镜像拉起的容器被入侵。目前观察到有个别客户因未及时修复漏洞，导致容器被挖矿、被植入后门程序。</span></p> 
<p><img alt height="384" src="https://static.oschina.net/uploads/space/2021/1119/142439_znPt_5430600.png" width="700" referrerpolicy="no-referrer"></p> 
<p><span style="color:#333333">容器安全服务-镜像安全-本地镜像控制台链接：</span><u><em>https://console.cloud.tencent.com/tcss/security/image</em></u><br> <span style="color:#333333">容器安全服务-运行时安全-文件查杀控制台链接：</span><u><em>https://console.cloud.tencent.com/tcss/runtime/tojanDetection</em></u></p>
                                        </div>
                                      
</div>
            