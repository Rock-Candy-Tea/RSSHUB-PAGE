
---
title: '百度地图api使用城市列表组件选择城市、省份获取对应城市信息（省市经纬度）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97e0dbb8a65b4826b9f625423a6abc2c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
author: 掘金
comments: false
date: Thu, 08 Sep 2022 03:06:43 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97e0dbb8a65b4826b9f625423a6abc2c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
---

<div>   
<div class="markdown-body cache"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:-apple-system-font,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei UI,Microsoft YaHei,Arial,sans-serif;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:23px;margin-bottom:5px;font-weight:700;padding-left:10px;border-left:5px solid #773098&#125;.markdown-body h2&#123;font-size:19px;font-weight:700;padding-left:10px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:17px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;font-size:14px;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;display:block;max-width:100%;margin:1em 0;border-radius:6px;box-shadow:2px 4px 7px #999;user-select:none&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-family:-apple-system-font,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei UI,Microsoft YaHei,Arial,sans-serif;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-family:-apple-system-font,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei UI,Microsoft YaHei,Arial,sans-serif;font-weight:400;font-size:.9em;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8;scroll-behavior:smooth&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:14px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5;border-collapse:collapse&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px;border:1px solid #916dd5&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p> “我报名参加金石计划1期挑战——瓜分10万奖池，这是我的第二篇文章，<a href="https://s.juejin.cn/ds/jooSN7t" title="https://s.juejin.cn/ds/jooSN7t" target="_blank">点击查看活动详情</a>”</p>
<blockquote>
<p> Hello大家好啊，写文章是一个比较好的习惯，但我却有点喜欢偷懒，导致这一篇文章在周一的时候就写了，到了周末才开始着手。之前写文章有的时候不知道题材是什么，但自从实习之后会遇到很多值得记录的业务场景。最近也在读一本书《下班后开始新的一天》，通过这本书我了解到了，可以把一天分成两天过，上班的时候工作如果能够享受这个过程是最佳的，下班之后应该享受属于自己的4个小时，可以找自己喜欢的事情、找到自己的副业。目前对我而言，写博客是蛮享受的一个过程。</p>
</blockquote>
<p> 最近在开发地图相关项目的时候，突然有这么一个需求：需要在添加设备的表单选择位置时弹出百度地图的组件，点击地图上的某一处返回对应的经纬度信息。且右上角需要有一个省份城市切换的控制器用来返回相应的省市信息给表单对象<code>（对用户直接缩小地图切换省份的操作不做出省份切换）</code>。
  这一次的业务其实是在基于vue2.0的项目，但我最近在研究<code>vue3.0 + typescript + hooks</code>，因此就决定将这次的demo以v3+ts的形式编写，事实证明，这一波操作确实是将复杂度提升了一个档次，本来非常简单的逻辑现在需要考虑到<code>地图异步加载拿不到全局对象BMap、地图组件难取得hooks中的Geocoder等问题</code>，有点没事找事的意思哈哈。不过核心函数代码是不区分<code>v2、v3</code>的，核心函数的部分其实也就是本文的中心，并且，这个核心函数的部分还非常简单易懂。
 因为完整的代码越写越觉得自己有点多此一举，因此就不在文章上分享了，更多的还是想找点<code>vue3+typescript+hooks</code>搭建项目的感觉。源码地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2FCrivk%2Fcsdn-related-demo%2Ftree%2Fmaster%2FVue%2Fv3-baidu-map" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/Crivk/csdn-related-demo/tree/master/Vue/v3-baidu-map" ref="nofollow noopener noreferrer">vue3-ts-baidu-map</a>。</p>
<hr>
<h1 data-id="heading-1">一、核心代码</h1>
<p> 那么我们直接开始，这样一个业务其实是比较简单的，实现省市选择器可以使用<code>自定义组件 + 地图api提供的添加自定义组件</code>，也可以使用<code>地图自带的城市列表控件</code>。相对来说使用地图自带的控件会更加容易一些且更有兼容性一些。</p>
<blockquote>
<p> 以下是<a href="https://link.juejin.cn/?target=https%3A%2F%2Flbsyun.baidu.com%2Fjsdemo.htm%23b_07" target="_blank" rel="nofollow noopener noreferrer" title="https://lbsyun.baidu.com/jsdemo.htm#b_07" ref="nofollow noopener noreferrer">地图api官网</a>提供的<strong>城市列表控件</strong>Demo中的添加控件的部分代码，可以看到其中只配置了 <em>anchor、offset</em>两个属性。</p>
</blockquote>
<div align="center"> 
<img width="700" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97e0dbb8a65b4826b9f625423a6abc2c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" title="官方Api" loading="lazy" referrerpolicy="no-referrer">
</div>
<blockquote>
<p>  但其实cityControl还可以配置对应的响应函数，如onChangeBefore、onChangeAfter、以及最为重要<code>onChangeSuccess</code>配置项。</p>
</blockquote>
<div align="center"> 
<img width="700" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe9b282023b1499497cbbf36b03508f2~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" title="切换成功回调函数参数结构" loading="lazy" referrerpolicy="no-referrer">
</div>
<blockquote>
<p>  通过日志打印，我们可以拿到onChangeSuccess回调函数中ev的结构。其中我们关心的数据有point中的<code>lng、lat</code>，细心的你也许发现了ev结构中的city并不符合我们的要求，因为如果选择城市则就只有城市信息、选择省份则就只有省份信息。所以需要我们的二次处理。
 这里我选择的是用经纬度逆解析<code>Geocoder</code>将城市列表选择得到的经纬度逆地址解析为详细地址，取得需要的<code>省份、城市</code>信息。</p>
