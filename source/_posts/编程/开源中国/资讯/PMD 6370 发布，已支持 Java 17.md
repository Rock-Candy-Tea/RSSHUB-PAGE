
---
title: 'PMD 6.37.0 发布，已支持 Java 17'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5628'
author: 开源中国
comments: false
date: Tue, 03 Aug 2021 06:48:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5628'
---

<div>   
<div class="content">
                                                                                            <p>PMD 是一个代码分析器，能够帮助发现常见的编程问题，比如未使用的变量、空的 catch 块、不必要的对象创建等等。最初仅支持 Java 代码，目前还可支持 JavaScript、<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fsalesforce.com%2F">Salesforce.com</a> Apex 和 Visualforce、PLSQL、Apache Velocity、XML 和 XSL 。</p> 
<p>PMD 6.37.0 正式发布，本次更新内容如下：</p> 
<p><strong>值得注意的更新：</strong></p> 
<p>Java 17 支持：这个版本的 PMD 带来了对 Java 17 的支持。PMD 支持 JEP 409: Sealed Classes 已被提升为 Java 17 的标准语言特性。</p> 
<p><strong>重命名的规则：</strong></p> 
<p>Java 规则 <code>MissingBreakInSwitch</code> 已被重命名为 <code>ImplicitSwitchFallThrough</code>，以更好地反映该规则的目的；</p> 
<p><strong>废弃的规则：</strong></p> 
<ul> 
 <li>以下的 Java 规则已被废弃，并从快速入门规则集中删除，因为新规则 <code>SimplifiableTestAssertion</code> 合并了它们的功能： 
  <ul> 
   <li><code>UseAssertEqualsInsteadOfAssertTrue</code></li> 
   <li><code>UseAssertNullInsteadOfAssertTrue</code></li> 
   <li><code>UseAssertSameInsteadOfAssertTrue</code></li> 
   <li><code>UseAssertTrueInsteadOfAssertEquals</code></li> 
   <li><code>SimplifyBooleanAssertion</code></li> 
  </ul> </li> 
 <li>Java 规则<code>ReturnEmptyArrayRatherThanNull</code>已弃用并从快速入门规则集中删除，将使用新规则<code>ReturnEmptyCollectionRatherThanNull</code> 取代它；</li> 
 <li>以下 Java 规则已弃用并从快速入门规则集中删除，因为新规则<code>PrimitiveWrapperInstantiation</code>合并了它们的功能： 
  <ul> 
   <li><code>BooleanInstantiation</code></li> 
   <li><code>ByteInstantiation</code></li> 
   <li><code>IntegerInstantiation</code></li> 
   <li><code>LongInstantiation</code></li> 
   <li><code>ShortInstantiation</code></li> 
  </ul> </li> 
 <li>Java 规则 <code>UnnecessaryWrapperObjectCreation</code>已弃用，在 PMD 7 之前没有计划进行替换。</li> 
</ul> 
<p><strong>修复的问题：</strong></p> 
<ul> 
 <li>apex 
  <ul> 
   <li>[apex] ApexCRUDViolation 没有报告数据库类 DMLs、内联 no-arg 对象实例化和内联列表初始化；</li> 
   <li>[apex] ApexCRUDViolation 没有报告 SOQL 的循环；</li> 
  </ul> </li> 
 <li>Core： 
  <ul> 
   <li>[core] 语言版本比较</li> 
   <li>[xml] 允许使用 XPath 规则检查 Salesforce XML 元数据</li> 
   <li>[core] CPD 在使用 --skip-lexical-errors 运行时应避免不必要的拷贝；</li> 
  </ul> </li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpmd%2Fpmd%2Freleases%2Ftag%2Fpmd_releases%252F6.37.0" target="_blank">https://github.com/pmd/pmd/releases/tag/pmd_releases%2F6.37.0</a></p>
                                        </div>
                                      
</div>
            