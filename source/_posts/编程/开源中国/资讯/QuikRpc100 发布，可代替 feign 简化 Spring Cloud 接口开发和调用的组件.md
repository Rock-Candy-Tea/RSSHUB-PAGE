
---
title: 'QuikRpc1.0.0 发布，可代替 feign 简化 Spring Cloud 接口开发和调用的组件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2234'
author: 开源中国
comments: false
date: Wed, 22 Sep 2021 12:53:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2234'
---

<div>   
<div class="content">
                                                                                            <div> 
 <div> 
  <h1 style="margin-left:0; margin-right:0; text-align:left">介绍</h1> 
  <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">随着微服务兴起，越来越多的项目使用微服务架构进行开发，SpringCloud是最流行的微服务开发组件集之一。但是和dubbo相比，使用SpringCloud 开发和调用接口 要麻烦很多，很多开发人员都希望能简化SpringCloud 开发和调用过程和步骤，QuikRpc  就是用来简化SpringCloud 开发和调用过程的组件，使用QuikRpc 服务开发者只需要在service接口用注解标记哪个方法对外开放，服务使用者只需要像使用本地spring bean一样把service @Autowired进来即可，大大简化了spring cloud 服务接口开发和调用步骤，有效的降低了spring cloud的使用和学习成本。</p> 
  <div> 
   <h1 style="margin-left:0; margin-right:0; text-align:left">对比</h1> 
   <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>1 、用原生方式完成一个springcloud微服务接口开发与调用过程：</strong></p> 
   <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">     A、写一个service接口，在service实现类中实现业务</p> 
   <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">     B、写一个controller，调用service，完成接口暴漏</p> 
   <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">     C、写一个feign 接口，用于包装controller暴漏出来的接口</p> 
   <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">     D、消费者通过feign代理接口来调用 A步骤写的service代码</p> 
   <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>2、用</strong>QuikRpc<span> </span><strong>完成一个springcloud微服务接口开发与调用过程：</strong></p> 
   <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>   </strong><span> </span>A、写一个service接口，在接口上加上注解，在暴漏的方法上加上注解，在service实现类实现业务</p> 
   <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">    B、消费者@Autowired service到自己代码中完成调用。</p> 
   <div> 
    <h4 style="margin-left:0; margin-right:0; text-align:left">食用步骤</h4> 
    <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">1、给启动类所在项目添加POM依赖</p> 
    <div style="text-align:left"> 
     <div> 
      <pre style="margin-left:0; margin-right:0"><span> <span style="color:#000080"><span style="color:#333333"><<span style="color:#22863a">dependency</span>></span></span></span>
<span>    <span style="color:#000080"><span style="color:#333333"><<span style="color:#22863a">groupId</span>></span></span>com.fhs-opensource<span style="color:#000080"><span style="color:#333333"></<span style="color:#22863a">groupId</span>></span></span></span>
<span>    <span style="color:#000080"><span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span></span>easy-cloud-spring-boot-starter<span style="color:#000080"><span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span></span></span>
<span>    <span style="color:#000080"><span style="color:#333333"><<span style="color:#22863a">version</span>></span></span>1.0.0<span style="color:#000080"><span style="color:#333333"></<span style="color:#22863a">version</span>></span></span></span>
<span> <span style="color:#000080"><span style="color:#333333"></<span style="color:#22863a">dependency</span>></span></span></span></pre> 
     </div> 
    </div> 
    <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">2 需要将依赖的POJO和service放到单独的一个模块中，让服务提供者和消费者都可依赖到，service 接口代码示例如下：</p> 
    <div style="text-align:left"> 
     <div> 
      <pre style="margin-left:0; margin-right:0"><span><span><span style="color:#6a737d">@CloudApi</span></span><span>(</span><span>serviceName</span><span>=</span><span style="color:#dd2200"><span style="color:#032f62">"producer"</span></span><span>)</span><span style="color:#888888"><span style="color:#6a737d">//producer 是服务提供者的服务名称</span></span></span>
