
---
title: 'GoSkeleton v1.5.40 已经发布，基于 Gin 框架封装的 Web 项目骨架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9271'
author: 开源中国
comments: false
date: Tue, 25 Jan 2022 10:48:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9271'
---

<div>   
<div class="content">
                                                                                            <p>GoSkeleton v1.5.40 已经发布，基于 Gin 框架封装的 Web 项目骨架</p> 
<p>此版本更新内容包括：</p> 
<h4>V 1.5.40 2022-01-25 (最新版本)</h4> 
<ul> 
 <li>新增</li> 
</ul> 
<ul> 
 <li>1.用户 <code>token</code> 缓存到 <code>redis</code> 功能,如果项目使用了 <code>redis</code> , 请直接在 config/config.yml 文件中设置 <code>Token.IsCacheToRedis = 1</code></li> 
 <li>2.项目初始化时增加设置信任代理服务器ip列表，gin(v1.7.7)新增功能,详情参见相关配置项说明.</li> 
</ul> 
<ul> 
 <li>更新</li> 
</ul> 
<ul> 
 <li>1.配置文件缓存时加锁,避免开发者频繁注册时,程序出现提示。</li> 
 <li>2.用户token鉴权时,如果开启了redis缓存功能，优先查询redis.</li> 
 <li>3.users_for_postgresql 、users_for_sqlserver 文件同步更新 .</li> 
 <li>4.所有底层依赖包更新至最新版.</li> 
</ul> 
<p>详情查看：<a href="https://gitee.com/daitougege/GinSkeleton/releases/v1.5.40">https://gitee.com/daitougege/GinSkeleton/releases/v1.5.40</a></p>
                                        </div>
                                      
</div>
            