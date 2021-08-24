
---
title: 'Android 架构师之路1 UML图之用例图'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/002a7bdd54834869a7ee6468f0c26504~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 22:41:59 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/002a7bdd54834869a7ee6468f0c26504~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>用例图主要用来描述 用户、需求、系统功能单元 之间的关系。它展示了一个外部用户能够观察到的系统功能模型图。</p>
<p>【用途】：帮助开发团队以一种可视化的方式理解系统的功能需求。</p>
<p>用例图所包含的元素如下：</p>
<h4 data-id="heading-0">1. 参与者(Actor)</h4>
<p>表示与您的应用程序或系统进行交互的用户、组织或外部系统。用一个小人表示。</p>
<div align="center">
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/002a7bdd54834869a7ee6468f0c26504~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
</div>
<h4 data-id="heading-1">2. 用例(Use Case)</h4>
<p>用例就是外部可见的系统功能，对系统提供的服务进行描述。 用椭圆表示</p>
<div align="center">
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72b1c91aae084f44b490eb9283e669f8~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
</div>
<h4 data-id="heading-2">3. 子系统(Subsystem)</h4>
<p>用来展示系统的一部分功能，这部分功能联系紧密。</p>
<div align="center">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94575911cad04135b8927b191166953e~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
</div>
<h4 data-id="heading-3">4. 关系</h4>
<p>用例图中涉及的关系有：关联、泛化、包含、扩展；</p>
<p>如下表所示：</p>
<div align="center">
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3fdb9b701be845b9979d5b7c5ed24837~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
</div>
<p>a. 关联(Association)</p>
<p>表示参与者与用例之间的通信，任何一方都可发送或接受消息。</p>
<p>【箭头指向】：指向消息接收方</p>
<div align="center">
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6107437e8e564084bf84c2f63fc9b91d~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
</div>
<p>b. 泛化(Inheritance)</p>
<p>就是通常理解的继承关系，子用例和父用例相似，但表现出更特别的行为；子用例将继承父用例的所有结构、行为和关系。子用例可以使用父用例的一段行为，也可以重载它。父用例通常是抽象的。</p>
<p>【箭头指向】：指向父用例</p>
<div align="center">
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21a163931d4c4ec7ac4dcd86f1b11fcd~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
</div>
<p>c. 包含(Include)</p>
<p>包含关系用来把一个较复杂用例所表示的功能分解成较小的步骤；</p>
<p>【箭头指向】：指向分解出来的功能用例</p>
<div align="center">
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5285c6e4f51c49f38131de904919ee71~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
</div>
<p>d. 扩展(Extend)</p>
<p>扩展关系是指 用例功能的延伸，相当于为基础用例提供一个附加功能。</p>
<p>【箭头指向】：指向基础用例</p>
<div align="center">
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55b4f8c1a31f4dd88205d4f451efe314~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
</div>
<p>e. 依赖(Dependency)</p>
<p>以上4中关系，是UML定义的标准关系。 但VS2010的用例模型图中，添加了依赖关系，用带箭头的虚线表示</p>
<p>表示源用例依赖于目标用例；</p>
<p>【箭头指向】：指向被依赖项</p>
<div align="center">
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/efcb300938ea4834b2f2d7c033bc57cf~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
</div>
<h4 data-id="heading-4">5. 项目(Artifact)</h4>
<p>用例图虽然是用来帮助人们形象地理解功能需求，但却没多少人能够通看懂它。很多时候跟用户交流甚至用Excel都比用例图强，VS2010中引入了“项目”这样一个元素，以便让开发人员能够在用例图中链接一个普通文档。</p>
<p>用依赖关系把某个用例依赖到项目上</p>
<div align="center">
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ccbc5de102d0435785d3995569cfb0a5~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
</div>
<p>然后把项目-》属性 的Hyperlink 设置到你的文档上</p>
<p>这样当你在用例图上 双击项目时，就会打开相关联的文档。</p>
<h4 data-id="heading-5">6. 注释(Comment)</h4>
<div align="center">
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1f638d59d8344b2835f720080a8dbf4~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
</div>
<p>包含(include)、扩展(extend)、泛化(Inheritance) 的区别：</p>
<p>条件性：泛化中的子用例和include中的被包含的用例会无条件发生，而extend中的延伸用例的发生是有条件的；</p>
<p>直接性：泛化中的子用例和extend中的延伸用例为参与者提供直接服务，而include中被包含的用例为参与者提供间接服务。</p>
<p>对extend而言，延伸用例并不包含基础用例的内容，基础用例也不包含延伸用例的内容。</p>
<p>对Inheritance而言，子用例包含基础用例的所有内容及其和其他用例或参与者之间的关系；</p>
<p>一个用例图示例：</p>
<div align="center">
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c7cfe4192c44fa19472e933462531be~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
</div></div>  
</div>
            