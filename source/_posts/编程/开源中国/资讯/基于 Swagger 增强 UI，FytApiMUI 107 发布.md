
---
title: '基于 Swagger 增强 UI，FytApi.MUI 1.0.7 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/feiyit/fytapi.mui/raw/master/image/api.mui.theme.gif'
author: 开源中国
comments: false
date: Sat, 14 May 2022 17:59:00 GMT
thumbnail: 'https://gitee.com/feiyit/fytapi.mui/raw/master/image/api.mui.theme.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <p>FytApi.MUI  1.0.7 增加支持 netcore 3.1/5.0/6.0</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">更新内容</h4> 
<blockquote> 
 <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><span style="color:#e74c3c">支持更多平台 3.1/5.0/6.0</span></p> 
 <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">增加Body参数针对datetime添加当前时间默认值</p> 
 <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">优化Body参数文档注释中，描述信息总去掉数据类型</p> 
</blockquote> 
<p style="margin-left:0px; margin-right:0px; text-align:left">演示地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2F114.115.174.32%3A5100%2Ffytapiui%2Findex.html" target="_blank">fytapiui</a></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">介绍</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">基于swagger的轻量级,注入化的api-ui组件</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">特点</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">零浸入、轻量、简单、好看、好用</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">可配置权限认证以及Header，支持数组</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">支持 主题切换 ** 暗黑/亮白**</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">使用说明</h4> 
<ol> 
 <li> <p style="margin-left:0; margin-right:0">通过nuget搜索<span> </span><span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFytApi.MUI">FytApi.MUI</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">添加引用到API项目中</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">打开 Program.cs 配置</p> </li> 
</ol> 
<div style="text-align:left"> 
 <div> 
  <pre><span>// 默认 swagger 不要删除</span>