</blockquote>
<div align="center"> 
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb4857e3d5564e03908f33b3f390892c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" width="700" title="使用逆解析完成省份、城市信息的获取" loading="lazy" referrerpolicy="no-referrer"> 
</div>
<blockquote>
<p>而获取经纬度信息就比较简单了，只要用到百度地图中的marker以及给地图添加点击事件获取经纬度赋值给位置信息对象即可。</p>
</blockquote>
<div align="center"> 
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9b127a0d97a48f2b211bf227935aba1~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" width="700" title="添加点击事件获取经纬度位置" loading="lazy" referrerpolicy="no-referrer"> 
</div>
<h1 data-id="heading-2">二、可能遇到的问题</h1>
<p> 还是想跟大家分享一下在做这个demo项目中我遇到的一些问题，以及目前我解决它们的办法</p>
<h2 data-id="heading-3">1、关于百度地图相关变量报错的问题</h2>
<h3 data-id="heading-4">报错: TS2552: Cannot find name 'BMap'. Did you mean 'Map'? <code>或</code> TS2551: Property 'BMap' does not exist on type 'Window & typeof globalThis'. Did you mean 'Map'?</h3>
<h3 data-id="heading-5">解决方法：</h3>
<p>  这是因为我们没有对BMap等地图相关变量进行注册，这里我解决的方法是：<code>在src目录下创建global.d.ts</code>文件，并对window进行接口定义：</p>
<div align="center"> 
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34543dea9f8c4afca4fc9b3c31903b31~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" width="700" loading="lazy" referrerpolicy="no-referrer"> 
</div>
<h2 data-id="heading-6">2、处理地图script标签异步插入完成前获取不到地图相关对象报错问题</h2>
<h3 data-id="heading-7">问题：使用window.BMap、Map时报错undefined</h3>
<p>  下方图片中展示的是我将百度地图javascript标签插入body的方式，不同于直接在<code>public/index.html</code>中直接插入，这里我选择了异步插入，当组件调用地图hooks中的<code>initMap函数</code>就会调用<code>createMap方法</code>进而将js标签插入到body中。同时我将对地图添加事件函数、地图控件的方法也抽离了出来，这样就会造成一个问题：<code>因为相关添加的函数都是同步的，当执行时非常大可能地图script还未添加至body中，也就是window全局对象中没有地图相关变量</code>。</p>
<div align="center"> 
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac8117f9600640789b04292327ede5ed~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" width="700" loading="lazy" referrerpolicy="no-referrer"> 
</div>
<h3 data-id="heading-8">解决方法:</h3>
<p> 在这里我在外层分别定义了处理异步问题的事件栈与组件栈，并在onload的末尾加入判断异步栈中是否存在元素，存在则执行。也就是说我将添加的逻辑先缓存在了对应的栈中，当地图完成添加之后将缓存的函数拿出执行。</p>
<div align="center"> 
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec7ca747521449d2ae4c56bde9ad773e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" width="700" loading="lazy" referrerpolicy="no-referrer"> 
</div>
<h2 data-id="heading-9">3、使用Ant-design-vue 想要使 <a-input />标签处于只读状态</h2>
<h3 data-id="heading-10">解决方法：<code>给标签加上readOnly属性即可</code></h3>
<h1 data-id="heading-11">总结</h1>
<p>  以上便是本篇文章的全部内容啦，这一篇文章写了比较长的一段时间。主要是因为对于<code>vue3 + typescript</code>一些写法、api的不熟悉，以及异步加载百度地图可能造成的一系列问题的解决。（吐槽：还有隔壁情侣大晚上动静比较大，好几天没有休息好再加上这周工作量的增加，比较没有心思去完整的写完这篇文章）总的来说这一次的demo对自己学习新知识还是很有帮助的，就得多写写demo，多遇到一些bug，在视频、文章中看到的知识点才能被更加深刻的吸收进脑海中。
 说一个题外话，如果是在v2.x下要使用百度地图的话还是比较推荐使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdafrok.github.io%2Fvue-baidu-map%2F%23%2Fzh" target="_blank" rel="nofollow noopener noreferrer" title="https://dafrok.github.io/vue-baidu-map/#/zh" ref="nofollow noopener noreferrer">vue-baidu-map</a> 这个插件的，大佬封装的非常完整了，只要把控件以组件的方式往template中一放，就完成了控件的添加，还是相当方便的！就是在城市列表这个组件封装的时候并没有写到<code>onChangeSuccess</code>，因此没办法在标签上以<code>@onChangeSuccess</code>的方式实现组件切换位置信息的返回。</p></div>  
</div>
            