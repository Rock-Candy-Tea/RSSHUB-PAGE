
---
title: 'youtube-dl 2021.05.16 发布，视频下载命令行工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7479'
author: 开源中国
comments: false
date: Thu, 20 May 2021 07:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7479'
---

<div>   
<div class="content">
                                                                    
                                                        <p>youtube-dl 是一个小型的命令行工具，用于下载视频。虽然它最初仅支持 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fyoutube.com%2F">YouTube.com</a>，但它目前已支持许多其他平台，如 Anitube、<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Farchive.org%2F">Archive.org</a>、Bloomberg、CBS、Discovery、dropbox、eHow、flickr、Google+、MTV、MyVideo、NBC、SoundCloud、Southpark、Steam 和 Vimeo 等。它可以保存视频 MP4 和其他提供的格式，也可以只提取音轨。</p> 
<p>youtube-dl 2021.05.16 正式发布，本次更新内容如下：</p> 
<p><strong>Core</strong></p> 
<ul> 
 <li>[options] 修复缩略图选项组名称 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fpull%2F29042" target="_blank">#29042</a>)</li> 
 <li>[YoutubeDL] 改进 extract_info 文档 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fpull%2F28946" target="_blank">#28946</a>)</li> 
</ul> 
<p><strong>提取器</strong></p> 
<ul> 
 <li>[playstuff] 增加对 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fplay.stuff.co.nz" target="_blank">play.stuff.co.nz</a> 的支持 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fissues%2F28901" target="_blank">#28901</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fpull%2F28931" target="_blank">#28931</a>)</li> 
 <li>[eroprofile] 修复提取 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fissues%2F23200" target="_blank">#23200</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fpull%2F23626" target="_blank">#23626</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fissues%2F29008" target="_blank">#29008</a>)</li> 
 <li>[vivo] 增加对 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fvivo.st" target="_blank">vivo.st</a> 的支持 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fpull%2F29009" target="_blank">#29009</a>)</li> 
 <li>[generic] 增加对 og:audio 的支持 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fissues%2F28311" target="_blank">#28311</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fpull%2F29015" target="_blank">#29015</a>)</li> 
 <li>[phoenix] 修复提取 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fissues%2F29057" target="_blank">#29057</a>)</li> 
 <li>[generic] 添加对 sibnet 嵌入的支持</li> 
 <li>[generic] 为直接 videojs 下载 URL 添加 Referer header (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fissues%2F2879" target="_blank">#2879</a>,<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fissues%2F20217" target="_blank">#20217</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fissues%2F29053" target="_blank">#29053</a>)</li> 
 <li>[orf:radio] 将下载 URLs 切换到 HTTPS (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fissues%2F29012" target="_blank">#29012</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fpull%2F29046" target="_blank">#29046</a>)</li> 
 <li>[blinkx] 删除提取器 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fissues%2F28941" target="_blank">#28941</a>)</li> 
 <li>[medaltv] 放宽 URL 正则表达式 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fpull%2F28884" target="_blank">#28884</a>)</li> 
 <li>[funimation] 增加对 URL 中可选语言代码的支持 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fpull%2F28950" target="_blank">#28950</a>)</li> 
 <li>[gdcvault] 增加对 HTML5 视频的支持</li> 
 <li>[dispeak] 改进 FLV 提取 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fissues%2F13513" target="_blank">#13513</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fpull%2F28970" target="_blank">#28970</a>)</li> 
 <li>[kaltura] 改进 iframe 提取 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fpull%2F28969" target="_blank">#28969</a>)</li> 
 <li>[kaltura] 让嵌入代码的替代品真正发挥作用</li> 
 <li>[cda] 改进提取功能 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fissues%2F28709" target="_blank">#28709</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fpull%2F28937" target="_blank">#28937</a>)</li> 
 <li>[twitter] 改进从 vmap URL 的格式提取 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fissues%2F28909" target="_blank">#28909</a>)</li> 
 <li>[xtube] 修复格式提取 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fissues%2F28870" target="_blank">#28870</a>)</li> 
 <li>[svtplay] 改进提取 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fissues%2F28507" target="_blank">#28507</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fissues%2F28876" target="_blank">#28876</a>)</li> 
 <li>[tv2dk] 修复提取功能 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fissues%2F28888" target="_blank">#28888</a>)</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Freleases%2Ftag%2F2021.05.16" target="_blank">https://github.com/ytdl-org/youtube-dl/releases/tag/2021.05.16</a></p>
                                        </div>
                                      
</div>
            