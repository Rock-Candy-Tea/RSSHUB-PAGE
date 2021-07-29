
---
title: '对巨石应用说不：转转商业微前端qiankun历史项目迁移升级实践'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b49c341d790a4b2b853de1a9af516bfb~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 29 Jul 2021 04:24:34 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b49c341d790a4b2b853de1a9af516bfb~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">之前和大家分享过微前端的相关知识（具体可见之前的文章：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fhttps%3A%2F%2Fmp.weixin.qq.com%2Fs%2FGiIh6bgOsL0vmghne4B2vA%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://https://mp.weixin.qq.com/s/GiIh6bgOsL0vmghne4B2vA/" ref="nofollow noopener noreferrer">闲庭信步聊前端 - 见微知著微前端</a>），本次分享qiankun在转转商业的一些实践，及问题解答</h4>
<h2 data-id="heading-1">背景</h2>
<p>商业Crm开发多年，随着开发成长为巨石应用。打包慢、升级难、排查问题链路长，同时性能差，用户体验欠缺。加上产品对系统定位思考不合理，常年的堆积功能，系统混乱。对系统的改造迫在眉睫。</p>
<h2 data-id="heading-2">解决方案</h2>
<p>通过利用qiankun微前端框架拆分商业Crm，在主应用中不断拆出功能，部署在子应用上，Crm作为主应用（系统基座），加载子应用。在迁移功能到子应用的过程中，完成代码规范和技术栈升级。</p>
<h2 data-id="heading-3">成果</h2>
<p>已经成功拆分了部分页面，多系统运行，做到了用户无感知技术升级，替换了原有页面，打包和加载速度有所提升。最重要的是没有耽误正常的业务开发。</p>
<h2 data-id="heading-4">技术细节</h2>
<p>引入qiankun框架，主站点使用原生的qiankun包，文档如下：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fqiankun.umijs.org%2Fzh" target="_blank" rel="nofollow noopener noreferrer" title="https://qiankun.umijs.org/zh" ref="nofollow noopener noreferrer">qiankun.umijs.org/zh。</a></p>
<p>子应用使用了umi框架，umi提供了乾坤插件，使用方式和原生的qiankun相比使用更简单，同时可以和原生配合使用，文档可见：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fumijs.org%2Fzh-CN%2Fplugins%2Fplugin-qiankun" target="_blank" rel="nofollow noopener noreferrer" title="https://umijs.org/zh-CN/plugins/plugin-qiankun" ref="nofollow noopener noreferrer">umijs.org/zh-CN/plugi…</a></p>
<h4 data-id="heading-5">qiankun一共有两种加载子应用的方式</h4>
<p>1.提前注册,把需要加载的子应用提前写好，包括注入容器，路由匹配规则，子应用入口</p>
<pre><code class="copyable">import &#123; registerMicroApps, start &#125; from 'qiankun';

registerMicroApps([
  &#123;
    name: 'react app', // app name registered
    entry: '//localhost:7100',
    container: '#yourContainer',
    activeRule: '/yourActiveRule',
  &#125;,
  &#123;
    name: 'vue app',
    entry: &#123; scripts: ['//localhost:7100/main.js'] &#125;,
    container: '#yourContainer2',
    activeRule: '/yourActiveRule2',
  &#125;,
]);

