
---
title: 'OpenAPI Generator v5.3.0 发布，OpenAPI 规范自动生成代码'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6923'
author: 开源中国
comments: false
date: Wed, 27 Oct 2021 07:28:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6923'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">OpenAPI Generator v5.3.0 发布了！OpenAPI Generator 可用于在给定 OpenAPI 规范（v2, v3）的情况下自动生成 API 客户端库、server stubs、文档以及配置。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">5.3.0 版本包含大量的 bug 修复、功能增强，以​​及<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpulls%3Fq%3Dis%253Amerged%2Bis%253Apr%2Bmilestone%253A5.3.0%2Blabel%253A%2522Breaking%2Bchange%2B%2528with%2Bfallback%2529%2522" target="_blank">重大更改（带有回退）</a>。主要更新内容如下：</p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start">通用更新</h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">加入<span> </span><span style="color:#24292f">snake case lambda。<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10658" target="_blank"><u>#10658</u></a></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">在未关闭的流中加入<span> </span><code>try-with-resources </code><span> </span>语句。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10641" target="_blank"><u>#10641</u></a></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">改进版本管理：<span style="color:#2e3033">更新依赖项，删除不使用的依赖项。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10544" target="_blank">#10544</a> </p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#2e3033">修复某些环境中由换行符引发的 Windows 构建失败。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10529" target="_blank">#10529</a> </p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#24292f">更新模型生成、addProps 处理移入类型对象（</span>type object<span style="color:#24292f">）和 anyType 处理。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10505" target="_blank">#10505</a></p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Bash（</strong><span style="color:#333333">Bourne-Again SHell<span> </span></span><strong>）</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#24292f">将<span> </span><code>scriptName</code><span> </span>更改为<span> </span><code>x-codegen-script-name</code><span> </span>，以修复 dockerfile 。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10594" target="_blank">#10594</a> </li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>C 语言</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>改进 CMake 的 Libcurl 库。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10249" target="_blank">#10249 </a></li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>C＃</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复 CSharpOperationTest 类中的编译问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10574" target="_blank">#10574</a> </li> 
 <li><span style="color:#24292f"><strong>[csharp-netcore]：</strong>不初始化<span> </span><code>conditionalSerialization</code><span> </span>的默认值。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10551" target="_blank">#10551</a> </li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>C ++ </strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#24292f"><strong>[cpp-rest-sdk-client]：</strong>将布尔参数序列化为 true/false ， 而不是 1/0。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10554" target="_blank">#10554</a> </li> 
 <li><span style="color:#24292f"><strong>[cpp][qt]：</strong>整理</span><span style="color:#2e3033"><span> </span>cpp qt 的 reademe。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10549" target="_blank"><u>#10549</u></a></li> 
 <li><span style="color:#24292f">改进 C++ Restbed 模板。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10543" target="_blank"><u>#10543</u></a></li> 
 <li><span style="color:#24292f"><strong>[cpprestsdk]：<span> </span></strong>修复字符串转换，支持整数枚举。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10531" target="_blank">#10531</a> </li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Crystal</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#24292f"><strong>[crystal]：</strong></span><span style="color:#2e3033">修正<span> </span></span>Crystal<span style="color:#2e3033"><span> </span>客户端模板的一些问题 。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10629" target="_blank"><u>#10629</u></a></li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Dart</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#24292f"><strong>Dart：</strong>弃用 Dart jaguar 标记，因为它不适用于较新版本的 Dart。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10533" target="_blank">#10533</a> </li> 
 <li><span style="color:#24292f"><strong>[dart]</strong></span><span style="color:#2e3033"><strong>：</strong>删除 Json_serializable 这个实验性的生成器。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10532" target="_blank"><u>#10532</u></a><u> </u></li> 
 <li><span style="color:#24292f"><strong>[dart][dio]：</strong></span><span style="color:#2e3033">默认为模型导入之前</span><span style="color:#24292f">先</span><span style="color:#2e3033">检查</span><span style="color:#24292f"><span> </span></span><span style="color:#2e3033"><code>import-mappings<span> </span></code>参数。<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10528" target="_blank">#10528</a> </li> 
 <li><span style="color:#24292f"><strong>[dart-dio-next]：</strong>添加一个新的生成器选项（dio 或 dio_http）来更改 dio 包。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10497" target="_blank"><u>#10497</u></a></li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Elm</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>[elm]：</strong>修复为枚举生成的无效代码。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10328" target="_blank">#10328</a> </li> 
 <li><span style="color:#24292f"><strong>[bugfix][Elm]：</strong>修复了当响应模式为 Map (Dict) 时生成错误 Elm 代码的问题。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10310" target="_blank">#10310</a> </li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start">Go</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#24292f"><strong>[go]：</strong>修复 anyOf 编译错误。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10431" target="_blank"><u>#10431</u></a></li> 
 <li><strong>[go-server]：</strong>参数名与变量名冲突时，为参数名添加后缀。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10243" target="_blank">#10243</a></li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Haskell</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>[haskell-http-client]：<span> </span></strong>添加新功能：在<span style="color:#2e3033">查询字符串中可以选择不应该被编码的其他字符</span>（例如“+”或“:”）。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10424" target="_blank">#10424</a> </li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>HTML</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>更新了 HTML2 Doc Curl 示例。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10323" target="_blank"><u>#10323</u></a></li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start">Java</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>[java][jersey2]：</strong><span> </span>更新依赖项。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10659" target="_blank">#10659</a> </li> 
 <li>改进对<span> </span><span style="color:#24292f">Apache Httpclient 的支持。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10624" target="_blank">#10624</a> </li> 
 <li><strong>[Java][Feign]：</strong><span> </span>给 feign 结果添加 http 状态码。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10583" target="_blank">#10583</a> </li> 
 <li><span style="color:#24292f"><strong>[Java][RestTemplate]</strong>：</span>修复<span> </span><code>ApiClient.mustache</code><span> </span>不处理 cookie ApiKey 的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10578" target="_blank"><u>#10578</u></a></li> 
 <li><span style="color:#24292f"><strong>[java][jersey2]：</strong></span><span style="color:#2e3033">使用实现（</span><span style="color:#24292f">implementation</span><span style="color:#2e3033">）来代替编译，同时在 README 中添加 maven、gradle 的最小版本。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10571" target="_blank">#10571</a> </li> 
 <li><strong>[java]：</strong>将 Gradle 更新到 7.2<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10538" target="_blank">#10538</a></li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>K6</strong></h2> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#24292f"><strong>[ K6 Generator ]：<span> </span></strong>如果用作输入规范的 Swagger/OpenAPI 规范包含参数级别的示例，那么这些示例将被提取，并用作参数值。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F9750" target="_blank">#9750</a> </p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Kotlin</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复 Kotlin 枚举默认值。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10592" target="_blank">#10592</a></li> 
 <li>更新 Kotlin 多个平台，以适应未来的 Kotlin 1.6.0 版本。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10468" target="_blank">#10468</a></li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>PHP</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[PHP]： 更新 GuzzleHttp 版本至 7 。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10585" target="_blank">#10585</a></li> 
 <li>[php]： 修复 settype() 的<span> </span><code>'mixed'<span> </span></code>输入。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10576" target="_blank">#10576</a></li> 
 <li>[php-slim4]： 迁移 PHPUnit 配置。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10230" target="_blank">#10230</a></li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>PowerShell</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>为 powershell 生成器添加十进制支持。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10486" target="_blank">#10486</a></li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Python</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[Python] 修复了<code>_setitem_<span> </span></code>对组合实例抛错的问题。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10197" target="_blank">#10197</a></li> 
 <li>Python 客户端：修复布尔枚举用例。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F9926" target="_blank">#9926</a></li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start">R</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>为 R 客户端生成器添加十进制支持。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10487" target="_blank">#10487</a></li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start">Ruby</h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>Ruby：</strong>修复 Faraday 的弃用警告。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10559" target="_blank">#10559</a></li> 
 <li><strong>[REQ] [RUBY] [FARADAY]：</strong>允许配置中间件。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10495" target="_blank">#10495</a></li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Rust</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复 uuid 参数格式的字符串输出<span> </span><code>&str&str</code><span> </span>双重类型的问题。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10569" target="_blank">#10569</a></li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Scala</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复：现在会在正文中发送一个空字符串，代替之前发送的“”（空格字符），因为某些后端（例如<code>akka-http</code>）未能将其解析为 json。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10561" target="_blank">#10561</a></li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Swift</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>[swift5][client]：</strong><span> </span>添加对异步等待的支持<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10442" target="_blank">#10442</a></li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>TypeScript</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li><strong>[typescript-axios]：</strong><span> </span>更新到 Axios 0.23.0 。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10626" target="_blank">#10626</a></li> 
 <li><strong>fix[NestJS]：</strong>为默认的 header 使用正确的输入。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10616" target="_blank">#10616</a></li> 
 <li><strong>[typescript-axios]:</strong><span> </span>修复查询参数的无效用法。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10512" target="_blank">#10512</a></li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start"><strong>WSDL</strong></h2> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[wsdl]： 修复字符串比较的错误，更改次要格式。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10446" target="_blank">#10446</a></li> 
 <li>[Wsdl] 使用 oneOf 项和其他次要的更新/修复，来处理类型数组的架构属性。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10434" target="_blank">#10434</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Freleases%2Ftag%2Fv5.3.0" target="_blank">https://github.com/OpenAPITools/openapi-generator/releases/tag/v5.3.0</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            