
---
title: 'Hutool-5.8.0.M1 发布，尝试里程碑发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/img/201803/21114512_tLDC.jpg'
author: 开源中国
comments: false
date: Wed, 30 Mar 2022 09:47:00 GMT
thumbnail: 'https://static.oschina.net/uploads/img/201803/21114512_tLDC.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img src="https://static.oschina.net/uploads/img/201803/21114512_tLDC.jpg" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Hutool是一个小而全的Java工具类库，提供优雅、高效和便捷的工具方法。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">------------------------------------------------------------------------------------------</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">本来这个版本应该是5.7.23的，可惜用户提了一些issue，这些问题的解决必须修改原有代码结构：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">1、如MongoDB客户端封装，由于其驱动本身做了不兼容修改，包装的工具类不得不进行修改。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">2、涉及到Bean拷贝的代码部分（BeanCopier），由于一个参数失效，以为只是简单的一个bug，后来发现是整个设计有问题……崩溃程度可想而知，肝了两个晚上重构了这部分代码。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">3、修改代码的同时才发现还有很多部分的设计有问题，顺便做了小重构。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">4、为了解决每次大版本升级的可能带来的对老用户的影响，此次版本采用里程碑方式发布，版本为M1（感觉给用户送了颗CPU），也是解决Hutool每次“激进”升级的问题（毕竟年龄大了，要稳重）</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">5、希望购买代替捐赠，如果你希望支持下Hutool，可以去Hutool主页点->击进入周边商店购买Hutool周边来支持Hutool哦，这比捐赠实惠的多（毕竟捐赠者我不知道如何道谢，很有道德负担……）</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">鸣谢一下此次版本一起讨论和一起解决大量issue的Hutool几位成员：</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">@阿超 @Cherryrum @Husky</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">------------------------------------------------------------------------------------------</p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">5.8.0.M1</h1> 
<h3 style="margin-left:0; margin-right:0; text-align:left">❌不兼容特性</h3> 
<ul> 
 <li>【db 】 【不向下兼容 】增加MongoDB4.x支持返回MongoClient变更（pr#568@Gitee）</li> 
 <li>【json 】 【可能兼容问题】修改JSONObject结构，继承自MapWrapper</li> 
 <li>【core 】 【可能兼容问题】BeanCopier重构，新建XXXCopier，删除XXXValueProvider</li> 
 <li>【core 】 【可能兼容问题】URLEncoder废弃，URLEncoderUtil使用RFC3986</li> 
 <li>【core 】 【可能兼容问题】Base32分离编码和解码，以便减少数据加载，支持Hex模式</li> 
 <li>【core 】 【可能兼容问题】Base58分离编码和解码</li> 
 <li>【core 】 【可能兼容问题】Base62分离编码和解码，增加inverted模式支持</li> 
 <li>【core 】 【兼容问题 】PunyCode参数由String改为Charsequence</li> 
 <li>【cron 】 【可能兼容问题】SimpleValueParser改名为AbsValueParser，改为abstract</li> 
 <li>【poi 】 【可能兼容问题】ExcelUtil.getBigWriter返回值改为BigExcelWriter</li> 
 <li>【core 】 【可能兼容问题】Opt.ofEmptyAble参数由List改为Collection子类（pr#580@Gitee）</li> 
 <li>【json 】 【可能兼容问题】JSON转Bean时，使用JSON本身的相关设置，而非默认（issue#2212@Github）</li> 
 <li>【json 】 【可能兼容问题】JSONConfig中isOrder废弃，默认全部有序</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">🐣新特性</h3> 
