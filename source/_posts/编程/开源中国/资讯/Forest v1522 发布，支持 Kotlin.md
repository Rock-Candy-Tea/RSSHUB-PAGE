
---
title: 'Forest v1.5.22 发布，支持 Kotlin'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6196'
author: 开源中国
comments: false
date: Wed, 08 Jun 2022 15:23:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6196'
---

<div>   
<div class="content">
                                                                                            <div> 
 <h2>Forest介绍</h2> 
 <p>Forest 是一个开源的 Java HTTP 客户端框架，它能够将 HTTP 的所有请求信息（包括 URL、Header 以及 Body 等信息）绑定到您自定义的 Interface 方法上，能够通过调用本地接口方法的方式发送 HTTP 请求</p> 
 <h2>Forest 如何使用</h2> 
 <p>Forest 不需要您编写具体的 HTTP 调用过程，只需要您定义一个接口，然后通过 Forest 注解将 HTTP 请求的信息添加到接口的方法上即可。请求发送方通过调用您定义的接口便能自动发送请求和接受请求的响应</p> 
 <h2>Forest 的工作原理</h2> 
 <p>Forest 会将您定义好的接口通过动态代理的方式生成一个具体的实现类，然后组织、验证 HTTP 请求信息，绑定动态数据，转换数据形式，SSL 验证签名，调用后端 HTTP API(httpclient 等 API)执行实际请求，等待响应，失败重试，转换响应数据到 Java 类型等脏活累活都由这动态代理的实现类给包了。 请求发送方调用这个接口时，实际上就是在调用这个干脏活累活的实现类</p> 
 <h2>获得奖项</h2> 
 <p>2021 年度 OSC 中国开源项目评选「最受欢迎项目」</p> 
 <p>相关链接: <a href="https://www.oschina.net/project/top_cn_2021">https://www.oschina.net/project/top_cn_2021</a></p> 
 <h2>重点更新内容</h2> 
 <h4>统一连接池</h4> 
 <p>不用再分别定义 OkHttp 和 Httpclient 的连接池了，也不用担心异步请求和同步请求不在同一个连接池的烦恼了</p> 
 <p>本次更新统一连接池，可以通过 max-connections 和 max-route-connections 属性统一管理 OkHttp 和 HttpClient 所有后端的所有请求的最大请求数和最大每路由请求数，同时也包括异步请求在内可以一同进行限制</p> 
 <h4>参数定义返回类型</h4> 
 <p>当接口方法返回的是未知参数的泛型类型时，可以通过新增的<code>@Return</code>参数注解，来标识某个参数为返回类型</p> 
 <pre><code class="language-java">    // 通过 Class 类型参数来标识返回类型
    @Get("/user/info")
    <T> T getGenericClass(@Return Class<T> clazz);

    // 通过 Type 类型参数来标识返回类型
    @Get("/user/info")
    <T> T getGenericType(@Return Type type);

    // 通过 TypeReference 类型参数来标识返回类型
    @Get("/user/info")
    <T> T getGenericTypeReference(@Return TypeReference<T> typeReference);</code></pre> 
 <h2>官网和仓库地址</h2> 
 <blockquote> 
  <h4>官网地址:</h4> 
  <p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fforest.dtflyx.com" target="_blank">http://forest.dtflyx.com</a></p> 
  <h4>Gitee 仓库地址:</h4> 
  <p><a href="https://gitee.com/dromara/forest">https://gitee.com/dromara/forest</a></p> 
  <h4>Github 仓库地址:</h4> 
  <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdromara%2Fforest" target="_blank">https://github.com/dromara/forest</a></p> 
 </blockquote> 
 <h2>本次更新内容</h2> 
 <blockquote> 
  <h4>新增特性</h4> 
  <ul> 
   <li>feat: 统一连接池 (#I5APJA)</li> 
   <li>feat: 可配置异步请求线程池队列大小 (#I5B78X)</li> 
   <li>feat: 支持通过参数定义返回类型 (#I5ANZL)</li> 
  </ul> 
  <h4>修复问题</h4> 
  <ul> 
   <li>fix: spring 5.1 以下的低版本启动失败</li> 
   <li>fix: 请求地址中包含#字符会被转义导致资源找不到 (#I59O7M)</li> 
   <li>fix: 配置BaseRequest的baseURL属性后,完整请求路径中的默认端口号会被覆盖,导致请求失败 (#I4YBDV)</li> 
   <li>fix: 解决当@body注解在对象上标识以后，char&Character类型的属性无法从客户端传输至服务端问题</li> 
   <li>fix: kotlin项目启动异常 (#I50PDZ)</li> 
   <li>fix: RetryWhen重试条件接口在最后一次重试后会执行两次 (#I599BT)</li> 
  </ul> 
  <h4>其它改动</h4> 
  <ul> 
   <li>update: #I5ANZR 删除单元测试代码中的Log4j2依赖</li> 
  </ul> 
  <h4>特别鸣谢</h4> 
  <p>本次更新参与贡献的小伙伴</p> 
  <ul> 
   <li>@xiao4852</li> 
  </ul> 
 </blockquote> 
</div>
                                        </div>
                                      
</div>
            