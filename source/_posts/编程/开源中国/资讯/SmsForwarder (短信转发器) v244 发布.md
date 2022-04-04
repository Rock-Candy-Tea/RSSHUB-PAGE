
---
title: 'SmsForwarder (短信转发器) v2.4.4 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-cca48f0fa6541632724fa799ae97972bd2e.png'
author: 开源中国
comments: false
date: Mon, 04 Apr 2022 10:21:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-cca48f0fa6541632724fa799ae97972bd2e.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#24292f; text-align:start"><img alt src="https://oscimg.oschina.net/oscnet/up-cca48f0fa6541632724fa799ae97972bd2e.png" referrerpolicy="no-referrer"></p> 
<p style="color:#24292f; text-align:start"> </p> 
<p style="color:#24292f; text-align:start"><span style="background-color:#ffffff; color:#24292f">短信转发器——监控Android手机短信、来电、APP通知，并根据指定规则转发到其他手机：钉钉机器人、企业微信群机器人、飞书机器人、企业微信应用消息、邮箱、bark、webhook、Telegram机器人、Server酱、PushPlus、手机短信等。</span></p> 
<hr> 
<p style="color:#24292f; text-align:start">大版本更新之前，先发一个小版本更新，下一个版本（2.5.0）重点改造<span> </span><code>主动请求(远程控制)</code><span> </span>功能<br> 对暴露的api有什么想法欢迎提issue，在合法合规的前提下，酌情考虑会不会添加！</p> 
<h3 style="text-align:start">重点优化</h3> 
<ul> 
 <li>新增：一键克隆增加离线模式（导出备份json文件到Download目录，其他机器读取文件导入）</li> 
 <li>优化：一键克隆机制优化（替换db文件→操作现有db）</li> 
 <li>新增：Webhook发送通道支持设置Header (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpppscn%2FSmsForwarder%2Fissues%2F128" target="_blank">#128</a>)</li> 
 <li>优化：Email发送通道简化配置（常见邮箱不需要填写smtp信息）</li> 
</ul> 
<h3 style="text-align:start">常规优化</h3> 
<ul> 
 <li>新增：仅锁屏状态转发APP通知开关</li> 
 <li>新增：定时发布 每夜构建 版本（北京时间：23:30）</li> 
 <li>新增：定时推送电池状态 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpppscn%2FSmsForwarder%2Fpull%2F131" target="_blank">#131</a>)</li> 
 <li>修复：手动重发消息中UTC时间未转换本地时间 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpppscn%2FSmsForwarder%2Fissues%2F122" target="_blank">#122</a>)</li> 
 <li>优化：抽取电池状态信息工具类</li> 
 <li>新增：定时推送电池状态 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpppscn%2FSmsForwarder%2Fissues%2F121" target="_blank">#121</a>)</li> 
 <li>优化：内嵌 WebView 打开使用帮助</li> 
 <li>优化：界面微调（增加输入框提示等）</li> 
 <li>修复：Bark通道转发规则正则导致转发失败（去除对标题的正则替换）</li> 
</ul> 
<h3 style="text-align:start">APK版本说明：</h3> 
<ul> 
 <li>universal: 通用版（不在乎安装包大小/懒得选就用这个版本，包含以下3种CPU架构so）</li> 
 <li>armeabi-v7a: 32位ARM设备（备用机首选）</li> 
 <li>arm64-v8a: 64位ARM设备（主流旗舰机）</li> 
 <li>x86: 32位Intel设备（64位兼容）</li> 
</ul>
                                        </div>
                                      
</div>
            