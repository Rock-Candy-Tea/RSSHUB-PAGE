
---
title: 'HertzBeat v1.0.beta.7 发布，易用友好的云监控系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://images.gitee.com/uploads/images/2022/0407/213357_fde6fcbc_1767651.png'
author: 开源中国
comments: false
date: Fri, 08 Apr 2022 08:24:00 GMT
thumbnail: 'https://images.gitee.com/uploads/images/2022/0407/213357_fde6fcbc_1767651.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fdromara%2Fhertzbeat">HertzBeat赫兹跳动</a><span style="background-color:#ffffff; color:#6a737d"><span> </span>是由</span><a href="https://gitee.com/link?target=https%3A%2F%2Fdromara.org">Dromara</a><span style="background-color:#ffffff; color:#6a737d">孵化，</span><a href="https://gitee.com/link?target=https%3A%2F%2Ftancloud.cn">TanCloud</a><span style="background-color:#ffffff; color:#6a737d">开源的一个支持网站，API，PING，端口，数据库，全站，操作系统等监控类型，支持</span><span style="background-color:#ffffff; color:#40485b">阈值告警，告警通知(</span><span style="background-color:#efefef; color:#1c1e21">邮箱，webhook，钉钉，企业微信，飞书机器人</span><span style="background-color:#ffffff; color:#40485b">)</span><span style="background-color:#ffffff; color:#6a737d">，拥有易用友好的可视化操作界面的开源监控告警项目。</span>   </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#333333">官网:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhertzbeat.com%2F" target="_blank">hertzbeat.com</a><span> </span>|<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftancloud.cn%2F" target="_blank">tancloud.cn</a></strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start"><span style="background-color:#ffffff; color:#40485b">这个版本看这么多feature，其实简单来说主要是这几个，支持了ORACLE数据库的监控，包括ORACLE的基本信息，表空间，连接数，TPS，QPS等指标，支持了LINUX的CPU利用率，内存利用率，磁盘占用相关指标，使LINUX监控贴合实际业务，还有前端参数支持了KEY-VALUE，以后我们就可以在页面上配置HTTP Headers等类似参数了，还有就是参数配置那优化改版，把非常用告警参数隐藏起来了，稍微好看些，然后支持了windows下bat启动脚本，更多的就是稳定性的提升和一些其它的小修复小需求啦！</span></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start"> </p> 
<div style="text-align:start"> 
 <p style="color:#1c1e21; margin-left:0; margin-right:0; text-align:start">版本特性：</p> 
 <ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
  <li>feature 支持oracle数据库监控类型-xgf 由<span> </span><span style="background-color:#ffffff; color:#40485b">@gf-8</span><a href="https://gitee.com/xgf">  </a><span>贡献 thanks</span></li> 
  <li>feature oracle监控支持tablespace,连接数,qps,tps等指标</li> 
  <li>feature linux监控支持设置超时时间 (#49)</li> 
  <li>feature 检测网站SSL证书是否过期 (#50) 由<span> </span><a href="https://gitee.com/weihongbin">@魏宏斌<span> </span></a>提出 thanks</li> 
  <li>feature 页面配置参数支持KEY-VALUE数组(#57)</li> 
  <li>feature API和网站监控支持页面配置Headers和Params (#58)(#59)</li> 
  <li>feature API和网站监控支持页面配置 basic auth, digest auth (#60)</li> 
  <li>feature http 端口跟随SSL是否启用变更443或80 (#61)</li> 
  <li>feature 修改默认超时时间3000毫秒为6000毫秒 (#55)</li> 
  <li>feature:make tdengine optional, not required (#62)</li> 
  <li>feature:support win bat service (#65)</li> 
  <li>feature:support hide advanced params define (#68)</li> 
  <li>feature:enable auto redirect when 301 302 http code (#69)</li> 
  <li>feature:only collect available metrics when detect (#70)</li> 
  <li>feature:[website api]monitor support keyword match (#72)</li> 
  <li>feature:support linux cpu usage,memory usage,disk free (#76)</li> 
 </ol> 
 <p style="color:#1c1e21; margin-left:0; margin-right:0; text-align:start">BUG修复</p> 
 <ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
  <li>添加sqlserver关联文档，fix connection指标入库tdengine失败 (#41)</li> 
  <li>使用docker部署TDengine，开放tcp访问端口<a href="https://gitee.com/dromara/hertzbeat/pulls/16">!16:使用docker部署TDengine，开放tcp访问端口</a><span> </span>由<span> </span><a href="https://gitee.com/m8oo_admin">@老姜bei<span> </span></a>贡献 thanks</li> 
  <li>补充sureness配置文档 避免误配导致权限异常</li> 
  <li>bugfix:monitors always timeout alert (#67)</li> 
  <li>code format and optimization 由<span> </span><a href="https://gitee.com/learning-code">@学习代码的小白<span> </span></a>贡献 thanks</li> 
  <li>bugfix: remove oracle field - database_type due 11g not support 由<span> </span><a href="https://gitee.com/syongaaa">@常清静矣<span> </span></a>贡献 thanks</li> 
  <li>bugfix:fix linux interface metrics no instance (#75)</li> 
 </ol> 
 <p style="margin-left:0; margin-right:0">欢迎在线试用<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fconsole.tancloud.cn" target="_blank">https://console.tancloud.cn</a></p> 
 <p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">优化后的参数输入界面:<br> <img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2022/0407/213357_fde6fcbc_1767651.png" referrerpolicy="no-referrer"></p> 
 <p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">Linux新增指标:<br> <img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2022/0407/213742_ee1f0f05_1767651.png" referrerpolicy="no-referrer"></p> 
 <p style="color:#40485b; margin-left:0em; margin-right:0em; text-align:start">ORACLE监控:<br> 哦豁！oracle环境不在了，之前没有截图，先脑补一张！</p> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">-----------------------</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fusthe%2Fhertzbeat" target="_blank">HertzBeat赫兹节拍</a><span> </span>是由<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftancloud.cn%2F" target="_blank">TanCloud</a>开源的一个支持网站，API，PING，端口，数据库等监控类型，拥有易用友好的可视化操作界面的开源监控告警项目。<br> 我们也提供了对应的<span> </span><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fconsole.tancloud.cn%2F" target="_blank">SAAS版本监控云</a></strong>，中小团队和个人无需再为了监控自己的网站资源，而去部署一套繁琐的监控系统，<strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fconsole.tancloud.cn%2F" target="_blank">登陆即可免费开始</a></strong>。<br> HertzBeat 支持<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhertzbeat.com%2Fdocs%2Fadvanced%2Fextend-point" target="_blank">自定义监控</a><span> </span>,只用通过配置YML文件我们就可以自定义需要的监控类型和指标，来满足常见的个性化需求。<br> HertzBeat 模块化，<code>manager, collector, scheduler, warehouse, alerter</code><span> </span>各个模块解耦合，方便理解与定制开发。<br> HertzBeat 支持更自由化的告警配置(计算表达式)，支持告警通知，告警模版<br> 欢迎登陆 HertzBeat 的<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fconsole.tancloud.cn%2F" target="_blank">云环境TanCloud</a><span> </span>试用发现更多。<br> 我们正在快速迭代中，欢迎参与加入一起共建项目开源生态。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><code>HertzBeat</code>的多类型支持，易扩展，低耦合，希望能帮助开发者和中小团队快速搭建自有监控系统。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/dromara/hertzbeat" target="_blank">Gitee</a><span> </span><a href="https://gitee.com/dromara/hertzbeat" target="_blank">https://gitee.com/dromara/hertzbeat</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdromara%2Fhertzbeat" target="_blank">Github</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdromara%2Fhertzbeat" target="_blank">https://github.com/dromara/hertzbeat</a></p> 
<p style="color:#1c1e21; margin-left:0; margin-right:0; text-align:start">看到这里不妨给个Star支持下哦，灰常感谢，弯腰!</p> 
<p> </p>
                                        </div>
                                      
</div>
            