
---
title: 'OpenAPI Generator v6.0.1 发布，OpenAPI 规范自动生成代码'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1948'
author: 开源中国
comments: false
date: Wed, 06 Jul 2022 07:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1948'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#000000">OpenAPI Generator v6.0.1 现已发布。OpenAPI Generator 可用于在给定 OpenAPI 规范（v2, v3）的情况下自动生成 API 客户端库、server stubs、文档以及配置。</span></p> 
<p style="text-align:start"><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>v6.0.1 是一个包含增强功能的补丁版本，修复了涵盖 20 种编程语言的错误。有关更改的完整列表，请参阅 </span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpulls%3Fq%3Dis%253Apr%2Bis%253Amerged%2Bmilestone%253A6.0.1" target="_blank">"Pull Request" tab</a><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>。一些重点更新内容如下：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>General</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>用于标记源目录并省略 gradle 包装器的 Idea plugin <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12711" target="_blank">#12711</a></li> 
 <li>修复 camelcase lambda 中的错误，为 pascalcase 添加测试 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12639" target="_blank">#12639</a></li> 
 <li>添加新选项以自定义内联模型的命名规则 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12562" target="_blank">#12562</a></li> 
 <li>添加处理和使用模型测试用例的能力，在新的 v3.0.3 单元测试规范中使用它 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12619" target="_blank">#12619</a></li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>C</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li> <p>[C][Client] 设置 null json 的默认值<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12620" target="_blank">#12620</a></p> </li> 
 <li> <p>[C][Client] 支持自由形式的对象<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12557" target="_blank">#12557</a></p> </li> 
</ul> 
<p style="text-align:start"><strong>C#</strong></p> 
<ul> 
 <li> <p>[csharp-netcore] 修复：url escaping <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12739" target="_blank">#12739</a></p> </li> 
 <li> <p>[csharp-netcore] 添加对 ComVisible、CLSCompliant 属性的支持<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12733" target="_blank">#12733</a></p> </li> 
 <li> <p>修复生成参数（对象）示例时的 NPE <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12538" target="_blank">#12538</a></p> </li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>C++</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>[BUG] [CPP-UE4] 修复嵌套容器类型的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12747" target="_blank">codegen #12747</a></li> 
 <li>[cpp-qt-client] 添加对 AnyType 对象的支持<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12642" target="_blank">#12642</a></li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Crystal</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>[crystal][client] 设置标志时跳过生成操作示例<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12539" target="_blank">#12539</a></li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Dart</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>[Dart][Client] 支持解析 DateTime <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12433" target="_blank">#12433</a></li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Documentation</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>[html2] 为嵌套对象添加递归 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12428" target="_blank">#12428</a></li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Elixir</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>改进的 Elixir 代码生成 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12751" target="_blank">#12751</a></li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Elm</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li> <p>修复包含 UUID 的路径的无效 elm 代码 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12506" target="_blank">#12506</a></p> </li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Go</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li> <p>[Go] 使用 EqualFold 代替小写字符串比较 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12741" target="_blank">#12741</a></p> </li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>GraphQL</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li> <p>Graphql nodejs express 服务器列表修 复<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12476" target="_blank">#12476</a></p> </li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Haskell</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>[haskell-http-client] 放宽 Aeson 约束以允许 Aeson 1 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12486" target="_blank">#12486</a></li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Java</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>更新 jackson databind 到 2.12.6.1 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12698" target="_blank">#12698</a></li> 
 <li>[Java] 将 jackson-databind-nullable 更新为 0.2.3<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12693" target="_blank"> #12693</a></li> 
 <li>[Java] 将 RESTEasy 库更新到新版本<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12688" target="_blank">#12688</a></li> 
 <li>修复 Java 库中的 HTML-escaped token 和授权 URL <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12677" target="_blank">#12677</a></li> 
 <li>[java][okhttp-gson] 使用 builder 时保持 AST 的大小 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12610" target="_blank">#12610</a></li> 
 <li>[Spring] 修复参数中的 cookie 总是按要求生成<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12599" target="_blank">#12599</a></li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Kotlin</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>[Kotlin][Client] 替换 java.nio.* 以避免在 Android API 25 及以下版本中崩溃 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12529" target="_blank">#12529</a></li> 
 <li>[Kotlin] 修复使用 allOf 时的无效代码 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12594" target="_blank">#12594</a></li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>OCaml</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>[OCaml] 代码生成修复<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12395" target="_blank">#12395</a></li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>PHP</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>[PHP] 增强 Symfony 生成器 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12532" target="_blank">#12532</a></li> 
 <li>[php] 修复 PHP 客户端中的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fimplements" target="_blank">@implements</a> 注释 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F11908" target="_blank">#11908</a></li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>PowerShell</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>[PowerShell] 支持枚举整数 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12752" target="_blank">#12752</a></li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Python</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li> <p>修复 python-experimental 中的双重序列化错误 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12561" target="_blank">#12561</a></p> </li> 
 <li> <p>为 v3.0.3 单元测试规范添加示例客户端，包括自动生成的模型测试，在 CI 中运行测试 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12619" target="_blank">#12619</a></p> </li> 
 <li> <p>修复 GetItem 不适用于客户端生成的 allOf 模型，以及自 5.2.0 以来的故障 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12239" target="_blank">#12239</a></p> </li> 
 <li> <p>在 Python 2 和 Python 3 中使用 print() 函数<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12467" target="_blank">#12467</a></p> </li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Rust</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>修复字符串和 UUID 类型上的 double “String” <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12409" target="_blank">#12409</a></li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>R</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li> <p>[R] 将 toString 方法添加到 oneOf/anyOf 对象<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12727" target="_blank">#12727</a></p> </li> 
 <li> <p>[R] 修复嵌套 oneOf/anyOf <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12723" target="_blank">#12723</a></p> </li> 
 <li> <p>[R] 修复具有特殊项目名称的模型的反序列<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12658" target="_blank">化 #12658</a></p> </li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Swift</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li> <p>[swift5] 使其有可能选择不遵守 JSONncodable 一致性 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12664" target="_blank">#12664</a></p> </li> 
</ul> 
<p style="text-align:start"><strong><span><span><span><span><span style="color:#24292f"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>TypeScript</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<ul> 
 <li>[typescript-fetch] 在中间件中支持错误处理程序<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12716" target="_blank">#12716</a></li> 
 <li>修复 typescript 节点默认枚举<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Fpull%2F12633" target="_blank">#12633</a></li> 
</ul> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FOpenAPITools%2Fopenapi-generator%2Freleases%2Ftag%2Fv6.0.1" target="_blank">https://github.com/OpenAPITools/openapi-generator/releases/tag/v6.0.1</a></p>
                                        </div>
                                      
</div>
            