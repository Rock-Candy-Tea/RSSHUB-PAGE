
---
title: 'Android 架构师之路6 设计模式之工厂模式'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2eea6e2df314966be6bd75e41d5549e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 29 Aug 2021 05:02:50 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2eea6e2df314966be6bd75e41d5549e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">前言</h4>
<blockquote>
<p>工厂模式中，重要的是工厂类，而不是产品类。产品类可以是多种形式，多层继承或者是单个类都是可以的。但要明确的，工厂模式的接口只会返回一种类型的实例，这是在设计产品类的时候需要注意的，最好是有父类或者共同实现的接口。<br>
使用工厂模式，返回的实例一定是工厂创建的，而不是从其他对象中获取的。<br>
工厂模式返回的实例可以不是新创建的，返回由工厂创建好的实例也是可以的。</p>
</blockquote>
<p>工厂模式主要是为创建对象提供了接口。工厂模式按照《Java与模式》中的提法分为三类：</p>
<ol>
<li>简单工厂模式(Simple Factory)</li>
<li>工厂方法模式(Factory Method)</li>
<li>抽象工厂模式(Abstract Factory)</li>
</ol>
<h4 data-id="heading-1">1、工厂模式 - 简单工厂模式</h4>
<p>简单工厂优点：客户端可以免除直接创建产品对象的责任，而仅仅是“消费”产品。简单工厂模式通过这种做法实现了对责任的分割。</p>
<h5 data-id="heading-2">1.1、 简单工厂模式UML图</h5>
<div align="center">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2eea6e2df314966be6bd75e41d5549e~tplv-k3u1fbpfcp-watermark.image" alt="简单工厂模式UML图" loading="lazy" referrerpolicy="no-referrer">
</div>
<h5 data-id="heading-3">1.2、 代码实现</h5>
<h6 data-id="heading-4">定义接口</h6>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">/**
 * 地图规范
 * <span class="hljs-doctag">@author</span> Dream
 *
 */</span>
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">IMapView</span> </span>&#123;
    <span class="hljs-class"><span class="hljs-keyword">enum</span> <span class="hljs-title">MapType</span> </span>&#123;
        <span class="hljs-comment">// 空白背景模式常量</span>
        MAP_TYPE_NONE,
        <span class="hljs-comment">// 普通地图模式常量</span>
        MAP_TYPE_NORMAL,
        <span class="hljs-comment">// 卫星图模式常量</span>
        MAP_TYPE_SATELLITE
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> View <span class="hljs-title">getView</span><span class="hljs-params">()</span></span>;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">setMapType</span><span class="hljs-params">(MapType mapType)</span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-5">实现接口</h6>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">BaiduMapView</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">IMapView</span> </span>&#123;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> View <span class="hljs-title">getView</span><span class="hljs-params">()</span> </span>&#123;
        System.out.println(<span class="hljs-string">"调用了百度地图的getView"</span>);
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">null</span>;
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">setMapType</span><span class="hljs-params">(MapType mapType)</span> </span>&#123;
        System.out.println(<span class="hljs-string">"调用了百度地图的setMapType"</span>);
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">GaodeMapView</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">IMapView</span> </span>&#123;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> View <span class="hljs-title">getView</span><span class="hljs-params">()</span> </span>&#123;
        System.out.println(<span class="hljs-string">"调用了高德地图的getView"</span>);
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">null</span>;
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">setMapType</span><span class="hljs-params">(MapType mapType)</span> </span>&#123;
        System.out.println(<span class="hljs-string">"调用了高德地图的setMapType"</span>);
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-6">创建工厂类</h6>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MapViewFactory</span> </span>&#123;
    
    <span class="hljs-class"><span class="hljs-keyword">enum</span> <span class="hljs-title">MapType</span></span>&#123;
        Baidu,
        Gaode
    &#125;
    
    <span class="hljs-comment">//使用上一节课的内容---单例模式</span>
    <span class="hljs-comment">//懒汉式</span>
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> MapViewFactory mapViewFactory;
    
    <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-title">MapViewFactory</span><span class="hljs-params">()</span></span>&#123;
        
    &#125;
    
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> MapViewFactory <span class="hljs-title">getInstance</span><span class="hljs-params">()</span></span>&#123;
        <span class="hljs-keyword">if</span>(mapViewFactory == <span class="hljs-keyword">null</span>)&#123;
            mapViewFactory = <span class="hljs-keyword">new</span> MapViewFactory();
            ArrayList<String> list = <span class="hljs-keyword">new</span> ArrayList<String>();
            HashSet<String> hashSet = <span class="hljs-keyword">new</span> HashSet<String>();
        &#125;
        <span class="hljs-keyword">return</span> mapViewFactory;
    &#125;
    
    <span class="hljs-function"><span class="hljs-keyword">public</span> IMapView <span class="hljs-title">getMapView</span><span class="hljs-params">(MapType mapType)</span></span>&#123;
        IMapView mapView = <span class="hljs-keyword">null</span>;
        <span class="hljs-keyword">switch</span> (mapType) &#123;
        <span class="hljs-keyword">case</span> Baidu:
            mapView = <span class="hljs-keyword">new</span> BaiduMapView();
            <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> Gaode:
            mapView = <span class="hljs-keyword">new</span> GaodeMapView();
            <span class="hljs-keyword">break</span>;
        &#125;
        <span class="hljs-keyword">return</span> mapView;
    &#125;
    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-7">调用主函数</h6>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SimpleTest</span> </span>&#123;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
        <span class="hljs-comment">// 客户端和我们的地图模块耦合度大大降低了</span>
        IMapView mapView = MapViewFactory.getInstance().getMapView(
                MapViewFactory.MapType.Baidu);
        mapView.getView();
        mapView.setMapType(IMapView.MapType.MAP_TYPE_NONE);
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-8">运行结果</h6>
<pre><code class="hljs language-java copyable" lang="java">获得百度地图MapView
设置了高德地图类型
获得高德地图MapView
设置了高德地图类型
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-9">1.3、Android源码中使用</h5>
<pre><code class="hljs language-java copyable" lang="java">Android中简单工厂--BitmapFactory,XmlPullParserFactory,CertificateFactory
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">2、工厂模式 - 工厂方法模式</h4>
<p>工厂方法模式：把对象的实现延迟到子类完成<br>
工厂方法优点：允许系统在不修改具体工厂角色的情况下引进新产品。</p>
<h5 data-id="heading-11">2.1、 工厂方法模式UML图</h5>
<div align="center">
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2251afe527a4d26b5b6947223ee73a6~tplv-k3u1fbpfcp-watermark.image" alt="工厂方法模式UML图" loading="lazy" referrerpolicy="no-referrer">
</div>
<h5 data-id="heading-12">2.2、 代码实现</h5>
<h6 data-id="heading-13">产品接口与实现(Mapview)</h6>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">//接口</span>
<span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">IMapView</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onStart</span><span class="hljs-params">()</span></span>;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onResume</span><span class="hljs-params">()</span></span>;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onDestory</span><span class="hljs-params">()</span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">BaiduMapView</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">IMapView</span> </span>&#123;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onStart</span><span class="hljs-params">()</span> </span>&#123;
        System.out.println(<span class="hljs-string">"百度地图onStart"</span>);
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onResume</span><span class="hljs-params">()</span> </span>&#123;
        System.out.println(<span class="hljs-string">"百度地图onResume"</span>);
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onDestory</span><span class="hljs-params">()</span> </span>&#123;
        System.out.println(<span class="hljs-string">"百度地图onDestory"</span>);
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">GaodeMapView</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">IMapView</span> </span>&#123;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onStart</span><span class="hljs-params">()</span> </span>&#123;
        System.out.println(<span class="hljs-string">"高德地图onStart"</span>);
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onResume</span><span class="hljs-params">()</span> </span>&#123;
        System.out.println(<span class="hljs-string">"高德地图onResume"</span>);

    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onDestory</span><span class="hljs-params">()</span> </span>&#123;
        System.out.println(<span class="hljs-string">"高德地图onResume"</span>);
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-14">抽象工厂</h6>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">//抽象</span>
<span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AbsMapFactory</span> </span>&#123;
    <span class="hljs-comment">// 我只定义标准</span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <T extends IMapView> <span class="hljs-function">T <span class="hljs-title">createMapView</span><span class="hljs-params">(Class<T> clzz)</span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-15">实现工厂</h6>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">DefaultMapFactory</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">AbsMapFactory</span> </span>&#123;

    <span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> DefaultMapFactory defaultMapFactory;

    <span class="hljs-function"><span class="hljs-keyword">private</span> <span class="hljs-title">DefaultMapFactory</span><span class="hljs-params">()</span> </span>&#123;
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> DefaultMapFactory <span class="hljs-title">getInstance</span><span class="hljs-params">()</span></span>&#123;
        <span class="hljs-keyword">if</span>(defaultMapFactory == <span class="hljs-keyword">null</span>)&#123;
            defaultMapFactory = <span class="hljs-keyword">new</span> DefaultMapFactory();
        &#125;
        <span class="hljs-keyword">return</span> defaultMapFactory;
    &#125;


    <span class="hljs-meta">@Override</span>
    <span class="hljs-keyword">public</span> <T extends IMapView> <span class="hljs-function">T <span class="hljs-title">createMapView</span><span class="hljs-params">(Class<T> clzz)</span> </span>&#123;
        <span class="hljs-keyword">try</span> &#123;
            <span class="hljs-comment">// 反射</span>
            <span class="hljs-keyword">return</span> clzz.newInstance();
        &#125; <span class="hljs-keyword">catch</span> (Exception e) &#123;
            e.printStackTrace();
        &#125;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">null</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-16">调用主函数</h6>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">TestClient</span> </span>&#123;
    
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
        <span class="hljs-comment">//工厂方法模式</span>
        AbsMapFactory factory = DefaultMapFactory.getInstance();
        BaiduMapView mapView = factory.createMapView(BaiduMapView.class);
        mapView.onStart();

    &#125;
    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-17">运行结果</h6>
