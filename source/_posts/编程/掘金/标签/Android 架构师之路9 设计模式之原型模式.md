
---
title: 'Android 架构师之路9 设计模式之原型模式'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1fa48fe85e8b4633ba0d9fae09b6ac2f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 31 Aug 2021 21:45:08 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1fa48fe85e8b4633ba0d9fae09b6ac2f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">前言</h4>
<blockquote>
<p>原型模式（Prototype Pattern）是用于创建重复的对象，同时又能保证性能。这种类型的设计模式属于创建型模式，它提供了一种创建对象的最佳方式。<br>
这种模式是实现了一个原型接口，该接口用于创建当前对象的克隆。当直接创建对象的代价比较大时，则采用这种模式。例如，一个对象需要在一个高代价的数据库操作之后被创建。我们可以缓存该对象，在下一个请求时返回它的克隆，在需要的时候更新数据库，以此来减少数据库调用。</p>
</blockquote>
<h4 data-id="heading-1">1、原型模式特征</h4>
<h5 data-id="heading-2">1.1 原型模式UML图</h5>
<div align="center">
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1fa48fe85e8b4633ba0d9fae09b6ac2f~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
</div>
<h5 data-id="heading-3">1.2 角色划分</h5>
<ul>
<li><strong>Prototype：</strong> （克隆接口）要求是抽象（抽象类、接口）</li>
<li><strong>ConcretePrototype：</strong> 被复制的对象。此角色需要实现抽象的原型角色所要求的接口。</li>
<li><strong>Client：</strong> 客户端类向原型管理器提出创建对象的请求。</li>
</ul>
<h5 data-id="heading-4">1.3 使用场景</h5>
<p>1、资源优化场景。<br>
2、类初始化需要消化非常多的资源，这个资源包括数据、硬件资源等。<br>
3、性能和安全要求的场景。<br>
4、通过 new 产生一个对象需要非常繁琐的数据准备或访问权限，则可以使用原型模式。<br>
5、一个对象多个修改者的场景。<br>
6、一个对象需要提供给其他对象访问，而且各个调用者可能都需要修改其值时，可以考虑使用原型模式拷贝多个对象供调用者使用。<br>
7、在实际项目中，原型模式很少单独出现，一般是和工厂方法模式一起出现，通过 clone 的方法创建一个对象，然后由工厂方法提供给调用者。原型模式已经与 Java 融为浑然一体，大家可以随手拿来使用。</p>
<h4 data-id="heading-5">2、代码实现</h4>
<h5 data-id="heading-6">2.1 非原型模式</h5>
<h6 data-id="heading-7">OrderService</h6>
<hr>
<pre><code class="hljs language-java copyable" lang="java">
<span class="hljs-comment">/**
 * Created by Xionghu on 2017/7/5.
 * Desc:
 */</span>

