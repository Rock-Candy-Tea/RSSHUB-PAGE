
---
title: 'iOS 无侵入埋点方案！'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b321c31b1b19487281b65bb160c90978~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 17 May 2021 00:02:14 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b321c31b1b19487281b65bb160c90978~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">分享一个无侵入埋点方案。</h2>
<p>使用无侵入埋点方案的好处就是能将埋点代码和业务代码解耦。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b321c31b1b19487281b65bb160c90978~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
demo地址: <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2FAutoJiang%2FTrackDemo.git" target="_blank" rel="nofollow noopener noreferrer">这里</a></p>
<p>然而很多无侵入埋点都是hook系统的方式去，比如一些第三方埋点库，拥有自动埋点的功能。但是这个难以满足我们项目自定义化埋点的需求。</p>
<p>通过该无侵入埋点，可以做到将整个项目所有的业务埋点逻辑都写入在一个文件里。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e94cd8141f04f738936565e88fb4c3a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3c9635ec3c846479cf3df5a989b2ef9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>并且这个文件不会与任何业务代码耦合（我们看看引入的头文件）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44d03664ee16477ba9d2d1dcdc423359~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>具体细节请参考实现。
由于无侵入埋点的方案是基于当前项目中存在的埋点业务特点，定制化编写对应的格式，所以不太适合做成基础组件，因此楼主只给了一个demo，供大家参考。</p>
<h4 data-id="heading-1">原理:</h4>
<ol>
<li>基于运行时交换方法，以及动态添加方法的方式，hook要埋点的对象的方法，然后插入埋点代码。</li>
<li>可通过配置的方式生成插入代码。</li>
<li>动态下发json文件的方式，动态添加埋点。</li>
</ol>
<p>目前可支持两种方式，添加埋点。</p>
<h4 data-id="heading-2">方式一:</h4>
<ol>
<li>在该处添加要交换的对象、方法，以及替换方法 （hook_className_methodName:）</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd60904b7d56403f94675105a6e49a9f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>在该处添加交换方法。（注：必须保证参数一致）</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2c15b9e41a4407892da841d0c6d47f2~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>
<p>可通过KVC的方式来获取对象属性。（因为 self 为被hook的class，理论上可以获取self的任何属性）
例如：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af3b08e7c20a46dea3113fd9778a66e6~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ol>
<h4 data-id="heading-3">方式二:</h4>
<p>通过配置的方式添加埋点，在tracker.json下添加如下配置，即可添加埋点。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/447b99ac9f0a4e86a8220635740ac1a5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">注意事项：</h4>
<blockquote>
<p>有一个学习的氛围跟一个交流圈子特别重要，这是一个我的iOS开发公众号：编程大鑫，不管你是大牛还是小白都欢迎入驻 ，让我们一起进步，共同发展！</p>
</blockquote>
<ol>
<li>
<p>hookClass为hook的对象。</p>
</li>
<li>
<p>hookMethod为hook方法。</p>
</li>
<li>
<p>events为添加的事件，为数组类型。代表这一句代码里面存在多个埋点。types , refers数组个数必须和events一致。</p>
</li>
<li>
<p>"#0"代表取第一个参数，"#1"代表取第二个参数，"#2"代表取第三个参数，以此类推。</p>
</li>
<li>
<p>可通过self.articleInfo.articleBase.articleId的方式来获取成员属性。</p>
</li>
<li>
<p>该方式目前只支持对象类型的参数，不支持基础数据类型（方式一不受限制）。</p>
</li>
</ol></div>  
</div>
            