<ul> 
 <li>【http 】 HttpRequest.form采用TableMap方式（issue#I4W427@Gitee）</li> 
 <li>【core 】 AnnotationUtil增加getAnnotationAlias方法（pr#554@Gitee）</li> 
 <li>【core 】 FileUtil.extName增加对tar.gz特殊处理（issue#I4W5FS@Gitee）</li> 
 <li>【crypto 】 增加XXTEA实现（issue#I4WH2X@Gitee）</li> 
 <li>【core 】 增加Table实现（issue#2179@Github）</li> 
 <li>【core 】 增加UniqueKeySet（issue#I4WUWR@Gitee）</li> 
 <li>【core 】 阿拉伯数字转换成中文对发票票面金额转换的扩展（pr#570@Gitee）</li> 
 <li>【core 】 ArrayUtil增加replace方法（pr#570@Gitee）</li> 
 <li>【core 】 CsvReadConfig增加自定义标题行行号（issue#2180@Github）</li> 
 <li>【core 】 FileAppender优化初始List大小（pr#2197@Github）</li> 
 <li>【core 】 Base32增加pad支持（pr#2195@Github）</li> 
 <li>【core 】 Dict增加setFields方法（pr#578@Gitee）</li> 
 <li>【db 】 新加db.meta的索引相关接口（pr#563@Gitee）</li> 
 <li>【db 】 Oracle中Column#typeName后的长度去掉（pr#563@Gitee）</li> 
 <li>【poi 】 优化ExcelReader，采用只读模式（pr#2204@Gitee）</li> 
 <li>【poi 】 优化ExcelBase，将alias放入</li> 
 <li>【poi 】 优化ExcelBase，将alias放入</li> 
 <li>【core 】 改进StrUtil#startWith、endWith性能</li> 
 <li>【cron 】 增加CronPatternParser、MatcherTable</li> 
 <li>【http 】 GlobalHeaders增加系统属性allowUnsafeServerCertChange、allowUnsafeRenegotiation</li> 
 <li>【http 】 UserAgentUtil 解析，增加MiUI/XiaoMi浏览器判断逻辑（pr#581@Gitee）</li> 
 <li>【core 】 FileAppender添加锁构造（pr#2211@Github）</li> 
 <li>【poi 】 ExcelReader增加构造（pr#2213@Github）</li> 
 <li>【core 】 MapUtil提供change函数，EnumUtil提供getBy函数，通过lambda进行枚举字段映射（pr#583@Gitee）</li> 
 <li>【core 】 CompareUtil增加comparingIndexed（pr#585@Gitee）</li> 
 <li>【db 】 DruidDataSource构建时支持自定义参数（issue#I4ZKCW@Gitee）</li> 
 <li>【poi 】 ExcelWriter增加addImg重载（issue#2218@Github）</li> 
 <li>【bloomFilter】 增加FuncFilter</li> 
 <li>【http 】 增加GlobalInterceptor（issue#2217）</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">🐞Bug修复</h3> 
<ul> 
 <li>【core 】 修复ObjectUtil.hasNull传入null返回true的问题（pr#555@Gitee）</li> 
 <li>【core 】 修复NumberConverter对数字转换的问题（issue#I4WPF4@Gitee）</li> 
 <li>【core 】 修复ReflectUtil.getMethods获取接口方法问题（issue#I4WUWR@Gitee）</li> 
 <li>【core 】 修复NamingCase中大写转换问题（pr#572@Gitee）</li> 
 <li>【http 】 修复GET重定向时，携带参数问题（issue#2189@Github）</li> 
 <li>【core 】 修复FileUtil、FileCopier相对路径获取父路径错误问题（pr#2188@Github）</li> 
 <li>【core 】 修复CopyOptions中fieldNameEditor无效问题（issue#2202@Github）</li> 
 <li>【json 】 修复JSON对Map.Entry的解析问题</li> 
 <li>【core 】 修复MapConverter中map与map转换兼容问题</li> 
 <li>【poi 】 解决sax读取时，POI-5.2.x兼容性问题</li> 
 <li>【core 】 修复判断两段时间区间交集问题（pr#2210@Github）</li> 
 <li>【http 】 修复标签误删问题（issue#I4Z7BV@Gitee）</li> 
 <li>【core 】 修复Win下文件名带*问题（pr#584@Gitee）</li> 
 <li>【core 】 FileUtil.getMimeType增加rar、7z支持（issue#I4ZBN0@Gitee）</li> 
 <li>【json 】 JSON修复transient设置无效问题（issue#2212@Github）</li> 
 <li>【core 】 修复IterUtil.getElementType获取结果为null的问题（issue#2222@Github）</li> 
 <li>【core 】 修复农历转公历在闰月时错误（issue#I4ZSGJ@Gitee）</li> 
</ul>
                                        </div>
                                      
</div>
            