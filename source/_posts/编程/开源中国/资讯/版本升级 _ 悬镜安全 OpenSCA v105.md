
---
title: '版本升级 _ 悬镜安全 OpenSCA v1.0.5'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-190713160617f308a5fd37fffb6d6bfbe23.jpg'
author: 开源中国
comments: false
date: Thu, 21 Apr 2022 17:51:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-190713160617f308a5fd37fffb6d6bfbe23.jpg'
---

<div>   
<div class="content">
                                                                                            <h2 style="margin-left:0; margin-right:0; text-align:left"><span><strong>引言</strong></span></h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">邀君共探此，版本新更替。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">经过研发和产品伙伴们夜以继日的努力，OpenSCA1.0.5版本成功发布！本次版本升级更新了对语言的检测，让我们一起来看一下吧！</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><span><strong>v1.0.5更新内容</strong></span></h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span>新增Erlang语言Rebar包管理器rebar.lock文件的检测</span></strong></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><span><strong>使用方式</strong></span></h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">访问OpenSCA开源项目，下载OpenSCA最新版本：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="background-color:rgba(169, 40, 141, 0.17); color:#3e3e3e">https://gitee.com/XmirrorSecurity/OpenSCA-cli/</span></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><span><strong>检测能力</strong></span></h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">ps：紫色字体为新增部分哦~</p> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:1px; border:none; box-sizing:border-box; color:#444444; display:table; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px 0px 10px; max-width:100%; orphans:2; overflow:auto; padding:0px; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:776px; word-break:keep-all; word-spacing:0px"> 
 <tbody> 
  <tr> 
   <td style="background-color:rgba(169, 40, 141, 0.49); border-color:#3e3e3e #ffffff #3e3e3e #3e3e3e; border-image:initial; border-style:none; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:center"><strong>支持语言</strong></p> </td> 
   <td style="background-color:#a9288d; border-color:#3e3e3e #ffffff #3e3e3e #3e3e3e; border-image:initial; border-style:none; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:center"><strong>包管理器</strong></p> </td> 
   <td style="background-color:rgba(169, 40, 141, 0.49); border-color:#3e3e3e #ffffff #3e3e3e #3e3e3e; border-image:initial; border-style:none; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:center"><strong>解析文件</strong></p> </td> 
  </tr> 
  <tr> 
   <td style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:center">Java</p> </td> 
   <td style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:center">Maven</p> </td> 
   <td style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:center">pom.xml</p> </td> 
  </tr> 
  <tr> 
   <td style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:center">JavaScript</p> </td> 
   <td style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:center">Npm</p> </td> 
   <td style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:center">package-lock.json</p> <p style="margin-left:0; margin-right:0; text-align:center">package.json</p> <p style="margin-left:0; margin-right:0; text-align:center"><span>yarn.lock</span></p> </td> 
  </tr> 
  <tr> 
   <td style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:center">PHP</p> </td> 
   <td style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:center">Composer</p> </td> 
   <td style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:center">composer.lock</p> <p style="margin-left:0; margin-right:0; text-align:center"><span>composer.json</span></p> </td> 
  </tr> 
  <tr> 
   <td style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:center">Ruby</p> </td> 
   <td style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:center">Gem</p> </td> 
   <td style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:center">gemfile.lock</p> <p style="margin-left:0; margin-right:0; text-align:center"><span>gems.locked</span></p> </td> 
  </tr> 
  <tr> 
   <td style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:center">Golang</p> </td> 
   <td style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:center">Gomod</p> </td> 
   <td style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:center">go.mod</p> <p style="margin-left:0; margin-right:0; text-align:center">go.sum</p> </td> 
  </tr> 
  <tr> 
   <td style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:center">Rust</p> </td> 
   <td style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:center"><span>Cargo</span></p> </td> 
   <td style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:center"><span style="color:#3e3e3e">cargo.lock</span></p> </td> 
  </tr> 
  <tr> 
   <td style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:center"><strong><span style="color:#a9288d">Erlang</span></strong></p> </td> 
   <td style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:center"><strong><span style="color:#a9288d">Rebar</span></strong></p> </td> 
   <td style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:center"><strong><span style="color:#a9288d">rebar.lock</span></strong></p> </td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><span><strong>v1.0.6计划</strong></span></h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">根据小伙伴们对json文件的使用反馈，在新的版本中，OpenSCA检测结果会支持<span style="color:#a9288d"><strong>html格式</strong></span>的检测结果报告导出，方便大家在本地可视化查看开源组件安全检测结果。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">欢迎持续关注OpenSCA社区获取OpenSCA开源项目最新动态，您也可以在OpenSCA开源项目中提出您的需求或建议，将您希望尽快支持的编程语言反馈给我们，后续OpenSCA会逐步支持更多编程语言，丰富相关配置文件的解析，感谢您的支持。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><span><strong>总结</strong></span></h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">每一次版本的更新都凝聚了悬镜伙伴们的心血，我们希望OpenSCA的升级能切实为大家带来帮助，欢迎大家试用OpenSCA！创建一个充满活力的开源社区并非易事，我们愿为孺子牛致力于开源事业的发展，希望能有越来越多的伙伴加入们，共同为开源事业贡献自己的力量！</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><span><strong>彩蛋时间到</strong></span></h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span style="color:#222222">为了更好的提高用户体验度，完善OpenSCA开源威胁治理功能，现</span><span style="color:#a9288d"><strong>诚挚邀请各位伙伴参与问卷调查</strong></span><span style="color:#222222">，共建开源社区，后续会根据大家的需求逐步完善版本功能！</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify">                                                                            <img align="left" alt height="392" src="https://oscimg.oschina.net/oscnet/up-190713160617f308a5fd37fffb6d6bfbe23.jpg" width="392" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p>
                                        </div>
                                      
</div>
            