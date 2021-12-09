
---
title: 'Bean Searcher 发布 v3.2.0 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=865'
author: 开源中国
comments: false
date: Thu, 09 Dec 2021 13:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=865'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="margin-left:0em; margin-right:0em; text-align:start">Bean Searcher 发布 v3.2.0 版本，，具体更新内容如下：</p> 
<h3 style="margin-left:0em; margin-right:0em; text-align:start">✨ Features</h3> 
<ul> 
 <li><strong>Bean Searcher</strong> 
  <ul> 
   <li>重构<span> </span><code>FieldConvertor</code>：移除冗余参数<span> </span><code>targetType</code></li> 
   <li>新增<span> </span><code>EnumFieldConvertor</code>：用来做枚举字段转换</li> 
   <li>实体类 SearchBean 支持继承（可继承 @SearchBean 注解与映射字段）</li> 
   <li>注解<span> </span><code>@SearchBean</code><span> </span>新增<span> </span><code>inheritType</code><span> </span>属性，可控制继承规则</li> 
   <li>类<span> </span><code>DefaultDbMapping</code><span> </span>新增<span> </span><code>defaultInheritType</code><span> </span>属性，可配置实体类的默认继承规则</li> 
   <li>实体类 SearchBean 的映射字段支持省略 Setter 方法</li> 
   <li>新增<span> </span><code>ct</code>（<code>Contain</code>）运算符，用于取代<span> </span><code>in</code>（<code>Include</code>）运算符（使用<span> </span><code>in</code><span> </span>将输出警告）</li> 
  </ul> </li> 
 <li><strong>Bean Searcher Boot Starter</strong> 
  <ul> 
   <li>新增<span> </span><code>bean-searcher.field-convertor.use-enum</code><span> </span>配置项，表示是否自动添加<span> </span><code>EnumFieldConvertor</code>，默认<span> </span><code>true</code></li> 
   <li>新增<span> </span><code>bean-searcher.use-map-searcher</code><span> </span>配置项，表示是否自动创建<span> </span><code>MapSearcher</code><span> </span>检索器，默认<span> </span><code>true</code></li> 
   <li>新增<span> </span><code>bean-searcher.use-bean-searcher</code><span> </span>配置项，表示是否自动创建<span> </span><code>BeanSearcher</code><span> </span>检索器，默认<span> </span><code>true</code></li> 
  </ul> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">🌻 Better</h3> 
<ul> 
 <li><strong>Bean Searcher Boot Starter</strong> 
  <ul> 
   <li>使用 Searcher 类型注入检索器时，默认注入 MapSearcher，不再报错</li> 
   <li>提高兼容性，SpringBoot 最低版本支持到 v1.4+</li> 
  </ul> </li> 
</ul>
                                        </div>
                                      
</div>
            