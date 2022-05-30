
---
title: '云监控系统 HertzBeat v1.0 正式发布啦'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://avatars.githubusercontent.com/u/24788200?v=4?s=100'
author: 开源中国
comments: false
date: Mon, 30 May 2022 09:30:00 GMT
thumbnail: 'https://avatars.githubusercontent.com/u/24788200?v=4?s=100'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fdromara%2Fhertzbeat">HertzBeat 赫兹跳动</a><span style="background-color:#ffffff; color:#6a737d"><span> </span>是由<span> </span></span><a href="https://gitee.com/link?target=https%3A%2F%2Fdromara.org">Dromara</a><span style="background-color:#ffffff; color:#6a737d"><span> </span>孵化，</span><a href="https://gitee.com/link?target=https%3A%2F%2Ftancloud.cn">TanCloud</a><span style="background-color:#ffffff; color:#6a737d"><span> </span>开源的一个支持网站，API，PING，端口，数据库，全站，操作系统，中间件等监控类型，支持</span><span style="background-color:#ffffff; color:#40485b">阈值告警，告警通知 (</span><span style="background-color:#efefef; color:#1c1e21">邮箱，webhook，钉钉，企业微信，飞书机器人</span><span style="background-color:#ffffff; color:#40485b">)</span><span style="background-color:#ffffff; color:#6a737d">，拥有易用友好的可视化操作界面的开源监控告警项目。</span>   </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#333333">官网:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhertzbeat.com%2F" target="_blank">hertzbeat.com</a><span> </span>|<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftancloud.cn%2F" target="_blank">tancloud.cn</a></strong></p> 
<div style="text-align:start"> 
 <p style="margin-left:0; margin-right:0">从v1.0-beta.1到v1.0-beat.8，经过多个版本的迭代完善，我们很高兴宣布hertzbeat v1.0正式发布。强烈建议升级使用此版本。</p> 
 <p style="margin-left:0; margin-right:0">感谢从beat.1版本以来 HertzBeat Contributors 的贡献，社区同学和用户们的支持。 此版本更新支持了Redis的监控( @gcdd1993 贡献)，覆盖Redis的内存CPU等各个性能指标，全方面监控Redis。修复了多个bug进一步增强稳定性。</p> 
 <table cellspacing="0" style="border-collapse:collapse; border-spacing:0px; box-sizing:border-box; display:block; margin-bottom:16px; margin-top:0px; overflow:auto; width:879.203px; word-break:initial"> 
  <tbody> 
   <tr> 
    <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Ftomsun28" target="_blank"><img alt src="https://avatars.githubusercontent.com/u/24788200?v=4?s=100" width="100px;" referrerpolicy="no-referrer"><br> <strong>tomsun28</strong></a><br> <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Ftomsun28%2Fhertzbeat%2Fcommits%3Fauthor%3Dtomsun28" target="_blank">💻</a><span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Ftomsun28%2Fhertzbeat%2Fcommits%3Fauthor%3Dtomsun28" target="_blank">📖</a><span> </span><a href="https://gitee.com/dromara/hertzbeat/releases/v1.0#design-tomsun28">🎨</a></td> 
    <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fwang1027-wqh" target="_blank"><img alt src="https://avatars.githubusercontent.com/u/71161318?v=4?s=100" width="100px;" referrerpolicy="no-referrer"><br> <strong>会编程的王学长</strong></a><br> <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Ftomsun28%2Fhertzbeat%2Fcommits%3Fauthor%3Dwang1027-wqh" target="_blank">💻</a><span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Ftomsun28%2Fhertzbeat%2Fcommits%3Fauthor%3Dwang1027-wqh" target="_blank">📖</a><span> </span><a href="https://gitee.com/dromara/hertzbeat/releases/v1.0#design-wang1027-wqh">🎨</a></td> 
    <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><a href="https://gitee.com/link?target=https%3A%2F%2Fwww.maxkey.top%2F" target="_blank"><img alt src="https://avatars.githubusercontent.com/u/1563377?v=4?s=100" width="100px;" referrerpolicy="no-referrer"><br> <strong>MaxKey</strong></a><br> <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Ftomsun28%2Fhertzbeat%2Fcommits%3Fauthor%3Dshimingxy" target="_blank">💻</a><span> </span><a href="https://gitee.com/dromara/hertzbeat/releases/v1.0#design-shimingxy">🎨</a><span> </span><a href="https://gitee.com/dromara/hertzbeat/releases/v1.0#ideas-shimingxy">🤔</a></td> 
    <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><a href="https://gitee.com/link?target=https%3A%2F%2Fblog.gcdd.top%2F" target="_blank"><img alt src="https://avatars.githubusercontent.com/u/26523525?v=4?s=100" width="100px;" referrerpolicy="no-referrer"><br> <strong>观沧海</strong></a><br> <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Ftomsun28%2Fhertzbeat%2Fcommits%3Fauthor%3Dgcdd1993" target="_blank">💻</a><span> </span><a href="https://gitee.com/dromara/hertzbeat/releases/v1.0#design-gcdd1993">🎨</a><span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Ftomsun28%2Fhertzbeat%2Fissues%3Fq%3Dauthor%253Agcdd1993" target="_blank">🐛</a></td> 
    <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fa25017012" target="_blank"><img alt src="https://avatars.githubusercontent.com/u/32265356?v=4?s=100" width="100px;" referrerpolicy="no-referrer"><br> <strong>yuye</strong></a><br> <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Ftomsun28%2Fhertzbeat%2Fcommits%3Fauthor%3Da25017012" target="_blank">💻</a><span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Ftomsun28%2Fhertzbeat%2Fcommits%3Fauthor%3Da25017012" target="_blank">📖</a></td> 
    <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fjx10086" target="_blank"><img alt src="https://avatars.githubusercontent.com/u/5323228?v=4?s=100" width="100px;" referrerpolicy="no-referrer"><br> <strong>jx10086</strong></a><br> <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Ftomsun28%2Fhertzbeat%2Fcommits%3Fauthor%3Djx10086" target="_blank">💻</a><span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Ftomsun28%2Fhertzbeat%2Fissues%3Fq%3Dauthor%253Ajx10086" target="_blank">🐛</a></td> 
    <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2FwinnerTimer" target="_blank"><img alt src="https://avatars.githubusercontent.com/u/76024658?v=4?s=100" width="100px;" referrerpolicy="no-referrer"><br> <strong>winnerTimer</strong></a><br> <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Ftomsun28%2Fhertzbeat%2Fcommits%3Fauthor%3DwinnerTimer" target="_blank">💻</a><span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Ftomsun28%2Fhertzbeat%2Fissues%3Fq%3Dauthor%253AwinnerTimer" target="_blank">🐛</a></td> 
   </tr> 
   <tr> 
    <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fgoo-kits" target="_blank"><img alt src="https://avatars.githubusercontent.com/u/13163673?v=4?s=100" width="100px;" referrerpolicy="no-referrer"><br> <strong>goo-kits</strong></a><br> <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Ftomsun28%2Fhertzbeat%2Fcommits%3Fauthor%3Dgoo-kits" target="_blank">💻</a><span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Ftomsun28%2Fhertzbeat%2Fissues%3Fq%3Dauthor%253Agoo-kits" target="_blank">🐛</a></td> 
    <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fbrave4Time" target="_blank"><img alt src="https://avatars.githubusercontent.com/u/105094014?v=4?s=100" width="100px;" referrerpolicy="no-referrer"><br> <strong>brave4Time</strong></a><br> <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Ftomsun28%2Fhertzbeat%2Fcommits%3Fauthor%3Dbrave4Time" target="_blank">💻</a><span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Ftomsun28%2Fhertzbeat%2Fissues%3Fq%3Dauthor%253Abrave4Time" target="_blank">🐛</a></td> 
    <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fwalkerlee-lab" target="_blank"><img alt src="https://avatars.githubusercontent.com/u/8426753?v=4?s=100" width="100px;" referrerpolicy="no-referrer"><br> <strong>WalkerLee</strong></a><br> <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Ftomsun28%2Fhertzbeat%2Fcommits%3Fauthor%3Dwalkerlee-lab" target="_blank">💻</a><span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Ftomsun28%2Fhertzbeat%2Fissues%3Fq%3Dauthor%253Awalkerlee-lab" target="_blank">🐛</a></td> 
    <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Ffullofjoy" target="_blank"><img alt src="https://avatars.githubusercontent.com/u/30247571?v=4?s=100" width="100px;" referrerpolicy="no-referrer"><br> <strong>jianghang</strong></a><br> <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Ftomsun28%2Fhertzbeat%2Fcommits%3Fauthor%3Dfullofjoy" target="_blank">💻</a><span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Ftomsun28%2Fhertzbeat%2Fissues%3Fq%3Dauthor%253Afullofjoy" target="_blank">🐛</a></td> 
    <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2FChineseTony" target="_blank"><img alt src="https://avatars.githubusercontent.com/u/24618786?v=4?s=100" width="100px;" referrerpolicy="no-referrer"><br> <strong>ChineseTony</strong></a><br> <a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Ftomsun28%2Fhertzbeat%2Fcommits%3Fauthor%3DChineseTony" target="_blank">💻</a></td> 
   </tr> 
  </tbody> 
 </table> 
 <p style="margin-left:0; margin-right:0">特性：</p> 
 <ol> 
  <li><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fdromara%2Fhertzbeat%2Fpull%2F142" target="_blank">[monitor] feature:支持redis监控协议 #142</a>. contribute by @gcdd1993</li> 
  <li>Copyright & NOTICE contribute by @shimingxy</li> 
  <li><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fdromara%2Fhertzbeat%2Fpull%2F144" target="_blank">[alerter]bugfix: 支持系统告警设置触发次数 #144</a>.</li> 
  <li><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fdromara%2Fhertzbeat%2Fpull%2F146" target="_blank">[collector]feature: redis复用单连接 #146</a>.</li> 
  <li><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fdromara%2Fhertzbeat%2Fpull%2F159" target="_blank">[collector]隐藏日志中IP、账号与密码等敏感信息 #159</a><span> </span>idea from @goo-kits</li> 
  <li><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fdromara%2Fhertzbeat%2Fpull%2F137" target="_blank">支持 zookeeper 监控帮助文档 #137</a><span> </span>contributr by @wang1027-wqh</li> 
 </ol> 
 <p style="margin-left:0; margin-right:0">Bug修复.</p> 
 <ol> 
  <li><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fdromara%2Fhertzbeat%2Fpull%2F131" target="_blank">[monitor]bugfix: 修复resource bundle在en.HK加载资源错误问题 #131</a>.</li> 
  <li><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fdromara%2Fhertzbeat%2Fpull%2F132" target="_blank">[web-app]bugfix:修复当主题为dark时部分菜单不可见 #132</a>.</li> 
  <li><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fdromara%2Fhertzbeat%2Fpull%2F140" target="_blank">[monitor]bugfix: 修复通知策略过滤标签时只能选择一个 #140</a>. issue by @daqianxiaoyao</li> 
  <li><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fdromara%2Fhertzbeat%2Fpull%2F150" target="_blank">[td-engine store]bugfix: 修复tdengine入库指标数据时无table报错日志#150</a>. contribute by<span> </span><a href="https://gitee.com/33234567">@ChineseTony</a></li> 
  <li><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fdromara%2Fhertzbeat%2Fpull%2F153" target="_blank">[collector]bugfix: 修复 warehouse data queue 未消费异常 #153</a>. issue by @daqianxiaoyao</li> 
  <li><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fdromara%2Fhertzbeat%2Fpull%2F157" target="_blank">[web-app]bugfix: 修复黑暗主题时页面输入框校验出错时不可见 #157</a>. issue by @ConradWen</li> 
 </ol> 
 <p style="margin-left:0; margin-right:0"><span>云环境 </span><a href="https://gitee.com/link?target=https%3A%2F%2Fconsole.tancloud.cn" target="_blank">https://console.tancloud.cn</a>.</p> 
 <hr> 
 <p style="margin-left:0; margin-right:0">Redis监控来啦：</p> 
 <img alt="2022-05-29 20 23 58" src="https://user-images.githubusercontent.com/24788200/170868079-325ccc08-165f-4d0e-9ebb-18b0b5c9db3f.png" width="1910" referrerpolicy="no-referrer">
 <span> </span>
 <img alt="2022-05-29 20 24 21" src="https://user-images.githubusercontent.com/24788200/170868094-3c4de70f-934a-4a13-ae1a-0744c30f14f3.png" style="margin-bottom:0px !important" width="959" referrerpolicy="no-referrer">
