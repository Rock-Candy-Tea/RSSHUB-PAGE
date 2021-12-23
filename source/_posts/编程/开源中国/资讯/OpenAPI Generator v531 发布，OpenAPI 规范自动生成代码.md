
---
title: 'OpenAPI Generator v5.3.1 发布，OpenAPI 规范自动生成代码'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=515'
author: 开源中国
comments: false
date: Thu, 23 Dec 2021 07:13:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=515'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">OpenAPI Generator v5.3.1 现已发布。OpenAPI Generator 可用于在给定 OpenAPI 规范（v2, v3）的情况下自动生成 API 客户端库、server stubs、文档以及配置。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">v5.3.1 是 2021 年的最后一个稳定版本，包含了许多功能增强/错误修正和 2 个新的 generators/libraries：</span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F11020" target="_blank">csharp-netcore-functions</a> : [C#] 新的 Azure 函数生成器</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10253" target="_blank">volley (kotlin)</a>：Kotlin 客户端：添加 volley 库支持。</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">具体更新内容如下：</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>General </strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复 request body anyType 参数的 paramName 和 dataType <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F11075" target="_blank">#11075</a></li> 
 <li>比较 HTTP 身份验证安全模式名称不区分大小写<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10989" target="_blank">#10989</a></li> 
 <li>更好地处理解析器中引用无效模式时的 NPE 问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10882" target="_blank">#10882</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>Bash</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[Bash] 支持 post 表单数据<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10795" target="_blank">#10795</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#24292f"><strong>C</strong></span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[C][Client] 支持自定义数据类型（IntOrString）<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F11074" target="_blank">#11074</a></li> 
 <li>[C][Client] 使用 cpack 构建 deb 包<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10935" target="_blank">#10935</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>C#</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[C#] 新的 Azure 函数生成器<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F11020" target="_blank">#11020</a></li> 
 <li>[C#] 将 C# 依赖项更新到新版本<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10761" target="_blank">#10761</a></li> 
 <li>[csharp-netcore] 支持 Net 6.0 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10634" target="_blank">#10634</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#24292f"><strong>C++</strong></span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[cpp-pistache-server]：修复与 pistache 的构建 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10829" target="_blank">#10829</a></li> 
 <li>[cpprestsdk] CMake 构建系统改进<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10660" target="_blank">#10660</a></li> 
 <li>[Qt][C++] Oauth2 Authorization Code Flow 和 Implicit Flow 支持<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10183" target="_blank">#10183</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>Dart</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[dart][dio][built_value] 修复 additionalProperties 缺少的 serializer factory builders <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F11011" target="_blank">#11011</a></li> 
 <li>[dart-dio-next] 删除 dioLibrary 选项<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10931" target="_blank">#10931</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#24292f"><strong>Go</strong></span></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[GO] 不要规范 headers <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10779" target="_blank">#10779</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><strong>Groovy</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复 groovy build.gradle 中的 build-info-extractor-gradle <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F10760" target="_blank">#10760</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Freleases%2Ftag%2Fv5.3.1" target="_blank">https://github.com/OpenAPITools/openapi-generator/releases/tag/v5.3.1</a></p>
                                        </div>
                                      
</div>
            