<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">OrderService</span> </span>&#123;
    <span class="hljs-comment">/**
     * 订单拆分
     *
     * 需求：订单数量超过了100，我就拆分？
     *
     * <span class="hljs-doctag">@param</span> order
     * <span class="hljs-doctag">@return</span>
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> List<IOrder> <span class="hljs-title">getOrder</span><span class="hljs-params">(IOrder order)</span></span>&#123;
        List<IOrder> orderList = <span class="hljs-keyword">new</span> ArrayList<IOrder>();
        <span class="hljs-comment">//订单数量大于100就要进行拆分</span>
        IOrder newOrder = <span class="hljs-keyword">null</span>;
        <span class="hljs-keyword">while</span> (order.getOrderNumber() > <span class="hljs-number">100</span>)
        &#123;
            <span class="hljs-keyword">if</span>(order <span class="hljs-keyword">instanceof</span> PersonalOrder)
            &#123;
                PersonalOrder personalOrder = (PersonalOrder) order;
                PersonalOrder newPersonalOrder = <span class="hljs-keyword">new</span> PersonalOrder();
                newPersonalOrder.setOrderName(personalOrder.getOrderName());
                newPersonalOrder.setOrderUserName(personalOrder.getOrderUserName());
               <span class="hljs-comment">// newPersonalOrder.setOrderNumber(100);</span>
                newOrder = newPersonalOrder;
                <span class="hljs-comment">//例如：在android当中，我们经常使用Intent，一般情况都会new Intent();</span>
            &#125;<span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span>(order <span class="hljs-keyword">instanceof</span> EnterpriseOrder)&#123;
                EnterpriseOrder enterpriseOrder = (EnterpriseOrder) order;
                EnterpriseOrder newEnterpriseOrder = <span class="hljs-keyword">new</span> EnterpriseOrder();
                newEnterpriseOrder.setOrderName(enterpriseOrder.getOrderName());
                newEnterpriseOrder.setOrderCompany(enterpriseOrder
                        .getOrderCompany());
                newOrder = newEnterpriseOrder;
            &#125;
            <span class="hljs-comment">//拆分</span>
            newOrder.setOrderNumber(<span class="hljs-number">100</span>);
            orderList.add(newOrder);
            <span class="hljs-comment">//改变原来的订单数量</span>
            order.setOrderNumber(order.getOrderNumber()-<span class="hljs-number">100</span>);
        &#125;
        orderList.add(order);

        <span class="hljs-keyword">return</span> orderList;
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-8">注意：将来随着不断版本迭代，订单种类会不断增加，这样写导致if 、else if语句也随之增加</h5>
<h5 data-id="heading-9">造成可读性差、耦合度高的问题</h5>
<h5 data-id="heading-10">2.2 原型模式写法</h5>
<h6 data-id="heading-11">OrderService</h6>
<hr>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">OrderService</span> </span>&#123;
    <span class="hljs-comment">/**
     * 订单拆分
     *
     * 需求：订单数量超过了100，我就拆分？
     *
     * <span class="hljs-doctag">@param</span> order
     * <span class="hljs-doctag">@return</span>
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> List<IOrder> <span class="hljs-title">getOrder</span><span class="hljs-params">(IOrder order)</span></span>&#123;
        List<IOrder> orderList = <span class="hljs-keyword">new</span> ArrayList<IOrder>();
        <span class="hljs-comment">//订单数量大于100就要进行拆分</span>
        IOrder newOrder = <span class="hljs-keyword">null</span>;
        <span class="hljs-keyword">while</span> (order.getOrderNumber() > <span class="hljs-number">100</span>)
        &#123;
            newOrder = (IOrder)order.orderClone();
            <span class="hljs-comment">//拆分</span>
            newOrder.setOrderNumber(<span class="hljs-number">100</span>);
            orderList.add(newOrder);
            <span class="hljs-comment">//改变原来的订单数量</span>
            order.setOrderNumber(order.getOrderNumber()-<span class="hljs-number">100</span>);
        &#125;
        orderList.add(order);

        <span class="hljs-keyword">return</span> orderList;
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-12">通过 newOrder = (IOrder)order.orderClone();直接获取到order的返回类型 ， 结构很清晰</h6>
<h6 data-id="heading-13">Prototype(IOrder )</h6>
<hr>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">IOrderClonable</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">public</span> IOrderClonable <span class="hljs-title">orderClone</span><span class="hljs-params">()</span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">IOrder</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">IOrderClonable</span> </span>&#123;
    <span class="hljs-comment">/**
     * 设置订单数量
     * <span class="hljs-doctag">@param</span> number
     * <span class="hljs-doctag">@return</span>
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">setOrderNumber</span><span class="hljs-params">(<span class="hljs-keyword">int</span> number)</span></span>;

    <span class="hljs-comment">/**
     * 获取订单数量
     * <span class="hljs-doctag">@return</span>
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">int</span> <span class="hljs-title">getOrderNumber</span><span class="hljs-params">()</span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-14">ConcretePrototype</h6>
<hr>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PersonalOrder</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">IOrder</span> </span>&#123;
    <span class="hljs-keyword">private</span> String orderName;
    <span class="hljs-keyword">private</span> String orderUserName;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">int</span> orderNumber;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">int</span> <span class="hljs-title">getOrderNumber</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> orderNumber;
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">setOrderNumber</span><span class="hljs-params">(<span class="hljs-keyword">int</span> number)</span> </span>&#123;
        <span class="hljs-keyword">this</span>.orderNumber = number;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">getOrderName</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> orderName;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">setOrderName</span><span class="hljs-params">(String orderName)</span> </span>&#123;
        <span class="hljs-keyword">this</span>.orderName = orderName;
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">getOrderUserName</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> orderUserName;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">setOrderUserName</span><span class="hljs-params">(String orderUserName)</span> </span>&#123;
        <span class="hljs-keyword">this</span>.orderUserName = orderUserName;
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">toString</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">"PersonalOrder&#123;"</span> +
                <span class="hljs-string">"orderName='"</span> + orderName + <span class="hljs-string">''</span><span class="hljs-string">' +
                ", orderUserName='</span><span class="hljs-string">" + orderUserName + ''' +
                "</span>, orderNumber=<span class="hljs-string">" + orderNumber +
                '&#125;';
    &#125;

    @Override
    public IOrderClonable orderClone() &#123;
        PersonalOrder personalOrder = new PersonalOrder();
        personalOrder.setOrderName(orderName);
        personalOrder.setOrderUserName(orderUserName);
        return personalOrder;
    &#125;
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">/**
 * 企业订单
 * Created by Xionghu on 2017/7/5.
 * Desc:
 */</span>

