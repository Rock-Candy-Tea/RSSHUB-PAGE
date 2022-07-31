
---
title: 'OpenHarmony 3.2 Beta2 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5617'
author: 开源中国
comments: false
date: Sun, 31 Jul 2022 07:37:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5617'
---

<div>   
<div class="content">
                                                                    
                                                        <p>OpenHarmony 3.2 Beta2 已发布。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">版本概述</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">当前版本在OpenHarmony 3.2 Beta1的基础上，更新支持以下能力：</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>标准系统基础能力增强</strong></p> 
<ul> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: left;">新增支持窗口多热区分发机制。</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: left;">支持电源管理重启恢复机制。</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: left;">多模输入新增支持Input手写笔压感合成、倾角、按键输入。</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: left;">安全域支持预置应用预授权机制、指纹录入/认证/识别框架。</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: left;">驱动支持录像模式自拍镜像功能、音频音效控制、红外设备输入、音频USB插拔识别及事件上报。</li> 
</ul> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>标准系统应用程序框架能力增强</strong></p> 
<ul> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: left;">元能力支持卡片提供方添加静态和动态卡片、组件支持本地免安装启动、系统SA启动和访问组件、支持单实例Ability迁移、运行管理支持打开沙箱应用、系统应用ability不在最新任务列表显示。</li> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: left;">包管理支持获取当前包的包名和证书指纹信息NDK接口能力、查询指定应用的PackInfo信息、原子化服务老化卸载。</li> 
</ul> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>标准系统应用开发样例</strong></p> 
<ul> 
 <li style="color: rgb(64, 72, 91); margin-left: 0px; margin-right: 0px; text-align: left;">新增五子棋人机对战、二维码生成和解析、卡片使用、多媒体、短视频、面部识别能力等Demo样例，为开发者提供SDK使用的样例程序，方便开发者快速上手使用OpenHarmony系统基础能力。</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">配套关系</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>表1</strong><span> </span>版本软件和工具配套关系</p> 
<table cellspacing="0" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; box-sizing:border-box; color:#40485b; display:block; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Liberation Sans","PingFang SC","Microsoft YaHei","Hiragino Sans GB","Wenquanyi Micro Hei","WenQuanYi Zen Hei","ST Heiti",SimHei,SimSun,"WenQuanYi Zen Hei Sharp",sans-serif; font-size:16px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; margin-bottom:16px; margin-top:0px; orphans:2; overflow:auto; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:normal; widows:2; width:941px; word-break:initial; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th>软件</th> 
   <th>版本</th> 
   <th>备注</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">OpenHarmony</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">3.2 Beta2</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">NA</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">SDK</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">Ohos_sdk_public 3.2.5.5 (API Version 9 Beta1)<br> Ohos_sdk_full 3.2.5.5 (API Version 9 Beta1)</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">通过DevEco Studio默认获取的SDK为Public SDK。<br> 如需替换Full SDK，请参考<a href="https://gitee.com/openharmony/docs/blob/master/zh-cn/application-dev/quick-start/full-sdk-switch-guide.md">替换指南</a>。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">HUAWEI DevEco Studio（可选）</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">3.0 Beta4</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">OpenHarmony应用开发推荐使用。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">HUAWEI DevEco Device Tool（可选）</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">3.0 Release</td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px">OpenHarmony智能设备集成开发环境推荐使用。</td> 
  </tr> 
 </tbody> 
</table> 
<p><a href="https://gitee.com/openharmony/docs/blob/master/zh-cn/release-notes/OpenHarmony-v3.2-beta2.md">详情查看 release note</a>。</p>
                                        </div>
                                      
</div>
            