<pre><code class="copyable">百度地图onStart
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-18">2.2、 Java或Android中源码运用</h5>
<blockquote>
<p>分析List集合、Set集合、Map集合 源码<br>
lterator：遍历集合工厂方法抽象<br>
Itr：具体的工厂实现类</p>
</blockquote>
<blockquote>
<p>lterator-> 抽象（工厂方法抽象） -->AdsMapFactory<br>
Itr ->具体实现类->DefaultMapFactory<br>
AbstractList-> 抽象 -->ImapView</p>
</blockquote>
<pre><code class="copyable">      ArrayList-> 实现类-->  BaiduMapView
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-19">3、工厂模式 - 抽象工厂模式</h4>
<p>为了增加导航模块、全景图口快、定位模块而不仅仅是地图模块引入抽象工厂模式 （一组类要求相同约束）<br>
抽象工厂优点：向客户端提供一个接口，使得客户端在不必指定产品具体类型的情况下，创建多个产品族中的产品对象</p>
<h5 data-id="heading-20">3.1、 抽象工厂模式UML图</h5>
<div align="center">
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f378a96cfb134e0a9429aa88f42918c5~tplv-k3u1fbpfcp-watermark.image" alt="抽象工厂模式UML图" loading="lazy" referrerpolicy="no-referrer">
</div>
<h5 data-id="heading-21">3.2、 代码实现</h5>
<h6 data-id="heading-22">抽象工厂</h6>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AbsMapFactory</span> </span>&#123;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> AbsMapView <span class="hljs-title">createMapView</span><span class="hljs-params">()</span></span>;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> AbsMapNavigation <span class="hljs-title">createMapNavigation</span><span class="hljs-params">()</span></span>;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> AbsMapLocation <span class="hljs-title">createMapLocation</span><span class="hljs-params">()</span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-23">各种具体工厂</h6>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">GaodeMapFactory</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">AbsMapFactory</span> </span>&#123;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> AbsMapView <span class="hljs-title">createMapView</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> GaodeMapView();
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> AbsMapNavigation <span class="hljs-title">createMapNavigation</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> GaodeMapNavigation();
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> AbsMapLocation <span class="hljs-title">createMapLocation</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> GaodeMapLocation();
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">BaiduMapFactory</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">AbsMapFactory</span> </span>&#123;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> AbsMapView <span class="hljs-title">createMapView</span><span class="hljs-params">()</span> </span>&#123;

        <span class="hljs-keyword">return</span>  <span class="hljs-keyword">new</span> BaiduMapView();
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> AbsMapNavigation <span class="hljs-title">createMapNavigation</span><span class="hljs-params">()</span> </span>&#123;

        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> BaiduMapNavigation();
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> AbsMapLocation <span class="hljs-title">createMapLocation</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> BaiduMapLocation();
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-24">初始化工厂</h6>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">DefaultFactory</span> </span>&#123;


    <span class="hljs-comment">//使用反射</span>
    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span>  <T extends AbsMapFactory> <span class="hljs-function">T <span class="hljs-title">creatProduct</span><span class="hljs-params">(Class<T> clz)</span></span>&#123;
        AbsMapFactory api =<span class="hljs-keyword">null</span>;
        <span class="hljs-keyword">try</span> &#123;
            api =(AbsMapFactory) Class.forName(clz.getName()).newInstance();
        &#125; <span class="hljs-keyword">catch</span> (InstantiationException e) &#123;
            e.printStackTrace();
        &#125; <span class="hljs-keyword">catch</span> (IllegalAccessException e) &#123;
            e.printStackTrace();
        &#125; <span class="hljs-keyword">catch</span> (ClassNotFoundException e) &#123;
            e.printStackTrace();
        &#125;

        <span class="hljs-keyword">return</span> (T)api;
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-25">工厂内各产品</h6>
<p>定位产品</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AbsMapLocation</span> </span>&#123;
    
    <span class="hljs-comment">/**
     * 定位
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <span class="hljs-keyword">void</span> <span class="hljs-title">location</span><span class="hljs-params">()</span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">BaiduMapLocation</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">AbsMapLocation</span> </span>&#123;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">location</span><span class="hljs-params">()</span> </span>&#123;
        System.out.println(<span class="hljs-string">"百度地图定位..."</span>);
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">GaodeMapLocation</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">AbsMapLocation</span> </span>&#123;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">location</span><span class="hljs-params">()</span> </span>&#123;
        System.out.println(<span class="hljs-string">"高德地图定位..."</span>);
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>地图产品</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AbsMapView</span> </span>&#123;
    
    <span class="hljs-comment">/**
     * Result for IActivityManager.startActivity: an error where the
     * start had to be canceled.
     * <span class="hljs-doctag">@hide</span>
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onStart</span><span class="hljs-params">()</span></span>;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onResume</span><span class="hljs-params">()</span></span>;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onDestory</span><span class="hljs-params">()</span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">BaiduMapView</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">AbsMapView</span> </span>&#123;

    
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onStart</span><span class="hljs-params">()</span> </span>&#123;
        System.out.println(<span class="hljs-string">"百度地图调用了onStart"</span>);
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onResume</span><span class="hljs-params">()</span> </span>&#123;
        System.out.println(<span class="hljs-string">"百度地图调用了onResume"</span>);
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onDestory</span><span class="hljs-params">()</span> </span>&#123;
        System.out.println(<span class="hljs-string">"百度地图调用了onDestory"</span>);
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">GaodeMapView</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">AbsMapView</span> </span>&#123;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onStart</span><span class="hljs-params">()</span> </span>&#123;
        System.out.println(<span class="hljs-string">"高德地图调用了onStart"</span>);
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onResume</span><span class="hljs-params">()</span> </span>&#123;
        System.out.println(<span class="hljs-string">"高德地图调用了onResume"</span>);
    &#125;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onDestory</span><span class="hljs-params">()</span> </span>&#123;
        System.out.println(<span class="hljs-string">"高德地图调用了onDestory"</span>);
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>导航产品</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AbsMapNavigation</span> </span>&#123;
    
    <span class="hljs-comment">/**
     * 路线规划
     */</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">abstract</span> <span class="hljs-keyword">void</span> <span class="hljs-title">turnByTurn</span><span class="hljs-params">()</span></span>;
    
    <span class="hljs-comment">//......很多功能方法</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">BaiduMapNavigation</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">AbsMapNavigation</span> </span>&#123;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">turnByTurn</span><span class="hljs-params">()</span> </span>&#123;
        System.out.println(<span class="hljs-string">"百度地图导航路线规划"</span>);
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">GaodeMapNavigation</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">AbsMapNavigation</span> </span>&#123;

    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">turnByTurn</span><span class="hljs-params">()</span> </span>&#123;
        System.out.println(<span class="hljs-string">"高德地图导航功能路线规划"</span>);
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-26">调用主函数</h6>
<pre><code class="hljs language-java copyable" lang="java">
<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Test</span> </span>&#123;
    
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">main</span><span class="hljs-params">(String[] args)</span> </span>&#123;
        <span class="hljs-comment">//直接初始化某地图</span>
        AbsMapFactory factory = <span class="hljs-keyword">new</span> BaiduMapFactory();
        factory.createMapView().onStart();
        factory.createMapLocation().location();

        <span class="hljs-comment">//反射初始化某地图</span>
        AbsMapFactory factory2 =  DefaultFactory.creatProduct(GaodeMapFactory.class);
        factory2.createMapView().onStart();
        factory2.createMapLocation().location();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-27">运行结果</h6>
<pre><code class="copyable">百度地图调用了onStart
百度地图定位...
高德地图调用了onStart
高德地图定位...
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-28">3.3、 Android源码中使用</h5>
<blockquote>
<p>Activity、Service --- AbsMapView或者AbsMapNavgation<br>
我们自定义的Activity（如BaseActivity）、Service ---BaiduMapView 或 BaiduMapNavgation<br>
ActivityManager、ServiceManager --- 类似于我们通常所说的AbsMapFactory</p>
</blockquote>
<h4 data-id="heading-29">总结：</h4>
<blockquote>
<p>简单工厂 ： 用来生产同一等级结构中的任意产品。（对于增加新的产品，无能为力）<br>
工厂方法 ：用来生产同一等级结构中的固定产品。（支持增加任意产品）<br>
抽象工厂 ：用来生产不同产品族的全部产品。（对于增加新的产品，无能为力；支持增加产品族）<br>
<br>
以上三种工厂 方法在等级结构和产品族这两个方向上的支持程度不同。所以要根据情况考虑应该使用哪种方法。</p>
</blockquote></div>  
</div>
            