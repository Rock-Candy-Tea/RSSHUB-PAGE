
---
title: 'SmsForwarder (短信转发器) v3.0.5 Kotlin 全新重构版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-2eaad8bb66073c28ed5bfe1a2125fb291f9.webp'
author: 开源中国
comments: false
date: Fri, 01 Jul 2022 18:21:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-2eaad8bb66073c28ed5bfe1a2125fb291f9.webp'
---

<div>   
<div class="content">
                                                                                            <p style="color:#24292f; margin-left:0; margin-right:0; text-align:start"><strong>短信转发器 —— 不仅只转发短信，备用机必备神器！</strong></p> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start">        监控 Android 手机短信、来电、APP 通知，并根据指定规则转发到其他手机：钉钉机器人、企业微信群机器人、飞书机器人、企业微信应用消息、邮箱、bark、webhook、Telegram 机器人、Server 酱、PushPlus、手机短信等。</p> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start"><strong>包括主动控制服务端与客户端，让你轻松远程发短信、查短信、查通话、查话簿、查电量等。（V3.0 新增）</strong></p> 
<p style="color:#24292f; margin-left:0; margin-right:0; text-align:start"> </p> 
<p><br> <img alt src="https://oscimg.oschina.net/oscnet/up-2eaad8bb66073c28ed5bfe1a2125fb291f9.webp" referrerpolicy="no-referrer"></p> 
<p> </p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">V3.0 界面预览：</h2> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-f22969aa2f67487230ebd8850198ff512da.webp" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:start">更新日志</h3> 
<ul> 
 <li>重构：采用 Kotlin 全新重构（不是迁移代码）</li> 
 <li>重构：全新的界面 XUI 实现（略微提升点前端美感）</li> 
 <li>重构：全新的 HttpServer 实现（采用 AndServer，目前有6个API）</li> 
 <li>新增：增加 Frpc 支持内网穿透（按需下载 FrpcLib 动态库支持）</li> 
 <li>新增：主动控制·客户端（界面直接远程发短信等）</li> 
 <li>新增：保活措施 Cactus（双进程前台服务，JobScheduler，onePix(一像素)，WorkManager，无声音乐）</li> 
 <li>优化：适配 Android 4.4 ~ 12.0</li> 
 <li>优化：舍弃 emailkit 依赖，直接基于 android-mail 重写</li> 
 <li>优化：自动过滤指定时间内的重复消息</li> 
 <li>修复：v2.x 的 issue</li> 
 <li>精简：一些不必要的功能（含尚未迁移的小功能）</li> 
</ul> 
<hr> 
<ul> 
 <li>修复：短信广播中的权限判断导致OV系手机转发异常 (v3.0.1)</li> 
 <li>修复：在子线程中调用Toast的异常情况处理 (v3.0.1)</li> 
</ul> 
<hr> 
<ul> 
 <li>优化：统一卡槽ID枚举值（ 0=Sim1, 1=Sim2, -1=获取失败）【未做机型适配】 (v3.0.2)</li> 
 <li>修复：卡槽匹配转发规则错误（卡槽id：-1=获取失败、0=卡槽1、1=卡槽2，但是 Rule 表里存的是 SIM1/SIM2） (v3.0.2)</li> 
 <li>修复：通用设置中无法关闭转发应用通知开关 (v3.0.2)</li> 
 <li>修复：无网络时主动控制·服务端界面自动获取IP异常 (v3.0.2)</li> 
 <li>整理：隐私权政策内容 (v3.0.2)</li> 
 <li>优化：在线更新【主界面检测】 (v3.0.2)</li> 
</ul> 
<hr> 
<ul> 
 <li>优化：仅测试转发规则与发送通道时Toast提示 (v3.0.3)</li> 
 <li>优化：主动控制·服务端定时更新UI机制 (v3.0.3)</li> 
 <li>精简：ANR异常捕获依赖（ANR-WatchDog）【可能会增加耗电】 (v3.0.3)</li> 
 <li>修复：转发规则编辑页面关闭自定义模板/正则替换时没有清空输入框 (v3.0.3)</li> 
 <li>新增：启动时异步获取已安装App信息开关 (v3.0.3)</li> 
 <li>新增：应用列表分类展示(用户应用/系统应用)/按应用名排序 (v3.0.3)</li> 
 <li>新增：自定义模板支持&#123;&#123;APP名称&#125;&#125;标签（仅启用异步获取App列表时有值） (v3.0.3)</li> 
 <li>修复：v3.0.2来电转发卡槽信息获取失败 (v3.0.3)</li> 
 <li>新增：按需启用Cactus增强保活措施的开关【开启后可能会增加耗电】 (v3.0.3)</li> 
