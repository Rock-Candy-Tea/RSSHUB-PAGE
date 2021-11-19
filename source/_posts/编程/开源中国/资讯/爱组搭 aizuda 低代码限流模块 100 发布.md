
---
title: '爱组搭 aizuda 低代码限流模块 1.0.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://portrait.gitee.com/uploads/avatars/namespace/2879/8637007_aizuda_1636162864.png!avatar100'
author: 开源中国
comments: false
date: Fri, 19 Nov 2021 02:18:00 GMT
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
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/aizuda/aizuda-components-examples">爱组搭 ~ 组件源码示例演示</a></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">模块介绍</h1> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0">aizuda-limiter</p> <p style="margin-left:0; margin-right:0">限流模块，主要内容 api 限流，短信，邮件 发送限流、控制恶意利用验证码功能 等。</p> </li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span style="color:#f92672"><dependency></span></span>
<span>  <span style="color:#f92672"><groupId></span>com.aizuda<span style="color:#f92672"></groupId></span></span>
<span>  <span style="color:#f92672"><artifactId></span>aizuda-limiter<span style="color:#f92672"></artifactId></span></span>
<span>  <span style="color:#f92672"><version></span>1.0.0<span style="color:#f92672"></version></span></span>
<span><span style="color:#f92672"></dependency></span></span></pre> 
 </div> 
</div> 
<p>使用简单优雅</p> 
<pre><code class="language-java">  @GetMapping("/test")
    @RateLimit(
            // 唯一标示，支持SpEL表达式（可无），#name 为获取当前访问参数 name 内容
            key = "#name",
            // 限定阈值，时间间隔 interval 范围内超过该数量会触发锁
            count = 2,
            // 限制间隔时长（可无，默认 3 分钟）例如 5s 五秒，6m 六分钟，7h 七小时，8d 八天
            interval = "100s",
            // 策略（可无） ip 为获取当前访问IP地址（内置策略），自定义策略 user 为获取当前用户
            strategy = &#123; "ip", "user" &#125;,
            // 提示消息（可无）
            message = "请勿频繁操作"
    )
    public String test(String name) &#123;
        return "test" + name;
    &#125;</code></pre> 
<p> </p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">aizuda-security</p> <p style="margin-left:0; margin-right:0">安全模块，主要内容 api 请求解密，响应加密，单点登录 等。</p> </li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span><span style="color:#f92672"><span style="color:#333333"><<span style="color:#22863a">dependency</span>></span></span></span>
<span>  <span style="color:#f92672"><span style="color:#333333"><<span style="color:#22863a">groupId</span>></span></span>com.aizuda<span style="color:#f92672"><span style="color:#333333"></<span style="color:#22863a">groupId</span>></span></span></span>
<span>  <span style="color:#f92672"><span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span></span>aizuda-security<span style="color:#f92672"><span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span></span></span>
<span>  <span style="color:#f92672"><span style="color:#333333"><<span style="color:#22863a">version</span>></span></span>0.0.1<span style="color:#f92672"><span style="color:#333333"></<span style="color:#22863a">version</span>></span></span></span>
<span><span style="color:#f92672"><span style="color:#333333"></<span style="color:#22863a">dependency</span>></span></span></span>
</pre> 
 </div> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">API 快速加密解密，注解<strong><span style="color:#e74c3c"> @RestEncrypt</span></strong></p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code>    <span style="color:#6a737d">/**
     * 测试 post json 请求
     * 注意！！当前注解申明 json 入参为明文不需要解密逻辑，默认处理加密响应数据
     */</span>
    <span style="color:#032f62">@RestEncrypt</span>(decrypt = false)
    <span style="color:#032f62">@PostMapping</span>(<span style="color:#032f62">"/testJson"</span>)
    public User testJson(<span style="color:#032f62">@RequestBody</span> LoginParam loginParam) &#123;
        <span style="color:#d73a49">return</span> <span style="color:#d73a49">User</span><span style="color:#6f42c1">.newUser</span>(loginParam);
    &#125;

    <span style="color:#6a737d">/**
     * 测试 post json 解密请求
     * 注意！！当前注解申明 json 入参为明文不需要解密逻辑，默认处理加密响应数据
     */</span>
    @<span style="color:#d73a49">RestEncrypt</span>
    @<span style="color:#d73a49">PostMapping</span>(<span style="color:#032f62">"/testJsonDecrypt"</span>)
    <span style="color:#d73a49">public</span> <span style="color:#d73a49">User</span> <span style="color:#d73a49">testJsonDecrypt</span>(<span style="color:#032f62">@RequestBody</span> LoginParam loginParam) &#123;
        <span style="color:#d73a49">System</span><span style="color:#6f42c1">.out</span><span style="color:#6f42c1">.println</span>(<span style="color:#032f62">"解密内容 = "</span> + JacksonUtils.toJSONString(loginParam));
        <span style="color:#d73a49">return</span> <span style="color:#d73a49">User</span><span style="color:#6f42c1">.newUser</span>(loginParam);
    &#125;

    <span style="color:#6a737d">/**
     * 测试 post json 解密请求，不加密响应数据
     */</span>
    @<span style="color:#d73a49">RestEncrypt</span>(encrypt = false)
    @<span style="color:#d73a49">PostMapping</span>(<span style="color:#032f62">"/testJsonEncrypt"</span>)
    <span style="color:#d73a49">public</span> <span style="color:#d73a49">User</span> <span style="color:#d73a49">testJsonEncrypt</span>(<span style="color:#032f62">@RequestBody</span> LoginParam loginParam) &#123;
        <span style="color:#d73a49">System</span><span style="color:#6f42c1">.out</span><span style="color:#6f42c1">.println</span>(<span style="color:#032f62">"解密内容 = "</span> + JacksonUtils.toJSONString(loginParam));
        <span style="color:#d73a49">return</span> <span style="color:#d73a49">User</span><span style="color:#6f42c1">.newUser</span>(loginParam);
    &#125;</code></pre>
                                        </div>
                                      
</div>
            