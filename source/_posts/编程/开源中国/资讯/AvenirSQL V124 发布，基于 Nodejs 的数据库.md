
---
title: 'AvenirSQL V1.2.4 发布，基于 Node.js 的数据库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2337'
author: 开源中国
comments: false
date: Sat, 07 Aug 2021 09:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2337'
---

<div>   
<div class="content">
                                                                    
                                                        <p>AvenirSQL V1.2.4 已经发布，基于 Node.js 的数据库。</p> 
<p>此版本更新内容包括：</p> 
<p>功能： 1.增加set命令，支持查看数据库的配置以及修改配置。</p> 
<p>详情查看：<a href="https://gitee.com/onlyyyy/AvenirSQL/releases/V1.2.4">https://gitee.com/onlyyyy/AvenirSQL/releases/V1.2.4</a></p> 
<h2>介绍</h2> 
<p>用Node.js设计一个数据库，支持常见的SQL语句</p> 
<h2>安装使用</h2> 
<p><code>git clone https://gitee.com/onlyyyy/AvenirSQL</code></p> 
<p><code>cd AvenirSQL</code></p> 
<p><code>npm i pm2 -g</code> 安装pm2管理工具</p> 
<p><code>pm2 start AvenirSQL</code> 注意查看run.ini 设置数据库的配置文件</p> 
<p>更新配置需要重启数据库</p> 
<p><code>pm2 restart AvenirSQL</code></p> 
<p>建议使用高版本Node.js(v14+),通过版本管理工具n进行更新：</p> 
<p><strong>目前n只支持Mac和Linux</strong></p> 
<pre>npm i n -g

n lts//下载最新版Nodejs</pre> 
<h2>技术特点</h2> 
<ul> 
 <li>1.支持增删改查</li> 
 <li>2.精确查找支持哈希索引，范围查找支持B+树索引</li> 
 <li>3.智能缓存，提升QPS性能</li> 
 <li>4.提供用户管理，cli程序(curl.js)</li> 
 <li>5.实现串行锁功能</li> 
 <li>6.灵活的策略配置</li> 
</ul>
                                        </div>
                                      
</div>
            