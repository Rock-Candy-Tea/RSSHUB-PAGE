
---
title: 'iOS KVO底层实现原理 （一）'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb61ea80111a4951b8363aec51a8306a~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 09 Jul 2021 04:03:36 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb61ea80111a4951b8363aec51a8306a~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">iOS KVO底层实现原理 （一）</h3>
<ul>
<li>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F93859511%23KVO_1" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/93859511#KVO_1" ref="nofollow noopener noreferrer">一，KVO简述</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F93859511%23KVC__28" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/93859511#KVC__28" ref="nofollow noopener noreferrer">二，KVC 简述</a></li>
<li>
<ul>
<li>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F93859511%231_KVC_30" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/93859511#1_KVC_30" ref="nofollow noopener noreferrer">1. KVC定义</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F93859511%232__46" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/93859511#2__46" ref="nofollow noopener noreferrer">2. 方法调用</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F93859511%233_KVC_91" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/93859511#3_KVC_91" ref="nofollow noopener noreferrer">3. KVC准则</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F93859511%23KVO_100" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/93859511#KVO_100" ref="nofollow noopener noreferrer">三，KVO实现原</a><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F93859511%23KVO_100" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/93859511#KVO_100" ref="nofollow noopener noreferrer">理探索</a></li>
<li>
<ul>
<li>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F93859511%231_KVO_135" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/93859511#1_KVO_135" ref="nofollow noopener noreferrer">1. 探寻KVO底层实现原理</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F93859511%232_KVO_140" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/93859511#2_KVO_140" ref="nofollow noopener noreferrer">2. KVO底层实现分析</a></li>
</ul>
</li>
</ul>
</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F93859511%23KVO_279" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/93859511#KVO_279" ref="nofollow noopener noreferrer">四，KVO底层原理</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F93859511%23KVO_409" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/93859511#KVO_409" ref="nofollow noopener noreferrer">五，KVO底层实现代码</a></li>
<li>
<ul>
<li>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F93859511%231_KVO_411" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/93859511#1_KVO_411" ref="nofollow noopener noreferrer">1. 通过代码来自己实现KVO监听</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F93859511%232__runtime__668" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/93859511#2__runtime__668" ref="nofollow noopener noreferrer">2. 通过 runtime 动态创建子类方式去实现</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<h2 data-id="heading-1">一，KVO简述</h2>
<p>KVO的全称 Key-Value Observing，俗称“键值监听”，可以用于监听某个对象属性值的改变。<br>
带着问题探索：</p>
<p>1.iOS用什么方式实现对一个对象的KVO？（KVO的本质是什么？）</p>
<pre><code class="copyable">答. 当一个对象使用了KVO监听，iOS系统会修改这个对象的isa指针，
改为指向一个全新的通过Runtime动态创建的子类，子类拥有自己的set方法实现，
set方法实现内部会顺序调用willChangeValueForKey方法、原来的setter方法实现、
didChangeValueForKey方法，而didChangeValueForKey方法内部
又会调用监听器的observeValueForKeyPath:ofObject:change:context:监听方法。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.如何手动触发KVO</p>
<pre><code class="copyable">答. 被监听的属性的值被修改时，就会自动触发KVO。
如果想要手动触发KVO，则需要我们自己调用willChangeValueForKey和
didChangeValueForKey方法即可在不改变属性值的情况下手动触发KVO
，并且这两个方法缺一不可。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.KVO 底层实现是什么?<br>
4.修改成员变量的值会出发 KVO 吗?<br>
5.KVC 赋值会出发 KVO 吗?<br>
6.</p>
<h2 data-id="heading-2">二，KVC 简述</h2>
<h4 data-id="heading-3">1. KVC定义</h4>
<p>KVC: Key-value coding is a mechanism for indirectly accessing anobject’s attributes and relationships using string identifiers. 所谓键值编码，并不是访问器方法的启动和实例变量的访问这种直接的方式，而是使用表示属性的字符串来间接访问对象属性值的一种结构。 </p>
<p>只要存在访问器方法、声明属性或实例变量，就可以将其名字指定为字符串来访问。</p>
<p>之所以说键值编码的访问是接的：</p>
<ol>
<li>
<p>可以在运行中确定作为键的字符串</p>
</li>
<li>
<p>使用者无法知道实际访问属性的方法</p>
</li>
</ol>
<p>键值编码必需的方法在非正式协议NSKeyValueCoding中声明（头文件Foundation/NSKeyValueCoding.h）。默认在NSObject中实现。</p>
<h4 data-id="heading-4">2. 方法调用</h4>
<p>下面就以下两个方法的调用进行说明：</p>
<pre><code class="copyable"> (id)  valueForKey: (NSString *) key
<span class="copy-code-btn">复制代码</span></code></pre>
<p>返回表示属性的键字符串所对应的值。如果不能取得值，则将引起接收器调用方法valueForUndefinedKey:。</p>
<pre><code class="copyable"> (void)setValue: (id) value  forKey: (NSString*) key
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将键字符串key所对应的属性的值设置为value。不能设定属性时，将引起接收器调用方法setValue:ForUndefinedKey:。 执行时，有访问器的属性会使用访问器，没有访问器的属性也可以设定值和访问。因为上面两个方法均为实例方法，可以在方法体内访问实例变量。  </p>
<p>访问过程如下：</p>
<ol>
<li>
<p>接收器中如果有key访问器（或getKey、isKey、_key、_getKey、setKey）则</p>
</li>
<li>
<p>使用它。</p>
</li>
<li>
<p>没有访问器时，使用接收器的类方法accessInstanceVariablesDirectly来查询。返回YES时，如果存在实例变量key（或_key、isKey、_isKey等）则返回或设置其值。使用引用计数管理方式时，实例变量如果为对象，则旧值会被自动释放，新值被保存并</p>
</li>
<li>
<p>代入。</p>
</li>
</ol>
<ul>
<li>
<p>(BOOL)accessInstanceVariablesDirectly</p>
<p>通常定义为返回YES，可以在子类中改变。该类方法返回YES时，使用键值编码可以访问该类的实例变量。返回NO时不可以访问。只要该方法返回YES，实例变量的可视属性即使有@private修饰，也可以</p>
</li>
<li>
<p>访问。</p>
</li>
</ul>
<ol>
<li>
<p>既没有访问器也没有实例变量时，将引起接收器调用方法valueForUndefinedKey:或setValue:forUndefinedKey:。</p>
<p>(id) valueForUndefinedKey: (NSStirng *) key</p>
</li>
</ol>
<p> 不能取得键字符串对应的值时，从方法valueForKey：中调用该方法。默认情况下，该方法的执行会触发NSUndefinedKeyException。不过，通过在子类中修改定义，就可以返回其他对象。</p>
<pre><code class="copyable">  (void) setValue: (id) value  forUndefinedKey: (NSString *) key
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不能设置键字符串key对应的属性值时，从方法setValue:forKey中调用该方法。默认情况下，该方法的执行会触发异常NSUndefinedKeyException。不过，通过在子类中修改定义，可以返回其他对象。</p>
<ol>
<li>如果该返回值不是对象，则返回被适当的对象包装的值；设置值时也应先包装成相应的对象。</li>
</ol>
<p>属性为对象时，该对象还可能持有属性。这时候可以用“.”连接表示键的字符串，这种表示方式称为键路径。只要能找到对象，点和键多长都没有关系。</p>
<pre><code class="copyable"> (id) valueForKeyPath:(NSString *) keyPath
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以点切分键路径，并使用第一个键向接收器发送valueForKey：方法。然后，再使用键路径的下一个键，向得到的对象发送valueForKey：方法，如此反复操作，返回最后获得的对象。</p>
<pre><code class="copyable"> (void)setValue: (id) value  forKeyPath:(NSString *) keyPath
<span class="copy-code-btn">复制代码</span></code></pre>
<p>与valueForKeyPath：方法一样取出对象，这里只对路径中的最后一个键调用setValue：forKey：方法，并设定属性值为value。</p>
<h4 data-id="heading-5">3. KVC准则</h4>
<ol>
<li>
<p>随访问器方法而改变。</p>
</li>
<li>
<p>使用setValue：forKey：和键进行改变。此时也可能不经由访问</p>
</li>
<li>
<p>器。</p>
</li>
<li>
<p>使用setValue：forKeyPath：和键路径进行改变。此时也可能不经由访问器。不仅仅是最终的监视对象的属性，当路径中的属性发生变化时，也会被通知。</p>
</li>
</ol>
<h2 data-id="heading-6">三，KVO实现原理探索</h2>
<ol>
<li>
<p>首先需要了解KVO基本使用，KVO的全称 Key-Value Observing，俗称“键值监听”，可以用于监听某个对象属性值的改变。KVO：key-value observing,是在KVC基础上实现的，当某个对象的属性发生改变时，通知其它对象的机制。仅仅在以KVC准则来访问访问器或实例变量的情况下，才可以监视属性的变化。在方法内直接改变实例变量的值时，就不能监视了。</p>
<ul>
<li>
<p>(void)viewDidLoad &#123;
[super viewDidLoad];
Person *p1 = [[Person alloc] init];
Person *p2 = [[Person alloc] init];
p1.age = 1;
p1.age = 2;
p2.age = 2;
// self 监听 p1的 age属性
NSKeyValueObservingOptions options = NSKeyValueObservingOptionNew | NSKeyValueObservingOptionOld;</p>
<p>[p1 addObserver:self forKeyPath:@"age" options:options context:nil];
p1.age = 10;
[p1 removeObserver:self forKeyPath:@"age"];</p>
</li>
</ul>
<p>&#125;</p>
<ul>
<li>(void)observeValueForKeyPath:(NSString *)keyPath ofObject:(id)object change:(NSDictionary<NSKeyValueChangeKey,id> *)change context:(void *)context</li>
</ul>
<p>&#123;
NSLog(@"监听到%@的%@改变了%@", object, keyPath,change);
&#125;</p>
<p>// 打印内容
监听到<Person: 0x604000205460>的age改变了&#123;
kind = 1;
new = 10;
old = 2;
&#125;</p>
</li>
</ol>
<p>上述代码中可以看出，在添加监听之后，age属性的值在发生改变时，就会通知到监听者，执行监听者的observeValueForKeyPath方法。</p>
<h4 data-id="heading-7">1. 探寻KVO底层实现原理</h4>
<p>通过上述代码我们发现，一旦age属性的值发生改变时，就会通知到监听者，并且我们知道赋值操作都是调用 set方法，我们可以来到Person类中重写age的set方法，观察是否是KVO在set方法内部做了一些操作来通知监听者。 我们发现即使重写了set方法，p1对象和p2对象调用同样的set方法，但是我们发现p1除了调用set方法之外还会另外执行监听器的observeValueForKeyPath方法。 说明KVO在运行时获取对p1对象做了一些改变。相当于在程序运行过程中，对p1对象做了一些变化，使得p1对象在调用setage方法的时候可能做了一些额外的操作，所以问题出在对象身上，两个对象在内存中肯定不一样，两个对象可能本质上并不一样。接下来来探索KVO内部是怎么实现的。</p>
<h4 data-id="heading-8">2. KVO底层实现分析</h4>
<ul>
<li>首先我们对上述代码中添加监听的地方打断点，看观察一下，addObserver方法对p1对象做了什么处理？也就是说p1对象在经过addObserver方法之后发生了什么改变，我们通过打印isa指针如下图所示</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb61ea80111a4951b8363aec51a8306a~tplv-k3u1fbpfcp-zoom-1.image" alt="addObserver对p1对象的处理" loading="lazy" referrerpolicy="no-referrer"><br>
通过上图我们发现，p1对象执行过addObserver操作之后，p1对象的isa指针由之前的指向类对象Person变为指向NSKVONotifyin_Person类对象，而p2对象没有任何改变。也就是说一旦p1对象添加了KVO监听以后，其isa指针就会发生变化，因此set方法的执行效果就不一样了。</p>
<p>那么我们先来观察p2对象在内容中是如何存储的，然后对比p2来观察p1。<br>
首先我们知道，p2在调用setage方法的时候，首先会通过p2对象中的isa指针找到Person类对象，然后在类对象中找到setage方法。然后找到方法对应的实现。如下图所示</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1fc1df83c4164782be996b89ffcb2192~tplv-k3u1fbpfcp-zoom-1.image" alt="未使用KVO监听的对象放大实现路径" loading="lazy" referrerpolicy="no-referrer"><br>
但是刚才我们发现p1对象的isa指针在经过KVO监听之后已经指向了NSKVONotifyin_Person类对象，NSKVONotifyin_Person其实是Person的子类，那么也就是说其superclass指针是指向Person类对象的，NSKVONotifyin_Person是runtime在运行时生成的。那么p1对象在调用setage方法的时候，肯定会根据p1的isa找到NSKVONotifyin_Person，在NSKVONotifyin_Person中找setage的方法及实现。</p>
<p>经过查阅资料我们可以了解到。<br>
NSKVONotifyin_Person中的setage方法中其实调用了 Fundation框架中C语言函数 _NSsetIntValueAndNotify，_NSsetIntValueAndNotify内部做的操作相当于，首先调用willChangeValueForKey 将要改变方法，之后调用父类的setage方法对成员变量赋值，最后调用didChangeValueForKey已经改变方法。didChangeValueForKey中会调用监听器的监听方法，最终来到监听者的observeValueForKeyPath方法中。</p>
<ul>
<li>那么如何验证KVO真的如上面所讲的方式实现？</li>
</ul>
<p>首先经过之前打断点打印isa指针，我们已经验证了，在执行添加监听的方法时，会将isa指针指向一个通过runtime创建的Person的子类NSKVONotifyin_Person。</p>
<p>另外我们可以通过打印方法实现的地址来看一下p1和p2的setage的方法实现的地址在添加KVO前后有什么变化。</p>
<pre><code class="copyable">// 通过methodForSelector找到方法实现的地址
NSLog(@"添加KVO监听之前 - p1 = %p, p2 = %p", [p1 methodForSelector: @selector(setAge:)],[p2 methodForSelector: @selector(setAge:)]);
    
