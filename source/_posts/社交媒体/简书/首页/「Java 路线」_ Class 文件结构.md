
---
title: '「Java 路线」_ Class 文件结构'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/10107787-6d8f0b818c76beba.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/10107787-6d8f0b818c76beba.png'
---

<div>   
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1920" data-height="1080"><img data-original-src="//upload-images.jianshu.io/upload_images/10107787-6d8f0b818c76beba.png" data-original-width="1920" data-original-height="1080" data-original-format="image/png" data-original-filesize="296301" src="https://upload-images.jianshu.io/upload_images/10107787-6d8f0b818c76beba.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<blockquote>
<p><strong>点赞关注，不再迷路，你的支持对我意义重大！</strong></p>
<p>🔥 <strong>Hi，我是丑丑。本文 <a href="https://www.jianshu.com/p/6e3feee3fca5" target="_blank">「Java 路线」| 导读 —— 他山之石，可以攻玉</a> 已收录，这里有 Android 进阶成长路线笔记 & 博客，欢迎跟着彭丑丑一起成长。（联系方式在 GitHub）</strong></p>
</blockquote>
<h2>前言</h2>
<ul>
<li>
<code>Class 文件</code>是<code>Java</code>技术体系的重要组成部分，在学习整个虚拟机的执行引擎之前，应该清楚<code>Class 文件</code>的结构；</li>
<li>这篇文章将带你理解<code>Class 文件</code>的基本结构，希望能帮上忙。</li>
</ul>
<h2>延伸文章</h2>
<ul>
<li><p>对于<code>Java</code>编译过程不了解，请阅读：<a href="https://www.jianshu.com/p/b1d2608848dd" target="_blank">《Java | 聊一聊编译过程（编译前端 & 编译后端）》</a></p></li>
<li><p>对于<code>类加载</code>的流程不太了解，请阅读：<a href="https://www.jianshu.com/p/993206508d35" target="_blank">《Java | 谈谈你对类加载过程的理解》</a></p></li>
</ul>
<h2>目录</h2>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1403" data-height="1547"><img data-original-src="//upload-images.jianshu.io/upload_images/10107787-8c6b63cc1e8e1d7c.png" data-original-width="1403" data-original-height="1547" data-original-format="image/png" data-original-filesize="141570" src="https://upload-images.jianshu.io/upload_images/10107787-8c6b63cc1e8e1d7c.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<hr>
<h2>1. 什么是 Class 文件？</h2>
<ul>
<li><p><strong>定义</strong>：或称字节码，可以看作<code>Java 虚拟机</code>的可执行文件</p></li>
<li><p><strong>作用</strong>：对应于一个类 / 抽象类 / 接口的定义信息</p></li>
<li><p><strong>意义</strong>：<strong><code>Java 虚拟机 & Class 文件</code>共同构成了<code>Java</code>无关性的基础</strong></p></li>
<li>
<p><strong>来源</strong></p>
<ul>
<li><ol>
<li>由<code>Java 源码</code>经过<code>Java 编译器</code>编译后得到，以磁盘文件形式存在</li>
</ol></li>
<li><ol start="2">
<li>由字节码生成技术<code>（如javassist / CGLib / ASM）</code>生成，以内存中二进制流形式存在</li>
</ol></li>
</ul>
</li>
</ul>
<blockquote>
<h6># 咬文嚼字 #</h6>
<p>虽然字节码不一定是以 <strong>“磁盘文件”</strong> 的形式存在，但是通常在很多文献 & 资料中会笼统地将字节码表述为<code>Class 文件</code>，这里不必钻牛角尖。</p>
</blockquote>
<p>更多信息请务必阅读：<a href="https://www.jianshu.com/p/4e0ac401fe7b" target="_blank">《Java | 为什么 Java 实现了平台无关性》</a></p>
<hr>
<h2>2. Class 文件的大致结构</h2>
<ul>
<li>
<code>Class 文件</code>是一种强协议的紧凑型结构（遵循《Java 虚拟机规范》）</li>
<li>
<code>Class 文件</code>有三种数据结构：<strong>无符号数、TVL、表</strong>，具体如下：</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2226" data-height="582"><img data-original-src="//upload-images.jianshu.io/upload_images/10107787-2cf800ac0a3f76de.png" data-original-width="2226" data-original-height="582" data-original-format="image/png" data-original-filesize="194779" src="https://upload-images.jianshu.io/upload_images/10107787-2cf800ac0a3f76de.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li>
<code>Class 文件</code>本质上也是一个表，大致结构如下图：</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1816" data-height="1362"><img data-original-src="//upload-images.jianshu.io/upload_images/10107787-1f55a62889b67a52.png" data-original-width="1816" data-original-height="1362" data-original-format="image/png" data-original-filesize="262149" src="https://upload-images.jianshu.io/upload_images/10107787-1f55a62889b67a52.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li>
<strong>魔数：</strong>固定值<code>0xCAFEBABE</code>，用于鉴别为合法的<code>Class 文件</code>
</li>
<li>
<strong>版本号：</strong>表示<code>Class 文件</code>的目标版本号，高版本的虚拟机可以向前兼容旧版本<code>Class 文件</code>
</li>
<li>
<strong>访问标志：</strong>一个<code>u2</code>无符号数，用于表示本类 / 接口的访问信息。其中每个标志位的值与<code>java.lang.reflect.Modifier</code>中的常量一一对应：</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="2088" data-height="1096"><img data-original-src="//upload-images.jianshu.io/upload_images/10107787-a05288ca98c4bd87.png" data-original-width="2088" data-original-height="1096" data-original-format="image/png" data-original-filesize="191932" src="https://upload-images.jianshu.io/upload_images/10107787-a05288ca98c4bd87.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<ul>
<li><p><strong>本类索引 & 父类索引 & 接口索引集</strong>：是一个索引值，（共经过 2 次索引后）指向常量池中一个<code>utf-8</code>编码的 <strong>全限定名</strong>，例如：<code>java/lang/Object;</code></p></li>
<li><p><strong>字段表集合：</strong>用于描述类或接口中声明的变量<strong>（包括类变量与成员变量）</strong></p></li>
<li><p><strong>方法表集合：</strong>用于描述类或接口中声明的方法<strong>（包括类方法与成员方法）</strong></p></li>
<li><p><strong>属性表集合：</strong>用于描述 Class 文件、字段表、方法表中携带的属性</p></li>
</ul>
<hr>
<p>下面，我将概括表中各个重点数据项的具体含义！</p>
<h2>3. 常量池（const pool）</h2>
<ul>
<li><strong>常量池中的每一项常量都是一个表</strong></li>
<li>
<strong>存放两种类常量：字面量（Literal）</strong>和 <strong>符号引用（Symbolic References）</strong>
</li>
</ul>
<p><strong>符号引用（Symbolic References）</strong>是一个字符串类型的字面量（存储在常量池），它的作用是唯一地标示一个实体，最重要的特点如下：</p>
<ul>
<li><p><strong>平台无关性</strong><br>
这一点与<code>Java</code>的特性是一脉相承的。符号引用与具体虚拟机实现内存布局无关，需要在运行期将符号引用转换为<strong>直接引用（Direct Reference）</strong>，这个直接引用才是符号引用在虚拟机中的真实存在。</p></li>
<li><p><strong>唯一性</strong><br>
无歧义地标示一个目标，以方法为例，如果是本类中声明的方法，不需要添加类名（如：<code>Method func:()V</code>）；如果是其他类中声明的方法， 需要添加类名前缀（如：<code>Method com/Base.func:()V</code>）。</p></li>
</ul>
<p>常量池表结构有一个共同的特点，就是表结构的首元素是<code>u1</code>的标志位，代表当前的常量类型，截止到<code>Java 13</code>总共有 20 种常量：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1099" data-height="804"><img data-original-src="//upload-images.jianshu.io/upload_images/10107787-4cb8e3d52127c0c7.png" data-original-width="1099" data-original-height="804" data-original-format="image/png" data-original-filesize="302203" src="https://upload-images.jianshu.io/upload_images/10107787-4cb8e3d52127c0c7.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">常量类型 —— 引用自《深入理解Java虚拟机》</div>
</div>
<h2>4. 本类索引 & 父类索引 & 接口索引集</h2>
<ul>
<li>本类索引肯定存在，只有一个</li>
<li>
<code>Java</code>是类单继承，所以父类索引只有一个（特例：<code>Object</code>的父类索引为 0）</li>
<li>
<code>Java</code>是接口多继承，所以接口索引有零或多个</li>
</ul>
<p>这三个索引值均指向常量池中<code>CONSTANT_Class_info</code>常量，而<code>CONSTANT_Class_info</code>常量本质上也是一个索引值，指向<code>CONSTANT_Utf8_info</code>常量。经过 2次 索引，这三个索引最终指向对应 <strong>类 / 接口的全限定名</strong></p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="885" data-height="164"><img data-original-src="//upload-images.jianshu.io/upload_images/10107787-e603c5117158c123.png" data-original-width="885" data-original-height="164" data-original-format="image/png" data-original-filesize="54572" src="https://upload-images.jianshu.io/upload_images/10107787-e603c5117158c123.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">2 次索引后指向全限定名 —— 引用自《深入理解Java虚拟机》</div>
</div>
<h2>5. 字段表（field_info）</h2>
<p>字段表用于描述类字段与实例字段，但只包括在本类中声明的字段，既不包括父类中声明的字段，也不包括方法内部声明的局部变量。要注意的是，编译器生成的字段是包括的，例如编译器会为非静态内部类添加外部类的引用字段。字段表的基本结构如下：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1770" data-height="804"><img data-original-src="//upload-images.jianshu.io/upload_images/10107787-f4d0e9a657663032.png" data-original-width="1770" data-original-height="804" data-original-format="image/png" data-original-filesize="135387" src="https://upload-images.jianshu.io/upload_images/10107787-f4d0e9a657663032.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">字段表的基本结构</div>
</div>
<ul>
<li>
<strong>access_flags：</strong>字段的访问标志位</li>
<li>
<strong>name_index：</strong>常量池索引，最终指向字段的简单名称，见第 8 节</li>
<li>
<strong>descriptor_index：</strong>常量池索引，最终指向字段的描述符，见第 8 节</li>
<li>
<strong>attributes_count & attributes：</strong>字段属性，为字段的附加信息，见第 8 节</li>
</ul>
<hr>
<h2>6. 方法表（method_info）</h2>
<p>方法表和字段表的设计是很相似的。方法表用于描述类方法与实例方法，但只包括在本类中声明的方法或者重写的方法，不包括父类或父接口中声明的方法。需要注意的是，编译器生成的方法是包括的，例如类构造器<code><clinit>()</code>与实例构造器<code><init>()</code>。方法表的基本结构如下：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1766" data-height="798"><img data-original-src="//upload-images.jianshu.io/upload_images/10107787-90c113c69a494d8f.png" data-original-width="1766" data-original-height="798" data-original-format="image/png" data-original-filesize="134023" src="https://upload-images.jianshu.io/upload_images/10107787-90c113c69a494d8f.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">方法表的基本结构</div>
</div>
<p>可以看到，方法表和字段表的基本结构是完全一致的，此处不再赘述。需要特别指出的是，方法里面的代码在方法的<code>Code属性</code>，方法的受检异常声明在<code>Exception属性</code>。</p>
<hr>
<h2>7. 属性表（attribute_info）</h2>
<ul>
<li><strong>属性相当于字段表或方法表的附加信息</strong></li>
<li>
<strong>每一项属性都是一个表</strong>，基本结构如下图所示：</li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1768" data-height="606"><img data-original-src="//upload-images.jianshu.io/upload_images/10107787-3a2fdf34a1975bd5.png" data-original-width="1768" data-original-height="606" data-original-format="image/png" data-original-filesize="87293" src="https://upload-images.jianshu.io/upload_images/10107787-3a2fdf34a1975bd5.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">属性表的基本结构</div>
</div>
<ul>
<li>
<strong>attribute_name_index：</strong>常量池索引，最终指向一个属性名。<code>Class 文件</code>使用属性名来区分每一种属性，截止到<code>Java 12</code>，总共有 29 种预定义属性。</li>
<li>
<strong>attribute_length：</strong>不同属性的属性信息是不同的，因此需要一个长度表表示属性信息占用的长度</li>
<li>
<strong>info：</strong>属性信息</li>
</ul>
<blockquote>
<h6># 你觉得呢？#</h6>
<p>市面上你能找到的介绍虚拟机的书籍，普遍都会按顺序罗列出每种属性的信息。笔者并不是说这种方式不好，因为作为书籍的阐述方式需要考虑到读者可接受度 & 参考性的问题。但是如果以博客的阐述方式也采用同样地方式，岂非成为知识搬运工？因此，我将从不同的问题域出发，在每个问题域中介绍每种属性。</p>
</blockquote>
<h6>Code 属性</h6>
<h6>Exceptions 属性</h6>
<ul>
<li>请阅读：<br>
<a href="https://www.jianshu.com/p/993206508d35" target="_blank">《Java | 从方法调用到方法返回的过程（正常返回）》</a><br>
<a href="https://www.jianshu.com/p/993206508d35" target="_blank">《Java | 从方法调用到方法返回的过程（异常返回）》</a>
</li>
</ul>
<hr>
<h6>LocalVariableTable 属性</h6>
<hr>
<p><strong>LocalVariableTypeTable 属性</strong><br>
<strong>Signature 属性</strong></p>
<p>泛型中所谓的类型擦除，其实只是擦除<code>Code 属性</code>中的泛型信息，在类常量池属性中其实还保留着泛型信息，这也是在运行时可以反射获取泛型信息的根本依据。在这篇文章里，我们详细讨论：<a href="https://www.jianshu.com/p/9da8ad003f37" target="_blank">《Java | 关于泛型能问的都在这里了（含Kotlin）》</a>，请关注！</p>
<hr>
<p><strong>RuntimeVisibleAnnotations 属性</strong><br>
<strong>RuntimeInvisibleAnnotations 属性</strong><br>
<strong>RuntimeVisibleParameterAnnotations 属性</strong><br>
<strong>RuntimeInvisibleParameterAnnotations 属性</strong></p>
<p>注解在编译后擦除，如果注解的保留级别为<code>CLASS & RUNTIME</code>，在 Class 文件中还会生成对应的注解属性。在这篇文章里，我们详细讨论：<a href="https://www.jianshu.com/p/5871e1186840" target="_blank">《Java | 这是一篇全面的注解使用攻略（含 Kotlin）》</a>，请关注！</p>
<hr>
<h6>InnerClasses 属性</h6>
<ul>
<li>请阅读：<a href="https://www.jianshu.com/p/993206508d35" target="_blank">《Java | 为什么非静态内部类会持有外部类的引用》</a>
</li>
</ul>
<h2>8. 信息描述规则</h2>
<p>Editting...</p>
<hr>
<h4>参考资料</h4>
<ul>
<li>《深入理解Java虚拟机（第3版本）》（第6章）—— 周志明 著</li>
<li>《深入理解Android：Java虚拟机 ART》（第2章） —— 邓凡平 著</li>
<li>《深入理解 JVM 字节码》（第2、3、4章）—— 张亚 著</li>
</ul>
<hr>
<blockquote>
<p><strong>创作不易，你的「三连」是丑丑最大的动力，我们下次见！</strong></p>
</blockquote>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1120" data-height="630"><img data-original-src="//upload-images.jianshu.io/upload_images/10107787-8a6d3a74f22bec02.png" data-original-width="1120" data-original-height="630" data-original-format="image/png" data-original-filesize="1335756" src="https://upload-images.jianshu.io/upload_images/10107787-8a6d3a74f22bec02.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
  
</div>
            