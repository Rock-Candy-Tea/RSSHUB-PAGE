
---
title: 'smart-http v1.1.9 发布，一款开源 http 服务器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-4543532539095aa42c220d6b39d53ec9ac9.png'
author: 开源中国
comments: false
date: Mon, 01 Nov 2021 09:28:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-4543532539095aa42c220d6b39d53ec9ac9.png'
---

<div>   
<div class="content">
                                                                                            <p>smart-http 是一款采用 smart-socket 研发的可编程式 http 应用微内核，用户可以在此基础上很轻松的开展 Http 或者 WebSocket 相关的服务端/客户端程序开发。</p> 
<p>smart-http 自发布以来获得了很多用户的青睐，通过长期紧密的互动交流，促使该项目从易用性、稳定性和运行性能等方面都得到了显著的进步。</p> 
<p>本次发布的两项新特性：Gzip压缩传输和异步响应式服务，皆来自用户的实际需求，我也在第一时间连夜爆肝予以支持。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:justify"><strong><span style="color:#ff6827">Gzip压缩传输</span></strong></h2> 
<p>通过启用压缩技术可以大大减少网络传输的数据量，提高网页的加载、渲染速度。当然，启用压缩模式会增加些许服务器的性能开销，如果是静态文件可以采用缓存技术消除该影响。</p> 
<p>为了检验压缩传输的效果，我们针对同一份文件分别启用压缩模式和非压缩模式的执行http请求（见下图）。可以看到在没有进行的压缩的时候，传输的字节数高达 8541 个字节，而启用压缩后则骤降至 1557 字节，这样的压缩比还是非常可观的。</p> 
<p><img height="512" src="https://oscimg.oschina.net/oscnet/up-4543532539095aa42c220d6b39d53ec9ac9.png" width="1080" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:justify"><strong><span style="color:#ff6827">异步响应式 </span></strong></h2> 
<p><img height="827" src="https://oscimg.oschina.net/oscnet/up-21dd40ad4f7520e3996c836482253a0f7ff.png" width="1023" referrerpolicy="no-referrer"></p> 
<p>因为 smart-http 使用的是 AIO 模型，无需额外的 IO 线程组，所以一般推荐直接在 smart-http 线程组中处理你的业务逻辑，即同步响应模式。</p> 
<p>但是，假如当前存在与 smart-http 线程组同等数量的客户端都发起大文件上传请求时，会耗尽 smart-http 线程组的全部线程资源，此时再来一个普通的 http 请求将得不到及时响应。针对该场景，可以将请求分发至另外一组线程组（专门处理长耗时任务），待其执行完毕再通过异步响应方式往客户端输出结果。</p> 
<p>启用 smart-http 的异步响应式功能只需重写 HttpServerHandler 的 handle 方法，并于异步线程组中适当的时候调用 future.complete 方法即可（如下图示例）。</p> 
<p><img height="590" src="https://oscimg.oschina.net/oscnet/up-49f149ad0bfa20757864ba8225b114f01ec.png" width="1080" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:justify"><strong><span style="color:#ff6827">更新内容</span></strong></p> 
<ol style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">smart-socket 升级至1.5.13</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">修复 Http/1.0 keep-alive 设置不生效的 bug。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">支持 Gzip 压缩传输。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">支持 Server Name 配置化。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">支持异步响应式服务。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">支持启用debug模式打印 HTTP 请求&响应码流（<span style="color:#ff2941">生产环境慎用，可能存在信息安全隐患</span>）。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">其他代码优化及示例的补充。</p> </li> 
</ol>
                                        </div>
                                      
</div>
            