
---
title: 'Ampache 4.4.3 发布，多媒体应用与文件管理器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4309'
author: 开源中国
comments: false
date: Sun, 06 Jun 2021 07:16:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4309'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Ampache 是一款安装在服务端的、提供音乐管理、播放、更新服务的软件。用户可以通过网络使用该软件提供的各种功能。Ampache 还允许多帐户管理、保存播放列表和共享列表等，是一个优秀的在线音乐服务解决方案。</p> 
<p>Ampache 4.4.3 已发布，更新内容如下：</p> 
<p><strong>新增：</strong></p> 
<ul> 
 <li>Catalog::update_counts 来管理目录变化；</li> 
 <li>从你的标签中收集更多的艺术文件；</li> 
 <li>允许 RatingMatch 插件对 ”专辑->艺术家“ 进行评级（原来是歌曲->专辑->艺术家）；</li> 
</ul> 
<p><strong>改变</strong>：</p> 
<ul> 
 <li>在转码时计算 MP3 流的长度以避免提前切断它；</li> 
</ul> 
<p><strong>删除：</strong></p> 
<ul> 
 <li>当专辑艺术家不明显时不要应用它</li> 
</ul> 
<p><strong>修复：</strong></p> 
<ul> 
 <li>CVE-2021-32644</li> 
 <li>识别一个独特的 album_artist 查询；</li> 
 <li>搜索文件标签时不要返回重复的艺术作品；</li> 
 <li>random::advanced_sql 中的 SQL 查询有歧义；</li> 
 <li>过滤随机和搜索页面类型元素；</li> 
 <li>现在播放的统计数据在不需要的时候会被覆盖掉；</li> 
 <li>SubSonic: 
  <ul> 
   <li>getNowPlaying 无法返回正在播放的媒体或正确的时间；</li> 
   <li>createShare 不能正确设置 object_id，并且忽略了 expires 值；</li> 
  </ul> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fampache%2Fampache%2Freleases%2Ftag%2F4.4.3" target="_blank">https://github.com/ampache/ampache/releases/tag/4.4.3</a></p>
                                        </div>
                                      
</div>
            