<span><strong><span style="color:#d73a49">public</span></strong> <strong><span><span style="color:#d73a49">interface</span></span></strong><span> </span><strong style="color:#445588"><span><span style="color:#6f42c1">UserService</span></span></strong><span> </span><span>&#123;</span></span>

<span>    <span><span style="color:#6a737d">@CloudMethod</span></span>  <span style="color:#888888"><span style="color:#6a737d">//加此注解意思是此方法提供给其他微服务调用</span></span></span>
<span>    <strong style="color:#445588"><span>List</span></strong><span><span><</span></span><strong style="color:#445588"><span>UserDto</span></strong><span><span>></span></span><span> </span><strong style="color:#990000"><span><span style="color:#6f42c1">listByIds</span></span></strong><span><span><span>(</span></span></span><strong style="color:#445588"><span><span>String</span></span></strong><span><span><span>[]</span></span></span><span><span> </span></span><span><span><span>ids</span></span></span><span><span><span>)</span></span>;</span></span>
<span><span>&#125;</span></span></pre> 
     </div> 
    </div> 
    <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">此模块需要依赖：</p> 
    <div style="text-align:left"> 
     <div> 
      <pre style="margin-left:0; margin-right:0"><span> <span style="color:#000080"><span style="color:#333333"><<span style="color:#22863a">dependency</span>></span></span></span>
<span>     <span style="color:#000080"><span style="color:#333333"><<span style="color:#22863a">groupId</span>></span></span>com.fhs-opensource<span style="color:#000080"><span style="color:#333333"></<span style="color:#22863a">groupId</span>></span></span></span>
<span>     <span style="color:#000080"><span style="color:#333333"><<span style="color:#22863a">artifactId</span>></span></span>easy_cloud_anno<span style="color:#000080"><span style="color:#333333"></<span style="color:#22863a">artifactId</span>></span></span></span>
<span>     <span style="color:#000080"><span style="color:#333333"><<span style="color:#22863a">version</span>></span></span>1.0.0<span style="color:#000080"><span style="color:#333333"></<span style="color:#22863a">version</span>></span></span></span>
<span> <span style="color:#000080"><span style="color:#333333"></<span style="color:#22863a">dependency</span>></span></span></span></pre> 
     </div> 
    </div> 
    <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">3 消费者 和提供者启动类添加 @EnableEasyCloud(basePackages = "com.fhs") 其中com.fhs 指的是service类的包，可以多个</p> 
    <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">4 在消费者需要调用userservice的地方直接@Autowired 即可</p> 
    <div style="text-align:left"> 
     <div> 
      <pre style="margin-left:0; margin-right:0"><span> <span><span style="color:#032f62">@Autowired</span></span></span>
<span> <strong>private</strong> <strong style="color:#445588">UserService</strong> <span>userService</span><span>;</span></span></pre> 
     </div> 
    </div> 
    <h4 style="margin-left:0; margin-right:0; text-align:left">需要注意的点-一定要看完</h4> 
    <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">1、如果参数或者返回值有泛型的情况下，或者嵌套层级过深，可能会有问题，这是Java编译机制和fastjson的问题<br> 2、如果参数类型定义了map,反序列化后value的类型可能和你原来的类型不同，比如date 会变成日期字符串，所以map vallue只推荐使用字符串，数字，boolean类型传参，当然尽量不要用map  <br> 3、本插件消费者是通过restTemplate调用服务端接口，服务端接口路径为：/easyCloud/proxy/&#123;serviceClass&#125;/&#123;methodName&#125; 如果项目中用到了权限插件请放行<br> 4、如果服务间调用希望加权限认证，可以自定义一个resttemplate，配合spring拦截器或者过滤器拦截/easyCloud/proxy开头请求实现认证</p> 
   </div> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            