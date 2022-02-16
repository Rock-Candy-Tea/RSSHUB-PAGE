
---
title: 'HertzBea t赫兹节拍 v1.0.beta.3 发布，易用友好的高性能监控告警系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3822'
author: 开源中国
comments: false
date: Wed, 16 Feb 2022 18:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3822'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">HertzBeat 赫兹节拍. </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#40485b">网站监测，PING连通性，端口可用性，数据库监控，API监控，全站监控，自定义监控，阈值告警，告警通知。</span></p> 
<div style="text-align:left"> 
 <p style="margin-left:0; margin-right:0"><strong>官网:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhertzbeat.com%2F" target="_blank">hertzbeat.com</a><span> </span>|<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftancloud.cn%2F" target="_blank">tancloud.cn</a></strong></p> 
</div> 
<p style="color:#40485b; margin-left:0em; margin-right:0em; text-align:start">特性：</p> 
<ol> 
 <li>API监控支持POST请求BODY内容，自定义Content-Type 由@random-chat贡献thanks</li> 
 <li>新增全站监控类型，支持网站地图sitemap的形式对全站的所用网页进行监控 感谢 庞 的需求和测试支持</li> 
 <li>调整API监控参数易用性</li> 
 <li>文档更新。</li> 
</ol> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">BUG修复</p> 
<ol> 
 <li>bugfix某些情况账户密码加密解析失败<span> </span><a href="https://gitee.com/dromara/hertzbeat/issues/I4TG2E">#I4TG2E:BUG：某些情况账户密码加密解析失败</a></li> 
 <li>修复安装包启动脚本</li> 
 <li>fix多余租户ID依赖,删除多余表字段</li> 
 <li>fix多行数据入库tdengine覆盖问题</li> 
</ol> 
<p style="color:#40485b; margin-left:0em; margin-right:0em; text-align:start">欢迎在线试用<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fconsole.tancloud.cn" target="_blank">https://console.tancloud.cn</a></p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fusthe%2Fhertzbeat" target="_blank">HertzBeat赫兹节拍</a><span> </span>是由<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftancloud.cn%2F" target="_blank">TanCloud</a>开源的一个支持网站，API，PING，端口，数据库等监控类型，拥有易用友好的可视化操作界面的开源监控告警项目。<br> 我们也提供了对应的<span> </span><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fconsole.tancloud.cn%2F" target="_blank">SAAS版本监控云</a></strong>，中小团队和个人无需再为了监控自己的网站资源，而去部署一套繁琐的监控系统，<strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fconsole.tancloud.cn%2F" target="_blank">登陆即可免费开始</a></strong>。<br> HertzBeat 支持<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhertzbeat.com%2Fdocs%2Fadvanced%2Fextend-point" target="_blank">自定义监控</a><span> </span>,只用通过配置YML文件我们就可以自定义需要的监控类型和指标，来满足常见的个性化需求。<br> HertzBeat 模块化，<code>manager, collector, scheduler, warehouse, alerter</code><span> </span>各个模块解耦合，方便理解与定制开发。<br> HertzBeat 支持更自由化的告警配置(计算表达式)，支持告警通知，告警模版<br> 欢迎登陆 HertzBeat 的<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fconsole.tancloud.cn%2F" target="_blank">云环境TanCloud</a><span> </span>试用发现更多。<br> 我们正在快速迭代中，欢迎参与加入一起共建项目开源生态。</p> 
 <p style="margin-left:0; margin-right:0"><code>HertzBeat</code>的多类型支持，易扩展，低耦合，希望能帮助开发者和中小团队快速搭建自有监控系统。</p> 
</blockquote> 
<p><iframe frameborder="0" height="600px" scrolling="no" src="https://player.bilibili.com/player.html?aid=551403148&bvid=BV1Vi4y1f7i8&cid=504787541&page=1" style="box-sizing: inherit; color: rgb(51, 51, 51); font-family: -apple-system, "system-ui", "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Helvetica Neue", Helvetica, Arial, sans-serif; font-size: 16px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: left; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;" width="800px"></iframe></p> 
<hr> 
<p> </p>
                                        </div>
                                      
</div>
            