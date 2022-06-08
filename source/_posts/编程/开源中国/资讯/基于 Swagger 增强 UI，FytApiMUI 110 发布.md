
---
title: '基于 Swagger 增强 UI，FytApi.MUI 1.1.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/feiyit/fytapi.mui/raw/master/image/default.png'
author: 开源中国
comments: false
date: Wed, 08 Jun 2022 09:24:00 GMT
thumbnail: 'https://gitee.com/feiyit/fytapi.mui/raw/master/image/default.png'
---

<div>   
<div class="content">
                                                                                            <h4 style="margin-left:0; margin-right:0; text-align:left">更新内容</h4> 
<blockquote> 
 <p>【解决】 亮白主题，API列表滚动条样式问题<br> 【新增】 全局设置，支持请求地址大小写，默认全部小写<br> 【新增】 get参数 增加数据类型提示，支持多层级注释及格式<br> 【优化】 get参数&#123;id&#125;参数替换<br> 【优化】 公共方法提取可用，删除重复及无用代码<br> 【优化】 部分UI调整</p> 
</blockquote> 
<h4 style="margin-left:0; margin-right:0; text-align:left">介绍</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">基于swagger的轻量级,注入化的api-ui组件</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">支持netcore 3.1/5.0/6.0</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">特点</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">零浸入、轻量、简单、好看、好用</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">可配置权限认证以及Header，支持数组</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">支持 主题切换 ** 暗黑/亮白**</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">返回值Json示例，表格可视化展示数据注释信息，支持层级嵌套</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">演示地址</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">[<a href="https://gitee.com/link?target=http%3A%2F%2F114.115.174.32%3A5100%2Ffytapiui%2Findex.html">fytapiui</a>]()</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">使用说明</h4> 
<ol> 
 <li> <p style="margin-left:0; margin-right:0">通过nuget搜索<span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFytApi.MUI">FytApi.MUI</a></p> </li> 
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
<span><span>&#125;)</span><span>;</span></span>
<span>app.UseStaticFiles<span>()</span><span>;</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<ol start="4"> 
 <li>增加XML注释</li> 
</ol> 
<div style="text-align:left"> 
 <div> 
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
<span><span>&#125;)</span><span>;</span></span>
<span>app.UseStaticFiles<span>()</span><span>;</span></span>
</pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
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
<span>https://localhost:7235/fytapiui</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:left">UI预览</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt src="https://gitee.com/feiyit/fytapi.mui/raw/master/image/default.png" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt src="https://gitee.com/feiyit/fytapi.mui/raw/master/image/dark.png" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt src="https://gitee.com/feiyit/fytapi.mui/raw/master/image/api.mui.gif" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt src="https://gitee.com/feiyit/fytapi.mui/raw/master/image/api.mui.theme.gif" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            