</div> 
<p> </p> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdromara%2Fhertzbeat" target="_blank">HertzBeat 赫兹跳动</a><span> </span>是一个支持网站，API，PING，端口，数据库，操作系统等监控类型，拥有易用友好的可视化操作界面的开源监控告警项目。<br> 我们也提供了对应的<span> </span><strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fconsole.tancloud.cn" target="_blank">SAAS 版本监控云</a></strong>，中小团队和个人无需再为了监控自己的网站资源，而去部署一套繁琐的监控系统，<strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fconsole.tancloud.cn" target="_blank">登录即可免费开始</a></strong>。<br> HertzBeat 支持<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhertzbeat.com%2Fdocs%2Fadvanced%2Fextend-point" target="_blank">自定义监控</a><span> </span>, 只用通过配置 YML 文件我们就可以自定义需要的监控类型和指标，来满足常见的个性化需求。<br> HertzBeat 模块化，<code>manager, collector, scheduler, warehouse, alerter</code><span> </span>各个模块解耦合，方便理解与定制开发。<br> HertzBeat 支持更自由化的告警配置 (计算表达式)，支持告警通知，告警模版，邮件钉钉微信飞书等及时通知送达<br> 欢迎登录 HertzBeat 的<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fconsole.tancloud.cn" target="_blank">云环境 TanCloud</a><span> </span>试用发现更多。<br> 我们正在快速迭代中，欢迎参与加入一起共建项目开源生态。</p> 
</blockquote> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><code>HertzBeat</code><span> </span>的多类型支持，易扩展，低耦合，希望能帮助开发者和中小团队快速搭建自有监控系统。</p> 
</blockquote> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">老铁们可以通过演示视频来直观了解功能：<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1DY4y1i7ts" target="_blank">https://www.bilibili.com/video/BV1DY4y1i7ts</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">欢迎在线试用<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fconsole.tancloud.cn">https://console.tancloud.cn</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>仓库地址</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdromara%2Fhertzbeat" target="_blank">Github</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdromara%2Fhertzbeat" target="_blank">https://github.com/dromara/hertzbeat</a><br> <a href="https://gitee.com/dromara/hertzbeat">Gitee</a><span> </span><a href="https://gitee.com/dromara/hertzbeat">https://gitee.com/dromara/hertzbeat</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">看到这里不妨给个 Star 支持下哦，灰常感谢，弯腰！！</p>
                                        </div>
                                      
</div>
            