
---
title: 'SpringBoot整合Swagger管理API接口详解'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=9162'
author: 掘金
comments: false
date: Wed, 12 May 2021 20:12:58 GMT
thumbnail: 'https://picsum.photos/400/300?random=9162'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Swagger概念</h1>
<ul>
<li><strong>传统API文档管理缺点:</strong>
<ul>
<li>对API文档更新时需要通知前端人员,导致文档更新交流不及时,API接口返回信息不明确</li>
<li>缺乏在线接口测试,需要使用额外的API测试工具:postman,SoapUI</li>
<li>接口文档太多,不便于管理</li>
</ul>
</li>
<li><strong>为了解决传统API文档维护问题,方便进行测试后台RESTful接口并实现动态更新,引入Swagger接口工具</strong></li>
<li><strong>Swagger工具优点:</strong>
<ul>
<li><strong>功能丰富:</strong> 支持多种注解,自动生成接口文档界面,支持在界面测试API接口功能</li>
<li><strong>及时更新:</strong> 在开发工程中编写好注释,就可以及时更新API文档</li>
<li><strong>整合简单:</strong> 通过添加pom.xml依赖和简单配置,内嵌于应用中就可同时发布API接口文档界面,不需要部署独立服务</li>
</ul>
</li>
</ul>
<h1 data-id="heading-1">整合Swagger生成API文档</h1>
<h3 data-id="heading-2">SpringBoot项目</h3>
<pre><code class="copyable">1.引入Maven依赖springfox-swagger2和springfox-swagger-ui
2.创建SwaggerConfig类实现Swagger生成API文档逻辑:
生成API文档的扫包范围apis
创建API文档信息ApiInfoBuilder.title("文档标题").description("文档描述").termOfServiceUrl("网址Url").version("版本号").build()
3.在SwaggerConfig类上标注@EnableSwagger2注解开启Swagger功能
4.创建SwaggerController类,在类中创建API接口
5.在SwaggerController类上标注@Api("接口描述")注解作整体接口描述
6.在SwaggerController类里API接口上被标注@ApiOperation("具体接口描述")注解,标注@ApiImplicitParam(name="参数名称",value="参数值",required=true,dataType="参数类型")
7.<注意>:不要在API接口类上标注RequestMapping注解(这样会生成所有请求接口,没有可读性):
 根据相应的请求方式,标注@XxxMapping注解
8.创建启动类启动
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">微服务集群项目</h3>
<ul>
<li>在微服务项目中,Swagger是在每个服务进行集成的,需要将整个微服务中的Swagger进行合成到同一台服务器上:
<ul>
<li><strong>使用Zuul+Swagger实现</strong></li>
<li><strong>使用Nginx+Swagger实现,以项目类型跳转到不同的接口文档</strong></li>
</ul>
</li>
</ul>
<h5 data-id="heading-4">使用Zuul+Swagger实现微服务整个API接口文档的管理</h5>
<ul>
<li>SpringBoot中支持对Swagger进行管理,只需要在Zuul网关中添加对应服务的Swagger文档即可</li>
<li><strong>原理:</strong> 每个独立服务都会集成Swagger自动生成API文档,前端发送服务请求到Zuul网关,Zuul根据请求调用对应服务的Swagger查询API接口</li>
</ul>
<pre><code class="copyable">在各个微服务的类中:
1.在各个微服务中引入SpringBoot支持的Swagger依赖swagger-spring-boot-starter
2.配置文件,可省略不写:
(swagger.base-package=需要生成文档的包名)
3.在微服务的主类上标注@EnableSwagger2Doc文档注解,生成Swagger文档,
4.在微服务的主类上标注@Api("接口描述")注解作整体接口描述
5.在SwaggerController类里API接口上被标注@ApiOperation("具体接口描述")注解
6.标注@ApiImplicitParam(name="参数名称",value="参数值",required=true,dataType="参数类型")

在Zuul网关类中:
1.引入SpringBoot支持的Swagger依赖swagger-spring-boot-starter
2.在Zuul网关类中创建SwaggerAPI文档的配置类逻辑方法
添加文档来源:resource.add(swaggerResource("文档名称","API接口文档","版本号"))
3.在SwaggerAPI文档的配置类上标注@Component将配置类添加到容器中
4.在Zuul网关类上标注@EnableSwagger2Doc开启Swagger文档注解
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            