
---
title: '版本升级 _ OpenSCA v1.0.3版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8422'
author: 开源中国
comments: false
date: Tue, 12 Apr 2022 08:42:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8422'
---

<div>   
<div class="content">
                                                                    
                                                        <h4 style="margin-left:0px; margin-right:0px; text-align:start"><strong>引言</strong></h4> 
<div style="margin-left:0; margin-right:0; text-align:justify"> 
 <p style="margin-left:0; margin-right:0">千呼万唤始出来，版本升级换容颜！</p> 
 <p style="margin-left:0; margin-right:0">在万众期待中，OpenSCA v1.0.3版本终于成功孵化，顺利发版！经过研发和产品伙伴们夜以继日的努力，本次版本升级更新了<span style="color:#a9288d">语言检测</span>和<span style="color:#a9288d">文件解析</span>。话不多说，让我们一起来看一下吧！</p> 
 <h4 style="margin-left:0px; margin-right:0px"><strong>v1.0.3更新内容</strong></h4> 
 <p>⚫   新增<strong>JavaScript</strong>语言<strong>npm</strong>包管理器<strong>yarn.lock</strong>的检测</p> 
 <p style="margin-left:0; margin-right:0"><span>⚫</span>   新增<strong>PHP</strong>语言<strong>composer</strong>依赖管理工具<strong>composer.json</strong>的检测</p> 
 <p style="margin-left:0; margin-right:0"><span>⚫</span>   新增<strong>Ruby</strong>语言<strong>gem</strong>包管理器<strong>gems.locked</strong>的检测</p> 
 <p style="margin-left:0; margin-right:0"><span>⚫</span>   新增<strong>Golang</strong>语言检测支持</p> 
 <p style="margin-left:0; margin-right:0">      🔷 <span style="color:#a9288d"><strong>go mod 包管理器 go.mod、god.sum文件的解析</strong></span></p> 
 <p style="margin-left:0; margin-right:0"> </p> 
 <h4 style="margin-left:0px; margin-right:0px"><strong>检测能力</strong></h4> 
 <p>ps：紫色字体为新增部分哦~</p> 
 <table cellspacing="0" style="border-collapse:collapse; box-sizing:border-box !important; display:table; margin:0px 0px 10px; max-width:100%; outline:0px; overflow-wrap:break-word !important; padding:0px; width:677px"> 
  <tbody> 
   <tr> 
    <td colspan="1" rowspan="1" style="background-color:rgba(169, 40, 141, 0.49); border-color:#3e3e3e #ffffff #3e3e3e #3e3e3e; border-image:initial; border-style:none; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center"><strong>支持语言</strong></p> </td> 
    <td colspan="1" rowspan="1" style="background-color:#a9288d; border-color:#3e3e3e #ffffff #3e3e3e #3e3e3e; border-image:initial; border-style:none; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center"><strong>包管理器</strong></p> </td> 
    <td colspan="1" rowspan="1" style="background-color:rgba(169, 40, 141, 0.49); border-color:#3e3e3e #ffffff #3e3e3e #3e3e3e; border-image:initial; border-style:none; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center"><strong>解析文件</strong></p> </td> 
   </tr> 
   <tr> 
    <td colspan="1" rowspan="1" style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:center">Java</p> </td> 
    <td colspan="1" rowspan="1" style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:center">Maven</p> </td> 
    <td colspan="1" rowspan="1" style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:center">pom.xml</p> </td> 
   </tr> 
   <tr> 
    <td colspan="1" rowspan="1" style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:center">JavaScript</p> </td> 
    <td colspan="1" rowspan="1" style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:center">Npm</p> </td> 
    <td colspan="1" rowspan="1" style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">package-lock.json</p> <p style="margin-left:0px; margin-right:0px; text-align:center">package.json</p> <p style="margin-left:0px; margin-right:0px; text-align:center"><span style="color:#a9288d">yarn.lock</span></p> </td> 
   </tr> 
   <tr> 
    <td colspan="1" rowspan="1" style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:center">PHP</p> </td> 
    <td colspan="1" rowspan="1" style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:center">Composer</p> </td> 
    <td colspan="1" rowspan="1" style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">composer.lock</p> <p style="margin-left:0px; margin-right:0px; text-align:center"><span style="color:#a9288d">composer.json</span></p> </td> 
   </tr> 
   <tr> 
    <td colspan="1" rowspan="1" style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:center">Ruby</p> </td> 
    <td colspan="1" rowspan="1" style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:center">Gem</p> </td> 
    <td colspan="1" rowspan="1" style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">gemfile.lock</p> <p style="margin-left:0px; margin-right:0px; text-align:center"><span style="color:#a9288d">gems.locked</span></p> </td> 
   </tr> 
   <tr> 
    <td colspan="1" rowspan="1" style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:center">Golong</p> </td> 
    <td colspan="1" rowspan="1" style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0; margin-right:0; text-align:center">Go mod</p> </td> 
    <td colspan="1" rowspan="1" style="background-color:rgba(255, 255, 255, 0); border-color:#3e3e3e #3e3e3e #dfdfdf; border-image:initial; border-style:none none solid; border-width:1px"> <p style="margin-left:0px; margin-right:0px; text-align:center">go.mod</p> <p style="margin-left:0px; margin-right:0px; text-align:center">go.sum</p> </td> 
   </tr> 
  </tbody> 
 </table> 
 <p style="margin-left:0; margin-right:0"> </p> 
 <h4><strong>v1.0.4计划</strong></h4> 
 <p>在之后的版本中，OpenSCA会计划支持Rust语言的检测。</p> 
 <p style="margin-left:0; margin-right:0">欢迎持续关注OpenSCA社区获取OpenSCA开源项目最新动态，您也可以在OpenSCA开源项目中提出您的需求或建议，将您希望尽快支持的编程语言反馈给我们，后续OpenSCA会逐步支持更多编程语言，丰富相关配置文件的解析，感谢您的支持。</p> 
 <p style="margin-left:0; margin-right:0"> </p> 
 <h4 style="margin-left:0px; margin-right:0px"><strong>总结</strong></h4> 
 <p>每一次版本的更新都凝聚了悬镜伙伴们的心血，我们希望OpenSCA的升级能切实为大家带来帮助。创建一个充满活力的开源社区并非易事，但总要勇敢踏出第一步才会有康庄大道的可能。</p> 
 <p style="margin-left:0; margin-right:0">我们愿为孺子牛致力于开源事业的发展，希望能有越来越多的伙伴加入我们，共同为开源事业贡献自己的力量！</p> 
 <ul> 
  <li style="margin-left: 0px; margin-right: 0px;"><strong><span style="color:#a9288d">OpenSCA</span></strong><span style="color:#a9288d">是悬镜安全旗下源鉴<strong>OSS</strong>开源威胁管控产品的开源版本</span>，继承了源鉴<strong>OSS</strong>的多源<strong>SCA</strong>开源应用安全缺陷检测等核心能力。</li> 
  <li style="color: rgb(62, 62, 62); margin-left: 0px; margin-right: 0px;"><strong><span style="color:#293239">OpenSCA</span></strong><span style="color:#293239">用开源的方式做开源风险治理，致力于做软件供应链安全的护航者，守护中国软件供应链安全。</span></li> 
  <li style="color: rgb(62, 62, 62); margin-left: 0px; margin-right: 0px;"><strong><span style="color:#293239">OpenSCA</span></strong><span style="color:#293239">的代码会在<strong>Gitee</strong>持续迭代，欢迎<strong>Star</strong>和<strong>PR</strong>，成为我们的开源贡献者，也可提交问题或建议至<strong>Issues</strong>。</span><span style="color:#a9288d">我们会参考大家的建议不断完善<strong>OpenSCA</strong>开源项目，敬请期待更多功能的支持。</span></li> 
 </ul> 
</div>
                                        </div>
                                      
</div>
            