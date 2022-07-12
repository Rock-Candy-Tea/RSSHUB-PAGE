
---
title: 'HertzBeat v1.1.1 发布，易用友好的云监控系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-de2ad8c3cb108b9be85c277eda1296559c0.png'
author: 开源中国
comments: false
date: Tue, 12 Jul 2022 08:58:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-de2ad8c3cb108b9be85c277eda1296559c0.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:black; margin-left:0; margin-right:0; text-align:left"><strong style="color:black">官网:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhertzbeat.com" target="_blank">hertzbeat.com</a><span> </span>|<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftancloud.cn" target="_blank">tancloud.cn</a></strong></p> 
<p style="color:black; margin-left:0; margin-right:0; text-align:left">大家早上好，监控告警系统 HertzBeat v1.1.1 发布啦！<span style="background-color:#ffffff; color:#40485b">这个版本带来了自定义监控增强，采集指标数据可以作为变量赋值给下一个采集。修复了若干bug，提升整体稳定性。</span></p> 
<p style="color:black; margin-left:0; margin-right:0; text-align:left">只需要一条 docker 命令即可安装体验 heartbeat ：<br> <code>docker run -d -p 1157:1157 --name hertzbeat tancloud/hertzbeat</code></p> 
<p style="color:black; margin-left:0; margin-right:0; text-align:left">花一分钟快来试试吧。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img height="1712" src="https://oscimg.oschina.net/oscnet/up-de2ad8c3cb108b9be85c277eda1296559c0.png" width="3840" referrerpolicy="no-referrer"></p> 
<p style="color:black; margin-left:0; margin-right:0; text-align:left">感谢 hertzbeat 贡献者们的贡献！👍👍</p> 
<p style="color:black; margin-left:0; margin-right:0; text-align:left">特性：</p> 
<p style="margin-left:0; margin-right:0"> </p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>[script] feature 升级docker的基础镜像为 openjdk:11.0.15-jre-slim #205</li> 
 <li>[monitor] 支持前置采集指标数据作为变量赋值给下一采集流程 #206.</li> 
 <li>[collector] 使用基本的http headers头实现basic auth替换前置模式 #212</li> 
 <li>[manager,alerter] 支持告警通知设置丁丁微信飞书自定义 webhook url #213</li> 
 <li>[monitor] feature 更新数值指标数据不带末尾为0的小数点 #217</li> 
 <li>[web-app]feature:toggle [enable and cancel] button #218</li> 
 <li>[manager] 更新监控define yml文件前缀名称 "app" or "param"，便于自定义监控区别 #221</li> 
</ol> 
<p style="color:black; margin-left:0; margin-right:0; text-align:left">BUG 修复.</p> 
<p style="margin-left:0; margin-right:0"> </p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>[update] docker-compose 添加jpa自动执行脚本,删除sql脚本 #198<span> </span>contribute by<span> </span>@dowell<span> </span>.</li> 
 <li>修复自定义监控描述文档 #199<span> </span>contribute by<span> </span>@dowell</li> 
 <li>[manager] bugfix oracle performance 指标采集异常问题 #201.</li> 
 <li>[common] bugfix 告警状态无法页面手动更新问题 #203</li> 
 <li>[manager] bugfix windows监控类型名称错误问题 #204</li> 
 <li>fix time zone todo issue #210<span> </span>contribute by @djzeng</li> 
 <li>[common] bugfix 雪花算法生成ID大小超出 0x1FFFFFFFFFFFFFF 导致前端不识别问题 #211</li> 
 <li>[manager] 修改监控页面取消监控功能再启动监控导致多生成jobId，原有监控项目并没有真实取消 #215<span> </span>contribute by<span> </span>@yangshihui</li> 
 <li>[warehouse] 修复tdengine对特殊字段建表失败导致数据无法入库问题 #220</li> 
</ol> 
<p style="color:black; margin-left:0; margin-right:0; text-align:left">在线环境 https://console.tancloud.cn.</p> 
<p style="color:black; margin-left:0; margin-right:0; text-align:left">Have Fun!</p> 
<blockquote> 
 <p style="color:black; margin-left:0; margin-right:0">HertzBeat 赫兹跳动 是由<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdromara.org" target="_blank">Dromara</a><span> </span>孵化，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftancloud.cn" target="_blank">TanCloud</a><span> </span>开源的一个支持网站，API，PING，端口，数据库，操作系统等监控类型，拥有易用友好的可视化操作界面的开源监控告警项目。<br> 我们也提供了对应的<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fconsole.tancloud.cn" target="_blank">SAAS 版本监控云</a><strong style="color:black">，中小团队和个人无需再为了监控自己的网站资源，而去部署一套繁琐的监控系统，</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fconsole.tancloud.cn" target="_blank">登录即可免费开始</a>。<br> HertzBeat 支持<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhertzbeat.com%2Fdocs%2Fadvanced%2Fextend-point" target="_blank">自定义监控</a><span> </span>, 只用通过配置 YML 文件我们就可以自定义需要的监控类型和指标，来满足常见的个性化需求。<br> HertzBeat 模块化，<code>manager, collector, warehouse, alerter</code><span> </span>各个模块解耦合，方便理解与定制开发。<br> HertzBeat 支持更自由化的告警配置 (计算表达式)，支持告警通知，告警模版，邮件钉钉微信飞书等及时通知送达<br> 欢迎登录 HertzBeat 的<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fconsole.tancloud.cn" target="_blank">云环境 TanCloud</a><span> </span>试用发现更多。<br> 我们正在快速迭代中，欢迎参与加入一起共建项目开源生态。</p> 
</blockquote> 
<blockquote> 
 <p style="color:black; margin-left:0; margin-right:0"><code>HertzBeat</code><span> </span>的多类型支持，易扩展，低耦合，希望能帮助开发者和中小团队快速搭建自有监控系统。</p> 
</blockquote> 
<p style="color:black; margin-left:0; margin-right:0; text-align:left"><strong style="color:black">仓库地址</strong></p> 
<p style="color:black; margin-left:0; margin-right:0; text-align:left"><strong style="color:black">Gitee https://gitee.com/dromara/hertzbea</strong></p> 
<p style="color:black; margin-left:0; margin-right:0; text-align:left"><strong style="color:black">Github https://github.com/dromara/hertzbeat</strong></p> 
<p style="color:black; margin-left:0; margin-right:0; text-align:left">看到这里不妨 Star 支持下哦，灰常感谢！</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left"><strong style="color:black">一条命令即可开启监控之旅：</strong><br> <code>docker run -d -p 1157:1157 --name hertzbeat tancloud/hertzbeat</code></h4>
                                        </div>
                                      
</div>
            