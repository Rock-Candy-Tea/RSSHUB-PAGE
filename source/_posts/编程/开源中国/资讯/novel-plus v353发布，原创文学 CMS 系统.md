
---
title: 'novel-plus v3.5.3发布，原创文学 CMS 系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://s3.ax1x.com/2020/12/27/r5400A.png'
author: 开源中国
comments: false
date: Sat, 29 May 2021 07:54:00 GMT
thumbnail: 'https://s3.ax1x.com/2020/12/27/r5400A.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left">novel-plus v3.5.3发布了，主要改进包括：</p> 
<ul> 
 <li style="text-align:justify">[优化]图片上传流程优化</li> 
 <li style="text-align:justify">[优化]首页SEO优化</li> 
 <li style="text-align:justify">[优化]小说详情页SEO优化</li> 
</ul> 
<h4 style="text-align:left">演示站点</h4> 
<p style="text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2F47.106.243.172%3A8888%2F" target="_blank">点击前往</a></p> 
<h4 style="text-align:start">项目介绍</h4> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2F201206030%2Ffiction_house" target="_blank">小说精品屋</a>是一个多平台（web、安卓app、微信小程序）、功能完善的屏幕自适应小说漫画连载系统，包含精品小说专区、轻小说专区和漫画专区。包括小说/漫画分类、小说/漫画搜索、小说/漫画排行、完本小说/漫画、小说/漫画评分、小说/漫画在线阅读、小说/漫画书架、小说/漫画阅读记录、小说TXT下载、小说弹幕、小说/漫画自动爬取、小说内容自动分享到微博、邮件自动推广、链接自动推送到百度搜索引擎等功能。包含电脑端、移动端、微信小程序等多个平台。</p> 
<p style="text-align:left">小说精品屋-plus是在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2F201206030%2Ffiction_house" target="_blank">小说精品屋</a>的基础上，去除了漫画和弹幕模块，专注于小说，<span style="background-color:#ffffff; color:#444444">是一个多端（PC、WAP）阅读、功能完善的原创文学CMS系统，由前台门户系统、作家后台管理系统、平台后台管理系统、爬虫管理系统等多个子系统构成，支持多模版、会员充值、订阅模式、新闻发布和实时统计报表等功能，新书自动入库，老书自动更新。</span></p> 
<p style="text-align:left">小说精品屋-plus重新进行了数据库设计、代码重构和功能增强，提升了程序整体的可读性和性能，增加了很多商用特性。主要增强如下：</p> 
<ul> 
 <li>数据库重新设计，结构调整。</li> 
 <li> 服务端代码重构，MyBatis3升级为MyBatis3DynamicSql。</li> 
 <li> 移动站与PC站站点分离，浏览器自动识别跳转。</li> 
 <li> PC站UI更新。</li> 
 <li> 支持前端模版自定义，内置多套模版。</li> 
 <li> 新闻模块。</li> 
 <li> 排行榜。</li> 
 <li> 小说评论模块。</li> 
 <li> 阅读主题模块。</li> 
 <li> 作家专区。</li> 
 <li> 充值。</li> 
 <li> 订阅。</li> 
 <li> 后台管理系统。</li> 
 <li> 爬虫管理系统。</li> 
</ul> 
<h4 style="text-align:start">项目结构</h4> 
<div style="text-align:start"> 
 <div> 
  <pre style="text-align:left">novel-plus <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">-- 父工程</span></span></span></span></span></span>
├── novel-common <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">-- 通用模块</span></span></span></span></span></span>
├── novel-front <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">-- 前台门户&作家后台管理子系统（可拆分）</span></span></span></span></span></span>
├── novel-crawl <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">-- 爬虫管理子系统</span></span></span></span></span></span>
├── novel-admin <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">-- 平台后台管理子系统</span></span></span></span></span></span>
└── templates <span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d"><span style="color:#6a737d">-- 前端模版</span></span></span></span></span></span></pre> 
 </div> 
