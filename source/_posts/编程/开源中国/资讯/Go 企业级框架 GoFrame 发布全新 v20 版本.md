
---
title: 'Go 企业级框架 GoFrame 发布全新 v2.0 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3442'
author: 开源中国
comments: false
date: Wed, 09 Mar 2022 00:37:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3442'
---

<div>   
<div class="content">
                                                                                            <div style="margin-left:0; margin-right:0; text-align:start"> 
 <div style="margin-left:-15px; margin-right:-15px"> 
  <div style="margin-left:0; margin-right:0"> 
   <div style="margin-left:0; margin-right:0"> 
    <div style="margin-left:0; margin-right:0"> 
     <p style="margin-left:0; margin-right:0">大家好啊！万众瞩目的<code>GoFrame v2</code>版本终于发布了正式版本！本次版本包含了大量改进以及新特性，同时新增了一些开创性的功能特性。</p> 
     <p style="margin-left:0; margin-right:0">去年夏天到今年春天，一路以来的努力，希望大家满意。</p> 
     <p style="margin-left:0; margin-right:0">感谢所有社区小伙伴的贡献，感谢社区朋友们的支持！</p> 
     <p style="margin-left:0; margin-right:0">新的一年，我们继续，脚踏实地，不忘初心！</p> 
     <h1 style="margin-left:0; margin-right:0">一、重要特性</h1> 
     <h2 style="margin-left:0; margin-right:0">1、新版工程设计</h2> 
     <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
      <li>更加严谨规范</li> 
      <li>命名风格的规范</li> 
      <li>指针与值传递参数的规范</li> 
      <li>进一步简便、提高开发效率</li> 
      <li>新版开发工具支持工程规范准确落地</li> 
      <li><code>Entity/DAO/DO</code>特性</li> 
      <li>面向接口化设计</li> 
      <li>更多详细介绍：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D30740161" target="_blank">工程开发设计</a></li> 
     </ul> 
     <h2 style="margin-left:0; margin-right:0">2、全链路跟踪特性</h2> 
     <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
      <li>可观测性更进一步：大胆的前瞻以及决心</li> 
      <li>框架默认启用<code>OpenTelemetry</code>特性</li> 
      <li>框架默认创建<code>TraceID</code>，按照<code>OpenTelemetry</code>生成标准</li> 
      <li>框架核心组件均支持链路跟踪信息传递</li> 
      <li>日志组件支持链路信息打印</li> 
      <li>更多详细介绍：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D35356689" target="_blank">全链路跟踪设计</a></li> 
     </ul> 
     <h2 style="margin-left:0; margin-right:0">3、规范路由注册特性</h2> 
     <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
      <li>规范化API按照结构化编程设计</li> 
      <li>规范化API接口方法参数风格定义</li> 
      <li>更加简化的路由注册与维护</li> 
      <li>统一接口返回数据格式设计</li> 
      <li>自动的API参数对象化接收与校验</li> 
      <li>自动生成基于标准<code>OpenAPIv3</code>协议的接口文档</li> 
      <li>自动生成<code>SwaggerUI</code>页面</li> 
      <li>更多详细介绍：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D30736904" target="_blank">路由注册-规范路由</a></li> 
     </ul> 
     <h2 style="margin-left:0; margin-right:0">4、全错误堆栈特性</h2> 
     <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
      <li>框架层面所做的重大决定</li> 
      <li>框架<span> </span><strong>所有</strong><span> </span>组件错误均支持错误堆栈</li> 
      <li>详细介绍：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D35356691" target="_blank">全错误堆栈设计</a></li> 
     </ul> 
     <h2 style="margin-left:0; margin-right:0">5、全新错误码特性</h2> 
     <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
      <li>采用接口化设计，扩展性高</li> 
      <li>提供可供选择的常见错误码</li> 
      <li>框架核心组价底层已增加错误码支持，例如根据<code>error</code>中的错误码可以识别是否<code>DB</code>执行错误</li> 
      <li>更多详细介绍：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D30739375" target="_blank">错误处理-错误码特性</a></li> 
     </ul> 
     <h2 style="margin-left:0; margin-right:0">6、组件接口化设计</h2> 
     <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
      <li>自顶向下统一化的接口化设计</li> 
      <li>核心组件均采用接口化设计</li> 
      <li>更高的扩展性、可定制性</li> 
      <li>更多详细介绍：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D35356693" target="_blank">接口化与泛型设计</a></li> 
     </ul> 
     <h2 style="margin-left:0; margin-right:0">7、框架泛型的支持</h2> 
     <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
      <li>什么是框架<code>gvar</code>泛型？</li> 
      <li>框架<code>gvar</code>泛型在框架核心组件中的大量使用</li> 
      <li>框架<code>gvar</code>泛型的重要价值</li> 
      <li>为什么不建议在顶层业务中使用泛型</li> 
      <li>更多详细介绍：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D35356693" target="_blank">接口化与泛型设计</a></li> 
     </ul> 
     <h2 style="margin-left:0; margin-right:0">8、ORM的大量改进</h2> 
     <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
      <li>详细介绍：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D1114686" target="_blank">数据库ORM</a></li> 
     </ul> 
     <h2 style="margin-left:0; margin-right:0">9、其他重要改进</h2> 
     <h3 style="margin-left:0; margin-right:0">1）日志组件<code>Handler</code>特性</h3> 
     <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
      <li>采用中间件设计</li> 
      <li>支持多个<code>Handler</code>处理</li> 
      <li>为开发者自定义日志处理提供了更灵活强大的支持</li> 
      <li>更多详细介绍：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D17207121" target="_blank">日志组件-Handler</a></li> 
     </ul> 
     <h3 style="margin-left:0; margin-right:0">2）日志组件颜色打印</h3> 
     <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
      <li>在终端中默认输出颜色打印</li> 
      <li>默认不同级别不同的颜色，可配置</li> 
      <li>输出到文件/自定义<code>Writer</code>默认关闭，可通过相关配置开启</li> 
      <li>更多详细介绍：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D20086799" target="_blank">日志组件-颜色打印</a></li> 
     </ul> 
     <h3 style="margin-left:0; margin-right:0">4）调试模式介绍完善</h3> 
     <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
      <li>更多详细介绍：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D1114207" target="_blank">调试模式</a></li> 
     </ul> 
     <h1 style="margin-left:0; margin-right:0">二、功能改进</h1> 
     <h2 style="margin-left:0; margin-right:0">1、数据组件</h2> 
     <ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
      <li><code>/database/gdb</code> 
       <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
        <li>废弃<code>Table</code>方法，统一使用<code>Model</code>方法创建<code>Model</code>对象。</li> 
        <li>废弃<code>Model</code>中的<code>Struct/Structs</code>方法，统一使用<code>Scan</code>方法执行查询结果到<code>Struct</code>对象/对象数组映射转换：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D7301845" target="_blank">ORM查询-Scan</a></li> 
        <li>废弃<code>BatchInsert/BatchReplace/BatchSave</code>方法，统一使用<code>Insert/Replace/Save</code>方法实现，内部自动实现参数类型识别采用单条写入还是批量写入：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D1114344" target="_blank">ORM链式操作-写入保存</a></li> 
        <li>增加<code>DoFilter</code>接口方法，用于<code>ORM</code>提交执行<code>SQL&Args</code>到底层<code>driver</code>之前的<code>SQL&Args</code>自定义过滤：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D1114158" target="_blank">ORM接口开发-回调处理</a></li> 
        <li>增加<code>DoCommit</code>接口方法，用于<code>ORM</code>提交执行<code>SQL&Args</code>到底层<code>driver</code>之前的自定义处理：https://</li> 
        <li>增加<code>ConvertDataForRecord</code>接口方法，用于自定义的数据转换处理。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D1114158" target="_blank">ORM接口开发-回调处理</a></li> 
        <li>增加<code>Raw</code>方法，用于通过原始<code>SQL</code>语句构建<code>Model</code>对象，随后可以使用<code>Model</code>的链式操作以及各种特性：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D1114373" target="_blank">ORM链式操作-模型创建</a></li> 
        <li>增加<code>Handler</code>特性，用于自定义的<code>Model</code>对象修改，并返回新的<code>Model</code>对象，可<span style="color:#172b4d">轻松地复用常见的逻辑</span>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D20087340" target="_blank">ORM链式操作-Handler特性</a></li> 
        <li>增加<code>Union/UnionAll</code>特性，用于多条<code>SQL/Model</code>的查询结果合并：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D7302295" target="_blank">ORM查询-Union/UnionAll</a></li> 
        <li>增加<code>With</code>特性对条件查询以及排序语句的配置支持：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D7297190" target="_blank">模型关联-With特性</a></li> 
        <li>增加<code>OnDuplicate/OnDuplicateEx</code>方法，用于指定<code>Save</code>方法的更新/不更新字段：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D1114344" target="_blank">ORM链式操作-写入保存</a></li> 
        <li>增加<code>Wheref/WhereOrf</code>方法，用于带有格式化字符串语句的条件传递：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D7301832" target="_blank">ORM查询-Where/WhereOr/WhereNot</a></li> 
        <li>增加<code>WhereLT/WhereLTE/WhereGT/WhereGTE</code>以及<code>WhereOrLT/WhereOrLTE/WhereOrGT/WhereOrGTE</code>方法，用以为ORM添加常见的比较条件：https://</li> 
        <li>增加<code>WherePrefix/WhereOrPrefix</code>方法，用以在为条件字段加上表前缀，常用于关联查询中：https://</li> 
        <li>增加<code>FieldsPrefix/FieldsExPrefix</code>方法，用于为查询的字段增加自定义的表前缀，常用于关联查询中：https://</li> 
        <li>增加<code>FieldsCount/FieldsSum/FieldsMin/FieldsMax/FieldsAvg</code>方法，用于增加常见的统一查询条件：https://</li> 
        <li>增加<code>LeftJoinOnField/RightJoinOnField/InnerJoinOnField</code>方法，用于便捷关联带有相同字段名称的表：https://</li> 
        <li>增加<code>OmitEmptyWhere/OmitEmptyData</code>方法，用于特定过滤<code>Where</code>条件和<code>Data</code>数据中的空值数据：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D1114229" target="_blank">ORM链式操作-字段过滤</a></li> 
        <li>增加<code>OmitNil/OmitNilWhere/OmitNilData</code>方法，用于特定过滤<code>Where</code>条件和<code>Data</code>数据中的<code>nil</code>数据：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D1114229" target="_blank">ORM链式操作-字段过滤</a></li> 
        <li>增加<code>TimeZone</code>配置项，用于数据库查询的自定义时区转换（目前支持<code>mysql/pgsql</code>）：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D1114245" target="_blank">ORM使用配置</a></li> 
        <li>改进<code>Cache</code>缓存特性，支持增加准确的缓存参数控制：https://</li> 
        <li>增加<code>Close</code>方法，用于手动关闭数据库连接：https://</li> 
        <li>去掉<code>ORM</code>在使用没有自定义配置时默认<code>100</code>连接数的配置限制。</li> 
        <li>改进时间维护特性，不再自动过滤开发者提交的<code>CreatedAt/UpdatedAt/DeletedAt</code>相关参数，意味着开发者可以在<code>ORM</code>操作中自定义相关时间字段的更新。</li> 
        <li>改进数据库执行的SQL日志记录，增加影响行数记录：https://</li> 
        <li>接口方法<code>HandleSqlBeforeCommit</code>名称修改为了<code>DoCommit</code>。</li> 
        <li>数据库方法操作统一增加<code>context.Context</code>作为第一必须参数。</li> 
        <li>修复<code>gdb</code>组件的<code>With</code>特性多层级查询失效问题。</li> 
        <li>删除查询结果类型<code>Record/Result</code>的所有已废弃的方法。</li> 
        <li>单元测试完善。</li> 
       </ol> </li> 
      <li><code>/database/gredis</code> 
       <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
        <li> <p style="margin-left:0; margin-right:0">采用适配器模式，以接口化设计重构该组件，以提高扩展性：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D30739675" target="_blank">Redis-接口化设计</a></p> </li> 
        <li>默认提供基于第三方<code>goredis</code>包的适配器实现，增加了对<code>Redis</code>集群的支持：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D1114217" target="_blank">Redis-配置管理</a></li> 
        <li>由于集群特性的支持，配置文件格式发生改变：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D1114217" target="_blank">Redis-配置管理</a></li> 
       </ol> </li> 
     </ol> 
     <h2 style="margin-left:0; margin-right:0">2、网络组件</h2> 
     <ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
      <li><code>/net/ghttp</code> 
       <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
        <li>新增路由注册方式：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D30736904" target="_blank">路由注册-规范路由</a></li> 
        <li>默认将<code>Request</code>对象注入到<code>ctx</code>上下文对象中，并增加<code>RequestFromCtx/g.RequestFromCtx</code>方法获取<code>ctx</code>中的<code>Request</code>对象。</li> 
        <li>将<code>Client</code>功能特性进行抽离，封装为<code>gclient</code>组件：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fdisplay%2Fgf%2FHTTPClient" target="_blank">HTTPClient</a></li> 
        <li><code>Server</code>日志增加对<code>ctx</code>上下文链路信息打印的支持，并改进日志格式：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D7298186" target="_blank">链路跟踪</a></li> 
        <li>参数获取返回统一使用<code>*gvar.Var</code>泛型对象。</li> 
        <li>废弃<code>ghttp</code>中相关的<code>HTTP Client</code>直接操作方法，必须通过创建<code>Client</code>对象来实现客户端访问操作。</li> 
        <li>废弃<code>Controller</code>路由注册方式，并删除相关实现逻辑代码。</li> 
       </ol> </li> 
      <li><code>/net/gtrace</code> 
       <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
        <li>升级<code><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fgo.opentelemetry.io%2Fotel" target="_blank">go.opentelemetry.io/otel</a></code>到最新的正式版。</li> 
        <li>完善全新的链路跟踪使用文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D3673684" target="_blank">链路跟踪</a></li> 
       </ol> </li> 
     </ol> 
     <h2 style="margin-left:0; margin-right:0">3、系统组件</h2> 
     <ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
      <li><code>/os/glog</code> 
       <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
        <li>为推进可观测性特性，落实链路跟踪规范，所有日志打印方法均增加<code>context.Context</code>参数。</li> 
        <li>日志组件增加了<code>Handler</code>特性，采用中间件设计、支持多个<code>Handler</code>处理，为开发者自定义日志处理提供了更灵活强大的支持：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D17207121" target="_blank">日志组件-Handler</a></li> 
        <li>日志组件增加了对内容的颜色打印特性支持，在终端中默认输出颜色打印，输出到文件/自定义<code>Writer</code>默认关闭、可通过相关配置开启：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D20086799" target="_blank">日志组件-颜色打印</a></li> 
        <li>废弃<code>Println</code>方法。</li> 
        <li>文档更新：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D1114673" target="_blank">日志组件</a></li> 
       </ol> </li> 
      <li><code>/os/gres</code> 
       <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
        <li>新增<code>Export</code>方法用于将资源组件中的文件导出到本地磁盘：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D35359297" target="_blank">资源管理-方法介绍</a></li> 
       </ol> </li> 
      <li><code>/os/gfile</code> 
       <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
        <li>新增<code>SizeFormat</code>方法用于获取指定文件格式化后的大小字符串。</li> 
        <li>文档更新：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D1114225" target="_blank">文件管理-gfile</a></li> 
       </ol> </li> 
      <li><code>/os/gcache</code> 
       <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
        <li>采用适配器模式，以接口化设计重构该组件，以提高扩展性：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D1114265" target="_blank">缓存管理-接口化设计</a></li> 
        <li>默认提供了基于进程内存的缓存实现：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D1114311" target="_blank">缓存管理-内存缓存</a></li> 
        <li>所有操作方法增加了<code>context.Context</code>上下文参数。</li> 
        <li>参数获取返回统一使用<code>*gvar.Var</code>泛型对象。</li> 
        <li>增加<code>Must*</code>方法，用以直接获取参数并在产生错误时直接<code>panic</code>。</li> 
       </ol> </li> 
      <li><code>/os/gcfg</code> 
       <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
        <li>采用适配器模式，以接口化设计重构该组件，以提高扩展性：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D30739639" target="_blank">配置管理-接口化设计</a></li> 
        <li>默认提供了基于文件系统的配置管理实现：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D1114668" target="_blank">配置管理</a></li> 
        <li>参数获取返回统一使用<code>*gvar.Var</code>泛型对象。</li> 
        <li>所有操作方法增加了<code>context.Context</code>上下文参数。</li> 
        <li>增加<code>GetWithEnv</code>方法，当配置适配器中无法查找到对应的参数时，将会自动读取环境变量中的相应参数：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D1114668%23id-%25E9%2585%258D%25E7%25BD%25AE%25E7%25AE%25A1%25E7%2590%2586-%25E9%2585%258D%25E7%25BD%25AE%25E8%25AF%25BB%25E5%258F%2596" target="_blank">配置管理-配置读取</a></li> 
        <li>增加<code>GetWithCmd</code>方法，当配置适配器中无法查找到对应的参数时，将会自动读取命令行参数中的相应参数：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D1114668%23id-%25E9%2585%258D%25E7%25BD%25AE%25E7%25AE%25A1%25E7%2590%2586-%25E9%2585%258D%25E7%25BD%25AE%25E8%25AF%25BB%25E5%258F%2596" target="_blank">配置管理-配置读取</a></li> 
        <li>增加<code>Must*</code>方法，用以直接获取参数并在产生错误时直接<code>panic</code>。</li> 
        <li>配置组件易用性改进，通过单例对象访问配置组件将会按照<code>toml/yaml/yml/json/ini/xml</code>文件后缀自动检索配置文件：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D1114668" target="_blank">配置管理</a></li> 
       </ol> </li> 
      <li><code>/os/gcmd</code> 
       <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
        <li>参数获取返回统一使用<code>*gvar.Var</code>泛型对象。</li> 
        <li>全新的多层级命令行管理方式，支持自动生成命令行使用提示：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D35357521" target="_blank">命令管理-命令行对象</a></li> 
        <li>增加基于对象的命令行管理方式，更适合大量的终端命令场景：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D35357523" target="_blank">命令管理-结构化参数</a></li> 
       </ol> </li> 
      <li><code>/os/genv</code> 
       <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
        <li>参数获取返回统一使用<code>*gvar.Var</code>泛型对象。</li> 
       </ol> </li> 
      <li><code>/os/gcron</code> 
       <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
        <li>定时任务方法定义增加<code>context.Context</code>参数。</li> 
        <li>所有创建定时任务方法增加<code>context.Context</code>参数。</li> 
        <li>文档更新：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D1114187" target="_blank">定时任务-gcron</a></li> 
       </ol> </li> 
      <li><code>/os/gtime</code> 
       <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
        <li>废弃<code>Second/Millisecond/Microsecond/Nanosecond</code>包方法，使用<code>Timestamp/TimestampMilli/TimestampMicro/TimestampNano</code>方法替代。</li> 
        <li>文档更新：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D1114883" target="_blank">时间管理-gtime</a></li> 
       </ol> </li> 
      <li><code>/os/gtimer</code> 
       <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
        <li>定时器方法定义增加<code>context.Context</code>参数。</li> 
        <li>所有创建定时器方法增加<code>context.Context</code>参数。</li> 
        <li>改进基于优先级队列数据结构存储的定时任务执行检测机制，提高执行性能。</li> 
        <li>文档更新：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D1114363" target="_blank">定时器-gtimer</a></li> 
       </ol> </li> 
      <li><code>/os/grpool</code> 
       <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
        <li>回调方法定义增加<code>context.Context</code>参数。</li> 
        <li><code>goroutine</code>池任务添加方法增加<code>context.Context</code>参数。</li> 
        <li>文档更新：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D1114246" target="_blank">协程管理-grpool</a></li> 
       </ol> </li> 
      <li><code>/os/gsession</code> 
       <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
        <li><code>gsession.Storage</code>接口增加<code>ctx</code>上下文参数输输入，用于承接上下文信息、实现完整的链路跟踪。并未保证严谨性增加<code>error</code>返回参数：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fdisplay%2Fgf%2FSession" target="_blank">Session</a></li> 
        <li>参数获取返回统一使用<code>*gvar.Var</code>泛型对象。</li> 
       </ol> </li> 
      <li><code>/os/gview</code> 
       <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
        <li>模板解析方法统一增加<code>context.Context</code>参数。</li> 
        <li>增加<code>plus/minus/times/divide</code>四则运算内置模板方法。</li> 
        <li>文档更新：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D1114680" target="_blank">模板引擎</a></li> 
       </ol> </li> 
      <li><code>/os/gstructs</code> 
       <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
        <li>将框架<code>internal</code>中的<code>structs</code>包开放，命名为<code>gstructs</code>，用于<code>struct</code>反射操作的高级使用包：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D30739219" target="_blank">对象信息-gstructs</a></li> 
       </ol> </li> 
     </ol> 
     <h2 style="margin-left:0; margin-right:0">4、错误处理</h2> 
     <ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
      <li><code>/errors/gerror</code> 
       <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
        <li>增加<code>Message</code>方法，用于获取指定错误码的错误信息。</li> 
        <li>增加<code>CodeMessage</code>方法，用于获取指定错误的错误码信息。</li> 
        <li>增加<code>NewOption</code>方法，用于自定义配置的错误对象创建，献给框架高级玩家。</li> 
        <li>增加<code>HasStack</code>方法，用于判断给定的error接口对象是否实现（包含）了堆栈信息。</li> 
        <li>错误码从整型改为接口对象，以实现可定制性并提高可扩展性，详情参考<code>gcode</code>组件介绍：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D30739375" target="_blank">错误处理-错误码特性</a></li> 
        <li>提高易用性，改进<code>NewCode/NewCodeSkip/WrapCode/WrapCodeSkip</code>方法，调增<code>text</code>输入参数为非必须，默认使用对应错误码的<code>Message</code>信息。</li> 
       </ol> </li> 
      <li><code>/errors/gcode</code> 
       <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
        <li>增加<code>gcode</code>错误码组件，提供可定制型和扩展性极强的错误码管理，结合<code>gerror</code>组件实现强大的错误处理：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D3671864" target="_blank">错误处理-错误码使用</a></li> 
       </ol> </li> 
     </ol> 
     <h2 style="margin-left:0; margin-right:0">5、其他组件</h2> 
     <ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
      <li><code>/container/garray</code> 
       <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
        <li>各数组类型统一增加<code>At</code>方法，用于直接获取返回索引位置的数据。</li> 
        <li>文档更新：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D27756273" target="_blank">数组类型-方法介绍</a></li> 
       </ol> </li> 
      <li><code>/debug/gdebug</code> 
       <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
        <li>增加<code>TestDataContent</code>方法，用于直接获取测试包下<code>testdata</code>目录下指定路径文件内容。</li> 
        <li>文档更新：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D1114365" target="_blank">调试功能-gdebug</a></li> 
       </ol> </li> 
      <li><code>/encoding/gjson</code> 
       <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
        <li>废弃大部分的<code>Get*</code>方法，统一使用<code>Get</code>方法获取指定<code>pattern</code>的内容，并统一返回<code>*gvar.Var</code>泛型对象，开发者根据业务场景自行通过对应方法便捷转换为特定类型变量。</li> 
        <li>增加若干<code>Must*</code>方法。</li> 
        <li>使用文档全面更新：https://</li> 
       </ol> </li> 
      <li><code>/frame/g</code> 
       <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
        <li>增加<code>ModelRaw</code>方法，用于便捷创建基于原生<code>SQL</code>的数据库<code>Model</code>对象。</li> 
        <li>为通过<code>/frame/g</code>模块创建的<code>ORM</code>对象增加<code>logger</code>配置，通过自动读取配置文件，自动初始化：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D1114245" target="_blank">ORM使用配置</a></li> 
        <li>为通过<code>/frame/g</code>模块创建的<code>Server</code>对象增加<code>logger</code>配置，通过自动读取配置文件，自动初始化：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D1114489" target="_blank">服务配置</a></li> 
       </ol> </li> 
      <li><code>/frame/gmvc</code> 
       <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
        <li>标记废除<code>gmvc</code>耦合模块，未来不再进一步支持。</li> 
       </ol> </li> 
      <li><code>/util/gutil</code> 
       <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
        <li>改进实现<code>Dump</code>方法，不再使用<code>json</code>包实现类型打印，而是自实现了对任意类型的打印特性，并且支持打印详细的数据类型：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D30739221" target="_blank">工具方法-gutil</a></li> 
        <li>增加<code>SliceToMapWithColumnAsKey</code>方法，用以将<code>Slice</code>按照一定规则转换为<code>Map</code>。</li> 
       </ol> </li> 
      <li><code>/utils/gvalid</code> 
       <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
        <li>增加<code>bail</code>校验规则，以及<code>Bail</code>链式操作方法，用以在数据校验不通过时直接退出校验，不再执行后续校验规则。</li> 
        <li>增加<code>datetime</code>校验规则，用以校验常用日期时间类型，其中日期之间支持的连接符号只支持<code>-</code>，格式如：<code>2006-01-02 12:00:00</code>。</li> 
        <li>去掉包校验方法，统一使用链式操作实现数据校验。</li> 
        <li>所以校验方法增加<code>context.Context</code>参数。</li> 
        <li>全新、超完善的数据校验组件使用文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D1114678" target="_blank">数据校验</a></li> 
       </ol> </li> 
     </ol> 
     <div style="margin-left:0; margin-right:0"> 
      <div style="margin-left:0; margin-right:0"> 
       <p style="margin-left:0; margin-right:0">其他大量的改进细节，这里不再赘述，感兴趣的小伙伴可参阅官网<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2F" target="_blank">goframe.org</a></p> 
      </div> 
     </div> 
     <h1 style="margin-left:0; margin-right:0">三、CLI工具链 </h1> 
     <ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
      <li>采用全新<code>gcmd</code>命令行对象封装重构实现。</li> 
      <li>改进<code>init</code>命令，支持<code>SingleRepo/MonoRepo</code>两种仓库初始化。并且项目初始化不再依赖远端仓库。</li> 
      <li>改进<code>gen dao</code>命令，采用全新的<code>V2</code>工程化设计，自动生成<code>entity/dao/dto</code>代码文件。</li> 
      <li>去掉<code>update</code>命令，工具的更新统一走<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgogf%2Fgf-cli" target="_blank">https://github.com/gogf/gf-cli</a></li> 
      <li>去掉<code>get</code>命令。</li> 
      <li>全新文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D1114260" target="_blank">开发工具</a></li> 
     </ol> 
    </div> 
   </div> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            