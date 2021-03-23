
---
title: 'Flutter开发：设置应用名称以及图标'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4714d1fea86349288e94bbe78f8be721~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 22 Mar 2021 23:23:51 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4714d1fea86349288e94bbe78f8be721~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>最近在用Flutter开发App项目，一切都是新的，一切都要学习。不过经过一段时间的开发适应和磨合，趋于稳定状态。本篇博文来分享一下Flutter设置App的应用名字和应用logo图标的方法，知识点虽然简单，但是不知道这个知识点就不行，所以还是要记录下来，分享一下。</p>
<p>其实，Flutter设置App的应用名称和图标是要分开来操作的，Android和iOS是分开设置对应的App名称和图标的，这一点一定要注意。也可以把Android和iOS的应用名称和图标分开设置，可以设置不一样，但是毕竟一个App为了保证一致性，还是不要这样做，老老实实保证Android和iOS两个端的应用信息保持一致吧。</p>
<p>Flutter在新建过程中，生成的project name是默认的应用名称，应用图标也是默认的，具体效果如下所示：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4714d1fea86349288e94bbe78f8be721~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>一、Flutter中设置Android的应用名称和图标</p>
<p>这里把应用名称和图标放在一起介绍，具体操作如下所以。</p>
<p>1、首先要定位到修改应用名称的文件，有两种打开方式，第一种方式就是用VS Code编辑器打开项目，然后找到项目里面的Android目录下的Android—>app—>src—>main—>AndroidManifest.xml文件，找到对应的位置进行修改；第二种方式就是打开Android Studio编辑器打开项目里面的Android文件，依然是在app—>src—>main—>AndroidManifest.xml文件中进行修改，具体的操作如下所示：</p>
<p>（1）AndroidManifest.xml文件中application下面的label对应的值就是应用的名称；</p>
<p>（2）AndroidManifest.xml文件中application下面的icon对应的值就是应用的图标文件；</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1658ec8b01949ed8d3af2416ac8a3bb~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d717ff9e3cc04f24a8f38c72f053b096~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4f8396390614506bd1c93e9679e2a2a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>二、Flutter中设置iOS的应用名称和图标</p>
<p>1、由于苹果的icon设置有点特殊，建议开发者直接通过xcode编辑器打开项目的iOS文件夹，然后在xcode编辑器里面进行iOS端的应用图标设置。但是iOS端的应用名称有两种设置方式：第一种就是用VS Code编辑器打开项目，找到iOS目录下的ios—>Runner—>Info.plist文件，然后找到对应的设置应用名称的键值对进行设置；第二种方式就是直接在xcode里面Runner—>Runner—>Info.plist文件里面对应的设置应用名称的键值对进行设置，具体操作如下所示：</p>
<p>（1）Info.plist文件里面对应的含有App名字的键值对就是设置应用名称的地方；</p>
<p>（2）Assets.xcassets文件里面的AppIcon里面对应的就是设置应用图标的地方；</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24f322db21a443d48be99fd279184c68~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c0b121bb56c493b92cdf2bb28db2a43~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/82eeedcd68fe4469a73a6a9d3888919b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>设置完应用名称和图标的最终效果，如下所示：</p>
<p><img alt class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67a88ad5acad4b1f97f3cf88be2a7ebd~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>以上就是本章全部内容，欢迎关注三掌柜的微信公众号“iOS开发by三掌柜”，三掌柜的新浪微博“三掌柜666”，欢迎关注！</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            