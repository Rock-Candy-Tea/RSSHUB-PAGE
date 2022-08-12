
---
title: 'ThingsPanel-0.3.0 发布，增加规则引擎、权限系统、优化设备接入'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-7332c36c0228f9659c84e7bdb6bc9d40d30.png'
author: 开源中国
comments: false
date: Fri, 12 Aug 2022 10:24:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-7332c36c0228f9659c84e7bdb6bc9d40d30.png'
---

<div>   
<div class="content">
                                                                                            <h2 style="text-align:start">新增功能<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fthingspanel.io%2Fdocs%2Fsysteminduction%2Freleases%23%25E6%2596%25B0%25E5%25A2%259E%25E5%258A%259F%25E8%2583%25BD" target="_blank">​</a></h2> 
<ul> 
 <li>增加了Redis作为缓存模块</li> 
 <li>增加了RBAC权限管理模块，使用的是Casbin权限框架，权限粒度具体到设备、按钮或者接口</li> 
</ul> 
<p><img height="942" src="https://oscimg.oschina.net/oscnet/up-7332c36c0228f9659c84e7bdb6bc9d40d30.png" width="1920" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>增加了角色管理页面，支持多个角色。</li> 
 <li> <p><img height="942" src="https://oscimg.oschina.net/oscnet/up-4aba51f15f57e748cf3926f205f07d7ebf1.png" width="1920" referrerpolicy="no-referrer"></p> </li> 
 <li>增加了权限管理页面，权限精细到操作。</li> 
 <li><img height="942" src="https://oscimg.oschina.net/oscnet/up-7d2dbdb7d17511147c6c7ee14d70ccd1584.png" width="1920" referrerpolicy="no-referrer"> <p> </p> </li> 
 <li>系统后端增加了对Docker环境变量的支持，方便配置。</li> 
 <li>简化了部署，增加了对华为云/阿里云的适配。</li> 
 <li>增加了接入规则引擎和数据转发功能。</li> 
 <li> <p><img height="942" src="https://oscimg.oschina.net/oscnet/up-53ca996565f1d578cd6efebb0d1098947cb.png" width="1920" referrerpolicy="no-referrer"></p> </li> 
 <li> <p><img height="942" src="https://oscimg.oschina.net/oscnet/up-fcd7c03255bc00df39b6106e8a7eef2aa08.png" width="1920" referrerpolicy="no-referrer"></p> </li> 
 <li>重写了业务-设备分组-设备模块，支持设备无限分组</li> 
</ul> 
<p><img height="942" src="https://oscimg.oschina.net/oscnet/up-2ad2b68dbb16365e09bdae0eca76009ed95.png" width="1920" referrerpolicy="no-referrer"></p> 
<p><img height="435" src="https://oscimg.oschina.net/oscnet/up-a10a52c68f67ca88f11df3ebc20b36f4510.png" width="911" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>增加了操作设备的日志，支持查询手动操作和自动操作记录</li> 
</ul> 
<p><img height="942" src="https://oscimg.oschina.net/oscnet/up-45641c9bda3f802322f5b7cfc8a786d6568.png" width="1920" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:start">优化和修复<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fthingspanel.io%2Fdocs%2Fsysteminduction%2Freleases%23%25E4%25BC%2598%25E5%258C%2596%25E5%2592%258C%25E4%25BF%25AE%25E5%25A4%258D" target="_blank">​</a></h3> 
<ul> 
 <li>优化了首次登录加载速度。</li> 
 <li>优化了整体的UI。</li> 
 <li>优化了部分表索引和排序，提高了操作的流畅度。</li> 
 <li>提高了压力测试标准，对各方面性能和结构进行了优化。</li> 
 <li>优化了自动化的告警和控制策略。</li> 
 <li>重写了用户添加功能和页面。</li> 
 <li>优化了告警信息页面。</li> 
</ul>
                                        </div>
                                      
</div>
            