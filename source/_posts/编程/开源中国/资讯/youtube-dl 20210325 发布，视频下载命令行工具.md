
---
title: 'youtube-dl 2021.03.25 发布，视频下载命令行工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6188'
author: 开源中国
comments: false
date: Fri, 26 Mar 2021 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6188'
---

<div>   
<div class="content">
                                                                                            <p>youtube-dl 是一个小型的命令行工具，用于下载视频。虽然它最初仅支持 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fyoutube.com%2F" target="_blank">YouTube.com</a>，但它目前已支持许多其他平台，如 Anitube、<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Farchive.org%2F" target="_blank">Archive.org</a>、Bloomberg、CBS、Discovery、dropbox、eHow、flickr、Google+、MTV、MyVideo、NBC、SoundCloud、Southpark、Steam 和 Vimeo 等。它可以保存视频 MP4 和其他提供的格式，也可以只提取音轨。</p> 
<p>youtube-dl 2021.03.25 正式发布，本次更新内容如下：</p> 
<p>提取器：</p> 
<ul> 
 <li>[zoom] 增加对 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fzoom.us" target="_blank">zoom.us</a> 的支持 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fissues%2F16597" target="_blank">#16597</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fpull%2F27002" target="_blank">#27002</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fissues%2F28531" target="_blank">#28531</a>)</li> 
 <li>[bbc] 修复 BBC IPlayer 剧集/群组提取 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fpull%2F28360" target="_blank">#28360</a>)</li> 
 <li>[youtube] 修正 youtube_include_dash_manifest 的默认值 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fissues%2F28523" target="_blank">#28523</a>)</li> 
 <li>[zingmp3] 修复提取 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fpull%2F11589" target="_blank">#11589</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fissues%2F16409" target="_blank">#16409</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fpull%2F16968" target="_blank">#16968</a>, <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fissues%2F27205" target="_blank">#27205</a>)</li> 
 <li>[vgtv] 增加对新的 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Ftv.aftonbladet.se" target="_blank">tv.aftonbladet.se</a> URL模式的支持 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fpull%2F28514" target="_blank">#28514</a>)</li> 
 <li>[tiktok] 检测被设为私人的视频 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fissues%2F28453" target="_blank">#28453</a>)</li> 
 <li>[vvvvid] 修复 kenc 格式提取 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fissues%2F28473" target="_blank">#28473</a>)</li> 
 <li>[mlb] 修复视频提取 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fissues%2F21241" target="_blank">#21241</a>)</li> 
 <li>[svtplay] 改进提取 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fissues%2F28448" target="_blank">#28448</a>)</li> 
 <li>[applepodcasts] 修复提取 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fissues%2F28445" target="_blank">#28445</a>)</li> 
 <li>[rtve] 改进提取 
  <ul> 
   <li>提取所有格式</li> 
   <li>修复 RTVE Infantil 提取 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Fpull%2F24851" target="_blank">#24851</a>)</li> 
   <li>提取 is_live 和 series</li> 
  </ul> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fytdl-org%2Fyoutube-dl%2Freleases%2Ftag%2F2021.03.25" target="_blank">https://github.com/ytdl-org/youtube-dl/releases/tag/2021.03.25</a></p>
                                        </div>
                                      
</div>
            