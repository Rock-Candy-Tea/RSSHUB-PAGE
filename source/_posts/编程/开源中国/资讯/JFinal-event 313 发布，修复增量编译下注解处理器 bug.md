
---
title: 'JFinal-event 3.1.3 发布，修复增量编译下注解处理器 bug'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-a6ebf66636f082b15a31e2c2e0b38c3042e.gif'
author: 开源中国
comments: false
date: Fri, 03 Sep 2021 00:07:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-a6ebf66636f082b15a31e2c2e0b38c3042e.gif'
---

<div>   
<div class="content">
                                                                                            <h2>一、前言</h2> 
<p>在 <a href="https://gitee.com/596392912/mica-auto">mica-auto</a> 2.1.3 中笔者修复了 mica-auto 在编辑器中增量编译的问题，本周抽出时间对 <code>JFinal-event</code> 也做了一番调整，修复了增量编译和对一些依赖进行了升级。</p> 
<h2>二、更新记录</h2> 
<h3>2021-09-02 v3.1.3</h3> 
<ul> 
 <li> <p>✨ 代码优化。</p> </li> 
 <li> <p>🐛 修复异常抛出。</p> </li> 
 <li> <p>🐛 修复注解处理器增量编译问题。</p> </li> 
 <li> <p>⬆️ 依赖升级。</p> </li> 
</ul> 
<h2>三、更新说明</h2> 
<p>此次更新主要对 3.0.0 新增的采用 <code>Annotation Processor</code> 技术，将运行期的事件类扫描改到了编译期。其中的增量编译进行了修复，从此可以不再使用类扫描，</p> 
<p>加快服务的启动时间，减少各种容器差异导致的类扫描问题。</p> 
<h2>四、使用</h2> 
<h3>4.1 maven</h3> 
<pre style="text-align:left"><span style="color:#117700"><</span><span style="color:#117700">dependency</span><span style="color:#117700">></span>
    <span style="color:#117700"><</span><span style="color:#117700">groupId</span><span style="color:#117700">></span>net.dreamlu<span style="color:#117700"></</span><span style="color:#117700">groupId</span><span style="color:#117700">></span>
    <span style="color:#117700"><</span><span style="color:#117700">artifactId</span><span style="color:#117700">></span>JFinal-event<span style="color:#117700"></</span><span style="color:#117700">artifactId</span><span style="color:#117700">></span>
    <span style="color:#117700"><</span><span style="color:#117700">version</span><span style="color:#117700">></span>3.1.3<span style="color:#117700"></</span><span style="color:#117700">version</span><span style="color:#117700">></span>
<span style="color:#117700"></</span><span style="color:#117700">dependency</span><span style="color:#117700">></span></pre> 
<h3>4.2 gradle >= 5.x</h3> 
<pre style="text-align:left"><span style="color:#000000">api</span>(<span style="color:#aa1111">"net.dreamlu:JFinal-event:3.1.3"</span>)
<span style="color:#000000">annotationProcessor</span>(<span style="color:#aa1111">"net.dreamlu:JFinal-event:3.1.3"</span>)</pre> 
<h3>4.3 gradle < 5.x</h3> 
<pre style="text-align:left"><span style="color:#000000">compile</span>(<span style="color:#aa1111">"net.dreamlu:JFinal-event:3.1.3"</span>)</pre> 
<h3>4.4 启动插件</h3> 
<pre style="text-align:left"><span style="color:#aa5500">// 初始化插件</span>
<span style="color:#000000">EventPlugin</span> <span style="color:#000000">plugin</span> <span style="color:#981a1a">=</span> <span style="color:#770088">new</span> <span style="color:#000000">EventPlugin</span>();
<span style="color:#aa5500">// 设置为异步，默认同步，或者使用`threadPool(ExecutorService executorService)`自定义线程池。</span>
<span style="color:#000000">plugin</span>.<span style="color:#000000">async</span>();
​
<span style="color:#aa5500">// 手动启动插件，用于 main 方法启动，jfinal中不需要，添加插件即可。</span>
<span style="color:#000000">plugin</span>.<span style="color:#000000">start</span>();
​
<span style="color:#aa5500">// 停止插件，用于 main 方法测试，jfinal中不需要，添加插件即可。</span>
<span style="color:#000000">plugin</span>.<span style="color:#000000">stop</span>();</pre> 
<h3>4.5 新建事件类</h3> 
<pre style="text-align:left"><span style="color:#770088">public</span> <span style="color:#770088">class</span> <span style="color:#0000ff">AccountEvent</span> &#123;
​
    <span style="color:#770088">private</span> <span style="color:#008855">Integer</span> <span style="color:#000000">id</span>;
    <span style="color:#770088">private</span> <span style="color:#008855">String</span> <span style="color:#000000">name</span>;
    <span style="color:#770088">private</span> <span style="color:#008855">Integer</span> <span style="color:#000000">age</span>;
