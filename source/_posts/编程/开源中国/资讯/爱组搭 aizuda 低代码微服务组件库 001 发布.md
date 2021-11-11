
---
title: '爱组搭 aizuda 低代码微服务组件库 0.0.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://portrait.gitee.com/uploads/avatars/namespace/2879/8637007_aizuda_1636162864.png!avatar100'
author: 开源中国
comments: false
date: Thu, 11 Nov 2021 17:09:00 GMT
thumbnail: 'https://portrait.gitee.com/uploads/avatars/namespace/2879/8637007_aizuda_1636162864.png!avatar100'
---

<div>   
<div class="content">
                                                                                            <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="logo" src="https://portrait.gitee.com/uploads/avatars/namespace/2879/8637007_aizuda_1636162864.png!avatar100" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">爱组搭  =  选择你喜欢的 + 组件 + 搭配 = 架构搞定</p> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0">爱组搭 ~ 低代码组件化开发平台之组件库</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">愿景：每个人都是架构师</p> </li> 
</ul> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/aizuda/aizuda-components-examples">爱组搭 ~ 组件源码示例演示</a></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">模块介绍</h1> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0">aizuda-security</p> <p style="margin-left:0; margin-right:0">安全模块，主要内容 api 请求解密，响应加密，单点登录 等。</p> </li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span style="color:#f92672"><dependency></span></span>
<span>  <span style="color:#f92672"><groupId></span>com.aizuda<span style="color:#f92672"></groupId></span></span>
<span>  <span style="color:#f92672"><artifactId></span>aizuda-security<span style="color:#f92672"></artifactId></span></span>
<span>  <span style="color:#f92672"><version></span>0.0.1<span style="color:#f92672"></version></span></span>
<span><span style="color:#f92672"></dependency></span></span>
</pre> 
 </div> 
</div> 
<p>API 快速加密解密，注解<strong><span style="color:#e74c3c"> @RestEncrypt</span></strong></p> 
<pre><code>    /**
     * 测试 post json 请求
     * 注意！！当前注解申明 json 入参为明文不需要解密逻辑，默认处理加密响应数据
     */
    @RestEncrypt(decrypt = false)
    @PostMapping("/testJson")
    public User testJson(@RequestBody LoginParam loginParam) &#123;
        return User.newUser(loginParam);
    &#125;

    /**
     * 测试 post json 解密请求
     * 注意！！当前注解申明 json 入参为明文不需要解密逻辑，默认处理加密响应数据
     */
    @RestEncrypt
    @PostMapping("/testJsonDecrypt")
    public User testJsonDecrypt(@RequestBody LoginParam loginParam) &#123;
        System.out.println("解密内容 = " + JacksonUtils.toJSONString(loginParam));
        return User.newUser(loginParam);
    &#125;

    /**
     * 测试 post json 解密请求，不加密响应数据
     */
    @RestEncrypt(encrypt = false)
    @PostMapping("/testJsonEncrypt")
    public User testJsonEncrypt(@RequestBody LoginParam loginParam) &#123;
        System.out.println("解密内容 = " + JacksonUtils.toJSONString(loginParam));
        return User.newUser(loginParam);
    &#125;</code></pre> 
<p> </p>
                                        </div>
                                      
</div>
            