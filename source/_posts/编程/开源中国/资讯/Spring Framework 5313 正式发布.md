
---
title: 'Spring Framework 5.3.13 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2512'
author: 开源中国
comments: false
date: Fri, 12 Nov 2021 06:53:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2512'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">Spring Framework 5.3.13 现已发布，分别包含 16 项修复和改进。</span></p> 
<p><strong><span style="background-color:#ffffff; color:#333333">主要更新内容</span></strong></p> 
<ul> 
 <li>新功能 
  <ul> 
   <li>在 DefaultClientResponse::createException 中使用ByteArrayDecoder</li> 
   <li>提高 UrlPathHelper.getSanitizedPath() 的效率</li> 
   <li>增加清理多部分临时文件的选项</li> 
   <li>在 CachedExpressionEvaluator 中增加对自定义表达式解析的支持</li> 
   <li>只在没有通过 Quartz 属性指定的情况下使用 LocalDataSourceJobStore</li> 
   <li>引入 TypeFilterUtils 来处理 @ComponentScan.Filter</li> 
   <li>改进 ExtendedEntityManagerCreator.createProxy() 中的映射功能</li> 
  </ul> </li> 
 <li>BUG 修复 
  <ul> 
   <li>当 jar 没有目录条目时缺少静态资源</li> 
   <li>MultipartParser 意外发出有关 "部分标头超出内存使用限"制的 DataBufferLimitException </li> 
   <li>UndertowHeadersAdapter 的 remove() 方法违反了 Map 规定</li> 
   <li>如果字符串文字包含逗号，则 SpEL 可变参数方法调用失败</li> 
  </ul> </li> 
 <li>文档 
  <ul> 
   <li>修复 webflux-webclient.adoc 中的语法</li> 
   <li>如果非必需 bean 不存在，懒惰注释会抛出异常</li> 
   <li>声明 LogFormatUtils limitLength 与 replaceNewlines 参数 </li> 
   <li>PersistenceExceptionTranslationInterceptor 试图实例化原型 PersistenceExceptionTranslator</li> 
  </ul> </li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fblog%2F2021%2F11%2F11%2Fspring-framework-5-3-13-available-now" target="_blank">更新公告</a>。</p> 
<p> </p>
                                        </div>
                                      
</div>
            