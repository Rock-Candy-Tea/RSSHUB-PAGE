
---
title: '基于 Swagger 增强 UI，FytApi.MUI 1.0.8 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/feiyit/fytapi.mui/raw/master/image/up-0526.gif'
author: 开源中国
comments: false
date: Thu, 26 May 2022 17:13:00 GMT
thumbnail: 'https://gitee.com/feiyit/fytapi.mui/raw/master/image/up-0526.gif'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">FytApi.MUI  支持 netcore 3.1/5.0/6.0</span></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">更新内容</h4> 
<blockquote> 
 <p style="margin-left:0px; margin-right:0px; text-align:left">【新增】返回值Jsno示例，支持多层级嵌套</p> 
 <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">【新增】返回值可视化表格数据注释信息，支持多层级嵌套</p> 
 <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">【优化】提交Body数据中，支持数组，默认值为：[]</p> 
</blockquote> 
<p><img alt src="https://gitee.com/feiyit/fytapi.mui/raw/master/image/up-0526.gif" width="800" referrerpolicy="no-referrer"><img alt height="399" src="https://oscimg.oschina.net/oscnet/up-1fafed0b819c32dc85dc43cef16e634fd91.gif" width="800" referrerpolicy="no-referrer"><img alt src="https://gitee.com/feiyit/fytapi.mui/raw/master/image/up-0526.gif" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#333333">演示地址：</span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2F114.115.174.32%3A5100%2Ffytapiui%2Findex.html" target="_blank">fytapiui</a></p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">介绍</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">基于 swagger 的轻量级，注入化的 api-ui 组件</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">特点</h4> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">零浸入、轻量、简单、好看、好用</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">可配置权限认证以及 Header，支持数组</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">支持 主题切换 ** 暗黑 / 亮白 **</p> 
<h4 style="margin-left:0; margin-right:0; text-align:left">使用说明</h4> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">通过 nuget 搜索<span> </span><span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FFytApi.MUI">FytApi.MUI</a></p> </li> 
 <li> <p style="margin-left:0; margin-right:0">添加引用到 API 项目中</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">打开 Program.cs 配置</p> </li> 
