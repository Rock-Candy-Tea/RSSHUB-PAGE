
---
title: 'ohUrlShortener 短链接系统 v1.2 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/barat/ohurlshortener/raw/main/screenshot.jpg'
author: 开源中国
comments: false
date: Mon, 11 Apr 2022 07:09:00 GMT
thumbnail: 'https://gitee.com/barat/ohurlshortener/raw/main/screenshot.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <p>应 Gitee 中不知名网友的 <a href="https://gitee.com/barat/ohurlshortener/issues/I51TGP">issue 提议</a>，<a href="https://www.oschina.net/p/ohurlshortener">ohUrlShortener</a> 发布了 v1.2 版本，主要的变化就是加入了 HTTP API 支持，完成以下操作：</p> 
<ol> 
 <li>新增短链接 <code>POST /api/url</code></li> 
 <li>禁用/启用 短链接 <code>PUT /api/url/:url/change_state</code></li> 
 <li>查询短链接统计数据 <code>GET /api/url/:url</code></li> 
 <li>新建管理员 <code>POST /api/account</code></li> 
 <li>修改管理员密码 <code>PUT /api/account/:account/update</code></li> 
</ol> 
<p>Linux、Windows、Mac 等系统发行版下载： https://gitee.com/barat/ohurlshortener/releases/v1.2</p> 
<p> </p> 
<p>ohUrlShortener 是一个适合中小型社区网站使用的短链接服务系统，支持短链接生产、查询及302转向，并自带点击量统计、独立IP数统计、访问日志查询：</p> 
<ol> 
 <li>支持 Docker One Step Start 部署、Makefile 编译打包</li> 
 <li>支持短链接生产、查询、存储、302转向</li> 
 <li>支持访问日志查询、访问量统计、独立IP数统计</li> 
 <li>支持 HTTP API 方式新建短链接、禁用/启用短链接、查看短链接统计信息、新建管理员、修改管理员密码</li> 
</ol> 
<p><img alt="Screenshot" src="https://gitee.com/barat/ohurlshortener/raw/main/screenshot.jpg" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p>源码开放，欢迎感兴趣的朋友参与共建。</p>
                                        </div>
                                      
</div>
            