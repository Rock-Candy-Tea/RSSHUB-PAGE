
---
title: 'GoEdge CDN v0.3.7 发布，包含大量优化'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-c403a74867da06b368dc6aea1c3a1ec9ed0.png'
author: 开源中国
comments: false
date: Mon, 20 Dec 2021 09:32:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-c403a74867da06b368dc6aea1c3a1ec9ed0.png'
---

<div>   
<div class="content">
                                                                                            <p><strong style="color:#333333">GoEdge</strong><span style="background-color:#ffffff; color:#333333">是一款可以帮你快速构建 CDN & WAF 平台的工具，支持HTTP、HTTPS、TCP、TLS、UDP、Proxy Protocol、IPv6、WAF等特性。</span></p> 
<p style="color:rgba(0, 0, 0, 0.87); margin-left:0; margin-right:0; text-align:start"><img alt height="352" src="https://oscimg.oschina.net/oscnet/up-c403a74867da06b368dc6aea1c3a1ec9ed0.png" width="600" referrerpolicy="no-referrer"></p> 
<p style="color:rgba(0, 0, 0, 0.87); margin-left:0; margin-right:0; text-align:start">v0.3.7 包含大量细节优化。</p> 
<h3 style="text-align:start">EdgeAdmin</h3> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0">功能增强：</p> 
  <ul> 
   <li>可以批量设置服务错误日志为已修复</li> 
   <li>服务 
    <ul> 
     <li>增加请求最大尺寸、服务连接数、单IP连接数等请求限制</li> 
     <li>路由规则增加专属域名设置</li> 
     <li>HTTP Header：实现请求方法、域名、状态码等限制，实现Header值替换功能</li> 
    </ul> </li> 
   <li>访问日志 
    <ul> 
     <li>访问日志增加是否记录499选项</li> 
     <li>访问日志实现记录和显示requestBody</li> 
     <li>访问日志增加单页显示条数选择</li> 
     <li>实现访问日志队列，可以设置写入队列长度、速度等</li> 
     <li>访问日志查询过慢的时候，显示提示建议增加新的日志节点</li> 
    </ul> </li> 
   <li>缓存 
    <ul> 
     <li>缓存配置增加Age、Expires Header配置</li> 
     <li>缓存配置增加支持Cache-Control: max-age选项</li> 
     <li>缓存默认key改为$&#123;scheme&#125;://$&#123;host&#125;$&#123;requestPath&#125;$&#123;isArgs&#125;$&#123;args&#125;，修改起来更加灵活</li> 
     <li>缓存支持请求方法设置</li> 
    </ul> </li> 
   <li>WAF 
    <ul> 
     <li>WAF规则集中增加是否忽略局域网IP选项</li> 
     <li>WAF自动生成的黑名单不再即使同步，防止影响配置同步</li> 
     <li>IPBox把IP加入黑名单可以选择过期时间/可以从已经添加的名单中删除/已经添加的名单中显示过期时间</li> 
     <li>修复公共黑名单/白名单无法搜索的Bug</li> 
     <li>可以修改分组代号</li> 
     <li>导入导出优化：导入时可以根据名称合并/导出时可以选择导出停用的分组</li> 
     <li>WAF添加规则：调整界面/增加正则表达式测试功能</li> 
    </ul> </li> 
   <li>请求ID： 
    <ul> 
     <li>访问日志弹窗中加入请求ID</li> 
     <li>多个提示页面增加请求ID</li> 
     <li>支持使用请求ID搜索访问日志</li> 
    </ul> </li> 
   <li>边缘节点 
    <ul> 
     <li>增加批量增加节点IP接口</li> 
     <li>SSH认证支持sudo</li> 
     <li>支持设置单节点最大线程数、单节点TCP最大连接数</li> 
    </ul> </li> 
   <li>请求条件增加不区分大小写选项</li> 
   <li>请求条件增加多个内置组合条件</li> 
   <li>生产环境下components.js不再动态生成，改成编译时生成静态文件</li> 
   <li>增加在线检查最新版本功能</li> 
   <li>界面优化 
    <ul> 
     <li>优化服务设置界面顶部导航，显示当前设置项目</li> 
     <li>将部分teaos.cn域名内容修改为goedge.cn</li> 
     <li>图表尺寸高度调小，以便能在同一屏幕内显示更多的内容</li> 
    </ul> </li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0">Bug修复：</p> 
  <ul> 
   <li>修复HSTS无法设置有效期的Bug</li> 
  </ul> </li> 
