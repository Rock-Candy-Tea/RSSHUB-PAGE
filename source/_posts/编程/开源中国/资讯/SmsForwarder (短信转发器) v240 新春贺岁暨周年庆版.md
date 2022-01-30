
---
title: 'SmsForwarder (短信转发器) v2.4.0 新春贺岁暨周年庆版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-e9c5292773567b86dfb59e3d5fedbf6b53d.png'
author: 开源中国
comments: false
date: Sun, 30 Jan 2022 20:29:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-e9c5292773567b86dfb59e3d5fedbf6b53d.png'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#40485b">短信转发器——监控Android手机短信、来电、APP通知，并根据指定规则转发到其他手机：钉钉机器人、企业微信群机器人、飞书机器人、企业微信应用消息、邮箱、bark、webhook、Telegram机器人、Server酱、PushPlus、手机短信等。</span></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-e9c5292773567b86dfb59e3d5fedbf6b53d.png" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><span>重要更新：</span></h3> 
<ul> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>新增：Gotify发送通道（自主推送通知服务）</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>优化：一键克隆机制优化，提高成功率</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>新增：smshub主被动模式 by xingxichen</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>优化：界面布局 & 用户体验优化</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>优化：关闭代码混淆（minifyEnabled=false），避免代码混淆后一些莫名其妙的问题，因此APK包有所变大</span></p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><span>常规更新：</span></h3> 
<ul> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>修复：多重匹配中”正则匹配“bug</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>优化：飞书使用Card发送通知消息 by xiao0yy</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>新增：支持一键克隆单条转发规则（长按弹出对话框）</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>新增：多重匹配增加匹配字段——通知标题、卡槽信息</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>新增：自定义模板 新增 &#123;&#123;通知标题&#125;&#125; 变量（APP通知有效，取值等同&#123;&#123;卡槽信息&#125;&#125;）</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>新增：允许开启自动关闭通知（单条通知处理完毕后自动关闭，避免多条通知堆叠）</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>新增：隐私政策对话框（合规化，同意后才能使用软件、未同意隐私协议前不进行任何组件初始化）</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>优化：邮件发送支持多个收件人（以半角逗号,分隔）</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>新增：Telegram允许指定请求方式(POST/GET) by pickmefly</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>优化：自定义模板（在焦点位置插入标签） by Nacll</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>优化：更换SIM卡后，卡槽信息自动刷新 by Nacll</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>新增：手动重发发送失败的消息 by Nacll</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>优化：敏感信息输入框增加明文/密文切换、清除按钮（明文状态下可粘贴）</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>新增：发送通道新增是否启用状态</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>优化：发送通道必填字段校验与界面优化</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>新增：pushplus增加标题模板</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>优化：发送失败重试简化配置、机制优化（手动请求时不重试）</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>新增：转发规则新增是否启用状态</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>新增：异常捕获类，记录crash日志</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>优化：移除RxJava</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>新增：OkHttp重试拦截器、设置超时时间为5秒</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>优化：电量预警增加是否持续通知开关</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>新增：Webhook的GET形式支持webParams【例如：PushDeer】</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>整理：英文语言包&界面布局微调 by malsony</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>优化：StepBar 控件（新手按1234步骤进行配置，已设置过则点亮）</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>精简：不需要获取 mImei 和 mImsi，避免异常</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>修复：来电转发的卡槽信息不准确（异常处理：获取卡槽失败时，默认为卡槽1）、转发文本标明通话类型：1.呼入 2.呼出 3.未接</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>优化：bark推送新增标题模板、时效性、声音、角标、链接设置项（兼容旧的配置）</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>优化：增加ABI配置（按CPU架构分别打包）</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>精简：删除不必要的资源文件、压缩图片资源</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>优化：细化权限请求判断</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>优化：GitHub Action 打包脚本（按CPU架构分别发包）</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>精简：替换FloatingActionButton组件</span></p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><span>APK版本说明：</span></h3> 
<ul> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>universal: 通用版（不在乎安装包大小/懒得选就用这个版本，包含以下3种CPU架构so）</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>armeabi-v7a: 32位ARM设备（备用机首选）</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>arm64-v8a: 64位ARM设备（主流旗舰机）</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>x86: 32位Intel设备</span></p> </li> 
</ul> 
<h3>使用文档</h3> 
<blockquote> 
 <p><a href="https://gitee.com/pp/SmsForwarder/wikis/pages">https://gitee.com/pp/SmsForwarder/wikis/pages</a></p> 
</blockquote> 
<p> </p> 
<p>值此新春佳节，发布一个新春贺岁暨周年庆版！提前祝大家，新春快乐，虎虎生威！<br> <br> 开源一年以来收到2.5K+的star和很多优秀的改进建议，感谢大家的支持与厚爱！</p>
                                        </div>
                                      
</div>
            