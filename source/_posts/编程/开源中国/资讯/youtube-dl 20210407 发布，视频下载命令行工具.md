
---
title: 'youtube-dl 2021.04.07 发布，视频下载命令行工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6946'
author: 开源中国
comments: false
date: Tue, 06 Apr 2021 23:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6946'
---

<div>   
<div class="content">
                                                                    
                                                        <p>youtube-dl 是一个小型的命令行工具，用于下载视频。虽然它最初仅支持 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fyoutube.com%2F">YouTube.com</a>，但它目前已支持许多其他平台，如 Anitube、<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Farchive.org%2F">Archive.org</a>、Bloomberg、CBS、Discovery、dropbox、eHow、flickr、Google+、MTV、MyVideo、NBC、SoundCloud、Southpark、Steam 和 Vimeo 等。它可以保存视频 MP4 和其他提供的格式，也可以只提取音轨。</p> 
<p>youtube-dl 2021.04.07 正式发布，本次更新内容如下：</p> 
<p>核心</p> 
<ul> 
 <li>[extractor/common]将 compat_cookies_SimpleCookie 用于 _get_cookies；</li> 
 <li>[compat]介绍 compat_cookies_SimpleCookie；</li> 
 <li>[extractor/common]改进 JSON-LD 的作者提取；</li> 
 <li>[extractor/common] 修复 python 2 上的 _get_cookies；</li> 
</ul> 
<p>提取器</p> 
<ul> 
 <li>[youtube] 修复受限地区的视频提取；</li> 
 <li>[line] 增加对 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Flive.line.me" target="_blank">live.line.me</a> 的支持；</li> 
 <li>[vimeo] 改进提取；</li> 
 <li>[优酷]更新 ccode；</li> 
 <li>[youtube] 宁愿选择直接输入元数据，也不要从播放列表中输入元数据；</li> 
 <li>[screencastomatic] 修复提取；</li> 
 <li>[palcomp3] 增加对 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fpalcomp3.com" target="_blank">palcomp3.com</a> 的支持；</li> 
 <li>[arnes] 增加对 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fvideo.arnes.si" target="_blank">video.arnes.si</a> 的支持；</li> 
 <li>[youtube:tab] 增加对 <code>#</code> 标签的支持；</li> 
</ul>
                                        </div>
                                      
</div>
            