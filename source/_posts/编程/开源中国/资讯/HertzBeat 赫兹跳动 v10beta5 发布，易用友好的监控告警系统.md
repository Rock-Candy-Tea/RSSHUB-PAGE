
---
title: 'HertzBeat 赫兹跳动 v1.0.beta.5 发布，易用友好的监控告警系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://images.gitee.com/uploads/images/2022/0309/224038_90957bee_1767651.png'
author: 开源中国
comments: false
date: Thu, 10 Mar 2022 09:02:00 GMT
thumbnail: 'https://images.gitee.com/uploads/images/2022/0309/224038_90957bee_1767651.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fdromara%2Fhertzbeat">HertzBeat赫兹跳动</a><span style="background-color:#ffffff; color:#6a737d"><span> </span>是由</span><a href="https://gitee.com/link?target=https%3A%2F%2Fdromara.org">Dromara</a><span style="background-color:#ffffff; color:#6a737d">孵化，</span><a href="https://gitee.com/link?target=https%3A%2F%2Ftancloud.cn">TanCloud</a><span style="background-color:#ffffff; color:#6a737d">开源的一个支持网站，API，PING，端口，数据库，全站等监控类型，支持</span><span style="background-color:#ffffff; color:#40485b">阈值告警，告警通知(</span><span style="background-color:#efefef; color:#1c1e21">邮箱，webhook，钉钉，企业微信，飞书机器人</span><span style="background-color:#ffffff; color:#40485b">)</span><span style="background-color:#ffffff; color:#6a737d">，拥有易用友好的可视化操作界面的开源监控告警项目。</span>   </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#333333">官网:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhertzbeat.com%2F" target="_blank">hertzbeat.com</a><span> </span>|<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftancloud.cn%2F" target="_blank">tancloud.cn</a></strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">此升级版本包含了dashborad仪表盘重新设计，阈值表达式支持多指标，丰富了数据库监控类型，新增mariaDB和postgreSQL数据库的监控，控制台页面新增帮助文档等，欢迎使用。</p> 
<div style="text-align:start"> 
 <p style="margin-left:0em; margin-right:0em">特性：</p> 
 <ol> 
  <li>feature 支持mariadb监控类型 (#11)</li> 
  <li>feature dashboard仪表盘重构 (#13)</li> 
  <li>feature 告警配置支持多指标集合<span> </span><span> </span>由<span> </span><a href="https://gitee.com/pengliren">@pengliren<span> </span></a>提出 thanks</li> 
  <li>feature 支持postgresql数据库的监控 (#16)</li> 
  <li>新增监控默认开启探测.</li> 
  <li>新增mysql采集指标.</li> 
  <li>新增监控大类别，支持自定义监控页面菜单自动渲染</li> 
  <li>操作页面新增帮助链接，完善自定义和阈值帮助文档</li> 
  <li>feat: 模拟浏览器设置为chrome浏览器 #Issues 14 由<a href="https://gitee.com/learning-code">@学习代码的小白<span> </span></a>贡献 thanks</li> 
 </ol> 
 <p style="margin-left:0; margin-right:0">BUG修复</p> 
 <ol> 
  <li>登陆改登录，傻傻分不清.</li> 
  <li>文档新增常见问题，采集器http参数优化校验.</li> 
  <li>采集器调度第0优先级失败则取消后续的优化.</li> 
  <li>bugfix website monitor path Illegal character in path at index</li> 
  <li>bugfix深色主题适配问题 (#10)</li> 
  <li>fix国际化异常 放开hierarchy接口认证保护</li> 
 </ol> 
 <p style="margin-left:0; margin-right:0">欢迎在线试用<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fconsole.tancloud.cn" target="_blank">https://console.tancloud.cn</a></p> 
 <p style="margin-left:0; margin-right:0">新的dashboard:<br> <img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2022/0309/224038_90957bee_1767651.png" referrerpolicy="no-referrer"></p> 
 <p style="margin-left:0; margin-right:0">告警阈值配置支持多指标表达式:<br> <img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2022/0309/224120_af4173f7_1767651.png" referrerpolicy="no-referrer"></p> 
 <p style="margin-left:0em; margin-right:0em">新增mariaDB和postgreSQL数据库监控类型，欢迎体验！</p> 
</div> 
<p> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">-----------------------</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fusthe%2Fhertzbeat" target="_blank">HertzBeat赫兹节拍</a><span> </span>是由<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftancloud.cn%2F" target="_blank">TanCloud</a>开源的一个支持网站，API，PING，端口，数据库等监控类型，拥有易用友好的可视化操作界面的开源监控告警项目。<br> 我们也提供了对应的<span> </span><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fconsole.tancloud.cn%2F" target="_blank">SAAS版本监控云</a></strong>，中小团队和个人无需再为了监控自己的网站资源，而去部署一套繁琐的监控系统，<strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fconsole.tancloud.cn%2F" target="_blank">登陆即可免费开始</a></strong>。<br> HertzBeat 支持<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhertzbeat.com%2Fdocs%2Fadvanced%2Fextend-point" target="_blank">自定义监控</a><span> </span>,只用通过配置YML文件我们就可以自定义需要的监控类型和指标，来满足常见的个性化需求。<br> HertzBeat 模块化，<code>manager, collector, scheduler, warehouse, alerter</code><span> </span>各个模块解耦合，方便理解与定制开发。<br> HertzBeat 支持更自由化的告警配置(计算表达式)，支持告警通知，告警模版<br> 欢迎登陆 HertzBeat 的<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fconsole.tancloud.cn%2F" target="_blank">云环境TanCloud</a><span> </span>试用发现更多。<br> 我们正在快速迭代中，欢迎参与加入一起共建项目开源生态。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><code>HertzBeat</code>的多类型支持，易扩展，低耦合，希望能帮助开发者和中小团队快速搭建自有监控系统。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><iframe frameborder="0" height="600px" scrolling="no" src="https://player.bilibili.com/player.html?aid=551403148&bvid=BV1Vi4y1f7i8&cid=504787541&page=1" style="box-sizing: inherit; color: rgb(51, 51, 51); font-family: -apple-system, "system-ui", "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;" width="800px"></iframe></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/dromara/hertzbeat">GITEE仓库</a> <span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdromara%2Fhertzbeat" target="_blank">GITHUB仓库</a> 觉得还行给个star哦，感谢</p>
                                        </div>
                                      
</div>
            