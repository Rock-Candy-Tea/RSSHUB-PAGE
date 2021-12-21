
---
title: 'ng-zorro-antd 12.1.1 发布，Ant Design 的 Angular 实现'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4087'
author: 开源中国
comments: false
date: Tue, 21 Dec 2021 07:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4087'
---

<div>   
<div class="content">
                                                                                            <p data-darkreader-inline-color style="--darkreader-inline-color:#d8d4cf; color:#e8e6e3; margin-left:0px; margin-right:0px; text-align:start">ng-zorro-antd<span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292f"><span> </span>是 Ant Design 的 Angular 实现，主要用于研发企业级中后台产品。全部代码开源并遵循 MIT 协议，任何企业、组织及个人均可免费使用。</span></p> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#d8d4cf; color:#e8e6e3; margin-left:0px; margin-right:0px; text-align:start"><span data-darkreader-inline-color style="--darkreader-inline-color:#cecac3; color:#24292f">目前<span> </span></span>ng-zorro-antd 更新了 12.1.1 版本，带来如下变化：</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Bug 修复</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>date-picker,time-picker:</strong><span> </span>禁用自动填充 autocomplete 属性 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7088" target="_blank">#7088</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2Fbddc537f6f64b6697f95ef421c634045656e4903" target="_blank">bddc537</a>), closes<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F6718" target="_blank">#6718</a></li> 
 <li><strong>popconfirm:</strong><span> </span>修复箭头丢失样式 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7086" target="_blank">#7086</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F3f4a704fc126a3c1ccfe92ae0f045062f00fd1e8" target="_blank">3f4a704</a>)</li> 
 <li><strong>timeline:</strong><span> </span>清空数据时重置组件状态 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7109" target="_blank">#7109</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F0ece6123a586c96a6178e2ba939b9451c031bc14" target="_blank">0ece612</a>)</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">性能改进</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>carousel:</strong><span> </span><code>keydown</code><span> </span>事件取消不必要的脏值检测（change detection） (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7097" target="_blank">#7097</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2Fca3299ea5b00c7075d93871ec418e1527d390f8b" target="_blank">ca3299e</a>)</li> 
 <li><strong>cascader:</strong><span> </span><code>keydown</code><span> </span>事件取消不必要的脏值检测 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7060" target="_blank">#7060</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F9a37718d42ac05288393d7c7d9db4204ba7e640e" target="_blank">9a37718</a>)</li> 
 <li><strong>date-picker:</strong><span> </span>点击<span> </span><code>date-range-popup</code><span> </span>取消不必要的脏值检测 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7096" target="_blank">#7096</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F8f8c71b1aedd10ecd50c48d802835bd235f0f2ee" target="_blank">8f8c71b</a>)</li> 
 <li><strong>date-picker:</strong><span> </span>修复内存泄漏问题 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7113" target="_blank">#7113</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2Ffe9070aaf486b50b231b19ee55bfc0b4907a98a2" target="_blank">fe9070a</a>)</li> 
 <li><strong>icon:</strong><span> </span>切换图标时取消不必要的脏值检测 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7071" target="_blank">#7071</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2Fe998e4abef73f34783aa63e88e9f0adadc8301e7" target="_blank">e998e4a</a>)</li> 
 <li><strong>mention:</strong><span> </span><code>mousedown</code><span> </span>事件取消不必要的脏值检测 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7094" target="_blank">#7094</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F0d4ad23a1722a01974c29c4b9f13eeff70c40df5" target="_blank">0d4ad23</a>)</li> 
 <li><strong>switch:</strong><span> </span>减少触发脏值检测 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7105" target="_blank">#7105</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F6d9b1fff55bcb3d8a6c5ef2b9250cfcee6ce6039" target="_blank">6d9b1ff</a>)</li> 
 <li><strong>table:</strong><span> </span><code>nz-filter-trigger</code><span> </span>点击事件取消不必要的脏值检测 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7095" target="_blank">#7095</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F346c50d0a5b19160d51c8c6a3e61a389b4b92a52" target="_blank">346c50d</a>)</li> 
 <li><strong>time-picker:</strong><span> </span>滚动时取消不必要的脏值检测 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7063" target="_blank">#7063</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2Fbaf7f0a85ef386a4ebe9bef553e532e501129f6e" target="_blank">baf7f0a</a>)</li> 
 <li><strong>time-picker:</strong><span> </span>panel 被点击取消不必要的脏值检测 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7126" target="_blank">#7126</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F76da3ff9f6a64fb854999f3ef30c45980c3b6b7b" target="_blank">76da3ff</a>)</li> 
 <li><strong>tree:</strong><span> </span>节点点击时取消不必要的脏值检测 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fissues%2F7128" target="_blank">#7128</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Fcommit%2F55f1e047b32597397c42c779409beff7ab13b1f7" target="_blank">55f1e04</a>)</li> 
</ul> 
<p data-darkreader-inline-color style="--darkreader-inline-color:#d8d4cf; color:#e8e6e3; margin-left:0px; margin-right:0px; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNG-ZORRO%2Fng-zorro-antd%2Freleases%2Ftag%2F12.1.1" target="_blank">https://github.com/NG-ZORRO/ng-zorro-antd/releases/tag/12.1.1</a></p>
                                        </div>
                                      
</div>
            