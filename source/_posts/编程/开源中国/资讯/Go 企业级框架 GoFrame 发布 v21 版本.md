
---
title: 'Go 企业级框架 GoFrame 发布 v2.1 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7250'
author: 开源中国
comments: false
date: Tue, 21 Jun 2022 21:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7250'
---

<div>   
<div class="content">
                                                                                            <p style="color:#172b4d; margin-left:0; margin-right:0; text-align:start">大家好，本次发布的<code>v2.1</code>版本包含一些与业务实践相关的功能特性、改进以及Bug Fix，建议大家升级。</p> 
<h1 style="margin-left:0; margin-right:0; text-align:start">新特性</h1> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>开发工具新增<code>gen service</code>命令，支持自动化地根据<code>logic</code>层级代码，生成<code>service</code>接口代码、实现注入：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D49770772" target="_blank">接口维护-gen service</a></li> 
 <li> 数据库组件特性： 
  <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
   <li>新增<code>WhereBuilder</code>特性，用于更加灵活的<code>SQL</code>条件语句组合：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D7301832" target="_blank">ORM查询-Where/WhereOr/WhereNot</a></li> 
   <li>新增<code>Hook</code>特性，用于自定义钩子事件处理：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D48892502" target="_blank">ORM链式操作-Hook特性</a></li> 
  </ol> </li> 
 <li>框架新增<code>DeepCopy</code>特性，用于类型的深度拷贝： 
  <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
   <li>新增<code>gutil.Copy</code>方法，用于深度拷贝指定内容。</li> 
   <li>泛型类型新增<code>Copy</code>方法，用于深度拷贝自身内容。</li> 
   <li>框架部分数据类型已支持深度拷贝特性，例如：<code>gvar, garray, gmap</code>等基础容器类型。</li> 
  </ol> </li> 
</ol> 
<h1 style="margin-left:0; margin-right:0; text-align:start">主要改进</h1> 
<h2 style="margin-left:0; margin-right:0; text-align:start">社区组件</h2> 
<p style="color:#172b4d; margin-left:0; margin-right:0; text-align:start"><strong>ORM驱动实现</strong></p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>新增<code>drivers/clickhouse</code>，用于对接<code>clickhouse</code>到<code>goframe ORM</code>组件。</li> 
 <li>完善<code>clickhouse/mssql/pgsql/sqlite/oracle</code>组件单元测试。</li> 
 <li>将<code>mysql</code>驱动从主库迁移到社区模块，便于将<code>mysql</code>从主库解耦。因此从后续版本开始，开发者需要手动引入驱动依赖：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgogf%2Fgf%2Ftree%2Fmaster%2Fcontrib%2Fdrivers" target="_blank">https://github.com/gogf/gf/tree/master/contrib/drivers</a></li> 
</ol> 
<p style="color:#172b4d; margin-left:0; margin-right:0; text-align:start"><strong>注册发现实现</strong></p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>新增<code>polaris</code>北极星服务注册接口实现：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgogf%2Fgf%2Ftree%2Fmaster%2Fcontrib%2Fregistry%2Fpolaris" target="_blank">https://github.com/gogf/gf/tree/master/contrib/registry/polaris</a></li> 
 <li>改进<code>etcd</code>服务注册发现接口实现组件：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgogf%2Fgf%2Ftree%2Fmaster%2Fcontrib%2Fregistry%2Fetcd" target="_blank">https://github.com/gogf/gf/tree/master/contrib/registry/etcd</a></li> 
</ol> 
<h2 style="margin-left:0; margin-right:0; text-align:start">注册发现</h2> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>将<code>Service</code>实现对象改进为接口定义，并提供默认的<code>Service</code>实现，提高扩展性和易用性。</li> 
 <li>改进<code>HTTP/GRPC Client&Server</code>对接实现。</li> 
</ol> 
<h2 style="margin-left:0; margin-right:0; text-align:start">负载均衡</h2> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>改进<code>Node</code>接口定义，新增<code>Nodes</code>接口定义。</li> 
 <li>修复<code>HTTP Client</code>下的服务发现负载均衡问题。</li> 
