
---
title: '【得物技术】微前端，大世界-qiankun源码研读'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a55726d3a7c94513bd15114dfa2f69ab~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 30 Apr 2021 02:39:41 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a55726d3a7c94513bd15114dfa2f69ab~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>微前端，关于他的好和应用场景，很多师兄们也都介绍过了，那么我们使用的微前端方案qiankun是如何去做到应用的“微前端”的呢？</p>
<h1 data-id="heading-0">几个特性</h1>
<p>说到前端微服务，肯定不能不提他的<strong>几个特性</strong>。</p>
<ul>
<li>子应用并行</li>
<li>父子应用通信</li>
<li>预加载
<ul>
<li>空闲时预加载子应用的资源</li>
</ul>
</li>
<li>公共依赖的加载</li>
<li>按需加载</li>
<li>JS沙箱</li>
<li>CSS隔离</li>
</ul>
<p>做到以上的这几点，那么我们子应用就能多重组合，互不影响，面对大型项目的聚合，也不用担心项目汇总后的维护、打包、上线的问题。</p>
<p>这篇分享，就会简单的读一读qiankun 的源码，从大概流程上，了解他的实现原理和技术方案。</p>
<h1 data-id="heading-1">我们的应用怎么配置？-加入微前端Arya的怀抱吧</h1>
<p>Arya- 公司的前端平台微服务基座</p>
<p>Arya接入了权限平台的路由菜单和权限，可以动态挑选具有微服务能力的子应用的指定页面组合成一个新的平台，方便各个系统权限的下发和功能的汇聚。</p>
<h1 data-id="heading-2">创建流程</h1>
<h2 data-id="heading-3">初始化全局配置 - start(opts)</h2>
<p>/src/apis.ts</p>
<pre><code class="copyable">export function start(opts: FrameworkConfiguration = &#123;&#125;) &#123;
  // 默认值设置
  frameworkConfiguration = &#123; prefetch: true, singular: true, sandbox: true, ...opts &#125;;
  const &#123; prefetch, sandbox, singular, urlRerouteOnly, ...importEntryOpts &#125; = frameworkConfiguration;

  // 检查 prefetch 属性，如果需要预加载，则添加全局事件 single-spa:first-mount 监听，在第一个子应用挂载后预加载其他子应用资源，优化后续其他子应用的加载速度。
  if (prefetch) &#123;
    doPrefetchStrategy(microApps, prefetch, importEntryOpts);
  &#125;
// 参数设置是否启用沙箱运行环境，隔离
  if (sandbox) &#123;
    if (!window.Proxy) &#123;
      console.warn('[qiankun] Miss window.Proxy, proxySandbox will degenerate into snapshotSandbox');
      // 快照沙箱不支持非 singular 模式
      if (!singular) &#123;
        console.error('[qiankun] singular is forced to be true when sandbox enable but proxySandbox unavailable');
        frameworkConfiguration.singular = true;
      &#125;
    &#125;
  &#125;
// 启动主应用-  single-spa
  startSingleSpa(&#123; urlRerouteOnly &#125;);

  frameworkStartedDefer.resolve();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>start 函数负责初始化一些全局设置，然后启动应用。</li>
<li>这些初始化的配置参数有一部分将在 registerMicroApps 注册子应用的回调函数中使用。</li>
</ul>
<h2 data-id="heading-4">registerMicroApps(apps, lifeCycles?) - 注册子应用</h2>
<p>/src/apis.ts</p>
<pre><code class="copyable">export function registerMicroApps<T extends object = &#123;&#125;>(
  apps: Array<RegistrableApp<T>>,
  lifeCycles?: FrameworkLifeCycles<T>,
) &#123;
  // 防止重复注册子应用
  const unregisteredApps = apps.filter(app => !microApps.some(registeredApp => registeredApp.name === app.name));

  microApps = [...microApps, ...unregisteredApps];
  unregisteredApps.forEach(app => &#123;
    const &#123; name, activeRule, loader = noop, props, ...appConfig &#125; = app;
// 注册子应用
    registerApplication(&#123;
      name,
      app: async () => &#123;
        loader(true);
        await frameworkStartedDefer.promise;

        const &#123; mount, ...otherMicroAppConfigs &#125; = await loadApp(
          &#123; name, props, ...appConfig &#125;,
          frameworkConfiguration,
          lifeCycles,
        );

        return &#123;
          mount: [async () => loader(true), ...toArray(mount), async () => loader(false)],
          ...otherMicroAppConfigs,
        &#125;;
      &#125;,
      activeWhen: activeRule,
      customProps: props,
    &#125;);
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>13行， 调用single-spa 的 registerApplication 方法注册子应用。
<ul>
<li>传参：name、回调函数、activeRule 子应用激活的规则、props，主应用需要传给子应用的数据。
<ul>
<li>在符合 activeRule 激活规则时将会激活子应用，执行回调函数，返回生命周期钩子函数。</li>
</ul>
</li>
</ul>
</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a55726d3a7c94513bd15114dfa2f69ab~tplv-k3u1fbpfcp-watermark.image" alt="image - 2021-04-30T161910.059.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">获取子应用资源 - import-html-entry</h2>
<p>src/loader.ts</p>
<pre><code class="copyable">// get the entry html content and script executor
  const &#123; template, execScripts, assetPublicPath &#125; = await importEntry(entry, importEntryOpts);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用 import-html-entry 拉取子应用的静态资源。</li>
<li>调用之后返回的对象如下：</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/377086ceb3a9414d810455afe133cd16~tplv-k3u1fbpfcp-watermark.image" alt="image - 2021-04-30T162025.198.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9e89a91d0d943198b12fffea9218b34~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-04-30 下午4.21.14.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>拉取代码如下</li>
<li>GitHub地址：<a href="https://github.com/kuitos/import-html-entry#readme" target="_blank" rel="nofollow noopener noreferrer">github.com/kuitos/impo…</a>
<ul>
<li>如果能拉取静态资源，是否可以做简易的爬虫服务每日爬取页面执行资源是否加载正确？</li>
</ul>
</li>
</ul>
<pre><code class="copyable">export function importEntry(entry, opts = &#123;&#125;) &#123;
// ...

// html entry
if (typeof entry === 'string') &#123;
return importHTML(entry, &#123; fetch, getPublicPath, getTemplate &#125;);
&#125;

// config entry
if (Array.isArray(entry.scripts) || Array.isArray(entry.styles)) &#123;

const &#123; scripts = [], styles = [], html = '' &#125; = entry;
const setStylePlaceholder2HTML = tpl => styles.reduceRight((html, styleSrc) => `$&#123; genLinkReplaceSymbol(styleSrc) &#125;$&#123; html &#125;`, tpl);
const setScriptPlaceholder2HTML = tpl => scripts.reduce((html, scriptSrc) => `$&#123; html &#125;$&#123; genScriptReplaceSymbol(scriptSrc) &#125;`, tpl);

return getEmbedHTML(getTemplate(setScriptPlaceholder2HTML(setStylePlaceholder2HTML(html))), styles, &#123; fetch &#125;).then(embedHTML => (&#123;
// 这里处理同 importHTML , 省略
&#125;,
&#125;));

&#125; else &#123;
throw new SyntaxError('entry scripts or styles should be array!');
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">主应用挂载子应用 HTML 模板</h2>
<p>src/loader.ts</p>
<pre><code class="copyable">async () => &#123;
  if ((await validateSingularMode(singular, app)) && prevAppUnmountedDeferred) &#123;
    return prevAppUnmountedDeferred.promise;
  &#125;
  return undefined;
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>单实例进行检测。在单实例模式下，新的子应用挂载行为会在旧的子应用卸载之后才开始。
<ul>
<li>在旧的子应用卸载之后 -- 单例模式下的隔离方案。</li>
</ul>
</li>
</ul>
<pre><code class="copyable">
  const render = getRender(appName, appContent, container, legacyRender);

  // 第一次加载设置应用可见区域 dom 结构
  // 确保每次应用加载前容器 dom 结构已经设置完毕
  render(&#123; element, loading: true &#125;, 'loading');
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>render 函数内中将拉取的资源挂载到指定容器内的节点。</li>
</ul>
<pre><code class="copyable">const containerElement = document.createElement('div');
containerElement.innerHTML = appContent;
// appContent always wrapped with a singular div
const appElement = containerElement.firstChild as HTMLElement;

const containerElement = typeof container === 'string' ? document.querySelector(container) : container;

if (element) &#123;
  rawAppendChild.call(containerElement, element);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个阶段，主应用已经将子应用基础的 HTML 结构挂载在了主应用的某个容器内，接下来还需要执行子应用对应的 mount 方法（如 Vue.$mount）对子应用状态进行挂载。</p>
<p>此时页面还可以根据 loading 参数开启一个类似加载的效果，直至子应用全部内容加载完成。</p>
<h2 data-id="heading-7">沙箱运行环境</h2>
<p>src/loader.ts</p>
<pre><code class="copyable">let global = window;
  let mountSandbox = () => Promise.resolve();
  let unmountSandbox = () => Promise.resolve();
  if (sandbox) &#123;
    const sandboxInstance = createSandbox(
      appName,
      containerGetter,
      Boolean(singular),
      enableScopedCSS,
      excludeAssetFilter,
    );
    // 用沙箱的代理对象作为接下来使用的全局对象
    global = sandboxInstance.proxy as typeof window;
    mountSandbox = sandboxInstance.mount;
    unmountSandbox = sandboxInstance.unmount;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是沙箱核心判断逻辑，如果关闭了 sandbox  选项，那么所有子应用的沙箱环境都是 window，就很容易对全局状态产生污染。</p>
<h3 data-id="heading-8">生成应用运行时沙箱</h3>
<p>src/sandbox/index.ts</p>
<ul>
<li>app 环境沙箱
<ul>
<li>app 环境沙箱是指应用初始化过之后，应用会在什么样的上下文环境运行。每个应用的环境沙箱只会初始化一次，因为子应用只会触发一次 bootstrap 。</li>
<li>子应用在切换时，实际上切换的是 app 环境沙箱。</li>
</ul>
</li>
<li>render 沙箱
<ul>
<li>子应用在 app mount 开始前生成好的的沙箱。每次子应用切换过后，render 沙箱都会重现初始化。</li>
</ul>
</li>
</ul>
<p>这么设计的目的是为了保证每个子应用切换回来之后，还能运行在应用 bootstrap 之后的环境下。</p>
<pre><code class="copyable">  let sandbox: SandBox;
  if (window.Proxy) &#123;
    sandbox = singular ? new LegacySandbox(appName) : new ProxySandbox(appName);
  &#125; else &#123;
    sandbox = new SnapshotSandbox(appName);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>SandBox 内部的沙箱主要是通过是否支持 window.Proxy 分为 LegacySandbox 和 SnapshotSandbox 两种。</li>
</ul>
<h3 data-id="heading-9">LegacySandbox-单实例沙箱</h3>
<p>src/sandbox/legacy/sandbox.ts</p>
<pre><code class="copyable">const proxy = new Proxy(fakeWindow, &#123;
      set(_: Window, p: PropertyKey, value: any): boolean &#123;
        if (self.sandboxRunning) &#123;
          if (!rawWindow.hasOwnProperty(p)) &#123;
            addedPropsMapInSandbox.set(p, value);
          &#125; else if (!modifiedPropsOriginalValueMapInSandbox.has(p)) &#123;
            // 如果当前 window 对象存在该属性，且 record map 中未记录过，则记录该属性初始值
            const originalValue = (rawWindow as any)[p];
            modifiedPropsOriginalValueMapInSandbox.set(p, originalValue);
          &#125;

          currentUpdatedPropsValueMap.set(p, value);
          // 必须重新设置 window 对象保证下次 get 时能拿到已更新的数据
          (rawWindow as any)[p] = value;

          return true;
        &#125;

        if (process.env.NODE_ENV === 'development') &#123;
          console.warn(`[qiankun] Set window.$&#123;p.toString()&#125; while sandbox destroyed or inactive in $&#123;name&#125;!`);
        &#125;
        // 在 strict-mode 下，Proxy 的 handler.set 返回 false 会抛出 TypeError，在沙箱卸载的情况下应该忽略错误
        return true;
      &#125;,

      get(_: Window, p: PropertyKey): any &#123;
        if (p === 'top' || p === 'parent' || p === 'window' || p === 'self') &#123;
          return proxy;
        &#125;

        const value = (rawWindow as any)[p];
        return getTargetValue(rawWindow, value);
      &#125;,

      has(_: Window, p: string | number | symbol): boolean &#123;
        return p in rawWindow;
      &#125;,
    &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>以简单理解为子应用的 window 全局对象，子应用对全局属性的操作就是对该 proxy 对象属性的操作。</li>
</ul>
<pre><code class="copyable">// 子应用脚本文件的执行过程：
eval(
  // 这里将 proxy 作为 window 参数传入
  // 子应用的全局对象就是该子应用沙箱的 proxy 对象
  (function(window) &#123;
    /* 子应用脚本文件内容 */
  &#125;)(proxy)
);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>当调用 set 向子应用 proxy/window 对象设置属性时，所有的属性设置和更新都会先记录在 addedPropsMapInSandbox 或 modifiedPropsOriginalValueMapInSandbox 中，然后统一记录到 currentUpdatedPropsValueMap 中。</li>
<li>修改全局 window 的属性，完成值的设置。</li>
<li>当调用 get 从子应用 proxy/window 对象取值时，会直接从 window 对象中取值。对于非构造函数的取值将会对 this 指针绑定到 window 对象后，再返回函数。</li>
</ul>
<p>LegacySandbox  的沙箱隔离是通过激活沙箱时还原子应用状态，卸载时还原主应用状态（子应用挂载前的全局状态）实现的，具体源码实现在 src/sandbox/legacy/sandbox.ts 中的 SingularProxySandbox 方法。</p>
<h3 data-id="heading-10">ProxySandbox 多实例沙箱</h3>
<p>src/sandbox/proxySandbox.ts</p>
<pre><code class="copyable"> constructor(name: string) &#123;
    this.name = name;
    this.type = SandBoxType.Proxy;
    const &#123; updatedValueSet &#125; = this;

    const self = this;
    const rawWindow = window;
    const &#123; fakeWindow, propertiesWithGetter &#125; = createFakeWindow(rawWindow);

    const descriptorTargetMap = new Map<PropertyKey, SymbolTarget>();
    const hasOwnProperty = (key: PropertyKey) => fakeWindow.hasOwnProperty(key) || rawWindow.hasOwnProperty(key);

    const proxy = new Proxy(fakeWindow, &#123;
      set(target: FakeWindow, p: PropertyKey, value: any): boolean &#123;
        if (self.sandboxRunning) &#123;
          // @ts-ignore
          target[p] = value;
          updatedValueSet.add(p);

          interceptSystemJsProps(p, value);

          return true;
        &#125;

        if (process.env.NODE_ENV === 'development') &#123;
          console.warn(`[qiankun] Set window.$&#123;p.toString()&#125; while sandbox destroyed or inactive in $&#123;name&#125;!`);
        &#125;

        // 在 strict-mode 下，Proxy 的 handler.set 返回 false 会抛出 TypeError，在沙箱卸载的情况下应该忽略错误
        return true;
      &#125;,

      get(target: FakeWindow, p: PropertyKey): any &#123;
        if (p === Symbol.unscopables) return unscopables;

        // avoid who using window.window or window.self to escape the sandbox environment to touch the really window
        // see https://github.com/eligrey/FileSaver.js/blob/master/src/FileSaver.js#L13
        if (p === 'window' || p === 'self') &#123;
          return proxy;
        &#125;

        if (
          p === 'top' ||
          p === 'parent' ||
          (process.env.NODE_ENV === 'test' && (p === 'mockTop' || p === 'mockSafariTop'))
        ) &#123;
          // if your master app in an iframe context, allow these props escape the sandbox
          if (rawWindow === rawWindow.parent) &#123;
            return proxy;
          &#125;
          return (rawWindow as any)[p];
        &#125;

        // proxy.hasOwnProperty would invoke getter firstly, then its value represented as rawWindow.hasOwnProperty
        if (p === 'hasOwnProperty') &#123;
          return hasOwnProperty;
        &#125;

        // mark the symbol to document while accessing as document.createElement could know is invoked by which sandbox for dynamic append patcher
        if (p === 'document') &#123;
          document[attachDocProxySymbol] = proxy;
          // remove the mark in next tick, thus we can identify whether it in micro app or not
          // this approach is just a workaround, it could not cover all the complex scenarios, such as the micro app runs in the same task context with master in som case
          // fixme if you have any other good ideas
          nextTick(() => delete document[attachDocProxySymbol]);
          return document;
        &#125;

        // eslint-disable-next-line no-bitwise
        const value = propertiesWithGetter.has(p) ? (rawWindow as any)[p] : (target as any)[p] || (rawWindow as any)[p];
        return getTargetValue(rawWindow, value);
      &#125;,

      // trap in operator
      // see https://github.com/styled-components/styled-components/blob/master/packages/styled-components/src/constants.js#L12
      has(target: FakeWindow, p: string | number | symbol): boolean &#123;
        return p in unscopables || p in target || p in rawWindow;
      &#125;,

      getOwnPropertyDescriptor(target: FakeWindow, p: string | number | symbol): PropertyDescriptor | undefined &#123;
        /*
         as the descriptor of top/self/window/mockTop in raw window are configurable but not in proxy target, we need to get it from target to avoid TypeError
         see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy/handler/getOwnPropertyDescriptor
         > A property cannot be reported as non-configurable, if it does not exists as an own property of the target object or if it exists as a configurable own property of the target object.
         */
        if (target.hasOwnProperty(p)) &#123;
          const descriptor = Object.getOwnPropertyDescriptor(target, p);
          descriptorTargetMap.set(p, 'target');
          return descriptor;
        &#125;

        if (rawWindow.hasOwnProperty(p)) &#123;
          const descriptor = Object.getOwnPropertyDescriptor(rawWindow, p);
          descriptorTargetMap.set(p, 'rawWindow');
          return descriptor;
        &#125;

        return undefined;
      &#125;,

      // trap to support iterator with sandbox
      ownKeys(target: FakeWindow): PropertyKey[] &#123;
        return uniq(Reflect.ownKeys(rawWindow).concat(Reflect.ownKeys(target)));
      &#125;,

      defineProperty(target: Window, p: PropertyKey, attributes: PropertyDescriptor): boolean &#123;
        const from = descriptorTargetMap.get(p);
        /*
         Descriptor must be defined to native window while it comes from native window via Object.getOwnPropertyDescriptor(window, p),
         otherwise it would cause a TypeError with illegal invocation.
         */
        switch (from) &#123;
          case 'rawWindow':
            return Reflect.defineProperty(rawWindow, p, attributes);
          default:
            return Reflect.defineProperty(target, p, attributes);
        &#125;
      &#125;,

      deleteProperty(target: FakeWindow, p: string | number | symbol): boolean &#123;
        if (target.hasOwnProperty(p)) &#123;
          // @ts-ignore
          delete target[p];
          updatedValueSet.delete(p);

          return true;
        &#125;

        return true;
      &#125;,
    &#125;);

    this.proxy = proxy;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>当调用 set 向子应用 proxy/window 对象设置属性时，所有的属性设置和更新都会命中 updatedValueSet，存储在 updatedValueSet (18行 updatedValueSet.add(p) )集合中，从而避免对 window 对象产生影响。</li>
<li>当调用 get 从子应用 proxy/window 对象取值时，会优先从子应用的沙箱状态池 updatedValueSet 中取值，如果没有命中才从主应用的 window 对象中取值。对于非构造函数的取值将会对 this 指针绑定到 window 对象后，再返回函数。</li>
<li>如此一来，ProxySandbox 沙箱应用之间的隔离就完成了，所有子应用对 proxy/window 对象值的存取都受到了控制。设置值只会作用在沙箱内部的 updatedValueSet 集合上，取值也是优先取子应用独立状态池（updateValueMap）中的值，没有找到的话，再从 proxy/window 对象中取值。</li>
<li>相比较而言，ProxySandbox 是最完备的沙箱模式，完全隔离了对 window 对象的操作，也解决了快照模式中子应用运行期间仍然会对 window 造成污染的问题。</li>
</ul>
<h3 data-id="heading-11">SnapshotSandbox</h3>
<p>src/sandbox/snapshotSandbox.ts</p>
<p>不支持 window.Proxy 属性时，将会使用 SnapshotSandbox 沙箱，这个沙箱主要有以下几个步骤：</p>
<ol>
<li>激活时给Window打个快照。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5ffa73129224817930ce0eb1eb5f0a8~tplv-k3u1fbpfcp-watermark.image" alt="image - 2021-04-30T163731.313.png" loading="lazy" referrerpolicy="no-referrer">
2. 把window快照内的属性全部绑定在 modifyPropsMap 上，用于后续恢复变更。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c76055e2a1b4a1da3a5f2a503381000~tplv-k3u1fbpfcp-watermark.image" alt="image - 2021-04-30T163815.385.png" loading="lazy" referrerpolicy="no-referrer">
3. 记录变更，卸载时如果不一样，就恢复改变之前的window属性值。
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08adb6931f8f4c8aa05d81f31491db42~tplv-k3u1fbpfcp-watermark.image" alt="image - 2021-04-30T163837.704.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>SnapshotSandbox 沙箱就是利用快照实现了对 window 对象状态隔离的管理。相比较 ProxySandbox 而言，在子应用激活期间，SnapshotSandbox 将会对 window 对象造成污染，属于一个对不支持 Proxy 属性的浏览器的向下兼容方案。</p>
<h3 data-id="heading-12">动态添加样式表文件劫持</h3>
<p>src/sandbox/patchers/dynamicAppend.ts</p>
<ul>
<li>避免主应用、子应用样式污染。
<ul>
<li>主应用编译是classID加上hash码，避免主应用影响子应用的样式。</li>
</ul>
</li>
<li>子-子之间避免。
<ul>
<li>当前子应用处于激活状态，那么动态 style 样式表就会被添加到子应用容器内，在子应用卸载时样式表也可以和子应用一起被卸载，从而避免样式污染。</li>
</ul>
</li>
</ul>
<h3 data-id="heading-13">子应用的动态脚本执行</h3>
<p>对动态添加的脚本进行劫持的主要目的就是为了将动态脚本运行时的 window 对象替换成 proxy 代理对象，使子应用动态添加的脚本文件的运行上下文也替换成子应用自身。</p>
<h3 data-id="heading-14">卸载沙箱 - unmountSandbox</h3>
<p>src/loader.ts</p>
<pre><code class="copyable">unmountSandbox = sandboxInstance.unmount;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>src/sandbox/index.ts</p>
<pre><code class="copyable"> /**
     * 恢复 global 状态，使其能回到应用加载之前的状态
     */
    async unmount() &#123;
     // 循环执行卸载函数-移除dom/样式/脚本等；修改状态
      sideEffectsRebuilders = [...bootstrappingFreers, ...mountingFreers].map(free => free());
      sandbox.inactive();
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-15">通信</h2>
<p>src/globalState.ts</p>
<p>qiankun内部提供了 initGlobalState 方法用于注册 MicroAppStateActions 实例用于通信，该实例有三个方法，分别是：</p>
<ul>
<li>setGlobalState：设置 globalState - 设置新的值时，内部将执行 浅检查，如果检查到 globalState 发生改变则触发通知，通知到所有的 观察者 函数。</li>
<li>onGlobalStateChange：注册 观察者 函数 - 响应 globalState 变化，在 globalState 发生改变时触发该 观察者 函数。</li>
<li>offGlobalStateChange：取消 观察者 函数 - 该实例不再响应 globalState 变化。</li>
</ul>
<h1 data-id="heading-16">公共资源的提取</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22af077e7230480e8fe1cc0c79cc3d28~tplv-k3u1fbpfcp-watermark.image" alt="image - 2021-04-30T164239.214.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-17">回顾</h1>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1932d56a366540acae7114a20dcf1610~tplv-k3u1fbpfcp-watermark.image" alt="image - 2021-04-30T164256.474.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>文｜鬼灭
关注得物技术，携手走向技术的云端</p></div>  
</div>
            