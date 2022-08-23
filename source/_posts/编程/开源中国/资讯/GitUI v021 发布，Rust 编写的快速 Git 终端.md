
---
title: 'GitUI v0.21 发布，Rust 编写的快速 Git 终端'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0822/112131_HdNm_2720166.gif'
author: 开源中国
comments: false
date: Tue, 23 Aug 2022 07:10:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0822/112131_HdNm_2720166.gif'
---

<div>   
<div class="content">
                                                                                            <p>GitUI 是 Rust 编写的 Git 终端，主打特性是速度快和极简风格的 UI。</p> 
<p><strong>新版本主要变化</strong></p> 
<ul> 
 <li><strong>支持堆叠弹出框 (popup stacking)</strong></li> 
</ul> 
<p><img height="619" src="https://static.oschina.net/uploads/space/2022/0822/112131_HdNm_2720166.gif" width="1010" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong>支持 Android 模拟器 Termux</strong></li> 
</ul> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-9807d0b9250c310a40945a208344ab25e12.png" referrerpolicy="no-referrer"></p> 
<p><strong>新增</strong></p> 
<ul> 
 <li>堆叠弹出框 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fextrawurst%2Fgitui%2Fissues%2F846" target="_blank">#846</a>)</li> 
 <li>文件历史记录日志 [<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fcruessler" target="_blank">@cruessler</a>] (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fextrawurst%2Fgitui%2Fissues%2F381" target="_blank">#381</a>)</li> 
 <li>支持 Android 模拟器 Termux [<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FPeroSar" target="_blank">@PeroSar</a>] (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fextrawurst%2Fgitui%2Fissues%2F1139" target="_blank">#1139</a>)</li> 
 <li>如果在环境中设置了<code>GIT_DIR</code>和<code>GIT_WORK_DIR</code><span>，会进行使用 </span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fextrawurst%2Fgitui%2Fpull%2F1191" target="_blank">#1191</a>)</li> 
 <li>重新设计的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fextrawurst%2Fgitui%2Fblob%2Fv0.21.0%2FFAQ.md" target="_blank">FAQ</a> 页面</li> 
 <li>在 wayland 上支持复制到剪贴板 [<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJayceFayne" target="_blank">@JayceFayne</a>] (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fextrawurst%2Fgitui%2Fissues%2F397" target="_blank">#397</a>)</li> 
</ul> 
<p style="text-align:start"><strong>Bugfix</strong></p> 
<ul> 
 <li>opening tags list without remotes (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fextrawurst%2Fgitui%2Fissues%2F1111" target="_blank">#1111</a>)</li> 
 <li>tabs indentation in blame [<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ffersilva16" target="_blank">@fersilva16</a>] (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fextrawurst%2Fgitui%2Fissues%2F1117" target="_blank">#1117</a>)</li> 
 <li>switch focus to index after staging last file (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fextrawurst%2Fgitui%2Fpull%2F1169" target="_blank">#1169</a>)</li> 
 <li>fix stashlist multi marking not updated after dropping (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fextrawurst%2Fgitui%2Fpull%2F1207" target="_blank">#1207</a>)</li> 
 <li>exact matches have a higher priority and are placed to the top of the list when fuzzily finding files (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fextrawurst%2Fgitui%2Fpull%2F1183" target="_blank">#1183</a>)</li> 
</ul> 
<p style="text-align:start"><strong>变更</strong></p> 
<ul> 
 <li>最低要求的 Rust 版本升级到 1.60 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fextrawurst%2Fgitui%2Fpull%2F1279" target="_blank">#1279</a>)</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fextrawurst%2Fgitui%2Freleases%2Ftag%2Fv0.21.0" target="_blank">详情查看 release note</a>。</p>
                                        </div>
                                      
</div>
            