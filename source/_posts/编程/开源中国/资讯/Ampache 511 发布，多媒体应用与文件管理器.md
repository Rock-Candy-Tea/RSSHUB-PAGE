
---
title: 'Ampache 5.1.1 发布，多媒体应用与文件管理器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7928'
author: 开源中国
comments: false
date: Sat, 13 Nov 2021 07:32:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7928'
---

<div>   
<div class="content">
                                                                                            <p>Ampache 是一款安装在服务端的、提供音乐管理、播放、更新服务的软件。用户可以通过网络使用该软件提供的各种功能。Ampache 还允许多帐户管理、保存播放列表和共享列表等，是一个优秀的在线音乐服务解决方案。</p> 
<h3>新增</h3> 
<ul> 
 <li>清理不在数据库中的缓存文件</li> 
 <li>在配置中添加 transcode_flv</li> 
 <li>在专辑搜索中添加播放列表、播放列表名称</li> 
 <li>当配置未被写入时，将用户发送到错误页面</li> 
 <li>配置版本 58 
  <ul> 
   <li>删除了subsonic_stream_scrobble</li> 
  </ul> </li> 
 <li>Database 5.1.0 Build 5: 
  <ul> 
   <li>添加 <code>subsonic_always_download</code> 到偏好设置中</li> 
  </ul> </li> 
</ul> 
<h3>更改</h3> 
<ul> 
 <li>从源头重新构建 aurora.js 模块</li> 
 <li>以同样的方式在磁盘上执行波形和缓存</li> 
 <li>通过连接而不是选择来使流派搜索更快</li> 
 <li>当使用浏览/播放列表时，为压缩文件发送一个平面文件路径</li> 
</ul> 
<h3>移除</h3> 
<ul> 
 <li>移除仪表板上的播客链接</li> 
 <li>从配置中删除 subsonic_stream_scrobble</li> 
</ul> 
<h3>修复</h3> 
<ul> 
 <li>在html5播放器中的翻译中使用加点符号</li> 
 <li>再次为localplay发送通用的客户端名称</li> 
 <li>对 localplay 的访问使用设置的权限级别</li> 
 <li>网络播放器的播放列表在移动/添加后会被打乱顺序</li> 
 <li>缓存过程可能会缓存错误的歌曲</li> 
 <li>搜索中缺失用户 ID</li> 
 <li>设置 Localplay 播放实例不会更新首选项</li> 
 <li>……</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fampache%2Fampache%2Freleases%2Ftag%2F5.1.1" target="_blank">https://github.com/ampache/ampache/releases/tag/5.1.1</a></p>
                                        </div>
                                      
</div>
            