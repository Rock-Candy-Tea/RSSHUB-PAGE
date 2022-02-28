
---
title: 'HertzBeat 赫兹跳动 v1.0.beta.4 发布，易用友好的高性能监控告警系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7775'
author: 开源中国
comments: false
date: Mon, 28 Feb 2022 08:43:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7775'
---

<div>   
<div class="content">
                                                                    
                                                        <p><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fdromara%2Fhertzbeat">HertzBeat赫兹跳动</a><span style="background-color:#ffffff; color:#6a737d"><span> </span>是由</span><a href="https://gitee.com/link?target=https%3A%2F%2Fdromara.org">Dromara</a><span style="background-color:#ffffff; color:#6a737d">孵化，</span><a href="https://gitee.com/link?target=https%3A%2F%2Ftancloud.cn">TanCloud</a><span style="background-color:#ffffff; color:#6a737d">开源的一个支持网站，API，PING，端口，数据库，全站等监控类型，支持</span><span style="background-color:#ffffff; color:#40485b">阈值告警，告警通知(</span><span style="background-color:#efefef; color:#1c1e21">邮箱，webhook，钉钉，企业微信，飞书机器人</span><span style="background-color:#ffffff; color:#40485b">)</span><span style="background-color:#ffffff; color:#6a737d">，拥有易用友好的可视化操作界面的开源监控告警项目。</span>   </p> 
<p><strong style="color:#333333">官网:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhertzbeat.com%2F" target="_blank">hertzbeat.com</a><span> </span>|<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftancloud.cn%2F" target="_blank">tancloud.cn</a></strong></p> 
<p style="color:#40485b; margin-left:0em; margin-right:0em; text-align:start">此升级版本包含了大量特性与修复，包括用户急需的账户用户配置，丰富了主流第三方告警通知(企业微信机器人，钉钉机器人，飞书机器人)，更好看的邮件模版，自定义邮件服务器等，欢迎使用。</p> 
<p style="color:#40485b; margin-left:0em; margin-right:0em; text-align:start">版本特性：</p> 
<ol> 
 <li>告警通知：集成飞书官方WebHook实现推送告警信息 #PR9 由<span> </span><span style="background-color:#ffffff; color:#40485b">@learning-code </span>贡献 thanks</li> 
 <li>告警通知：实现企业微信WebHook告警信息推送 #PR8 由<span> </span><span style="background-color:#ffffff; color:#40485b">@learning-code</span><a href="https://gitee.com/learning-code"> </a><span>贡献 thanks</span></li> 
 <li>告警通知：告警邮件通知模版优化 由<span> </span><span style="background-color:#ffffff; color:#40485b">@learning-code</span><a href="https://gitee.com/learning-code"> </a><span>贡献 thanks</span></li> 
 <li>告警通知：集成钉钉群机器人实现推送告警信息</li> 
 <li>账户：暴露支持YML文件配置登陆用户账户信息</li> 
 <li>支持自定义邮件服务器</li> 
 <li>新增帮助中心，监控告警等功能使用过程中的帮助文档.<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Ftancloud.cn%2Fdocs%2Fhelp%2Fguide" target="_blank">https://tancloud.cn/docs/help/guide</a></li> 
 <li>DOC其它文档更新，本地启动帮助</li> 
 <li>新LOGO更新</li> 
 <li>监控采集间隔时间放开为7天</li> 
 <li>新增controller接口入参限定修饰符 由<span> </span><span style="background-color:#ffffff; color:#40485b">@learning-code</span><a href="https://gitee.com/learning-code"> </a><span>贡献 thanks</span></li> 
</ol> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">BUG修复</p> 
<ol> 
 <li>监控host参数修复校验.</li> 
 <li>fixBug自定义邮件服务器未生效</li> 
 <li>邮件页面优化，fix告警级别未转译</li> 
 <li>fix监控删除后告警定义关联未删除</li> 
 <li>调整jvm启动内存大小,fixOOM</li> 
 <li>fixbug重启后状态异常监控无法触发恢复告警</li> 
 <li>fix pmd error</li> 
 <li>bugfix告警设置确定后异常,按钮还在旋转</li> 
 <li>fix多余租户ID依赖</li> 
 <li>fix receiver的email类型错误，调整弹出框大小</li> 
 <li>fixbug告警定义关联监控不存在时异常</li> 
</ol> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">欢迎在线试用<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fconsole.tancloud.cn" target="_blank">https://console.tancloud.cn</a></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">版本升级注意⚠️</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">1.0-beta2升级上来，MYSQL的数据库需执行。<br> ALTER TABLE alert_define_monitor_bind DROP monitor_name;</p> 
<p style="color:#40485b; margin-left:0em; margin-right:0em; text-align:start">1.0-beta2,1.0-beta3升级上来，MYSQL的数据库需执行。<br> ALTER TABLE notice_receiver ADD access_token varchar(255);</p> 
<p>-----------------------</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fusthe%2Fhertzbeat" target="_blank">HertzBeat赫兹节拍</a><span> </span>是由<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftancloud.cn%2F" target="_blank">TanCloud</a>开源的一个支持网站，API，PING，端口，数据库等监控类型，拥有易用友好的可视化操作界面的开源监控告警项目。<br> 我们也提供了对应的<span> </span><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fconsole.tancloud.cn%2F" target="_blank">SAAS版本监控云</a></strong>，中小团队和个人无需再为了监控自己的网站资源，而去部署一套繁琐的监控系统，<strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fconsole.tancloud.cn%2F" target="_blank">登陆即可免费开始</a></strong>。<br> HertzBeat 支持<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhertzbeat.com%2Fdocs%2Fadvanced%2Fextend-point" target="_blank">自定义监控</a><span> </span>,只用通过配置YML文件我们就可以自定义需要的监控类型和指标，来满足常见的个性化需求。<br> HertzBeat 模块化，<code>manager, collector, scheduler, warehouse, alerter</code><span> </span>各个模块解耦合，方便理解与定制开发。<br> HertzBeat 支持更自由化的告警配置(计算表达式)，支持告警通知，告警模版<br> 欢迎登陆 HertzBeat 的<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fconsole.tancloud.cn%2F" target="_blank">云环境TanCloud</a><span> </span>试用发现更多。<br> 我们正在快速迭代中，欢迎参与加入一起共建项目开源生态。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><code>HertzBeat</code>的多类型支持，易扩展，低耦合，希望能帮助开发者和中小团队快速搭建自有监控系统。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><iframe frameborder="0" height="600px" scrolling="no" src="https://player.bilibili.com/player.html?aid=551403148&bvid=BV1Vi4y1f7i8&cid=504787541&page=1" style="box-sizing: inherit; color: rgb(51, 51, 51); font-family: -apple-system, "system-ui", "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;" width="800px"></iframe></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/dromara/hertzbeat">GITEE仓库</a>  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdromara%2Fhertzbeat" target="_blank">GITHUB仓库</a> 觉得还行给个star哦，感谢</p>
                                        </div>
                                      
</div>
            