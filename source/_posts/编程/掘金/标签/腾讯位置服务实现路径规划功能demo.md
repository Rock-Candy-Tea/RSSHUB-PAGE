
---
title: '腾讯位置服务实现路径规划功能demo'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16d3129294a24c439967cc20a1bad6f7~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image'
author: 掘金
comments: false
date: Wed, 04 Aug 2021 05:23:32 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16d3129294a24c439967cc20a1bad6f7~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一.前言</h2>
<p>这个腾讯位置服务产品初体验小demo能够实现的基本功能有：实现输入(定位)当前位置及终点位置，在地图上规划出两点之间路线，并显示路线所需的距离及路费，确认行程后通过动画模拟车辆在路线上行驶。</p>
<h2 data-id="heading-1">二.实现步骤</h2>
<p>实现效果：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16d3129294a24c439967cc20a1bad6f7~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer">
新建一个Android项目并新建一个Activity，命名为DrivingRouteActivity，先来画一下UI布局，布局比较简单，由一个腾讯SDK包下的地图组件MapView，以及两个用于输入起始位置的输入框，两个确认路线规划的Button，一个定位当前位置的ImageView，一个用于显示行程信息的TextView组成，布局代码只是为了方便展示实现功能，所以下面直接贴出布局代码：</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-meta"><?xml version="1.0" encoding="utf-8"?></span>
<span class="hljs-tag"><<span class="hljs-name">LinearLayout</span> <span class="hljs-attr">xmlns:android</span>=<span class="hljs-string">"http://schemas.android.com/apk/res/android"</span>
    <span class="hljs-attr">xmlns:app</span>=<span class="hljs-string">"http://schemas.android.com/apk/res-auto"</span>
    <span class="hljs-attr">xmlns:tools</span>=<span class="hljs-string">"http://schemas.android.com/tools"</span>
    <span class="hljs-attr">android:layout_width</span>=<span class="hljs-string">"match_parent"</span>
    <span class="hljs-attr">android:layout_height</span>=<span class="hljs-string">"match_parent"</span>
    <span class="hljs-attr">android:orientation</span>=<span class="hljs-string">"vertical"</span>
    <span class="hljs-attr">tools:context</span>=<span class="hljs-string">".activity.DrivingRouteActivity"</span>></span>
 
    <span class="hljs-tag"><<span class="hljs-name">com.tencent.tencentmap.mapsdk.maps.MapView</span>
        <span class="hljs-attr">android:id</span>=<span class="hljs-string">"@+id/mapview"</span>
        <span class="hljs-attr">android:layout_width</span>=<span class="hljs-string">"match_parent"</span>
        <span class="hljs-attr">android:layout_height</span>=<span class="hljs-string">"wrap_content"</span>
        <span class="hljs-attr">android:layout_weight</span>=<span class="hljs-string">"1"</span>/></span>
 
    <span class="hljs-tag"><<span class="hljs-name">LinearLayout</span>
        <span class="hljs-attr">android:layout_width</span>=<span class="hljs-string">"match_parent"</span>
        <span class="hljs-attr">android:layout_height</span>=<span class="hljs-string">"wrap_content"</span>
        <span class="hljs-attr">android:orientation</span>=<span class="hljs-string">"vertical"</span>
        <span class="hljs-attr">android:gravity</span>=<span class="hljs-string">"bottom"</span>
        <span class="hljs-attr">android:paddingTop</span>=<span class="hljs-string">"10dp"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">LinearLayout</span>
            <span class="hljs-attr">android:layout_width</span>=<span class="hljs-string">"match_parent"</span>
            <span class="hljs-attr">android:layout_height</span>=<span class="hljs-string">"wrap_content"</span>
            <span class="hljs-attr">android:orientation</span>=<span class="hljs-string">"horizontal"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">EditText</span>
                <span class="hljs-attr">android:id</span>=<span class="hljs-string">"@+id/from_et"</span>
                <span class="hljs-attr">android:hint</span>=<span class="hljs-string">"您在哪儿上车"</span>
                <span class="hljs-attr">android:layout_weight</span>=<span class="hljs-string">"1"</span>
                <span class="hljs-attr">android:layout_marginTop</span>=<span class="hljs-string">"10dp"</span>
                <span class="hljs-attr">android:layout_marginBottom</span>=<span class="hljs-string">"10dp"</span>
                <span class="hljs-attr">android:layout_marginLeft</span>=<span class="hljs-string">"10dp"</span>
                <span class="hljs-attr">android:layout_width</span>=<span class="hljs-string">"match_parent"</span>
                <span class="hljs-attr">android:layout_height</span>=<span class="hljs-string">"50dp"</span>></span><span class="hljs-tag"></<span class="hljs-name">EditText</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">ImageButton</span>
                <span class="hljs-attr">android:id</span>=<span class="hljs-string">"@+id/location_ib"</span>
                <span class="hljs-attr">android:background</span>=<span class="hljs-string">"@drawable/sendtocar_balloon"</span>
                <span class="hljs-attr">android:layout_marginTop</span>=<span class="hljs-string">"10dp"</span>
                <span class="hljs-attr">android:layout_marginBottom</span>=<span class="hljs-string">"10dp"</span>
                <span class="hljs-attr">android:layout_marginRight</span>=<span class="hljs-string">"10dp"</span>
                <span class="hljs-attr">android:layout_width</span>=<span class="hljs-string">"50dp"</span>
                <span class="hljs-attr">android:layout_height</span>=<span class="hljs-string">"50dp"</span>></span><span class="hljs-tag"></<span class="hljs-name">ImageButton</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">LinearLayout</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">EditText</span>
            <span class="hljs-attr">android:id</span>=<span class="hljs-string">"@+id/to_et"</span>
            <span class="hljs-attr">android:hint</span>=<span class="hljs-string">"您要去哪儿"</span>
            <span class="hljs-attr">android:layout_width</span>=<span class="hljs-string">"match_parent"</span>
            <span class="hljs-attr">android:layout_height</span>=<span class="hljs-string">"50dp"</span>
            <span class="hljs-attr">android:layout_marginBottom</span>=<span class="hljs-string">"5dp"</span>
            <span class="hljs-attr">android:layout_marginLeft</span>=<span class="hljs-string">"10dp"</span>
            <span class="hljs-attr">android:layout_marginRight</span>=<span class="hljs-string">"10dp"</span>></span><span class="hljs-tag"></<span class="hljs-name">EditText</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">TextView</span>
            <span class="hljs-attr">android:id</span>=<span class="hljs-string">"@+id/orderdesc_tv"</span>
            <span class="hljs-attr">android:layout_width</span>=<span class="hljs-string">"match_parent"</span>
            <span class="hljs-attr">android:layout_height</span>=<span class="hljs-string">"wrap_content"</span>
            <span class="hljs-attr">android:gravity</span>=<span class="hljs-string">"center"</span>
            <span class="hljs-attr">android:textSize</span>=<span class="hljs-string">"20sp"</span>></span><span class="hljs-tag"></<span class="hljs-name">TextView</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Button</span>
            <span class="hljs-attr">android:id</span>=<span class="hljs-string">"@+id/confirm_btn"</span>
            <span class="hljs-attr">android:text</span>=<span class="hljs-string">"确定"</span>
            <span class="hljs-attr">android:layout_width</span>=<span class="hljs-string">"match_parent"</span>
            <span class="hljs-attr">android:layout_height</span>=<span class="hljs-string">"50dp"</span>
            <span class="hljs-attr">android:layout_marginBottom</span>=<span class="hljs-string">"10dp"</span>
            <span class="hljs-attr">android:layout_marginLeft</span>=<span class="hljs-string">"10dp"</span>
            <span class="hljs-attr">android:layout_marginRight</span>=<span class="hljs-string">"10dp"</span>
            <span class="hljs-attr">android:visibility</span>=<span class="hljs-string">"gone"</span>></span><span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">Button</span>
            <span class="hljs-attr">android:id</span>=<span class="hljs-string">"@+id/order_btn"</span>
            <span class="hljs-attr">android:text</span>=<span class="hljs-string">"预约快车"</span>
            <span class="hljs-attr">android:layout_width</span>=<span class="hljs-string">"match_parent"</span>
            <span class="hljs-attr">android:layout_height</span>=<span class="hljs-string">"50dp"</span>
            <span class="hljs-attr">android:layout_marginBottom</span>=<span class="hljs-string">"10dp"</span>
            <span class="hljs-attr">android:layout_marginLeft</span>=<span class="hljs-string">"10dp"</span>
            <span class="hljs-attr">android:layout_marginRight</span>=<span class="hljs-string">"10dp"</span>></span><span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">LinearLayout</span>></span>
 
