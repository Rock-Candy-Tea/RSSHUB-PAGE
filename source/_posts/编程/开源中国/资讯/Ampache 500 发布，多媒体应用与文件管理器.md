
---
title: 'Ampache 5.0.0 发布，多媒体应用与文件管理器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8904'
author: 开源中国
comments: false
date: Thu, 02 Sep 2021 06:26:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8904'
---

<div>   
<div class="content">
                                                                                            <p>Ampache 是一款安装在服务端的、提供音乐管理、播放、更新服务的软件。用户可以通过网络使用该软件提供的各种功能。Ampache 还允许多帐户管理、保存播放列表和共享列表等，是一个优秀的在线音乐服务解决方案。</p> 
<p>Ampache 5.0.0 发布，更新内容如下：</p> 
<ul> 
 <li>Ampache 现在不再使用 date()，而是使用 IntlDateFormatter 和你的地区设置来识别格式。这意味着基于 date() 格式的 'custom_datetime' 是不正确的。因此 Ampache 现在需要启用 php-intl module/dll。</li> 
 <li>对于新的安装，默认的数据库 charset/collation 和表引擎已经发生了改变 
  <ul> 
   <li>MyISAM => InnoDB</li> 
   <li>utf8 => utf8mb4</li> 
   <li>utf8_unicode_ci => utf8mb4_unicode_ci</li> 
   <li>设置 <code>database_charset = "utf8"</code></li> 
   <li>设置 <code>database_collation = "utf8_unicode_ci"</code></li> 
  </ul> </li> 
</ul> 
<p>新增：</p> 
<ul> 
 <li>私人目录 —— 你现在可以为你的音乐文件夹设置一个公共或每个用户的目录</li> 
 <li>在用户请求转码之前用转码缓存来缓存转码文件</li> 
 <li>增加了一个 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fcontributing.md%2F" target="_blank">CONTRIBUTING.md</a> 文件</li> 
 <li>现在需要 php-intl 来将日期格式转换成你的地区语言</li> 
 <li>增加了按原始年份浏览专辑的功能</li> 
 <li>在 WebUI 中添加了 CatalogUpdate 导入命令</li> 
 <li>新的数据库选项 
  <ul> 
   <li>use_original_year: 按专辑的原始年份浏览</li> 
   <li>hide_single_artist: 对于只有一个艺术家的专辑，隐藏歌曲艺术家栏</li> 
   <li>show_license: 在歌曲行中隐藏许可证栏</li> 
   <li>hide_genres: 隐藏所有浏览表行中的流派列</li> 
  </ul> </li> 
 <li>新的 cli 命令 
  <ul> 
   <li><code>run:moveCatalogPath</code>: 改变一个目录路径</li> 
   <li><code>run:cacheProcess</code>: 运行缓存过程</li> 
   <li><code>export:databaseArt</code>: 导出所有数据库艺术到 local_metadata_dir</li> 
  </ul> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fampache%2Fampache%2Freleases%2Ftag%2F5.0.0" target="_blank">https://github.com/ampache/ampache/releases/tag/5.0.0</a></p>
                                        </div>
                                      
</div>
            