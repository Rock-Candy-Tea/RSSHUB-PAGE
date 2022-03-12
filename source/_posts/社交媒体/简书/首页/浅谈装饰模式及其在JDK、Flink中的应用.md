
---
title: '浅谈装饰模式及其在JDK、Flink中的应用'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/195230-71fe2faba82085bc.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/195230-71fe2faba82085bc.png'
---

<div>   
<h3>前言</h3>
<p>上周末在家翻看之前写的部分文章，发现在设计模式方面甚少涉猎。在阅读开源项目源码的过程中，我们经常会接触到各种设计模式，深入理解它们无疑大有裨益，能够帮助我们快速get到那些masterminds背后的思想。今天就来谈一谈应用较为广泛的<strong>装饰模式</strong>。</p>
<h3>装饰模式与四要素</h3>
<p>装饰模式属于GoF设计模式分类中的结构型模式。</p>
<blockquote>
<p>所谓装饰模式（decorator pattern），就是在<strong>不改变原有类，也不影响其他继承自该类的子类的行为</strong>的基础上，为原有类在<strong>运行期动态地添加新行为</strong>的模式。(Attach additional responsibilities to an object dynamically)</p>
</blockquote>
<p>我们知道，类继承是为类扩充功能的一般方案。而<strong>装饰模式作为类继承的替代方案存在</strong>(Decorators provide a flexible alternative to subclassing for extending functionality)，其意义在于：</p>
<blockquote>
<p>类继承扩充的功能在编译期就被确定，而装饰模式扩充的功能可以在运行时由调用方确定。如果要为类同时扩充多个<strong>相互独立而又可以组合</strong>的功能，采用类继承方案就意味着为每种组合创建新的类，容易造成子类泛滥。装饰模式就可以灵活地按需组合（就像现实中的小装饰品可以随意摆放一样），更加简洁且易于修改。</p>
</blockquote>
<p>下面的UML类图示出实现装饰模式的四要素。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1182" data-height="924"><img data-original-src="//upload-images.jianshu.io/upload_images/195230-71fe2faba82085bc.png" data-original-width="1182" data-original-height="924" data-original-format="image/png" data-original-filesize="264440" src="https://upload-images.jianshu.io/upload_images/195230-71fe2faba82085bc.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<blockquote>
<ul>
<li>构件（Component）：接口，用于定义整个实体空间的最基础的行为规范；</li>
<li>构件实体（ConcreteComponent）：实现Component的实体类，本身具有一些功能，同时也是被装饰（被扩充）的类；</li>
<li>装饰器（Decorator）：实现Component的类，其中维护一个ConcreteComponent的实例，具体的装饰功能由其子类实现；</li>
<li>装饰器实体（ConcreteDecorator）：继承Decorator并实现具体的装饰功能。</li>
</ul>
</blockquote>
<p>通过下面两句话即可使用装饰器实体ConcreteDecorator实现的扩充功能：</p>
<pre><code class="java">Component component = new ConcreteDecorator(new ConcreteComponent());
component.operation();
</code></pre>
<p>可见，调用方只需要额外调用装饰器实体的构造函数，而不必关心Component/ConcreteComponent在装饰之后的变化。不过由上也可以看出，装饰模式会new出更多的对象，当装饰器实体的链比较长时会有性能问题，并且出现问题时也不利于debug。</p>
<p>上面所有内容讲的装饰模式叫做<strong>透明装饰模式</strong>，即用户总可以只用Component来调用所有功能。相对地，还有一种<strong>半透明装饰模式</strong>，即装饰器实体中允许存在Component中不存在的新方法（如someNewBehavior()），调用方式相应就变成：</p>
<pre><code class="java">ConcreteDecorator component = new ConcreteDecorator(new ConcreteComponent());
component.someNewBehavior();
</code></pre>
<p>由于扩充功能可以在新方法中定义，半透明装饰模式更加灵活，但是就无法对用户屏蔽ConcreteDecorator存在的现实了。更重要的是，<strong>半透明装饰模式下对实例进行多次（链式）装饰是没有意义的</strong>，因为只能调用最后一次装饰时装饰器实体的新增方法。</p>
<p>干说了这么多，举两个示例来帮助理解吧。</p>
<h3>Java I/O中的装饰模式</h3>
<p>装饰模式在java.io包中广泛使用，包括基于字节流的InputStream/OutputStream和基于字符的Reader/Writer体系。以下以InputStream为例。</p>
<p>InputStream是所有字节输入流的基类，其下有众多子类，如基于文件的FileInputStream、基于对象的ObjectInputStream、基于字节数组的ByteArrayInputStream等。有些时候，我们想为这些流加一些其他的小特性，如缓冲、压缩等，用装饰模式实现就非常方便。相关的部分类图如下所示。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1850" data-height="562"><img data-original-src="//upload-images.jianshu.io/upload_images/195230-57b48e7318132d76.png" data-original-width="1850" data-original-height="562" data-original-format="image/png" data-original-filesize="56968" src="https://upload-images.jianshu.io/upload_images/195230-57b48e7318132d76.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>这个类图很标准，其中：</p>
<ul>
<li>构件是InputStream；</li>
<li>构件实体是FileInputStream、ObjectInputStream等等；</li>
<li>装饰器是FilterInputStream；</li>
<li>装饰器实体是FilterInputStream的所有子类。</li>
</ul>
<p>观察一下装饰器FilterInputStream的开头，可以发现它持有InputStream的引用，并且实现了InputStream中的所有方法（实际上就是简单地代理了一下）。具体的装饰器实体就继承FilterInputStream，并实现对应的扩充功能。如下图所示。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="840" data-height="1502"><img data-original-src="//upload-images.jianshu.io/upload_images/195230-3b1cc8db995d14c3.png" data-original-width="840" data-original-height="1502" data-original-format="image/png" data-original-filesize="147999" src="https://upload-images.jianshu.io/upload_images/195230-3b1cc8db995d14c3.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>以下就可以用BufferedInputStream和GZIPInputStream创建一个带缓冲、压缩的文件输入流。</p>
<pre><code class="java">InputStream is = new GZIPInputStream(new BufferedInputStream(new FileInputStream("test.txt")));
</code></pre>
<p>当然，如果我们想要自己实现一个InputStream的装饰器实例，创建一个FilterInputStream的子类即可，就不再举例了。</p>
<h3>Flink State TTL中的装饰模式</h3>
<p>笔者之前写过一篇文章<a href="https://www.jianshu.com/p/7ee464c40b04" target="_blank">《简析Flink状态生存时间（State TTL）机制的底层实现》</a>，这里就用到了装饰模式，但不像Java I/O那样标准。</p>
<p>为状态增加TTL的特性可以直接在原始状态之上实现，因此符合装饰模式的场景。Flink引入了一个AbstractTtlDecorator<T>抽象类作为装饰器，负责为状态类型T装饰上与TTL相关的基本逻辑。相关的部分类图如下所示。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1226" data-height="602"><img data-original-src="//upload-images.jianshu.io/upload_images/195230-66d7ea8f636a99dd.png" data-original-width="1226" data-original-height="602" data-original-format="image/png" data-original-filesize="54072" src="https://upload-images.jianshu.io/upload_images/195230-66d7ea8f636a99dd.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>可见，虽然AbstractTtlDecorator并未持有State的实例（只有State的类型参数），但是在其子类AbstractTtlState中，通过持有TTL状态上下文TTLStateContext间接地得到了State实例。例如，由AbstractTtlState派生出来的TtlMapState直接在原来的MapState上进行增删改查操作，只是附带上了AbstractTtlDecorator和AbstractTtlState提供的TTL逻辑而已。其他的TtlListState等也是同理。具体的代码可参见前面给的传送门，这里不再重复贴了。</p>
<p>虽然这种模式的类结构并不典型，但是也完全契合装饰模式的精神，Ttl*State对用户也是透明的。有很多开源框架都采用了这种相对松散的装饰模式，有时会被称为包装（Wrapper）模式。</p>
<h3>The End</h3>
<p>明天高考，各位小盆友加油加油。</p>
<p>民那晚安晚安。</p>
  
</div>
            