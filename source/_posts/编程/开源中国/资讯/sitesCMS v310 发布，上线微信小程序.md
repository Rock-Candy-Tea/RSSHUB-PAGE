
---
title: 'sitesCMS v3.1.0 发布，上线微信小程序'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-0c8b0af5b24ee10a2f23b8335dcc583ef1b.jpg'
author: 开源中国
comments: false
date: Wed, 29 Jun 2022 06:25:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-0c8b0af5b24ee10a2f23b8335dcc583ef1b.jpg'
---

<div>   
<div class="content">
                                                                                            <h3 style="margin-left:0; margin-right:0; text-align:justify">sitesCMS简介</h3> 
<p style="color:inherit; margin-left:0; margin-right:0; text-align:justify">sitesCMS 是基于<span> </span><strong style="color:inherit">JFinal</strong><span> </span>的<span> </span><strong style="color:inherit">多站点</strong><span> </span>CMS内容管理系统，遵循JFinal极简设计理念，轻量级、易扩展、学习简单，除JFinal外无其他重度依赖。精简的多站点功能设计，极易二次开发，一天一个网站不是梦。完善的API模块，支持<span> </span><strong style="color:inherit">微信小程序</strong><span> </span>、APP等各类小程序前端对接，打通移动端开发渠道，sitesCMS 不只是 CMS。<br> 官方网站：<code>http://sitescms.top/</code><br> 视频教程：<code>https://ke.qq.com/course/3551225?tuin=92419b8c</code></p> 
<h3 style="margin-left:0; margin-right:0; text-align:justify">更新内容</h3> 
<h4 style="margin-left:0; margin-right:0; text-align:justify"><span style="color:inherit">上线微信小程序</span></h4> 
<p style="color:inherit; margin-left:0; margin-right:0; text-align:justify">上线sitesCMS官方小程序，自主研发。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:center"><img alt height="344" src="https://oscimg.oschina.net/oscnet/up-0c8b0af5b24ee10a2f23b8335dcc583ef1b.jpg" width="344" referrerpolicy="no-referrer"></p> 
<p style="color:inherit; margin-left:0; margin-right:0; text-align:justify">前端使用<code>uniapp</code>框架，基于uniapp的跨平台功能，理论上还可以发布官方APP、H5网站、支付宝等各类小程序。官方小程序仅仅是一个简单的前端开发产物，有价值的是借助这次开发搭建了一个自有<strong style="color:inherit">前端开发脚手架</strong>，里面集成了请求处理插件(请求拦截器、响应拦截器)、样式框架、数据展示等常用基础功能，为后续移动端开发奠定基础。<br> 后端完全依赖于sitesCMS，在<code>cms</code>、<code>cds</code>的基础上新增<code>api</code>模块，支持前后端分离模式的接口验证、数据交互，为后续的移动端扩展提供基础能力。这也是本次升级的核心内容，通过开发一个自有小程序为sitesCMS添加了api模块功能，为后续的小程序、app等移动端开发奠定了基础。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:justify"><span style="color:inherit">官网支持https访问</span></h4> 
<p style="color:inherit; margin-left:0; margin-right:0; text-align:justify">小程序的请求必须是https的，为了处理小程序数据请求特意为官网配置了https服务处理，基于sitesCMS是很容易开通https请求处理能力的，只需四步：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:inherit">申请SSL证书，从阿里云申请免费的就行；</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:inherit">将证书文件放置到resources目录；</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:inherit">修改undertow.txt配置文件，添加https相关配置；</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span style="color:inherit">开放服务器443端口权限；</span></p> </li> 
</ul> 
<p style="color:inherit; margin-left:0; margin-right:0; text-align:justify">打完收工。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:justify">后续计划</h3> 
<h4 style="margin-left:0; margin-right:0; text-align:justify"><span style="color:inherit">完善微信小程序</span></h4> 
<p style="color:inherit; margin-left:0; margin-right:0; text-align:justify">现在发布的只是初始版本，功能比较简单，后续肯定还会逐步丰富小程序功能，借此进一步完善脚手架搭建。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:justify"><span style="color:inherit">完善api模块</span></h4> 
<p style="color:inherit; margin-left:0; margin-right:0; text-align:justify">api模块的终极目标是预制所有接口验证的通用功能，比如IP白名单、登录、token验证、参数验证等，现在已经具备了基础模型，后续会逐步完善。</p> 
<h4 style="margin-left:0; margin-right:0; text-align:justify"><span style="color:inherit">uniapp视频教程</span></h4> 
<p style="color:inherit; margin-left:0; margin-right:0; text-align:justify">虽然现在已经有很多uniapp视频教程了，但是多数还都是面向纯前端开发人员的，很少有针对像我这种<strong style="color:inherit">伪全栈</strong>人员的，后续准备自己出一套uniapp相关的视频教程，希望能帮助到一些伪全栈开发人员。</p> 
<p> </p> 
<p> </p>
                                        </div>
                                      
</div>
            