
---
title: '微信小程序开发框架对比 - Taro vs Remax'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5009'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 23:01:48 GMT
thumbnail: 'https://picsum.photos/400/300?random=5009'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">综述</h2>
<p>近期由于公司要开发微信小程序，因此对目前流行的小程序开发框架做了一些预研工作。</p>
<p>首先，目前流行的小程序开发框架主要有：</p>
<ul>
<li>
<p><strong>Taro</strong>（京东，React系，Taro3大改版后也支持Vue/Vue3，主打多平台小程序适配，以及H5、RN，大而全，希望对标Vue系的Uniapp，但感觉坑会不少）</p>
</li>
<li>
<p><strong>Uniapp</strong>（QCloud，Vue系，早先集成了MpVue，主打一套代码，多端部署，支持各种小程序平台、H5、IOS、Android等，适合某些固定的业务场景，听说外包用的很多，滑稽脸~ ）</p>
</li>
<li>
<p><strong>Remax</strong>（蚂蚁，React系，专注于使用 React 技术栈开发小程序，尤其微信小程序，支持和微信小程序进行混合开发，意味着它几乎完美继承原生小程序的能力，且可复用小程序社区。对其他小程序平台也有Remax one的跨端适配支持，小而精，未来可期~）</p>
</li>
<li>
<p><strong>MpVue</strong>（美团，Vue系，2年未维护，如果希望使用Vue开发小程序，选Uniapp吧~）</p>
</li>
<li>
<p><strong>Wepy</strong>（官方，让小程序支持组件化开发的框架，目前已被其他框架大大超越，欢迎进入到历史书中...）</p>
</li>
<li>
<p><strong>原生开发</strong>（官方，能力相比最初已大幅加强，但无法使用 Vue 和 React 的技术栈是一大硬伤，小程序开发工具的开发体验也和我们熟悉的 VSCode 有差距）</p>
</li>
</ul>
<p>通过对各个框架的初步了解和资料查阅，以及结合团队对于扩展技术栈的需求，重点选择React系的 <code>Taro</code> 和 <code>Remax</code>进行对比，通过使用这两个框架分别实现 <code>TodoList</code> 示例，来对比两者的区别。</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2FAaronKong%2Ftodo-list-remax" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/AaronKong/todo-list-remax" ref="nofollow noopener noreferrer">todolist-remax</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2FAaronKong%2Ftodo-list-taro" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/AaronKong/todo-list-taro" ref="nofollow noopener noreferrer">todolist-taro</a></li>
</ul>
<h2 data-id="heading-1">一、总体设计理念</h2>
<blockquote>
<p>【引自Remax官网】
Taro 3.0 版本的实现原理与 Remax 大同小异，没有太大的区别。主要区别在于以下两个方面：</p>
<ul>
<li><strong>跨平台设计</strong>，我们深知要打造一个面面俱到的多平台框架会有非常多的坑，与其挖一个大坑填不上，我们选择把有限的精力放在框架的核心功能上，并提供跨平台同构机制以及一个精简的跨平台实现（Remax One），让开发者可以根据自己的业务需求去做跨平台实现。</li>
<li><strong>专注 React</strong>，因为 React 是我们自己大量使用和熟悉的前端框架，Remax 会持续专注在 React 技术栈。</li>
</ul>
</blockquote>
<h2 data-id="heading-2">二、对比维度</h2>
<ol>
<li>开发体验（Remax > Taro）</li>
<li>组件&API能力（Remax > Taro）</li>
<li>插件支持-less（均支持）</li>
<li>第三方小程序组件库支持（Remax > Taro）、</li>
<li>运行性能-虚拟列表（Remax > Taro）</li>
<li>打包大小（Taro > Remax）</li>
<li>维护情况/社区（Taro > Remax）</li>
</ol>
<p><del>其他维度：</del></p>
<ul>
<li><del>多端适配：支持的多端适配（H5、多小程序平台、ReactNative）</del></li>
<li><del>自定义组件编写是否方便？</del></li>
<li><del>配置Webpack能力？</del></li>
<li><del>全局数据状态管理</del></li>
</ul>
<h3 data-id="heading-3">1、开发体验</h3>
<ul>
<li>创建项目：均可不安装全局包，使用一行命令即可新建项目
<ul>
<li>Taro： <code>npx @tarojs/cli init myApp</code></li>
<li>Remax: <code>npx create-remax-app my-app</code></li>
</ul>
</li>
<li>创建项目速度： Remax 明显快于Taro，1min vs 3-5min
<ul>
<li>得益于Remax仅安装核心库，十分小巧</li>
<li>Remax的初始项目一共仅包含 <code>react</code> 和 <code>remax</code> 两个包，相比之下，Taro一共有十几个包;</li>
</ul>
</li>
<li>代码检查：Taro自带eslint，而remax无提示，不过有代码提示，基本也没差</li>
<li>代码调试：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fremaxjs.org%2Fguide%2Fbasic%2Fdevtools" target="_blank" rel="nofollow noopener noreferrer" title="https://remaxjs.org/guide/basic/devtools" ref="nofollow noopener noreferrer">remax</a></li>
<li>编译报错：咋个都不提示呢。。。特别是Taro，不支持Web标签，会白屏，但也没报错</li>
<li>Web标签支持：Remax会自动帮你将<code><div></code>转成<code><View></code>，不过还是不建议写<code><div></code></li>
</ul>
<h3 data-id="heading-4">2、组件&API能力：</h3>
<blockquote>
<p>1、均支持和小程序原生组件/API混合开发</p>
<p>2、但实现思路稍有不同，Remax小而精，Taro大而全</p>
<p>3、因为实现思路不同，调用时的开发体验也不同。Remax更统一，而Taro需区分组件和api，以及区分使用的小程序平台，分别通过不同的包引入</p>
<p>4、总体上，Remax对微信原生小程序的支持度更高，因为原生小程序是官方维护，因此坑更少</p>
</blockquote>
<ul>
<li><strong>Remax</strong>
<ul>
<li>
<p>Remax/wechat 是微信小程序的组件库，基本可以完整使用原生小程序的能力，包括组件和API：<code>import &#123; View, Text, Image, navigateTo &#125; from 'remax/wechat';</code></p>
</li>
<li>
<p>Remax/one 是可以兼容所有小程序平台的组件库，目前仅支持少量组件跨端，如 <code><Button> <Input> <View> <Text></code>等</p>
</li>
<li>
<p>Remax 对小程序 API 做了简单的 Promise 封装，所有 API 通过平台对应的文件导出。</p>
</li>
<li>
<p>Remax使用小程序的API也需要遵守一定的规范：</p>
<ul>
<li>1、首字母大写与驼峰式命名，如小程序中的 <code><open-data></code> 需要改为 <code><OpenData></code></li>
<li>2、<code><Block>组件不可用</code>，但Taro支持，原因未知。</li>
</ul>
</li>
</ul>
</li>
<li><strong>Taro</strong>
<ul>
<li>开发规范：支持使用原生小程序的组件和API</li>
<li>1、通过 <code>@tarojs/components</code> 引入组件，如 <code><View></code> <code><Text></code> <code><OpenData></code> 等</li>
<li>2、通过 <code>@tarojs/taro</code> 引入API,如 <code>navigateTo</code>, <code>canIUse</code> 等</li>
<li>3、首字母大写与驼峰式命名</li>
<li>4、组件的事件传递都要以 <code>on</code> 开头：在微信小程序中 <code>bind</code> 开头这样的用法，都需要转成以 <code>on</code> 开头的形式，比如 <code>bindInput</code> 要写成 <code>onInput</code>，这个用起来会有点烦，不如remax来的直接...</li>
</ul>
</li>
</ul>
<h3 data-id="heading-5">3、插件支持（less）：</h3>
<ul>
<li><strong>Remax</strong>
<ul>
<li>默认不支持</li>
<li>需安装插件<code>@remax/plugin-less</code>，参见<a href="https://link.juejin.cn/?target=https%3A%2F%2Fremaxjs.org%2Fguide%2Fadvanced%2Fplugin" target="_blank" rel="nofollow noopener noreferrer" title="https://remaxjs.org/guide/advanced/plugin" ref="nofollow noopener noreferrer">使用插件</a></li>
</ul>
</li>
<li><strong>Taro</strong>
<ul>
<li>默认支持</li>
</ul>
</li>
</ul>
<h3 data-id="heading-6">4、第三方小程序组件库支持</h3>
<ul>
<li><a target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined">Remax</a></li>
</ul>
<p>你可以在 React 组件中直接使用小程序的自定义组件。包括支持原生 UI 组件库，如：weui, min-ali-ui等等。</p>
<ul>
<li>Taro</li>
</ul>
<p>未知</p>
<h3 data-id="heading-7">5、运行性能（虚拟列表）</h3>
<ul>
<li>Remax
<ul>
<li>第三方库 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fremax-virtual-list.vercel.app%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://remax-virtual-list.vercel.app/" ref="nofollow noopener noreferrer">remax-virutal-list</a></li>
</ul>
</li>
<li>Taro
<ul>
<li>官方库 <code>@tarojs/components/virtual-list</code> ，具体见 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fnervjs.github.io%2Ftaro%2Fdocs%2Fvirtual-list" target="_blank" rel="nofollow noopener noreferrer" title="https://nervjs.github.io/taro/docs/virtual-list" ref="nofollow noopener noreferrer">长列表渲染（虚拟列表）</a></li>
<li>然而引入后运行实例时报错了，查了下需要开启小程序开发工具的<strong>增强编译</strong>（然而并没有找到该选项，只好暂时放弃了。。。）</li>
</ul>
</li>
</ul>
<h3 data-id="heading-8">6、打包大小</h3>
<ul>
<li>Remax（459KB）
<ul>
<li>remax-vendor.js 229kb</li>
<li>base.wxml 153kb</li>
</ul>
</li>
<li>Taro（263KB）
<ul>
<li>taro.js 103kb</li>
<li>app.js 84kb</li>
<li>base.wxml 54kb</li>
</ul>
</li>
</ul>
<h3 data-id="heading-9">7、维护情况/社区</h3>
<ul>
<li>Remax 官方文档精简，相当<strong>克制</strong>，只放有用的信息</li>
<li>Taro 官方文档和社区内容丰富</li>
<li>由于两者均支持原生小程序的混合开发，因此都可复用微信小程序的社区</li>
</ul>
<h2 data-id="heading-10">三、综合评价</h2>
<blockquote>
<p>reamx 小而精 vs taro 大而杂</p>
</blockquote>
<p><strong>Remax小而精</strong>：</p>
<ul>
<li>官方文档精简，相当<strong>克制</strong>，只放有用的信息</li>
<li>项目依赖少，初始项目仅2个依赖包，创建时的打印信息精简，速度快，体验好。同时也提供了可扩展的能力，比如less插件的支持</li>
<li>充分复用微信小程序组件和api，引入 <code>remax/wechat</code> 即可，仅做promise化。另外，兼容其他平台的部分使用了 <code>Remax One</code> ，和微信小程序解耦，对于只需开发微信小程序的用户来说，简单高效</li>
</ul>
<p><strong>Taro大而杂</strong>：</p>
<ul>
<li>官方文档和社区内容丰富，还有自己的组件库TaroUI，看起来是搞大事的！</li>
<li>初始项目即支持10几个平台的跨端打包命令，虽然我只想开发一个微信小程序而已~</li>
<li><code>@tarojs/component</code> , <code>@tarojs/taro</code> 分别维护跨平台的组件和API，尽管如此，我只是想开发一个微信小程序而已~</li>
<li>性能和打包这块，很明显有花精力做优化，打包后的小程序包很小，而且提供了 VirtualList 的组件库支持，很棒了~</li>
</ul>
<blockquote>
<p>Remax 思路清晰，未来可期</p>
<p>Taro 摊子铺的大，未来注定会很坎坷</p>
</blockquote>
<p>经过和技术部的同事的讨论，最终确定用 Remax 来进行微信小程序的开发。
理由是团队中有人之前已经深度使用过 Remax 开发小程序，这个很重要，节省了不少趟坑的时间；
另外React+TS的开发模式也很香，期待一下下~</p>
<p>谢谢阅读，希望本文能对你有所帮助，也欢迎点赞和留言~</p></div>  
</div>
            