<span class="hljs-tag"></<span class="hljs-name">LinearLayout</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">1.账号注册与配置</h3>
<p>在开发之前，我们需要到腾讯位置服务官网注册一个账号
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ffa5e2abc524986b89378903be3afe0~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"> 注册后进入控制台
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01cd4ea0e5e74575b7cf5fb902e64418~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer">选择key管理，点击创建新秘钥，按照申请信息提交申请</p>
<p>将上面申请的key在application标签下进行如下配置（value替换成自己的key）</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">meta-data</span>
    <span class="hljs-attr">android:name</span>=<span class="hljs-string">"TencentMapSDK"</span>
    <span class="hljs-attr">android:value</span>=<span class="hljs-string">"XXXXX-XXXXX-XXXXX-XXXXX-XXXXX-XXXXX"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9996b0fa1b0345d58d7526c02e6b9dd5~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">2.引入腾讯Android地图SDK</h3>
<p>进入Android地图SDK，下载3D版地图SDK压缩包
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83ecc782702b4c16befeb5c1a9fa5746~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer">下载完成后打开压缩包，将libs文件夹下的jar包拷贝到app的libs目录下，右键该jar包选择add as library添加为依赖，并且在项目app\src\main路径下建立名为jniLibs的目录，把压缩包libs/jniLibs/strip文件夹下的所有包放到jniLibs目录下
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b1f799707f8471997fb2a97fc85bbdc~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer">引入后在AndroidManifest.xml文件下配置相关权限</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-comment"><!-- 访问网络获取地图服务 --></span>
<span class="hljs-tag"><<span class="hljs-name">uses-permission</span> <span class="hljs-attr">android:name</span>=<span class="hljs-string">"android.permission.INTERNET"</span> /></span>
<span class="hljs-comment"><!-- 检查网络可用性 --></span>
<span class="hljs-tag"><<span class="hljs-name">uses-permission</span> <span class="hljs-attr">android:name</span>=<span class="hljs-string">"android.permission.ACCESS_NETWORK_STATE"</span> /></span>
<span class="hljs-comment"><!-- 访问WiFi状态 --></span>
<span class="hljs-tag"><<span class="hljs-name">uses-permission</span> <span class="hljs-attr">android:name</span>=<span class="hljs-string">"android.permission.ACCESS_WIFI_STATE"</span> /></span>
<span class="hljs-comment"><!-- 需要外部存储写权限用于保存地图缓存 --></span>
<span class="hljs-tag"><<span class="hljs-name">uses-permission</span> <span class="hljs-attr">android:name</span>=<span class="hljs-string">"android.permission.WRITE_EXTERNAL_STORAGE"</span> /></span>
<span class="hljs-comment"><!-- 获取 device id 辨别设备 --></span>
<span class="hljs-tag"><<span class="hljs-name">uses-permission</span> <span class="hljs-attr">android:name</span>=<span class="hljs-string">"android.permission.READ_PHONE_STATE"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">3.地图初始化</h3>
<p>配置完成，现在开始实现我们的逻辑交互，为了让实现逻辑更加清晰，我将业务逻辑代码与视图渲染代码分到了两个包中，除了activity包中的DrivingRouteActivity之外，新建了一个present包，并在包下建立一个DrivingRoutePresent类，分别由DrivingRouteActivity负责对UI组件进行视图渲染，由DrivingRoutePresent类负责业务逻辑。这里我还新建了一个contract包，并创建一个DrivingRouteContract接口，通过这个接口定义的方法，实现DrivingRoutePresent与DrivingRouteActivity之间的交互。我们在DrivingRouteContract接口中定义两个接口，一个View接口供DrivingRouteActivity实现，一个Presenter接口供DrivingRoutePresent实现，并定义一些初始化的方法</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">DrivingRouteContract</span> </span>&#123;
    
    <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">View</span></span>&#123;
        <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">initView</span><span class="hljs-params">()</span></span>;<span class="hljs-comment">//初始化View</span>
        <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">initOnClick</span><span class="hljs-params">()</span></span>;<span class="hljs-comment">//初始化OnClickListener</span>
        <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">setOrderDescTV</span><span class="hljs-params">(String content)</span></span>;<span class="hljs-comment">//渲染订单行程信息</span>
        <span class="hljs-function">EditText <span class="hljs-title">getFromET</span><span class="hljs-params">()</span></span>;
    &#125;
 
    <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">Presenter</span></span>&#123;
        <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">attachView</span><span class="hljs-params">(DrivingRouteContract.View view)</span></span>;<span class="hljs-comment">//绑定View</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着再让DrivingRouteActivity实现DrivingRouteContract.View接口并声明UI中的组件进行初始化</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">DrivingRouteActivity</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Activity</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">DrivingRouteContract</span>.<span class="hljs-title">View</span>, <span class="hljs-title">View</span>.<span class="hljs-title">OnClickListener</span> </span>&#123;
    <span class="hljs-keyword">private</span> MapView mapView;
    <span class="hljs-keyword">private</span> TencentMap mMap;
    <span class="hljs-keyword">private</span> Button confirmBtn;
    <span class="hljs-keyword">private</span> Button orderBtn;
    <span class="hljs-keyword">private</span> ImageButton locationIB;
    <span class="hljs-keyword">private</span> EditText fromET;
    <span class="hljs-keyword">private</span> EditText toET;
    <span class="hljs-keyword">private</span> TextView orderDescTV;
   <span class="hljs-keyword">private</span> DrivingRoutePresent drivingRoutePresent;
 
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onCreate</span><span class="hljs-params">(Bundle savedInstanceState)</span> </span>&#123;
        <span class="hljs-keyword">super</span>.onCreate(savedInstanceState);
        setContentView(R.layout.activity_driving_route);
        initView();
        initOnClick();
    &#125;
 
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onClick</span><span class="hljs-params">(View view)</span> </span>&#123;
        <span class="hljs-keyword">switch</span> (view.getId())&#123;
            <span class="hljs-keyword">case</span> R.id.order_btn:
                <span class="hljs-comment">//实现行程路线规划</span>
                <span class="hljs-keyword">break</span>;
            <span class="hljs-keyword">case</span> R.id.confirm_btn:
                <span class="hljs-comment">//开启动画移动</span>
                <span class="hljs-keyword">break</span>;
            <span class="hljs-keyword">case</span> R.id.location_ib:
                <span class="hljs-comment">//定位当前位置</span>
                <span class="hljs-keyword">break</span>;
        &#125;
    &#125;
 
    <span class="hljs-comment">/**
     * mapview的生命周期管理
     */</span>
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onStart</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">super</span>.onStart();
        mapView.onStart();
    &#125;
 
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onResume</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">super</span>.onResume();
        mapView.onResume();
    &#125;
 
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onPause</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">super</span>.onPause();
        mapView.onPause();
    &#125;
 
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onStop</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">super</span>.onStop();
        mapView.onStop();
    &#125;
 
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onDestroy</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">super</span>.onDestroy();
        mapView.onDestroy();
    &#125;
 
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onRestart</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">super</span>.onRestart();
        mapView.onRestart();
    &#125;
 
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">initView</span><span class="hljs-params">()</span> </span>&#123;
        mapView = findViewById(R.id.mapview);
        confirmBtn = findViewById(R.id.confirm_btn);
        orderBtn = findViewById(R.id.order_btn);
        locationIB = findViewById(R.id.location_ib);
        fromET = findViewById(R.id.from_et);
        toET = findViewById(R.id.to_et);
        orderDescTV = findViewById(R.id.orderdesc_tv);
        mMap = mapView.getMap();
 
        drivingRoutePresent = <span class="hljs-keyword">new</span> DrivingRoutePresent();
        drivingRoutePresent.attachView(<span class="hljs-keyword">this</span>);
    &#125;
 
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">initOnClick</span><span class="hljs-params">()</span> </span>&#123;
        orderBtn.setOnClickListener(<span class="hljs-keyword">this</span>);
        confirmBtn.setOnClickListener(<span class="hljs-keyword">this</span>);
        locationIB.setOnClickListener(<span class="hljs-keyword">this</span>);
    &#125;
    
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">setOrderDescTV</span><span class="hljs-params">(String content)</span> </span>&#123;
        orderDescTV.setText(content);
    &#125;
 
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> EditText <span class="hljs-title">getFromET</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">return</span> fromET;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>DrivingRoutePresent实现DrivingRouteContract.Presenter接口</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">DrivingRoutePresent</span> <span class="hljs-keyword">implements</span> <span class="hljs-title">DrivingRouteContract</span>.<span class="hljs-title">Presenter</span> </span>&#123;
    
    <span class="hljs-keyword">private</span> DrivingRouteContract.View drinvingRouteView;
    
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">attachView</span><span class="hljs-params">(DrivingRouteContract.View view)</span> </span>&#123;
        drinvingRouteView = view;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为我们后面在多个地方都需要用到当前应用的上下文，为了方便，需要再编写一个全局的应用上下文工具类来帮助我们获取上下文，建立一个util包并创建一个GlobalApplication类</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">GlobalApplication</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Application</span> </span>&#123;
 
    <span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> Context context;
 
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onCreate</span><span class="hljs-params">()</span> </span>&#123;
        <span class="hljs-keyword">super</span>.onCreate();
        context = getApplicationContext();
    &#125;
 
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> Context <span class="hljs-title">getContext</span><span class="hljs-params">()</span></span>&#123;
        <span class="hljs-keyword">return</span> context;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时，在Android类文件的application标签中加入下面属性，让应用启动时加载上面的GlobalApplication</p>
