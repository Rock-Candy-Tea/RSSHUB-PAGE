
---
title: 'Eclipse华丽转身之控件表格工厂'
categories: 
    - 编程
    - 开源中国
    - 数字型账号用户博客

author: 开源中国
comments: false
date: 2021-03-23 06:28:25
thumbnail: 'https://www.oschina.net/img/hot3.png'
---

<div>   
<div class="content">
                                                                                                                    <div class="ad-wrap" style="margin-bottom: 8px;">
            <a data-traceid="blog_detail_above_text_link_1" data-tracepid="blog_detail_above_text_link" style="color:#A00; font-weight:bold;" href="https://e.cn.miaozhen.com/r/k=2226845&p=7qZiO&dx=__IPDX__&rt=2&pro=s&ns=__IP__&ni=__IESID__&v=__LOC__&xa=__ADPLATFORM__&tr=__REQUESTID__&o=https://ascend.huawei.com/zh/#/ecosystem/all-wisdom?utm_campaign=%252004MHQHQ210KA01N&utm_medium=pm-display&utm_source=OSCHINA&source=pc_blog&utm_object=ai_NA&utm_content=ascend_wisdom_ad" target="_blank">昇腾众智计划火热上线！140个算子/模型等你来挑战！>>><img src="https://www.oschina.net/img/hot3.png" align="absmiddle" style="max-height: 32px;max-width: 32px;margin-top: -4px;" referrerpolicy="no-referrer"></a>
            </div>
                                                                                                    <p style="color:#333333; text-align:center"><img src="https://mmbiz.qpic.cn/mmbiz_jpg/icQbWvrFMeJWia6SEwRu8D1byPWLMDt0HyibsqR4FCLcvBl1BnmjOEuJ1TRd7Nr4gEo7qUaK7zppZq4YqfQw8NnBg/640?wx_fmt=jpeg" width="578" referrerpolicy="no-referrer"></p> 
