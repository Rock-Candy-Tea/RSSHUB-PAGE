
---
title: 'MyFaces Core 2.0.25 发布，JSF 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5542'
author: 开源中国
comments: false
date: Mon, 17 May 2021 00:14:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5542'
---

<div>   
<div class="content">
                                                                    
                                                        <p>MyFaces Core 2.0.25 现已发布。MyFaces 是 JSF (JavaServerFaces) Web框架（JSR 127）的一个实现。JavaServer（tm）Faces Web 框架是一个新的实现 MVC 模式的规范。</p> 
<p><strong>主要更新内容</strong></p> 
<ul> 
 <li>修复了 JSF myfaces 对 WeakHashMap 的同步访问</li> 
 <li>对于空的 selectManyCheckbox 组件不调用验证器</li> 
 <li>在 ValidatorException 之后，FacesMessage.Severity 总是设置为 ERROR</li> 
 <li>修复了 EL 3.0 收集结构损坏的问题</li> 
 <li>修复了自动滚动在某些环境下不起作用的问题</li> 
 <li>在 UIData、UIForm、UINamingContainer 和 UIRepeat 的 visitTree 中，pushComponentToEL 应该在调用 isVisitable 之前被调用</li> 
 <li>修复了 _ComponentAttributesMap 中的并发问题</li> 
 <li>Classpath._searchDir 现在可以抛出 NullPointerException</li> 
 <li>修复了 oam.view.facelets.util.ClassPath 中的 JarFile 从未发布的问题</li> 
 <li>修复了超出范围的字符串引发异常的问题</li> 
 <li>NumberConverter.getAsObject 为 BigInteger 属性返回 Long 值</li> 
 <li>使用 SecureRandom 生成令牌</li> 
</ul> 
<p>详细内容请查看<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmail-archives.apache.org%2Fmod_mbox%2Fwww-announce%2F202105.mbox%2F%253Cpony-318124ad103a9149f882f053df0a81d4ff1fd29d-b1ac88f1ba6b319524d485fcebcc7fd0e5704c59%40announce.apache.org%253E" target="_blank">更新公告</a>。</p>
                                        </div>
                                      
</div>
            