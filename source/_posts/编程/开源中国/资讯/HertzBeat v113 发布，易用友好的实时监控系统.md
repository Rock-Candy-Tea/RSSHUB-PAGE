
---
title: 'HertzBeat v1.1.3 发布，易用友好的实时监控系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-de2ad8c3cb108b9be85c277eda1296559c0.png'
author: 开源中国
comments: false
date: Thu, 08 Sep 2022 08:47:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-de2ad8c3cb108b9be85c277eda1296559c0.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:black; margin-left:0; margin-right:0; text-align:left"><strong style="color:black">官网:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhertzbeat.com" target="_blank">hertzbeat.com</a><span> </span>|<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftancloud.cn" target="_blank">tancloud.cn</a></strong></p> 
<p style="color:black; margin-left:0; margin-right:0; text-align:left">大家早上好，监控告警系统 HertzBeat v1.1.3 发布啦！<span style="background-color:#ffffff; color:#40485b">这个版本支持了apache kafka监控，SSL证书过期监控等。修复了若干bug，提升整体稳定性。</span></p> 
<p style="color:black; margin-left:0; margin-right:0; text-align:left">只需要一条 docker 命令即可安装体验 heartbeat ：<br> <code>docker run -d -p 1157:1157 --name hertzbeat tancloud/hertzbeat</code></p> 
<p style="color:black; margin-left:0; margin-right:0; text-align:left">花一分钟快来试试吧。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img height="1712" src="https://oscimg.oschina.net/oscnet/up-de2ad8c3cb108b9be85c277eda1296559c0.png" width="3840" referrerpolicy="no-referrer"></p> 
<p style="color:black; margin-left:0; margin-right:0; text-align:left">感谢 hertzbeat 贡献者们的贡献！👍👍</p> 
<p style="color:black; margin-left:0; margin-right:0; text-align:left">特性：</p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>[web-app]feature: 优化UI布局，支持 host 点击复制按钮 #260</li> 
 <li>[monitor] feature: 支持apache kafak 应用类型监控 #263<span> </span>contribute by @wang1027-wqh</li> 
 <li>[webapp] 支持历史图片查询历史最大3个月回溯时间范围 #265<span> </span>issue by @ericfrol</li> 
 <li>[monitor] 支持网站SSL证书有效期可用性监控 #266<span> </span>suggest by @noear</li> 
 <li>[web-app] 将默认新增监控的采集周期时间从600秒变更为120秒 #268</li> 
 <li>[web-app] 优化UI页面，帮助文档按钮，菜单栏等 #272</li> 
 <li>[alert,webapp] 告警中心告警支持一键清空功能 #273<span> </span>issue by @ericfrol</li> 
 <li>[web-app] 设计更新登记界面背景UI #276</li> 
</ol> 
<p style="color:black; margin-left:0; margin-right:0; text-align:left">BUG 修复.</p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>[docs] 修复自定义监控jsonpath样例文档错误 #262<span> </span>contribute by @woshiniusange .</li> 
 <li>[monitor] 变更redis数据库监控指标组名称，更新帮助文档 #264</li> 
 <li>[manager] bugfix 修复当标签key不为空，值为空时告警中心标签不展示问题 #270<span> </span>issue by<span> </span><a href="https://gitee.com/hello_brother_niu">@你好牛三哥</a></li> 
 <li>[alert] bugfix: 修复告警阈值全局默认参数不生效问题 #275<span> </span>issue by<span> </span><a href="https://gitee.com/hello_brother_niu">@你好牛三哥</a></li> 
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
            