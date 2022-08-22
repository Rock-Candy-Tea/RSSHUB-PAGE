
---
title: 'ohUrlShortener 短链接系统 v1.6 发布，统计功能增强'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/barat/ohurlshortener/raw/main/screenshot.jpg'
author: 开源中国
comments: false
date: Mon, 22 Aug 2022 10:03:00 GMT
thumbnail: 'https://gitee.com/barat/ohurlshortener/raw/main/screenshot.jpg'
---

<div>   
<div class="content">
                                                                                            <p>上个版本发布之后，ohUrlShortener 短链接系统收到热心网友们提出的不少问题，这个版本中对遗留的 issue 进行了处理，主要变化内容包括：</p> 
<ol> 
 <li>重新设计了统计功能的实现方法，解决统计页面相应超时或卡顿等情况</li> 
 <li>升级 Base58 相关库 btcsuite/btcutil 到 btcd/btcutil 并升级版本</li> 
 <li>Dashboard 页面新增更加丰富的统计指标</li> 
 <li>处理批量新增短链接时可能出现的重复 bug</li> 
 <li>其他部分必要的改进</li> 
</ol> 
<p>详细提交记录可以查阅 <a href="https://gitee.com/barat/ohurlshortener/commits/main">https://gitee.com/barat/ohurlshortener/commits/main</a></p> 
<hr> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">ohUrlShortener 是适合中小型社区网站使用的短链接服务系统，支持短链接生产、查询及302转向，并自带点击量统计、独立IP数统计、访问日志查询：</p> 
<ol> 
 <li>支持 Docker One Step Start 部署、Makefile 编译打包</li> 
 <li>支持短链接生产、查询、存储、302转向</li> 
 <li>支持访问日志查询、访问量统计、独立IP数统计</li> 
 <li>支持 HTTP API 方式新建短链接、禁用/启用短链接、查看短链接统计信息、新建管理员、修改管理员密码</li> 
 <li>支持访问日志导出，方便线下分析</li> 
</ol> 
<p><img alt src="https://gitee.com/barat/ohurlshortener/raw/main/screenshot.jpg" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p> </p>
                                        </div>
                                      
</div>
            