<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">EnterpriseOrder</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">IOrder</span> </span>&#123;
    <span class="hljs-keyword">private</span> String orderName;
    <span class="hljs-keyword">private</span> String orderCompany;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">int</span> orderNumber;

    <span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">getOrderName</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> orderName;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">setOrderName</span><span class="hljs-params">(String orderName)</span> </span>&#123;
        <span class="hljs-keyword">this</span>.orderName = orderName;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">getOrderCompany</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> orderCompany;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">setOrderCompany</span><span class="hljs-params">(String orderCompany)</span> </span>&#123;
        <span class="hljs-keyword">this</span>.orderCompany = orderCompany;
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">int</span> <span class="hljs-title">getOrderNumber</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> orderNumber;
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">setOrderNumber</span><span class="hljs-params">(<span class="hljs-keyword">int</span> number)</span> </span>&#123;
        <span class="hljs-keyword">this</span>.orderNumber = number;
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">toString</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">"EnterpriseOrder&#123;"</span> +
                <span class="hljs-string">"orderName='"</span> + orderName + <span class="hljs-string">''</span><span class="hljs-string">' +
                ", orderCompany='</span><span class="hljs-string">" + orderCompany + ''' +
                "</span>, orderNumber=<span class="hljs-string">" + orderNumber +
                '&#125;';
    &#125;
    @Override
    public IOrder orderClone() &#123;
        EnterpriseOrder enterpriceOrder = new EnterpriseOrder();
        enterpriceOrder.setOrderCompany(orderCompany);
        enterpriceOrder.setOrderName(orderName);
        return enterpriceOrder;
    &#125;
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">OrderTest</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
        PersonalOrder personalOrder = <span class="hljs-keyword">new</span> PersonalOrder();
        personalOrder.setOrderName(<span class="hljs-string">"手机"</span>);
        personalOrder.setOrderUserName(<span class="hljs-string">"kpioneer"</span>);
        personalOrder.setOrderNumber(<span class="hljs-number">999</span>);


        EnterpriseOrder enterpriseOrder = <span class="hljs-keyword">new</span> EnterpriseOrder();
        enterpriseOrder.setOrderName(<span class="hljs-string">"电脑"</span>);
        enterpriseOrder.setOrderCompany(<span class="hljs-string">"haocai"</span>);
        enterpriseOrder.setOrderNumber(<span class="hljs-number">666</span>);
        <span class="hljs-comment">//将来随着不断版本迭代，订单种类会不断增加</span>

        <span class="hljs-comment">// 获取拆分后的订单</span>
        <span class="hljs-comment">// 结果是拆分为10个订单</span>
        List<IOrder> order = OrderService.getOrder(enterpriseOrder);
        <span class="hljs-keyword">for</span> (IOrder iOrder : order) &#123;
            System.out.println(<span class="hljs-string">"订单信息:"</span> + iOrder.toString());
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果输出：</p>
<hr>
<pre><code class="copyable">订单信息:EnterpriseOrder&#123;orderName='电脑', orderCompany='haocai', orderNumber=100&#125;
订单信息:EnterpriseOrder&#123;orderName='电脑', orderCompany='haocai', orderNumber=100&#125;
订单信息:EnterpriseOrder&#123;orderName='电脑', orderCompany='haocai', orderNumber=100&#125;
订单信息:EnterpriseOrder&#123;orderName='电脑', orderCompany='haocai', orderNumber=100&#125;
订单信息:EnterpriseOrder&#123;orderName='电脑', orderCompany='haocai', orderNumber=100&#125;
订单信息:EnterpriseOrder&#123;orderName='电脑', orderCompany='haocai', orderNumber=100&#125;
订单信息:EnterpriseOrder&#123;orderName='电脑', orderCompany='haocai', orderNumber=66&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">3、Android中源码使用</h4>
<p>原型模式中的拷贝分为"浅拷贝"和"深拷贝":<br>
浅拷贝: 对值类型的成员变量进行值的复制,对引用类型的成员变量只复制引用,不复制引用的对象.<br>
深拷贝: 对值类型的成员变量进行值的复制,对引用类型的成员变量也进行引用对象的复制.</p>
<h6 data-id="heading-16">clone源码</h6>
<hr>
<pre><code class="hljs language-java copyable" lang="java">  <span class="hljs-function"><span class="hljs-keyword">protected</span> Object <span class="hljs-title">clone</span><span class="hljs-params">()</span> <span class="hljs-keyword">throws</span> CloneNotSupportedException </span>&#123;
        <span class="hljs-keyword">if</span> (!(<span class="hljs-keyword">this</span> <span class="hljs-keyword">instanceof</span> Cloneable)) &#123;
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> CloneNotSupportedException(<span class="hljs-string">"Class "</span> + getClass().getName() +
                                                 <span class="hljs-string">" doesn't implement Cloneable"</span>);
        &#125;

        <span class="hljs-keyword">return</span> internalClone();
    &#125;

    <span class="hljs-comment">/*
     * Native helper method for cloning.
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-keyword">native</span> Object <span class="hljs-title">internalClone</span><span class="hljs-params">()</span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Java 默认的克隆是浅度克隆</p>
<hr>
<pre><code class="hljs language-java copyable" lang="java">    ArrayList<String>list1= <span class="hljs-keyword">new</span> ArrayList<>();
    ArrayList<String>list2 = (ArrayList<String>) list1.clone();

    <span class="hljs-function"><span class="hljs-keyword">public</span> Object <span class="hljs-title">clone</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">try</span> &#123;
            ArrayList<?> v = (ArrayList<?>) <span class="hljs-keyword">super</span>.clone();
            v.elementData = Arrays.copyOf(elementData, size);
            v.modCount = <span class="hljs-number">0</span>;
            <span class="hljs-keyword">return</span> v;
        &#125; <span class="hljs-keyword">catch</span> (CloneNotSupportedException e) &#123;
            <span class="hljs-comment">// this shouldn't happen, since we are Cloneable</span>
            <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> InternalError(e);
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-17">3.1 Java提供原型模式使用</h5>
<h6 data-id="heading-18">Prototype(AbsOrder )</h6>
<hr>
<pre><code class="hljs language-java copyable" lang="java"> <span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AbsOrder</span>  <span class="hljs-keyword">implements</span> <span class="hljs-title">Cloneable</span> </span>&#123;
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">protected</span> AbsOrder <span class="hljs-title">clone</span><span class="hljs-params">()</span> <span class="hljs-keyword">throws</span> CloneNotSupportedException </span>&#123;
        <span class="hljs-keyword">return</span> (AbsOrder) <span class="hljs-keyword">super</span>.clone();
    &#125;

    <span class="hljs-comment">/**
     * 设置订单数量
     * <span class="hljs-doctag">@param</span> number
     * <span class="hljs-doctag">@return</span>
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <span class="hljs-keyword">void</span> <span class="hljs-title">setOrderNumber</span><span class="hljs-params">(<span class="hljs-keyword">int</span> number)</span></span>;

    <span class="hljs-comment">/**
     * 获取订单数量
     * <span class="hljs-doctag">@return</span>
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <span class="hljs-keyword">int</span> <span class="hljs-title">getOrderNumber</span><span class="hljs-params">()</span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-19">OrderService</h6>
<hr>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">OrderService</span> </span>&#123;
    <span class="hljs-comment">/**
     * 订单拆分
     *
     * 需求：订单数量超过了100，我就拆分？
     *
     * <span class="hljs-doctag">@param</span> order
     * <span class="hljs-doctag">@return</span>
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> List<AbsOrder> <span class="hljs-title">getOrder</span><span class="hljs-params">(AbsOrder order)</span> <span class="hljs-keyword">throws</span> CloneNotSupportedException </span>&#123;
        List<AbsOrder> orderList = <span class="hljs-keyword">new</span> ArrayList<AbsOrder>();
        <span class="hljs-comment">//订单数量大于100就要进行拆分</span>
        AbsOrder newOrder = <span class="hljs-keyword">null</span>;
        <span class="hljs-keyword">while</span> (order.getOrderNumber() > <span class="hljs-number">100</span>)
        &#123;
            newOrder= order.clone();

            <span class="hljs-comment">//拆分</span>
            newOrder.setOrderNumber(<span class="hljs-number">100</span>);
            orderList.add(newOrder);
            <span class="hljs-comment">//改变原来的订单数量</span>
            order.setOrderNumber(order.getOrderNumber()-<span class="hljs-number">100</span>);
        &#125;
        orderList.add(order);

        <span class="hljs-keyword">return</span> orderList;
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-20">ConcretePrototype</h6>
<hr>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">EnterpriseOrder</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">AbsOrder</span> </span>&#123;
    <span class="hljs-keyword">private</span> String orderName;
    <span class="hljs-keyword">private</span> String orderCompany;
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">int</span> orderNumber;

    <span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">getOrderName</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> orderName;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">setOrderName</span><span class="hljs-params">(String orderName)</span> </span>&#123;
        <span class="hljs-keyword">this</span>.orderName = orderName;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">getOrderCompany</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> orderCompany;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">setOrderCompany</span><span class="hljs-params">(String orderCompany)</span> </span>&#123;
        <span class="hljs-keyword">this</span>.orderCompany = orderCompany;
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">int</span> <span class="hljs-title">getOrderNumber</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> orderNumber;
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">setOrderNumber</span><span class="hljs-params">(<span class="hljs-keyword">int</span> number)</span> </span>&#123;
        <span class="hljs-keyword">this</span>.orderNumber = number;
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> String <span class="hljs-title">toString</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">"EnterpriseOrder&#123;"</span> +
                <span class="hljs-string">"orderName='"</span> + orderName + <span class="hljs-string">''</span><span class="hljs-string">' +
                ", orderCompany='</span><span class="hljs-string">" + orderCompany + ''' +
                "</span>, orderNumber=<span class="hljs-string">" + orderNumber +
                '&#125;';
    &#125;
    @Override
    protected AbsOrder clone() throws CloneNotSupportedException &#123;
        return (AbsOrder) super.clone();
    &#125;
&#125;
</span><span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-21">3.2 Android中使用</h5>
<hr>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">OneActivity</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">AppCompatActivity</span> </span>&#123;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onCreate</span><span class="hljs-params">(Bundle savedInstanceState)</span> </span>&#123;
        <span class="hljs-keyword">super</span>.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Intent intent = getIntent();
        intent.getStringExtra(<span class="hljs-string">"name"</span>);

        <span class="hljs-comment">//启动一个新的Activity</span>
        <span class="hljs-comment">// intent.clone()自动帮我们clone Extra参数（name）</span>
        Intent intent2 = (Intent) intent.clone();
        intent2.setClass(<span class="hljs-keyword">this</span>,TwoActivity.class);
        startActivity(intent2);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            