
---
title: 'backup-db 2.0.0 发布，带 Web 管理界面的数据库备份工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://raw.githubusercontent.com/jeessy2/backup-db/master/backup-db-web.png'
author: 开源中国
comments: false
date: Fri, 12 Nov 2021 16:02:00 GMT
thumbnail: 'https://raw.githubusercontent.com/jeessy2/backup-db/master/backup-db-web.png'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:start">原理：Docker容器中安装postgres-client和mysql-client，并加入本备份工具，增强备份功能。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><strong>v2.0.0全新升级：</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>一个镜像同时支持postgres和mysql/mariadb</li> 
 <li>支持webhook通知</li> 
 <li>支持备份后的文件另存到对象存储中</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:start"><strong><span style="background-color:#ffffff; color:#333333">现有功能：</span></strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> 支持自定义命令</li> 
 <li>网页中配置，简单又方便</li> 
 <li>支持多个项目备份，最多16个</li> 
 <li>支持备份后的文件另存到对象存储(在也怕硬盘坏了)</li> 
 <li>每日凌晨自动备份</li> 
 <li>可设置备份文件最大保存天数</li> 
 <li>可设置登陆用户名密码，默认为空</li> 
 <li>webhook通知 <p> </p> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>docker中使用（</strong>登录 http://your_docker_ip:9977 并配置<strong>）</strong></p> 
<pre><code>docker run -d \
  --name backup-db \
  --restart=always \
  -p 9977:9977 \
  -v /opt/backup-db-files:/app/backup-db-files \
  jeessy/backup-db</code></pre> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
</ul> 
<p><img align="left" src="https://raw.githubusercontent.com/jeessy2/backup-db/master/backup-db-web.png" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p> </p>
                                        </div>
                                      
</div>
            