</ul> 
<hr> 
<ul> 
 <li>优化：未开启异步获取已安装App信息开关时，规则编辑不显示已安装APP下拉框 (v3.0.4)</li> 
 <li>优化：允许不填写服务端地址直接进入 主动控制·客户端 -> 一键换新机 -> 离线模式 (v3.0.4)</li> 
 <li>修复：测试TG/Webhook发送通道时，子线程调用Toast引发FC (v3.0.4)</li> 
 <li>修复：发件人昵称插入 &#123;&#123;接收时间&#125;&#125; 时转码失败（Nested Group） (v3.0.4)</li> 
 <li>优化：邮件主题、发件人昵称替换冒号、换行为 - (v3.0.4)</li> 
 <li>整理：替换 在线升级 & FrpcLib下载 URL的域名 (v3.0.4)</li> 
 <li>新增：主动控制·客户端增加服务地址历史记录（测试接口通过后自动加入） (v3.0.4)</li> 
 <li>优化：主动控制·客户端发送短信手机号长度限制放宽到20位（短信平台号） (v3.0.4)</li> 
 <li>优化：提高主动控制·客户端远程查通话、远程查话簿兼容性（兼容鸿蒙2.0） (v3.0.4)</li> 
 <li>新增：关于页面增加QQ频道入口 (v3.0.4)</li> 
</ul> 
<hr> 
<ul> 
 <li>优化：发送通道<code>webhook</code>支持HTTP基本认证 【格式：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fusername%3Apassword%40domain.com%2Furi%25E3%2580%2591" target="_blank">http://username:password@domain.com/uri】</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpppscn%2FSmsForwarder%2Fissues%2F175" target="_blank">#175</a> (v3.0.5)</li> 
 <li>优化：发送通道<code>企业微信应用</code>获取access_token失败时记录错误日志 (v3.0.5)</li> 
 <li>优化：发送通道<code>短信</code>发送权限未授权/仅当无网络启用时记录错误日志 (v3.0.5)</li> 
 <li>修复：邮箱发送通道收件地址不支持逗号分隔Bug（已支持逗号/分号） (v3.0.5)</li> 
 <li>优化：测试发送通道/转发规则时创建子线程运行 & 异常捕获 (v3.0.5)</li> 
 <li>优化：发送通道<code>Telegram</code>代理主机名支持域名解析<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpppscn%2FSmsForwarder%2Fissues%2F172" target="_blank">#172</a> (v3.0.5)</li> 
 <li>新增：远程查配置接口增加卡槽信息与备注<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpppscn%2FSmsForwarder%2Fissues%2F174" target="_blank">#174</a> (v3.0.5)</li> 
 <li>修复：发送通道<code>Telegram</code>启用Socks5支持用户密码鉴权<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpppscn%2FSmsForwarder%2Fissues%2F172" target="_blank">#172</a> (v3.0.5)</li> 
 <li>优化：发送通道<code>webhook</code>的<code>webParams</code>非空时（wiki:2.1/2.2）不再限制必须包含<code>[msg]</code>标签 (v3.0.5)</li> 
 <li>优化：发送通道<code>Bark</code>/<code>Gotify</code>支持HTTP基本认证 【格式：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fusername%3Apassword%40domain.com%2Furi%25E3%2580%2591" target="_blank">http://username:password@domain.com/uri】</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpppscn%2FSmsForwarder%2Fissues%2F170" target="_blank">#170</a> (v3.0.5)</li> 
 <li>优化：支持<code>正则替换===右边</code>添加\n用于手动换行 (v3.0.5)</li> 
 <li>优化：webhook通道替换POST时替换webParams中[timestamp]/[sign]标签 (v3.0.5)</li> 
 <li>新增：主动控制·客户端 -> 一键换新机 支持导出导入Frpc配置 (v3.0.5)</li> 
 <li>优化：FrpcLib下载流程（增加确认对话框） (v3.0.5)</li> 
 <li>新增：免打扰(禁用转发)时间段 (v3.0.5)</li> 
 <li>修复：钉钉群机器人不填写加签密钥时报错（Empty key） (v3.0.5)</li> 
</ul> 
<hr> 
<p><span style="background-color:#ffffff; color:#333333">更多更新细节参见 Wiki：https://gitee.com/pp/SmsForwarder/wikis/Home</span></p> 
<blockquote> 
 <p>PS. 自 <strong>2022-06-09</strong> 发布 <strong>3.0</strong> 以来，经过几个小版本的迭代，目前已经趋于稳定，3.x 版本的7天活跃用户占比已攀升到 <strong>31.81%，想要升级的用户可以试试了</strong></p> 
</blockquote> 
<p style="text-align:start"><strong>Q：升级到<span> </span><code>3.x</code><span> </span>发现很耗电，怎么办？</strong></p> 
<p style="color:#24292f; text-align:start"><strong>A：</strong><span> </span><strong>尝试以下操作：</strong></p> 
<p style="color:#24292f; text-align:start">1、在线升级至最新版本后，离线导出配置：主动控制·客户端→一键换新机→离线模式→导出</p> 
<p style="color:#24292f; text-align:start">2、卸载当前apk全新安装最新版后，离线导入配置</p> 
<p style="color:#24292f; text-align:start">3、用不上内置的内网穿透功能的话，不要点击<span> </span><code>内网穿透·Frpc</code><span> </span>下载 FrpcLib 动态库</p> 
<blockquote> 
 <p>PS.下载后App启动时会动态加载增加内存消耗，如果误点击下载了，也可以在<span> </span><code>关于软件</code><span> </span>中<span> </span><code>删除动态库</code></p> 
</blockquote> 
<p style="color:#24292f; text-align:start">4、以上操作都不行的话，还是退回<span> </span><code>2.4.4</code><span> </span>先用着吧</p>
                                        </div>
                                      
</div>
            