</div> 
<h4 style="text-align:start">技术选型</h4> 
<table cellspacing="0" style="width:942px"> 
 <thead> 
  <tr> 
   <th>技术</th> 
   <th>说明</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5">SpringBoot</td> 
   <td style="border-color:#dfe2e5">Spring应用快速开发脚手架</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">MyBatis</td> 
   <td style="border-color:#dfe2e5">持久层ORM框架</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">MyBatis Dynamic SQL</td> 
   <td style="border-color:#dfe2e5">Mybatis动态sql</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">PageHelper</td> 
   <td style="border-color:#dfe2e5">MyBatis分页插件</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">MyBatisGenerator</td> 
   <td style="border-color:#dfe2e5">持久层代码生成插件</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Sharding-Jdbc</td> 
   <td style="border-color:#dfe2e5">代码层分库分表中间件</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">JJWT</td> 
   <td style="border-color:#dfe2e5">JWT登录支持</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">SpringSecurity</td> 
   <td style="border-color:#dfe2e5">安全框架</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Shiro</td> 
   <td style="border-color:#dfe2e5">安全框架</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Ehcache</td> 
   <td style="border-color:#dfe2e5">Java进程内缓存框架(默认缓存)</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Redis</td> 
   <td style="border-color:#dfe2e5">分布式缓存(缓存替换方案，默认关闭，一行配置开启)</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">ElasticSearch</td> 
   <td style="border-color:#dfe2e5">搜索引擎(搜索增强方案，默认关闭，一行配置开启)</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">RabbitMq</td> 
   <td style="border-color:#dfe2e5">消息队列(流量削峰，默认关闭，一行配置开启)</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">OSS</td> 
   <td style="border-color:#dfe2e5">阿里云对象存储服务(图片存储方式之一，一行配置即可切换)</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">FastDfs</td> 
   <td style="border-color:#dfe2e5">开源轻量级分布式文件系统(图片存储方式之一，一行配置即可切换)</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Redisson</td> 
   <td style="border-color:#dfe2e5">实现分布式锁</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Lombok</td> 
   <td style="border-color:#dfe2e5">简化对象封装工具</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Docker</td> 
   <td style="border-color:#dfe2e5">应用容器引擎</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Mysql</td> 
   <td style="border-color:#dfe2e5">数据库服务</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Thymeleaf</td> 
   <td style="border-color:#dfe2e5">模板引擎</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5">Layui</td> 
   <td style="border-color:#dfe2e5">前端UI</td> 
  </tr> 
 </tbody> 
</table> 
<h4 style="text-align:left">橙色主题模版截图</h4> 
<p style="text-align:left">PC站截图</p> 
<ol> 
 <li>首页</li> 
