
---
title: '爱组搭 aizuda 低代码安全模块 1.0.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://portrait.gitee.com/uploads/avatars/namespace/2879/8637007_aizuda_1636162864.png!avatar100'
author: 开源中国
comments: false
date: Thu, 09 Dec 2021 09:33:00 GMT
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
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/aizuda/aizuda-components-examples">爱组搭 ~ 组件源码示例演示</a>     <span> </span><a href="https://gitee.com/aizuda/aizuda-components">源码地址</a></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">1、新版修改为实体实现  Encrypted  类就自动具备解密加密能力。</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">2、接口无感签名验证。</p> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <div style="margin-right:8px">
  <a href="https://www.oschina.net/project/top_cn_2021?id=527">爱组搭 AiZuDa 参与 2021 年度 OSC 中国开源项目评选，用你 高贵的手 快来 投一票 https://www.oschina.net/project/top_cn_2021?id=527</a>
 </div> 
</div> 
<h1 style="margin-left:0; margin-right:0; text-align:left">安全模块</h1> 
<ul> 
 <li>aizuda-security 主要内容 api 请求 签名 解密，响应加密，单点登录 等。</li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span style="color:#f92672"><dependency></span></span>
<span>  <span style="color:#f92672"><groupId></span>com.aizuda<span style="color:#f92672"></groupId></span></span>
<span>  <span style="color:#f92672"><artifactId></span>aizuda-security<span style="color:#f92672"></artifactId></span></span>
<span>  <span style="color:#f92672"><version></span>1.0.0<span style="color:#f92672"></version></span></span>
<span><span style="color:#f92672"></dependency></span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">签名规则</p> 
</blockquote> 
<div style="text-align:left"> 
 <div> 
  <pre><span>md5( md5(传入内容) + timestamp ) = sign</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<blockquote> 
 <p style="margin-left:0; margin-right:0">请求约定</p> 
</blockquote> 
<div style="text-align:left"> 
 <div> 
  <pre><span>时间戳 timestamp 签名 sign 参数（ MD5 算法 ）需要放在 header 或 url 明文传输。</span>

<span>开启加密签名内容为加密后的密文</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<ul> 
 <li>单点登录功能支持，登录支持 cookie 或 token 两种模式，更多细节点击<span> </span><a href="https://gitee.com/baomidou/kisso">kisso</a></li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <pre><span>// 生成 jwt 票据，访问请求头设置‘ accessToken=票据内容 ’ 适合前后分离模式单点登录</span>
<span>String jwtToken = SSOToken.create().setId(1).setIssuer("admin").setOrigin(TokenOrigin.HTML5).getToken();</span>

<span>// 解析票据</span>
<span>SSOToken ssoToken = SSOToken.parser(jwtToken);</span>

<span>// Cookie 模式设置</span>
<span>SSOHelper.setCookie(request, response,  new SSOToken().setId(String.valueOf(1)).setIssuer("admin"));</span>

<span>// 安全配置如下</span>
<span>kisso:</span>
<span>  config:</span>
<span>    # 开启 https 有效，传输更安全</span>
<span>    cookie-secure: true</span>
<span>    # 防止 XSS 防止脚本攻击</span>
<span>    cookie-http-only: true</span>
<span>    # 防止 CSRF 跨站攻击</span>
<span>    cookie-same-site: Lax</span>
<span>    # 加密算法 RSA</span>
<span>    sign-algorithm: RS512</span>
<span>    ...</span></pre> 
 </div> 
</div> 
<p> </p>
                                        </div>
                                      
</div>
            