</ol> 
<h2 style="margin-left:0; margin-right:0; text-align:start">网络组件</h2> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li><code>gclient</code> 
  <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
   <li>改进服务发现实现逻辑。</li> 
   <li>修复客户端关闭错误，引起的连接池无法复用问题。</li> 
  </ol> </li> 
 <li><code>ghttp</code> 
  <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
   <li>改进<code>Request.GetUrl</code>方法对<code>URL Schema</code>获取细节。</li> 
   <li>参数接收支持<code>UploadFile</code>属性自动接收。</li> 
   <li>新增接口文档自定义UI指导文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D47703685" target="_blank">接口文档-自定义UI</a></li> 
   <li>接口文档默认依赖的外部<code>JS CDN</code>改为<code>unpkg.com</code>。</li> 
   <li>改进服务注册实现逻辑。</li> 
   <li>改进内部细节实现逻辑。</li> 
   <li>修复参数为空判断问题。</li> 
  </ol> </li> 
 <li><code>goai</code> 
  <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
   <li>改进更规范化符合<code>OpenAPIV3</code>协议实现。</li> 
   <li>支持所有<code>x-</code>开头的自定义标签，自动添加<code>OpenAPIV3</code>的结果中。</li> 
  </ol> </li> 
</ol> 
<h2 style="margin-left:0; margin-right:0; text-align:start">系统组件</h2> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li><code>gcfg</code> 
  <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
   <li>默认的文件系统接口实现新增对<code>property</code>文件格式的支持。</li> 
  </ol> </li> 
 <li><code>gcmd</code> 
  <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
   <li>参数解析新增<code>CaseSensitive</code>配置，默认不区分大小写解析，特别针对结构化参数接收影响较大：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D35357523" target="_blank">命令管理-结构化参数</a></li> 
   <li>新增跨进程的链路跟踪特性：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D51304910" target="_blank">命令管理-链路跟踪</a></li> 
  </ol> </li> 
 <li><code>glog</code> 
  <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
   <li>新增全局的<code>Handler</code>设置功能，开发者可以全局自定义处理<code>glog</code>组件的所有日志，例如全局输出<code>JSON</code>文件格式：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D17207121" target="_blank">日志组件-Handler</a></li> 
   <li>新增默认的<code>JSON</code>格式<code>Handler</code>供开发者使用：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D17207121" target="_blank">日志组件-Handler</a></li> 
  </ol> </li> 
 <li><code>gsession</code> 
  <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
   <li>解决当访问用户过多造成的内存占用过大的问题。</li> 
  </ol> </li> 
 <li><code>gproc</code> 
  <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
   <li>新增跨进程的链路跟踪特性：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D51304915" target="_blank">进程管理-链路跟踪</a></li> 
  </ol> </li> 
</ol> 
<h2 style="margin-left:0; margin-right:0; text-align:start">容器组件</h2> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li><code>garray</code> 
  <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
   <li>改进<code>Unique</code>方法性能，增加<code>DeepCopy</code>接口实现。</li> 
  </ol> </li> 
 <li><code>glist</code> 
  <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
   <li>增加<code>DeepCopy</code>接口实现。</li> 
  </ol> </li> 
 <li><code>gmap</code> 
  <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
   <li>增加<code>DeepCopy</code>接口实现。</li> 
  </ol> </li> 
 <li><code>gset</code> 
  <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
   <li>增加<code>DeepCopy</code>接口实现。</li> 
  </ol> </li> 
 <li><code>gtype</code> 
  <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
   <li>增加<code>DeepCopy</code>接口实现。</li> 
  </ol> </li> 
 <li><code>gvar</code> 
  <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
   <li>增加<code>Copy</code>方法，用于深度拷贝当前泛型对象。</li> 
   <li>增加<code>DeepCopy</code>接口实现。</li> 
  </ol> </li> 