​
    <span style="color:#aa5500">// 省略 get set</span>
&#125;</pre> 
<h3>4.6 编写监听</h3> 
<pre style="text-align:left"><span style="color:#770088">public</span> <span style="color:#770088">class</span> <span style="color:#0000ff">Test1Listener</span> &#123;
​
    <span style="color:#555555">@EventListener</span>
    <span style="color:#770088">public</span> <span style="color:#008855">void</span> <span style="color:#000000">listenTest1Event</span>(<span style="color:#000000">AccountEvent</span> <span style="color:#000000">event</span>) &#123;
        <span style="color:#000000">System</span>.<span style="color:#000000">out</span>.<span style="color:#000000">println</span>(<span style="color:#aa1111">"AccountEvent："</span> <span style="color:#981a1a">+</span> <span style="color:#000000">event</span>);
    &#125;
​
&#125;</pre> 
<h3>4.7 发送事件</h3> 
<pre style="text-align:left"><span style="color:#000000">AccountEvent</span> <span style="color:#000000">event</span> <span style="color:#981a1a">=</span> <span style="color:#770088">new</span> <span style="color:#000000">AccountEvent</span>();
<span style="color:#000000">event</span>.<span style="color:#000000">setId</span>(<span style="color:#116644">1</span>);
<span style="color:#000000">event</span>.<span style="color:#000000">setName</span>(<span style="color:#aa1111">"张三"</span>);
<span style="color:#000000">event</span>.<span style="color:#000000">setAge</span>(<span style="color:#116644">18</span>);
​
<span style="color:#000000">EventKit</span>.<span style="color:#000000">post</span>(<span style="color:#000000">event</span>);</pre> 
<h3>4.8 Idea 跳转插件</h3> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-a6ebf66636f082b15a31e2c2e0b38c3042e.gif" referrerpolicy="no-referrer"></p> 
<p><a href="https://gitee.com/596392912/JFinal-event/attach_files">Idea 插件 JFinal-eventx下载</a></p> 
<h2>五、回顾</h2> 
<p>或许这次真的是最后的一个版本了，由于精力有限，笔者已经停止更新其它的几个 JFinal 插件，下面随我一起回顾下 <code>JFinal-event</code> 的这6年多。</p> 
<ul> 
 <li> <p>2015-04-27 初始化项目 网名（孤独的√3）</p> </li> 
 <li> <p>2015-05-06 <code>v0.1</code> 版本发布推送到 maven 中央库</p> </li> 
 <li> <p>2015-06-25 <code>v0.3</code> 支持异步，去掉了 guava 包，因为只用了一个 Multimap 集合。</p> </li> 
 <li> <p>2015-07-04 <code>v0.4.2</code> 添加事件排序</p> </li> 
 <li> <p>2016-08-19 <code>v1.4.0</code> 添加事件 tag</p> </li> 
 <li> <p>2017-04-22 <code>v1.5.1</code> 添加了基于 rmi 的远程 Event（2.x弃用）</p> </li> 
 <li> <p>2017-10-10 <code>v2.0.0</code> 基于注解和方法的兼听，不再需要单独编写 Listener 类。</p> </li> 
 <li> <p>2018-03-02 <code>v2.1.0</code> 添加 <code>`CtrlHolderEvent</code> 处理同步、异步中 <code>request、session、header</code> 等参数传递。网名（如梦技术）</p> </li> 
 <li> <p>2018-10-09 <code>v2.2.2</code> 升级到 jfinal 3.5 支持JFinal新版本的 bean inject。</p> </li> 
 <li> <p>2019-04-08 <code>v2.3.0</code> 支持普通类作为 event 事件源，不再需要继承 <code>ApplicationEvent</code>。</p> </li> 
 <li> <p>2019-07-19 <code>v3.0.0</code> 采用注解处理器将类扫描提到编译期提升十倍的启动速度。</p> </li> 
 <li> <p>2020-03-29 <code>v3.1.2</code> 新增 Idea 快速跳转插件。</p> </li> 
</ul> 
<p>感谢码云提供了这么好的一个平台作为码云提供了这么一个优秀的平台，也感谢 JFinal-event 从 JFinal 中学习到了不少极简设计。</p> 
<h2>六、最后</h2> 
<p>笔者近几年将更多的精力放到的我新的 mica 系列开源项目中，其中包括 <a href="https://gitee.com/596392912/mica-auto">mica-auto</a>（Spring boot stater 利器）、<a href="https://gitee.com/596392912/mica">mica</a>（Spring cloud 微服务组件集）、<a href="https://gitee.com/596392912/mica-mqtt">mica-mqtt</a>（基于 t-io 的物联网 mqtt 客户端和服务端）等，欢迎 star。</p>
                                        </div>
                                      
</div>
            