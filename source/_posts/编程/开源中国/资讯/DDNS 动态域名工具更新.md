
---
title: 'DDNS 动态域名工具更新'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6892'
author: 开源中国
comments: false
date: Sun, 29 Aug 2021 08:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6892'
---

<div>   
<div class="content">
                                                                                            <p>DDNS 是一个动态域名工具，本次更新如下说明：</p> 
<ul> 
 <li>去掉不稳定的外网IP查询工具类和不必要的依赖</li> 
 <li>框架升级为spring-boot2.1.3</li> 
 <li>去掉quartz和jsoup</li> 
 <li>去掉脚本和配置文件</li> 
 <li>更新逻辑，支持新域名RR，如果当前RR不存在，则会新增一条域名解析记录</li> 
 <li>封装Docker，同时支持arm和x86架构</li> 
</ul>
                                        </div>
                                      
</div>
            