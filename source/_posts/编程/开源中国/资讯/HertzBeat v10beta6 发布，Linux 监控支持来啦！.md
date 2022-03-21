
---
title: 'HertzBeat v1.0.beta.6 发布，Linux 监控支持来啦！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://images.gitee.com/uploads/images/2022/0320/144158_03e1ec56_1767651.png'
author: 开源中国
comments: false
date: Mon, 21 Mar 2022 08:16:00 GMT
thumbnail: 'https://images.gitee.com/uploads/images/2022/0320/144158_03e1ec56_1767651.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fdromara%2Fhertzbeat">HertzBeat赫兹跳动</a><span style="background-color:#ffffff; color:#6a737d"><span> </span>是由</span><a href="https://gitee.com/link?target=https%3A%2F%2Fdromara.org">Dromara</a><span style="background-color:#ffffff; color:#6a737d">孵化，</span><a href="https://gitee.com/link?target=https%3A%2F%2Ftancloud.cn">TanCloud</a><span style="background-color:#ffffff; color:#6a737d">开源的一个支持网站，API，PING，端口，数据库，全站，操作系统等监控类型，支持</span><span style="background-color:#ffffff; color:#40485b">阈值告警，告警通知(</span><span style="background-color:#efefef; color:#1c1e21">邮箱，webhook，钉钉，企业微信，飞书机器人</span><span style="background-color:#ffffff; color:#40485b">)</span><span style="background-color:#ffffff; color:#6a737d">，拥有易用友好的可视化操作界面的开源监控告警项目。</span>   </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#333333">官网:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhertzbeat.com%2F" target="_blank">hertzbeat.com</a><span> </span>|<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftancloud.cn%2F" target="_blank">tancloud.cn</a></strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start"><span style="background-color:#fafafa; color:#1c1e21">此升级版本包含了很多同学需要的Linux操作系统监控支持，支持其CPU，内存，磁盘，网络等指标，重要的是同步支持了SSH自定义，我们可以很方便的写shell脚本监控我们想要的Linux指标，也新增了对主流的数据库SqlServer监控支持等，更多功能欢迎使用。</span></p> 
<div style="text-align:start"> 
 <p style="color:#1c1e21; text-align:start">版本特性：</p> 
 <ol style="margin-left:0; margin-right:0"> 
  <li>feature 新增支持Linux操作系统监控类型(支持CPU内存磁盘网卡等监控指标) (#20)</li> 
  <li>feature 新增支持microsoft sqlserver数据库监控类型 (#37)</li> 
  <li>feature 添加docker-compose部署方案 (#27) 由 @jx10086 贡献 thanks</li> 
  <li>feature 监控列表支持状态过滤和字段搜索功能 (#29)</li> 
  <li>feature 新增mysql,postgresql等数据库查询超时时间设置 (#18) 由 @学习代码的小白 贡献</li> 
  <li>[纳管]修改为[监控]表述,[探测]修改为[测试]表述</li> 
  <li>feature add github build and translate action (#22)</li> 
  <li>feature 新增贡献指南，本地代码启动文档</li> 
  <li>docs 指定mysql和tdengine版本，避免环境问题</li> 
 </ol> 
 <p style="color:#1c1e21; text-align:start">BUG修复</p> 
 <ol style="margin-left:0; margin-right:0"> 
  <li>fix 由于链接复用不佳造成创建过多链接监控异常 (#26)</li> 
  <li>fix 页面全局监控搜索结果异常 (#28) issue by @Suremotoo</li> 
  <li>代码优化 #I4U9BT 由 @学习代码的小白 贡献</li> 
  <li>fix 服务启动脚本偶现端口占用误判问题</li> 
  <li>时间本地时区格式化 (#35)</li> 
  <li>fix 此版本引入问题jdbc解析异常 (#36)</li> 
  <li>fix jdbc并发注册加载时由于spi机制加载死锁问题 (#40)</li> 
 </ol> 
 <p> </p> 
 <p style="margin-left:0; margin-right:0">欢迎在线试用<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fconsole.tancloud.cn" target="_blank">https://console.tancloud.cn</a></p> 
 <p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">Linux操作系统监控:<br> <img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2022/0320/144158_03e1ec56_1767651.png" referrerpolicy="no-referrer"><br> <img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2022/0320/144226_27b2509c_1767651.png" referrerpolicy="no-referrer"></p> 
 <p style="color:#40485b; margin-left:0em; margin-right:0em; text-align:start">SqlServer数据库监控:<br> <img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2022/0320/144251_e1ed4ba9_1767651.png" referrerpolicy="no-referrer"></p> 
 <p> </p> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">-----------------------</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fusthe%2Fhertzbeat" target="_blank">HertzBeat赫兹节拍</a><span> </span>是由<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftancloud.cn%2F" target="_blank">TanCloud</a>开源的一个支持网站，API，PING，端口，数据库等监控类型，拥有易用友好的可视化操作界面的开源监控告警项目。<br> 我们也提供了对应的<span> </span><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fconsole.tancloud.cn%2F" target="_blank">SAAS版本监控云</a></strong>，中小团队和个人无需再为了监控自己的网站资源，而去部署一套繁琐的监控系统，<strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fconsole.tancloud.cn%2F" target="_blank">登陆即可免费开始</a></strong>。<br> HertzBeat 支持<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhertzbeat.com%2Fdocs%2Fadvanced%2Fextend-point" target="_blank">自定义监控</a><span> </span>,只用通过配置YML文件我们就可以自定义需要的监控类型和指标，来满足常见的个性化需求。<br> HertzBeat 模块化，<code>manager, collector, scheduler, warehouse, alerter</code><span> </span>各个模块解耦合，方便理解与定制开发。<br> HertzBeat 支持更自由化的告警配置(计算表达式)，支持告警通知，告警模版<br> 欢迎登陆 HertzBeat 的<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fconsole.tancloud.cn%2F" target="_blank">云环境TanCloud</a><span> </span>试用发现更多。<br> 我们正在快速迭代中，欢迎参与加入一起共建项目开源生态。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><code>HertzBeat</code>的多类型支持，易扩展，低耦合，希望能帮助开发者和中小团队快速搭建自有监控系统。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><iframe frameborder="0" height="600px" scrolling="no" src="https://player.bilibili.com/player.html?aid=551403148&bvid=BV1Vi4y1f7i8&cid=504787541&page=1" style="box-sizing: inherit; color: rgb(51, 51, 51); font-family: -apple-system, "system-ui", "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;" width="800px"></iframe></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/dromara/hertzbeat" target="_blank">Gitee</a><span> </span><a href="https://gitee.com/dromara/hertzbeat" target="_blank">https://gitee.com/dromara/hertzbeat</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdromara%2Fhertzbeat" target="_blank">Github</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdromara%2Fhertzbeat" target="_blank">https://github.com/dromara/hertzbeat</a></p> 
<p style="color:#1c1e21; text-align:start">看到这里不妨给个Star哦，灰常感谢，弯腰!!</p>
                                        </div>
                                      
</div>
            