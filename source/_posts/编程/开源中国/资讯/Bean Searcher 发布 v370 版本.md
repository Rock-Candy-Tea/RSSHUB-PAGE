
---
title: 'Bean Searcher 发布 v3.7.0 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8254'
author: 开源中国
comments: false
date: Fri, 08 Jul 2022 13:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8254'
---

<div>   
<div class="content">
                                                                                            <h3 style="margin-left:0em; margin-right:0em; text-align:start">简介</h3> 
<div> 
 <div>
  很多系统都有列表检索（如：订单管理，用户管理）这样的需求，而每一个列表页所需展示的数据往往会横跨多张数据库表（比如订单管理页表格里的订单号列来自订单表，用户名列来自用户表），此时我们的后端所建的 域类（或实体类，与数据库表想关联的那个类）与页面所需展示的数据并不能形成一一对应关系。
 </div>   
 <div>
  因此，VO（View Object） 产生了。它介于页面数据与域类之间，页面展示的数据不再需要与后端的域类一一对应，而只需要与 VO 一一对应就可以了，而 VO 也不再需要与数据表做映射，业务代码里拼装就可以了。但此时，后端的逻辑又复杂了一点，因为我们不仅需要解析前端传来的参数，还要处理 域类（或者复杂的 SQL 查询语句）与 VO 之间的转换关系。而 Bean Searcher 认为，VO 不再需要与域类扯上关系，一个 VO 既可以与页面数据一一对应，又可以直接映射到数据库里的多张数据表（域类不同，它只映射到一张表），而这种新的 VO 称为 Search Bean。
 </div>   
 <div>
  在 Search Bean 出现之前，前端传来的检索条件都是需要业务代码解析处理的（因为普通的 VO 无法与数据库直接映射），并且查询结果也需要再做一次 VO 转换。而 Search Bean 出现之后，条件可以用 Search Bean 里的字段和参数直接表达，并且直接映射成数据库的查询语句。
 </div>   
 <div>
  所以，后端检索接口里的代码只需要收集页面的检索参数即可，余下的就全部交给 Bean Searcher 处理了，并且它返回的 SearchBean 就是前端所需的 VO 对象，也不需要再多做转换了。
 </div>   
 <div>
  而这，就是 Bean Searcher 之所以能极大提高研发生产力的原因！
 </div> 