</ol> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span><span style="color:#6a737d">// 默认 swagger 不要删除</span></span>
<span><span style="color:#d73a49">app</span><span style="color:#6f42c1">.UseSwagger</span><span>()</span><span>;</span></span>
<span><span style="color:#6a737d">// 兼容 默认 SwaggerUI  </span><strong><span style="color:#e74c3c">可保留可删除</span></strong></span>
<span><span style="color:#d73a49">app</span><span style="color:#6f42c1">.UseSwaggerUI</span><span>()</span><span>;</span></span>
<span><span style="color:#6a737d">// </span><span><span style="color:#6a737d">[</span></span><span style="color:#6a737d">增加]  配置UI HTTP请求管道，及相关中间件处理 ，这里配置和Swagger默认配置一样</span></span>
<span><span style="color:#d73a49">app</span><span style="color:#6f42c1">.UseFytApiUI</span><span>(</span>c <span>=></span></span>
<span><span>&#123;</span></span>
<span>   <span style="color:#d73a49">c</span><span style="color:#6f42c1">.SwaggerEndpoint</span><span>(</span><span style="color:#dd1144"><span style="color:#032f62">"/swagger/v1/swagger.json"</span></span>, <span style="color:#dd1144"><span style="color:#032f62">"devault"</span></span>,<span style="color:#dd1144"><span style="color:#032f62">"v1"</span></span><span>)</span><span>;</span></span>
<span><span>&#125;);
<span style="color:#6a737d">// 增加支持静态资源访问</span></span></span><span style="color:#6a737d"> </span>
<span style="color:#d73a49">app</span><span style="color:#6f42c1">.UseStaticFiles</span>();
</pre> 
 </div> 
</div> 
<ol start="4" style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>增加 XML 注释</li> 
</ol> 
<div style="text-align:left"> 
 <pre style="margin-left:0; margin-right:0"><span>在项目中右击,增加XML生成</span>
<span>参考如下代码</span>
<span>builder.Services.AddSwaggerGen<span>(</span><span><span>options</span> </span><span><span>=></span></span></span>
<span><span>&#123;</span></span>
<span>    <span style="color:#6a737d">// 配置相关组</span></span>
<span>    options.SwaggerDoc<span>(</span><span style="color:#dd1144"><span style="color:#032f62">"v1"</span></span>, <span style="color:#d73a49">new</span> Microsoft.OpenApi.Models.OpenApiInfo <span>&#123;</span> Title <span>=</span> <span style="color:#dd1144"><span style="color:#032f62">"天气"</span></span>, Version <span>=</span> <span style="color:#dd1144"><span style="color:#032f62">"v1"</span></span> <span>&#125;)</span><span>;</span></span>
<span>    options.SwaggerDoc<span>(</span><span style="color:#dd1144"><span style="color:#032f62">"v2"</span></span>, <span style="color:#d73a49">new</span> Microsoft.OpenApi.Models.OpenApiInfo <span>&#123;</span> Title <span>=</span> <span style="color:#dd1144"><span style="color:#032f62">"用户"</span></span>, Version <span>=</span> <span style="color:#dd1144"><span style="color:#032f62">"v1"</span></span> <span>&#125;)</span><span>;</span></span>
<span>    <span style="color:#6a737d">// 增加项目xml注释显示，如果有多个类库要显示，可以继续增加</span></span>
<span>    options.IncludeXmlComments<span>(</span>Path.Combine<span>(</span>AppContext.BaseDirectory, <span style="color:#dd1144"><span style="color:#032f62">"TestApi.xml"</span></span><span>)</span>,<span style="color:#005cc5">true</span><span>)</span><span>;</span></span>
<span>    <span style="color:#6a737d">// </span><span><span style="color:#6a737d">[</span></span><span style="color:#6a737d">示例]-增加Model xml显示</span></span>
<span>    options.IncludeXmlComments<span>(</span>Path.Combine<span>(</span>AppContext.BaseDirectory, <span style="color:#dd1144"><span style="color:#032f62">"TestApi.Model.xml"</span></span><span>)</span>,<span style="color:#005cc5">true</span><span>)</span><span>;</span></span>
<span><span>&#125;)</span><span>;</span></span>

<span><span style="color:#6a737d">// UI 和 Swagger配置一样一样滴</span></span>
<span>app.UseFytApiUI<span>(</span><span><span>c</span> </span><span><span>=></span></span></span>
<span><span>&#123;</span></span>
<span>    c.SwaggerEndpoint<span>(</span><span style="color:#dd1144"><span style="color:#032f62">"/swagger/v1/swagger.json"</span></span>, <span style="color:#dd1144"><span style="color:#032f62">"天气"</span></span>,<span style="color:#dd1144"><span style="color:#032f62">"v1"</span></span><span>)</span><span>;</span></span>
<span>    c.SwaggerEndpoint<span>(</span><span style="color:#dd1144"><span style="color:#032f62">"/swagger/v2/swagger.json"</span></span>, <span style="color:#dd1144"><span style="color:#032f62">"用户"</span></span>,<span style="color:#dd1144"><span style="color:#032f62">"v2"</span></span><span>)</span><span>;</span></span>
<span><span>&#125;)</span><span>;
<span style="color:#6a737d">// 增加支持静态资源访问</span></span></span>
app.UseStaticFiles();
</pre> 
</div> 
<ol start="5" style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>设置访问默认页</li> 
</ol> 
<div style="text-align:left"> 
 <div> 
  <pre style="margin-left:0; margin-right:0"><span>netcore6.<span>0</span>  启动配置默认访问的是swagger , 而本项目默认地址为 fytapiui</span>

<span>修改如下文件可设置默认访问</span>
<span>项目根目录 Properties/launchSettings.json</span>
<span> <span style="color:#dd1144"><span style="color:#032f62">"profiles"</span></span>: <span>&#123;</span></span>
<span>    <span style="color:#dd1144"><span style="color:#032f62">"SwaggerApi"</span></span>: <span>&#123;</span></span>
<span>      <span style="color:#dd1144"><span style="color:#032f62">"commandName"</span></span>: <span style="color:#dd1144"><span style="color:#032f62">"Project"</span></span>,</span>
<span>      <span style="color:#dd1144"><span style="color:#032f62">"dotnetRunMessages"</span></span>: <span style="color:#0086b3"><span style="color:#005cc5">true</span></span>,</span>
<span>      <span style="color:#dd1144"><span style="color:#032f62">"launchBrowser"</span></span>: <span style="color:#0086b3"><span style="color:#005cc5">true</span></span>,</span>
<span>      <span style="color:#dd1144"><span style="color:#032f62">"launchUrl"</span></span>: <span style="color:#dd1144"><span style="color:#032f62">"fytapiui/index.html"</span></span>,  <span style="color:#6a737d">//将swagger 修改为 fytapiui/index.html</span></span>
<span>      <span style="color:#dd1144"><span style="color:#032f62">"applicationUrl"</span></span>: <span style="color:#dd1144"><span style="color:#032f62">"https://localhost:7106;http://localhost:5106"</span></span>,</span>
<span>      <span style="color:#dd1144"><span style="color:#032f62">"environmentVariables"</span></span>: <span>&#123;</span></span>
<span>        <span style="color:#dd1144"><span style="color:#032f62">"ASPNETCORE_ENVIRONMENT"</span></span>: <span style="color:#dd1144"><span style="color:#032f62">"Development"</span></span></span>
<span>      <span>&#125;</span></span>
<span>    <span>&#125;</span>,</span>
<span>    <span style="color:#dd1144"><span style="color:#032f62">"IIS Express"</span></span>: <span>&#123;</span></span>
<span>      <span style="color:#dd1144"><span style="color:#032f62">"commandName"</span></span>: <span style="color:#dd1144"><span style="color:#032f62">"IISExpress"</span></span>,</span>
<span>      <span style="color:#dd1144"><span style="color:#032f62">"launchBrowser"</span></span>: <span style="color:#0086b3"><span style="color:#005cc5">true</span></span>,</span>
<span>      <span style="color:#dd1144"><span style="color:#032f62">"launchUrl"</span></span>: <span style="color:#dd1144"><span style="color:#032f62">"fytapiui/index.html"</span></span>, <span style="color:#6a737d">//将swagger 修改为 fytapiui/index.html</span></span>
<span>      <span style="color:#dd1144"><span style="color:#032f62">"environmentVariables"</span></span>: <span>&#123;</span></span>
<span>        <span style="color:#dd1144"><span style="color:#032f62">"ASPNETCORE_ENVIRONMENT"</span></span>: <span style="color:#dd1144"><span style="color:#032f62">"Development"</span></span></span>
<span>      <span>&#125;</span></span>
<span>    <span>&#125;</span></span>
<span>  <span>&#125;</span></span>

<span>重新启动项目即可 </span>
<span>https:<span style="color:#6a737d">//localhost:7235/fytapiui/index.html</span></span>
</pre> 
 </div> 
</div> 
<h4 style="margin-left:0; margin-right:0; text-align:left">UI 预览</h4> 
<p><img alt height="399" src="https://gitee.com/feiyit/fytapi.mui/raw/master/image/api.mui.theme.gif" width="800" referrerpolicy="no-referrer"></p> 
<p><img alt height="399" src="https://gitee.com/feiyit/fytapi.mui/raw/master/image/api.mui.gif" width="800" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            