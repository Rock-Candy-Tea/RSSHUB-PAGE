
---
title: 'Spring HATEOAS 1.4 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2212'
author: 开源中国
comments: false
date: Tue, 23 Nov 2021 06:45:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2212'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">Spring HATEOAS 1.4 现已发布。Spring HATEOAS 是一个用于实现 REST Web 服务的开发库，它提供了一些 API，以便在使用 Spring，特别是 Spring MVC 时可以轻松创建遵循 HATEOAS 原则的 REST 表述，其试图解决的核心问题是链接的创建和表述组装。</span></p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>HAL FORMS 属性描述中不支持自定义类型</li> 
 <li>将请求参数模板变量添加到已经包含一个生成无效模板的 URI</li> 
 <li>在 JsonPathLinksDiscoverer 中使用 Links.collector()</li> 
 <li>在 LinkDiscoverer.findLinkWithRel(...) 中修复 Javadoc</li> 
 <li>当内容是空 bean 并且 ObjectMapper 配置为不会在这些 bean 上失败时，序列化 EntityModel 出错</li> 
 <li>HAL FORMS 目标只能包含 URL</li> 
 <li>修复文档中的 HalModelBuilder 示例</li> 
 <li>重新公开 AnnotationMappingDiscoverer</li> 
 <li>如果没有注册媒体类型配置，则防止 IndexOutOfBoundException</li> 
 <li>在 MethodLinkBuilderFactory.linkTo(...) 方法中如何处理参数的定义不精确</li> 
 <li>将兼容性版本升级到 JDK 17</li> 
 <li>DummyInvocationUtils.methodOn(...) 在 JDK 17 上返回 Object 的方法失败</li> 
 <li>指向返回 Mono 的控制器方法时调用日志输出</li> 
 <li>避免在 Link.valueOf(...) 中创建多余的对象</li> 
 <li>HAL-FORMS 可供性方法是小写而不是大写</li> 
 <li>删除 Affordances 中的弃用</li> 
 <li>Link 属性的可空性声明错误</li> 
 <li>自定义转换器不用于枚举列表查询参数</li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2021%2F11%2F22%2Fspring-hateoas-1-4-released" target="_blank">更新公告</a>。</p> 
<p> </p>
                                        </div>
                                      
</div>
            