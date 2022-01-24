
---
title: 'yt-dlp 2022.01.21 发布，youtube-dl 分支'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4420'
author: 开源中国
comments: false
date: Mon, 24 Jan 2022 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4420'
---

<div>   
<div class="content">
                                                                                            <p>yt-dlp 是基于 youtube-dl 的一个分支，该项目的主要重点是添加新功能和补丁，同时与原始项目保持同步。</p> 
<p>yt-dlp 2022.01.21 发布，更新内容如下：</p> 
<ul> 
 <li>增加选项 <code>--concat-playlis</code> 以在一个播放列表中串联视频</li> 
 <li>允许多个和嵌套的配置文件</li> 
 <li>增加更多的后处理阶段 (<code>after_video</code>, <code>playlist</code>)</li> 
 <li>允许在任何后期处理阶段运行 <code>--exec</code></li> 
 <li>允许在任何后期处理阶段运行 <code>--print</code></li> 
 <li>允许使用 <code>-print</code> 列出格式、缩略图、字幕</li> 
 <li>添加字段 <code>video_autonumber</code>, <code>modified_date</code>, <code>modified_timestamp</code>, <code>playlist_count</code>, <code>channel_follower_count</code></li> 
 <li>只有在下载完所有格式后才写入 <code>download_archive</code></li> 
 <li>[FfmpegMetadata] 允许使用 <code>meta<n>_</code> 前缀设置单个数据流的元数据</li> 
 <li>增加选项 <code>-legacy-server-connect</code></li> 
 <li>允许在 <code>-extractor-args</code> 中使用转义 <code>,</code></li> 
 <li>允许在 <code>info.json</code> 中使用 unicode 字符</li> 
 <li>检查最终目录中是否存在缩略图/字幕</li> 
 <li>在 <code>sanitize_info</code> 中不要把空的容器当作 <code>None</code></li> 
 <li>修复 <code>s --ignore-no-formats --force-write-archive</code></li> 
 <li>修复多种格式的实时标题</li> 
 <li>在 <code>--list-thumbnails</code> 中列出播放列表缩略图</li> 
 <li>如果字幕下载失败，会引发错误</li> 
 <li>[utils] 在 <code>std_headers</code> 中增加<code>Sec-Fetch-Mode</code></li> 
 <li>[extractor] 从 JSON-LD 中提取章节</li> 
 <li>[extractor] 从 JSON-LD 中提取缩略图</li> 
 <li>[extractor] 改进<code>url_result</code>和相关的功能</li> 
 <li>[generic] 改进 KVS 播放器的提取</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyt-dlp%2Fyt-dlp%2Freleases%2F" target="_blank">https://github.com/yt-dlp/yt-dlp/releases/</a></p>
                                        </div>
                                      
</div>
            