</ul> 
<h3 style="text-align:start">EdgeAPI</h3> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0">功能增强：</p> 
  <ul> 
   <li>节点任务查询时增加排除的任务类型</li> 
   <li>多个API支持查询用户查询</li> 
   <li>健康检查不再使用密钥加密Header，防止节点无法正常解码</li> 
   <li>用户账单增加多个API</li> 
   <li>增加或者缩短多个数据清理任务</li> 
   <li>增加GRPC最大能接收的消息尺寸为128M</li> 
   <li>自动将API节点的IP加入到边缘节点的白名单，防止误封</li> 
   <li>增加edge-api goman命令，可以查看当前运行的一部分goroutine</li> 
   <li>优化ip2region查询代码，避免在初始化时使用大量内存</li> 
   <li>节点因阈值切换到备用IP时保持在线状态，防止因切换IP而导致节点上所有IP均不可用</li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0">Bug修复：</p> 
  <ul> 
   <li>修复新启动节点时获取不到最新配置的Bug</li> 
   <li>修复通过IP查询IP名单时没有过滤已删除IP的Bug</li> 
  </ul> </li> 
</ul> 
<h3 style="text-align:start">EdgeNode</h3> 
<ul> 
 <li> <p style="margin-left:0; margin-right:0">功能增强：</p> 
  <ul> 
   <li>优化ip2region查询代码，避免在初始化时使用大量内存</li> 
   <li>端口提示被占用时提示语中加入当前占用端口的进程名</li> 
   <li>可以上报服务相关配置错误</li> 
   <li>因WAF规则拦截而关闭连接时，不记录499</li> 
   <li>增加$&#123;cache.age&#125;变量</li> 
   <li>增加$&#123;cache.key&#125;变量</li> 
   <li>增加$&#123;requestId&#125;变量</li> 
   <li>增加$&#123;isArgs&#125;请求变量</li> 
   <li>URL跳转时检查前后跳转的URL是否一致，防止无限跳转</li> 
   <li>优化验证码页面</li> 
   <li>多个提示页面增加请求ID、增加变量支持</li> 
   <li>将RPC连接错误级别从error改为warning</li> 
   <li>降低ttlcache最大内存增量</li> 
   <li>WAF忽略客户端断开连接错误</li> 
   <li>回源主机名为“跟随源站”时，获得的源站主机名去除常规端口80和443</li> 
   <li>缓存增加UPDATING和STALE状态</li> 
   <li>启动时增加sid设置，以便于让sudo命令启动的进程可以在后台常驻</li> 
   <li>在开发环境下打印Go语言内部HTTP调试信息</li> 
   <li>优化系统goroutine使用，减少goroutine数量，增加goman命令查看goroutine数量指令</li> 
   <li>使用空struct&#123;&#125;代替bool节约内存</li> 
   <li>在URL跳转、重写规则跳转、自动跳转到HTTPS等处增加响应Header</li> 
   <li>自动过期和批量清除缓存时延时删除缓存文件，防止客户端在访问缓存过程中被删</li> 
   <li>TLS连接增加握手超时检查，防止空连接长时间无法关闭</li> 
   <li>增加edge-node conns命令打印当前总连接数</li> 
   <li>当使用quit退出进程时，同时也禁用缓存策略，防止多个进程写入缓存冲突</li> 
   <li>优化SSL证书查找速度</li> 
  </ul> </li> 
 <li> <p style="margin-left:0; margin-right:0">Bug修复：</p> 
  <ul> 
   <li>修复WAF中scheme checkpoint值为空的问题</li> 
   <li>修复TOA管理中可能出现的panic错误</li> 
   <li>上传访问日志时如果出现非法UTF-8（string field contains invalid UTF-8）问题，则重新处理后再次提交</li> 
   <li>修复WAF OnAction在并发时无法准确调用请求动作的Bug</li> 
   <li>修复当源站错误数过多而导致无源站可用的Bug</li> 
   <li>修复源站主动关闭连接时无法缓存内容的Bug</li> 
  </ul> </li> 
</ul> 
<p><span style="background-color:#ffffff; color:#24292f">下载：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdownloads" target="_blank">https://goedge.cn/downloads</a><br> <span style="background-color:#ffffff; color:#24292f">文档：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgoedge.cn%2Fdocs" target="_blank">https://goedge.cn/docs</a></p>
                                        </div>
                                      
</div>
            