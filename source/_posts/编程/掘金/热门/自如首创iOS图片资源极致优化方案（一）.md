
---
title: '自如首创iOS图片资源极致优化方案（一）'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d5fe8b14dec49be8721bcf34bb506dc~tplv-k3u1fbpfcp-zoom-crop-mark:1280:960:0:0.image'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 17:12:20 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d5fe8b14dec49be8721bcf34bb506dc~tplv-k3u1fbpfcp-zoom-crop-mark:1280:960:0:0.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">背景</h2>
<blockquote>
<p>iOS开发过程中对资源的管理业界没有给出一个优质方案，于是大项目通过不断迭代都会遇到包体过大的情况。包体瘦身便有了百家争鸣的局面，瘦身的矛头都指向了导致包体暴增的大boss：资源！但是没有一个方案是可以解决病根的，自如另辟蹊径，开创了资源管理系统新途径，并成功拿到3项相关技术专利</p>
</blockquote>
<h2 data-id="heading-1">资源管理通常遇到的问题</h2>
<blockquote>
<p>这里的前提是工程已经组件化，不同组件通过路由管理，组件间0耦合，组件管理使用cocoapod</p>
</blockquote>
<h3 data-id="heading-2">问题的产生原因</h3>
<p>在日常开发中，我们接到需求之后如果有图片就会导入到工程，如果这个图片经过迭代废弃了，很多人是不会主动去删除的，因为开发人员是不知道这个图片是不是在其他地方有人在用，删了可能引起严重丢图bug！所有，业界很少有人主动删图，因此大量废弃图片导致包体日益增加</p>
<h3 data-id="heading-3">业界通常遇到的问题</h3>
<p>问题：组件A里面有图片 x、y、z，组件B里面有q、r、x，这时候图片怎么管理？
方案1：把图片和组件放在一起做成pod组件来使用，无论是通过bundle还是通过xcasset，都会出现图片x重复。很多第三方都是这么做，比如阿里的：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d5fe8b14dec49be8721bcf34bb506dc~tplv-k3u1fbpfcp-zoom-crop-mark:1280:960:0:0.image" alt="16244379346304.jpg" loading="lazy" referrerpolicy="no-referrer">
这里面有俩问题
1，图片可能和其他组件重复
2，图片如果包含2x和3x，在出包的时候slicing就不会使用，xcasset本身在安装到具体手机的时候会自动选择使用2x还是3x，使用bundle或者指定asset目录的形式会使苹果的这一优化失效；另外，苹果会对xcasset里的png图片进行最优压缩，这一特性也会失效，从而导致包体无法缩减到最优状态</p>
<p>方案2：使用一个独立图片组件，这个组件包括工程中所有的图片
许多工程优化过程中经常会经过这个阶段，所有图片都放到一个pod组件库里面，作为一个基础组件使用，这样就可以解决图片重复问题，而且图片可以统一管理和统一压缩，基本趋于完美的状态。例如：组件A用到图片 x、y、z，组件B用到q、r、x，图片组件M包含 x、y、z、q、r，这样只需要A依赖M，B依赖M，最终打包的时候仅包含这5张图片就可以实现需求，图片也没有重复
这里存在一个问题
1，如果公司还有另一个项目P1，P1需要用到B组件，这时候P1就会引入5张图片！如果按需索取的话，应该仅仅引入q、r、x即可，这样直接打破了组件跨app使用的通用性，资源完全耦合到这一个app里了！</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/796025bdbbdf43c18e164403e4e4f1f8~tplv-k3u1fbpfcp-zoom-crop-mark:1280:960:0:0.image" alt="16244390071539.jpg" loading="lazy" referrerpolicy="no-referrer">
如果把所有图片都放主工程xcasset里，结果和方案2是一样的</p>
<h2 data-id="heading-4">自如资源管理无敌方案</h2>
<blockquote>
<p>简单来说，资源资源管理无敌方案就是云端管理图片和组件之间的关系，统计图片使用次数，云控3个月没有使用记录的图片</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9fef8221f2944debab1692ae8d603137~tplv-k3u1fbpfcp-zoom-crop-mark:1280:960:0:0.image" alt="16244397063915.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上是整体架构图，里面涉及到许多技术后面会慢慢讲，先说下这里如何解决的问题以及本方案的优势</p>
<p>1，一般方案中图片重复的问题，本方案图片和组件建立一对一关系，通过云端统一管理，不会出现重复问题
2，一般方案中的xcasset特性和slicing问题，本方案在打包期间实时从云端拉取图片，生成xcasset之后导入到工程，这些优质特性都会生效
3，一般方案中跨app使用问题，本方案图片和组件一对一对应，可以随意迁移到其他app，而不会缺少图片或图片重复</p>
<p>由此可见，云端管理系统可以解决市面上一般方案引起的一系列问题，除了解决这些问题之外，还可以统计图片使用次数，根据使用次数来评估废弃图片；另外，云端管理图片可以延伸为管理资源，plist、音视频、webp等资源</p>
<h2 data-id="heading-5">自如资源管理系统研发历程</h2>
<h3 data-id="heading-6">图片管理一期</h3>
<blockquote>
<p>图片一期属于头脑风暴的开始，奠定了资源管理的基础</p>
</blockquote>
<p>我们要解决的难点一共俩：</p>
<ol>
<li>iOS图片一般使用<code>UIImage imageNamed</code> 同步方式读取图片，云端管理之后如何不改变使用方式的情况下异步下载图片来使用</li>
<li>如何找出每个组件对应哪些图片</li>
</ol>
<p>第一个问题是主要问题，如果实现不了异步下载图片和不改变原有使用方式，图片管理这个事情就无法推动，图片管理方案也就失去了意义。好在最终我们找到了方案！这个功能我们放到了图片二期的时候来做，图片一期主要解决问题2</p>
<blockquote>
<p>找出工程中所有使用的图片，包括图片名称是拼接的、图片名是服务端控制的、图片名是个变量等</p>
</blockquote>
<p>找工程中的图片几种方法：</p>
<ol>
<li>根据查找使用API的方式定位，比如：<code>UIImage imageNamed</code></li>
<li>导出工程中所有的图片资源作为工程中使用的图片</li>
</ol>
<p>我们使用的组件化方案是采用pod管理各个组件的，组件的图片资源有的是放组件里的、有的是通过图片组件统一管理的、也有直接放主工程xcasset里的，因此，我们面临如何统计图片资源的问题。</p>
<p>统计工程中的所有图片方法：</p>
<ol>
<li>导出工程使用的所有图片到一个文件夹下（使用脚本批量处理）</li>
<li>每条业务线负责的组件都创建一个image_manager.txt文件，存放本组件使用到的图片。（这步有丢失图片的可能，因为有些图片可能是变量拼接的，由于人工疏忽而没有写入到image_manager.txt，但是测试阶段很容易发现问题）</li>
<li>我们要管理的资源定位是自研组件，因此无需考虑第三方图片的情况</li>
</ol>
<p>主工程作为特殊的组件处理，给主工程起一个工程ID名称，比如<code>ios_ziroom</code>，主工程组件的名称就是工程ID名称。这样主工程就可以跟组件一样的处理和图片之间的关系，每个组件收集完image_manager.txt之后，用脚本在打包的时候汇总所有的image_manager.txt文件内容，并且除重，得到的结果和工程中搜索到的资源进行对比，没差异之后说明统计的图片名称和资源都能对上号了，这些工作是为了资源云管理做的准备。</p>
<p>后期我们会对资源管理系统进行继续详细分享</p>
<blockquote>
<p>自如大前端研发中心招募新同学！
FE/IOS/Android工程师看过来</p>
</blockquote>
<blockquote>
<p>公司福利有：
全额五险一金，并额外购买商业保险
免费健身房+年度体检
公司附近租房9折优惠
每年2次晋升机会</p>
</blockquote>
<blockquote>
<p>办公地点：北京酒仙桥普天实业科技园
欢迎对技术有执着热爱的你加入我们！简历请投递 <a href="https://link.juejin.cn/?target=mailto%3Alich7%40ziroom.com" target="_blank" title="mailto:lich7@ziroom.com" ref="nofollow noopener noreferrer">lich7@ziroom.com</a>！</p>
</blockquote></div>  
</div>
            