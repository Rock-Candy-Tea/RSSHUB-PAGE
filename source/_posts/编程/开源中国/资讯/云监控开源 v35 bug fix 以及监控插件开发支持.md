
---
title: '云监控开源 v3.5 bug fix 以及监控插件开发支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3478'
author: 开源中国
comments: false
date: Sun, 06 Jun 2021 16:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3478'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start">该版本主要修复了部分bug 以及支持 linux shell 插件开发，主要修改点如下：</p> 
<ol> 
 <li>阿里云的日志服务器收不到本机 agent 数据包问题规避</li> 
 <li>mysql 自动连接失败问题fix</li> 
 <li>mysql db 编码统一使用 latin1编码（实际是utf编码）</li> 
 <li>agent日志配置同步偶尔失败问题 fix</li> 
 <li>插件支持开发者模式，并开放 linux shell 语言插件开发功能</li> 
</ol> 
<p style="text-align:start"> </p> 
<p style="text-align:start">linux shell 插件开发步骤：</p> 
<ol> 
 <li>﻿部署<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fopen.xrkmonitor.com%2F" target="_blank">开源版</a>监控系统</li> 
 <li>注册云账号，并申请开发者权限</li> 
 <li>在云版本上创建插件（需要在 gitee 上创建插件开源项目）</li> 
 <li>下载插件模板代码，并将模板代码导入到新创建的gitee 项目中</li> 
 <li>在云版本上提交插件灰度生成部署包</li> 
 <li>在<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fopen.xrkmonitor.com%2F" target="_blank">开源版</a>上绑定云账号</li> 
 <li>进入<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fopen.xrkmonitor.com%2F" target="_blank">开源版</a>插件市场，安装部署新创建的插件</li> 
 <li>在插件中添加自己的数据采集逻辑，并提交代码到 gitee</li> 
 <li>在云版本 “我的插件” 中提交灰度</li> 
 <li>在<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fopen.xrkmonitor.com%2F" target="_blank">开源版</a>更新部署验证通过后提交审核即可</li> 
</ol> 
<p style="text-align:start">linux shell 插件开发演示视频：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1Uv411V7sm%2F" target="_blank">https://www.bilibili.com/video/BV1Uv411V7sm/</a></p> 
<p style="text-align:start">插件开发文档说明：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fxrkmonitor.com%2Fmonitor%2Fshowdoc%2Fshowdoc%2Fweb%2F%23%2F11" target="_blank">http://xrkmonitor.com/monitor/showdoc/showdoc/web/#/11</a></p> 
<p style="text-align:start">版本源码：<a href="https://gitee.com/xrkmonitorcom/open/releases/v3.5" target="_blank">https://gitee.com/xrkmonitorcom/open/releases/v3.5</a></p>
                                        </div>
                                      
</div>
            