<span>app.UseSwagger<span>()</span><span>;</span></span>
<span>// 兼容 默认 SwaggerUI  可保留可删除</span>
<span>app.UseSwaggerUI<span>()</span><span>;</span></span>
<span>// <span>[</span>增加]  配置UI HTTP请求管道，及相关中间件处理 ，这里配置和Swagger默认配置一样</span>
<span>app.UseFytApiUI<span>(</span>c <span>=></span></span>
<span><span>&#123;</span></span>
<span>   c.SwaggerEndpoint<span>(</span><span style="color:#dd1144">"/swagger/v1/swagger.json"</span>, <span style="color:#dd1144">"devault"</span>,<span style="color:#dd1144">"v1"</span><span>)</span><span>;</span></span>
<span><span>&#125;);
// 增加支持静态资源访问</span></span> 
app.UseStaticFiles();
</pre> 
 </div> 
</div> 
<ol start="4"> 
 <li>增加XML注释</li> 
</ol> 
<div style="text-align:left"> 
 <pre><span>在项目中右击,增加XML生成</span>
<span>参考如下代码</span>
<span>builder.Services.AddSwaggerGen<span>(</span>options <span>=></span></span>
<span><span>&#123;</span></span>
<span>    // 配置相关组</span>
<span>    options.SwaggerDoc<span>(</span><span style="color:#dd1144">"v1"</span>, new Microsoft.OpenApi.Models.OpenApiInfo <span>&#123;</span> Title <span>=</span> <span style="color:#dd1144">"天气"</span>, Version <span>=</span> <span style="color:#dd1144">"v1"</span> <span>&#125;)</span><span>;</span></span>
<span>    options.SwaggerDoc<span>(</span><span style="color:#dd1144">"v2"</span>, new Microsoft.OpenApi.Models.OpenApiInfo <span>&#123;</span> Title <span>=</span> <span style="color:#dd1144">"用户"</span>, Version <span>=</span> <span style="color:#dd1144">"v1"</span> <span>&#125;)</span><span>;</span></span>
<span>    // 增加项目xml注释显示，如果有多个类库要显示，可以继续增加</span>
<span>    options.IncludeXmlComments<span>(</span>Path.Combine<span>(</span>AppContext.BaseDirectory, <span style="color:#dd1144">"TestApi.xml"</span><span>)</span>,true<span>)</span><span>;</span></span>
<span>    // <span>[</span>示例]-增加Model xml显示</span>
<span>    options.IncludeXmlComments<span>(</span>Path.Combine<span>(</span>AppContext.BaseDirectory, <span style="color:#dd1144">"TestApi.Model.xml"</span><span>)</span>,true<span>)</span><span>;</span></span>
<span><span>&#125;)</span><span>;</span></span>

<span>// UI 和 Swagger配置一样一样滴</span>
<span>app.UseFytApiUI<span>(</span>c <span>=></span></span>
<span><span>&#123;</span></span>
<span>    c.SwaggerEndpoint<span>(</span><span style="color:#dd1144">"/swagger/v1/swagger.json"</span>, <span style="color:#dd1144">"天气"</span>,<span style="color:#dd1144">"v1"</span><span>)</span><span>;</span></span>
<span>    c.SwaggerEndpoint<span>(</span><span style="color:#dd1144">"/swagger/v2/swagger.json"</span>, <span style="color:#dd1144">"用户"</span>,<span style="color:#dd1144">"v2"</span><span>)</span><span>;</span></span>
<span><span>&#125;)</span><span>;
// 增加支持静态资源访问</span></span>
app.UseStaticFiles();
</pre> 
</div> 
<ol start="5"> 
 <li>设置访问默认页</li> 
</ol> 
<div style="text-align:left"> 
 <div> 
  <pre><span>netcore6.0  启动配置默认访问的是swagger , 而本项目默认地址为 fytapiui</span>

<span>修改如下文件可设置默认访问</span>
<span>项目根目录 Properties/launchSettings.json</span>
<span> <span style="color:#dd1144">"profiles"</span>: <span>&#123;</span></span>
<span>    <span style="color:#dd1144">"SwaggerApi"</span>: <span>&#123;</span></span>
<span>      <span style="color:#dd1144">"commandName"</span>: <span style="color:#dd1144">"Project"</span>,</span>
<span>      <span style="color:#dd1144">"dotnetRunMessages"</span>: <span style="color:#0086b3">true</span>,</span>
<span>      <span style="color:#dd1144">"launchBrowser"</span>: <span style="color:#0086b3">true</span>,</span>
<span>      <span style="color:#dd1144">"launchUrl"</span>: <span style="color:#dd1144">"fytapiui/index.html"</span>,  //将swagger 修改为 fytapiui/index.html</span>
<span>      <span style="color:#dd1144">"applicationUrl"</span>: <span style="color:#dd1144">"https://localhost:7106;http://localhost:5106"</span>,</span>
<span>      <span style="color:#dd1144">"environmentVariables"</span>: <span>&#123;</span></span>
<span>        <span style="color:#dd1144">"ASPNETCORE_ENVIRONMENT"</span>: <span style="color:#dd1144">"Development"</span></span>
<span>      <span>&#125;</span></span>
<span>    <span>&#125;</span>,</span>
<span>    <span style="color:#dd1144">"IIS Express"</span>: <span>&#123;</span></span>
<span>      <span style="color:#dd1144">"commandName"</span>: <span style="color:#dd1144">"IISExpress"</span>,</span>
<span>      <span style="color:#dd1144">"launchBrowser"</span>: <span style="color:#0086b3">true</span>,</span>
<span>      <span style="color:#dd1144">"launchUrl"</span>: <span style="color:#dd1144">"fytapiui/index.html"</span>, //将swagger 修改为 fytapiui/index.html</span>
<span>      <span style="color:#dd1144">"environmentVariables"</span>: <span>&#123;</span></span>
<span>        <span style="color:#dd1144">"ASPNETCORE_ENVIRONMENT"</span>: <span style="color:#dd1144">"Development"</span></span>
<span>      <span>&#125;</span></span>
<span>    <span>&#125;</span></span>
<span>  <span>&#125;</span></span>

<span>重新启动项目即可 </span>
<span>https://localhost:7235/fytapiui</span>
</pre> 
 </div> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:left">UI预览</h4> 
<p><img alt src="https://gitee.com/feiyit/fytapi.mui/raw/master/image/api.mui.theme.gif" referrerpolicy="no-referrer"></p> 
<p><img alt src="https://gitee.com/feiyit/fytapi.mui/raw/master/image/api.mui.gif" referrerpolicy="no-referrer"></p> 
<p> </p>
                                        </div>
                                      
</div>
            