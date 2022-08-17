
---
title: 'HertzBeat v1.1.2 发布，易用友好的云监控系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-de2ad8c3cb108b9be85c277eda1296559c0.png'
author: 开源中国
comments: false
date: Wed, 17 Aug 2022 00:29:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-de2ad8c3cb108b9be85c277eda1296559c0.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:black; margin-left:0; margin-right:0; text-align:left"><strong style="color:black">官网:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhertzbeat.com" target="_blank">hertzbeat.com</a><span> </span>|<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftancloud.cn" target="_blank">tancloud.cn</a></strong></p> 
<p style="color:black; margin-left:0; margin-right:0; text-align:left">大家早上好，监控告警系统 HertzBeat v1.1.2发布啦！<span style="background-color:#ffffff; color:#40485b">这个版本带来了自定义监控JMX协议，支持tomcat,JVM监控和Flink监控，翻译了用户英文文档。修复了若干bug，提升整体稳定性。</span></p> 
<p style="color:black; margin-left:0; margin-right:0; text-align:left">只需要一条 docker 命令即可安装体验 heartbeat ：<br> <code>docker run -d -p 1157:1157 --name hertzbeat tancloud/hertzbeat</code></p> 
<p style="color:black; margin-left:0; margin-right:0; text-align:left">花一分钟快来试试吧。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img height="1712" src="https://oscimg.oschina.net/oscnet/up-de2ad8c3cb108b9be85c277eda1296559c0.png" width="3840" referrerpolicy="no-referrer"></p> 
<p style="color:black; margin-left:0; margin-right:0; text-align:left">感谢 hertzbeat 贡献者们的贡献！👍👍</p> 
<p style="color:black; margin-left:0; margin-right:0; text-align:left">特性：</p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>[[home,docs] 支持中英文文档全同步 #226] contribute by @DreamGirl524</li> 
 <li>[[web-app,home]新增 install yarn lock，避免本地启动问题 #230].</li> 
 <li>[[common]支持env LANG来设置中英文切换 #231].</li> 
 <li>[Feature 新增 jmx 采集协议，支持tomcat应用服务器监控 #232] contribute by @wang1027-wqh</li> 
 <li>[[monitor]默认系统语言设置为en #233].</li> 
 <li>[Adding all files apache license #234] contribute by<span> </span>@Oyiyou</li> 
 <li>[[monitor] 支持 apache flink 监控 #240] contribute by @cuipiheqiuqiu</li> 
 <li>[[monitor] 支持http协议监控个性化设置超时时间 #241]</li> 
 <li>[[manager]支持 JVM 虚拟机监控 #249]</li> 
</ol> 
<p style="color:black; margin-left:0; margin-right:0; text-align:left">BUG 修复.</p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>[[home] 修复文档 mysql-init spring.datasource.url #225] contribute by<span> </span>@liuyang<span> </span>.</li> 
 <li>[Doc#修复文档 对参数国际化名称修复 #199] contribute by<span> </span>@dowell</li> 
 <li>[[collector] bugfix:  解决周期性任务调度时间超时10秒的问题. #246] contribute by @cuipiheqiuqiu .</li> 
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
            