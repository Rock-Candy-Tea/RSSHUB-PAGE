
---
title: 'Android 可扩展视图设计'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89116dd65a7948c193b8a7129726a5eb~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 19 Jul 2021 22:27:09 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89116dd65a7948c193b8a7129726a5eb~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<h3 data-id="heading-1">问题</h3>
<p>飞书团队在去年对Chat页面进行了布局优化，在优化的时候发现了一个现象：很多布局（特别是RootView）往往会被附加非常多的功能（输入法监控、渲染耗时统计 、侧边栏滑出抽屉等），而且这些功能在很多场景下都会被用到。</p>
<p>当时面临一个问题：<strong>如何优雅地扩展一个View的功能？</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89116dd65a7948c193b8a7129726a5eb~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">常用方案</h3>
<p>对于View的功能扩展，一般有三条路可走：</p>
<ol>
<li>一个自定义View的无限膨胀</li>
<li>多层自定义View</li>
<li>多重继承自定义View</li>
</ol>
<p>但是，这三个方案都有问题：</p>
<ol>
<li>一个自定义View，会完全没有可复用性，可维护性差</li>
<li>多层自定义View，会有过度绘制问题（增加了视图层级）</li>
<li>多重继承自定义View，会有耦合性问题，因为如果有N个功能自由组合，使用继承的方式来实现，最终自定义View的个数会是：<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>C</mi><mo stretchy="false">(</mo><mi>N</mi><mo separator="true">,</mo><mn>1</mn><mo stretchy="false">)</mo><mo>+</mo><mi>C</mi><mo stretchy="false">(</mo><mi>N</mi><mo separator="true">,</mo><mn>2</mn><mo stretchy="false">)</mo><mo>+</mo><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi><mo>+</mo><mi>C</mi><mo stretchy="false">(</mo><mi>N</mi><mo separator="true">,</mo><mi>N</mi><mo stretchy="false">)</mo></mrow><annotation encoding="application/x-tex">C(N,1)+C(N,2)+...+C(N,N)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal" style="margin-right:0.07153em;">C</span><span class="mopen">(</span><span class="mord mathnormal" style="margin-right:0.10903em;">N</span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord">1</span><span class="mclose">)</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">+</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal" style="margin-right:0.07153em;">C</span><span class="mopen">(</span><span class="mord mathnormal" style="margin-right:0.10903em;">N</span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord">2</span><span class="mclose">)</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">+</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height:0.66666em;vertical-align:-0.08333em;"></span><span class="mord">.</span><span class="mord">.</span><span class="mord">.</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">+</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal" style="margin-right:0.07153em;">C</span><span class="mopen">(</span><span class="mord mathnormal" style="margin-right:0.10903em;">N</span><span class="mpunct">,</span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord mathnormal" style="margin-right:0.10903em;">N</span><span class="mclose">)</span></span></span></span></span></li>
</ol>
<h3 data-id="heading-3">一个想法</h3>
<p>我们知道，在软件设计中有一对非常重要的概念：<strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fbeenupper%2Fp%2F12534463.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/beenupper/p/12534463.html" ref="nofollow noopener noreferrer">is-a 和 has-a</a></strong> <strong>。</strong> 简单理解，is-a表示继承关系，has-a是组合关系，而has-a要比is-a拥有更好的可扩展性。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f309ad4ed996410ebb62c69837d0d70e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么在扩展视图功能的时候，是不是也可以用has-a（组合）代替常用的is-a（继承）？</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3ecf43ea3f849b3b97e38da88df5dd0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>答案是可以的，而且我们可以使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.yimipuzi.com%2F1006.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.yimipuzi.com/1006.html" ref="nofollow noopener noreferrer">委托模式</a>来实现它，委托模式天然适合这个工作：<strong>设计的出发点就是为has-a替代is-a提供解决方案的，</strong> 而Kotlin在语言层面对委托模式提供了非常优雅的支持，在这种场景下可以使用它的<strong>by接口委托</strong> <strong>。</strong></p>
<h2 data-id="heading-4">探索</h2>
<h3 data-id="heading-5">概念定义</h3>
<ul>
<li><strong>Widget：</strong> 系统View / ViewGroup、自定义View / ViewGroup。</li>
<li><strong>WidgetPlus：</strong> 委托者。继承自Widget，并可通过register()的方式has some items。</li>
<li><strong>DelegateItem：</strong> 被委托者。接受来自WidgetPlus的委托，负责业务逻辑的具体实现。</li>
<li><strong>IDelegate：</strong> 被委托者接口。</li>
</ul>
<p>不支持在 Docs 外粘贴 block</p>
<h3 data-id="heading-6">流程设计</h3>
<p>无法复制加载中的内容</p>
<h3 data-id="heading-7">角色转换</h3>
<p>在被委托接口IDelagate的“润滑”下，Widget、WidgetPlus和Item相互之间是可以做到无缝转换的</p>
<ul>
<li>
<p><strong>Widget -> WidgetPlus</strong></p>
<ul>
<li>简单描述：一个视图可以改造为功能可扩展的视图（<strong>可双向</strong>）</li>
<li>转换方法：实现IDelegate接口、支持item注册</li>
</ul>
</li>
<li>
<p><strong>Widget -> DelegateItem</strong></p>
<ul>
<li>简单描述：自定义视图可以被改造为一个功能项，供其它可扩展视图动态配置（<strong>可双向</strong>）</li>
<li>转换方法：自定义Widget移除对Widget的继承，实现IDelegate接口</li>
</ul>
</li>
<li>
<p><strong>WidgetPlus -> DelegateItem</strong></p>
<ul>
<li>简单描述：一个可扩展视图（本身带有一部分功能），可被改造为功能项（<strong>可双向</strong>）</li>
<li>转换方法：移除对Widget的继承，保留IDelegate接口的实现</li>
</ul>
</li>
</ul>
<p>无法复制加载中的内容</p>
<h3 data-id="heading-8">通信和调用</h3>
<ul>
<li>
<p>可扩展视图和扩展项应该支持双向通信：</p>
<ul>
<li>
<p>WidgetPlus -> DelegateItem</p>
<ul>
<li>这个比较简单，WidgetPlus会用组合的方式持有Item，在收到业务或系统的请求时，委托Item去执行具体的实现逻辑。</li>
</ul>
</li>
<li>
<p>DelegateItem -> WidgetPlus</p>
<ul>
<li>在Item初始化的时候，需要传入WidgetPlus的相关信息（widgetPlus、context、attrs、defStyleAttr、defStyleRes）</li>
</ul>
</li>
</ul>
</li>
<li>
<p>WidgetPlus跟Items拥有相同的API，需要设置调用原则：</p>
<ul>
<li>所有公共方法，一律使用WidgetPlus对象来触发（无论是在外部代码还是Item内部）</li>
<li>Item私有方法，使用Item对象来触发</li>
</ul>
</li>
</ul>
<h3 data-id="heading-9">竞争机制</h3>
<p>一个WidgetPlus同时持有多个Item的时候，如果这些Item被委托实现了相同的方法，那么就会出现Item的内部竞争问题。这里，可以根据方法类别来分别处理：</p>
<ol>
<li>
<p>无返回值方法</p>
<ol>
<li>比如<code>onMeasure()</code>，按照Item注册列表顺序执行</li>
</ol>
</li>
<li>
<p>有返回值方法</p>
</li>
</ol>
<ul>
<li>比如<code>onTouchEvent():Boolean</code>，这里出现了<strong>功能冲突</strong>，因为不可能同时返回多个值，只能取第一个返回值作为WidgetPlus的返回值。</li>
<li>对于这种情形，可以打印日志以便Develop时就被发现，解决方法有两种：</li>
</ul>
<ol>
<li>合而为一，即把两个Item合并，在一个Item中处理冲突；</li>
<li>分而治之，即把其中一个Item转换为WidgetPlus，创建两级视图。</li>
</ol>
<h2 data-id="heading-10">关键点</h2>
<h3 data-id="heading-11">1:1</h3>
<ul>
<li>一个WidgetPlus可以无限扩展Item功能项，但是对一种Item功能项只能持有一个对象。</li>
<li>但是，由于外部调用具有不可控性，所以register()的入参应该是<strong>Item的Class对象</strong>，在WidgetPlus内部反射调用Item的构造来生成对象。</li>
</ul>
<h3 data-id="heading-12">Center</h3>
<p>WidgetPlus中还是有一部分代码量的，为了减少Widget的转换成本、增加后续的可维护性，可以在WidgetPlus和Item直接<strong>再加一层DelegateCenter，由它来统一管理。</strong></p>
<p>无法复制加载中的内容</p>
<h3 data-id="heading-13">Super</h3>
<ul>
<li>问题：在重写Widget的系统方法时，是需要执行superMethod的，而Item在进行业务实现时，无法直接触发到这个superMethod的。</li>
<li>有两个解决方案：</li>
</ul>
<ol>
<li>把Widget的method拆分为methodBefore()、methodAfter()、isHasSuper()，分别委托Item实现</li>
<li>把superMethod作为委托参数，这里可以使用Kotlin的方法类型参数</li>
</ol>
<p>很显然，第二种方案要更好。</p>
<h2 data-id="heading-14">示意代码</h2>
<pre><code class="copyable"> /**

 * Widget

 */