<pre><code class="hljs language-java copyable" lang="java">android:name=<span class="hljs-string">".util.GlobalApplication"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>到这里，我们就完成了界面与业务代码的基本设计，运行app，可以看到显示的基本地图信息。接下来我们来实现一下路线规划的功能。腾讯官方Android地图SDK开发文档对路线规划服务和地址解析都有较详细的说明。
另外还提供了调用示例Demo。如果不清楚如何调用的话可以参考官方Demo或参考下面代码。</p>
<h3 data-id="heading-5">4.地址解析与路线规划</h3>
<p>首先我们在DrivingRouteContract.Presenter接口申明一个用于通过地址查找经纬度的geocoder方法和一个用于路线规划的routePlan方法</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">DrivingRouteContract</span> </span>&#123;
    
    <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">View</span></span>&#123;
        <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">initView</span><span class="hljs-params">()</span></span>;<span class="hljs-comment">//初始化View</span>
        <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">initOnClick</span><span class="hljs-params">()</span></span>;<span class="hljs-comment">//初始化OnClickListener</span>
        <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">setOrderDescTV</span><span class="hljs-params">(String content)</span></span>;<span class="hljs-comment">//渲染订单行程信息</span>
        <span class="hljs-function">EditText <span class="hljs-title">getFromET</span><span class="hljs-params">()</span></span>;
    &#125;
 
    <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">Presenter</span></span>&#123;
        <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">attachView</span><span class="hljs-params">(DrivingRouteContract.View view)</span></span>;<span class="hljs-comment">//绑定View</span>
        <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">geocoder</span><span class="hljs-params">(String address, Integer type)</span></span>;<span class="hljs-comment">//地址解码，转经纬度</span>
        <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">routePlan</span><span class="hljs-params">()</span></span>;<span class="hljs-comment">//实现路线规划</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过腾讯Android地图SDK路线规划服务的开发文档，我们了解到要获得规划路线需要先获取起点和终点的经纬度，而在一般业务场景中，我们几乎不会让用户手动输入经纬度，所以我这里还需要用到地址解析服务，通过输入中文地址来获取经纬度，再通过经纬度规划路线（不过在实际业务中最好是加上关键词输入提示这个服务，方便用户找到输入的位置）。</p>