NSKeyValueObservingOptions options = NSKeyValueObservingOptionNew | NSKeyValueObservingOptionOld;
[p1 addObserver:self forKeyPath:@"age" options:options context:nil];

NSLog(@"添加KVO监听之后 - p1 = %p, p2 = %p", [p1 methodForSelector: @selector(setAge:)],[p2 methodForSelector: @selector(setAge:)]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2159fdcdec004704a40ef12058714b1a~tplv-k3u1fbpfcp-zoom-1.image" alt="setage的方法实现的地址在添加KVO前后的变化" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们发现在添加KVO监听之前，p1和p2的setAge方法实现的地址相同，而经过KVO监听之后，p1的setAge方法实现的地址发生了变化，我们通过打印方法实现来看一下前后的变化发现，确实如我们上面所讲的一样，p1的setAge方法的实现由Person类方法中的setAge方法转换为了C语言的Foundation框架的_NSsetIntValueAndNotify函数。</p>
<p>Foundation框架中会根据属性的类型，调用不同的方法。例如我们之前定义的int类型的age属性，那么我们看到Foundation框架中调用的_NSsetIntValueAndNotify函数。那么我们把age的属性类型变为double重新打印一遍</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f97b934747c456eacce82523ff7c92d~tplv-k3u1fbpfcp-zoom-1.image" alt="_NSSetDoubleValueAndNotify函数" loading="lazy" referrerpolicy="no-referrer"><br>
我们发现调用的函数变为了_NSSetDoubleValueAndNotify，那么这说明Foundation框架中有许多此类型的函数，通过属性的不同类型调用不同的函数。 那么我们可以推测Foundation框架中还有很多例如_NSSetBoolValueAndNotify、_NSSetCharValueAndNotify、_NSSetFloatValueAndNotify、_NSSetLongValueAndNotify等等函数。 我们可以找到Foundation框架文件，通过命令行查询关键字找到相关函数 </p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cbef75738ecd428da7a9ac9c40c6a982~tplv-k3u1fbpfcp-zoom-1.image" alt="相关函数" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>NSKVONotifyin_Person内部结构是怎样的？</li>
</ul>
<p>首先我们知道，NSKVONotifyin_Person作为Person的子类，其superclass指针指向Person类，并且NSKVONotifyin_Person内部一定对setAge方法做了单独的实现，那么NSKVONotifyin_Person同Person类的差别可能就在于其内存储的对象方法及实现不同。</p>
<p>我们通过runtime分别打印Person类对象和NSKVONotifyin_Person类对象内存储的对象方法</p>
<pre><code class="copyable">- (void)viewDidLoad &#123;
    [super viewDidLoad];

    Person *p1 = [[Person alloc] init];
    p1.age = 1.0;
    Person *p2 = [[Person alloc] init];
    p1.age = 2.0;
    // self 监听 p1的 age属性
    NSKeyValueObservingOptions options = NSKeyValueObservingOptionNew | NSKeyValueObservingOptionOld;
    [p1 addObserver:self forKeyPath:@"age" options:options context:nil];

    [self printMethods: object_getClass(p2)];
    [self printMethods: object_getClass(p1)];

    [p1 removeObserver:self forKeyPath:@"age"];
&#125;

- (void) printMethods:(Class)cls
&#123;
    unsigned int count ;
    Method *methods = class_copyMethodList(cls, &count);
    NSMutableString *methodNames = [NSMutableString string];
    [methodNames appendFormat:@"%@ - ", cls];
    
    for (int i = 0 ; i < count; i++) &#123;
        Method method = methods[i];
        NSString *methodName  = NSStringFromSelector(method_getName(method));
        
        [methodNames appendString: methodName];
        [methodNames appendString:@" "];
        
    &#125;
    
    NSLog(@"%@",methodNames);
    free(methods);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述打印内容如下:</p>
<p>通过上述代码我们发现NSKVONotifyin_Person中有4个对象方法。分别为setAge: class dealloc _isKVOA，那么至此我们可以画出NSKVONotifyin_Person的内存结构以及方法调用顺序。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b2326105ff34b469a0dd5246ca6f296~tplv-k3u1fbpfcp-zoom-1.image" alt="NSKVONotifyin_Person的内存结构以及方法调用顺序" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里NSKVONotifyin_Person重写class方法是为了隐藏NSKVONotifyin_Person。不被外界所看到。我们在p1添加过KVO监听之后，分别打印p1和p2对象的class可以发现他们都返回Person。</p>
<pre><code class="copyable">NSLog(@"%@,%@",[p1 class],[p2 class]);
// 打印结果 Person,Person
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果NSKVONotifyin_Person不重写class方法，那么当对象要调用class对象方法的时候就会一直向上找来到nsobject，而nsobect的class的实现大致为返回自己isa指向的类，返回p1的isa指向的类那么打印出来的类就是NSKVONotifyin_Person，但是apple不希望将NSKVONotifyin_Person类暴露出来，并且不希望我们知道NSKVONotifyin_Person内部实现，所以在内部重写了class类，直接返回Person类，所以外界在调用p1的class对象方法时，是Person类。这样p1给外界的感觉p1还是Person类，并不知道NSKVONotifyin_Person子类的存在。</p>
<p>那么我们可以猜测NSKVONotifyin_Person内重写的class内部实现大致为:</p>
<pre><code class="copyable">- (Class) class &#123;
     // 得到类对象，在找到类对象父类
     return class_getSuperclass(object_getClass(self));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>验证didChangeValueForKey:内部会调用observer的observeValueForKeyPath:ofObject:change:context:方法.</li>
</ul>
<p>我们在Person类中重写willChangeValueForKey:和didChangeValueForKey:方法，模拟他们的实现。</p>
<pre><code class="copyable">- (void)setAge:(int)age
&#123;
    NSLog(@"setAge:");
    _age = age;
&#125;
- (void)willChangeValueForKey:(NSString *)key
&#123;
    NSLog(@"willChangeValueForKey: - begin");
    [super willChangeValueForKey:key];
    NSLog(@"willChangeValueForKey: - end");
&#125;
- (void)didChangeValueForKey:(NSString *)key
&#123;
    NSLog(@"didChangeValueForKey: - begin");
    [super didChangeValueForKey:key];
    NSLog(@"didChangeValueForKey: - end");
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再次运行来查看didChangeValueForKey的方法内运行过程，通过打印内容可以看到，确实在didChangeValueForKey方法内部已经调用了observer的observeValueForKeyPath:ofObject:change:context:方法。<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/377d87cf5d7b40ee869df9c3566802a0~tplv-k3u1fbpfcp-zoom-1.image" alt="didChangeValueForKey内运行顺序" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">四，KVO底层原理</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19daf5f27406470f915f6739832e56c9~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>首先创建一个 Person 类 内部有个 name 属性,然后 创建p1 和 p2两个实例对象,其中p1添加了kvo监听,p2没有添加 kvo 监听,然后重写了 observeValueForKeyPath 方法 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fxn--person-9n6jx20u.name%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://xn--person-9n6jx20u.name/" ref="nofollow noopener noreferrer">监听Person.name</a> 属性发生改变时候的通知.</li>
</ol>
<p> 从本质上来看 Person 给name赋值的时候 调用的是 setName 方法 ,无论 p1还是p2 调用的 setter 方法都是一样的,为什么 p1改变 name 属性值就能有通知, p2确没有,调用的 都是同一个 setName:(NSString *)name 方法,区别怎么那么大?</p>
<ol>
<li>接下来打印下p1和p2的内存地址 看看p1和p2内存地址能不能一探究竟.</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9362aa89db4441678c089f779ee3945e~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>
<p>从 p1</p>
</li>
<li>
<p>和 p2内存地址上也看不出来什么东东.接着打印 p1和 p2 的 class 信息<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c55d911aa8ee42b386fc78d39f122ba8~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>打印 o</p>
</li>
<li>
<p>bject_getClass 试试看，我们都知道object_getClass(id) 才会返回这个实例对象的真实 class 类型<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/705adc4740be480c94a19bce393df083~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>打印 s</p>
</li>
<li>
<p>etName 方法实现IMP指针有没有发生改变,我们知道同一个方法的实现 IMP 地址是不变的.<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0164f1281e948d2b2c783c994a9d45b~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>这里连 setName方法都不一样了 , 为了一探究竟 对上边的 NSKVONotifying_Person 和 添加 KVO 之后的 imp 指针进行进一步研</p>
</li>
<li>
<p>究.</p>
</li>
</ol>
<ul>
<li>首先 在 lldb 上输入 imp1和 imp2<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0213c3cd7f4d4a138219dacce2003b3a~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"><br>
发生了 imp1 方法实现在 Foundation 框架里的 _NSSetObjectValueAndNotify 函数中 ,而 imp2 则调用了 Person setName 方法<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf2aea0c100e4cab92da7ecce41e7ced~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"><br>
也就是说添加了 KVO 之后 p1 修改 name 值之后 不再调用 Person 的 setName方法 ,而 p2没有添加 kvo 监听 依然正常调用 setName:方法 ,由此可以得出 p1 添加完 KVO 监听后 系统修改了默认方法实现,那么既然没有调用 setName: 方法 为什</li>
<li>么 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fp1.name%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://p1.name/" ref="nofollow noopener noreferrer">p1.name</a>的值也发生了改变?</li>
</ul>
<ol>
<li>接下来我们准备对刚才 NSKVONotifying_Person 类进行下一步研究, NSKVONotifying_Person 和 Person 有没有内在的联系呢? 研究一下NSKVONotifying_Person和 Person 之间的联系时什么？<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/043d470a6bc34131818768521ffee309~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"><br>
通过打印 NSKVONotifying_Person 的 superclass 和 Person 的 superclass 可以得出, NSKVONotifying_Person是一个 Person 子类,那么为什么苹果会动态创建这么一个 子类呢? NSKVONotifying_Person 这个子类 跟 Person 内部有哪些不</li>
<li>同呢 ?</li>
</ol>
<p>这个时候 我们去输出下 Person 和 NSKVONotifying_Person 内部的方法列表 和 属性列表 ,看看NSKVONotifying_Person 子类都添加了那些方法和属性.</p>
<pre><code class="copyable">- (void)viewDidLoad &#123;
    [super viewDidLoad];

    
    Person *p1 = [[Person alloc] init];
    Person *p2 = [[Person alloc] init];
    
    id cls1 = object_getClass(p1);
    id cls2 = object_getClass(p2);
    NSLog(@"添加 KVO 之前: cls1 = %@  cls2 = %@ ",cls1,cls2);
    
    [p1 addObserver:self forKeyPath:@"name" options:NSKeyValueObservingOptionNew context:NULL];
     cls1 = object_getClass(p1);
     cls2 = object_getClass(p2);
    
    
    NSString *methodList1 = [self printPersonMethods:cls1];
    NSString *methodList2 = [self printPersonMethods:cls2];

    NSLog(@"%@",methodList1);
    NSLog(@"%@",methodList2);

    
//  NSLog(@"添加 KVO 之后: cls1 = %@  cls2 = %@ ",cls1,cls2);
    
//  id super_cls1 = class_getSuperclass(cls1);
//  id super_cls2 = class_getSuperclass(cls2);
//
//  NSLog(@"super_cls1 = %@ ,super_cls2 = %@",super_cls1,super_cls2);
//
//  p1.name = @"dzb";
//  p2.name = @"123";

&#125;

- (NSString *) printPersonMethods:(id)obj &#123;
    
    unsigned int count = 0;
    Method *methods = class_copyMethodList([obj class],&count);
    NSMutableString *methodList = [NSMutableString string];
    [methodList appendString:@"[\n"];
    for (int i = 0; i<count; i++) &#123;
        Method method = methods[i];
        SEL sel = method_getName(method);
        [methodList appendFormat:@"%@",NSStringFromSelector(sel)];
        [methodList appendString:@"\n"];
    &#125;
    
    [methodList appendFormat:@"]"];
    
    free(methods);
    
    return methodList;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出结果如下：<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67ea92f49ee44c94ab287438a5f81e0c~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"><br>
从输出结果可以看出来 NSKVONotifying_Person 内部也有一个 setName:方法 还重写了 class 和 dealloc 方法 , _isKVOA, 那么我们可以大致的得出, p1添加 kVO 后 runtime 动态的生成了一个 NSKVONotifying_Person子类 并重写了 setName 方法 ,那么 setName 内部一定是做了一些事情,才会触发 observeValueForKeyPath 监听方法.</p>
<ol>
<li>继续探究 NSKVONotifying_Person 子类 重写 setName 都做了什么?<br>
其实 setName 方法内部 是调用了 Foundation 的 _NSSetObjectValueAndNotify 函数 ,在</li>
<li>_NSSetObjectValueAndNotify 内部：</li>
</ol>
<ul>
<li>
<ol>
<li>首先会调用 willChangeValueForKey</li>
</ol>
</li>
<li>
<ol>
<li>然后给 name 属性赋</li>
<li>
<ol>
<li>值</li>
</ol>
</li>
<li>
<ol>
<li>最后调用 didChangeValueForKey</li>
</ol>
</li>
<li>
<ol>
<li>最后调用 observer 的 observeValueForKeyPath 去告诉监听器属性值发生了改变 .</li>
</ol>
</li>
</ol>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1691f9cbcb9942bf82112ccbb25e9b27~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li>由于苹果 Foundation 框架是不</li>
<li>开源的 ,所以我们依然可以通过重写Person 的 willChangeValueForKey 和 didChangeValueForKey 验证我们的猜想 .<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/65bd3a15415049feb189ac84ff3c1ffa~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></li>
</ol>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fxn--p1-2f3cm3g0re1uxoqezqh4o6k.name%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://xn--p1-2f3cm3g0re1uxoqezqh4o6k.name/" ref="nofollow noopener noreferrer">首先</a><a href="https://link.juejin.cn/?target=http%3A%2F%2Fxn--p1-2f3cm3g0re1uxoqezqh4o6k.name%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://xn--p1-2f3cm3g0re1uxoqezqh4o6k.name/" ref="nofollow noopener noreferrer">当我们改变p1.name</a> 的值时 并不是首先执行的 setName: 这个方法 ,而是先调用了 willChangeValueForKey 其次 调用父类的 setter 方法 对属性赋值 ,然后再调用 didChangeValueForKey 方法 ,并在</p>
<p> didChangeValueForKey 内部 调用监听器的 observeValueForKeyPath方法 告诉外界 属性值发生了改变.</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff57a3b7a1774ebeb672ea2339279476~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fabf6d26387c4e8ebb2aed8f5d4c6fcd~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>至于重写了 dealloc 和 class 方法 是为了做一些 KVO 释放内存 和 隐藏外界对于 NSKVONotifying_Person 子类的存在</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/466326ca440e4687a4702cad17d1cf35~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>10.这就是我们调用 [p1 class] 和 [p2 class]结果都显示 Person 类 ,让我们误以为 Person 没有发生变化</p>
<ul>
<li>KVC 对属性赋值时候 是会在这个类里边 去查找 _age isAge setAge setIsAge 等方法的 ,最终会调用属性的 setter 方法 ,那么如果添加了 KVO 还是会被触发的 .<br>
相反 设置成员变量 _age 由于不会触发 setter 方法 ,因此不会去触发 KVO 相关的代码 .</li>
</ul>
<h2 data-id="heading-10">五，KVO底层实现代码</h2>
<h4 data-id="heading-11">1. 通过代码来自己实现KVO监听</h4>
<ol>
<li>
<p>ViewController调用实现</p>
<p>#import "ViewController.h"
#import "Person.h"
#import "NSObject+KCKVO.h"
#import "Dog.h"</p>
<p>@interface ViewController ()
@property (nonatomic, strong) Person *p;
@end</p>
<p>// 分类
@implementation ViewController</p>
<ul>
<li>
<p>(void)viewDidLoad &#123;
[super viewDidLoad];</p>
<p>self.p = [[Person alloc] init];
[self.p lg_addObserver:self forKeyPath:@"name"];
self.p.name  = @"kongyulu";</p>
</li>
</ul>
<p>&#125;</p>
<p>#pragma mark - value 回调</p>
<ul>
<li>(void)lg_observeValueForKeyPath:(NSString *)keyPath ofObject:(id)object newValue:(id)newValue&#123;
NSLog(@"lg_observeValueForKeyPath - %@",newValue);</li>
</ul>
<p>&#125;</p>
<p>#pragma mark - dealloc</p>
<ul>
<li>(void)dealloc&#123;</li>
</ul>
<p>&#125;</p>
<ul>
<li>(void)touchesBegan:(NSSet<UITouch *> *)touches withEvent:(UIEvent *)event&#123;
self.p.name = [NSString stringWithFormat:@"%@+",self.p.name];</li>
</ul>
<p>&#125;</p>
<p>@end</p>
</li>
<li>
<p>定义两个类</p>
</li>
</ol>
<ul>
<li>
<p>定义Person类</p>
<p>#import <Foundation/Foundation.h></p>
<p>@interface Person : NSObject&#123;
@public
NSString *girl;
&#125;</p>
<p>@property (nonatomic, copy) NSString *name;
@property (nonatomic, assign) int age;</p>
<p>@property (nonatomic, strong) NSMutableArray *mArray;</p>
<ul>
<li>(instancetype)shared;</li>
</ul>
<p>@end</p>
<p>#import "Person.h"</p>
<p>@implementation Person</p>
<ul>
<li>(void)setName:(NSString *)name&#123;
NSLog(@"设置方法 ");</li>
</ul>
<p>&#125;</p>
<ul>
<li>(void)dealloc&#123;
NSLog(@"父走了");</li>
</ul>
<p>&#125;</p>
<p>@end
#import "Person.h"</p>
<p>@implementation Person</p>
<ul>
<li>(void)setName:(NSString *)name&#123;
NSLog(@"设置方法 ");</li>
</ul>
<p>&#125;</p>
<ul>
<li>(void)dealloc&#123;
NSLog(@"父走了");</li>
</ul>
<p>&#125;</p>
<p>@end</p>
</li>
<li>
<p>定义Dog类</p>
<p>#import <Foundation/Foundation.h>
#import "Person.h"</p>
<p>@interface Dog : Person</p>
<p>@property (nonatomic, copy) NSString *name;
@property (nonatomic, assign) int age;</p>
<p>@end</p>
<p>#import "Dog.h"</p>
<p>@implementation Dog</p>
<ul>
<li>(void)dealloc&#123;
NSLog(@"儿子走了");</li>
</ul>
<p>&#125;
@end</p>
</li>
</ul>
<ol>
<li>定义NSObject的一个实现KVO监听的分类NSObject+KCKVO</li>
</ol>
<ul>
<li>
<p>头文件</p>
<p>#import <Foundation/Foundation.h></p>
<p>typedef void(^KCKVOBlock)(id observer,NSString *keyPath,id oldValue,id newValue);</p>
<p>@interface NSObject (KCKVO)</p>
<ul>
<li>
<p>(void)lg_addObserver:(NSObject *)observer forKeyPath:(NSString *)keyPath;</p>
</li>
<li>
<p>(void)lg_removeObserver:(NSObject *)observer forKeyPath:(NSString *)keyPath;</p>
</li>
</ul>
<p>@end</p>
</li>
<li>
<p>实现类</p>
<p>#import "NSObject+KCKVO.h"
#import <objc/message.h></p>
<p>static NSString *const kKCKVOPrefix = @"KCKVO_";
static NSString *const kKCKVOAssiociateKey = @"kKCKVO_AssiociateKey";</p>
<p>@implementation NSObject (KCKVO)</p>
<ul>
<li>
<p>(void)lg_addObserver:(NSObject *)observer forKeyPath:(NSString *)keyPath&#123;
// 1: 是否有setter方法
// id superClassName = object_getClassName(self); // person
// setName
NSString *setterMethodName = setterForGetter(keyPath); // setName:
SEL setterSel = NSSelectorFromString(setterMethodName);
// method
Method method = class_getInstanceMethod([self class], setterSel);// runtime 1900009931
if (!method) &#123;
@throw [[NSException alloc] initWithName:NSExtensionItemAttachmentsKey reason:@"没有setter方法" userInfo:nil];
&#125;</p>
<p>//2: 动态生成子类
Class childClass = [self creatChildClassWithKeypath:keyPath];
if (!childClass) &#123;
NSLog(@"创建失败");
&#125;
// 3.0 消息转发
// observer
// 关联对象
objc_setAssociatedObject(self, (__bridge const void * _Nonnull)(kKCKVOAssiociateKey), observer, OBJC_ASSOCIATION_RETAIN_NONATOMIC);</p>
</li>
</ul>
<p>&#125;</p>
<p>#pragma mark - 动态创建子类</p>
<ul>
<li>
<p>(Class)creatChildClassWithKeypath:(NSString *)keyPath&#123;</p>
<p>NSString *oldClassName   = NSStringFromClass([self class]);//person
NSString *childClassName = [NSString stringWithFormat:@"%@%@",kKCKVOPrefix,oldClassName];</p>
<p>//2: 动态生成子类
//2.1 申请类
Class childClass = objc_allocateClassPair([self class], childClassName.UTF8String, 0);
//2.2 注册类
objc_registerClassPair(childClass);
//2.3 添class
SEL classSel = NSSelectorFromString(@"class");
Method classMethod = class_getClassMethod([self class], classSel);
const char *classType = method_getTypeEncoding(classMethod);
class_addMethod(childClass, classSel, (IMP)lg_Class, classType);
//2.4 setter : setName:
SEL setterSel = NSSelectorFromString(setterForGetter(keyPath));
Method setterMethod = class_getClassMethod([self class], setterSel);
const char *setterType = method_getTypeEncoding(setterMethod);
class_addMethod(childClass, setterSel, (IMP)lg_setter, setterType);
//2.5 isa 指向
object_setClass(self, childClass);
return childClass;</p>
</li>
</ul>
<p>&#125;</p>
<p>/**
判断是否存在该方法
*/</p>
<ul>
<li>
<p>(BOOL)hasSeletor:(SEL)selector&#123;</p>
<p>Class observedClass = object_getClass(self);
unsigned int methodCount = 0;
//得到一堆方法的名字列表  //class_copyIvarList 实例变量  //class_copyPropertyList 得到所有属性名字
Method *methodList = class_copyMethodList(observedClass, &methodCount);</p>
<p>for (int i = 0; i<methodCount; i++) &#123;
SEL sel = method_getName(methodList[i]);
if (selector == sel) &#123;
free(methodList);
return YES;
&#125;
&#125;
free(methodList);
return NO;</p>
</li>
</ul>
<p>&#125;</p>
<p>#pragma mark - 函数区域
static Class lg_Class(id self,SEL _cmd)&#123;
return class_getSuperclass(object_getClass(self));
&#125;</p>
<p>static void lg_setter(id self,SEL _cmd,id value)&#123;</p>
<pre><code class="copyable">NSLog(@"lg_setter - %@",value);

id observer = objc_getAssociatedObject(self, (__bridge const void * _Nonnull)(kKCKVOAssiociateKey));
SEL handlSEL = @selector(lg_observeValueForKeyPath: ofObject:newValue:);
NSString *keypath = getterForSetter(NSStringFromSelector(_cmd));
objc_msgSend(observer,handlSEL,keypath,self,value);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>//    [observer performSelector:@selector(lg_observeValueForKeyPath: ofObject:newValue:) withObject:self afterDelay:0];
&#125;</p>
<p>#pragma mark - 从get方法获取set方法的名称 name ===>>> setName:
static NSString  * setterForGetter(NSString *getter)&#123;</p>
<pre><code class="copyable">if (getter.length <= 0) &#123; return nil; &#125;

NSString *firstString = [[getter substringToIndex:1] uppercaseString];
NSString *leaveString = [getter substringFromIndex:1];

return [NSString stringWithFormat:@"set%@%@:",firstString,leaveString];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
<p>#pragma mark - 从set方法获取getter方法的名称 setName:===> name
static NSString * getterForSetter(NSString *setter)&#123;</p>
<pre><code class="copyable">if (setter.length <= 0 || ![setter hasPrefix:@"set"] || ![setter hasSuffix:@":"]) &#123; return nil;&#125;

NSRange range = NSMakeRange(3, setter.length-4);
NSString *getter = [setter substringWithRange:range];
NSString *firstString = [[getter substringToIndex:1] lowercaseString];
getter = [getter stringByReplacingCharactersInRange:NSMakeRange(0, 1) withString:firstString];

return getter;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
<p>@end</p>
</li>
</ul>
<p>4.运行打印结果：<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5369f4907bc94bcfb14f89e3838b50ba~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-12">2. 通过 runtime 动态创建子类方式去实现</h4>
<ol>
<li>
<p>动态创建一个 NSKVONotifying_Person 子类</p>
<p>/**
运行时动态的创建子类</p>
<p>@param super_cls 父类
@return 返回子类
*/</p>
<ul>
<li>(Class) registerSubClassWithSuperClass:(Class)super_cls  &#123;
///动态的创建 子类
NSString *clsName = [NSString stringWithFormat:@"NSKVONotifying_%@",super_cls];
///一个 NSObject 默认分配16个字节内存
Class sub_cls = objc_allocateClassPair(super_cls,clsName.UTF8String,16);
///注册一个子类
objc_registerClassPair(sub_cls);
///将父类 isa 指针指向 子类
object_setClass(self, sub_cls);
return sub_cls;</li>
</ul>
<p>&#125;</p>
</li>
<li>
<p>动态的给这个子类 动态添加方法 setter 方法 didChangeValueForKey方法 class 方法实现</p>
<p>///动态创建子类  NSKVONotifying_xxx
Class sub_cls = [self registerSubClassWithSuperClass:super_cls];</p>
<pre><code class="copyable">///给子类动态的添加 class setter  didChangeValueForKey 实现
Method class_method = class_getInstanceMethod(super_cls, @selector(class));
Method changeValue_method = class_getInstanceMethod(super_cls, @selector(didChangeValueForKey:));

class_addMethod(sub_cls, @selector(class), (IMP)kvo_class,method_getTypeEncoding(class_method));
///给子类动态的添加 didChangeValueForKey
class_addMethod(sub_cls, @selector(didChangeValueForKey:), (IMP)didChangeValue,method_getTypeEncoding(changeValue_method));
///动态的给子类添加 setter 方法
class_addMethod(sub_cls, setterSel, (IMP)kvo_setter,method_getTypeEncoding(method));

///将观察者对象跟当前实例 self 关联起来
objc_setAssociatedObject(self,(__bridge const void * _Nonnull)(KVOAssociatedObservers), observer, OBJC_ASSOCIATION_RETAIN_NONATOMIC);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>重写 class 方法实现</p>
<p>/**
自实现 class 方法</p>
<p>@param self 当前类实现
@param _cmd  class
@return  返回父类 Class 外界不会知道 NSKVONotifying_子类存在
*/
static Class kvo_class(id self,SEL _cmd) &#123;
return class_getSuperclass(object_getClass(self));
&#125;</p>
</li>
<li>
<p>重写 setter 方法实现</p>
<p>/**
自实现 setter 方法</p>
<p>@param self 当前类实现
@param _cmd  setter
@param newValue  赋值
*/
static void kvo_setter(id self,SEL _cmd,id newValue) &#123;</p>
<pre><code class="copyable">NSString *setterName = NSStringFromSelector(_cmd);
NSString *getterName = getterForSetter(setterName);

///将要改变属性的值
[self willChangeValueForKey:getterName];

///调用 super setter 方法
struct objc_super suer_cls = &#123;
    .receiver = self,
    .super_class = class_getSuperclass(object_getClass(self))
&#125;;

///存储旧值
objc_setAssociatedObject(self,(__bridge const void * _Nonnull)(KVOAssociatedOldValue),[self valueForKey:getterName], OBJC_ASSOCIATION_RETAIN_NONATOMIC);
///调用父类 setter 方法 设置新值
objc_msgSendSuper(&suer_cls,_cmd,newValue);
///改变监听属性值后 调用 didChangeValueForKey 并在内部 调用
[self didChangeValueForKey:getterName];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;;</p>
</li>
<li>
<p>重写 didChangeValueForKey 方法实现</p>
<p>/**
didChangeValueForkey 实现方法 , 当根据 SEL (didChangeValueForkey:) 会找到方法 IMP 实现
*/
static void didChangeValue(id self,SEL _cmd,NSString *key) &#123;</p>
<pre><code class="copyable">id newValue = [self valueForKey:key];
id observer = objc_getAssociatedObject(self,(__bridge const void * _Nonnull)(KVOAssociatedObservers));
id oldValue = objc_getAssociatedObject(self,(__bridge const void * _Nonnull)(KVOAssociatedOldValue));

NSMutableDictionary *change = [NSMutableDictionary dictionary];
if (oldValue) &#123;
    change[@"oldValue"] = oldValue;
&#125; else &#123;
    change[@"oldValue"] = [NSNull null];
&#125;
if (newValue) &#123;
    change[@"newValue"] = newValue;
&#125; else &#123;
    change[@"newValue"] = newValue;
&#125;

[observer observeValueForKeyPath:key ofObject:self change:change context:NULL];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>&#125;</p>
</li>
</ol>
<p><strong>文章接下来还会持续更新，你也可以私信我及时获取最新资料以及面试相关资料。如果你有什么意见和建议欢迎给我留言。</strong></p>
<h3 data-id="heading-13">求喜欢IOS的小伙伴关注 ！喜欢的话给一个赞吧！谢谢！谢谢！谢谢！</h3>
<blockquote>
<p><strong>点击获取：<a href="https://link.juejin.cn/?target=https%3A%2F%2Flinks.jianshu.com%2Fgo%3Fto%3Dhttps%253A%252F%252Fdocs.qq.com%252Fdoc%252FDT25JSVR4SllGVUlj" target="_blank" rel="nofollow noopener noreferrer" title="https://links.jianshu.com/go?to=https%3A%2F%2Fdocs.qq.com%2Fdoc%2FDT25JSVR4SllGVUlj" ref="nofollow noopener noreferrer">iOS面试资料</a></strong></p>
</blockquote>
<p><strong>收录：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fkyl282889543%2Farticle%2Fdetails%2F93859511" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/kyl282889543/article/details/93859511" ref="nofollow noopener noreferrer">原文</a></strong></p></div>  
</div>
            