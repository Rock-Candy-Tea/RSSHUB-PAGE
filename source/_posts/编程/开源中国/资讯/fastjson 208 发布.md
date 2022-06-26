
---
title: 'fastjson 2.0.8 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9922'
author: 开源中国
comments: false
date: Sun, 26 Jun 2022 07:43:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9922'
---

<div>   
<div class="content">
                                                                                            <h4>FASTJSON 2.0 介绍</h4> 
<p style="color:#24292f; text-align:start"><code>FASTJSON v2</code>是<code>FASTJSON</code>项目的重要升级，目标是为下一个十年提供一个高性能的<code>JSON</code>库。通过同一套<code>API</code>，</p> 
<ul> 
 <li>支持<code>JSON/JSONB</code>两种协议，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falibaba.github.io%2Ffastjson2%2Fjsonpath_cn" target="_blank"><code>JSONPath</code></a><span> </span>是一等公民。</li> 
 <li>支持全量解析和部分解析。</li> 
 <li>支持<code>Java</code>服务端、客户端<code>Android</code>、大数据场景。</li> 
 <li>支持<code>Kotlin</code><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falibaba.github.io%2Ffastjson2%2Fkotlin_cn" target="_blank">https://alibaba.github.io/fastjson2/kotlin_cn</a></li> 
 <li>支持<code>JSON Schema</code><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falibaba.github.io%2Ffastjson2%2Fjson_schema_cn" target="_blank">https://alibaba.github.io/fastjson2/json_schema_cn</a></li> 
 <li>支持<code>Android 8+</code><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frepo1.maven.org%2Fmaven2%2Fcom%2Falibaba%2Ffastjson2%2Ffastjson2%2F2.0.8.android%2F" target="_blank">(2.0.8.android)</a></li> 
 <li>支持<code>Graal Native-Image</code><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frepo1.maven.org%2Fmaven2%2Fcom%2Falibaba%2Ffastjson2%2Ffastjson2%2F2.0.8.graal%2F" target="_blank">(2.0.8.graal)</a></li> 
</ul> 
<h4 style="margin-left:0px; margin-right:0px; text-align:start"><strong>FASTJSON 2.0.8 版本介绍</strong></h4> 
<p style="color:#24292f; text-align:start">经过很多用户在生产环境验证，2.0.8 完全生产可用。对fastjson 1.x也有很好的兼容性，如果不想改代码的同学，可以尝试直接使用2.0.8的兼容包升级，兼容包是计划长期维护的，如果发现问题提issue反馈。</p> 
<h4 style="margin-left:0px; margin-right:0px; text-align:start"><strong>Issues</strong></h4> 
<ol> 
 <li>修改LocalDateTime的缺省序列化格式为"yyyy-MM-dd HH🇲🇲ss"，LocalDate的缺省序列化格式为"yyyy-MM-dd"，LocalTime的缺省序列化格式为"HH🇲🇲ss"，没有特定需求时，不需要做配置定制序列化。<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F463" target="_blank">#463</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F459" target="_blank">#459</a></li> 
 <li>Date对象反序列化支持输入空字符串识别为null<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F467" target="_blank">#467</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F504" target="_blank">#504</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F493" target="_blank">#493</a></li> 
 <li>修复某些场景日期类型配置JSONField.format无效的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F468" target="_blank">#468</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F495" target="_blank">#495</a></li> 
 <li>兼容包支持ParserConfig配置propertyNamingStrategy<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F505" target="_blank">#505</a></li> 
 <li>修复TypeReference传入参数无法正确解析的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F501" target="_blank">#501</a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F474" target="_blank">#474</a></li> 
 <li>修复BigDecimal类型反序列化输入科学计数法数值结果不对的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F492" target="_blank">#492</a></li> 
 <li>兼容包支持Feature. UseNativeJavaObject<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F488" target="_blank">#488</a></li> 
 <li>修复JSONPath在多层嵌套读取结果不对的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F487" target="_blank">#487</a></li> 
 <li>修复兼容包JSON.parseObject不支持输入空置的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F482" target="_blank">#482</a></li> 
 <li>修复mongo GeoJsonPoint类型的支持 bug<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F483" target="_blank">#483</a></li> 
 <li>修复JSONPath设置多层节点不存在时不生效的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F476" target="_blank">#476</a></li> 
 <li>JSONArray保留toJSONString方法，方便升级，提升兼容性</li> 
 <li>JSON.parseObject方法支持InputStream和Reader输入<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F103" target="_blank">#103</a></li> 
 <li>修复JSONPath对"$"结果返回不对的问题</li> 
 <li>修复JSONWriter.Feature.IgnoreNoneSerializable对rootObject不生效的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F477" target="_blank">#477</a></li> 
 <li>新增支持ContextNameFilter/ContextValueFilter<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F484" target="_blank">#484</a></li> 
 <li>修复对象数组类型字段反序列化报错的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F464" target="_blank">#464</a></li> 
 <li>修复PropertyFilter导致输出Null的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fissues%2F471" target="_blank">#471</a></li> 
