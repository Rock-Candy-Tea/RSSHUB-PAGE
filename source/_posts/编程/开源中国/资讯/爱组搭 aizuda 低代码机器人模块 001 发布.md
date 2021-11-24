
---
title: '爱组搭 aizuda 低代码机器人模块 0.0.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://portrait.gitee.com/uploads/avatars/namespace/2879/8637007_aizuda_1636162864.png!avatar100'
author: 开源中国
comments: false
date: Wed, 24 Nov 2021 13:03:00 GMT
thumbnail: 'https://portrait.gitee.com/uploads/avatars/namespace/2879/8637007_aizuda_1636162864.png!avatar100'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="logo" src="https://portrait.gitee.com/uploads/avatars/namespace/2879/8637007_aizuda_1636162864.png!avatar100" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">爱组搭  =  选择你喜欢的 + 组件 + 搭配 = 架构搞定</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">爱组搭 ~ 低代码组件化开发平台之组件库</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">愿景：每个人都是架构师</p> </li> 
</ul> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/aizuda/aizuda-components-examples">爱组搭 ~ 组件源码示例演示</a>      <a href="https://gitee.com/aizuda/aizuda-components">源码地址</a></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">机器人模块</h1> 
<ul> 
 <li>aizuda-robot 主要内容 bug 异常 推送到 企业微信 飞书 钉钉 等平台。</li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span style="color:#f92672"><dependency></span></span>
<span>  <span style="color:#f92672"><groupId></span>com.aizuda<span style="color:#f92672"></groupId></span></span>
<span>  <span style="color:#f92672"><artifactId></span>aizuda-robot<span style="color:#f92672"></artifactId></span></span>
<span>  <span style="color:#f92672"><version></span>0.0.1<span style="color:#f92672"></version></span></span>
<span><span style="color:#f92672"></dependency></span></span></pre> 
 </div> 
</div> 
<p> 引入依赖后加上配置即可</p> 
<pre><code># 企业微信 ，飞书 ，钉钉 三选一或者配置多个，不需要的配置必须删除
aizuda:
  robot:
    weChat:
      key: 自己申请
    dingTalk:
      accessToken: 自己申请
      secret: 自己申请
    feiShu:
      key: 自己申请
      secret: 自己申请</code></pre> 
<p> </p> 
<h3>目前已经开发模块，欢迎大家参与完善。</h3> 
<h1 style="margin-left:0; margin-right:0; text-align:left">公共模块</h1> 
<ul> 
 <li>aizuda-common 主要内容 工具类 等。</li> 
</ul> 
<h1 style="margin-left:0; margin-right:0; text-align:left">限流模块</h1> 
<ul> 
 <li>aizuda-limiter 主要内容 api 限流，短信，邮件 发送限流、控制恶意利用验证码功能 等。</li> 
</ul> 
<h1 style="margin-left:0; margin-right:0; text-align:left">安全模块</h1> 
<ul> 
 <li>aizuda-security 主要内容 api 请求解密，响应加密，单点登录 等。</li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            