<p><strong><span style="color:#888888">​转载本文需注明出处：微信公众号EAWorld，违者必究。</span></strong></p> 
<p><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWNMttktDrLmHuQcJ03UOoUyVrx30M2pcMhPD3uVibss3rGdt8AfPy5Fae2I5mNoldg1BGHeyZFhPA/640?wx_fmt=png" width="29" referrerpolicy="no-referrer"></p> 
<p><strong>Eclipse</strong></p> 
<p><span style="color:#5f79a1"><strong>插件开发</strong></span></p> 
<p><span>书归正传，接演前文~（<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzI5MDEzMzg5Nw%3D%3D%26mid%3D2660407089%26idx%3D1%26sn%3D3954c3c63abdd746b917183c308c2881%26chksm%3Df742b5d7c0353cc1ed402bd2cf0b7b10352a400bacc5afbb55f406b3ea12806cd0724f60ba00%26scene%3D21%23wechat_redirect" target="_blank" rel="nofollow">Eclipse插件开发之简单控件封装——那些年冗长的裹脚布</a>）上回我们介绍了对象编辑器的封装，对象编辑器之外就是控件工厂的封装，而在众多类型的控件工厂中，想必大家最关心的，莫过于对槽点满满的原生Tree/Table的封装。这回我们便好好来说道说道~</span></p> 
<p><span>在此之前，我们还是要简单介绍一下控件工厂。</span></p> 
<p><em><strong>控件工厂</strong></em></p> 
<p> </p> 
<p><span><span>根据不同的UI需求，我们框架封装了许多控件工厂来完成灵活的应用需求。</span></span></p> 
<p><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWia6SEwRu8D1byPWLMDt0HyAHk6DXiaMkIibjnAPbROcx94HD8tAeKQbxylsEicsN69oYGicZnul0JlRQ/640?wx_fmt=png" width="562" referrerpolicy="no-referrer"></p> 
<p><span>IControlFactory控件工厂，因为有一些控件是运行时才会被创建的，而且要创建的控件也有可能不确定，所以提供一个这样的工厂用来创建控件,下图为它的类结构图。</span></p> 
<p><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWia6SEwRu8D1byPWLMDt0HyoMl82VGBKEjJ7ic7FibicbribHChUnc41nia3gwhTn11hLuhSpicqqWzBF8A/640?wx_fmt=png" width="542" referrerpolicy="no-referrer"></p> 
<p><span>AbstractControlFactory是IControlFactory的基类。这个基类在实现IValueContaier的同时还实现了IValueChangeListener和IValidateListener这样主要是通过Proxy的模式，只在内部的控件中添加自己作为Listener。</span></p> 
<p> </p> 
<p><em><strong>表格工厂</strong></em></p> 
<p> </p> 
<p> </p> 
<p><span>我们知道，无论是SWT的Table还是JFace的TableViewer/TreeViewer，都不能满。我们广泛需求，比如修改数据。而在我们开发过程中，表格往往是个非常普遍多次使用的控件，所以这里就要引入我们的表格工厂的封装了。那么，我们先简述以下表格工厂相关的几个概念（构建器、数据转换器、备忘录）。</span></p> 
<p><span><strong><em><span>表格构建器</span></em></strong></span></p> 
<p>Builder分为KTableBuilder和KTreeBuilder，其实他们是使用了第三方表格组件KTable来进行构造表格。</p> 
<p><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWia6SEwRu8D1byPWLMDt0Hy4PlUomicCzunuQKP5evMx6Nuft2FcCaYrx4zvm2iab2KTm2qBYFTBFNQ/640?wx_fmt=png" width="336" referrerpolicy="no-referrer"></p> 
<p>先来说一下KTable表格工厂的构建器KTableBuilder，下图为Builder的关系类图；</p> 
<p style="text-align:center"><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWia6SEwRu8D1byPWLMDt0HyTu7cxDN8xp1HDJ31zmrwWttVLGNfhbbp0AybbMhyS6RsQBCyiadicOag/640?wx_fmt=png" referrerpolicy="no-referrer"></p> 
<p>当需要使用一个KTableBuilder的时候我们一般直接new一个对象出来，可以看下它三种构造函数中带参数的一种；</p> 
<pre><code><span><span style="color:#ca7d37">public</span> KTableBuilder(KTable r_KTable, IKTableColumn[] r_Columns, ITableDataProvider r_TableDataProvider, IAdaptable r_Adaptable) &#123;</span></code><code><span>    <span style="color:#ca7d37">this</span>.setTableColumns(r_Columns);</span></code><code><span>    <span style="color:#ca7d37">this</span>.setDataProvider(r_TableDataProvider);</span></code><code><span>    <span style="color:#ca7d37">this</span>.build(r_KTable,r_Adaptable);</span></code><code><span>  &#125;</span></code></pre> 
<p>其中的ITableDataProvider就是数据提供者接口，为表格提供数据和排序。然后表格构建器通过doBuild方法来绘制表格。</p> 
<p><span><strong><em><span>数据转换器</span></em></strong></span></p> 
<p>Translator数据转换器，可以将数据转换成复杂控件使用的数据，如表格使用的列表数据；</p> 
<p>举一个例子来理解什么是Translator，例如Stuido的逻辑流文件（*.bizx文件），用文本编辑器开打后可以看到图形化编辑器中的图元的信息都是使用XML规范来描述的，比如一个运算逻辑图元属性如下图；</p> 
<p><img height="913" src="https://mmbiz.qpic.cn/mmbiz_png/icWTZoE41zuB8uLD6sicHm6CtyKpQFRpYXxic9zRMuk0krTEzZXUCOE92BWtVqqBfGWIMQvKp70ZokfFu2uibJhZSQ/640?wx_fmt=png" width="1163" referrerpolicy="no-referrer"></p> 
<p>则图片上表格中的值与模型对象之间的关系，这样就不难理解Translator数据转换器需要做的事情了，接下来看下它的类图；</p> 
<p><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWia6SEwRu8D1byPWLMDt0HyTNdfKzS9TicHsJTpI9Ysh7tJOtgPvadgHdzs4Sq0ZL2353r082HavvA/640?wx_fmt=png" width="549" referrerpolicy="no-referrer"></p> 
<p>其中AbstractKTableFactory# doCreateControl方法，在创建UI控件的时候调用了getTranslator方法返回的就是实现IObjectTranslator接口的子类；</p> 
<pre><code><span><span><span style="color:#ca7d37">protected</span> Control <span style="color:#dd1144">doCreateControl</span><span>(Composite r_Parent, UIDefinition r_UIDefinition)</span> </span>&#123;</span></code><code><span>………………………………………………………………………</span></code><code><span>    IObjectTranslator t_Translator = <span style="color:#ca7d37">this</span>.getTranslator();</span></code><code><span>    IKTableColumn[] t_Columns = <span style="color:#ca7d37">this</span>.getColumns();</span></code><code><span>    <span style="color:#ca7d37">for</span> (<span style="color:#ca7d37">int</span> i = <span style="color:#0e9ce5">0</span>; i < t_Columns.length; i++) &#123;</span></code><code><span>      <span style="color:#ca7d37">if</span> (t_Columns[i] <span style="color:#ca7d37">instanceof</span> AbstractTableColumn) &#123;</span></code><code><span>        AbstractTableColumn t_Column = (AbstractTableColumn) t_Columns[i];</span></code><code><span>        t_Column.setIntrospector(t_Translator.getIntrospector());</span></code><code><span><em>//这里会为每一个column设置一个数据访问器</em></span></code><code><span>      &#125;</span></code><code><span>    &#125;</span></code><code><span>………………………………………………………………………</span></code><code><span>    <span style="color:#ca7d37">return</span> createActionComposite(r_Parent, r_UIDefinition.isView());</span></code><code><span>  &#125;</span></code></pre> 
<p>看下IObjectTranslator接口中定义的方法；</p> 
<p style="text-align:justify"><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWia6SEwRu8D1byPWLMDt0HybR4wib2Ahm0jICV88h1CemlXOmx3ArTJibQQ0NC8nSSbmmLQ81K5JwUw/640?wx_fmt=png" referrerpolicy="no-referrer">同样formeTree和toTree方法，适用于KTreeBuilder创建出来的UI控件上表格数据的保存和回显；</p> 
<p><img height="106" src="https://mmbiz.qpic.cn/mmbiz_png/icWTZoE41zuB8uLD6sicHm6CtyKpQFRpYXONojX7ZgVHrcHT3ric7TCibu5vQc8wB0SL76mq6V2bQic6Znz5n0PSjog/640?wx_fmt=png" width="865" referrerpolicy="no-referrer"></p> 
<p>fromTable方法在AbstractKTableFactory中的save方法中被调用，一般用于UI界面上编写好数据，类似按保存按钮，或者向导中“确定”或者“完成”按钮时候调用,用于把表格中填写的数据存在一个数据备忘录IMemento中。</p> 
<p>toTable方法在这个UI界面被构造的时候方法中，new一个数据备忘录IMemento（后面的章节会讲到）的时候被调用，用于回显上一次填写的数据。</p> 
<p><strong><em><span>备忘录</span></em></strong></p> 
<p>IMemento提供一个数据备份和恢复的接口，可以用来备份数据和恢复数据.它与IStore非常相似,但是为了便于理解,使用Memento名字。可以参考Memento模式，下图为实现IMemento接口的子类，都可以根据自己控件的特性来备份恢复数据；</p> 
<p><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWia6SEwRu8D1byPWLMDt0HypoAXnW1PsoZiatwREvUwMhF4muqme51taMSSibq23Pkia9PIgwlhOC3OQ/640?wx_fmt=png" referrerpolicy="no-referrer"></p> 
<p>接口中就定义了2个方法，分别为backup备份数据，restore恢复数据，我们先可以来看一下TableMemento中的方法；</p> 
<pre><code><span><span style="color:#ca7d37">protected</span> List doBackup(String r_Type, Object r_Model) &#123;</span></code><code><span>    <span style="color:#ca7d37">if</span> (<span style="color:#0e9ce5">null</span>==<span style="color:#ca7d37">this</span>.objectTranslator) &#123;</span></code><code><span>      <span style="color:#ca7d37">return</span> new ArrayList();</span></code><code><span>    &#125; <span style="color:#ca7d37">else</span>&#123;    </span></code><code><span>      <span style="color:#ca7d37">return</span> <span style="color:#ca7d37">this</span>.objectTranslator.toTable(r_Type, r_Model);</span></code><code><span>    &#125;</span></code><code><span>  &#125;</span></code></pre> 
<p>在Translator章节中我们讲述了toTable方法，它是翻译成一个可以用于表格数据的列表，在AbstractKtableFactory中构造UI的方法中(doCreateControl)方法中我们会新建一个TableMemento的实例对象。在构造TableMemento实例的时候就会调用构造函数中的backup方法来保存UI界面中控件的值。</p> 
<p>那接口中restore恢复数据何时被调用呢？可以看下图，例如我们在数据集编辑器中空白处点击右键出现的菜单如下图；</p> 
<p style="text-align:center"><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWia6SEwRu8D1byPWLMDt0Hya4LGIbA4t47QjLSk8FFlKvbjQvrTd0TYqM7R3hhLJb3Ejtu3Cu83gw/640?wx_fmt=png" referrerpolicy="no-referrer"></p> 
<p>ICommand是用来提供Redo和Undo的接口，SimpleCommand则是ICommand的实现类，实现类中的redo和undo方法都会调用IMemento实现类的restore方法调用后来恢复数据。</p> 
<p> </p> 
<p>基本概念说完了，我们看下具体的表格工厂：KTable、KTree、Table。</p> 
<p> </p> 
<p><span style="color:#4a94e7"><strong>KTable表格工厂</strong></span></p> 
<p style="text-align:center"><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWia6SEwRu8D1byPWLMDt0Hy0t6AJ7vfSr3Qiap3bUn0TYkLdmZRluEz4Dq1pWHy2rVUdXyDI9X5Tjw/640?wx_fmt=png" referrerpolicy="no-referrer"></p> 
<p style="text-align:justify">AbstractKtableFactory用来支持表格控件的创建。</p> 
<p style="text-align:center"><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWia6SEwRu8D1byPWLMDt0HytXNb3OQkiczWOn7ibAHPldIvC6DgTlCH0oO0sMQf743dAHTq8ZAv4I3w/640?wx_fmt=png" referrerpolicy="no-referrer"></p> 
<p><strong>getCloumns方法</strong>：返回一个IKTableColumn []的数组，必须由子类来实现，IKTableColumn是用来支持Ktable的表格列，一般只需要构造一个KPropertyTableColumn（该数据列用来通过property来访问对象）就可以了。</p> 
<p><strong>getActionProvider方法</strong>：返回的IKTableActionProvider是控件上的一些Action操作，通常可以通过创建DefaultKTableActionProvider对象来实现。子类可以重写这个方法来构造自己的Action来进行对表中的数据进行操作。</p> 
<p><strong>getTranslator方法</strong>：返回数据数据转换器，通常为自己自定义的数据转换类</p> 
<p style="text-align:center"><span style="color:#4a94e7"><strong>KTree表格工厂</strong></span></p> 
<p style="text-align:center"><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWia6SEwRu8D1byPWLMDt0HyfoELLicZCLzMDPg8JNeDlOKxr4yoYyhu9wUgjraXX9yRNIOl8BONuXA/640?wx_fmt=png" referrerpolicy="no-referrer"></p> 
<p>AbstractKTreeFactory和AbstractKTableFacotory区别不大。通过UI界面可以看到区别，“参数”和“返回值”就好比一个树的跟节点root，而参数param1和参数param2为“参数”root的子节点。</p> 
<p>AbstractKTreeFactory中是使用KTreeBuilder来构造表格的，KTreeBuilde中有一个重要的属性ITreeNode,下图是它的类关系图：</p> 
<p style="text-align:center"><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWia6SEwRu8D1byPWLMDt0Hyo8akbxBJYmGXhwZXrhBPXmDFzW6786rfER1X2y8QcFXN4w6JSP2RxQ/640?wx_fmt=png" referrerpolicy="no-referrer"></p> 
<p style="text-align:justify">DefaultTreeNode实现了ITreeNode的接口并且继承了AbstractPropertyAwareElement（能够监控属性改变的类，当属性改变时，会发出相应的信息通知所有的监听者），KTreeBuilder类里面有一个方法叫做setRootNode()可以设置树的根节点，而ITreeNode的子类都可以构造自己的节点然后通过setParent()的方法设置父类节点，或者调用add()方法来添加自己的孩子节点，其中重要的是DefaultTreeNode的setUserObject()方法，它是用来为每个节点set一个对象的方法。我们来看一个示例（逻辑流出入参的数据转换器BusinessLogicTranslator）：</p> 
<p><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWia6SEwRu8D1byPWLMDt0HyR0mPdsHFAhgjXeSSNyVuib65oXZe3hwqhmdJjOzPdDXHPmIY4mrLkIQ/640?wx_fmt=png" referrerpolicy="no-referrer"></p> 
<p style="text-align:center"><span style="color:#4a94e7"><strong>Table表格工厂</strong></span></p> 
<p><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWia6SEwRu8D1byPWLMDt0Hy0TtALgCGRicjKp2hS49ichxPhUEPB45iakL7FjicZp2QC6gNzIShCEbzHQ/640?wx_fmt=png" width="542" referrerpolicy="no-referrer"></p> 
<p style="text-align:justify">AbstractTableFactory和AbstractKTableFactory基本很相像，看下一它的类关系图如下：</p> 
<p style="text-align:center"><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWia6SEwRu8D1byPWLMDt0Hy9vlcP7QRsA2SGNZK0RMdMNjK8YgmIS95Y7GgyHnsDC0OOqiaTHuIHEQ/640?wx_fmt=png" referrerpolicy="no-referrer"></p> 
<p style="text-align:justify">在AbstractTableFactory中构造表格的TableBuilder可以从上类图中看出来，其实是就是封装了eclipse自身的TableViewer，而不是AbstractKTableFactory中封装的KTable，这是两者之间本质的区别。</p> 
<p><em><strong>IKTableColumn</strong></em></p> 
<p> </p> 
<p>说完了表格工厂以后，我们回头再来看之前表格工厂里提到的一个方法getCloumns()，在这个方法中返回的是IKTableColumn []的数组。上文图中的表格列都是最基本的输入框也就是KPropertyTableColumn，除此之外还有哪些Column的封装呢？</p> 
<p><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWia6SEwRu8D1byPWLMDt0HyFia37f2UX0ma2rcUFdnkzZRBC7hqHDXS8KNDNwaJmumwNnHNYmxRMMg/640?wx_fmt=png" referrerpolicy="no-referrer"></p> 
<p>通过此图列举的类不难看出，表格Column的常用封装都可以满足了，无论是下拉框、复选框、还是带有图片的Column。那么下一篇我们就来详细说一下，表格工厂Column的封装，除此之外还有更为复杂的Column封装（如图），以及其他几个控件工厂的介绍。</p> 
<p><img src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWia6SEwRu8D1byPWLMDt0Hyou2ibHRoojgs9nLRkGrcmSGVsMgMjtn8hquQDCfv5MmibvQxmW6qCucQ/640?wx_fmt=png" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#888888; color:#f8f8f9">  - end -  </span></p> 
<p><img align="left" src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWNMttktDrLmHuQcJ03UOoUunmd86IcpnpibGKUJ2JEyiaDLFOOwPrEZjQythJnyMq6BlbQ9UxYcI0w/640?wx_fmt=png" width="129" referrerpolicy="no-referrer"><span><strong>关于作者</strong><span>：</span>leaf淼，普元高级软件工程师，善于Studio插件的开发与设计，目前负责EOS/BPS Studio产品开发，曾参与浦发银行BPM流程产品开发、太平洋保险集团微服务平台开发等。</span></p> 
<p> </p> 
<p> </p> 
<p> </p> 
<p><img align="left" src="https://mmbiz.qpic.cn/mmbiz_png/icQbWvrFMeJWaNBdc2NWGRMLOZT5ntKc9qSzg9vyORia2VmUhhfsXx4Q9xBBSFIPDEF7y4YKDpy1uG37WliaqCBbw/640?wx_fmt=png" width="130" referrerpolicy="no-referrer"><span><strong><span>关于EAWorld</span></strong><span>：微服务，DevOps，数据治理，移动架构原创技术分享。<strong>长按二维码关注！</strong></span></span></p>
                                        </div>
                                      
</div>
            