<p>在DrivingRoutePresent类中实现这两个方法</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">final</span> Integer FROM_TYPE = <span class="hljs-number">0x100</span>; <span class="hljs-comment">//获取起始位置坐标</span>
<span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">final</span> Integer TO_TYPE = <span class="hljs-number">0x101</span>; <span class="hljs-comment">//获取目的位置坐标</span>
<span class="hljs-keyword">private</span> LatLng fromLatLng;
<span class="hljs-keyword">private</span> LatLng toLatLng;
 
<span class="hljs-comment">/**
 * 地址解码
 * <span class="hljs-doctag">@param</span> address 传入需要解码的地址
 * <span class="hljs-doctag">@param</span> type 地址类型，起始位置、目的位置
 */</span>
<span class="hljs-meta">@Override</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">geocoder</span><span class="hljs-params">(String address, <span class="hljs-keyword">final</span> Integer type)</span> </span>&#123;
    TencentSearch tencentSearch = <span class="hljs-keyword">new</span> TencentSearch(GlobalApplication.getContext());
    Address2GeoParam address2GeoParam =
            <span class="hljs-keyword">new</span> Address2GeoParam(address);
    tencentSearch.address2geo(address2GeoParam, <span class="hljs-keyword">new</span> HttpResponseListener<BaseObject>() &#123;
 
        <span class="hljs-meta">@Override</span>
        <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onSuccess</span><span class="hljs-params">(<span class="hljs-keyword">int</span> arg0, BaseObject arg1)</span> </span>&#123;
            <span class="hljs-keyword">if</span> (arg1 == <span class="hljs-keyword">null</span>) &#123;
                <span class="hljs-keyword">return</span>;
            &#125;
            Address2GeoResultObject obj = (Address2GeoResultObject)arg1;
            <span class="hljs-keyword">if</span> (obj.result.latLng != <span class="hljs-keyword">null</span>) &#123;
                <span class="hljs-keyword">if</span> (type==FROM_TYPE)
                    fromLatLng = obj.result.latLng;
                <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (type==TO_TYPE)
                    toLatLng = obj.result.latLng;
                routePlan();
            &#125;
        &#125;
 
        <span class="hljs-meta">@Override</span>
        <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onFailure</span><span class="hljs-params">(<span class="hljs-keyword">int</span> arg0, String arg1, Throwable arg2)</span> </span>&#123;
            Log.e(<span class="hljs-string">"test"</span>, <span class="hljs-string">"error code:"</span> + arg0 + <span class="hljs-string">", msg:"</span> + arg1);
        &#125;
    &#125;);
&#125;
 
<span class="hljs-keyword">private</span> TencentSearch tencentSearch = <span class="hljs-keyword">new</span> TencentSearch(GlobalApplication.getContext());
<span class="hljs-keyword">private</span> StringBuffer lineStringBuilder = <span class="hljs-keyword">new</span> StringBuffer();<span class="hljs-comment">//路线坐标</span>
<span class="hljs-keyword">private</span> Double taxiFare = <span class="hljs-number">0d</span>;<span class="hljs-comment">//预估打车费用</span>
<span class="hljs-keyword">private</span> Float distance = <span class="hljs-number">0f</span>;<span class="hljs-comment">//预计全程里程</span>
 
<span class="hljs-comment">/**
 * 路线规划
 */</span>
<span class="hljs-meta">@Override</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">routePlan</span><span class="hljs-params">()</span> </span>&#123;
    <span class="hljs-keyword">if</span> (fromLatLng!=<span class="hljs-keyword">null</span>&&toLatLng!=<span class="hljs-keyword">null</span>)&#123;
        Toast.makeText(GlobalApplication.getContext(), <span class="hljs-string">"正在为您规划路线"</span>, Toast.LENGTH_SHORT).show();
        DrivingParam drivingParam = <span class="hljs-keyword">new</span> DrivingParam(fromLatLng, toLatLng);
        drivingParam.policy(DrivingParam.Policy.TRIP);<span class="hljs-comment">//驾车路线规划策略，网约车场景，送乘客</span>
        drivingParam.setCarNumber(<span class="hljs-string">"粤A00001"</span>);<span class="hljs-comment">//填入车牌号，在路线规划时会避让车牌限行区域</span>
        tencentSearch.getRoutePlan(drivingParam, <span class="hljs-keyword">new</span> HttpResponseListener<DrivingResultObject>() &#123;
 
            <span class="hljs-meta">@Override</span>
            <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onSuccess</span><span class="hljs-params">(<span class="hljs-keyword">int</span> i, DrivingResultObject drivingResultObject)</span> </span>&#123;
                <span class="hljs-keyword">for</span> (DrivingResultObject.Route route : drivingResultObject.result.routes)&#123;
                    <span class="hljs-keyword">for</span> (LatLng latLng : route.polyline)&#123;
                        lineStringBuilder.append(latLng.latitude + <span class="hljs-string">","</span> + latLng.longitude);
                        lineStringBuilder.append(<span class="hljs-string">","</span>);
                    &#125;
                    distance += route.distance;
                    taxiFare += route.taxi_fare.fare;
                &#125;
                drinvingRouteView.setOrderDescTV(<span class="hljs-string">"行程大约"</span> + distance + <span class="hljs-string">"m,预计¥"</span> + taxiFare + <span class="hljs-string">"元"</span>);
 
                <span class="hljs-comment">//清空行程路线，里程，费用信息</span>
                lineStringBuilder = <span class="hljs-keyword">new</span> StringBuffer();
                distance = <span class="hljs-number">0f</span>;
                taxiFare = <span class="hljs-number">0d</span>;
            &#125;
 
            <span class="hljs-meta">@Override</span>
            <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onFailure</span><span class="hljs-params">(<span class="hljs-keyword">int</span> i, String s, Throwable throwable)</span> </span>&#123;
                Log.d(<span class="hljs-string">"DrivingRouteActivity"</span>, <span class="hljs-string">"onSuccess: "</span> + s + i);
            &#125;
        &#125;);
 
        fromLatLng=<span class="hljs-keyword">null</span>;
        toLatLng=<span class="hljs-keyword">null</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中geocoder方法用于获得我们输入的起始位置（从哪儿上车），以及输入的目的位置（到哪儿下车）的坐标经纬度，记录位置的经纬度后调用routePlan方法请求路线规划接口，并记录下里程，费用信息，路线行驶过程中经过的点的经纬度（用于后面实现小车移动）。</p>
<p>路线规划接口除了上面使用的几个常用参数外，还有很多接口参数，具体可以查看官方接口文档按需要加入</p>
<blockquote>
<p>参考官方接口文档：<a href="https://link.juejin.cn/?target=https%3A%2F%2Flbs.qq.com%2FAndroidDocs%2Fdoc_3d%2Findex.html" target="_blank" rel="nofollow noopener noreferrer" title="https://lbs.qq.com/AndroidDocs/doc_3d/index.html" ref="nofollow noopener noreferrer">lbs.qq.com/AndroidDocs…</a></p>
</blockquote>
<h3 data-id="heading-6">5.车辆行驶动画</h3>
<p>有了路线规划方法后，给"预约快车"按钮添加实现</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@Override</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onClick</span><span class="hljs-params">(View view)</span> </span>&#123;
    <span class="hljs-keyword">switch</span> (view.getId())&#123;
        <span class="hljs-keyword">case</span> R.id.order_btn:
            drivingRoutePresent.geocoder(fromET.getText().toString(), DrivingRoutePresent.FROM_TYPE);
            drivingRoutePresent.geocoder(toET.getText().toString(), DrivingRoutePresent.TO_TYPE);
            confirmBtn.setVisibility(View.VISIBLE);
            orderBtn.setVisibility(View.GONE);
            <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> R.id.confirm_btn:
            <span class="hljs-comment">//开启动画移动</span>
            <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> R.id.location_ib:
            <span class="hljs-comment">//定位当前位置</span>
            <span class="hljs-keyword">break</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时，运行APP，输入起点和终点就可以获得驾车的规划路线了</p>
<p>接下来，我们再实现一下效果图上小车根据规划路线行驶的功能</p>
<p>在DrivingRouteContract.View接口中加入小车动画初始化方法initAnimation</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">DrivingRouteContract</span> </span>&#123;
 
    <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">Model</span></span>&#123;
    &#125;
 
    <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">View</span></span>&#123;
        <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">initView</span><span class="hljs-params">()</span></span>;<span class="hljs-comment">//初始化View</span>
        <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">initOnClick</span><span class="hljs-params">()</span></span>;<span class="hljs-comment">//初始化OnClickListener</span>
        <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">setOrderDescTV</span><span class="hljs-params">(String content)</span></span>;<span class="hljs-comment">//渲染订单行程信息</span>
        <span class="hljs-function">EditText <span class="hljs-title">getFromET</span><span class="hljs-params">()</span></span>;
        <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">initAnimation</span><span class="hljs-params">(String line)</span></span>;<span class="hljs-comment">//初始化小车移动动画</span>
    &#125;
 
    <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">Presenter</span></span>&#123;
        <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">attachView</span><span class="hljs-params">(DrivingRouteContract.View view)</span></span>;<span class="hljs-comment">//绑定View</span>
        <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">startLocation</span><span class="hljs-params">(<span class="hljs-keyword">boolean</span> single)</span></span>;
        <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">stopLocation</span><span class="hljs-params">()</span></span>;
        <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">geocoder</span><span class="hljs-params">(String address, Integer type)</span></span>;<span class="hljs-comment">//地址解码，转经纬度</span>
        <span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">routePlan</span><span class="hljs-params">()</span></span>;<span class="hljs-comment">//实现路线规划</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现initAnimation方法，关于Marker其他参数同样参考上面的接口文档</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">private</span> Marker mCarMarker;
<span class="hljs-keyword">private</span> LatLng[] mCarLatLngArray;
<span class="hljs-keyword">private</span> MarkerTranslateAnimator mAnimator;
 
<span class="hljs-meta">@Override</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">initAnimation</span><span class="hljs-params">(String line)</span> </span>&#123;
    <span class="hljs-comment">//拆分获得经纬度数组</span>
    String[] linePointsStr = line.split(<span class="hljs-string">","</span>);
    mCarLatLngArray = <span class="hljs-keyword">new</span> LatLng[linePointsStr.length / <span class="hljs-number">2</span>];
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">int</span> i = <span class="hljs-number">0</span>; i < mCarLatLngArray.length; i++) &#123;
        <span class="hljs-keyword">double</span> latitude = Double.parseDouble(linePointsStr[i * <span class="hljs-number">2</span>]);
        <span class="hljs-keyword">double</span> longitude = Double.parseDouble(linePointsStr[i * <span class="hljs-number">2</span> + <span class="hljs-number">1</span>]);
        mCarLatLngArray[i] = <span class="hljs-keyword">new</span> LatLng(latitude, longitude);
    &#125;
 
    <span class="hljs-comment">//添加小车路线</span>
    mMap.addPolyline(<span class="hljs-keyword">new</span> PolylineOptions().add(mCarLatLngArray)
        .color(R.color.colorLine));<span class="hljs-comment">//这个颜色是colors.xml中自定义的颜色</span>
 
    <span class="hljs-comment">//添加小车</span>
    LatLng carLatLng = mCarLatLngArray[<span class="hljs-number">0</span>];
    mCarMarker = mMap.addMarker(
            <span class="hljs-keyword">new</span> MarkerOptions(carLatLng)
                    .anchor(<span class="hljs-number">0.5f</span>, <span class="hljs-number">0.5f</span>)
                    .icon(BitmapDescriptorFactory.fromResource(R.mipmap.taxi_t))<span class="hljs-comment">//小车图标</span>
                    .flat(<span class="hljs-keyword">true</span>)
                    .clockwise(<span class="hljs-keyword">false</span>));
 
    <span class="hljs-comment">//创建移动动画</span>
    mAnimator = <span class="hljs-keyword">new</span> MarkerTranslateAnimator(mCarMarker, <span class="hljs-number">50</span> * <span class="hljs-number">1000</span>, mCarLatLngArray, <span class="hljs-keyword">true</span>);
 
    <span class="hljs-comment">//调整最佳视野</span>
    mMap.animateCamera(CameraUpdateFactory.newLatLngBounds(
            LatLngBounds.builder().include(Arrays.asList(mCarLatLngArray)).build(), <span class="hljs-number">50</span>));
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>并在routePlan方法中调用这个方法，传入行驶路线字符串</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">//初始化小车动画</span>
drinvingRouteView.initAnimation(lineStringBuilder.substring(<span class="hljs-number">0</span>, lineStringBuilder.length()-<span class="hljs-number">1</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完整代码参考</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-comment">/**
 * 路线规划
 */</span>
<span class="hljs-meta">@Override</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">routePlan</span><span class="hljs-params">()</span> </span>&#123;
    <span class="hljs-keyword">if</span> (fromLatLng!=<span class="hljs-keyword">null</span>&&toLatLng!=<span class="hljs-keyword">null</span>)&#123;
        Toast.makeText(GlobalApplication.getContext(), <span class="hljs-string">"正在为您规划路线"</span>, Toast.LENGTH_SHORT).show();
        DrivingParam drivingParam = <span class="hljs-keyword">new</span> DrivingParam(fromLatLng, toLatLng);
        drivingParam.policy(DrivingParam.Policy.TRIP);<span class="hljs-comment">//驾车路线规划策略，网约车场景，送乘客</span>
        drivingParam.setCarNumber(<span class="hljs-string">"粤A00001"</span>);<span class="hljs-comment">//填入车牌号，在路线规划时会避让车牌限行区域</span>
        tencentSearch.getRoutePlan(drivingParam, <span class="hljs-keyword">new</span> HttpResponseListener<DrivingResultObject>() &#123;
 
            <span class="hljs-meta">@Override</span>
            <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onSuccess</span><span class="hljs-params">(<span class="hljs-keyword">int</span> i, DrivingResultObject drivingResultObject)</span> </span>&#123;
                <span class="hljs-keyword">for</span> (DrivingResultObject.Route route : drivingResultObject.result.routes)&#123;
                    <span class="hljs-keyword">for</span> (LatLng latLng : route.polyline)&#123;
                        lineStringBuilder.append(latLng.latitude + <span class="hljs-string">","</span> + latLng.longitude);
                        lineStringBuilder.append(<span class="hljs-string">","</span>);
                    &#125;
                    distance += route.distance;
                    taxiFare += route.taxi_fare.fare;
                &#125;
                <span class="hljs-comment">//初始化小车动画</span>
                drinvingRouteView.initAnimation(lineStringBuilder.substring(<span class="hljs-number">0</span>, lineStringBuilder.length()-<span class="hljs-number">1</span>));
                drinvingRouteView.setOrderDescTV(<span class="hljs-string">"行程大约"</span> + distance + <span class="hljs-string">"m,预计¥"</span> + taxiFare + <span class="hljs-string">"元"</span>);
 
                <span class="hljs-comment">//清空行程路线，里程，费用信息</span>
                lineStringBuilder = <span class="hljs-keyword">new</span> StringBuffer();
                distance = <span class="hljs-number">0f</span>;
                taxiFare = <span class="hljs-number">0d</span>;
            &#125;
 
            <span class="hljs-meta">@Override</span>
            <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onFailure</span><span class="hljs-params">(<span class="hljs-keyword">int</span> i, String s, Throwable throwable)</span> </span>&#123;
                Log.d(<span class="hljs-string">"DrivingRouteActivity"</span>, <span class="hljs-string">"onSuccess: "</span> + s + i);
            &#125;
        &#125;);
 
        fromLatLng=<span class="hljs-keyword">null</span>;
        toLatLng=<span class="hljs-keyword">null</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后我们在"确定"按钮的点击事件上调用MarkerTranslateAnimator的startAnimation方法来开始动画</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@Override</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onClick</span><span class="hljs-params">(View view)</span> </span>&#123;
    <span class="hljs-keyword">switch</span> (view.getId())&#123;
        <span class="hljs-keyword">case</span> R.id.order_btn:
            drivingRoutePresent.geocoder(fromET.getText().toString(), DrivingRoutePresent.FROM_TYPE);
            drivingRoutePresent.geocoder(toET.getText().toString(), DrivingRoutePresent.TO_TYPE);
            confirmBtn.setVisibility(View.VISIBLE);
            orderBtn.setVisibility(View.GONE);
            <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> R.id.confirm_btn:
            <span class="hljs-comment">//开启动画移动</span>
            mAnimator.startAnimation();
            orderBtn.setVisibility(View.VISIBLE);
            confirmBtn.setVisibility(View.GONE);
            <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> R.id.location_ib:
            <span class="hljs-comment">//定位当前位置</span>
            <span class="hljs-keyword">break</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">6.引入腾讯Android定位SDK</h3>
<p>基本效果已经完成了，现在还差最后一个定位功能，要实现定位功能需要引入另一个SDK（Android定位SDK）</p>
<p>我们打开Android定位SDK开发文档，下载最新的SDK
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7be616e149d5437c9573cafae48e0d68~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer">将压缩包内的jar包放入app的libs包下，并添加为依赖
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57d7c638d14c4282ace5b9679a353180~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer">再把压缩包libs文件夹下的各个so文件拷贝到项目jniLibs的对应目录中
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7f6ddcc287e47f1a078951d6084c0fa~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24cefb4cef36410985633f8f491cfe8f~tplv-k3u1fbpfcp-no-mark:1280:960:0:0.image" alt loading="lazy" referrerpolicy="no-referrer">打开AndroidManifest.xml文件，加入下面权限配置</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-comment"><!-- 通过GPS得到精确位置 --></span>
<span class="hljs-tag"><<span class="hljs-name">uses-permission</span> <span class="hljs-attr">android:name</span>=<span class="hljs-string">"android.permission.ACCESS_FINE_LOCATION"</span> /></span>
<span class="hljs-comment"><!-- 通过网络得到粗略位置 --></span>
<span class="hljs-tag"><<span class="hljs-name">uses-permission</span> <span class="hljs-attr">android:name</span>=<span class="hljs-string">"android.permission.ACCESS_COARSE_LOCATION"</span> /></span>
<span class="hljs-comment"><!-- 访问网络. 某些位置信息需要从网络服务器获取 --></span>
<span class="hljs-tag"><<span class="hljs-name">uses-permission</span> <span class="hljs-attr">android:name</span>=<span class="hljs-string">"android.permission.INTERNET"</span> /></span>
<span class="hljs-comment"><!-- 访问WiFi状态. 需要WiFi信息用于网络定位 --></span>
<span class="hljs-tag"><<span class="hljs-name">uses-permission</span> <span class="hljs-attr">android:name</span>=<span class="hljs-string">"android.permission.ACCESS_WIFI_STATE"</span> /></span>
<span class="hljs-comment"><!-- 修改WiFi状态. 发起WiFi扫描, 需要WiFi信息用于网络定位 --></span>
<span class="hljs-tag"><<span class="hljs-name">uses-permission</span> <span class="hljs-attr">android:name</span>=<span class="hljs-string">"android.permission.CHANGE_WIFI_STATE"</span> /></span>
<span class="hljs-comment"><!-- 访问网络状态, 检测网络的可用性. 需要网络运营商相关信息用于网络定位 --></span>
<span class="hljs-tag"><<span class="hljs-name">uses-permission</span> <span class="hljs-attr">android:name</span>=<span class="hljs-string">"android.permission.ACCESS_NETWORK_STATE"</span> /></span>
<span class="hljs-comment"><!-- 访问网络的变化, 需要某些信息用于网络定位 --></span>
<span class="hljs-tag"><<span class="hljs-name">uses-permission</span> <span class="hljs-attr">android:name</span>=<span class="hljs-string">"android.permission.CHANGE_NETWORK_STATE"</span> /></span>
<span class="hljs-comment"><!-- 访问手机当前状态, 需要device id用于网络定位 --></span>
<span class="hljs-tag"><<span class="hljs-name">uses-permission</span> <span class="hljs-attr">android:name</span>=<span class="hljs-string">"android.permission.READ_PHONE_STATE"</span> /></span>
<span class="hljs-comment"><!-- 支持A-GPS辅助定位 --></span>
<span class="hljs-tag"><<span class="hljs-name">uses-permission</span> <span class="hljs-attr">android:name</span>=<span class="hljs-string">"android.permission.ACCESS_LOCATION_EXTRA_COMMANDS"</span> /></span>
<span class="hljs-comment"><!-- 用于 log 日志 --></span>
<span class="hljs-tag"><<span class="hljs-name">uses-permission</span> <span class="hljs-attr">android:name</span>=<span class="hljs-string">"android.permission.WRITE_EXTERNAL_STORAGE"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">7.显示当前定位</h3>
<p>配置完成后，我们在DrivingRouteContract.Presenter接口中加入一个开始定位的startLocation和一个结束定位的stopLocation方法</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">startLocation</span><span class="hljs-params">(<span class="hljs-keyword">boolean</span> single)</span></span>;
<span class="hljs-function"><span class="hljs-keyword">void</span> <span class="hljs-title">stopLocation</span><span class="hljs-params">()</span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再实现一下DrivingRoutePresent的方法</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-keyword">private</span> <span class="hljs-keyword">boolean</span> IS_SINGLE_LOCATION_MODE = <span class="hljs-keyword">false</span>;<span class="hljs-comment">//是否连续定位</span>
<span class="hljs-keyword">private</span> TencentLocationManager mLocationManager = TencentLocationManager.getInstance(GlobalApplication.getContext());
<span class="hljs-keyword">private</span> TencentLocationRequest locationRequest;
 
<span class="hljs-meta">@Override</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">startLocation</span><span class="hljs-params">(<span class="hljs-keyword">boolean</span> single)</span> </span>&#123;
    IS_SINGLE_LOCATION_MODE = single;<span class="hljs-comment">//因为这里只需要定位一次，所以加了个参数</span>
    locationRequest = TencentLocationRequest.create();
    locationRequest.setInterval(<span class="hljs-number">5000</span>);<span class="hljs-comment">//定位间隔</span>
    <span class="hljs-comment">//根据用户获取的位置信息的详细程度，REQUEST_LEVEL_ADMIN_AREA:包含经纬度，位置所处的中国大陆行政区划</span>
    locationRequest.setRequestLevel(TencentLocationRequest.REQUEST_LEVEL_ADMIN_AREA);
    locationRequest.setAllowGPS(<span class="hljs-keyword">true</span>);<span class="hljs-comment">//是否允许使用GPS定位</span>
    mLocationManager.requestLocationUpdates(locationRequest, <span class="hljs-keyword">this</span>);<span class="hljs-comment">//连续定位</span>
&#125;
 
<span class="hljs-meta">@Override</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">stopLocation</span><span class="hljs-params">()</span> </span>&#123;
    mLocationManager.removeUpdates(<span class="hljs-keyword">this</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除此之外，为了获得定位的位置信息，我们还需要让DrivingRoutePresent额外实现TencentLocationListener接口，实现onLocationChanged（用于接收定位结果）和onStatusUpdate（用于接收GPS,WiFi,Cell的状态码）方法。</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onLocationChanged</span><span class="hljs-params">(TencentLocation tencentLocation, <span class="hljs-keyword">int</span> i, String s)</span> </span>&#123;
        <span class="hljs-keyword">if</span> (IS_SINGLE_LOCATION_MODE)
            stopLocation();
        <span class="hljs-keyword">switch</span> (i)&#123;
            <span class="hljs-keyword">case</span> TencentLocation.ERROR_OK:
                <span class="hljs-comment">//定位成功</span>
                drinvingRouteView.setLocation(tencentLocation);
                <span class="hljs-comment">//渲染定位信息</span>
                <span class="hljs-keyword">if</span> (drinvingRouteView.getFromET()!=<span class="hljs-keyword">null</span>&&drinvingRouteView.getFromET().getText().toString().trim().equals(<span class="hljs-string">""</span>))
                    drinvingRouteView.getFromET().setText(tencentLocation.getAddress());
<span class="hljs-comment">//                Toast.makeText(GlobalApplication.getContext(), "定位成功", Toast.LENGTH_SHORT).show();</span>
                <span class="hljs-keyword">break</span>;
            <span class="hljs-keyword">case</span> TencentLocation.ERROR_NETWORK:
                Toast.makeText(GlobalApplication.getContext(), <span class="hljs-string">"网络问题引起的定位失败"</span>, Toast.LENGTH_SHORT).show();
                <span class="hljs-keyword">break</span>;
            <span class="hljs-keyword">case</span> TencentLocation.ERROR_BAD_JSON:
                Toast.makeText(GlobalApplication.getContext(), <span class="hljs-string">"GPS, Wi-Fi 或基站错误引起的定位失败"</span>, Toast.LENGTH_SHORT).show();
                <span class="hljs-keyword">break</span>;
            <span class="hljs-keyword">case</span> TencentLocation.ERROR_WGS84:
                Toast.makeText(GlobalApplication.getContext(), <span class="hljs-string">"无法将WGS84坐标转换成GCJ-02坐标时的定位失败"</span>, Toast.LENGTH_SHORT).show();
                <span class="hljs-keyword">break</span>;
            <span class="hljs-keyword">case</span> TencentLocation.ERROR_UNKNOWN:
                Toast.makeText(GlobalApplication.getContext(), <span class="hljs-string">"未知原因引起的定位失败"</span>, Toast.LENGTH_SHORT).show();
                <span class="hljs-keyword">break</span>;
        &#125;
    &#125;
 
    <span class="hljs-meta">@Override</span>
    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onStatusUpdate</span><span class="hljs-params">(String s, <span class="hljs-keyword">int</span> i, String s1)</span> </span>&#123;
        <span class="hljs-comment">//TencentLocationListener回调此方法传入的GPS,WiFi,Cell状态码，具体状态码查看Android定位SDK开发文档</span>
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，我们再把给定位的小按钮绑定的点击事件加上实现，在onResume和onPause方法调用一下startLocation和stopLocation方法让app在开启或切换回当前Activity时自动定位</p>
<pre><code class="hljs language-java copyable" lang="java"><span class="hljs-meta">@Override</span>
<span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onClick</span><span class="hljs-params">(View view)</span> </span>&#123;
    <span class="hljs-keyword">switch</span> (view.getId())&#123;
        <span class="hljs-keyword">case</span> R.id.order_btn:
            drivingRoutePresent.geocoder(fromET.getText().toString(), DrivingRoutePresent.FROM_TYPE);
            drivingRoutePresent.geocoder(toET.getText().toString(), DrivingRoutePresent.TO_TYPE);
            confirmBtn.setVisibility(View.VISIBLE);
            orderBtn.setVisibility(View.GONE);
            <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> R.id.confirm_btn:
            <span class="hljs-comment">//开启动画移动</span>
            mAnimator.startAnimation();
            orderBtn.setVisibility(View.VISIBLE);
            confirmBtn.setVisibility(View.GONE);
            <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> R.id.location_ib:
            <span class="hljs-comment">//定位一次</span>
            drivingRoutePresent.startLocation(<span class="hljs-keyword">true</span>);
            <span class="hljs-keyword">break</span>;
    &#125;
&#125;
 
<span class="hljs-meta">@Override</span>
<span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onResume</span><span class="hljs-params">()</span> </span>&#123;
    <span class="hljs-keyword">super</span>.onResume();
    mapView.onResume();
    drivingRoutePresent.startLocation(<span class="hljs-keyword">true</span>);
&#125;
 
<span class="hljs-meta">@Override</span>
<span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">void</span> <span class="hljs-title">onPause</span><span class="hljs-params">()</span> </span>&#123;
    <span class="hljs-keyword">super</span>.onPause();
    mapView.onPause();
    drivingRoutePresent.stopLocation();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">三.结尾</h2>
<p>写到这里，效果图上所有的功能就基本完成了，总的来说，功能还是十分强大的，对于有相关需求的企业来说开发起来非常省时省力。另外开发文档和接口文档也比较详细。由于时间有限，暂时只体验了其中的几个服务，有更多需求的同学可以自行到官网探索。</p></div>  
</div>
            