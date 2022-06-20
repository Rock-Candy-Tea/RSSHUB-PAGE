
---
title: '云监控系统 HertzBeat v1.1.0 发布，一条命令开启监控之旅!'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-de2ad8c3cb108b9be85c277eda1296559c0.png'
author: 开源中国
comments: false
date: Mon, 20 Jun 2022 08:52:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-de2ad8c3cb108b9be85c277eda1296559c0.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:black; margin-left:0; margin-right:0"><strong style="color:black">官网: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhertzbeat.com" target="_blank">hertzbeat.com</a> | <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftancloud.cn" target="_blank">tancloud.cn</a></strong></p> 
<p style="color:black; margin-left:0; margin-right:0">大家早上好啊，监控告警系统 HertzBeat v1.1.0 发布啦！这个版本我们支持了SNMP协议，并使用SNMP协议监控支持了windwos操作系统的应用监控。SNMP协议支持自定义监控，欢迎贡献基于SNMP的监控实践。<br> 另一个重大变更是我们默认使用了H2数据库来替换MYSQL数据库作为存储，来方便使用者们的安装部署，现在只需要一条docker命令即可安装体验heartbeat ：<br> <code>docker run -d -p 1157:1157 --name hertzbeat tancloud/hertzbeat</code></p> 
<p style="color:black; margin-left:0; margin-right:0; text-align:left">花一分钟快来试试吧。</p> 
<p><img height="1712" src="https://oscimg.oschina.net/oscnet/up-de2ad8c3cb108b9be85c277eda1296559c0.png" width="3840" referrerpolicy="no-referrer"></p> 
<p style="color:black; margin-left:0; margin-right:0">感谢hertzbeat贡献者们的贡献！👍👍</p> 
<p style="color:black; margin-left:0; margin-right:0">特性：</p> 
<ol style="list-style-type:decimal"> 
 <li> <p>[monitor]feature: 支持SNMP协议和Windows操作系统监控 #192. contribute by @ChineseTony</p> </li> 
 <li> <p>[monitor]默认使用H2数据库替换MYSQL数据库 #191</p> </li> 
 <li> <p>[manager]支持监控参数的英文国际化，国际化更近一步 #184.</p> </li> 
 <li> <p>[script]支持了amd64和arm64版本的docker 镜像 #189.</p> </li> 
 <li> <p>[monitor]feature: 支持采集oracle多表空间指标数据 #163 contribute by @brave4Time</p> </li> 
 <li> <p>[monitor]数据库表统一添加前缀 hzb_ #193 issue from @shimingxy</p> </li> 
</ol> 
<p style="color:black; margin-left:0; margin-right:0">BUG修复.</p> 
<ol style="list-style-type:decimal"> 
 <li> <p>[monitor]修改在tencent centos版本下无法采集CPU指标问题 #164 contribute by @wyt199905 .</p> </li> 
 <li> <p>[manager]修复oracle监控percentage指标采集问题 #168</p> </li> 
 <li> <p>[monitor] bugfix: 修复elasticsearch监控在basic认证情况下采集失败 #174 contribute by @weifuqing</p> </li> 
 <li> <p>修改oracle监控参数[数据库名称]有歧义导致的监控失败 #182 @zklmcookle</p> </li> 
</ol> 
<p style="color:black; margin-left:0; margin-right:0">在线环境 https://console.tancloud.cn.</p> 
<hr> 
<p style="color:black; margin-left:0; margin-right:0">Windows 监控来啦：</p> 
<p><img alt="2022-06-19 11 30 57" src="https://user-images.githubusercontent.com/24788200/174481159-b8a73c87-aff5-4c4c-befb-bd0d26685d71.png" width="1444" referrerpolicy="no-referrer"></p> 
<p style="color:black; margin-left:0; margin-right:0">升级⚠️⚠️⚠️⚠️请注意低版本升级到v1.1.0需要先执行下面的SQL脚本. 现在我们的表名称有个统一前缀 hzb_ prefix.</p> 
<pre><code>ALTER  TABLE alert RENAME TO hzb_alert;
ALTER  TABLE alert_define RENAME TO hzb_alert_define;
ALTER  TABLE alert_define_monitor_bind RENAME TO hzb_alert_define_monitor_bind;
ALTER  TABLE monitor RENAME TO hzb_monitor;
ALTER  TABLE notice_receiver RENAME TO hzb_notice_receiver;
ALTER  TABLE notice_rule RENAME TO hzb_notice_rule;
ALTER  TABLE param RENAME TO hzb_param;
ALTER  TABLE param_define RENAME TO hzb_param_define;
ALTER  TABLE tag RENAME TO hzb_tag;
ALTER  TABLE tag_monitor_bind RENAME TO hzb_tag_monitor_bind;
commit;
</code></pre> 
<p style="color:black; margin-left:0; margin-right:0">Have Fun!</p> 
<blockquote> 
 <p style="color:black; margin-left:0; margin-right:0">HertzBeat赫兹跳动 是由<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdromara.org" target="_blank">Dromara</a>孵化，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftancloud.cn" target="_blank">TanCloud</a>开源的一个支持网站，API，PING，端口，数据库，操作系统等监控类型，拥有易用友好的可视化操作界面的开源监控告警项目。<br> 我们也提供了对应的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fconsole.tancloud.cn" target="_blank">SAAS版本监控云</a><strong style="color:black">，中小团队和个人无需再为了监控自己的网站资源，而去部署一套繁琐的监控系统，</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fconsole.tancloud.cn" target="_blank">登录即可免费开始</a>。<br> HertzBeat 支持<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhertzbeat.com%2Fdocs%2Fadvanced%2Fextend-point" target="_blank">自定义监控</a> ,只用通过配置YML文件我们就可以自定义需要的监控类型和指标，来满足常见的个性化需求。<br> HertzBeat 模块化，<code>manager, collector, warehouse, alerter</code> 各个模块解耦合，方便理解与定制开发。<br> HertzBeat 支持更自由化的告警配置(计算表达式)，支持告警通知，告警模版，邮件钉钉微信飞书等及时通知送达<br> 欢迎登录 HertzBeat 的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fconsole.tancloud.cn" target="_blank">云环境TanCloud</a> 试用发现更多。<br> 我们正在快速迭代中，欢迎参与加入一起共建项目开源生态。</p> 
</blockquote> 
<blockquote> 
 <p style="color:black; margin-left:0; margin-right:0"><code>HertzBeat</code>的多类型支持，易扩展，低耦合，希望能帮助开发者和中小团队快速搭建自有监控系统。</p> 
</blockquote> 
<p style="color:black; margin-left:0; margin-right:0"><strong style="color:black">仓库地址</strong></p> 
<p style="color:black; margin-left:0; margin-right:0"><strong style="color:black">Gitee https://gitee.com/dromara/hertzbea</strong></p> 
<p style="color:black; margin-left:0; margin-right:0"><strong style="color:black">Github https://github.com/dromara/hertzbeat</strong></p> 
<p style="color:black; margin-left:0; margin-right:0">看到这里不妨 Star 支持下哦，灰常感谢！</p> 
<h4><span>一句话版本更新总结</span></h4> 
<p style="color:black; margin-left:0; margin-right:0"><strong style="color:black">支持SNMP协议，Windows监控，一条命令即可开启监控之旅：</strong><br> <code>docker run -d -p 1157:1157 --name hertzbeat tancloud/hertzbeat</code></p>
                                        </div>
                                      
</div>
            