</ol> 
<h2 style="margin-left:0; margin-right:0; text-align:start">数据库组件</h2> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li><code>gdb</code> 
  <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
   <li>新增<code>WhereBuilder</code>特性，用于更加灵活的<code>SQL</code>条件语句组合：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D7301832" target="_blank">ORM查询-Where/WhereOr/WhereNot</a></li> 
   <li>新增<code>HOOK</code>特性，用于自定义钩子事件处理：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D48892502" target="_blank">ORM链式操作-Hook特性</a></li> 
   <li>改进数据提交到底层<code>driver</code>前的数据转换处理逻辑。</li> 
   <li>将<code>mysql</code>驱动从主库迁移到社区模块，便于将<code>mysql</code>从主库解耦。因此从后续版本开始，开发者需要手动引入驱动依赖：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgogf%2Fgf%2Ftree%2Fmaster%2Fcontrib%2Fdrivers" target="_blank">https://github.com/gogf/gf/tree/master/contrib/drivers</a></li> 
  </ol> </li> 
</ol> 
<h2 style="margin-left:0; margin-right:0; text-align:start">编解码组件</h2> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li><code>gproperty</code> 
  <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
   <li>新增<code>gproperty</code>组件，用于解析<code>Java Property</code>格式文件。</li> 
  </ol> </li> 
 <li><code>gjson</code> 
  <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
   <li>新增对<code>property</code>文件格式的编解码、数据操作支持：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D1114881" target="_blank">通用编解码-gjson</a></li> 
   <li>修复对大整形数据读取的精度丢失问题。</li> 
  </ol> </li> 
</ol> 
<h2 style="margin-left:0; margin-right:0; text-align:start">文本处理</h2> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li><code>gstr</code> 
  <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
   <li>改进<code>WordWrap</code>方法，使得对<code>Unicode</code>特别是中文换行更加友好。</li> 
   <li>修复<code>RepliceI</code>忽略大小写字符串替换在特定场景下的问题。</li> 
  </ol> </li> 
</ol> 
<h2 style="margin-left:0; margin-right:0; text-align:start">错误处理</h2> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li><code>gerror</code> 
  <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
   <li>新增<code>Unwrap</code>方法（同<code>Next</code>方法），用以支持<code>Golang</code>新版本的<code>Unwrap</code>错误接口。</li> 
   <li>新增<code>Equal</code>方法，用于判断两个错误是否相等：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D49770752" target="_blank">错误处理-错误比较</a></li> 
   <li>新增<code>Is</code>方法，用于支持<code>Golang</code>新版本的<code>Is</code>错误接口：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D49770752" target="_blank">错误处理-错误比较</a></li> 
  </ol> </li> 
</ol> 
<h2 style="margin-left:0; margin-right:0; text-align:start">工具方法</h2> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li><code>gconv</code> 
  <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
   <li>去掉整型转换时对八进制字符串的支持。</li> 
   <li>改进内部实现逻辑，提高可读性保障可维护性。</li> 
  </ol> </li> 
 <li><code>gutil</code> 
  <ol style="list-style-type:lower-alpha; margin-left:0; margin-right:0"> 
   <li>新增<code>gutil.Copy</code>方法，用于深度拷贝指定内容。</li> 
   <li>改进<code>gutil.Dump</code>方法。</li> 
  </ol> </li> 
</ol> 
<h1 style="margin-left:0; margin-right:0; text-align:start">开发工具</h1> 
<p style="color:#172b4d; margin-left:0; margin-right:0; text-align:start">相对于主库稳定的代码组件，CLI开发工具在近期的版本发布有一些非兼容更新，各位在升级时注意发布记录，细节请查看源码调整。</p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>改进<code>build</code>命令，支持指定<code>pack</code>代码文件的生成目录，参数有个别调整。</li> 
 <li>改进<code>docker</code>命令，支持多个<code>docker tag</code>的重命名及仓库自动推送。</li> 
 <li>改进<code>gen dao</code>命令，支持自定义<code>dao/do/entity</code>代码生成目录，不再强制生成到<code>service/internal</code>目录下：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D3673173" target="_blank">数据规范-gen dao</a></li> 
 <li>新增<code>gen service</code>命令，支持自动化地根据<code>logic</code>层级代码，生成<code>service</code>接口代码：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoframe.org%2Fpages%2Fviewpage.action%3FpageId%3D49770772" target="_blank">接口维护-gen service</a></li> 
 <li>修复<code>run</code>命令自定义程序启动参数问题、<code>gofmt/goimports</code>程序路径带空格问题。</li> 
</ol> 
<p> </p>
                                        </div>
                                      
</div>
            