package android.widget;

public class LinearLayout extends ViewGroup &#123;

    protected void onMeasure(int widthMeasureSpec, int heightMeasureSpec) &#123;&#125;

&#125;



 /**

 * WidgetPlus

 */

class LinearLayoutPlus() : LinearLayout(), IDelegate by DelegateCenter() &#123;

    override fun onMeasure(widthMeasureSpec: Int, heightMeasureSpec: Int) &#123;

        onDelegateMeasure(widthMeasureSpec, heightMeasureSpec) &#123; _, _ ->

                 super.onMeasure(widthMeasureSpec, heightMeasureSpec)&#125;

    &#125;

&#125;



 /**

 * Center

 */

class DelegateCenter() : IDelegate &#123;



    private val itemList = mutableListOf<IItem>()



    fun register(item: Class<IDelegate>) &#123;

        plusList.add(item.newInstance())

    &#125;

    

    fun unRegister(item: Class<IDelegate>) &#123;

        plusList.remove(item)

    &#125;

    

    override fun onDelegateMeasure(

                 widthMeasureSpec: Int,

                 heightMeasureSpec: Int,

                 superMethod: (Int, Int) -> Unit) &#123;

        for (item in itemList) &#123;

            item.onDelegateMeasure(widthMeasureSpec, heightMeasureSpec,superMethod)

        &#125;

    &#125;

