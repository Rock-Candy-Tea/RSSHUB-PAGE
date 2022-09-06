
---
title: 'Melog v3.1.0 正式发布，新版支持 Docker 部署'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4151'
author: 开源中国
comments: false
date: Tue, 06 Sep 2022 18:56:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4151'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#24292f">melog，一个基于 jj.js (nodejs) 构建的简单轻量级 blog 系统。</span></p> 
<h2 style="margin-left:0em; margin-right:0em; text-align:left">v3.1.0 更新日志</h2> 
<ul> 
 <li>[新增] 新增install模块，不用再手工导入数据库文件了</li> 
 <li>[新增] 新增docker部署，部署方式见README.md</li> 
 <li>[优化] 优化路由设置</li> 
 <li>[优化] 优化专题页显示样式</li> 
 <li>[优化] 优化前台tips函数逻辑</li> 
 <li>[修改] 默认关闭调试模式</li> 
 <li>[修改] 默认绑定ip改为0.0.0.0</li> 
 <li>[依赖] 更新依赖jj.js版本到0.8.7</li> 
 <li>[依赖] 更换依赖jimp为jimp-compact，大幅减小程序体积</li> 
</ul> 
<p><span style="background-color:#ffffff; color:#000000">项目地址：</span><span style="background-color:#ffffff; color:#000000"> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyafoo%2Fmelog" target="_blank">https://github.com/yafoo/melog</a></p> 
<p>Docker部署：</p> 
<pre><code class="language-bash"># 镜像拉取
docker pull yafoo/melog

# 容器运行
docker run -p 3003:3003 --restart unless-stopped --name melog -d yafoo/melog

# 容器运行（配置文件、站点数据保存到宿主机）
docker run -p 3003:3003 --restart unless-stopped --name melog -d -v $PWD/melog/config:/melog/config -v $PWD/melog/upload:/melog/public/upload yafoo/melog</code></pre> 
<p> </p>
                                        </div>
                                      
</div>
            