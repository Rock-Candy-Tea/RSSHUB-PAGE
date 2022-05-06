
---
title: '🔥🔥🔥Mall4j 2.1 发布拉~ 后台管理 vue 升级~'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-13fa9c7f53fafedd5a5b834159f664eacf0.png'
author: 开源中国
comments: false
date: Fri, 06 May 2022 09:52:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-13fa9c7f53fafedd5a5b834159f664eacf0.png'
---

<div>   
<div class="content">
                                                                                            <p><img src="https://oscimg.oschina.net/oscnet/up-13fa9c7f53fafedd5a5b834159f664eacf0.png" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0em; margin-right:0em; text-align:start">后台管理 vue 项目 mall4v 升级</p> 
<ol> 
 <li> <p style="margin-left:0; margin-right:0"><strong>升级 vue/cli 创建</strong></p> <p style="margin-left:0; margin-right:0">使用新版本<span> </span><code>vue/cli</code><span> </span>重构项目，兼容高版本<span> </span><code>node</code></p> <p style="margin-left:0; margin-right:0">移除<span> </span><code>gulp</code><span> </span>，改用<span> </span><code>cli</code><span> </span>内置<span> </span><code>webpack</code><span> </span>编译，提升速率</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>前端登录重构</strong></p> <p style="margin-left:0; margin-right:0">前端使用密钥对时间戳+密码组成的字符串进行ASE加密</p> <p style="margin-left:0; margin-right:0">添加<span> </span><code>captcha</code><span> </span>图形验证码</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>升级依赖版本</strong></p> 
  <ol style="list-style-type:lower-roman"> 
   <li>vue : 2.6.14</li> 
   <li>vue-router: 3.5.2</li> 
   <li>element-ui: 2.15.7</li> 
   <li>eslint: 3.19.0</li> 
  </ol> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>新增依赖</strong></p> 
  <ol style="list-style-type:lower-roman"> 
   <li> <p style="margin-left:0; margin-right:0">crypto-js: 4.1.1 (AES 加密)</p> </li> 
   <li> <p style="margin-left:0; margin-right:0">sass: 1.33.0</p> </li> 
   <li> <p style="margin-left:0; margin-right:0">sass-loader: 8.0.2</p> </li> 
  </ol> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>优化配置文件</strong></p> <p style="margin-left:0; margin-right:0">移除原有 /config 目录下环境配置</p> <p style="margin-left:0; margin-right:0">新增<span> </span><code>.env.development</code><span> </span>、<code>.env.production</code><span> </span>配置文件</p> 
  <div> 
   <pre><code><em>// .env.development</em>

# just a flag
ENV = <span style="color:#dd1144">'development'</span>

<em>// api接口请求地址</em>
VUE_APP_BASE_API = <span style="color:#dd1144">'http://192.168.1.17:8085'</span>

# 静态资源文件url
VUE_APP_RESOURCES_URL = <span style="color:#dd1144">'https://img.mall4j.com/'</span>

</code></pre> 
   <div style="text-align:center">
     
   </div> 
  </div> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>优化 eslint 配置</strong></p> <p style="margin-left:0; margin-right:0">优化原有代码格式标准</p> </li> 
</ol> 
<h2 style="margin-left:0; margin-right:0; text-align:left">相关截图</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left">1. 后台截图</h3> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2021/1110/143738_88a8a1e6_5094767.gif" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">2. 移动端截图</h3> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2021/1110/145209_2ec1ad04_5094767.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            