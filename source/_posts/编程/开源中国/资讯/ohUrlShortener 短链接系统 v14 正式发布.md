
---
title: 'ohUrlShortener 短链接系统 v1.4 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/barat/ohurlshortener/raw/main/screenshot.jpg'
author: 开源中国
comments: false
date: Mon, 09 May 2022 09:55:00 GMT
thumbnail: 'https://gitee.com/barat/ohurlshortener/raw/main/screenshot.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <p>应网友提出的<a href="https://gitee.com/barat/ohurlshortener/issues/I556YL"> Issue 需求</a>，ohUrlShortener 短链接系统正式发布了 v1.4 版本。</p> 
<p>此版本主要集中在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fhub.docker.com%2Fr%2Fbaratsemet%2Fohurlshortener-admin" target="_blank">ohUrlShortener-Admin</a> 管理端，内容包括：</p> 
<ol> 
 <li>「访问日志」页面查询功能增强，支持指定时间段查询访问日志</li> 
 <li>「访问日志」页面统计功能支持，支持指定时间段查询统计结果</li> 
</ol> 
<p>Docker 版本升级提示：</p> 
<ol> 
 <li>在 &#123;project&#125;/docker 目录中，执行 ./stop_desotry.sh 停止运行的容器</li> 
 <li>在 &#123;project&#125;/docker 目录中，修改 vars.env 文件中 OH_ADMIN_VERSION 、OH_PORTAL_VERSION 为 1.4</li> 
 <li>在 &#123;project&#125;/docker 目录中，执行 ./one_step_start.sh 开始拉去并启动容器</li> 
</ol> 
<hr> 
<p>适合中小型社区网站使用的短链接服务系统，支持短链接生产、查询及302转向，并自带点击量统计、独立IP数统计、访问日志查询：</p> 
<ol> 
 <li>支持 Docker One Step Start 部署、Makefile 编译打包</li> 
 <li>支持短链接生产、查询、存储、302转向</li> 
 <li>支持访问日志查询、访问量统计、独立IP数统计</li> 
 <li>支持 HTTP API 方式新建短链接、禁用/启用短链接、查看短链接统计信息、新建管理员、修改管理员密码</li> 
 <li>支持访问日志导出，方便线下分析</li> 
</ol> 
<p><img alt src="https://gitee.com/barat/ohurlshortener/raw/main/screenshot.jpg" referrerpolicy="no-referrer"></p> 
<p>欢迎感兴趣的朋友参与开源共建，项目源代码 <a href="https://gitee.com/barat/ohurlshortener">https://gitee.com/barat/ohurlshortener</a></p>
                                        </div>
                                      
</div>
            