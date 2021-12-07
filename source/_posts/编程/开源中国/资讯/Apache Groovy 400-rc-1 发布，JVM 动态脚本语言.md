
---
title: 'Apache Groovy 4.0.0-rc-1 发布，JVM 动态脚本语言'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1003'
author: 开源中国
comments: false
date: Tue, 07 Dec 2021 06:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1003'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Apache Groovy 4.0.0 的第一个 RC 版本现已发布，这<span style="background-color:#ffffff; color:#333333">是一个用于 JVM 的多面性编程语言。</span></p> 
<p><strong><span style="background-color:#ffffff; color:#333333">主要更新内容</span></strong></p> 
<ul> 
 <li>Bug 修复 
  <ul> 
   <li>低效的代码生成</li> 
   <li><span style="background-color:#ffffff; color:#182026">调用间接默认接口方法时，动态/静态编译都会失败</span></li> 
   <li>STC 无法捕获 lambda 返回类型的类型错误</li> 
   <li>STC 使用错误类型实例化参数化函数，导致不健全</li> 
   <li>STC：<span style="background-color:#ffffff; color:#182026">lowed bound </span>通配符推理产生误报</li> 
   <li>结合使用地点方差和菱形运算符推断出错误的类型参数</li> 
   <li>SC：从 lambda 访问私有属性的强制转换异常</li> 
   <li>使用同名的超类和超接口方法会出错</li> 
   <li>SC：从非公共接口调用接口默认方法时出现 IncompatibleClassChangeError</li> 
  </ul> </li> 
 <li>改进 
  <ul> 
   <li>可以使用收集器改进 DGM 方法的泛型信息</li> 
   <li>在启用静态编译的情况下，应在编译时捕获抽象方法的 "super" 调用</li> 
   <li>Java8 不会将枚举值加载到注释属性中</li> 
   <li>StaticTypeCheckingSupport#evaluateExpression 可以为简单表达式提供轻量级评估</li> 
   <li>可以改进 TupleConstructor 以使用更智能的模式来处理默认值</li> 
   <li>STC：根据目标方法检查 lambda 或闭包参数类型</li> 
   <li>SC: === 和 !== 编译为 ScriptBytecodeAdapter#compareIdentical</li> 
   <li>提供一种机制来确定在同一阶段运行的 AST 转换的优先级</li> 
  </ul> </li> 
</ul> 
<p>详情请查看<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmail-archives.apache.org%2Fmod_mbox%2Fwww-announce%2F202112.mbox%2F%253CCADRx3PMmqhCVd%3DVSGEKBpdVn%2BGmDY_KGBGRAYjD0%3De4FErHyVg%40mail.gmail.com%253E" target="_blank">更新公告</a>。</p> 
<p> </p>
                                        </div>
                                      
</div>
            