&#125;



 /**

 * delegate interface

 */

interface IDelegate : IItem &#123;

     

     fun register(item: Class<IDelegate>)

     

     fun unRegister(item: Class<IDelegate>)

&#125;



 /**

 * Item interface

 */

interface IItem&#123;

    fun onDelegateMeasure(widthMeasureSpec: Int, heightMeasureSpec: Int, 

                  superMethod: (Int, Int) -> Unit)

&#125;



 /**

 * Item1

 */

 class Item1() : IItem() &#123;

    override fun onDelegateMeasure(widthMeasureSpec: Int, heightMeasureSpec: I  nt, superMethod: (Int, Int) -> Unit) &#123;&#125;

&#125;



 /**

 * Item2

 */

 class Item2() : IItem() &#123;

    override fun onDelegateMeasure(widthMeasureSpec: Int, heightMeasureSpec: Int, superMethod: (Int, Int) -> Unit) &#123;&#125;

&#125;



/**

 * main

 */

fun main() &#123;

    val plus = LinearLayoutPlus(context, attrs)

    plus.register(Item1::class.java)

    plus.register(Item2::class.java)

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">背景知识</h2>
<h3 data-id="heading-16">类与类之间的关系</h3>
<ul>
<li>类与类之间有六种关系：</li>
</ul>






















