</ol> 
<p style="text-align:left"><img alt="img" src="https://s3.ax1x.com/2020/12/27/r5400A.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">2. 分类索引页</p> 
<p style="text-align:left"><img alt="img" src="https://oscimg.oschina.net/oscnet/up-d0b2e03129bfae47b8bb96a491b73d383c5.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">3. 搜索页</p> 
<p style="text-align:left"><img alt="img" src="https://s3.ax1x.com/2020/12/27/r5TO8x.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">4. 排行榜</p> 
<p style="text-align:left"><img alt="img" src="https://oscimg.oschina.net/oscnet/up-78d5a68586cd92a86c669311f414508f922.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">5. 详情页</p> 
<p style="text-align:left"><img alt="img" src="https://oscimg.oschina.net/oscnet/up-8be2495a2869f93626b0c9c1df6f329747a.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">6. 阅读页</p> 
<p style="text-align:left"><img alt="img" src="https://oscimg.oschina.net/oscnet/up-517c84148d2db8e11717a8bbecc57fa1be7.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">7. 用户中心</p> 
<p style="text-align:left"><img alt="img" src="https://oscimg.oschina.net/oscnet/up-805a30e7a663a3fd5cb39a7ea26bc132a01.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">8. 充值</p> 
<p style="text-align:left"><img alt="img" src="https://oscimg.oschina.net/oscnet/up-5a601b0b3af3224d0bebcfe12fc15075d34.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><img alt="img" src="https://oscimg.oschina.net/oscnet/up-face25d02c07b05b2ce954cc4bf4ee6a0cc.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">9. 作家专区</p> 
<p style="text-align:left"><img alt="img" src="https://s3.ax1x.com/2020/11/17/DVFiQI.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">10. 购买</p> 
<p style="text-align:left"><img alt="img" src="https://oscimg.oschina.net/oscnet/up-f849960f4c1303fea77d26e64fc505a7180.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">手机站截图</p> 
<ol> 
 <li> <p>首页</p> <img alt="index" src="https://s3.ax1x.com/2020/12/27/r5447n.jpg" width="300" referrerpolicy="no-referrer"></li> 
 <li> <p>小说列表页</p> <img alt="微信图片_20190904181558" src="https://s3.ax1x.com/2020/12/27/r55xKg.jpg" width="300" referrerpolicy="no-referrer"></li> 
 <li> <p>小说详情页</p> <img alt="QQ图片20191018161901" src="https://s3.ax1x.com/2020/12/28/roZWOf.jpg" width="300" referrerpolicy="no-referrer"></li> 
 <li> <p>小说阅读页</p> <img alt="QQ图片20191018161901" src="https://s3.ax1x.com/2020/12/27/r55Stx.jpg" width="300" referrerpolicy="no-referrer"></li> 
</ol> 
<p style="text-align:left">爬虫管理系统截图</p> 
<p style="text-align:left"><img alt="img" src="https://s1.ax1x.com/2020/11/03/BsOgbD.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"> </p> 
<p style="text-align:left">后台管理系统截图</p> 
<p style="text-align:left"><img alt="img" src="https://s3.ax1x.com/2020/12/01/DWgLNT.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"> </p> 
<h4 style="text-align:left">深色主题模版截图</h4> 
<p style="text-align:left">PC站截图</p> 
<ol> 
 <li> <p>首页</p> <p><img alt="index" src="https://static.oschina.net/uploads/img/202006/24151811_wIus.png" referrerpolicy="no-referrer"></p> </li> 
</ol> 
<p style="text-align:left">手机站截图</p> 
<ol> 
 <li> <p>首页</p> <p><img alt="index" src="https://static.oschina.net/uploads/img/202006/24151812_OOob.jpg" referrerpolicy="no-referrer"></p> </li> 
 <li> <p>小说详情页</p> <p><img alt="微信图片_20190904181558" src="https://static.oschina.net/uploads/img/202006/24151812_ZosF.png" referrerpolicy="no-referrer"></p> </li> 
 <li> <p>目录页</p> <p><img alt="QQ图片20191018161901" src="https://static.oschina.net/uploads/img/202006/24151812_Krva.png" referrerpolicy="no-referrer"></p> </li> 
 <li> <p>小说阅读页</p> <p><img alt="QQ图片20191018161901" src="https://static.oschina.net/uploads/img/202006/24151813_fDgT.png" referrerpolicy="no-referrer"></p> </li> 
</ol> 
<h4 style="text-align:left">蓝色主题模版截图（更新中）</h4> 
<p style="text-align:left"><img alt="QQ图片20191018161901" src="https://s3.ax1x.com/2020/12/27/r5Fe0A.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:start"><strong>喜欢此项目的可以给我的GitHub和Gitee加个Star支持一下 。</strong></p> 
<h4 style="text-align:start">代码仓库</h4> 
<p style="text-align:left"><span style="color:#000000">Gitee仓库地址：https://gitee.com/novel_dev_team/novel-plus</span></p> 
<p style="text-align:justify"><span style="color:#000000">GitHub仓库地址：https://github.com/201206030/novel-plus</span></p>
                                        </div>
                                      
</div>
            