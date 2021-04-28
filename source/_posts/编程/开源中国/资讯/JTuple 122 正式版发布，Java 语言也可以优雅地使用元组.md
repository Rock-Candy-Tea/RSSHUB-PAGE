
---
title: 'JTuple 1.2.2 正式版发布，Java 语言也可以优雅地使用元组'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7105'
author: 开源中国
comments: false
date: Wed, 28 Apr 2021 09:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7105'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">JTuple 1.2.2 正式版发布了，本次更新内容：</span></p> 
<ol> 
 <li>新增<code>count</code>方法，用于统计某个数据在元组当中出现的次数</li> 
 <li>升级<code>junit</code>版本</li> 
</ol> 
<p> 项目地址：</p> 
<p>github:<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fsd4324530%2FJTuple" target="_blank">https://github.com/sd4324530/JTuple</a></p> 
<p>gitee:<a href="https://gitee.com/pyinjava/jtuple">https://gitee.com/pyinjava/jtuple</a></p> 
<h3 style="text-align:left">JTuple</h3> 
<p style="text-align:left">Java 语言版本的元组数据类型，实现了元组类型的特性（不可变、 可迭代）以及常用操作方法</p> 
<p style="text-align:left">轻量级，无依赖，线程安全</p> 
<h3 style="text-align:left">元组的意义</h3> 
<p style="text-align:left">元组最重要的意义是用来实现多值返现。 很多时候我们需要返回一组值，更可怕的是这组值的类型可能并不完全一样，比如http请求时，有请求的返回码（int）以及响应报文（String）</p> 
<p style="text-align:left">对于java人员来说，遇到这种情况时，一般的解决方案是编写一个类，类里只有2个属性，分别是以上2个，然后返回给调用者。是不是有种胸闷的感觉。折腾，造孽啊</p> 
<p style="text-align:left">或者就返回一个列表，但是因为类型不统一，只能用List<Object>，后续处理的代码的可读性会很差，我相信任何一个技术水平过关或者有职业操守的程序员都不会这么做</p> 
<p style="text-align:left">元组的出现，就是为了解决这种情况的，很多年轻的语言（Python, Scala...）都内置了元组，本项目就是让Java开发人员也可以享受到元组带来的编程时的便捷和快乐</p> 
<h2 style="text-align:left">主要实现</h2> 
<table cellspacing="0" style="width:776px"> 
 <tbody> 
  <tr> 
   <th>类名</th> 
   <th>描述</th> 
  </tr> 
 </tbody> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd">Tuple</td> 
   <td style="border-color:#dddddd">元组抽象，实现元组数据结构以及常用操作方法</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">Tuple0</td> 
   <td style="border-color:#dddddd">空元组，不包含任何元素</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">Tuple1</td> 
   <td style="border-color:#dddddd">只包含1个元素的元组</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">Tuple2</td> 
   <td style="border-color:#dddddd">只包含2个元素的元组</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">Tuple3</td> 
   <td style="border-color:#dddddd">只包含3个元素的元组</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">Tuple4</td> 
   <td style="border-color:#dddddd">只包含4个元素的元组</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">Tuple5</td> 
   <td style="border-color:#dddddd">只包含5个元素的元组</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">TupleN</td> 
   <td style="border-color:#dddddd">包含N个元素的元组</td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="text-align:left">元组操作</h2> 
<table cellspacing="0" style="width:776px"> 
 <tbody> 
  <tr> 
   <th>操作API</th> 
   <th>说明</th> 
  </tr> 
 </tbody> 
 <tbody> 
  <tr> 
   <td style="border-color:#dddddd">add</td> 
   <td style="border-color:#dddddd">元组合并</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">foreach</td> 
   <td style="border-color:#dddddd">元组迭代</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">forEachWithIndex</td> 
   <td style="border-color:#dddddd">元组带序号迭代</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">swap</td> 
   <td style="border-color:#dddddd">元组翻转</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">toArray</td> 
   <td style="border-color:#dddddd">元组转成数组</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">toList</td> 
   <td style="border-color:#dddddd">元组转成列表</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">get</td> 
   <td style="border-color:#dddddd">获取元组某一个元素</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">contains</td> 
   <td style="border-color:#dddddd">元组中是否包含某个元素</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">subTuple</td> 
   <td style="border-color:#dddddd">截取子元组</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">equals</td> 
   <td style="border-color:#dddddd">比较2个元组内容是否相同</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">toString</td> 
   <td style="border-color:#dddddd">输出字符串表示的元组，如: (123, 456)</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">repeat</td> 
   <td style="border-color:#dddddd">重复元组内的所有元素</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">stream</td> 
   <td style="border-color:#dddddd">将元组转换成流，类似List.stream</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">parallelStream</td> 
   <td style="border-color:#dddddd">将元组转换成并行流，类似List.parallelStream</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">sort</td> 
   <td style="border-color:#dddddd">将元组列表（数组）进行排序</td> 
  </tr> 
  <tr> 
   <td style="border-color:#dddddd">count</td> 
   <td style="border-color:#dddddd">统计某个数据在元组当中出现的次数</td> 
  </tr> 
 </tbody> 
</table>
                                        </div>
                                      
</div>
            