<table><thead><tr><th><strong>关系</strong></th><th><strong>描述</strong></th><th><strong>耦合度</strong></th><th><strong>语义</strong></th><th><strong>代码层面</strong></th></tr></thead><tbody><tr><td><strong>继承</strong></td><td>继承指的是一个类（称为子类、子接口）继承另外的一个类（称为父类、父接口）的功能，并可以增加它自己新功能的能力</td><td>☆☆☆☆☆☆</td><td>is-a</td><td>在Java中继承关系通过关键字extends明确标识</td></tr><tr><td><strong>实现</strong></td><td>实现指的是一个类实现接口（可以是多个）的功能</td><td>☆☆☆☆☆</td><td>is-a</td><td>在Java中实现关系通过关键字implements明确标识</td></tr><tr><td><strong>组合</strong></td><td>它体现整体与部分间的关系，而且具有不可分割性，生命周期是一致的</td><td>☆☆☆☆</td><td>contains-a</td><td>类B作为类A的成员变量，只能从语义上来区别聚合和关联</td></tr><tr><td><strong>聚合</strong></td><td>它体现整体与部分间的关系，它们是可分离的，各有自己的生命周期</td><td>☆☆☆</td><td>has-a</td><td>类B作为类A的成员变量，只能从语义上来区别组合和关联</td></tr><tr><td><strong>关联</strong></td><td>这种使用关系具有长期性，而且双方的关系一般是平等的</td><td>☆☆</td><td>has-a</td><td>类B作为类A的成员变量，只能从语义上来区别组合和聚合</td></tr><tr><td><strong>依赖</strong></td><td>这种使用关系具有临时性，非常的脆弱</td><td>☆</td><td>use-a</td><td>类B作为入参，在类A的某个方法中被使用</td></tr></tbody></table>
<ul>
<li>继承和实现体现的一种<strong>纵向关系</strong>，一般是明确无异议的。而组合、聚合、关联和依赖体现的是<strong>横向关系</strong>，它们之间就比较难区分了，这几种关系都是语义级别的，从代码层面并不能完全区分。</li>
</ul>
<h3 data-id="heading-17">委托模式</h3>
<ul>
<li><strong>定义</strong>：有两个对象参与处理同一个请求，接受请求的对象将请求委托给另一个对象来处理。</li>
<li><strong>能力：</strong> 是一种基础模式，状态模式、策略模式、访问者模式等在本质上就是在特殊场合采用了委托模式，<strong>委托模式使得我们可以用组合、聚合、关联来替代继承。</strong></li>
<li><strong>委托模式不能等价于代理模式：</strong> 虽然它们都是把业务需要实现的逻辑交给一个目标实现类来完成，但是使用代理模式的目的在于提供一种代理以<strong>控制</strong>对这个对象的访问，但是委托模式的出发点是将某个对象的请求<strong>拜托</strong>给另一个对象。</li>
<li>委托模式是可以自由切换被委托者，委托者甚至可以自实现业务逻辑，例如Java ClassLoader的双亲委派模型中，在委托父加载器加载失败的情况下，可以切换为自己去加载。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2540f3860221426c9e58054302306019~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-18">加入我们</h1>
<p>飞书 - 字节跳动旗下企业协作平台，集视频会议、在线文档、移动办公、协同软件的一站式企业沟通协作平台。目前飞书业务正在飞速发展中，在北京、深圳等城市都有研发中心，前端、移动端、Rust、服务端、测试、产品等职位都有足够的HC，期待你的加入，和我们一起做有挑战的事情（请戳链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Ffuture.feishu.cn%2Frecruit%25EF%25BC%2589" title="https://link.juejin.cn/?target=https%3A%2F%2Ffuture.feishu.cn%2Frecruit%25EF%25BC%2589" target="_blank">future.feishu.cn/recruit）</a></p>
<p>我们也欢迎和飞书的同学一起进行技术问题的交流，有兴趣的同学请点击 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fapplink.feishu.cn%2Fclient%2Fchat%2Fchatter%2Fadd_by_link%3Flink_token%3D850v2629-a47c-4f2c-ae70-04de11f260e2" title="https://link.juejin.cn/?target=https%3A%2F%2Fapplink.feishu.cn%2Fclient%2Fchat%2Fchatter%2Fadd_by_link%3Flink_token%3D850v2629-a47c-4f2c-ae70-04de11f260e2" target="_blank">飞书技术交流群</a> 入群交流</p></div>  
</div>
            