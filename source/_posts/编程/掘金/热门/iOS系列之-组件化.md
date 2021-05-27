
---
title: 'iOS系列之-组件化'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://picsum.photos/400/300?random=3082'
author: 掘金
comments: false
date: Tue, 18 May 2021 05:51:13 GMT
thumbnail: 'https://picsum.photos/400/300?random=3082'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">MGJRouter 蘑菇街组件实现原理</h1>
<h2 data-id="heading-1">方案一 url-block</h2>
<p>这是蘑菇街中应用的一种页面间调用的方式，通过在启动时注册组件提供的服务，把调用组件使用的url和组件提供的服务block对应起来，保存到内存中。在使用组件的服务时，通过url找到对应的block，然后获取服务。</p>
<h3 data-id="heading-2">注册</h3>
<pre><code class="copyable">[MGJRouter registerURLPattern:@"mgj://detail?id=:id" toHandler:^(NSDictionary *routerParameters) &#123;
    NSNumber *id = routerParameters[@"id"];
    // create view controller with id
    // push view controller
&#125;];
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">调用：</h3>
<ul>
<li>url的参数传递受到限制，只能传递常规的字符串参数，无法传递非常规参数，如UIImage、NSData等类型</li>
<li>没有区分本地调用和远程调用的情况，尤其是远程调用，会因为url参数受限，导致一些功能受限</li>
<li>组件本身依赖了中间件，且分散注册使的耦合较多</li>
</ul>
<h2 data-id="heading-4">方案二、protocol-class</h2>
<p>针对方案一的问题，蘑菇街又提出了另一种组件化的方案，就是通过protocol定义服务接口，组件通过实现该接口来提供接口定义的服务，具体实现就是把protocol和class做一个映射，同时在内存中保存一张映射表，使用的时候，就通过protocol找到对应的class来获取需要的服务。</p>
<h3 data-id="heading-5">注册：</h3>
<pre><code class="copyable">[ModuleManager registerClass:ClassA forProtocol:ProtocolA]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">调用</h3>
<pre><code class="copyable">[ModuleManager classForProtocol:ProtocolA]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>蘑菇街的这种方案确实解决了方案一中无法传递非常规参数的问题，使得组件间的调用更为方便，但是它依然没有解决组件依赖中间件的问题、内存中维护映射表的问题、组件的分散调用的问题。设计思想和方案一类似，都是通过给组件加了一层wrapper，然后给使用者调用。</p>
<h1 data-id="heading-7">方案三、target-action</h1>
<p>casa的方案是通过给组件包装一层wrapper来给外界提供服务，然后调用者通过依赖中间件来使用服务；其中，中间件是通过runtime来调用组件的服务，是真正意义上的解耦，也是该方案最核心的地方。具体实施过程是给组件封装一层target对象来对外提供服务，不会对原来组件造成入侵；然后，通过实现中间件的category来提供服务给调用者，这样使用者只需要依赖中间件，而组件则不需要依赖中间件。
也就是每个组件创建一个target类(由组件开发者维护)，其内部定义了组件对外暴露的action（方法）。和组件通信时，其实质是调用一个特定的target-action的方法。target类的类名必须以Target_开头，比如Target_A，action的方法名必须以Action_开头，比如Action_nativeFetchDetailViewController。注意，暴露出来的这个target类并不是这个组件的具体实现，它只是为了方便调用者使用，target类的实现文件中会引入组件的头文件，实现声明文件中的功能，从而达到调用组件的目的。</p>
<p>使用者只需要依赖中间件，而中间件又不依赖组件，这是真正意义上的解耦。但是casa的这个方案有个问题就是hardcode，在中间件的category里有hardcode，casa的解释是在组件间调用时，最好是去model化，所以不可避免的引入了hardcode，并且所有的hardcode只存在于分类中。针对这个问题，有人提议，把所有的model做成组件化下沉，然后让所有的组件都可以自由的访问model，不过在我看来，这种方案虽然解决了组件间传递model的依赖问题，但是为了解决这个小问题，直接把整个model层组件化后暴露给所有组件，容易造成数据泄露，付出的代价有点大。针对这个问题，经过和网友讨论，一致觉得组件间调用时用字典传递数据，组件内调用时用model传递数据，这样即减少组件间数据对model的耦合，又方便了组件内使用model传递数据的便捷性。</p></div>  
</div>
            