</ol> 
<h4 style="margin-left:0px; margin-right:0px; text-align:start"><strong>MAVEN 依赖配置</strong></h4> 
<div style="text-align:start"> 
 <pre><<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>com.alibaba.fastjson2</<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>fastjson2</<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>2.0.8</<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>
</<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>></pre> 
</div> 
<ul> 
 <li>GraalVM版本</li> 
</ul> 
<div style="text-align:start"> 
 <pre><<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>com.alibaba.fastjson2</<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>fastjson2</<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>2.0.8.graal</<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>
</<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>></pre> 
</div> 
<ul> 
 <li>Android版本</li> 
</ul> 
<div style="text-align:start"> 
 <pre><<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>com.alibaba.fastjson2</<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>fastjson2</<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>2.0.8.android</<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>
</<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>></pre> 
</div> 
<ul> 
 <li>1.x 兼容版本</li> 
</ul> 
<div style="text-align:start"> 
 <pre><<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>com.alibaba</<span style="color:var(--color-prettylights-syntax-entity-tag)">groupId</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>fastjson</<span style="color:var(--color-prettylights-syntax-entity-tag)">artifactId</span>>
<<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>2.0.8</<span style="color:var(--color-prettylights-syntax-entity-tag)">version</span>>
</<span style="color:var(--color-prettylights-syntax-entity-tag)">dependency</span>></pre> 
</div> 
<h4 style="margin-left:0px; margin-right:0px; text-align:start"><strong>相关链接</strong></h4> 
<ul> 
 <li>相关issue 25个<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Fmilestone%2F7" target="_blank">https://github.com/alibaba/fastjson2/milestone/7</a></li> 
 <li>代码tag<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Freleases%2Ftag%2F2.0.8" target="_blank">https://github.com/alibaba/fastjson2/releases/tag/2.0.8</a></li> 
 <li>标准版本<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frepo1.maven.org%2Fmaven2%2Fcom%2Falibaba%2Ffastjson2%2Ffastjson2%2F2.0.8%2F" target="_blank">https://repo1.maven.org/maven2/com/alibaba/fastjson2/fastjson2/2.0.8/</a></li> 
 <li>graal支持版本<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frepo1.maven.org%2Fmaven2%2Fcom%2Falibaba%2Ffastjson2%2Ffastjson2%2F2.0.8.graal%2F" target="_blank">https://repo1.maven.org/maven2/com/alibaba/fastjson2/fastjson2/2.0.8.graal/</a><span> </span>(仅在GraalVM 22.1 JDK17上做过验证)</li> 
 <li>android版本<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frepo1.maven.org%2Fmaven2%2Fcom%2Falibaba%2Ffastjson2%2Ffastjson2%2F2.0.8.android%2F" target="_blank">https://repo1.maven.org/maven2/com/alibaba/fastjson2/fastjson2/2.0.8.android/</a></li> 
 <li>1.x兼容版本<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Frepo1.maven.org%2Fmaven2%2Fcom%2Falibaba%2Ffastjson%2F2.0.8%2F" target="_blank">https://repo1.maven.org/maven2/com/alibaba/fastjson/2.0.8/</a></li> 
</ul> 
<p><span style="background-color:#ffffff; color:#333333">详情可查看：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Ffastjson2%2Freleases%2Ftag%2F2.0.8" target="_blank">https://github.com/alibaba/fastjson2/releases/tag/2.0.8</a> </p>
                                        </div>
                                      
</div>
            