</div> 
<p> </p> 
<h3 style="margin-left:0em; margin-right:0em; text-align:start">v3.7.0 更新内容</h3> 
<h3 style="margin-left:0em; margin-right:0em; text-align:start">✨ Features</h3> 
<ul> 
 <li>Bean Searcher 
  <ul> 
   <li>新增<span> </span><code>SqlServerDialect</code><span> </span>方言实现，支持 SqlServer 2012+</li> 
   <li>新增<span> </span><code>OrLike</code><span> </span>运算符，参见：<a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2Fejlchina%2Fbean-searcher%2Fissues%2F38" target="_blank">https://github.com/ejlchina/bean-searcher/issues/38</a></li> 
   <li>增强<span> </span><code>SqlExecutor</code>：新增<span> </span><code>SlowListener</code><span> </span>接口，可让用户在代码中监听慢 SQL</li> 
   <li>增强<span> </span><code>DefaultDbMapping</code>：新增<span> </span><code>underlineCase</code><span> </span>属性，可配置自动映射时是否开启<span> </span><code>驼峰->下划线</code><span> </span>的风格转换</li> 
   <li>增强<span> </span><code>Dialect</code>：新增<span> </span><code>hasILike()</code><span> </span>方法，当忽略大小写查询时，可利用数据库的<span> </span><code>ilike</code><span> </span>关键字提升查询性能</li> 
   <li>增强<span> </span><code>EnumFieldConvertor</code>：支持<span> </span><code>整型</code><span> </span>转换为枚举（按枚举序号转换）</li> 
   <li>增强<span> </span><code>EnumFieldConvertor</code>：新增<span> </span><code>failOnError</code><span> </span>属性, 可配置在遇到非法值无法转换时是否报错，默认<span> </span><code>true</code></li> 
   <li>增强<span> </span><code>EnumFieldConvertor</code>：新增<span> </span><code>ignoreCase</code><span> </span>属性, 可配置字符串值匹配枚举时是否忽略大小写，默认<span> </span><code>false</code></li> 
   <li>优化<span> </span><code>SQL 日志</code>：普通 SQL 显示执行耗时，慢 SQL 日志级别调整为<span> </span><code>WARN</code><span> </span>并输出关联的实体类</li> 
   <li>优化<span> </span><code>DefaultSqlExecutor</code>，当执行 count sql 且查询结果为<span> </span><code>0</code><span> </span>时，则不再执行 list sql</li> 
   <li>优化<span> </span><code>参数构建器</code><span> </span>的<span> </span><code>page(..)</code><span> </span>与<span> </span><code>limit(..)</code><span> </span>方法，它们起始页码也受页码配置约束（<strong>破坏性更新</strong>）</li> 
   <li>优化<span> </span><code>Dialect</code>：为<span> </span><code>toUpperCase(..)</code><span> </span>添加默认实现，用户自定义方言时，只有一个<span> </span><code>forPaginate(..)</code><span> </span>方法必须实现</li> 
   <li>优化<span> </span><code>DefaultParamResolver</code>：默认使用<span> </span><code>page</code><span> </span>分页参数提取器</li> 
   <li>优化<span> </span><code>检索器</code><span> </span>的 count 与 sum 检索, 当无记录统计时，返回<span> </span><code>0</code><span> </span>而非<span> </span><code>null</code>, 并再次优化检索性能</li> 
   <li>重构<span> </span><code>FetchType#ALL</code><span> </span>重命名为<span> </span><code>FetchType#DEFAULT</code></li> 
  </ul> </li> 
 <li>Bean Searcher Boot Starter 
  <ul> 
   <li>新增<span> </span><code>bean-searcher.sql.slow-sql-threshold</code><span> </span>配置键，可配置慢 SQL 阈值（单位毫秒），默认为<span> </span><code>500</code></li> 
   <li>新增<span> </span><code>bean-searcher.sql.default-mapping.underline-case</code><span> </span>配置键，可配置自动映射时是否开始 驼峰->下划线 的风格转换，默认为<span> </span><code>true</code></li> 
   <li>新增<span> </span><code>bean-searcher.field-convertor.enum-fail-on-error</code><span> </span>配置键，可配置在遇到非法值无法转换时是否报错，默认<span> </span><code>true</code></li> 
   <li>新增<span> </span><code>bean-searcher.field-convertor.enum-ignore-case</code><span> </span>配置键，可配置字符串值匹配枚举时是否忽略大小写，默认<span> </span><code>false</code></li> 
   <li>支持 用户配置一个<span> </span><code>SqlExecutor.SlowListener</code><span> </span>的 Spring Bean 来监听慢 SQL</li> 
   <li>支持 用户配置<span> </span><code>bean-searcher.sql.dialect</code><span> </span>为<span> </span><code>SqlServer</code><span> </span>来使用 Sql Server 方言</li> 
   <li>升级<span> </span><code>spring-boot</code><span> </span>-><span> </span><code>v2.6.8</code></li> 
  </ul> </li> 
</ul> 
<h4 style="margin-left:0; margin-right:0; text-align:left">你还在问 Bean Searcher 是什么？</h4> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>快来看它如何让你的效率提升 100 倍：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuejin.cn%2Fpost%2F7027733039299952676" target="_blank">https://juejin.cn/post/7027733039299952676</a></li> 
 <li>快来看它为何与被 MybatisPlus 直接的区别：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjuejin.cn%2Fpost%2F7092411551507808264" target="_blank">https://juejin.cn/post/7092411551507808264</a></li> 
 <li>超详细文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbs.zhxu.cn%2F" target="_blank">https://bs.zhxu.cn/</a></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">如果觉得不错点个 STAR 吧 ^_^：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>Github:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Ftroyzhxu%2Fbean-searcher" target="_blank">https://github.com/troyzhxu/bean-searcher</a></li> 
 <li>Gitee:   <a href="https://gitee.com/troyzhxu/bean-searcher">https://gitee.com/troyzhxu/bean-searcher</a></li> 
</ul> 
<p> </p> 
<p> </p>
                                        </div>
                                      
</div>
            