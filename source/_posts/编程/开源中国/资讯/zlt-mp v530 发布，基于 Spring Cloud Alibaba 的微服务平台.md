
---
title: 'zlt-mp v5.3.0 发布，基于 Spring Cloud Alibaba 的微服务平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-a3ed4ccd0987d8434fe11056644a41c074a.png'
author: 开源中国
comments: false
date: Mon, 09 May 2022 08:54:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-a3ed4ccd0987d8434fe11056644a41c074a.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-a3ed4ccd0987d8434fe11056644a41c074a.png" referrerpolicy="no-referrer"></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">功能介绍</h1> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-2ba2d06a6a1d728c5fd8af4e3cce1810d54.png" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">更新内容</h2> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><span>特性 / 增强</span></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p>增加服务版本号隔离</p> </li> 
 <li> <p>优化授权中心redis-token内存占用</p> </li> 
 <li> <p>适配mybatis-plus拦截器新配置方式</p> </li> 
 <li> <p>升级spring-boot到2.5.13</p> </li> 
 <li> <p>升级spring-cloud到2020.0.5</p> </li> 
 <li> <p>升级spring-boot-admin到2.5.6</p> </li> 
 <li> <p>升级mybatis-plus到3.5.1<strong style="color:#ffffff">内容说明</strong></p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><span>一、</span>服务版本号隔离</h3> 
<h4 style="text-align:left"><span>1.1. 适用场景</span></h4> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">这个是用于<strong style="color:black">解决</strong>微服务<strong style="color:black">服务冲突乱窜</strong>的问题；</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">指的是在开发环境过程中，开发人员可能只会在本地启动自己开发的服务进行调试，而其他服务则使用服务器上的；这样就可能会在注册中心中出现同一个服务同时存在多个不同版本的实例（如下图所示的<code>业务服务B</code>）</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-f888e194a3ecb864eca5068d19c56029558.png" referrerpolicy="no-referrer"></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">这样如果<span> </span><code>开发A</code><span> </span>本来想要调试自己本地服务的时候，网关调用业务服务B时的请求则有可能会跳转到其他人的实例上，如服务器上的或者开发B的实例。</p> 
<h4 style="text-align:left"><span>1.2. 隔离逻辑</span></h4> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">本次更新主要是基于 Spring Cloud 的负载均衡组件<span> </span><code>LoadBalancer</code>，通过<span> </span><code>版本号</code><span> </span>来实现<span> </span><code>自定义负载均衡</code><span> </span>规则，解决这个服务乱窜问题；以上图为例，主要实例选择逻辑如下：</p> 
<ol style="margin-left:0; margin-right:0"> 
 <li> <p><strong style="color:black">普通用户</strong>访问服务器上的页面时，请求的所有路由只调用<span> </span><code>服务器实例</code></p> </li> 
 <li> <p><strong style="color:black">开发A</strong>访问时，请求的所有路由优先调用<span> </span><code>开发A本机实例</code><span> </span>如果没有则调用<span> </span><code>服务器实例</code></p> </li> 
 <li> <p><strong style="color:black">开发B</strong>访问时同上，请求的所有路由优先调用<span> </span><code>开发B本机实例</code><span> </span>如果没有则调用<span> </span><code>服务器实例</code></p> </li> 
</ol> 
<h4 style="text-align:left"><span>1.3. 使用说明</span></h4> 
<p><span>1.3.1. 开关配置</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">通过以下配置来设置是否开启<span> </span><code>版本隔离</code><span> </span>功能，默认为<span> </span><code>false</code></p> 
<pre style="text-align:left"><code><span style="color:#d19a66">zlt:</span>
  <span style="color:#d19a66">loadbalance:</span>
    <span style="color:#d19a66">isolation:</span>
      <span style="color:#d19a66">enabled:</span> <span style="color:#56b6c2">true</span>
</code></pre> 
<p><span>1.3.2. 服务版本配置</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">使用注册中心的元数据(metadata)来区分版本。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">主流的注册中心都带有元数据管理，以Nacos为例，可以在 Spring Cloud 的配置中通过以下两种方式添加服务的版本号：</p> 
<pre style="text-align:left"><code><span style="color:#d19a66">spring:</span>
  <span style="color:#d19a66">cloud:</span>
    <span style="color:#d19a66">nacos:</span>
      <span style="color:#d19a66">discovery:</span>
        <span style="color:#d19a66">metadata:</span>
          <span style="color:#d19a66">version:</span> <span style="color:#98c379">zlt</span>
</code></pre> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">或者</p> 
<pre style="text-align:left"><code><span style="color:#d19a66">zlt:</span>
  <span style="color:#d19a66">loadbalance:</span>
    <span style="color:#d19a66">version:</span> <span style="color:#98c379">zlt</span>
</code></pre> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">启动服务后元数据就会注册上去，如下图所示：</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-99a55dacddd16c46845aaf011df08c993e1.png" referrerpolicy="no-referrer"></p> 
<p><span>1.3.3. 版本入参</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">开发人员可以通过<span> </span><code>postman</code><span> </span>工具调用接口的时候在<span> </span><code>header参数</code><span> </span>中添加自己的<span> </span><code>版本号</code>：</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-134b225eb2439b53930616e91bf8aa0d916.png" referrerpolicy="no-referrer"></p> 
<h3 style="margin-left:0; margin-right:0; text-align:left"><span>二、</span>优化授权中心redis-token内存占用</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">使用 redis-token 时，每授权一个 token 之后 security 会在 redis 中生成<span> </span><code>client_id_to_access</code><span> </span>和<span> </span><code>uname_to_access</code><span> </span>两个队列，分别用于存放某个 client_id 下的所有 access_token 以及某个 username 下的所有 access_token。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">由于集合无法单独对元素进行过期时间设置，所以理论上如果一直有用户授权，会一直刷新集合的过期时间，导致内容无限扩大，存在<span> </span><code>内存溢出</code><span> </span>的风险。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left">本版本的解决方式：增加一个 redis 的销毁监听器，专门负责清除这两个集合下的过期数据。</p> 
<h3 style="text-align:left"><span>三、适配 mybatis-plus 拦截器新配置方式</span></h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#000000">mybatis-plus 3.4 版本后分页拦截器<span> </span></span><code>PaginationInterceptor</code><span style="background-color:#ffffff; color:#000000"><span> </span>被弃用，替换成<span> </span></span><code>MybatisPlusInterceptor</code></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left"><strong>项目地址</strong></h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Gitee 地址： <a href="https://gitee.com/zlt2000/microservices-platform">https://gitee.com/zlt2000/microservices-platform</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Github 地址： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzlt2000%2Fmicroservices-platform" target="_blank">https://github.com/zlt2000/microservices-platform</a></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">项目文档</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fzlt2000%2Fmicroservices-platform%2F919417" target="_blank">https://www.kancloud.cn/zlt2000/microservices-platform/919417</a></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">项目更新日志</h2> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Fzlt2000%2Fmicroservices-platform%2F936235" target="_blank">https://www.kancloud.cn/zlt2000/microservices-platform/9362</a></p>
                                        </div>
                                      
</div>
            