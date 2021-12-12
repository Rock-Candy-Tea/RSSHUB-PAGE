
---
title: 'SmsForwarder (短信转发器) v2.3.0 双 12 狂欢版'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-d3f9ae4885863f997ae3ec7a51591c6bb2e.png'
author: 开源中国
comments: false
date: Sun, 12 Dec 2021 20:09:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-d3f9ae4885863f997ae3ec7a51591c6bb2e.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt height="144" src="https://oscimg.oschina.net/oscnet/up-d3f9ae4885863f997ae3ec7a51591c6bb2e.png" width="144" referrerpolicy="no-referrer"></p> 
<hr> 
<p style="color:#24292f; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpppscn%2FSmsForwarder%2Freleases" target="_blank"><img alt="GitHub release" src="https://camo.githubusercontent.com/452d98b1388cbbe0c185805940d8cb3f0ec7be9150b58670a714ea427b0d686d/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f72656c656173652f70707073636e2f536d73466f727761726465722e737667" referrerpolicy="no-referrer"></a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpppscn%2FSmsForwarder%2Fstargazers" target="_blank"><img alt="GitHub stars" src="https://camo.githubusercontent.com/c3f7ceb530c7c5e0f402483a8573e7d3ec93d78b3b142a47e339c357a6fc8e58/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f70707073636e2f536d73466f72776172646572" referrerpolicy="no-referrer"></a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpppscn%2FSmsForwarder%2Fnetwork%2Fmembers" target="_blank"><img alt="GitHub forks" src="https://camo.githubusercontent.com/371140c7cffd251f0fdb6b12b07c7deb78d9b97594050cc780688de249a88d58/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f666f726b732f70707073636e2f536d73466f72776172646572" referrerpolicy="no-referrer"></a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpppscn%2FSmsForwarder%2Fissues" target="_blank"><img alt="GitHub issues" src="https://camo.githubusercontent.com/c2d839a5c5637ccc20aaa430107d79bfdffef11846a8bf6aa5c5cccd35ae02ab/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6973737565732f70707073636e2f536d73466f72776172646572" referrerpolicy="no-referrer"></a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpppscn%2FSmsForwarder%2Fblob%2Fmain%2FLICENSE" target="_blank"><img alt="GitHub license" src="https://camo.githubusercontent.com/caba1de75a3026f5db23d219f5242853ae2135eca3e986ff23cac2dd29c3a509/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f70707073636e2f536d73466f72776172646572" referrerpolicy="no-referrer"></a></p> 
<p style="color:#24292f; text-align:start">短信转发器——监控Android手机短信、来电、APP通知，并根据指定规则转发到其他手机：钉钉机器人、企业微信群机器人、飞书机器人、企业微信应用消息、邮箱、bark、webhook、Telegram机器人、Server酱、PushPlus、手机短信等。</p> 
<p style="color:#24292f; text-align:start"><img alt height="835" src="https://oscimg.oschina.net/oscnet/up-89df766c78cb11c5f9c0e2b8efed802dfa5.png" width="1372" referrerpolicy="no-referrer"></p> 
<hr> 
<p><strong>本次更新内容：</strong></p> 
<ul> 
 <li><strong>新增：Telegram通过socks5/HTTP代理转发</strong></li> 
 <li>优化：关于软件页面下打开开机启动，将尝试跳转到系统自启动设置界面</li> 
 <li>优化：限制只能安装只内部卡，避免自启动失败（待验证）</li> 
 <li>修复：转发到其他手机，多个手机号用分号分隔无效的bug</li> 
 <li>优化：日志增加一个中间状态 & 记录接口请求重试日志</li> 
 <li>优化：电池状态监听（剩余电量预警上下限，电池状态改变）</li> 
 <li><strong>新增：转发规则上支持配置正则替换内容</strong>（用法：详见 <a href="https://gitee.com/pp/SmsForwarder/wikis/%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98">开源仓库Wiki</a>）</li> 
 <li>优化：升级XUpdate组件版本</li> 
 <li>优化：同一卡槽同一秒的重复未接来电广播不再重复处理（部分机型会收到两条广播？）</li> 
 <li>修复：多个企业微信应用 access_token 并存问题</li> 
</ul>
                                        </div>
                                      
</div>
            