start();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.第二种方式loadMicroApp，动态加载子应用。这种方式的好处是可以随时随地，按照业务需求加载子应用</p>
<p>方法的属性介绍：</p>
<ul>
<li>
<p>name：区分子应用，在拥有多个子应用的时候，name非常重要，用于通信</p>
</li>
<li>
<p>entry：子应用入口，在本地环境和线上环境可能有区别，需要在区分配置。</p>
</li>
<li>
<p>container:  微应用的容器节点的选择器或者 Element 实例</p>
</li>
<li>
<p>通过initGlobalState，可以实现主应用和子应用的通信。</p>
</li>
</ul>
<p>下面介绍我们在系统中的使用细节</p>
<h5 data-id="heading-6">主站点系统配置</h5>
<p>安装</p>
<pre><code class="copyable">"qiankun": "2.4.1",
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将所有需要迁移的路由更改指向，指到专属中转页面，在转转商业Crm中的是</p>
<pre><code class="copyable">component: () => import('@views/Child')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在Child.jsx中部署乾坤的加载逻辑</p>
<pre><code class="copyable">import &#123; loadMicroApp, initGlobalState &#125; from 'qiankun';
that.microApp = loadMicroApp(
  &#123;
    name: 'crmtest',
    entry: 'https://crm.xxxxxxx.com/childfirst',
    container: this.containerRef.current,
    props: &#123; authList: this.props.authList &#125;
  &#125;,
  &#123;
    getPublicPath: (v) => &#123;
      return '//s1.xxxxxxx.com/biz/bizcrmweb_child_first/static/js/';
    &#125;
  &#125;
);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>商业Crm采用的方式是loadMicroApp，这样的好处是非常灵活，加载哪个微应用可以动态配置，可以随时替换。</p>
<p><strong>子应用系统配置</strong></p>
<p>子应用使用了umi，所以直接使用</p>
<pre><code class="copyable">"@umijs/plugin-qiankun": "2.22.0",
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是umi提供的qiankun插件，使用相比原生的qiankun要更简单。
安装插件以后，在umi指定的config文件夹下面的config.js 开启插件：</p>
<pre><code class="copyable">qiankun: &#123;
    slave: &#123;&#125;,
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在入口文件（通常是app.js）上声明生命周期方法，便于主应用调用。注意：不暴露生命周期会导致系统报错。</p>
<pre><code class="copyable">export const qiankun = &#123;
  // 应用加载之前
  async bootstrap(props) &#123;
    console.log('app1 bootstrap', props)
  &#125;,
  // 应用 render 之前触发
  async mount(props) &#123;
    console.log('app1 mount', props);
    props.onGlobalStateChange((state, prev) => &#123; // state: 变更后的状态; prev 变更前的状态
      console.log(state, prev, '子应用收到信息')
    &#125;)
    // props.setGlobalState(state);
  &#125;,
  // 应用卸载之后触发
  async unmount(props) &#123;
    console.log('app1 unmount', props)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置结束后，启动多个项目，将子应用指到主应用规定的域名地址上，就可以开始调试了。</p>
<h2 data-id="heading-7">排坑答疑阶段</h2>
<p><strong>1.子应用还需要有路由配置吗？如何跳转？</strong></p>
<p>子应用需要有完整的路由配置，主应用将所有的子应用路由都指到了同一个页面（crm是指到了前面提到的child.jsx）,并不区分页面，但是路由的是变化的，</p>
<p>如下所示：</p>
<pre><code class="copyable">  [&#123;
    path: 'child',
    component: () => import('@views/Child'),
  &#125;, &#123;
    path: 'tools/paper',
    component: () => import('@views/Child'),
  &#125;, &#123;
    path: 'finance/saledetail',
    component: () => import('@views/Child')
  &#125;]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时子应用的路由系统会启用，根据当前的路由加载不一样的页面进来。</p>
<p><strong>2.权限系统是如何运行的？</strong></p>
<p>在crm目前的方案中，权限系统是从主应用中注入到子应用中的，每次切换路由，主应用先去加载权限，再加载子应用，保证子应用的权限及时更新。</p>
<p>如下：通过props注入进系统</p>
<pre><code class="copyable">import &#123; loadMicroApp, initGlobalState &#125; from 'qiankun';
that.microApp = loadMicroApp(
  &#123;
    name: 'crmtest',
    entry: 'https://crm.xxxxxxx.com/childfirst',
    container: this.containerRef.current,
    props: &#123; authList: this.props.authList &#125;
  &#125;,
  &#123;
    getPublicPath: (v) => &#123;
      return '//s1.xxxxxxx.com/biz/bizcrmweb_child_first/static/js/';
    &#125;
  &#125;
);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.<strong>如何保证样式隔离？</strong></p>
<p>样式隔离是微前端开发中非常重要的问题。</p>
<p>Qiankun在子应用切换的过程中，会自动注销掉上一个应用的样式，这样可以避免微应用之间的干扰。</p>
<p>对于父应用和子应用之间的样式干扰，要分情况对待。</p>
<p>如果是框架的样式干扰，例如商业Crm有技术栈改进的需求（antd3升级到antd4），可以通过给框架样式加前缀，利用webpack处理，自动转换。</p>
<p>对于全局自定义样式有两种处理方法，一种是跟随主应用，子应用就不再配置特别的全局样式。</p>
<p>二是加应用前缀，以及CSS module，也可以解决问题。</p>
<p><strong>4.为什么不开启 scoped css 功能解决样式隔离问题？</strong></p>
<p>对于Vue框架的系统，开启 scoped css 是一个比较省事的解决方案，但是由于React使用合成事件，开启 scoped css 会在页面中开启一个shaow dom容器，这个容器会导致冒泡到document上的事件无法触发，所以不能使用。</p>
<p>不过React官方已经意识到了这个问题，新版本不再全部冒泡的document上。</p>
<p><strong>5.测试环境和线上环境的静态资源配置?</strong></p>
<p>如果公司的静态资源没有部署在系统域名下，可以通过入口处的补充属性getPublicPath指定</p>
<pre><code class="copyable">  &#123;
    getPublicPath: (v) => &#123;
      return '//s1.xxxxxxx.com/static/js/'; // 静态资源链接
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>6.为什么主应用访问子应用资源会提示跨域？</strong></p>
<p>这个问题官方有过回答</p>
<p>由于 qiankun 是通过 fetch 去获取微应用的引入的静态资源的，所以必须要求这些静态资源支持跨域。</p>
<p>如果是自己的脚本，可以通过开发服务端跨域来支持。如果是三方脚本且无法为其添加跨域头，可以将脚本拖到本地，由自己的服务器 serve 来支持跨域。</p>
<p><strong>7.使用umi的qiankun组件为什么会抛出访问不安全的问题？</strong></p>
<p>问题如图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b49c341d790a4b2b853de1a9af516bfb~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果是在https环境下访问http的资源，就会被umi抛出这个问题。这个问题多半出现在
开发阶段，线上部署在同域名下就不会有问题。</p>
<p>解决办法是在node_modules搜索这个错误拦截，删除这段安全判断代码。</p>
<p>或者将两个站点都改成http访问。</p>
<p><strong>8.umi的@umijs/plugin-locale没有提供自定义前缀入参，该如何添加样式前缀？</strong></p>
<p>可以把umi的@umijs/plugin-locale组件拷贝出来，自己添加一个前缀属性，然后当作自定义插件使用。</p>
<h2 data-id="heading-8">结语</h2>
<p>微前端的概念已经提出来很久了，但是微前端的需要解决的问题还有很多，并不是所有的项目都适合微前端方案。本文分享了微前端的一种实践思路，以及各种具体问题的处理，希望对大家有所帮助。</p>
<p>另外，除了目前比较受欢迎的qiankun以外，webpack5推出的模块联邦也是非常不错的方案，大家也可以尝试一下。</p></div>  
</div>
            